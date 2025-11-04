###############################################################################
# This script is used to create results directories for all experiments
# based on the scripts used to run the experiments. It also creates symbolic
# links to the serialized files in each of the experiment
# results directories.
#
# User configuration
###############################################################################

# Specify the model configuration file name
model_configuration_file_name: str = "configuration.csv"

# Specify the name of the script that generates the baseline results
baseline_generation_script_file_name: str = "run_baseline.py"

# Specify the prefix of the experiment script file names
experiment_script_file_name_prefix: str = "run_"

###############################################################################
# Script customisation typically ends here.
#
# See the end of the script to customise the generation of results.
###############################################################################

from pathlib import Path
from joblib import dump, load
from gcubed.model import Model
from gcubed.projections.baseline_projections import BaselineProjections
from gcubed.linearisation.solved_model import SolvedModel
from gcubed.model_configuration import ModelConfiguration
from gcubed import configure_logging
from gcubed.reporting import experiment_results_folder

# Get the name of this script - to use when setting up the results storage directory.
experiment_script_name: str = Path(__file__).name

# Get the directory that contains the model's Python scripts.
python_directory_path: Path = Path(__file__).resolve().parent

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
results_directory_path: Path = experiment_results_folder(
    configuration=model_configuration,
    root_results_directory_path=root_results_directory_path,
    experiment_script_name=experiment_script_name,
)

full_path_to_baseline_generation_script: Path = (
    python_directory_path / baseline_generation_script_file_name
)

assert (
    full_path_to_baseline_generation_script.exists()
), f"Cannot find the {full_path_to_baseline_generation_script} script."

baseline_results_folder: Path = (
    results_directory_path.parent / f"{baseline_generation_script_file_name[:-3]}"
)

# Get the list of Python scripts in the python folder that start with `run`.
experiment_scripts: list[str] = [
    file.name  # Use file.name to get just the file name
    for file in python_directory_path.iterdir()
    if file.is_file()
    and file.suffix == ".py"
    and file.name.startswith(experiment_script_file_name_prefix)
]

assert (
    baseline_results_folder.exists()
), f"Cannot find the {baseline_results_folder} folder. Run the {full_path_to_baseline_generation_script} script first."

# Get the list of serialized data files
serialized_files: list[str] = [
    file.name  # Use file.name to get just the file name
    for file in baseline_results_folder.iterdir()
    if file.is_file() and file.suffix == ".joblib"
]

for experiment_script in experiment_scripts:
    experiment_results_folder: Path = (
        results_directory_path.parent / f"{experiment_script[:-3]}"
    )
    if experiment_results_folder == baseline_results_folder:
        continue
    experiment_results_folder.mkdir(parents=True, exist_ok=True)
    for serialized_file in serialized_files:
        symbolic_link: Path = Path(experiment_results_folder) / serialized_file
        if not symbolic_link.exists():
            target = Path("path/to/target")
            link = Path("path/to/symlink")
            symbolic_link.symlink_to(baseline_results_folder / serialized_file)
