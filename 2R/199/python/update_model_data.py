#!/usr/bin/env python3
"""Regenerate model data and independently preview or apply baseline tuning.

Edit only the three settings immediately below.  All work is disabled by
default, so running an unchanged copy of this script is a safe no-op.
"""

from __future__ import annotations

import importlib
import logging
from pathlib import Path
from types import ModuleType
from typing import Any, Callable


# User-editable execution settings.  Tuning modes are: disabled, summary, apply.
UPDATE_DATABASE_IO_TABLES_AND_LABOR_FORCE_GROWTH: bool = False
INTR_TUNING_MODE: str = "apply"
INTX_TUNING_MODE: str = "apply"


LOGGER = logging.getLogger(__name__)
VALID_TUNING_MODES = frozenset({"disabled", "summary", "apply"})


def _validate_execution_settings() -> None:
    """Reject invalid tuning modes before importing either optional package."""

    if type(UPDATE_DATABASE_IO_TABLES_AND_LABOR_FORCE_GROWTH) is not bool:
        raise ValueError(
            "UPDATE_DATABASE_IO_TABLES_AND_LABOR_FORCE_GROWTH must be True or "
            f"False; received {UPDATE_DATABASE_IO_TABLES_AND_LABOR_FORCE_GROWTH!r}."
        )
    for setting_name, value in (
        ("INTR_TUNING_MODE", INTR_TUNING_MODE),
        ("INTX_TUNING_MODE", INTX_TUNING_MODE),
    ):
        if type(value) is not str or value not in VALID_TUNING_MODES:
            choices = ", ".join(repr(mode) for mode in sorted(VALID_TUNING_MODES))
            raise ValueError(
                f"{setting_name} must be one of {choices}; received {value!r}."
            )


def _model_directory() -> Path:
    """Return the model-build directory independently of the working directory."""

    return Path(__file__).resolve().parents[1]


def _load_msgdata_modules() -> tuple[ModuleType, ModuleType, ModuleType] | None:
    """Load msgdata lazily, skipping only absence of its top-level package."""

    try:
        importlib.import_module("msgdata")
    except ModuleNotFoundError as error:
        if error.name == "msgdata":
            return None
        raise

    return (
        importlib.import_module("msgdata.data_configuration"),
        importlib.import_module("msgdata.un"),
        importlib.import_module("msgdata.database"),
    )


def _run_model_data_update(model_directory: Path) -> bool:
    """Run the two public operations behind the data repository's data target."""

    modules = _load_msgdata_modules()
    if modules is None:
        LOGGER.info(
            "Model-data updating was enabled, but msgdata is not available. "
            "The database, IO tables, and productivity-adjusted labour-force "
            "growth rates were not updated."
        )
        return False

    data_configuration_module, un_module, database_module = modules
    version = model_directory.parent.name
    build = model_directory.name
    data_configuration_file = (
        model_directory.parents[2]
        / "data"
        / "configurations"
        / f"data_configuration_{version}_{build}.yaml"
    )
    data_configuration = data_configuration_module.DataConfiguration(
        configuration_file_path=data_configuration_file
    )
    configured_model = data_configuration.model_configuration
    configured_identity = (configured_model.version, configured_model.build)
    expected_identity = (version, build)
    if configured_identity != expected_identity:
        raise ValueError(
            f"Data configuration {data_configuration_file} identifies model "
            f"{configured_identity[0]}/{configured_identity[1]}, expected "
            f"{expected_identity[0]}/{expected_identity[1]}."
        )

    LOGGER.info(
        "Regenerating productivity-adjusted labour-force growth rates for %s/%s.",
        version,
        build,
    )
    un_module.create_productivity_adjusted_labor_supply_growth_projections(
        data_configuration
    )
    LOGGER.info("Regenerating the database and IO tables for %s/%s.", version, build)
    database_module.update_model_data(data_configuration)
    LOGGER.info(
        "Regenerated the database, IO tables, and productivity-adjusted "
        "labour-force growth rates for %s/%s.",
        version,
        build,
    )
    return True


def _load_model_configuration(model_directory: Path) -> Any:
    """Load the refreshed model configuration only when tuning is enabled."""

    module = importlib.import_module("gcubed.model_configuration")
    return module.ModelConfiguration.from_model_directory(
        model_directory,
        validation_profile="baseline_input_generation",
    )


def _run_tuning(model_directory: Path) -> None:
    """Dispatch INTR and INTX modes independently in the required order."""

    if INTR_TUNING_MODE == "disabled" and INTX_TUNING_MODE == "disabled":
        LOGGER.info(
            "INTR tuning is disabled. Set INTR_TUNING_MODE to 'summary' or "
            "'apply' to run it."
        )
        LOGGER.info(
            "INTX tuning is disabled. Set INTX_TUNING_MODE to 'summary' or "
            "'apply' to run it."
        )
        return

    model_configuration = _load_model_configuration(model_directory)
    tuning_module = importlib.import_module("gcubed.tuning")
    operations: tuple[tuple[str, str, Callable[..., Any]], ...] = (
        (
            "INTR",
            INTR_TUNING_MODE,
            tuning_module.tune_real_interest_rates,
        ),
        (
            "INTX",
            INTX_TUNING_MODE,
            tuning_module.tune_monetary_policy_adjustments,
        ),
    )
    for name, mode, operation in operations:
        if mode == "disabled":
            LOGGER.info(
                "%s tuning is disabled. Set %s_TUNING_MODE to 'summary' or "
                "'apply' to run it.",
                name,
                name,
            )
            continue
        summary = operation(model_configuration, mode=mode)
        LOGGER.info(
            "%s tuning completed in %s mode with status: %s",
            name,
            mode,
            getattr(summary, "status", "completed"),
        )
        if mode == "summary":
            LOGGER.info(
                "%s tuning changes were summarized but not applied. Set "
                "%s_TUNING_MODE = 'apply' in this script and rerun it to "
                "apply those changes.",
                name,
                name,
            )


def main() -> int:
    """Run the independently configured data and tuning operations."""

    _validate_execution_settings()
    model_directory = _model_directory()

    if UPDATE_DATABASE_IO_TABLES_AND_LABOR_FORCE_GROWTH:
        _run_model_data_update(model_directory)
    else:
        LOGGER.info(
            "Model-data updating is disabled. Set "
            "UPDATE_DATABASE_IO_TABLES_AND_LABOR_FORCE_GROWTH = True to "
            "regenerate the database, IO tables, and productivity-adjusted "
            "labour-force growth rates."
        )

    _run_tuning(model_directory)
    return 0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    raise SystemExit(main())
