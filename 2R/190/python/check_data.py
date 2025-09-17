###############################################################################
# User specified variables to deterimine which model configuration to use.
###############################################################################

# Specify the model configuration file name
model_configuration_file_name: str = "configuration.csv"

# Bounding years for analysis.


# The first year must be on or after the first database year.
# The last year must be before the last projection year.
# Typically, these bounds are tight around the first projection year.
first_database_year_to_check: int = 2017
last_database_year_to_check: int = 2019

# The first year must be on or after the first database year.
# The last year must be before the last projection year.
# Typically, these bounds are tight around the first projection year.
first_projections_year_to_check: int = 2017
last_projections_year_to_check: int = 2021

###############################################################################
# Customisation typically ends here.
###############################################################################

from pathlib import Path
import logging
from typing import List
from gcubed.data.database_validator import DatabaseValidator
from gcubed.model_configuration import ModelConfiguration
from gcubed.reporting import experiment_results_folder
from gcubed.model import Model
from gcubed.projections.baseline_projections import BaselineProjections
from gcubed.linearisation.solved_model import SolvedModel
from gcubed import configure_logging

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

# Solve the model
model: Model = Model(configuration=model_configuration)
chosen_database_years: List[str] = [
    str(year)
    for year in range(
        first_database_year_to_check, last_database_year_to_check + 1
    )
]
database_validator: DatabaseValidator = DatabaseValidator(
    model_configuration=model.configuration,
    sym_data=model.sym_data,
    parameters=model.parameters,
    data=model.database.data.loc[:, chosen_database_years],
    results_folder=results_folder,
)

database_validator.validate_all_relationships()

database_validator.generate_database_metrics()

# Finish before trying to work with projections as well.
# Comment out this early exit to do a check with the projections as well.
exit(0)

# Can also work with the data and database projections.
solved_model: SolvedModel = SolvedModel(model=model)
baseline_projections: BaselineProjections = BaselineProjections(
    solved_model=solved_model,
)
chosen_projections_years: List[str] = [
    str(year)
    for year in range(
        first_projections_year_to_check, last_projections_year_to_check + 1
    )
]
projections_validator: DatabaseValidator = DatabaseValidator(
    model_configuration=model.configuration,
    sym_data=model.sym_data,
    parameters=model.parameters,
    data=baseline_projections.combined_database_and_projections.loc[
        :, chosen_projections_years
    ],
    results_folder=results_folder,
)

projections_validator.validate_all_relationships()
