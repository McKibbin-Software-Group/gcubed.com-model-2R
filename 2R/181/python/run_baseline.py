###############################################################################
# User specified variables to deterimine which model configuration to use.
###############################################################################

# Specify the model configuration file name
model_configuration_file_name: str = "configuration.csv"

# Specify the name of the experiment directory
# (located in the model's simulations directory)
experiment_directory_name: str = "baseline"

###############################################################################
# Baseline customisation typically ends here.
#
# See the end of the script to customise the generation of results.
###############################################################################

from pathlib import Path
import pickle
from gcubed.model import Model
from gcubed.projections.baseline_projections import BaselineProjections
from gcubed.linearisation.solved_model import SolvedModel
from gcubed.model_configuration import ModelConfiguration
from gcubed import configure_logging
from gcubed.reporting import experiment_results_folder, generate_all_simulation_results

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

# Check to see if a solved model has been pickled in the results folder.
model: Model = Model(configuration=model_configuration)
solved_model: SolvedModel = SolvedModel(model=model)

# Generate the baseline projections
baseline_projections: BaselineProjections = BaselineProjections(
    solved_model=solved_model,
)
baseline_projections_pickle_file: Path = results_folder / "baseline_projections.pickle"
with open(baseline_projections_pickle_file, "wb") as file:
    pickle.dump(baseline_projections, file)

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

generate_all_simulation_results(
    chartpack_path=model_configuration.simulations_directory
    / experiment_directory_name
    / "chartpack.csv",
    documentation_path=model_configuration.simulations_directory
    / experiment_directory_name
    / "documentation.md",
    template_path=model_configuration.chartpacks_directory / "chart-template.html",
    results_directory_path=results_folder,
    all_projections=[baseline_projections],
)
