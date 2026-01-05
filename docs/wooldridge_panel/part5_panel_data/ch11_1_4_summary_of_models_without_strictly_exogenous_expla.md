# Summary of Models without Strictly Exogenous Explanatory Variables

> Pages: 325-326

Before leaving this section, it is useful to summarize the general approach we have taken to estimate models that do not satisfy strict exogeneity: first, a transformation is used to eliminate the unobserved effect; next, instruments are chosen for the endogenous variables in the transformed equation. In the previous subsections we have stated various assumptions, but we have not catalogued them as in Chapter 10, largely because there are so many variants. For example, in Section 11.1.3 we saw that different assumptions lead to different sets of instruments. The importance of carefully stating assumptions—such as (11.2), (11.34), (11.36), and (11.37)—cannot be overstated.

First differencing, which allows for more general violations of strict exogeneity than the within transformation, has an additional benefit: it is easy to test the firstdifferenced equation for serial correlation after pooled 2SLS estimation. The test suggested in Problem 8.10 is immediately applicable with the change in notation that all variables are in first differences. Arellano and Bond (1991) propose tests for serial correlation in the original errors, fuit: t ¼ 1; ... ; Tg; the tests are based on GMM estimation. When the original model has a lagged dependent variable, it makes more sense to test for serial correlation in fuitg: models with lagged dependent variables are usually taken to have errors that are serially uncorrelated, in which case the firstdifferenced errors must be serially correlated. As Arellano and Bond point out, serial 

{326}------------------------------------------------

correlation in fuitg generally invalidates using lags of yit as IVs in the first-differenced equation. Of course, one might ask why we would be interested in r<sup>1</sup> in model (11.4) if fuitg is generally serially correlated.