"""Create portable fiscal contraction experiment files.

Generated scripts derive the experiment directory from their own location.
"""

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
# - experiment: file names, report years, overwrite behavior
# - baseline: saved or created solved model used by the run script
# - simulation_designs: generated design files and layer ordering
# - layers: scenario shocks, event years, prefixes, selectors, and values
# - chartpack: report window, derivations, chart prefixes, and selectors
###############################################################################

EXPERIMENT_CONFIGURATION_YAML: str = """
experiment:
  model_configuration_file_name: configuration.csv
  scenario_name: Fiscal contraction in all regions
  run_script_file_name: run_experiment.py
  readme_file_name: README.md
  documentation_file_name: documentation.md
  chartpack_file_name: chartpack.csv
  report_template_file_name: chart-template.html
  overwrite_generated_files: true
baseline:
  results_folder_name: baseline
  solved_model_file_name: solved_model.joblib
  ask_to_solve_model_if_missing: true
  solve_model_if_missing: false
simulation_designs:
  - key: fiscal_contraction
    name: Fiscal contraction in all regions
    design_file_name: design.csv
    description: Government spending excluding labor is reduced in all regions for three years.
    layer_ids:
      - fiscal_contraction_all_regions
layers:
  - id: fiscal_contraction_all_regions
    name: Fiscal contraction in all regions
    data_file_name: fiscal_contraction.csv
    event_year: 2026
    description: Temporary 10 percent of GDP cut to government spending excluding labor in all regions for 2026-2028.
    shocks:
      - variable_prefix: GOVS
        variable_type: exo
        selectors:
          regions: all
        value_path:
          type: temporary_constant
          start_year: 2026
          end_year: 2028
          value: -10
chartpack:
  title: Fiscal contraction in all regions
  first_result_year: 2025
  last_result_year: 2040
  derivations:
    - GDPRGROWTH
  charts:
    - variable_prefix: GOVS
      selectors: {regions: all}
    - variable_prefix: GCET
      selectors: {regions: all}
    - variable_prefix: GOVT
      selectors: {regions: all}
    - variable_prefix: DEFI
      selectors: {regions: all}
    - variable_prefix: DEFN
      selectors: {regions: all}
    - variable_prefix: TAXT
      selectors: {regions: all}
    - variable_prefix: GDPR
      selectors: {regions: all}
    - variable_prefix: GDPRGROWTH
      selectors: {regions: all}
    - variable_prefix: GNER
      selectors: {regions: all}
    - variable_prefix: CONP
      selectors: {regions: all}
    - variable_prefix: INVT
      selectors: {regions: all}
    - variable_prefix: INFL
      selectors: {regions: all}
    - variable_prefix: INTN
      selectors: {regions: all}
    - variable_prefix: INTR
      selectors: {regions: all}
    - variable_prefix: EXCH
      selectors: {regions: all}
    - variable_prefix: NEER
      selectors: {regions: all}
    - variable_prefix: REER
      selectors: {regions: all}
    - variable_prefix: TBAL
      selectors: {regions: all}
    - variable_prefix: LABO
      selectors: {regions: all}
    - variable_prefix: STMT
      selectors: {regions: all}
run:
  show_final_results: false
"""

###############################################################################
# IMPLEMENTATION
# Ordinary experiment changes should be made in the YAML block above.
###############################################################################

RUN_SCRIPT_TEMPLATE: str = r"""from pathlib import Path
import logging
import pickle
import sys

from joblib import dump, load

# Resolve paths from this script's location in the simulation folder.
experiment_directory_path: Path = Path(__file__).resolve().parent
simulations_directory_path: Path = experiment_directory_path.parent
model_directory_path: Path = simulations_directory_path.parent
model_python_directory_path: Path = model_directory_path / "python"
root_results_directory_path: Path = model_directory_path.parent.parent / "results"

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
        logging.warning(f"Loading solved model from {solved_model_file}")
        with open(solved_model_file, "rb") as file:
            return load(file)

    should_solve_model: bool = solve_model_if_missing
    if (
        not should_solve_model
        and ask_to_solve_model_if_missing
        and sys.stdin.isatty()
    ):
        response = input(
            f"Solved model not found at {solved_model_file}. "
            "Solve the model now and save it there? [y/N] "
        )
        should_solve_model = response.strip().lower() in {"y", "yes"}

    if not should_solve_model:
        raise FileNotFoundError(
            f"Solved model not found at {solved_model_file}. "
            "Set solve_model_if_missing=True, answer yes when prompted, "
            "or run the baseline first."
        )

    solved_model_file.parent.mkdir(parents=True, exist_ok=True)
    model: Model = Model(configuration=model_configuration)
    solved_model: SolvedModel = SolvedModel(model=model)
    with open(solved_model_file, "wb") as file:
        logging.info("Serialising the solved model")
        dump(
            solved_model,
            file,
            compress=("zlib", 0),
            protocol=pickle.HIGHEST_PROTOCOL,
        )
    return solved_model


model_configuration_file_path: Path = model_directory_path / model_configuration_file_name
assert (
    model_configuration_file_path.exists()
), f"Model configuration file not found at {model_configuration_file_path}"

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
    experiment_design_file=f"{experiment_directory_name}/{experiment_design_file_name}",
    derivations=derivations,
)
runner.run()

for index, projections in enumerate(runner.all_projections):
    projections.database_projections.to_csv(
        results_folder / f"{index} database projections.csv",
        index=True,
    )
    projections.publishable_projections.to_csv(
        results_folder / f"{index} publishable projections.csv",
        index=True,
    )

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
    "simulation_designs",
    "layers",
    "chartpack",
    "run",
)


def load_experiment_configuration() -> dict:
    configuration = yaml.safe_load(EXPERIMENT_CONFIGURATION_YAML)
    assert isinstance(configuration, dict), "Experiment YAML must parse to a mapping."
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


def parse_sets_text(sets_text: str) -> dict[str, str]:
    if not isinstance(sets_text, str) or not sets_text.strip():
        return {}
    entries = [entry.strip() for entry in sets_text.split(",") if entry.strip()]
    result: dict[str, str] = {}
    for entry in entries:
        key, value = entry.split("=", maxsplit=1)
        result[key.strip()] = value.strip()
    return result


def variable_arguments(variable_name: str) -> list[str]:
    match = re.match(r"^[^(]+(?:\((.*)\))?$", variable_name)
    if match is None or match.group(1) is None or match.group(1) == "":
        return []
    return [part.strip() for part in match.group(1).split(",")]


def load_variable_summary(model_directory_path: Path) -> list[dict[str, str]]:
    path = model_directory_path / "diagnostics" / "variable summary.csv"
    assert path.exists(), f"Variable summary file not found at {path}"
    with path.open(newline="") as file:
        return list(csv.DictReader(file))


def prefix_rows(
    variable_prefix: str, variable_summary: list[dict[str, str]]
) -> list[dict[str, str]]:
    return [row for row in variable_summary if row["prefix"] == variable_prefix]


def selected_members(
    selector_value,
    dimension: str,
    available_members: set[str],
) -> set[str] | None:
    if selector_value is None or selector_value == "all":
        return None
    if isinstance(selector_value, str):
        selector_value = [selector_value]
    result = {str(member) for member in selector_value}
    invalid = sorted(result - available_members)
    assert not invalid, (
        f"Unknown selector members for {dimension}: {invalid}; "
        f"valid members are {sorted(available_members)}"
    )
    return result


def validate_selectors_for_prefix(rows: list[dict[str, str]], selectors: dict) -> None:
    for dimension, selector_value in selectors.items():
        available_members = {
            parse_sets_text(row.get("sets", "")).get(dimension)
            for row in rows
            if dimension in parse_sets_text(row.get("sets", ""))
        }
        available_members.discard(None)
        assert (
            available_members
        ), f"Selector dimension {dimension} is not available for prefix {rows[0]['prefix']}."
        selected_members(selector_value, dimension, available_members)


def row_matches_selectors(row: dict[str, str], selectors: dict) -> bool:
    row_sets = parse_sets_text(row.get("sets", ""))
    for dimension, selector_value in selectors.items():
        if selector_value is None or selector_value == "all":
            continue
        if isinstance(selector_value, str):
            selector_value = [selector_value]
        if row_sets.get(dimension) not in {str(member) for member in selector_value}:
            return False
    return True


def resolve_variables(
    series_or_shock: dict,
    variable_summary: list[dict[str, str]],
    region_members: list[str],
) -> list[str]:
    variable_prefix = series_or_shock["variable_prefix"]
    selectors = series_or_shock.get("selectors", {})
    require_prefix_only(variable_prefix)

    rows = prefix_rows(variable_prefix, variable_summary)
    if rows:
        expected_type = series_or_shock.get("variable_type")
        if expected_type is not None:
            invalid_types = sorted({row["var_type"] for row in rows} - {expected_type})
            assert not invalid_types, (
                f"Configured {variable_prefix} as {expected_type}, "
                f"but model metadata includes types {invalid_types}."
            )
        validate_selectors_for_prefix(rows, selectors)
        matching_rows = [row for row in rows if row_matches_selectors(row, selectors)]
        assert matching_rows, f"No variables resolved for {series_or_shock}"
        return [row["name"] for row in matching_rows]

    if variable_prefix in DERIVED_REGION_PREFIXES:
        selected_regions = selectors.get("regions", "all")
        if selected_regions == "all" or selected_regions is None:
            regions = region_members
        else:
            if isinstance(selected_regions, str):
                selected_regions = [selected_regions]
            invalid = sorted(set(selected_regions) - set(region_members))
            assert not invalid, f"Unknown regions for derived series: {invalid}"
            regions = list(selected_regions)
        return [f"{variable_prefix}({region})" for region in regions]

    raise AssertionError(
        f"The model does not include variables with prefix {variable_prefix}."
    )


def validate_year(year: int, projection_years: range, context: str) -> None:
    assert (
        year in projection_years
    ), f"{context} year {year} is outside projection years."


def validate_layer_years(
    layer: dict, projection_years: range, first_projection_year: int
) -> None:
    event_year = int(layer["event_year"])
    validate_year(event_year, projection_years, f"Layer {layer['id']} event")
    assert event_year > first_projection_year, (
        f"Layer {layer['id']} event year {event_year} must be after "
        f"first projection year {first_projection_year}."
    )
    for shock in layer["shocks"]:
        path = shock["value_path"]
        for key in ("start_year", "end_year"):
            if key in path:
                validate_year(
                    int(path[key]), projection_years, f"Layer {layer['id']} {key}"
                )
        if path["type"] == "explicit":
            for year in path["values"]:
                validate_year(
                    int(year), projection_years, f"Layer {layer['id']} explicit shock"
                )


def output_years(event_year: int, last_projection_year: int) -> list[int]:
    return list(range(event_year, last_projection_year + 1))


def shock_values(
    value_path: dict, years: list[int], event_year: int
) -> list[float | int]:
    path_type = value_path["type"]
    if path_type == "permanent_constant":
        start_year = int(value_path.get("start_year", event_year))
        value = value_path["value"]
        assert (
            start_year >= event_year
        ), "Shock cannot start before its layer event year."
        return [value if year >= start_year else 0 for year in years]
    if path_type == "temporary_constant":
        start_year = int(value_path["start_year"])
        end_year = int(value_path["end_year"])
        value = value_path["value"]
        assert (
            start_year >= event_year
        ), "Shock cannot start before its layer event year."
        assert (
            end_year >= start_year
        ), "Temporary shock end_year must be after start_year."
        return [value if start_year <= year <= end_year else 0 for year in years]
    if path_type == "explicit":
        values_by_year = {
            int(year): value for year, value in value_path["values"].items()
        }
        assert all(
            year >= event_year for year in values_by_year
        ), "Explicit shock cannot include non-zero years before event year."
        return [values_by_year.get(year, 0) for year in years]
    raise ValueError(f"Unsupported value_path type: {path_type}")


def layer_lookup(layers: list[dict]) -> dict[str, dict]:
    result = {layer["id"]: layer for layer in layers}
    assert len(result) == len(layers), "Layer ids must be unique."
    return result


def design_rows(design: dict, layers_by_id: dict[str, dict]) -> list[list[object]]:
    rows: list[list[object]] = [["name", "data", "event_year", "description"]]
    last_event_year: int | None = None
    for layer_id in design["layer_ids"]:
        layer = layers_by_id[layer_id]
        event_year = int(layer["event_year"])
        if last_event_year is not None:
            assert (
                event_year >= last_event_year
            ), "Design event years must be weakly increasing."
        last_event_year = event_year
        rows.append(
            [
                layer["name"],
                layer["data_file_name"],
                event_year,
                layer["description"],
            ]
        )
    return rows


def layer_rows(
    layer: dict,
    variable_summary: list[dict[str, str]],
    region_members: list[str],
    last_projection_year: int,
) -> list[list[object]]:
    event_year = int(layer["event_year"])
    years = output_years(
        event_year=event_year, last_projection_year=last_projection_year
    )
    rows: list[list[object]] = [["name", *years]]
    for shock in layer["shocks"]:
        values = shock_values(
            value_path=shock["value_path"],
            years=years,
            event_year=event_year,
        )
        for variable in resolve_variables(shock, variable_summary, region_members):
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


def chartpack_rows(
    chartpack_config: dict,
    variable_summary: list[dict[str, str]],
    region_members: list[str],
) -> list[list[str]]:
    rows: list[list[str]] = [["type", "attributes", "variable", "label"]]
    rows.append(["pack", "", "", chartpack_config["title"]])
    chart_attributes = pack_attributes(chartpack_config)

    for chart in chartpack_config["charts"]:
        rows.append(["chart", chart_attributes, "", ""])
        series_definitions = chart.get("series") or [chart]
        for series_definition in series_definitions:
            for variable in resolve_variables(
                series_definition, variable_summary, region_members
            ):
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


def render_readme(configuration: dict, setup_script_file_name: str) -> str:
    experiment = configuration["experiment"]
    designs = configuration["simulation_designs"]
    layers = configuration["layers"]
    design_inventory = "".join(
        f"- `{design['design_file_name']}`: Design file for {design['name']}.\n"
        for design in designs
    )
    layer_inventory = "".join(
        f"- `{layer['data_file_name']}`: Layer data for {layer['name']}.\n"
        for layer in layers
    )
    return f"""# {experiment['scenario_name']}

This experiment applies a temporary fiscal contraction in every model region. Government spending excluding labor is reduced by 10 percent of GDP from 2026 through 2028, then returns to the baseline path.

The shock lowers public demand directly. Lower government purchases affect output, consumption, investment, fiscal balances, interest rates, inflation, exchange rates, trade balances, labor demand, and asset values relative to the baseline. The setup and run scripts derive the experiment directory from their own location, so the folder can be renamed without editing generated files.

View [the detailed documentation for the experiment]({experiment['documentation_file_name']}).

## Files

- `{setup_script_file_name}`: Regenerates this experiment from the editable YAML configuration block.
- `{experiment['run_script_file_name']}`: Runs the fiscal contraction simulation and generates the report outputs.
- `{experiment['readme_file_name']}`: Explains the experiment and lists the files in this experiment directory.
- `{experiment['documentation_file_name']}`: Brief report-header text included in generated results reports.
{design_inventory}{layer_inventory}- `{experiment['chartpack_file_name']}`: Defines the charts for the fiscal contraction report.
"""


def render_documentation() -> str:
    return """This experiment reduces government spending excluding labor in all regions by 10 percent of GDP from 2026 through 2028. The shock is temporary: spending returns to the baseline path after 2028.

The fiscal contraction directly lowers public demand and changes fiscal balances. The report shows the resulting deviations in government spending, output, consumption, investment, inflation, interest rates, exchange rates, trade balances, labor demand, and asset values relative to baseline.
"""


def render_run_script(configuration: dict) -> str:
    experiment = configuration["experiment"]
    baseline = configuration["baseline"]
    run = configuration["run"]
    design = configuration["simulation_designs"][0]
    template = Template(RUN_SCRIPT_TEMPLATE)
    return template.substitute(
        model_configuration_file_name=experiment["model_configuration_file_name"],
        design_file_name=design["design_file_name"],
        chartpack_file_name=experiment["chartpack_file_name"],
        documentation_file_name=experiment["documentation_file_name"],
        report_template_file_name=experiment["report_template_file_name"],
        baseline_results_folder_name=baseline["results_folder_name"],
        solved_model_file_name=baseline["solved_model_file_name"],
        ask_to_solve_model_if_missing=bool(baseline["ask_to_solve_model_if_missing"]),
        solve_model_if_missing=bool(baseline["solve_model_if_missing"]),
        show_final_results=bool(run["show_final_results"]),
        derivation_names=repr(configuration["chartpack"].get("derivations", [])),
    )


def main() -> None:
    configuration = load_experiment_configuration()
    experiment_config = configuration["experiment"]

    experiment_directory_path: Path = Path(__file__).resolve().parent
    simulations_directory_path: Path = experiment_directory_path.parent
    model_directory_path: Path = simulations_directory_path.parent
    model_python_directory_path: Path = model_directory_path / "python"
    model_configuration_file_path: Path = (
        model_directory_path / experiment_config["model_configuration_file_name"]
    )
    report_template_path = (
        model_directory_path
        / "templates"
        / experiment_config["report_template_file_name"]
    )

    assert (
        model_configuration_file_path.exists()
    ), f"Model configuration file not found at {model_configuration_file_path}"
    assert (
        report_template_path.exists()
    ), f"Report template not found at {report_template_path}"

    if str(model_python_directory_path) not in sys.path:
        sys.path.insert(0, str(model_python_directory_path))

    from gcubed.model_configuration import ModelConfiguration

    model_configuration = ModelConfiguration(
        configuration_file=model_configuration_file_path
    )
    variable_summary = load_variable_summary(model_directory_path)
    region_members = []
    for row in variable_summary:
        sets = parse_sets_text(row.get("sets", ""))
        region = sets.get("regions")
        if region is not None and region not in region_members:
            region_members.append(region)
    projection_years = range(
        model_configuration.first_projection_year,
        model_configuration.last_projection_year + 1,
    )

    for layer in configuration["layers"]:
        validate_layer_years(
            layer=layer,
            projection_years=projection_years,
            first_projection_year=model_configuration.first_projection_year,
        )
        for shock in layer["shocks"]:
            resolve_variables(shock, variable_summary, region_members)

    first_result_year = int(configuration["chartpack"]["first_result_year"])
    last_result_year = int(configuration["chartpack"]["last_result_year"])
    validate_year(first_result_year, projection_years, "First result")
    validate_year(last_result_year, projection_years, "Last result")
    assert (
        first_result_year <= last_result_year
    ), "first_result_year must be <= last_result_year"

    layers_by_id = layer_lookup(configuration["layers"])
    overwrite = bool(experiment_config["overwrite_generated_files"])

    write_text(
        experiment_directory_path / experiment_config["readme_file_name"],
        render_readme(configuration, setup_script_file_name=Path(__file__).name),
        overwrite=overwrite,
    )
    write_text(
        experiment_directory_path / experiment_config["documentation_file_name"],
        render_documentation(),
        overwrite=overwrite,
    )
    for design in configuration["simulation_designs"]:
        write_csv(
            experiment_directory_path / design["design_file_name"],
            design_rows(design, layers_by_id),
            overwrite=overwrite,
        )
    for layer in configuration["layers"]:
        write_csv(
            experiment_directory_path / layer["data_file_name"],
            layer_rows(
                layer=layer,
                variable_summary=variable_summary,
                region_members=region_members,
                last_projection_year=model_configuration.last_projection_year,
            ),
            overwrite=overwrite,
        )
    write_csv(
        experiment_directory_path / experiment_config["chartpack_file_name"],
        chartpack_rows(configuration["chartpack"], variable_summary, region_members),
        overwrite=overwrite,
    )
    write_text(
        experiment_directory_path / experiment_config["run_script_file_name"],
        render_run_script(configuration),
        overwrite=overwrite,
    )


if __name__ == "__main__":
    main()
