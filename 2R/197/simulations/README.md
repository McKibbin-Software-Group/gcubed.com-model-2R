# Simulation experiments

This folder contains the files needed to:

1. Run the model baseline.
2. Run simulation experiments using that baseline.

Note that most if not all simulations, of the baseline or experiments that overlay the baseline need to be set up in a way that tailors them to the specific regions and sectors etc. in the model being used. Thus, they are distributed as setup scripts. Those scripts generate all of the other files that are needed to do the required simulation work. Importantly, they generate the Python script that actually runs the baseline or runs the experiment.

Thus, the typical usage pattern is to run the setup script once, possibly after customising the many ways in which it can be configured. Then you can run the baseline or run the experiment that has been set up and you can do so as many times as you want, without having to repeat the setup process.

Also note that you no longer need to solve the model and generate baseline projections in advance of running a specific experiment. If the solved model is not available each experiment is automatically set up to solve the model first, generate the baseline projections and then do the simulation using those baseline projections.

## Preliminaries

There are still some simple preliminaries that need to be completed. 


### Set up the G-Cubed software that is specific to the model being used

Before running the the baseline or simulation experiments, make sure that the correct version of the Python G-Cubed software is installed.

Access the model's `python` folder and run:

```bash
setup_python_gcubed.py
```

### Update the model definition (if necessary)

If the SYM definition of the model has been altered in any way then the SYM processor needs to be run.

Again, access the model's `python` folder and run:

```bash
update_model_definition.py
```

### Solve the model and create the baseline projections.

If the model or its data or parameters have changed in any way, the model will need to be resolved.

If you have never set up the baseline generation before, you will need to do so. 

Access the `simulations/baseline` folder and run:

```bash
setup_baseline.py
```

Once it has completed, it will create the script you need to run to solve the model and create the baseline projections.

```bash
run_baseline.py
```

## Experiments

Each experiment is typically a subfolder within the models `simulations` folder. The name of the folder typically indicates the nature of the experiment.

When first accessed, that subfolder for the experiment contains the experiment's setup script.

Edit the configuration details in that script and then run it to generate the script needed to run the experiment, `run_experiment.py`, and the various shock files and design files and chartpack files and documentation that make up the details of the experiment itself. See [SETUP SCRIPT CONFIGURATION SYNTAX](<SETUP.md>) for documentation of the YAML configuration syntax used by the setup scripts.