# The Limiting Distribution of the 2SLS Coefficient Vector

> Pages: 118-120

We can derive the limiting distribution of the 2SLS coefficient vector using an argument similar to that used in Section 3.1.3 for OLS. In this case, let  $V_i \equiv \begin{bmatrix} X'_i & \hat{s}_i \end{bmatrix}'$  denote the vector of regressors in the 2SLS second

<span id="page-118-0"></span><sup>&</sup>lt;sup>11</sup>See, e.g., the preface to Borjas (2005).

{119}------------------------------------------------

stage, equation [\(4.1.9\)](#page-105-0). The 2SLS estimator can then be written

$$\hat{\Gamma}_{2SLS} \equiv \left[\sum_{i} V_{i} V_{i}'\right]^{-1} \sum_{i} V_{i} \mathbf{Y}_{i},$$

where <sup>0</sup> 0 is the corresponding coe¢ cient vector. Note that

$$\hat{\Gamma}_{2SLS} = \Gamma + \left[ \sum_{i} V_i V_i' \right]^{-1} \sum_{i} V_i [\eta_i + \rho(\mathbf{s}_i - \hat{\mathbf{s}}_i)]$$

$$= \Gamma + \left[ \sum_{i} V_i V_i' \right]^{-1} \sum_{i} V_i \eta_i$$
(4.2.1)

where the second equality comes from the fact that the Örst-stage residuals, (s<sup>i</sup> s^i), are orthogonal to V<sup>i</sup> in the sample. The limiting distribution of the 2SLS coe¢ cient vector is therefore the limiting distribution of [ P i ViV 0 i <sup>1</sup> P i Vi<sup>i</sup> . This quantity is a little harder to work with than the corresponding OLS quantity, because the regressors in this case involve estimated Ötted values, s^<sup>i</sup> . A Slutsky-type argument shows, however, that we get the same limiting distribution replacing estimated Ötted values with the corresponding population Ötted values (i.e., replacing s^<sup>i</sup> with [X<sup>0</sup> <sup>i</sup><sup>10</sup> + 11z<sup>i</sup> ]). It therefore follows that ^ <sup>2</sup>SLS has an asymptotically normal distribution, with probability limit , and a covariance matrix estimated consistently by [ P i ViV 0 i 1 -P i ViV 0 i 2 i P i ViV 0 i 1 . This is a sandwich formula like the one for OLS standard errors (White, 1982). As with OLS, if <sup>i</sup> is conditionally homoskedastic given covariates and instruments, the consistent covariance matrix estimator simpliÖes to [ P i ViV 0 i 1 2 .

There is little new here, but there is one tricky point. It seems natural to construct 2SLS estimates manually by Örst estimating the Örst stage [\(4.1.4a\)](#page-102-1) and then plugging the Ötted values into equation [\(4.1.9\)](#page-105-0) and estimating this by OLS. Thatís Öne as far as the coe¢ cient estimates go, but the resulting standard errors will be incorrect. Conventional regression software does not know that you are trying to construct a 2SLS estimate. The residual variance estimator that goes into the standard formulas will therefore be incorrect. When constructing standard errors, the software will estimate the residual variance of the equation you estimate by OLS in the second stage:

$$Y_i - [\alpha' X_i + \rho \hat{s}_i] = [\eta_i + \rho(S_i - \hat{s}_i)],$$

replacing the coe¢ cients with the corresponding estimates. The correct residual variance estimator, however, uses the original endogenous regressor to construct residuals and not the Örst-stage Ötted values, s^<sup>i</sup> . In other words, the residual you want is y<sup>i</sup> [ <sup>0</sup>X<sup>i</sup> + s<sup>i</sup> ] = <sup>i</sup> , so as to consistently estimate 2 , and not <sup>i</sup> + (s<sup>i</sup> s^i). Although this problem is easy to Öx (you can construct the appropriate residual variance estimator in a separate calculation), software designed for 2SLS gets this right automatically, and may help

{120}------------------------------------------------

you avoid other common 2SLS mistakes.