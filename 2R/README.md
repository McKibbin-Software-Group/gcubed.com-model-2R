# Model version 2R

2 Region / 2 sector symmetric model of the USA and the Rest of the World. The model is symmetric in the sense that the rest of the world has been altered to match the USA.

## Model stability

The log and linear versions of this model are stable.

## Historical build log through to model build 164

## Update 166 

New monetary regimes

## Update 165

starting databases in 2010

## Update 161

incorporate forward looking money rules	with weight mrule_f

## Update 152

new variiables added for differetn definiiation for nominal growth in the money rule

## Update 151

adjustment of import prices so PRIM exludes tariffs

## Update 150

wage of v=government employees fixed in real terms

## Update 149

syncronisation of all G-Cubed versions

## Update 148

IMQT edflatedby PRID insted of PRIM to ensure TBAL is in te correct unitsUpdate 147
PRIM redefined to be net of tariff import price index

## Update 146

GDPR redefined to net out tariff revenue from the value ofimports

## Update 145

all model versions synchronized and data updated

## Update 144

PMR replaced PMQ in   IMQT

## Update  143

data updates

## Update 142

modprod now starts in 2010 because initial productrivity gaps are from actaul data in 2010.Update 141

sector specific share of forward and backward looking firms

## Update 140

Price deflator for imports change to deflate by	PRIM
new equations for IMQT; PRIM; GDPR; PGDP; Update 137
lower elasticity of subsitution in output level in Gas utilities and
gas extraction

## Update 136

Swap percentage BTA for unit tax version BCT
lower coal substitution elasticities
new US IO table without coal into coal

## Update 135

Add full-dimensioned BTA variable

## Update 134tc

Data for Austalia refined for 2014-2016

## Update 133tc

reduce potential growth to 1.4% from 1.8%
reduce real interest rate r0 to 3.6% ; rate of time pref stays at 2.2%

## Update v132tc

Replace TCAR with two variables, TCP and TCAX, to work around 
linearization issues.  TCP is a shock to price equations that is 
a nonlinear function of the real carbon tax and must be computed
outside the model.  TCAX is the real carbon tax itself (same as
previous use of TCAX) but it is now only used in revenue 
calculations.

## Update v131

new data GTAP9, OECDEO98, UN trade 15, energy 15
baseyear for calibration 2011
forecast year 2016

## Update v130

carbon coeeficients redefned to be CO2 coefficients

## Update v129a

replacing TCAI and TCEX with TCAR and -TCAR
TCAR dimensionaility changed to (goods,regions)

## Update v129

implementation of a new capital controls targeting regime through targeting of the
real exchange rate relative to the US (initially just China).

## Update2 v125 - v128 experiments on data revisions

## Update v124

data revisions based on Larry's complete data update 7/7/15 -
most changes in developing country aggregations

## Update v123

major update incorporating a series of updates from version 115 including

* data revisions

* parameter revisions

* sectoral adjustment costs of capital changed from 4 to:
  * 1 for crude oil extraction
  * 1 for gas extraction
  * 15 for mining

* d/f substitution change from:
  * 0.5 to 1.5 for petroleum refining
  * 0.5 to 1.5 for crude oil
  * 0.2 to 1.5 for gas extraction
  * 2.0 to 0.9 for non-durable manufaturing

* sigma_o changed
  * 1.0014 to 0.5 for mining
  * 0.5 to 1.0044 for non-durable manufacturing

* sigma_e changed
  * 0.2 to    0.8            for electric utilities
  * 0.5 to    0.9325         for gas utilities
  * 0.5 to    1.1474         for mining
  * 0.5 to    0.670909311    for agriculture
  * 0.5 to    0.8045         for durable manufacturing
  * 0.5 to    1.0            for non-durable manufacturing

* sigma_m changed
  * 1.0 to     2.7654        for mining
  * 1.0 to     2.36149       for services

* sigma_oR for the US changed from 1.0 to 1.1 which is the same as other countries

* mrule_ex change to -10 from 0 for China and -0.1 for LDC and EEB

* SHEF redefined as sector by region to accommodate Yiyong iterator

* SHK added for sector by region capital efficiency shock

* SHY redefined to sector by region rathern than region by sector

* SHSR defined as increase in sectoral input demand

## Update v115

EXNA, IMNA and TBNA dropped to areduce definitiations of trade variables

## Update v114a

  PBAL defined in own GDP a new variable PBAG added to the govt
budget constraint so payment to foreigners through PBAL can come from governments
  PBAL=PBAG or from the private sector PBAG=0 (default assumption)

## Update: v114

with sector specific adjustment costs and increase in adjustment cost for mining from 4 to 15 iceberg transaction costs in trade

## Update: v113

Reintroduce the changes to the money rule and IMPX from v110.

## Update: v112

Reintroduce the PRID change to match the version of the 
model used in the first draft of the fiscal paper (which had 
GOVT and the PRID change).

## Update: v111

Support disaggregation of the electric sector by splitting
goods into more classes to handle the fact that generation
is not traded, just total electricity.

Remove the changes from v110 and the PRID change from v109
to facilitate comparison with the model used in the original 
version of the CES paper (which had GOVT but not the change
to PRID).

## Update: v110

New monetary rule with the actual policy rate (INTN) adjusting 
gradually towards a desired policy rate (INPN). 

New variable IMPX added to each equation for IMP to allow an 
exogenous switch of imports by country i towards country j 
away from country k. If used the total of IMP shocks for a 
country MUST sum to zero.

## Update: v109

GOVT added as the sum of both GCET+GOVL*exp(WAGE-PRID)
PRID defined to be the sum of PRP rather than PRD to avoid
problem with carbon tax accountingUpdate: v108
Increment version number to reflect the difference between
Warwick's original v107, which did not include the change in
v102 and had invert set to 1 instead of 0.

## Update: v107

Crude oil and gas separated as in v101-A.  Total profit PRFT
defined so revenue can be passed through the nonlinear algorithm
if needed.

## Update: v106

Taxes not dropped from IO tables in data build.

## Update: v105

New notation with LDC replaced by ROW, rest of OECD replaced by rest of advanced economies.

## Update: v103-v104

Warwick's internal revisions associated with updating of the
data programs.

## Update: v102

Adjustment to TCAX and TCAR so that the real tax, TCAX (usually
entered as shock) is converted to a nominal tax, TCAR, before
it enters the PRD equations.

## Update: v101-B

Due to problems with the Japanese IO table, the changes from
v101-A were not used and the split was reimplemented in v107.
However, for a time there were parallel versions of the model
with and without the split of oil and gas.  During that period,
the emissions coefficients on the old sectoral split were
changed as described below.  Since v101-A was never used,
the main development branch became v101-B.

No changes in the code or data but major refinements to the
way emission coefficients are calculated in Setparsym2.ox.
The coefficient on crude oil and gas extraction (5) was
replaced with separate coeefficients on gas utilities (2)
and petroleum refining (3).

## Update: v101-A

Increment version number due to split of crude oil and gas into
two separate sectors.  The old sector 5 becomes crude oil (5) and
natural gas extraction (6).  Mining becomes sector 7, Agriculture
becomes sector 8, and Forestry is merged into Agriculture and
Wood Products during data construction.

## Update: v100

Compute emissions from OUY-EXQ instead of OUG+IMQ-EXQ.  Using
OUY is consistent with measuring emissions at the individual
input level.  Using OUG+IMQ is not because OUY is not equal to
OUG+IMQ (since OUY is an Armington function of OUG and IMQ).

## Update: v99

No changes in the code or data but major refinements to the
baseline via productivity projections in cycle. Increment
the version number for clarity.

## Update: v98

Revise input-output data to eliminate GTAP's very large flow of
coal into the US sector G-Cubed uses for refined petroleum.  W
Without the change, there was a large flow of coal into refining
and an accompanying flow of refined products into electricity
which is inconsistent with actual US IO tables.  Now the coal
goes straight to electricity.

## Update: v97

Integrate v95 code that allows TAXE to incorporate nonlinear
effects by computing it outside the model and then inserting
it exogenously.  The original and new versions can be switched
via an optional module.

## Update: v96

Merge in TITCH changes from version 92.1.  Note that v95 is
a separate branch with other changes and will need to be merged
in later in v97.

## Update: v94

Create new price PRS, which is the pre-tax version of PRY,
in preparation for sector-specific unit taxes.  Use it to
simplify equations where PRY/(1+TAX) used to appear.  Segregate
equations where sector-specific taxes appear to allow variants
with and without them.  Also, expand TITC to differ by sector.

## Update: April 7, 2010

new baseyear 2006
GTAP v7 data
new country definitions for Europe and Russia
parameter eufor weighting european countries in some versions

## Updated July 2008

sector specific aeei
aeei in consumption
new labgrow = 1.5%
new time preference = 2.5%
yield curve risk premium RISR added
total stock market value
