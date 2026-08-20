###############################################################################
# User specified variables to determine SYM processor behavior.
###############################################################################

# SYM processor executable. Override by setting the SYM environment variable.
sym_executable_name: str = "sym"

# Specify the model configuration file name.
model_configuration_file_name: str = "model_configuration.yaml"

###############################################################################
# Customisation typically ends here.
###############################################################################

import yaml
from pathlib import Path
import os
import re
import shutil
import subprocess


# Get the path to the model directory, relative to this script.
python_directory_path: Path = Path(__file__).resolve().parent
model_directory_path: Path = python_directory_path.parent

# Get the path to the model configuration file.
model_configuration_file_path: Path = (
    model_directory_path / model_configuration_file_name
)

# Get the path to the SYM directory.
sym_directory_path: Path = model_directory_path / "sym"


def build_number(build: str) -> int:
    match = re.match(r"^([0-9]+)", build)
    assert match is not None, f"Could not determine numeric build from {build}"
    return int(match.group(1))


def root_sym_file_name(version: str, build: str) -> str:
    if build_number(build) < 181:
        return f"ggg-{version}-{build}.sym"
    return "ggg-model.sym"


def load_model_version_and_build(configuration_file_path: Path) -> tuple[str, str]:
    with configuration_file_path.open(encoding="utf-8") as configuration_file:
        configuration = yaml.safe_load(configuration_file)

    assert isinstance(configuration, dict), "Model configuration must be a mapping."
    assert configuration.get("schema_version") == 1, (
        "Only model configuration schema version 1 is supported."
    )
    model = configuration.get("model")
    assert isinstance(model, dict), "Model configuration must contain a model mapping."
    version = model.get("version")
    build = model.get("build")
    assert isinstance(version, str) and version, (
        "model.version not found in the model configuration file."
    )
    assert isinstance(build, str) and build, (
        "model.build not found in the model configuration file."
    )
    assert version == configuration_file_path.parent.parent.name, (
        "model.version must match the model version directory."
    )
    assert build == configuration_file_path.parent.name, (
        "model.build must match the model build directory."
    )

    return version, build


def remove_generated_sym_files(sym_directory_path: Path) -> None:
    for pattern in ("*.html", "*.csv", "*.lis", "*.py"):
        for file_path in sym_directory_path.glob(pattern):
            if file_path.is_file() or file_path.is_symlink():
                file_path.unlink()


def print_directory_listing(directory_path: Path) -> None:
    entries = sorted(directory_path.iterdir(), key=lambda path: path.name.lower())
    print(f"total {len(entries)}")
    for entry in entries:
        entry_type = "d" if entry.is_dir() else "-"
        print(f"{entry_type} {entry.name}")


def main() -> None:
    assert (
        model_configuration_file_path.exists()
    ), f"Model configuration file not found at {model_configuration_file_path}"

    version, build = load_model_version_and_build(
        configuration_file_path=model_configuration_file_path
    )
    root_sym_file: str = root_sym_file_name(version=version, build=build)
    root_sym_file_path: Path = sym_directory_path / root_sym_file
    model_output_stem: str = f"model_{version}_{build}"
    sym_executable: str = os.environ.get("SYM", sym_executable_name)

    assert sym_directory_path.exists(), f"SYM directory not found at {sym_directory_path}"
    assert root_sym_file_path.exists(), f"Root SYM file not found at {root_sym_file_path}"
    assert shutil.which(sym_executable) is not None, (
        f"SYM processor executable not found: {sym_executable}. "
        "Set the SYM environment variable or edit sym_executable_name."
    )

    print(
        f"Running SYM processor for model {version} build {build} "
        f"starting from {root_sym_file} ..."
    )

    remove_generated_sym_files(sym_directory_path=sym_directory_path)

    subprocess.run(
        [sym_executable, "-html", root_sym_file, f"{model_output_stem}.html"],
        cwd=sym_directory_path,
        check=True,
    )
    subprocess.run(
        [sym_executable, "-python", root_sym_file, f"{model_output_stem}.py"],
        cwd=sym_directory_path,
        check=True,
    )

    print(f"Updated files in {version}/{build}/sym:")
    print_directory_listing(directory_path=sym_directory_path)
    print(
        "... The SYM processor has finished running. Check that a *.py file "
        "has been created and check that there is no rubbish.lis file."
    )


if __name__ == "__main__":
    main()
