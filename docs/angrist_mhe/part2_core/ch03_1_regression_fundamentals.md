# Regression Fundamentals

> Pages: 37-38

The end of the previous chapter introduces regression models as a computational device for the estimation of treatment-control di§erences in an experiment, with and without covariates. Because the regressor of interest in the class size study discussed in Section [2.3](#page-31-1) was randomly assigned, the resulting estimates have a causal interpretation. In most cases, however, regression is used with observational data. Without the beneÖt of random assignment, regression estimates may or may not have a causal interpretation. We return to the central question of what makes a regression causal later in this chapter.

Setting aside the relatively abstract causality problem for the moment, we start with the mechanical properties of regression estimates. These are universal features of the population regression vector and its sample analog that have nothing to do with a researcherís interpretation of his output. This chapter begins by reviewing these properties, which include:

- (i) the intimate connection between the population regression function and the conditional expectation function
  - (ii) how and why regression coe¢ cients change as covariates are added or removed from the model
  - (iii) the close link between regression and other "control strategies" such as matching

{38}------------------------------------------------

(iv) the sampling distribution of regression estimates