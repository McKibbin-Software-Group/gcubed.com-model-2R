# Simulation baselines and experiments

Each child directory contains a maintained Python command for a baseline or
experiment. The run script is the client-owned source of runtime configuration
and execution order. It can load or solve the required model, construct a
baseline, project designs, perform any target-fitting optimisation or
external-projection fixed point, create derivations, persist named
projections, and generate results.

Some directories also contain optional `setup.yaml` and `setup.py` files.
Setup is only a convenience for generating standard simulation-layer CSVs,
optimisation-target CSVs, ordered design YAMLs, and chartpack YAMLs. It never
generates a run script, documentation, maintained controls, parameters, or
results. Running setup always replaces all files it declares for generation.

After those standard resources exist, the setup files may be deleted. The run
script continues to work and clients may maintain the layers, designs,
chartpacks, and other resources directly.

## Typical use

1. Install the Python G-Cubed version named in the build README.
2. Regenerate the model definition if the SYM source changed.
3. Optionally edit `setup.yaml` and run `python setup.py` to regenerate its
   declared standard resources.
4. Review the documented `CLIENT CONFIGURATION` in the applicable run script.
5. Run `python run_baseline.py`, `python run_experiment.py`,
   `python run_optimisation.py`, or `python run_fixed_point.py`.

Every run command creates its results folder and uses the standard G-Cubed
logger configuration. `setup.py` is the deliberate no-log exception.

For the ownership rules and complete workflow, see
[How to set up experiments and baselines](<../../../docs/How to set up experiments and baselines.md>).
For examples across the active builds, see the
[199 simulation reference experiments](<../../../docs/199 simulation reference experiments.md>).
