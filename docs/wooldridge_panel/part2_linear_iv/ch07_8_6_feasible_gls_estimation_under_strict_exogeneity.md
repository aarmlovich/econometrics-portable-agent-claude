# Feasible GLS Estimation under Strict Exogeneity

> Pages: 191-192

When  $E(\mathbf{u}_i\mathbf{u}_i') \neq \sigma^2\mathbf{I}_T$ , it is reasonable to consider a feasible GLS analysis rather than a pooled OLS analysis. In Chapter 10 we will cover a particular FGLS analysis after we introduce unobserved components panel data models. With large N and small T, nothing precludes an FGLS analysis in the current setting. However, we must remember that FGLS is not even guaranteed to produce consistent, let alone efficient, estimators under Assumptions POLS.1 and POLS.2. Unless  $\Omega = E(\mathbf{u}_i\mathbf{u}_i')$  is a diagonal matrix, Assumption POLS.1 should be replaced with the strict exogeneity assumption (7.6). (Problem 7.7 covers the case when  $\Omega$  is diagonal.) Sometimes we are

{192}------------------------------------------------

willing to assume strict exogeneity in static and finite distributed lag models. As we saw earlier, it cannot hold in models with lagged  $y_{it}$ , and it can fail in static models or distributed lag models if there is feedback from  $y_{it}$  to future  $\mathbf{z}_{it}$ .