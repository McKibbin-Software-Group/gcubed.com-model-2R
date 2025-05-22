#!/bin/bash

function directory_from_repo_url() {
    _var=${1##*/}
    _var=${_var%.*}
    echo ${_var}
}

function enter_directory() {
    cd "${1}"
    echo "Changed directory from: ${OLDPWD} -> ${PWD}"
}

function adjust_file_ownership_and_mode() {
    # Change the owner of all files inside repo if necessary - required when running rootless docker
    # By keeping the original group the invoking user still has access
    enter_directory "${workspace_mount}"
    echo "Adjusting repo ownership and modes if necessary"
    sudo chown -R $(id -u):$(id -g) .
    sudo chmod -R u+rwX,g+rwX .
    # Set the SGID on all directories so that the correct group is applied if created outside the devcontainer
    sudo find . -type d -exec chmod g+s {} +
}

function show_current_commit() {
    echo "${1}$(git --no-optional-locks symbolic-ref --short HEAD 2>/dev/null) / $(git --no-optional-locks rev-parse --short HEAD 2>/dev/null)"
}

while getopts "u:" flag
do
    case "${flag}" in
        u) user_data_defaults_directory="${OPTARG}";;
    esac
done

workspace_mount="${WORKSPACE_MOUNT}"
gcubed_root="${GCUBED_ROOT}"

echo -e "\n******************************** INFO ***************************************************"
echo "User info: $(id)"
echo -e "Machine info: $(uname -a)\n"
echo "Current directory: ${PWD}"
echo "User data defaults source directory: ${user_data_defaults_directory}"
echo -e "Project root directory: ${gcubed_root}\n"
echo "WORKSPACE_MOUNT env var: ${workspace_mount}"
echo -e "GCUBED_ROOT env var: ${gcubed_root}\n"

show_current_commit "Repo's current commit: "
echo -e "*****************************************************************************************\n"

# Check required environment variables
if [ -z "${workspace_mount}" ]; then
  echo "ERROR: WORKSPACE_MOUNT environment variable is not set."
  echo "ERROR: Contact G-Cubed support - aborting..."
  exit 1
fi

if [ -z "${gcubed_root}" ]; then
  echo "ERROR: GCUBED_ROOT environment variable is not set."
  echo "ERROR: Contact G-Cubed support - aborting..."
  exit 1
fi

# Ensure user data directory exists, or abort
if [ ! -d "${gcubed_root}" ]; then
  echo "ERROR: Directory '${gcubed_root}' does not exist. Repo not properly configured."
  echo "ERROR: Contact G-Cubed support - aborting..."
  exit 1
fi

# Run 'globally' required setup
adjust_file_ownership_and_mode

# Finish if the container is already set up
if [ -f /tmp/gcubed-container-initialised-semaphore ]; then
  echo "Container already initialized - no further setup required"
  exit 0
fi

# copy default userdata setup & settings in. NOTE: no-clobber
cp -r --no-clobber ${user_data_defaults_directory}/. ${gcubed_root}

# install the Python part of the G-Cubed venv switcher
# NOTE: relies on the TOML file having been previously installed by, eg, Dockerfile
enter_directory /home/vscode/extensions/gcubed-venv-switcher
sudo $(which uv) pip install --system -r pyproject.toml

# install the git hook
enter_directory "${workspace_mount}"
echo "Installing git hook"
cp .devcontainer/gcubed-setup/git-hooks/post-checkout .git/hooks

# make some small QoL changes
echo "Making QoL changes..."
echo 'alias ll="ls -alhF"' >> ~/.bashrc
echo 'cd() { if [ "$#" -eq 0 ]; then command cd "'"${gcubed_root}"'"; else command cd "$@"; fi; }' >> ~/.bashrc
echo 'export EDITOR="code --wait"' >> ~/.bashrc
git config --global core.autocrlf input

# Mark initialization complete
touch /tmp/gcubed-container-initialised-semaphore

echo "Done!"
