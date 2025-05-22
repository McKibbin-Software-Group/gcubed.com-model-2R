from gcubed.model_parameters.parameters import Parameters
from gcubed.data.database import Database


class Parameters2R181(Parameters):
    """
    This class does customised parameter calibration.
    """

    def __init__(self, database: Database, base_year: int) -> None:
        """

        ### Overview

        No custom parameter calibrations are required by this model version.

        ### Arguments

        `database`: The database used to calibrate the parameters.

        `base_year`: The base year that the database needs to be rebased to before
        calibration of the parameters.

        """
        super().__init__(database=database, base_year=base_year)
