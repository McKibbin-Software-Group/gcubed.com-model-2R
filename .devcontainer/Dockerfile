ARG PYTHON_VARIANT=1-3.12
FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VARIANT}

ARG SYM_REPOSITORY
ARG SYM_REPOSITORY_TAG
ARG SYM_SOURCE_WORKING_DIRECTORY
ARG SYM_EXECUTABLE_DIRECTORY
ARG VENV_SWITCHER_TAG
ARG TZ
ENV TZ=${TZ}

# Install the G-Cubed venv switcher files directly from the latest GitHub release.
# Installation/activation will occur in gcubed-setup.sh

RUN set -eux; \
  mkdir -p /home/vscode/extensions/gcubed-venv-switcher; \
  cd /home/vscode/extensions/gcubed-venv-switcher; \
  echo "VENV_SWITCHER_TAG = '${VENV_SWITCHER_TAG}'"; \
  if [ "${VENV_SWITCHER_TAG}" = "latest" ]; then \
    curl -L -O https://github.com/McKibbin-Software-Group/gcubed-build-switcher/releases/latest/download/pyproject.toml; \
    curl -L -O https://github.com/McKibbin-Software-Group/gcubed-build-switcher/releases/latest/download/gcubed-vscode-venv-switcher.vsix; \
  else \
    curl -L -O https://github.com/McKibbin-Software-Group/gcubed-build-switcher/releases/download/${VENV_SWITCHER_TAG}/pyproject.toml; \
    curl -L -O https://github.com/McKibbin-Software-Group/gcubed-build-switcher/releases/download/${VENV_SWITCHER_TAG}/gcubed-vscode-venv-switcher.vsix; \
  fi; \
  export DEBIAN_FRONTEND=noninteractive; \
  apt-get update; \
  apt-get install --no-install-recommends -y \
      tzdata curl ca-certificates byacc=1:2.0.20221106-1; \
  apt-get autoremove -y; \
  apt-get clean; \
  rm -rf /var/lib/apt/lists/*; \
  git clone --depth 1 --single-branch --branch "${SYM_REPOSITORY_TAG}" "${SYM_REPOSITORY}" "${SYM_SOURCE_WORKING_DIRECTORY}"; \
  cd "${SYM_SOURCE_WORKING_DIRECTORY}/src"; \
  make; \
  chmod a-w+x sym; \
  mkdir -p "${SYM_EXECUTABLE_DIRECTORY}"; \
  mv sym "${SYM_EXECUTABLE_DIRECTORY}"; \
  cd; \
  rm -rf "${SYM_SOURCE_WORKING_DIRECTORY}"; \
  su vscode -c "curl -LsSf https://astral.sh/uv/0.6.3/install.sh | sh"

