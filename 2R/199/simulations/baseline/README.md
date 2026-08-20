# Baseline

This folder contains the script to set up the baseline projections.

Optionally edit `setup.yaml`, then run `setup.py` to overwrite its declared baseline chartpack or design artefacts. The maintained `run_baseline.py` owns all runtime configuration and does not read setup.
The maintained `run_baseline.py` source runs the baseline projections and report.

To configure the setup for the baseline, edit the `setup.yaml` file.
This includes the configuration of the baseline chartpack, which determines the charts included in the
baseline report and the variables included in those charts. See the [instructions](INSTRUCTIONS.md)
with details on how to configure the chartpack from the baseline setup script.

The run_baseline.py script will generate a report for the baseline projections. **It will also solve
the model and save the solved model to a joblib file in the results folder. This allows you to
reuse the solved model for faster iteration on the baseline projections without needing to
re-solve the model each time.**

You can change configuration settings in the run_baseline.py script.

You can also directly modify the chartpack that defines the baseline projections reports.

The run script, README, and report documentation are maintained source files; running `setup.py` does not regenerate them.

View [the detailed documentation for the baseline projections](documentation.md).
