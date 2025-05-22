# USA tariff trade war with the rest of the world.

Tariff increases are imposed by the USA on the rest of the world. These increases are reciprocated.

## Non-linear version simulation layers

The first simulation layer contains just the tariff revenue. It must have an event year of 2019.

It contains the actual tariff revenue by good / region calculated using the non-linear equation.

The second simulation layer contains the tariff rate changes. It must have an event year on or after 2019.

## How to run the non-linear simulation experiment

### Modify the SYM model

To use a nonlinear tariff calculation, first alter the SYM model as follows:

1. Make the TXM variable exogenous (change the `end` attribute to `exo` in the variable declaration).

2. Comment out the TXM equations in the fiscal closure SYM files.

3. Run the SYM processor to update the files used as a basis for running the model.

### Regenerate the new model solution and baseline projections.

Rerun the baseline using the `run_baseline.py` script.

### Generate the appropriate baseline projections

Use the `design_nonlinear_baseline.csv` file to exclude the tariff changes from the experiment.

Run the `run_experiment_6_nonlinear_baseline.py` experiment several times until the tariff revenue simulation layer does not alter when a new run is done.

This results in a runner with final projections that are valid to use as a baseline, before the introduction of the tariff changes.

### Generate the final projections

Use the `design_nonlinear_final.csv` file to include the tariff changes in the experiment.

Run the `run_experiment_6_nonlinear_final.py` experiment several times until the tariff revenue simulation layer does not alter when a new run is done.

This results in a runner with final projections that are valid to use as the final projections, after the introduction of the tariff changes.

### Results

Compare the final projections of the two runners to get the deviations caused by the tariff changes, when doing the tariff revenue calculations in a non-linear fashion.

