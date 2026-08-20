from pathlib import Path

from gcubed import configure_logging
from gcubed.model_configuration import ModelConfiguration
from gcubed.model_parameters import generate_baseline_data_files_and_user_parameters
from gcubed.reporting import experiment_results_folder

###############################################################################
# This script sets up the various CSV files containing the information needed
# to adjust the baseline projections for exogenous variables in the GCubed model.
###############################################################################

# Specify the model configuration file name.
MODEL_CONFIGURATION_FILE_NAME: str = "model_configuration.yaml"

# Set this to True to overwrite the standard baseline data files. Set it to
# False to write template files with "_template" appended to their names.
OVERWRITE_BASELINE_FILES: bool = True

# Preserve every existing user-owned parameter value. Runtime-derived
# parameters, including capital returns, are deliberately omitted.
PRESERVE_EXISTING_USER_PARAMETERS: bool = True

###############################################################################
# Customisation typically ends here.
###############################################################################


def main() -> None:
    script_path: Path = Path(__file__).resolve()
    model_directory_path: Path = script_path.parent.parent
    model_configuration_file_path: Path = (
        model_directory_path / MODEL_CONFIGURATION_FILE_NAME
    )

    assert (
        model_configuration_file_path.exists()
    ), f"Model configuration file not found at {model_configuration_file_path}"

    model_configuration: ModelConfiguration = ModelConfiguration(
        configuration_file=model_configuration_file_path,
        validation_profile="baseline_input_generation",
    )
    results_folder: str = experiment_results_folder(
        configuration=model_configuration,
        root_results_directory_path=model_directory_path.parent.parent / "results",
        experiment_script_name=script_path.name,
    )

    configure_logging(folder=results_folder)
    generate_baseline_data_files_and_user_parameters(
        model_configuration=model_configuration,
        overwrite=OVERWRITE_BASELINE_FILES,
        preserve_existing_user_parameters=PRESERVE_EXISTING_USER_PARAMETERS,
    )


if __name__ == "__main__":
    main()
