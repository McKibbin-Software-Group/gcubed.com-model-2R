# USA tariff trade war with the rest of the world.

Tariff increases are imposed by the USA on the rest of the world. These increases are reciprocated.

## Linear version simulation layer

The simulation layer contains the tariff rate changes. It must have an event year on or after 2019.

## How to run the linear simulation experiment

### Check the SYM model

To use a linear tariff calculation, first alter the SYM model as follows:

1. Make the TXM variable endgenous (change the `exo` attribute to `end` in the variable declaration)

2. Ensure that the TXM equations are included in the fiscal closure SYM files.

3. Run the SYM processor to update the files used as a basis for running the model.

### Regenerate the new model solution and baseline projections.

Rerun the baseline using the `run_baseline.py` script.

### Run the experiment

Run `run_experiment_6_linear.py` to run the experiment.