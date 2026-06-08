# Setup YAML Configuration Reference

This document describes the YAML configuration blocks embedded near the top of
the baseline and experiment setup scripts in the model repositories. These
scripts live in experiment folders under each model build's `simulations`
directory, for example:

```text
models/<model>/<build>/simulations/baseline/setup_baseline.py
models/<model>/<build>/simulations/<experiment>/setup_experiment.py
```

The normal workflow is to edit only the YAML block, then run the setup script to
regenerate the README, documentation, chartpack, design files, layer data files,
and run script for that simulation.

## Baseline Setup

Baseline setup scripts use `BASELINE_CONFIGURATION_YAML` and require these
top-level sections:

```yaml
baseline:
files:
chartpack:
run_baseline:
```

### `baseline`

Controls model configuration lookup and overwrite behavior.

```yaml
baseline:
  model_configuration_file_name: configuration.csv
  overwrite_generated_files: true
```

- `model_configuration_file_name`: file name under the model build directory.
- `overwrite_generated_files`: when `true`, the setup script replaces generated
  files. When `false`, it raises an error if a generated file already exists.

### `files`

Names the generated baseline files in the `baseline` simulation folder.

```yaml
files:
  readme_file_name: README.md
  documentation_file_name: documentation.md
  chartpack_file_name: chartpack.csv
  run_script_file_name: run_baseline.py
```

### `chartpack`

Defines the baseline report title, optional report year window, and chart
variables. Chart variables are configured by prefix and selectors only. Do not
write full variable names such as `GDPR(USA)`.

```yaml
chartpack:
  title: Baseline
  first_result_year:
  last_result_year:
  charts:
    - variable_prefix: INFL
      selectors:
        regions: all
```

- `first_result_year` and `last_result_year` may be blank to leave that side of
  the chart window unconstrained.
- `charts` is a list. Each entry can be a single series definition or, in newer
  scripts, a chart with a `series` list.
- `variable_prefix` is matched against model metadata. Some setup scripts also
  support derived regional prefixes such as `GDPRGROWTH` and `UNRATE`.
- `selectors` narrows resolved variables. Common selectors are `regions`,
  `sectors`, and `goods`; trade-focused scripts may also use metadata dimensions
  such as `goods_o`, `dest`, `orig`, and `sec_std`.

### `run_baseline`

Controls defaults inserted into the generated `run_baseline.py`.

```yaml
run_baseline:
  force_model_to_resolve: true
  show_baseline_charts: true
  solved_model_file_name: solved_model.joblib
```

- `force_model_to_resolve`: when `true`, the generated run script solves the
  model even if a saved solved model exists.
- `show_baseline_charts`: opens or displays final report output when supported.
- `solved_model_file_name`: joblib file written under the baseline results
  folder.

## Standard Experiment Setup

Most experiment setup scripts use `EXPERIMENT_CONFIGURATION_YAML` with these
top-level sections:

```yaml
experiment:
baseline:
layers:
chartpack:
run:
```

Newer multi-design scripts add `simulation_designs` between `baseline` and
`layers`. Optimisation scripts replace `layers` with `controls` and `targets`.
Trade-policy experiments may add selector dimensions and value-path types needed
for bilateral trade instruments and phase-in schedules.

### `experiment`

Names the scenario and generated files.

```yaml
experiment:
  scenario_name: A temporary increase in the USA inflation target
  run_script_file_name: run_experiment.py
  readme_file_name: README.md
  documentation_file_name: documentation.md
  design_file_name: design.csv
  chartpack_file_name: chartpack.csv
  report_template_file_name: chart-template.html
  overwrite_generated_files: true
```

Common fields:

- `model_configuration_file_name`: optional model configuration file name when
  the setup script does not hardcode `configuration.csv`.
- `scenario_name`: user-facing scenario name for generated docs and reports.
- `scenario_summary`: optional longer scenario description used by some
  generated documentation.
- `run_script_file_name`, `readme_file_name`, `documentation_file_name`,
  `design_file_name`, `chartpack_file_name`: output file names generated into
  the experiment folder.
- `controls_file_name`, `targets_file_name`: optimisation workflow output file
  names generated into the experiment folder.
- `report_template_file_name`: HTML report template under the model build's
  `templates` directory. Present in newer setup scripts.
- `setup_script_file_name`: used by optimisation scripts when generated README
  text needs to refer to the setup script name.
- `overwrite_generated_files`: same behavior as in baseline setup.

### `baseline`

Tells the generated run script where to find, or whether to create, the solved
model used to rebuild baseline projections.

```yaml
baseline:
  results_folder_name: baseline
  solved_model_file_name: solved_model.joblib
  ask_to_solve_model_if_missing: true
  solve_model_if_missing: false
```

- `results_folder_name`: baseline results folder under
  `results/<version>/<build>/`.
- `solved_model_file_name`: saved solved model file in that folder.
- `ask_to_solve_model_if_missing`: if the run script is attached to a terminal,
  ask whether to solve and save the model when the joblib file is missing.
- `solve_model_if_missing`: solve automatically when the joblib file is missing.
  If both solving options are false, the generated run script fails until the
  baseline has been run or the flag is changed.

### `layers`

Defines one or more event layers. Each layer becomes a layer data CSV, and the
design file lists the layers in event order.

```yaml
layers:
  - name: Temporary USA inflation target increase
    data_file_name: adjustments.csv
    event_year: 2024
    description: The USA inflation target is increased by 1 percentage point for three years.
    shocks:
      - variable_prefix: INFX
        variable_type: exo
        selectors:
          regions: [USA]
        value_path:
          type: temporary_constant
          start_year: 2024
          end_year: 2026
          value: 1
```

Common layer fields:

- `id`: required by multi-design scripts so designs can reference layers. Simple
  single-design scripts do not require it.
- `name`: layer name written to the design CSV.
- `data_file_name`: generated CSV containing shock values by year.
- `event_year`: year the model treats as the event for that layer.
- `description`: design-file text explaining the layer.
- `shocks`: list of variable shock definitions.

Common shock fields:

- `variable_prefix`: model variable prefix. Use prefixes only, not full variable
  names.
- `variable_type`: optional metadata check, commonly `exo`.
- `selectors`: dimensions used to resolve all matching variables.
- `value_path`: rule for generating annual values.

### `value_path`

The supported `value_path.type` values depend on the setup script generation.
The setup scripts in this repository family use or support these forms.

```yaml
value_path:
  type: permanent_constant
  start_year: 2024
  value: 1
```

`permanent_constant` writes `value` from `start_year` onward. In newer
scripts, omitted `start_year` defaults to the layer `event_year`.

```yaml
value_path:
  type: temporary_constant
  start_year: 2024
  end_year: 2026
  value: 1
```

`temporary_constant` writes `value` from `start_year` through `end_year`, then
zero outside that period.

```yaml
value_path:
  type: explicit
  values:
    2024: 1
    2025: 0.75
    2026: 0.25
```

Some simple and newer 2A scripts also support `explicit`, where `values` maps
years to values and unspecified output years receive zero.

```yaml
value_path:
  type: constant
  start_year: 2026
  end_year: 2150
  value: -5
  units: percentage points
```

Some trade-policy setup scripts support legacy `constant`, writing `value`
from `start_year` through `end_year`. The optional `units` field is
documentation for readers of the YAML; generated CSVs contain numeric values.

```yaml
value_path:
  type: linear_phase_in
  start_year: 2026
  full_year: 2028
  end_year: 2150
  value: -5
  units: percentage points
```

`linear_phase_in` is a reusable path for any shock that is announced or
introduced gradually, reaches a full value, and then stays at that full value.
It writes zero before `start_year`, moves linearly from zero in `start_year` to
`value` in `full_year`, holds `value` through `end_year`, and writes zero after
`end_year`.

The ART trade-deal experiment uses this path for phased tariff reductions, but
the same pattern can apply to other gradual policy, technology, preference,
risk-premium, productivity, tax, spending, or regulatory shocks. For example,
with `start_year: 2026`, `full_year: 2028`, and `value: -5`, the generated
values are `-1.66667` in 2026, `-3.33333` in 2027, and `-5` from 2028 through
`end_year`.

Use `linear_phase_in` when a shock is phased in over several years but then
remains at the fully implemented level. The setup script should validate that
`start_year <= full_year <= end_year`. The optional `units` field is
documentation for readers of the YAML; generated CSVs contain numeric values.

## Multi-Design Experiments

Multi-design setup scripts add a `simulation_designs` section. Each design
names a generated design CSV and references layer IDs in the intended run order.

```yaml
simulation_designs:
  - key: expectedly_temporary
    name: Expectedly temporary USA inflation target increase
    design_file_name: expectedly_temporary_design.csv
    description: Agents know from the start that the increase is temporary.
    layer_ids:
      - expected_inflation_target_increase
```

- `key`: stable identifier used by the generated run script.
- `name`: user-facing design name.
- `design_file_name`: generated design CSV for that simulation design.
- `description`: explanatory text for generated docs.
- `layer_ids`: ordered list of `layers[].id` values. Event years must be
  weakly increasing in newer 2A setup scripts.

## Optimisation Experiments

The 2A optimisation setup scripts use this top-level shape:

```yaml
experiment:
  controls_file_name: controls.csv
  targets_file_name: targets.csv
baseline:
controls:
targets:
chartpack:
run:
```

### `controls`

Defines exogenous variables adjusted by the optimiser and solver tolerances.

```yaml
controls:
  layer_name: Potential output growth adjustment
  event_year: 2024
  description: Constant additive adjustment to potential output growth targets.
  variable_prefix: ROGY
  variable_type: exo
  selectors:
    regions: all
  first_control_year: 2024
  last_control_year: 2150
  initial_value: 0
  solver_xtol: 0.01
  solver_ftol: 0.01
```

- `layer_name`, `event_year`, and `description` feed the generated design and
  layer data.
- `variable_prefix`, `variable_type`, and `selectors` resolve control rows from
  model metadata.
- `first_control_year` and `last_control_year` define the years written into the
  generated controls CSV.
- `initial_value` seeds the optimiser.
- `solver_xtol` and `solver_ftol` are passed to `scipy.optimize.least_squares`.

### `targets`

Defines target variables and target paths.

```yaml
targets:
  variable_prefix: INFL
  selectors:
    regions: all
  first_target_year: 2030
  last_target_year: 2100
  target_value: 2.5
```

The long-run inflation finetuning setup uses a single `target_value` for every
resolved target variable and target year.

```yaml
targets:
  variable_prefix: YONL
  selectors:
    regions: all
  first_target_year: 2026
  last_target_year: 2050
  values_by_region:
    USA:
      default: 0
    ROW:
      default: -11
      values:
        2026: -1
        2027: -2
```

The labor productivity targeting setup uses `values_by_region`. Each region can
provide a `default` and optional year-specific `values` overrides.

## Chartpack Details

Experiment chartpacks mirror baseline chartpacks but may also request derived
series.

```yaml
chartpack:
  title: Inflation target increase
  first_result_year: 2024
  last_result_year: 2040
  derivations:
    - GDPRGROWTH
    - UNRATE
  charts:
    - variable_prefix: INFX
      selectors:
        regions: all
    - variable_prefix: UNRATE
      selectors:
        regions: all
    - label: Real GDP
      series:
        - variable_prefix: GDPR
          selectors:
            regions: [USA, ROW]
```

- `title`: report title.
- `first_result_year`, `last_result_year`: optional chart window.
- `derivations`: optional list of derived outputs to make available to charts.
  For supported regional derived outputs, the same prefix can be used in
  `charts` with a `regions` selector. The scanned setup scripts use
  `GDPRGROWTH`, `UNRATE`, and, in the labor productivity workflow, `YONL`.
- `UNRATE`: derived regional unemployment rate. To chart it, include `UNRATE`
  in `chartpack.derivations` and add a chart entry with
  `variable_prefix: UNRATE`. The generated run script then asks the derived
  variable subsystem to calculate `UNRATE(region)` rows for the report.
- `charts`: each item is either a direct series definition or a labeled chart
  with a `series` list.
- `selectors: all` selects every available member for that dimension. A scalar
  or list selects specific members.

## `run`

Controls defaults inserted into generated experiment run scripts.

```yaml
run:
  show_final_results: true
```

- `show_final_results`: whether generated report output is displayed when the
  run script finishes.

## Validation Rules And Conventions

- YAML must parse to a mapping and include every top-level section required by
  that setup script.
- Variable names are resolved from prefixes plus selectors. Full variable names
  with parentheses are rejected by the baseline and newer experiment setup
  scripts.
- Selector names must match dimensions available for the selected variable
  prefix in model metadata.
- Year fields are validated against the model projection years in newer 2A
  scripts.
- In newer event-layer scripts, shock `start_year` values cannot be before the
  layer `event_year`.
- Layer IDs must be unique in multi-design scripts.
- Generated file names are relative to the simulation folder containing the
  setup script.
- Results are written under `results/<version>/<build>/<simulation-folder-name>`.

## Minimal Examples

Baseline chartpack entry:

```yaml
chartpack:
  title: Baseline
  first_result_year:
  last_result_year:
  charts:
    - variable_prefix: INFL
      selectors: {regions: all}
```

Single-layer experiment:

```yaml
layers:
  - name: USA inflation target increase
    data_file_name: adjustments.csv
    event_year: 2024
    description: The USA inflation target is permanently increased by 1 percentage point.
    shocks:
      - variable_prefix: INFX
        variable_type: exo
        selectors: {regions: [USA]}
        value_path:
          type: permanent_constant
          start_year: 2024
          value: 1
```

Multi-layer surprise reversal:

```yaml
layers:
  - id: initial_permanent_inflation_target_increase
    name: Initially permanent USA inflation target increase
    data_file_name: initial_permanent_inflation_target_increase.csv
    event_year: 2024
    description: Agents initially expect the increase to remain in place.
    shocks:
      - variable_prefix: INFX
        variable_type: exo
        selectors: {regions: [USA]}
        value_path:
          type: permanent_constant
          start_year: 2024
          value: 1
  - id: surprise_inflation_target_reversal
    name: Surprise reversal of the USA inflation target increase
    data_file_name: surprise_inflation_target_reversal.csv
    event_year: 2027
    description: The increase is unexpectedly reversed.
    shocks:
      - variable_prefix: INFX
        variable_type: exo
        selectors: {regions: [USA]}
        value_path:
          type: permanent_constant
          start_year: 2027
          value: -1
```
