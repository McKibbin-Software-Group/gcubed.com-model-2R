from pathlib import Path
import csv
import re
import sys
from string import Template
from typing import Iterable

import yaml

###############################################################################
# EXPERIMENT CONFIGURATION
#
# Edit this YAML block to change the experiment. The setup code below should
# usually not need editing. Key sections are:
# - experiment: file names, report years, and overwrite behavior
# - baseline: saved or created solved model used by the run script
# - layers: scenario shocks, years, prefixes, selectors, and values
# - chartpack: report window, derivations, chart prefixes, and selectors
###############################################################################

EXPERIMENT_CONFIGURATION_YAML: str = """
experiment:
  model_configuration_file_name: configuration.csv
  scenario_name: An increase in the USA inflation target
  run_script_file_name: run_experiment.py
  readme_file_name: README.md
  documentation_file_name: documentation.md
  design_file_name: design.csv
  chartpack_file_name: chartpack.csv
  report_template_file_name: chart-template.html
  overwrite_generated_files: true
baseline:
  results_folder_name: baseline
  solved_model_file_name: solved_model.joblib
  ask_to_solve_model_if_missing: true
  solve_model_if_missing: false
layers:
  - name: USA inflation target increase
    data_file_name: adjustments.csv
    event_year: 2024
    description: The USA inflation target (INFX) is permanently increased by 1 percentage point.
    shocks:
      - variable_prefix: INFX
        selectors:
          regions: [USA]
        value_path:
          type: permanent_constant
          start_year: 2024
          value: 1
chartpack:
  title: Inflation target increase
  first_result_year:
  last_result_year: 2040
  derivations:
    - GDPRGROWTH
  charts:
    - variable_prefix: INFX
      selectors:
        regions: all
    - variable_prefix: INFL
      selectors:
        regions: all
    - variable_prefix: GDPRGROWTH
      selectors:
        regions: all
    - variable_prefix: GDPR
      selectors:
        regions: all
    - variable_prefix: INTN
      selectors:
        regions: all
    - variable_prefix: INTR
      selectors:
        regions: all
    - variable_prefix: EXCH
      selectors:
        regions: all
    - variable_prefix: NEER
      selectors:
        regions: all
run:
  show_final_results: true
"""

###############################################################################
# IMPLEMENTATION
# Ordinary experiment changes should be made in the YAML block above.
###############################################################################

RUN_SCRIPT_TEMPLATE: str = """from pathlib import Path
import logging
import pickle
import sys

from joblib import dump, load

# Resolve paths from this script's location in the simulation folder.
experiment_directory_path: Path = Path(__file__).resolve().parent
simulations_directory_path: Path = experiment_directory_path.parent
model_directory_path: Path = simulations_directory_path.parent
model_python_directory_path: Path = model_directory_path / \"python\"
root_results_directory_path: Path = model_directory_path.parent.parent / \"results\"

if str(model_python_directory_path) not in sys.path:
    sys.path.insert(0, str(model_python_directory_path))

from gcubed import configure_logging
from gcubed.linearisation.solved_model import SolvedModel
from gcubed.model import Model
from gcubed.model_configuration import ModelConfiguration
from gcubed.projections.baseline_projections import BaselineProjections
from gcubed.derivations import create_derivations
from gcubed.reporting import generate_all_simulation_results
from gcubed.runners.simulation_runner import SimulationRunner

###############################################################################
# RUN CONFIGURATION
#
# Edit these settings to change which generated experiment files are used,
# which solved model is loaded or created, and whether reports are displayed.
###############################################################################

experiment_directory_name: str = experiment_directory_path.name
model_configuration_file_name: str = "$model_configuration_file_name"
experiment_design_file_name: str = "$design_file_name"
chartpack_file_name: str = "$chartpack_file_name"
documentation_file_name: str = "$documentation_file_name"
report_template_file_name: str = "$report_template_file_name"
baseline_results_folder_name: str = "$baseline_results_folder_name"
solved_model_file_name: str = "$solved_model_file_name"
ask_to_solve_model_if_missing: bool = $ask_to_solve_model_if_missing
solve_model_if_missing: bool = $solve_model_if_missing
show_final_results: bool = $show_final_results
derivation_names: list[str] = $derivation_names

###############################################################################
# IMPLEMENTATION
# Ordinary run changes should be made in the configuration block above.
###############################################################################


def load_or_create_solved_model(
    model_configuration: ModelConfiguration,
    solved_model_file: Path,
) -> SolvedModel:
    if solved_model_file.exists():
        logging.warning(f\"Loading solved model from {solved_model_file}\")
        with open(solved_model_file, \"rb\") as file:
            return load(file)

    should_solve_model: bool = solve_model_if_missing
    if (
        not should_solve_model
        and ask_to_solve_model_if_missing
        and sys.stdin.isatty()
    ):
        response = input(
            f\"Solved model not found at {solved_model_file}. \"
            \"Solve the model now and save it there? [y/N] \"
        )
        should_solve_model = response.strip().lower() in {\"y\", \"yes\"}

    if not should_solve_model:
        raise FileNotFoundError(
            f\"Solved model not found at {solved_model_file}. \"
            \"Set solve_model_if_missing=True, answer yes when prompted, \"
            \"or run the baseline first.\"
        )

    solved_model_file.parent.mkdir(parents=True, exist_ok=True)
    model: Model = Model(configuration=model_configuration)
    solved_model: SolvedModel = SolvedModel(model=model)
    with open(solved_model_file, \"wb\") as file:
        logging.info(\"Serialising the solved model\")
        dump(
            solved_model,
            file,
            compress=(\"zlib\", 0),
            protocol=pickle.HIGHEST_PROTOCOL,
        )
    return solved_model


model_configuration_file_path: Path = model_directory_path / model_configuration_file_name
assert (
    model_configuration_file_path.exists()
), f\"Model configuration file not found at {model_configuration_file_path}\"

model_configuration: ModelConfiguration = ModelConfiguration(
    configuration_file=model_configuration_file_path
)

results_folder: Path = (
    root_results_directory_path
    / model_configuration.version
    / model_configuration.build
    / experiment_directory_name
)
results_folder.mkdir(parents=True, exist_ok=True)
configure_logging(folder=results_folder)

solved_model_file: Path = (
    root_results_directory_path
    / model_configuration.version
    / model_configuration.build
    / baseline_results_folder_name
    / solved_model_file_name
)
solved_model: SolvedModel = load_or_create_solved_model(
    model_configuration=model_configuration,
    solved_model_file=solved_model_file,
)
baseline_projections: BaselineProjections = BaselineProjections(
    solved_model=solved_model,
)

derivations = create_derivations(derivation_names)

runner: SimulationRunner = SimulationRunner(
    baseline_projections=baseline_projections,
    experiment_design_file=f\"{experiment_directory_name}/{experiment_design_file_name}\",
    derivations=derivations,
)
runner.run()

generate_all_simulation_results(
    chartpack_path=experiment_directory_path / chartpack_file_name,
    documentation_path=experiment_directory_path / documentation_file_name,
    template_path=model_directory_path / "templates" / report_template_file_name,
    results_directory_path=results_folder,
    all_projections=runner.all_projections,
    derivations=derivations,
    show_final_results=show_final_results,
)
"""

DERIVED_REGION_PREFIXES: set[str] = {"GDPRGROWTH"}
REQUIRED_CONFIGURATION_SECTIONS: tuple[str, ...] = (
    "experiment",
    "baseline",
    "layers",
    "chartpack",
    "run",
)


def load_experiment_configuration() -> dict:
    configuration = yaml.safe_load(EXPERIMENT_CONFIGURATION_YAML)
    assert isinstance(
        configuration, dict
    ), "The experiment configuration YAML must parse to a mapping."
    missing_sections = [
        section
        for section in REQUIRED_CONFIGURATION_SECTIONS
        if section not in configuration
    ]
    assert not missing_sections, f"Missing YAML sections: {missing_sections}"
    return configuration


def require_prefix_only(variable_prefix: str) -> None:
    assert variable_prefix, "Each series or shock must specify a variable_prefix."
    assert "(" not in variable_prefix and ")" not in variable_prefix, (
        "Configuration must use variable name prefixes only, "
        f"not full variable names: {variable_prefix}"
    )


def selected_members(selector_value, all_members: list[str]) -> list[str]:
    if selector_value is None or selector_value == "all":
        return list(all_members)
    if isinstance(selector_value, str):
        selector_value = [selector_value]
    result = list(selector_value)
    invalid = sorted(set(result) - set(all_members))
    assert (
        not invalid
    ), f"Unknown selector members {invalid}; valid members are {all_members}"
    return result


def variable_arguments(variable_name: str) -> list[str]:
    match = re.match(r"^[^(]+(?:\((.*)\))?$", variable_name)
    if match is None or match.group(1) is None or match.group(1) == "":
        return []
    return [part.strip() for part in match.group(1).split(",")]


def variable_matches_selectors(variable_name: str, selectors: dict, sym_data) -> bool:
    args = variable_arguments(variable_name)
    regions = selected_members(selectors.get("regions"), sym_data.regions_members)
    sectors = selected_members(selectors.get("sectors"), sym_data.sectors_members)
    goods = selected_members(selectors.get("goods"), sym_data.goods_members)

    if "regions" in selectors and not any(region in args for region in regions):
        return False
    if "sectors" in selectors and not any(sector in args for sector in sectors):
        return False
    if "goods" in selectors and not any(good in args for good in goods):
        return False
    return True


def derived_region_variables(
    variable_prefix: str, selectors: dict, sym_data
) -> list[str]:
    regions = selected_members(selectors.get("regions"), sym_data.regions_members)
    return [f"{variable_prefix}({region})" for region in regions]


def resolve_variables(series_or_shock: dict, sym_data) -> list[str]:
    variable_prefix = series_or_shock["variable_prefix"]
    selectors = series_or_shock.get("selectors", {})
    require_prefix_only(variable_prefix)

    if sym_data.has_variables_with_prefix(variable_prefix):
        variables = sym_data.variables_with_prefix(variable_prefix)
        result = [
            variable
            for variable in variables
            if variable_matches_selectors(variable, selectors, sym_data)
        ]
    elif variable_prefix in DERIVED_REGION_PREFIXES:
        result = derived_region_variables(variable_prefix, selectors, sym_data)
    else:
        raise AssertionError(
            f"The model does not include variables with prefix {variable_prefix}."
        )

    assert result, f"No variables resolved for {series_or_shock}"
    return result


def output_years(start_year: int, last_projection_year: int) -> list[int]:
    assert (
        start_year <= last_projection_year
    ), f"Shock start year {start_year} is after the model's last projection year {last_projection_year}."
    return list(range(start_year, last_projection_year + 1))


def shock_values(value_path: dict, years: list[int]) -> list[float | int]:
    path_type = value_path["type"]
    if path_type == "permanent_constant":
        return [value_path["value"] for _ in years]
    if path_type == "temporary_constant":
        start_year = int(value_path["start_year"])
        end_year = int(value_path["end_year"])
        value = value_path["value"]
        return [value if start_year <= year <= end_year else 0 for year in years]
    if path_type == "explicit":
        values_by_year = {
            int(year): value for year, value in value_path["values"].items()
        }
        return [values_by_year.get(year, 0) for year in years]
    raise ValueError(f"Unsupported value_path type: {path_type}")


def design_rows(layers: list[dict]) -> list[list[object]]:
    rows: list[list[object]] = [["name", "data", "event_year", "description"]]
    for layer in layers:
        rows.append(
            [
                layer["name"],
                layer["data_file_name"],
                layer["event_year"],
                layer["description"],
            ]
        )
    return rows


def layer_rows(layer: dict, sym_data, last_projection_year: int) -> list[list[object]]:
    start_year = min(
        int(shock["value_path"].get("start_year", layer["event_year"]))
        for shock in layer["shocks"]
    )
    years = output_years(
        start_year=start_year, last_projection_year=last_projection_year
    )
    rows: list[list[object]] = [["name", *years]]
    for shock in layer["shocks"]:
        values = shock_values(value_path=shock["value_path"], years=years)
        for variable in resolve_variables(shock, sym_data):
            rows.append([variable, *values])
    return rows


def pack_attributes(chartpack_config: dict) -> str:
    attributes: list[str] = []
    first_year = chartpack_config.get("first_result_year")
    last_year = chartpack_config.get("last_result_year")
    if first_year is not None:
        attributes.append(f"start_year={first_year}")
    if last_year is not None:
        attributes.append(f"end_year={last_year}")
    return "|".join(attributes)


def chartpack_rows(chartpack_config: dict, sym_data) -> list[list[str]]:
    rows: list[list[str]] = [["type", "attributes", "variable", "label"]]
    rows.append(
        ["pack", pack_attributes(chartpack_config), "", chartpack_config["title"]]
    )

    for chart in chartpack_config["charts"]:
        rows.append(["chart", "", "", ""])
        series_definitions = chart.get("series")
        if series_definitions is None:
            series_definitions = [chart]
        for series_definition in series_definitions:
            for variable in resolve_variables(series_definition, sym_data):
                rows.append(["series", "", variable, ""])
    return rows


def write_text(path: Path, text: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.write_text(text)


def write_csv(path: Path, rows: Iterable[list[object]], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    with path.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def render_readme(
    scenario_name: str,
    setup_script_file_name: str,
    run_script_file_name: str,
    readme_file_name: str,
    documentation_file_name: str,
    design_file_name: str,
    chartpack_file_name: str,
    layer_file_names: list[str],
) -> str:
    layer_file_inventory = "".join(
        f"- `{layer_file_name}`: Contains the permanent 1 percentage point shock "
        "to the inflation target from the scenario start onward.\n"
        for layer_file_name in layer_file_names
    )
    return (
        f"# {scenario_name}\n\n"
        "This experiment permanently raises the United States inflation target by "
        "1 percentage point. The increase is applied from the scenario start "
        "and remains in place through the projection horizon.\n\n"
        "Economically, a higher inflation target changes the nominal anchor for "
        "the United States. Monetary policy can tolerate a higher rate of price "
        "growth before tightening, which affects nominal interest rates, real "
        "interest rates, exchange rates, output, and inflation dynamics relative "
        "to the baseline.\n\n"
        f"View [the detailed documentation for the experiment]({documentation_file_name}).\n\n"
        "## Files\n\n"
        f"- `{setup_script_file_name}`: Regenerates this experiment from the "
        "editable YAML configuration block.\n"
        f"- `{run_script_file_name}`: Runs the experiment using the baseline "
        "solved model and produces the report outputs.\n"
        f"- `{readme_file_name}`: Explains the experiment and lists the files in "
        "this experiment directory.\n"
        f"- `{documentation_file_name}`: Brief report-header text included in "
        "generated results reports.\n"
        f"- `{design_file_name}`: Lists the simulation layers and points to their "
        "shock data files.\n"
        f"{layer_file_inventory}"
        f"- `{chartpack_file_name}`: Defines the charts to include in the "
        "generated experiment report.\n"
    )


def render_documentation() -> str:
    return (
        "This experiment permanently raises the United States inflation target "
        "by 1 percentage point. The policy change raises the nominal inflation "
        "target used for the United States while leaving the rest of the "
        "baseline assumptions unchanged.\n\n"
        "The main economic channel is monetary policy. A higher inflation target "
        "allows higher inflation before policy needs to tighten, affecting "
        "nominal and real interest rates, exchange rates, output, and inflation "
        "relative to the baseline projection.\n"
    )


def main() -> None:
    configuration = load_experiment_configuration()
    experiment_config = configuration["experiment"]
    baseline_config = configuration["baseline"]
    run_config = configuration["run"]

    experiment_directory_path: Path = Path(__file__).resolve().parent
    simulations_directory_path: Path = experiment_directory_path.parent
    model_directory_path: Path = simulations_directory_path.parent
    model_python_directory_path: Path = model_directory_path / "python"
    model_configuration_file_path: Path = (
        model_directory_path / experiment_config["model_configuration_file_name"]
    )

    assert (
        model_configuration_file_path.exists()
    ), f"Model configuration file not found at {model_configuration_file_path}"

    if str(model_python_directory_path) not in sys.path:
        sys.path.insert(0, str(model_python_directory_path))

    from gcubed.model import Model
    from gcubed.model_configuration import ModelConfiguration

    model_configuration = ModelConfiguration(
        configuration_file=model_configuration_file_path
    )
    model = Model(configuration=model_configuration)
    sym_data = model.sym_data
    overwrite = bool(experiment_config["overwrite_generated_files"])

    write_text(
        experiment_directory_path / experiment_config["readme_file_name"],
        render_readme(
            scenario_name=experiment_config["scenario_name"],
            setup_script_file_name=Path(__file__).name,
            run_script_file_name=experiment_config["run_script_file_name"],
            readme_file_name=experiment_config["readme_file_name"],
            documentation_file_name=experiment_config["documentation_file_name"],
            design_file_name=experiment_config["design_file_name"],
            chartpack_file_name=experiment_config["chartpack_file_name"],
            layer_file_names=[
                layer["data_file_name"] for layer in configuration["layers"]
            ],
        ),
        overwrite=overwrite,
    )
    write_text(
        experiment_directory_path / experiment_config["documentation_file_name"],
        render_documentation(),
        overwrite=overwrite,
    )
    write_csv(
        experiment_directory_path / experiment_config["design_file_name"],
        design_rows(configuration["layers"]),
        overwrite=overwrite,
    )
    for layer in configuration["layers"]:
        write_csv(
            experiment_directory_path / layer["data_file_name"],
            layer_rows(
                layer=layer,
                sym_data=sym_data,
                last_projection_year=model_configuration.last_projection_year,
            ),
            overwrite=overwrite,
        )
    write_csv(
        experiment_directory_path / experiment_config["chartpack_file_name"],
        chartpack_rows(configuration["chartpack"], sym_data),
        overwrite=overwrite,
    )
    write_text(
        experiment_directory_path / experiment_config["run_script_file_name"],
        Template(RUN_SCRIPT_TEMPLATE).substitute(
            model_configuration_file_name=experiment_config[
                "model_configuration_file_name"
            ],
            design_file_name=experiment_config["design_file_name"],
            chartpack_file_name=experiment_config["chartpack_file_name"],
            documentation_file_name=experiment_config["documentation_file_name"],
            report_template_file_name=experiment_config["report_template_file_name"],
            baseline_results_folder_name=baseline_config["results_folder_name"],
            solved_model_file_name=baseline_config["solved_model_file_name"],
            ask_to_solve_model_if_missing=baseline_config[
                "ask_to_solve_model_if_missing"
            ],
            solve_model_if_missing=baseline_config["solve_model_if_missing"],
            show_final_results=run_config["show_final_results"],
            derivation_names=repr(configuration["chartpack"].get("derivations", [])),
        ),
        overwrite=overwrite,
    )


if __name__ == "__main__":
    main()
