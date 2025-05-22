###############################################################################
# User specified variables to deterimine which model configuration to use.
###############################################################################

# Specify the model configuration file name
model_configuration_file_name: str = "configuration.csv"

# comparison model version
comparison_model_version: str = "2R"

# comparison model build
comparison_model_build: str = "180"

comparison_model_configuration_file_name: str = "configuration6G179.csv"

###############################################################################
# Customisation typically ends here.
###############################################################################

from pathlib import Path
import logging
import numpy as np
import pandas as pd
from gcubed.model_configuration import ModelConfiguration
from gcubed.model import Model
from gcubed import configure_logging
from gcubed.reporting import experiment_results_folder
from gcubed.data.database_comparator import DatabaseComparator


# Get the name of this script - to use when setting up the results storage directory.
experiment_script_name: str = Path(__file__).name

# Get the root directory for the model, relative to this script.
model_directory_path: Path = Path(__file__).resolve().parent.parent

# Get the path to the directory where all experiment results are stored for this devcontainer.
root_results_directory_path: Path = model_directory_path.parent.parent / "results"

# Get the path to the model configuration file.
model_configuration_file_path: Path = model_directory_path / model_configuration_file_name

# Check that the model configuration file exists.
assert model_configuration_file_path.exists(), f"Model configuration file not found at {model_configuration_file_path}"

# Load the model configuration
model_configuration: ModelConfiguration = ModelConfiguration(
    configuration_file=model_configuration_file_path
)

# Determine where the results will be saved.
results_folder: str = experiment_results_folder(
    configuration=model_configuration,
    root_results_directory_path=root_results_directory_path,
    experiment_script_name=experiment_script_name
)

# Set up logging
configure_logging(folder=results_folder)

comparison_model_configuration_file_path: Path = model_directory_path.parent.parent / comparison_model_version / comparison_model_build / comparison_model_configuration_file_name

comparison_model_configuration: ModelConfiguration = ModelConfiguration(
    configuration_file=comparison_model_configuration_file_path
)

# Generate the results from doing a comparison of the databases for the two models.
DatabaseComparator(
    model_a_configuration=model_configuration,
    model_b_configuration=comparison_model_configuration,
).save_comparison_results(output_directory_path=results_folder)