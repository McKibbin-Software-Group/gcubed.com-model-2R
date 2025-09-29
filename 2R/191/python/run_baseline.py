###############################################################################
# User specified variables to deterimine which model configuration to use.
###############################################################################

# Specify the model configuration file name
model_configuration_file_name: str = "configuration.csv"

# Specify the name of the experiment directory
# (located in the model's simulations directory)
experiment_directory_name: str = "baseline"

# Set to true if you want to force the model to be solved again.
# This needs to be done if the data, parameters or SYM files change.
force_model__to_be_resolved: bool = True

# Set to true if you want to force the  baseline to be regenerated.
# This needs to be done if the baseline assumptions change.
force_baseline_regeneration: bool = True

# Set to true if you want to see the baseline charts web page when the script finishes.
show_baseline_charts: bool = False

#############################################################################
# Baseline customisation typically ends here.
#
# See the end of the script to customise the generation of results.
###############################################################################

from pathlib import Path
import pickle
import logging
from gcubed.model import Model
from gcubed.projections.baseline_projections import BaselineProjections
from gcubed.linearisation.solved_model import SolvedModel
from gcubed.model_configuration import ModelConfiguration
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

# Generate the baseline projections
baseline_projections_pickle_file: Path = results_folder / "baseline_projections.pickle"
if not force_baseline_regeneration and not force_model__to_be_resolved and baseline_projections_pickle_file.exists():
    logging.warning(f"!!! Loading previous baseline {baseline_projections_pickle_file}")
    with open(baseline_projections_pickle_file, "rb") as file:
        baseline_projections: BaselineProjections = pickle.load(file)
else:

    # Check to see if a solved model has been pickled in the results folder.
    solved_model_pickle_file: str = results_folder / "solved_model.pickle"
    if not force_model__to_be_resolved and solved_model_pickle_file.exists():
        logging.warning(f"!!! Loading previously solved model from {solved_model_pickle_file}")
        with open(solved_model_pickle_file, "rb") as file:
            solved_model: SolvedModel = pickle.load(file)
    else:
        model: Model = Model(configuration=model_configuration)
        solved_model: SolvedModel = SolvedModel(model=model)
        with open(solved_model_pickle_file, "wb") as file:
            pickle.dump(solved_model, file)
        logging.info(
            f"Saved the solved model for later reuse. Delete {solved_model_pickle_file} if you want to re-solve the model."
        )

    baseline_projections: BaselineProjections = BaselineProjections(
        solved_model=solved_model,
    )
    with open(baseline_projections_pickle_file, "wb") as file:
        pickle.dump(baseline_projections, file)
    logging.info(
        f"Saved the baseline for later reuse. Delete {baseline_projections_pickle_file} if you want to regenerate the baseline."
    )

# Save the baseline projections to CSV files
baseline_projections.charting_projections.to_csv(
    results_folder / f"baseline projections.csv"
)

baseline_projections.projections.to_csv(
    results_folder / f"baseline raw projections.csv"
)

baseline_projections.database_projections.to_csv(
    results_folder / f"baseline database projections.csv"
)

derivations: Derivations = Derivations(sym_data=baseline_projections.model.sym_data)
derivations.add(derivation=growth_rates.GDPRGROWTH())
derivations.add(derivation=growth_rates.OUTPUTGROWTH())
derivations.add(derivation=growth_rates.SECTOROUTPUTGROWTH())

generate_all_simulation_results(
    chartpack_path=model_configuration.simulations_directory
    / experiment_directory_name
    / "chartpack.csv",
    documentation_path=model_configuration.simulations_directory
    / experiment_directory_name
    / "documentation.md",
    template_path=model_configuration.chartpacks_directory / "chart-template.html",
    results_directory_path=results_folder,
    derivations=derivations,
    all_projections=[baseline_projections],
    show_final_results=show_baseline_charts,
)