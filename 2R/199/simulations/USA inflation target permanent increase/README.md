# An increase in the USA inflation target

This experiment permanently raises the United States inflation target by 1 percentage point. The increase is applied from the scenario start and remains in place through the projection horizon.

Economically, a higher inflation target changes the nominal anchor for the United States. Monetary policy can tolerate a higher rate of price growth before tightening, which affects nominal interest rates, real interest rates, exchange rates, output, and inflation dynamics relative to the baseline.

The run script, README, and report documentation are maintained source files; running `setup.py` does not regenerate them.

View [the detailed documentation for the experiment](documentation.md).

## Files

- `setup.py`: Generates this experiment from the sibling `setup.yaml` configuration.
- `setup.yaml`: Declares the experiment and reporting configuration.
- `run_experiment.py`: Runs the experiment using the baseline solved model and produces the report outputs.
- `README.md`: Explains the experiment and lists the files in this experiment directory.
- `documentation.md`: Brief report-header text included in generated results reports.
- `design.yaml`: Lists the simulation layers and points to their shock data files.
- `adjustments.csv`: Contains the permanent 1 percentage point shock to the inflation target from the scenario start onward.
- `chartpack.yaml`: Defines the charts to include in the generated experiment report.
