###############################################################################
# User specified variables to deterimine which model configuration to use
# and which experiment to run.
###############################################################################

# Specify the model configuration file name
model_configuration_file_name: str = "configuration.csv"

# Specify the name of the experiment directory
# (located in the model's simulations directory)
experiment_directory_name: str = "experiment_5"

# Specify the name of the experiment design file
experiment_design_file_name: str = "design.csv"

# Set the name of the target filename
controls_file_name: str = "controls.csv"
"""
The name of the controls file.
"""

# Set the name of the target filename
targets_file_name: str = "targets.csv"
"""
The name of the targets file.
"""

# Fit a polynomial of this order to the control variable projections.
# 0 implies a constant path for the control variable.
# 1 implies a linear path for the control variable.
# 2 implies a quadratic path for the control variable.
# 3 implies a cubic path for the control variable.
# 4 implies a quartic path for the control variable.
polynomial_order: int = 0

# Set the first control year
first_control_year: int = 2023
"""
The first year in which changes can be made to the controls.
"""

# Set the last control year
last_control_year: int = 2150
"""
The last year in which changes can be made to the controls.
"""

###############################################################################
# Experiment customisation typically ends here.
#
# See the end of the script to customise the generation of results.
###############################################################################

import pickle
import logging
from pathlib import Path
from typing import List
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
import gcubed
from gcubed.model_configuration import ModelConfiguration
from gcubed.projections.baseline_projections import BaselineProjections
from gcubed.projections.projections import Projections
from gcubed.runners.simulation_runner import SimulationRunner
from gcubed import configure_logging
from gcubed.reporting import experiment_results_folder, generate_all_simulation_results
from gcubed.projections.derivations import Derivations
from gcubed.projections.derivation_definitions import (
    growth_rates,
)

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

# Load the previously saved baseline projections.
baseline_projections_pickle_file: Path = results_folder / "baseline_projections.pickle"
assert (
    baseline_projections_pickle_file.exists()
), f"Baseline projections pickle file not found at {baseline_projections_pickle_file}"
with open(baseline_projections_pickle_file, "rb") as file:
    baseline_projections: BaselineProjections = pickle.load(file)


#################

# Generate the list of control years used for polynomials in objective
# function evaluation.
control_years: list[int] = list(range(first_control_year, last_control_year + 1))
control_years_integers: np.ndarray = np.array(
    range(0, last_control_year - first_control_year + 1)
).reshape(1, last_control_year - first_control_year + 1)

# Generate the column labels of the years where control values can change.
control_year_labels: list[str] = [str(x) for x in control_years]

# Get the timestamp for the results
timestamp: str = gcubed.now()

# Set up targets and controls files
logging.info(
    f"Updating the values in the controls file, {controls_file_name} from {first_control_year} onwards."
)
absolute_path_of_controls_file: Path = (
    model_configuration.simulations_directory
    / experiment_directory_name
    / controls_file_name
)
assert (
    absolute_path_of_controls_file.exists()
), f"Could not find {controls_file_name} in the {experiment_directory_name} experiment."

absolute_path_of_targets_file: Path = (
    model_configuration.simulations_directory
    / experiment_directory_name
    / targets_file_name
)
assert (
    absolute_path_of_targets_file.exists()
), f"Could not find {targets_file_name} in the {experiment_directory_name} experiment."

# Check that the experiment design file exists.
assert (
    model_configuration.simulations_directory / experiment_directory_name / "design.csv"
), f"Could not find the design file for the {experiment_directory_name} experiment."

# Load the targets CSV file.
targets = pd.read_csv(
    absolute_path_of_targets_file,
    header=0,
    index_col=0,
)

# Load the starting CSV controls file to get starting values for controls.
controls = pd.read_csv(
    absolute_path_of_controls_file,
    header=0,
    index_col=0,
).astype(float)

# Set up the starting vector for the least squares solver.
# The start_x vector contains the values of each cell in the DataFrame,
# obtained by stacking the rows one after the other and then
# flattening the resulting array.
# Thus the first set of elements are for the first control variable
# and those are followed by the values for the second control variable etc.
start_x: np.ndarray = np.zeros(
    shape=(len(controls.index), polynomial_order + 1)
).flatten()

iteration: int = 1


def objective_function(x: np.ndarray) -> np.ndarray:
    """

    ### Overview

    The objective function passed as an input to the least squares
    algorithm.

    The input `x` is converted to a set of values for the exogenous
    variables that are the control variables. The simulation is then
    run with these control variable values. The resulting projections are
    compared to the target projections and the differences are returned as a vector.

    The least squares algorithm drives these differences to zero by minimising
    a quadratic function of these differences.

    ### Arguments

    `x`: The vector of values being used to evaluate the objective function.

    ### Returns

    The return value, the vector of actual projections less target projections,
    evaluated for the vector of input control variables, x.
    """

    global iteration

    # Enable easy access of polynomial coefficients for each control variable.
    coefficients: np.ndarray = x.reshape(len(controls.index), polynomial_order + 1)

    control_values: np.ndarray = np.tile(
        coefficients[:, 0].reshape(len(controls.index), 1),
        (1, control_years_integers.shape[1]),
    )
    if polynomial_order > 0:
        for i in range(1, polynomial_order + 1):
            control_values: np.ndarray = control_values + (
                coefficients[:, i].reshape(len(controls.index), 1)
                * (control_years_integers**i)
            )

    # Save the candidate control values to the simulation layer file to run the simulation
    new_control_values: pd.DataFrame = pd.DataFrame(
        control_values,
        index=controls.index,
        columns=control_year_labels,
    ).astype(float)

    controls.loc[:, control_year_labels] = new_control_values.to_numpy()
    controls.to_csv(absolute_path_of_controls_file)

    # Set up the simulation runner.
    runner: SimulationRunner = SimulationRunner(
        baseline_projections=baseline_projections,
        experiment_design_file=f"{experiment_directory_name}/design.csv",
    )

    # Run the simulation experiment.
    runner.run()

    # Access the final projections from the runner.
    trial_projections: pd.DataFrame = (
        runner.final_projections.publishable_projections.loc[
            targets.index, targets.columns
        ]
    )

    errors: pd.DataFrame = gcubed.projections.differences(
        original_projections=targets,
        new_projections=trial_projections,
    )
    logging.info(
        f"Iteration {iteration}:\n\nThe polynomial coefficients are:\n{coefficients}\nThe controls are:\n{controls.loc[:, control_year_labels]}\nThe differences from target are:\n{errors}\n\n"
    )

    result: np.ndarray = errors.to_numpy().flatten()

    iteration += 1
    return result


# Run the optimisation and report results
solver_results = least_squares(fun=objective_function, x0=start_x, xtol=1e-2, ftol=1e-2)
logging.info(f"Solver results: {solver_results}")


# Set up the simulation runner to run with the final set of control values.
runner: SimulationRunner = SimulationRunner(
    baseline_projections=baseline_projections,
    experiment_design_file=f"{experiment_directory_name}/{experiment_design_file_name}",
)

# Run the simulation a last time using the optimised controls projections.
runner.run()

all_projections: List[Projections] = runner.all_projections

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

derivations: Derivations = Derivations(sym_data=runner.model.sym_data)
derivations.add(derivation=growth_rates.GDPRGROWTH())

generate_all_simulation_results(
    chartpack_path=model_configuration.simulations_directory
    / experiment_directory_name
    / "chartpack.csv",
    documentation_path=model_configuration.simulations_directory
    / experiment_directory_name
    / "documentation.md",
    template_path=model_configuration.chartpacks_directory / "chart-template.html",
    results_directory_path=results_folder,
    all_projections=all_projections,
    derivations=derivations,
    show_final_results=True,
)
