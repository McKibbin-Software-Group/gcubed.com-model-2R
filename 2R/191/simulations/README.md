# Simulation experiments

Several simulation experiments are provided as examples.

The Python scripts to run the experiments are in the `python` folder.

To run a script, open it in your VS Code devcontainer and click on the run arrow in the top right corner of the editor.

## Preliminaries

Before running the experiments:

1. Make sure that the correct version of the Python G-Cubed version is installed.

```bash
setup_python_gcubed.py
```

2. Solve the model and create the baseline projections by running 

```bash
run_baseline.py
```

3. Share the solved model and baseline projections with the experiments (so that they do not have to be reproduced for each experiment that is run) by running:

```bash
share_baseline_projections_with_experiments.py
```

## Example experiments

Each of the following example experiments can be run using the python script with the matching experiment number. Thus, for experiment 1, run:

```bash
run_experiment_1.py
```

0. [No shock baseline](experiment_0/README.md) used to check that this just reproduces the original baseline.

1. [A permanent increase in the USA inflation target](experiment_1/README.md)

2. [A temporary increase in the USA inflation target](experiment_2/README.md)

3. [Unexpected reversal of permanent increase to inflation target in the USA](experiment_3/README.md)

4. [Anticipation effect for an investment tax credit](experiment_4/README.md)

5. [Find potential output growth consistent with achieving target inflation](experiment_5/README.md)

6. [Linear and Non-linear global tariff calculations](experiment_6/README.md)
