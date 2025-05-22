# Prebuilding a G-Cubed Environment

## Introduction
Standard G-Cubed deployment builds the container on the fly and loads G-Cubed Code builds as required.

Some customer IT/security requirements do not allow this mode of operation.

Prebuilding a G-Cubed environment 'packages' the entirety of a working customer devcontainer such that we can simply supply the customer with two files which can then operate in complete isolation and without Internet connectivity.

## Document Scope
This document only talks about preparing G-Cubed platform image files for standalone/isolated deployment.
It does not cover adapting to nor integrating with the customer environment.

There are a lot of caveats around using this process, and doing this with a customer requires careful deployment & operation design beforehand.  Items to consider in addition to what this document covers include but are not limited to:
* Setting up and access to the VS Code front-end
* Access to the execution environment from the front-end
* How will the customer interact with their repo
  * GitHub vs on-prem Git server
  * Git repo server vs on-disk
  * If on-prem, interactions (if any) between that and GitHub
* How will we deploy model updates
* How will we deploy G-Cubed code updates
* How will we deploy base image updates
* The environment within which the devcontainer will operate
  * How to deploy to that environment
  * Security restrictions
  * Effects of user and group IDs, vis-a-vis permissions, both inside and outside the container (this is often the trickiest piece) - especially when needing to align the Linux UID and GID permissions with the container's `vscode` user and group


## Process Overview
Deploying in this mode requires an advanced understanding of how the G-Cubed platform operates, Docker (not only images/containers etc but also permissions and user/group IDs inside & outside container), and Linux devops.  This document only covers the piece of work required to prepare a standalone G-Cubed devcontainer but does not cover requirements for installation, operation, customer repo interactions etc which are also necessary for the G-Cubed platform to operate correctly.

_**NOTE:** This process should only be started after proper planning and implementation design which covers all aspects of installation and operation of G-Cubed has been completed with the customer._

To understand this part of the process properly you need to understand how Docker works and how it creates and maintains 'images' vs 'containers' - please ensure you have a reasonable level of understanding before proceeding further.

In summary, from a storage perspective, a 'container' is an initially empty virtual disk layer that sits on top of one or more (usually multiple) Docker 'image' layers.  These image layers are created during the 'build' process and are usually defined by a supplier of an 'image'.  They essentially create the virtual 'machine' that is running when you start a Docker container for the first time.

When a Docker container is running, files are read from this stack of images (a file which sits higher in the stack takes precedence over the same file in lower layers) - with the 'container' layer being the 'highest' layer in the stack.  Anything written to disk is written to the 'container' layer.

The 'container' layer is ephemeral - created when a container is first started, and destroyed when the container is stopped.

Docker also has the capability to 'mount' external disk images (docker 'volumes') or directories into a running container (these images/directories appear at a predetermined location in the container directory structure).  These external disk images/directories are not destroyed when the container is stopped.

This means that information written to locations outside the mounted volumes/directories (ie written to a users home directory structure or to other locations on the virtual 'machine') is lost when the container is destroyed, but information written to mounted directories is retained.

G-Cubed devcontainers run in Docker containers and use these mechanisms. When a devcontainer is started Docker creates a container disk image layer and the customer repository is mounted into that environment from an external (local) directory.  This means that when a G-Cubed devcontainer is running there are conceptually three locations where data is stored -
1. The Docker 'image' stack (essentially the underlying 'machine' image).  This is built prior to the container starting and is immutable
1. The 'container' virtual disk - created as a layer over the image when a docker container is started.  Anything written to a location that is not an external mount is written to this layer, and is ephemeral
1. The repository mount location (*eg:* `/workspaces/<customer-repo-name>`).  Anything written here is retained between container rebuilds, however is still at risk of being changed/deleted at any time (hence why we encourage customers to actively use git and push any work that needs to be retained to the central repository)

When a G-Cubed devcontainer is started, there are a number of processes which run before the container is available for use.  These processes install all the dependencies and requirements to be able to run the G-Cubed applications (*ie* the sym processor is retrieved, compiled, and installed; all the python prerequisites are installed; the G-Cubed Build Switcher is installed; etc).  All of this is written to the container virtual disk.

Once the container is available and running, some additional dependencies (the Python G-Cubed Code requirements) are installed by the G-Cubed Build Switcher.  These dependencies are only loaded when initiated by the user, and are written into the repository mount (gcubed code and associated Python dependencies are loaded in the `venv_gcubed_*` directory structure), however may have some links into the 'global' environment (*ie* may, depending on circumstances, point to the global Python interpreter).

Work done by a user on G-Cubed models is stored in the repository mount.

To build a standalone deployable G-Cubed image we first create and run a customer G-Cubed devcontainer, change to each model and build directory and load the additional G-Cubed dependencies, and then use the Docker `commit` function to create an image from this fully instantiated environment.

The `commit` function essentially creates another image layer from the container virtual disk and captures a number of runtime elements which allow Docker to start a new container with exactly that same configuration.

This new image, along with a copy of the fully populated repository mount, can then be sent to the customer and used to instantiate the G-Cubed Devcontainer in an isolated environment.


## Initial Preparation
This version must be done on a system that is similar to the target platform (ie same processor & Linux kernel type).
* Instantiate a customer repo as normal
* Start the devcontainer & let it build normally
* Switch to each Model & Build in turn & run the virtual environment switcher in order to build the venvs
* Ensure the `gcubed-setup.sh` file is a version that includes a check for 'already created' semaphore

Prepare the `devcontainer.json`:
* move the existing `devcontainer.json` to, _eg_ `devcontainer-online.json`
* create a new `devcontainer-offline.json`

  ```json
  {
    "name": "<CUSTOMER NAME> Prebuilt G-Cubed v1.0.0",
    "image": "<image name>"
  }
  ```
  Image name will be what you use to create the Docker image as well.  Use a semver tagged naming convention which includes the target platform annotation, such as `customername-prebuild-x86_64:v1.0.0`.

* create a symlink from `devcontainer-offline.json` to `devcontainer.json`

  ```sh
  ln -s devcontainer-offline.json devcontainer.json
  ```
  This will make it easy to switch between online and offline modes simply by changing the simlink and rebuilding the devcontainer.


## Build
* Whilst the devcontainer is still running:
  * Start another host OS prompt
  * Use `docker commit` to generate an image
    * Use `docker ps` to obtain the container name
    * Use the tagged image name you created above

      ```sh
      docker commit <container-id-or-name> <tagged image name>
      ```

  * Using an appropriate naming convention export the image as a tar file

    ```sh
    docker save -o </output/path/customername-prebuild-x86_64:v1.0.0.tar> <customername-prebuild-x86_64:v1.0.0>
    ```

  * Archive the project root (ie the root of the customer repo)
    * `cd` into the directory containing the parent of the project root (_ie_ if the repo is in `/gcubed/customer-repo` then `cd /gcubed`)
    * use tar to archive the entire directory structure

      ```sh
      sudo tar --preserve-permissions --same-owner -cvf /output/path/<customer-repo>.tar <customer-repo>
      ```
      **NOTE:** No trailing `/` after the `<customer-repo>` directory name

  * You can now shut down the devcontainer.

## Deploy
This is the minimum required to deploy the image files to a customer system.  See additional work required, noted above in [Document Scope](#document-scope).

Copy the two `tar` files to a shared location on the target system.

Then, per G-Cubed user account:

* Log in as that user
* Install the Docker image into that user's local image cache:

  ```sh
  docker load -i </source/location/customername-prebuild-x86_64:v1.0.0.tar>
  ```

* Create a directory for the `devcontainer` (this should use the customer repo naming convention) and extract the project root archive:

  ```sh
  mkdir <destination for customer-models>
  cd <destination for customer-models>
  sudo tar -xvpf /shared/path/<customer-repo>.tar -C .
  ```
  **NOTE:** `<destination for customer-models>` should be in a user-private location such as `~/gcubed`.

The `devcontainer` is now ready to be started.

