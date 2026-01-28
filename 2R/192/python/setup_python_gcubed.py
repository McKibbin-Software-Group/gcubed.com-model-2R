# Expected you will adapt this per customer/model/build
import gcubed_build_switcher
import sys

GCUBED_CODE_BUILD_TAG = "gcubed-4-0-3-5"

# Take build tag from command line or use default
use_this_build_tag = sys.argv[1] if len(sys.argv) > 1 else GCUBED_CODE_BUILD_TAG

# Returns True or False
result = gcubed_build_switcher.activate_or_build_and_activate_venv(use_this_build_tag)
print(
    "Result: "
    + (
        "You are now using the right version of G-Cubed for this model build."
        if result is True
        else "Failed to switch to the right version of G-Cubed for this model build!"
    )
)
