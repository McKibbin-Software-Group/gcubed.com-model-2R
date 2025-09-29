###############################################################################
# Linearise the model to enable access to partial derivatives
# for chosen equations in the model.
#
# User specified variables to deterimine which model configuration to use.
###############################################################################

# Specify the model configuration file name
model_configuration_file_name: str = "configuration.csv"

# Specify the name prefixes of the variables for which to calculate partial derivatives.
variable_name_prefixes: list[str] = ["TAXM"]

###############################################################################
# Baseline customisation typically ends here.
#
# See the end of the script to customise the generation of results.
###############################################################################

from pathlib import Path
import pickle
from gcubed.model_configuration import ModelConfiguration
from gcubed.model import Model
from gcubed.linearisation.linear_model import LinearModel
from gcubed import configure_logging
from gcubed.reporting import experiment_results_folder

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
linear_model: LinearModel = LinearModel(model=model)


def save_derivatives(equation: str):
    linear_model.equation_partial_derivatives(lhs_variable_prefix=equation).to_csv(
        results_folder / f"linearisation partial derivatives - {equation}.csv",
        float_format="%.12f",
    )


for variable_name_prefix in variable_name_prefixes:
    save_derivatives(variable_name_prefix)
