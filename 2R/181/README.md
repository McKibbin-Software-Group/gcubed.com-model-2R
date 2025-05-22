# Overview

This document describes model 2R build 181.

Run the model using Python G-Cubed version 4.0.2.11.

## Simulation experiments

[A number of different example simulation experiments](simulations/README.md) are provided with this model build.

## Changes from model 2R build 180

1. Overhaul of parameter calibration class, moving emissions related parameters to the model's parameter calibration class.

2. Removed btucoef and related energy subsystem from sym files. This is no longer used.

3. Migrated to the new root SYM file naming convention `ggg-model.sym`.

4. Removed redundant `INTL` and `EXCL` variables, using the SYM `lag()` function instead.

5. Added basic report generation to the standard `run_baseline.py` script.
