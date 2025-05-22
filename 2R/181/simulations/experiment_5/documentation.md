This experiment uses unconstrained optimal control to determine the potential output growth projections that are consistent with achieving target inflation.

Determine the constant adjustment to make to the projections for potential output (ROGY) to ensure
all regions achieve their target inflation rate in the long run.

The optimal control experiment uses a least-squares search for the potential output constant adjustment in each region that ensures  consumer price inflation (`INFL`) in each region settles at 2.5% by 2100.

The experiment folder contains the CSV files required to do the optimal adjustment of the inflation target projections:

* design.csv - the design file
* target.csv - the targets file
* controls.csv - the controls file

The design file simply specifies that the controls.csv file is the simulation layer being used. In this case it is `ROGY(USA)`, the potential growth rate in the USA region and `ROGY(ROW)`, the potential growth rate in the rest of the World.

The targets files is similar in structure to a simulation layer CSV file. It has a row for each variable being targeted and a column for each of the years in which it is being targeted. Note that the endogenous variables do not need to be targeted in every year through to the last projection year. In this case it is `INFL(USA)`, consumer price inflation in the USA region and `INFL(ROW)`, consumer price inflation in the rest of the World.

The optimisation behaviour uses a least-squares minimisation routine to drive the targeted variables as close as possible to the targets. Deviations in each year are equally weighted in this example. Optimisation is done over the parameters of a polynomial function that is fitted to the control variables. The optimisation is unconstrained. The polynomial degree is set to 0 to force the adjustment to the `ROGY` control projections to be a constant value for each region.
