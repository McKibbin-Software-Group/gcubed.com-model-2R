###############################################################################
# User specified variables to deterimine which model configuration to use
# and which experiment to run.
#
# NOTE: THIS EXPERIMENT REQUIRES TXM TO BE EXOGENOUS IN THE SYM MODEL.
#
###############################################################################

# Specify the model configuration file name
model_configuration_file_name: str = "configuration.csv"

# Specify the name of the experiment directory
# (located in the model's simulations directory)
experiment_directory_name: str = "experiment_6"

# Specify the name of the baseline experiment design
# to include the tariff revenue projections layer.
experiment_design_file_name_baseline: str = "design_nonlinear_baseline.csv"

# Uncomment one of the following:
# experiment_design_file_name_final: str = "design_nonlinear_without_reciprocation.csv"
experiment_design_file_name_final: str = "design_nonlinear_with_reciprocation.csv"

# The name of the simulation layer to be updated (the non-linear results)
simulation_layer_to_adjust: str = "tariff_revenue.csv"

# The total number of iterations to run the simulation to get convergence
# of the tariff revenue.
number_of_iterations: int = 5

cap_on_prices: float = 10

###############################################################################
# Experiment customisation typically ends here.
#
# See the end of the script to customise the generation of results.
###############################################################################

import logging
import pickle
from pathlib import Path
from typing import List

import pandas as pd
from gcubed.model_configuration import ModelConfiguration
from gcubed.model_parameters.parameters import Parameters
from gcubed.projections.baseline_projections import BaselineProjections
from gcubed.projections.projections import Projections
from gcubed.runners.simulation_runner import SimulationRunner
from gcubed import configure_logging
from gcubed.reporting import experiment_results_folder, generate_all_simulation_results
from gcubed.projections.derivations import Derivations
from gcubed.projections.derivation_definitions import (
    bilateral_trade_balances,
    growth_rates,
    cumulation_variables,
)
from gcubed.sym_data import SymData

# Get the name of this script - to use when setting up the results storage directory.
experiment_script_name: str = Path(__file__).name

# Get the root directory for the model, relative to this script.
model_directory_path: Path = Path(__file__).resolve().parent.parent

# Get the path to the model configuration file.
model_configuration_file_path: Path = (
    model_directory_path / model_configuration_file_name
)

# Check that the model configuration file exists.
assert (
    model_configuration_file_path.exists()
), f"Model configuration file not found at {model_configuration_file_path}"

# Get the path to the directory where all experiment results are stored for this devcontainer.
root_results_directory_path: Path = model_directory_path.parent.parent / "results"

# Load the model configuration
model_configuration: ModelConfiguration = ModelConfiguration(
    configuration_file=model_configuration_file_path
)

# Determine where the results will be saved.
results_folder: str = experiment_results_folder(
    configuration=model_configuration,
    root_results_directory_path=root_results_directory_path,
    experiment_script_name=experiment_script_name,
)

# Set up logging
configure_logging(folder=results_folder)

# Check that the experiment design file exists and get its earliest event year.
baseline_experiment_design_file: Path = (
    model_configuration.simulations_directory
    / experiment_directory_name
    / experiment_design_file_name_baseline
)
assert (
    baseline_experiment_design_file.exists()
), f"Could not find the baseline design file for the {experiment_directory_name} experiment."

# Get the earliest event year from the design.csv file.
design_information: pd.DataFrame = pd.read_csv(baseline_experiment_design_file)
first_event_year: int = design_information["event_year"].min()

# Determine expected location of experiment adjustments file and check that the file exists.
adjustments_file_path: Path = (
    model_configuration.simulations_directory
    / experiment_directory_name
    / simulation_layer_to_adjust
)
assert (
    adjustments_file_path.exists()
), f"Could not find the simulation layer file where nonlinear projections will be saved: {adjustments_file_path}"

# Load the previously saved baseline projections.
baseline_projections_pickle_file: Path = results_folder / "baseline_projections.pickle"
assert (
    baseline_projections_pickle_file.exists()
), f"Baseline projections pickle file not found at {baseline_projections_pickle_file}"
with open(baseline_projections_pickle_file, "rb") as file:
    baseline_projections: BaselineProjections = pickle.load(file)

# Check that the TXM variable is exogenous
txm_variable_names = baseline_projections.sym_data.variables_with_prefix(
    variable_name_prefix="TXM"
)
assert (
    baseline_projections.sym_data.variable_summary.loc[txm_variable_names, "var_type"]
    == "exo"
).all(), "TXM is not exogenous."

# Determine the years through which the tax revenue projections will be updated.
simulation_years: list[str] = [
    str(x)
    for x in range(first_event_year, model_configuration.last_projection_year + 1)
]


def update_tax_revenue_projections(
    runner: SimulationRunner,
    counter: int = 0,
) -> None:
    """
    Update the tax revenue projections in the simulation layer.
    """

    model_configuration: ModelConfiguration = runner.model.configuration
    sym_data: SymData = runner.model.sym_data
    parameters: Parameters = runner.model.parameters

    good_dest_orig_index: pd.Index = pd.MultiIndex.from_product(
        [sym_data.goods_members, sym_data.regions_members, sym_data.regions_members],
        names=["goods", "dest", "orig"],
    )

    dest_orig_index: pd.Index = pd.MultiIndex.from_product(
        [sym_data.regions_members, sym_data.regions_members], names=["dest", "orig"]
    )

    good_dest_index: pd.Index = pd.MultiIndex.from_product(
        [sym_data.goods_members, sym_data.regions_members], names=["goods", "dest"]
    )

    dest_index: pd.Index = pd.Index(sym_data.regions_members, name="dest")

    # Get the dataframe containing all of the parameter values.
    all_parameters: pd.DataFrame = parameters.parameter_values
    all_parameters.index = all_parameters.name

    # Get the vector of co2coef parameter values.
    FTA: pd.DataFrame = all_parameters.loc[
        all_parameters.index.str.startswith("FTA("), ["value"]
    ]
    # Replicate the FTA to match against each good, stacking vertically into a single dataframe
    FTA = pd.concat(
        [FTA] * sym_data.non_electricity_generation_goods_count, ignore_index=True
    )
    FTA.index = good_dest_orig_index
    FTA.columns.name = "value"

    MUL: pd.DataFrame = all_parameters.loc[
        all_parameters.index.str.startswith("MUL("), ["value"]
    ]
    # Replicate the MUL to match against each good, stacking vertically into a single dataframe
    MUL = pd.concat(
        [MUL] * sym_data.non_electricity_generation_goods_count, ignore_index=True
    )
    MUL.index = good_dest_orig_index
    MUL.columns.name = "value"

    # Do the calculations using the final database projections.
    database_projections: pd.DataFrame = runner.final_projections.database_projections

    # Set up the dataframe for the calculation result.
    TXM: pd.DataFrame = (
        database_projections.loc[
            database_projections.index.str.startswith(f"TXM("),
            simulation_years,
        ]
        * 0.0
    )

    # Get the data for all of the variables that are on the RHS.
    TIM: pd.DataFrame = (
        database_projections.loc[
            database_projections.index.str.startswith(f"TIM("),
            simulation_years,
        ]
        / 100.0
    )
    TIM.index = good_dest_orig_index

    TIF: pd.DataFrame = (
        database_projections.loc[
            database_projections.index.str.startswith(f"TIF("),
            simulation_years,
        ]
        / 100.0
    )
    TIF.index = good_dest_index

    PIM: pd.DataFrame = (
        database_projections.loc[
            database_projections.index.str.startswith(f"PIM("),
            simulation_years,
        ]
        / 100.0
    )
    PIM.index = good_dest_orig_index

    PIM.iloc[:, -50:] = PIM.iloc[:, [-51]]

    PIM.to_csv(model_configuration.diagnostics_directory / f"PIM {counter}.csv")

    # Impose a ceiling on PIM values
    # Convert inf values in PIM to 30000
    PIM[PIM == float("inf")] = cap_on_prices
    PIM[PIM > cap_on_prices] = cap_on_prices

    IMP: pd.DataFrame = (
        database_projections.loc[
            database_projections.index.str.startswith(f"IMP("),
            simulation_years,
        ]
        / 100.0
    )

    # Convert to a fraction of US GDP (not needed in non-linear calculation)
    # IMP_YRAT_SCALE_FACTOR: pd.Series =  runner.model.database.gdp_ratio_scaling_factor(year=2018).loc[IMP.index]
    # IMP: pd.DataFrame = IMP.mul(IMP_YRAT_SCALE_FACTOR,axis="index")

    IMP.index = good_dest_orig_index

    IMP.iloc[:, -50:] = IMP.iloc[:, [-51]]

    PRID: pd.DataFrame = (
        database_projections.loc[
            database_projections.index.str.startswith(f"PRID("),
            simulation_years,
        ]
        / 100.0
    )
    PRID.index = dest_index

    imports: pd.DataFrame = IMP * PIM

    standard_tariff_revenue: pd.DataFrame = (imports * TIM).mul(
        MUL["value"], axis="index"
    )
    total_standard_tariff_revenue_by_good: pd.DataFrame = (
        standard_tariff_revenue.groupby(["goods", "dest"]).sum()
    )
    total_standard_tariff_revenue_by_good: pd.DataFrame = (
        total_standard_tariff_revenue_by_good.reindex(good_dest_index)
    )

    fta_tariff_revenue: pd.DataFrame = imports.mul(FTA["value"], axis="index")
    total_fta_tariff_revenue_by_good: pd.DataFrame = fta_tariff_revenue.groupby(
        ["goods", "dest"]
    ).sum()
    total_fta_tariff_revenue_by_good = total_fta_tariff_revenue_by_good.reindex(
        good_dest_index
    )
    total_fta_tariff_revenue_by_good: pd.DataFrame = (
        total_fta_tariff_revenue_by_good * TIF
    )

    # Combine standard and FTA tariff revenue and apply division by PRID and multiply by 100 to prepare for insertion into the adjustments layer.
    total_tariff_revenue_by_good: pd.DataFrame = (
        total_standard_tariff_revenue_by_good + total_fta_tariff_revenue_by_good
    )

    scaled_real_total_tariff_revenue_by_good: pd.DataFrame = (
        total_tariff_revenue_by_good.div(PRID, level="dest") * 100.0
    )

    # Update TXM projections
    TXM.loc[:, simulation_years] = scaled_real_total_tariff_revenue_by_good.to_numpy()

    # logging.debug(f"TXM\n{TXM.iloc[0:5,0:5]}")

    # Prevent terminal condition instability from infecting ever
    # earlier years with each iteration of the tax experiment
    # by making the last 10 observations equal to the 11th last.
    TXM.iloc[:, -30:] = TXM.iloc[:, [-31]]

    # Load the CSV experiment file that will be updated.
    adjustments = pd.read_csv(
        adjustments_file_path,
        header=0,
        index_col=0,
    ).astype(float)

    # Update the projections
    adjustments.loc[TXM.index, simulation_years] = TXM

    # logging.debug(f"tariff adjustments\n{adjustments.iloc[:,0:10]}")

    # # Save adjustments that will be used for the next iteration
    adjustments.to_csv(
        model_configuration.simulations_directory
        / experiment_directory_name
        / simulation_layer_to_adjust
    )


# Reset the tariff revenue projections to zero.
# Load the CSV experiment file that will be updated.
adjustments = pd.read_csv(
    adjustments_file_path,
    header=0,
    index_col=0,
).astype(float)

# Update the projections
adjustments.loc[:, simulation_years] = 0.0

# # Save adjustments that will be used for the next iteration
adjustments.to_csv(
    model_configuration.simulations_directory
    / experiment_directory_name
    / simulation_layer_to_adjust
)

# Run the baseline simulation several times to get convergence on tariff revenues for the baseline.
for i in range(1, number_of_iterations + 1):

    logging.info(f"Baseline simulation {i}")

    baseline_runner: SimulationRunner = SimulationRunner(
        baseline_projections=baseline_projections,
        experiment_design_file=f"{experiment_directory_name}/{experiment_design_file_name_baseline}",
    )

    # Run the simulation experiment.
    baseline_runner.run()

    update_tax_revenue_projections(
        runner=baseline_runner,
        counter=i,
    )

# Run the final simulation several times to get convergence on final tariff revenues.
for i in range(1, number_of_iterations + 1):

    logging.info(f"Final simulation {i}")

    final_runner: SimulationRunner = SimulationRunner(
        baseline_projections=baseline_projections,
        experiment_design_file=f"{experiment_directory_name}/{experiment_design_file_name_final}",
    )

    # Run the simulation experiment.
    final_runner.run()

    update_tax_revenue_projections(
        runner=final_runner,
        counter=10 + i,
    )

all_projections: List[Projections] = [
    baseline_runner.final_projections,
    final_runner.final_projections,
]

###############################################################################
# Adjust the following parameters to use different chart packs or
# report documentation or templates.
#
# The chartpack path is the location of the chartpack CSV file,
# typically stored either in the model's chartpack
# directory or in the experiment directory.
#
# The documentation path is the location of the Markdown documentation file
# explaining the experiment details, typically stored in the model's
# experiment directory.
#
# The template path is the location of the HTML template file
# used to generate the chartpack, typically stored in the model's
# chartpacks directory.
#
# The list of all projections is typically the list of all projections
# generated by the simulation runne, one for the baseline and one for
# each simulation layer.
#
# The derivations are the derived variables that are required for the experiment.
#
# The show_final_results flag determines whether the final results are displayed
# in your web browser. If shown, these are the deviations between the final
# simulation layer and the baseline projections.
###############################################################################

derivations: Derivations = Derivations(sym_data=baseline_runner.model.sym_data)
derivations.add(derivation=growth_rates.GDPRGROWTH())
derivations.add(derivation=bilateral_trade_balances.BTBAL())

generate_all_simulation_results(
    chartpack_path=model_configuration.simulations_directory
    / experiment_directory_name
    / "chartpack.csv",
    documentation_path=model_configuration.simulations_directory
    / experiment_directory_name
    / "documentation_nonlinear.md",
    template_path=model_configuration.chartpacks_directory / "chart-template.html",
    results_directory_path=results_folder,
    all_projections=all_projections,
    derivations=derivations,
    show_final_results=True,
)
