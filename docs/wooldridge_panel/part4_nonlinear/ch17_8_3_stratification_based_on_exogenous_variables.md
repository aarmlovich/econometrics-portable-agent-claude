# Stratification Based on Exogenous Variables

> Pages: 604-606

When w partitions as ðx; yÞ, where x is exogenous in a sense to be made precise, and stratification is based entirely on x, the standard unweighted estimator on the stratified sample is consistent and asymptotically normal. The sense in which x must be exogenous is that *y*<sup>o</sup> solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \ \mathrm{E}[q(\mathbf{w}, \boldsymbol{\theta}) \mid \mathbf{x}] \tag{17.78}$$

for each possible outcome x. This assumption holds in a variety of contexts with conditioning variables and correctly specified models. For example, as we discussed in Chapter 12, this holds for nonlinear regression when the conditional mean is correctly specified and *y*<sup>o</sup> is the vector of conditional mean parameters; in Chapter 13 we showed that this holds for conditional maximum likelihood when the density of y given x is correct. It also holds in other cases, including quasi-maximum likelihood, which we cover in Chapter 19. One interesting observation is that, in the linear regression model (17.74), the exogeneity of x must be strengthened to Eðu j xÞ ¼ 0.

In the case of VP sampling, selection on the basis of x means that each selection indicator sj is a deterministic function of x. The unweighted M-estimator on the stratified sample, ^*y*u, minimizes

$$\sum_{i=1}^{N} \sum_{j=1}^{J} h_{ij} s_{ij} q(\mathbf{w}_i, \boldsymbol{\theta}) = \sum_{i=1}^{N_0} q(\mathbf{w}_i, \boldsymbol{\theta})$$

{605}------------------------------------------------

Consistency follows from standard M-estimation results if we can show that  $\theta_0$  uniquely solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\theta}} \sum_{j=1}^{J} \mathrm{E}[h_{j} s_{j} q(\mathbf{w}, \boldsymbol{\theta})]$$
 (17.79)

Since  $s_j$  is a function of  $\mathbf{x}$  and  $h_j$  is independent of  $\mathbf{w}$  (and therefore  $\mathbf{x}$ ),  $\mathrm{E}[h_j s_j q(\mathbf{w}, \boldsymbol{\theta}) \,|\, \mathbf{x}] = \mathrm{E}(h_j \,|\, \mathbf{x}) s_j \mathrm{E}[q(\mathbf{w}, \boldsymbol{\theta}) \,|\, \mathbf{x}] = p_j s_j \mathrm{E}[q(\mathbf{w}, \boldsymbol{\theta}) \,|\, \mathbf{x}]$  for each j. By assumption,  $\mathrm{E}[q(\mathbf{w}, \boldsymbol{\theta}) \,|\, \mathbf{x}]$  is minimized at  $\boldsymbol{\theta}_0$  for all  $\mathbf{x}$ , and therefore so is  $p_j s_j \mathrm{E}[q(\mathbf{w}, \boldsymbol{\theta}) \,|\, \mathbf{x}]$  (but probably not uniquely). By iterated expectations it follows that  $\boldsymbol{\theta}_0$  is a solution to equation (17.79). Unlike in the case of the weighted estimator, it no longer suffices to assume that  $\boldsymbol{\theta}_0$  uniquely minimizes  $\mathrm{E}[q(\mathbf{w}, \boldsymbol{\theta})]$ ; we must directly assume  $\boldsymbol{\theta}_0$  is the unique solution to problem (17.79). This assumption could fail if, for example,  $p_j = 0$  for some j—so that we do not observe part of the population at all. (Unlike in the case of the weighted estimator,  $p_j = 0$  for at least some j is allowed for the unweighted estimator, subject to identification holding.) For example, in the context of linear wage regression, we could not identify the return to education if we only sample those with exactly a high school education.

Wooldridge (1999b) shows that the usual asymptotic variance estimators (see Section 12.5) are valid when stratification is based on  $\mathbf{x}$  and we ignore the stratification problem. For example, the usual conditional maximum likelihood analysis holds. In the case of regression, we can use the usual heteroskedasticity-robust variance matrix estimator. Or, if we assume homoskedasticity in the population, the nonrobust form [see equation (12.58)] is valid with the usual estimator of the error variance.

When a generalized conditional information matrix equality holds, and stratification is based on x, Wooldridge (1999b) shows that the unweighted estimator is more efficient than the weighted estimator. The key assumption is

$$E[\nabla_{\theta}q(\mathbf{w}, \boldsymbol{\theta}_{o})'\nabla_{\theta}q(\mathbf{w}, \boldsymbol{\theta}_{o}) \mid \mathbf{x}] = \sigma_{o}^{2}E[\nabla_{\theta}^{2}q(\mathbf{w}, \boldsymbol{\theta}_{o}) \mid \mathbf{x}]$$
(17.80)

for some  $\sigma_0^2 > 0$ . When assumption (17.80) holds and  $\theta_0$  solves equation (17.79), the asymptotic variance of the unweighted M-estimator is smaller than that for the weighted M-estimator. This generalization includes conditional maximum likelihood (with  $\sigma_0^2 = 1$ ) and nonlinear regression under homoskedasticity.

Very similar conclusions hold for standard stratified sampling. One useful fact is that, when stratification is based on  $\mathbf{x}$ , the estimator (17.73) is valid with  $p_j = H_j/Q_j$  (and  $N_0 = N$ ); therefore, we need not compute within-strata variation in the estimated score. The unweighted estimator is consistent when stratification is based on  $\mathbf{x}$  and the usual asymptotic variance matrix estimators are valid. The unweighted

{606}------------------------------------------------

estimator is also more efficient when assumption (17.80) holds. See Wooldridge (2001) for statements of assumptions and proofs of theorems.