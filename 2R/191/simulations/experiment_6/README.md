# USA tariff trade war with China, Canada and Mexico.

Tariff increases are imposed by the USA Canada. These increases are reciprocated.

The experiment has two forms:

* one based on calculating the tariff revenue in the usual way, within the model using a linear approximation to the tariff-revenue function.

* one where the tariff revenue calculation outside of the model to allow for non-linearities.

View [the documentation for the **linear** tariff experiment](documentation_linear.md).

View [the documentation for the **nonlinear** tariff experiment](documentation_nonlinear.md).

## Standard (linear) version

The simulation layer contains the tariff rate changes. It must have an event year on or after the
first projection year.

The following instructions set out how to run the standard version of this experiment.

### Check the SYM model

To use a linear tariff calculation, first alter the SYM model as follows:

1. Make the TXM variable endogenous (make sure the variable declaration includes `end` rather than `exo` in  its list of attributes).

2. Ensure that the TXM equation declaration is included in the fiscal closure SYM files.

3. Run the SYM processor to update the files used as a basis for running the model using the make file (run `make sym` at the terminal in VS Code).

### Regenerate the new model solution and baseline projections.

Rerun the baseline using the `run_baseline.py` script if the SYM files were altered since the baseline was last generated.

### Run the experiment

Run `run_experiment_6.py`.

## Non-linear version

The first simulation layer contains just the tariff revenue variables by good and region (`TXM`). 

**It must have an event year that is the year after the first projection year** so that tariff revenues
are computed for all projection years.

It contains the actual tariff revenue by good / region calculated using the non-linear equation.

The second simulation layer contains the tariff rate changes. It must have an event year on or after 2019.

## How to run the non-linear simulation experiment

### Modify the SYM model

To use a nonlinear tariff calculation, first alter the SYM model as follows:

1. Make the TXM variable exogenous (change the `end` attribute to `exo` in the variable declaration).

2. Comment out the TXM equations in the fiscal closure SYM files.

3. Run the SYM processor to update the files used as a basis for running the model.

### Regenerate the new model solution and baseline projections.

Rerun the baseline using the `run_baseline.py` script if the SYM files were altered since the baseline was last generated.

### Run the experiment

The experiment involves solving the model and then producing a baseline iteratively, to compute
the baseline tariff revenues (from tariff rates in the database and any tariffs specified in
custom baseline exogenous projections). The experiment is then re-run to iteratively solve for 
the tariff rates associated with the full set of simulation layers.

Run the experiment using the `run_experiment_6_nonlinear.py` script.

#### Generate the appropriate baseline projections

That script first uses the `design_nonlinear_baseline.csv` file to exclude the tariff changes from the experiment.

It then uses the `design_nonlinear_final.csv` file to include the tariff changes in the experiment.

### Results

Compare the final projections of the two runners to get the deviations caused by the tariff changes, 
when doing the tariff revenue calculations in a non-linear fashion.

