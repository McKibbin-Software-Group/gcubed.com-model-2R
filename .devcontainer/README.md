# Setup Instructions

This template is for the new "combined root devcontainer and customer data mode" G-Cubed standard installation which requires the execution environment to have Internet access in order to interact with GitHub and Python dependency sources. It:

  * Does not require a separate ‘base’ devcontainer image
  * Removes the dependence on GitHub Actions
  * Incorporates automatic installation of the two parts of the G-Cubed Code Build Switcher - the Python module to manage the venvs, and the VS Code Extension which switches the active venv when it receives a request from the Python part
  * Automatically aligns all branches `/.devcontainer` directory and `/Makefile` contents with those on the `main` branch

See the accompanying [standalone prebuild document](./README-STANDALONE-PREBUILD.md) for an introduction to building the customer devcontainer so that it can operate without Internet connectivity.

## Process
To set up a customer:

1. Use GitHub to make the customer's repository from this template:
   * Click the "Use This Template" button (green button, top right, on template repo's main code page)
   * Select "Create a new repository"
   * Select desired Owner and provide a customer-specific Name for the repository
   * Provide a description if you want
   * Ensure it is Private

1. Clone the **newly created customer repo** to a local drive
   * **Make sure to do this in a linux/macOS environment!**

1. In your local copy:
   * Build and open the devcontainer - this ensures that the `main` branch starts from a fully configured state
   * Copy the customer's model & data
     * It is assumed that customer's data will be copied to the root of the repo.  If not (ie if you for instance want to have all customer date in, say, the `/user_data` directory) then also update the `USER_DATA_SUBDIRECTORY` value in the `.devcontainer/customer-configuration.env` file to reflect this
   * Create a `README.md` file in the repo root directory appropriate for the customer

1. Test/validate the repo as necessary

1. Commit your changes and push them back to the *customer's* GitHub repo

1. Start a codespace from the GitHub repo, and test

1. If the customer is going to be running the devcontainer locally then recommend to them that they should clone using the HTTPS web URL as this will then utilise the git credential helper which makes things easier when authenticating on GitHub


## G-Cubed Code Build Switcher
It is assumed that the user data repo contains an `initialise.py` or equivalent script in each python simulation directory which will allow users to automatically install and/or enable the Python dependencies and environment required for that model.

Just in case, here is a sample python script which invokes the G-Cube Code Build Switcher & requests a venv switch. Takes the gcubed code build tag from command-line or defaults to a preset version.

```Python
import gcubed_build_switcher
import sys

# Take build tag from command line or use default
gcubed_code_build_tag = sys.argv[1] if len(sys.argv) > 1 else "<name of a default/fallback tag>"

# Returns True or False
result = gcubed_build_switcher.activate_or_build_and_activate_venv(gcubed_code_build_tag)
print(f"Result: {"It Verked!!" if result is True else "Oh noes!"}")

```

## Auto branch alignment

When creating or rebuilding a devcontainer the `gcubed-setup.sh` script copies `.devcontainer/gcubed-setup/git-hooks/post-checkout` (an executable shell script) to the `.git/hooks` directory.  This file is invoked on every checkout action and, when the checkout is for a branch that is not the default/main branch, will update the contents of `/.devcontainer` and `/Makefile` from the default/main branch.

***NOTE*** the switching process attempts to determine and use the name of the _default_ branch (which is normally `main`) and falls back to `main` if that process doesn't work.  It is nevertheless recommended that the `default` branch is indeed called `main`.

Items affected by changes to `/.devcontainer` files include:
  * Base devcontainer configuration
  * VS Code extensions installed into the devcontainer instance, and
  * Anything controlled by the `gcubed-setup.sh` script, which includes
     * Installation of the git hook used to align branches with the main branch
     * Permission settings on repo files
     * Installation of the Python component of the G-Cubed virtual environment switcher, including any of its dependencies
     * Various small ‘quality of life’ changes

Any changes are unstaged in local git history so that they can be reverted if necessary (which will last until the next switch back _into_ that branch).

### Motivation
The motivation for doing this is to simplify future upgrades and to provide G-Cubed users with a more consistent experience regardless of which branch they are on (_ie:_ not being prompted to rebuild the devcontainer every branch switch if branch configurations diverge; different and unexpected system behaviours when switching branches; devcontainer upgrades automatically flowing through to all branches; etc).

Though this doesn't protect users from consequences of altering devcontainer configuration in the main branch it does simplify recovery from such a situation (essentially an 'upgrade' process).

### Upgrading
Devcontainer upgrades are applied to the main branch.  Users will need to merge those upgrades into their repo’s main branch and then those upgrades will in turn be automatically applied to any branches that the users switch to.

If the upgrade interferes with the operation of a particular branch then that upgrade can be temporarily reverted using git.

### Exceptions
Since only `.devcontainers`and the `Makefile` are updated, any other changes will need to be applied manually if required.

`.vscode/settings.json` which controls editor settings is a notable example. The thinking behind this is that the user is provided with a default set of editor settings but is free to then modify those settings if/when required without fear that they will be overridden at every branch change.

