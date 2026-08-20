"""Generate this simulation's declared setup artefacts."""

from pathlib import Path

from gcubed.experiments import generate_setup_artefacts


def main() -> None:
    """Generate standard layers, ordered designs, and chartpacks."""
    generate_setup_artefacts(Path(__file__))


if __name__ == "__main__":
    main()
