# Inference

> Pages: 291-294

In Section 10.1 we used differencing to eliminate the unobserved effect ci with T ¼ 2. We now study the differencing transformation in the general case of model (10.41). For completeness, we state the first assumption as follows:

assumption FD.1: Same as Assumption FE.1.

We emphasize that the model and the interpretation of *b* are exactly as in Section 10.5. What differs is our method for estimating *b*.

Lagging the model (10.41) one period and subtracting gives

$$\Delta y_{it} = \Delta \mathbf{x}_{it} \boldsymbol{\beta} + \Delta u_{it}, \qquad t = 2, 3, \dots, T$$
 (10.63)

where Dyit ¼ yit yi;t1, Dxit ¼ xit xi;t1, and Duit ¼ uit ui;t1. As with the FE transformation, this first-differencing transformation eliminates the unobserved effect ci. In differencing we lose the first time period for each cross section: we now have T 1 time periods for each i, rather than T. If we start with T ¼ 2, then, after differencing, we arrive at one time period for each cross section: Dyi<sup>2</sup> ¼ Dxi2*b* þ Dui2.

Equation (10.63) makes it clear that the elements of xit must be time varying (for at least some cross section units); otherwise Dxit has elements that are identically zero for all i and t. Also, while the intercept in the original equation gets differenced away, equation (10.63) contains changes in time dummies if xit contains time dummies. In the T ¼ 2 case, the coefficient on the second-period time dummy becomes the intercept in the differenced equation. If we difference the general equation (10.43) we get

$$\Delta y_{it} = \theta_2(\Delta d z_t) + \dots + \theta_T(\Delta d T_t) + (\Delta d z_t) \mathbf{z}_i \gamma_2 + \dots + (\Delta d T_t) \mathbf{z}_i \gamma_T + \Delta \mathbf{w}_{it} \boldsymbol{\delta} + \Delta u_{it}$$
(10.64)

{292}------------------------------------------------

The parameters  $\theta_1$  and  $\gamma_1$  are not identified because they disappear from the transformed equation, just as with fixed effects.

The first-difference (FD) estimator,  $\hat{\beta}_{FD}$ , is the pooled OLS estimator from the regression

$$\Delta y_{it} \text{ on } \Delta \mathbf{x}_{it}, \qquad t = 2, \dots, T; i = 1, 2, \dots, N$$
 (10.65)

Under Assumption FD.1, pooled OLS estimation of the first-differenced equations will be consistent because

$$E(\Delta \mathbf{x}_{it}'\Delta u_{it}) = 0, \qquad t = 2, 3, \dots, T$$
(10.66)

Therefore, Assumption POLS.1 from Section 7.8 holds. In fact, strict exogeneity holds in the first-differenced equation:

$$E(\Delta u_{it} \mid \Delta \mathbf{x}_{i2}, \Delta \mathbf{x}_{i3}, \dots, \Delta \mathbf{x}_{iT}) = 0, \qquad t = 2, 3, \dots, T$$

which means the FD estimator is actually unbiased conditional on X.

To arrive at assumption (10.66) we clearly can get by with an assumption weaker than Assumption FD.1. The key point is that assumption (10.66) fails if  $u_{it}$  is correlated with  $\mathbf{x}_{i,t-1}$ ,  $\mathbf{x}_{it}$ , or  $\mathbf{x}_{i,t+1}$ , and so we just assume that  $\mathbf{x}_{is}$  is uncorrelated with  $u_{it}$  for all t and s.

For completeness, we state the rank condition for the FD estimator:

ASSUMPTION FD.2: 
$$\operatorname{rank}\left(\sum_{t=2}^{T} \operatorname{E}(\Delta \mathbf{x}_{it}' \Delta \mathbf{x}_{it})\right) = K.$$

In practice, Assumption FD.2 rules out time-constant explanatory variables and perfect collinearity among the time-varying variables.

Assuming the data have been ordered as we discussed earlier, first differencing is easy to implement provided we keep track of which transformed observations are valid and which are not. Differences for observation numbers 1, T+1, 2T+1,  $3T+1,\ldots$ , and (N-1)T+1 should be set to missing. These observations correspond to the first time period for every cross section unit in the original data set; by definition, there is no first difference for the t=1 observations. A little care is needed so that differences between the first time period for unit i+1 and the last time period for unit i are not treated as valid observations. Making sure these are set to missing is easy when a year variable or time period dummies have been included in the data set.

One reason to prefer the FD estimator to the FE estimator is that FD is easier to implement without special software. Are there statistical reasons to prefer FD to FE? Recall that, under Assumptions FE.1–FE.3, the fixed effects estimator is asymp-

{293}------------------------------------------------

totically efficient in the class of estimators using the strict exogeneity assumption FE.1. Therefore, the first difference estimator is less efficient than fixed effects under Assumptions FE.1–FE.3. Assumption FE.3 is key to the efficiency of FE. It assumes homoskedasticity and no serial correlation in  $u_{it}$ . Assuming that the  $\{u_{it}: t = 1, 2, ..., T\}$  are serially uncorrelated may be too strong. An alternative assumption is that the first difference of the idiosyncratic errors,  $\{e_{it} \equiv \Delta u_{it}, t = 2, ..., T\}$ , are serially uncorrelated (and have constant variance):

ASSUMPTION FD.3:  $E(\mathbf{e}_i \mathbf{e}_i' | \mathbf{x}_{i1}, \dots, \mathbf{x}_{iT}, c_i) = \sigma_e^2 \mathbf{I}_{T-1}$ , where  $\mathbf{e}_i$  is the  $(T-1) \times 1$  vector containing  $e_{it}$ ,  $t = 2, \dots, T$ .

Under Assumption FD.3 we can write  $u_{it} = u_{i,t-1} + e_{it}$ , so that no serial correlation in the  $e_{it}$  implies that  $u_{it}$  is a random walk. A random walk has substantial serial dependence, and so Assumption FD.3 represents an opposite extreme from Assumption FE.3.

Under Assumptions FD.1–FD.3 it can be shown that the FD estimator is most efficient in the class of estimators using the strict exogeneity assumption FE.1. Further, from the pooled OLS analysis in Section 7.8,

$$\operatorname{Avar}(\hat{\boldsymbol{\beta}}_{FD}) = \hat{\sigma}_e^2 (\Delta \mathbf{X}' \Delta \mathbf{X})^{-1}$$
(10.67)

where  $\hat{\sigma}_e^2$  is a consistent estimator of  $\sigma_e^2$ . The simplest estimator is obtained by computing the OLS residuals

$$\hat{\boldsymbol{e}}_{it} = \Delta y_{it} - \Delta \mathbf{x}_{it} \hat{\boldsymbol{\beta}}_{FD} \tag{10.68}$$

from the pooled regression (10.65). A consistent estimator of  $\sigma_e^2$  is

$$\hat{\sigma}_e^2 = [N(T-1) - K]^{-1} \sum_{i=1}^N \sum_{t=2}^T \hat{e}_{it}^2$$
(10.69)

which is the usual error variance estimator from regression (10.65). These equations show that, under Assumptions FD.1–FD.3, the usual OLS standard errors from the first difference regression (10.65) are asymptotically valid.

Unlike in the FE regression (10.48), the denominator in equation (10.69) is correctly obtained from regression (10.65). Dropping the first time period appropriately captures the lost degrees of freedom (N of them).

Under Assumption FD.3, all statistics reported from the pooled regression on the first-differenced data are asymptotically valid, including *F* statistics based on sums of squared residuals.

{294}------------------------------------------------

#### 10.6.2 Robust Variance Matrix

If Assumption FD.3 is violated, then, as usual, we can compute a robust variance matrix. The estimator in equation (7.26) applied in this context is

$$\operatorname{Avar}(\hat{\boldsymbol{\beta}}_{FD}) = (\Delta \mathbf{X}' \Delta \mathbf{X})^{-1} \left( \sum_{i=1}^{N} \Delta \mathbf{X}_{i}' \hat{\mathbf{e}}_{i} \hat{\mathbf{e}}_{i}' \Delta \mathbf{X}_{i} \right) (\Delta \mathbf{X}' \Delta \mathbf{X})^{-1}$$
(10.70)

where  $\Delta \mathbf{X}$  denotes the  $N(T-1) \times K$  matrix of stacked first differences of  $\mathbf{x}_{it}$ .

Example 10.6 (FD Estimation of the Effects of Job Training Grants): We now estimate the effect of job training grants on log(scrap) using first differencing. Specifically, we use pooled OLS on

$$\Delta \log(scrap_{it}) = \delta_1 + \delta_2 d89_t + \beta_1 \Delta grant_{it} + \beta_2 \Delta grant_{i,t-1} + \Delta u_{it}$$

Rather than difference the year dummies and omit the intercept, we simply include an intercept and a dummy variable for 1989 to capture the aggregate time effects. If we were specifically interested in the year effects from the structural model (in levels), then we should difference those as well.

The estimated equation is

$$\Delta \log(\hat{s}crap) = -.091 - .096 \ d89 - .223 \ \Delta grant - .351 \ \Delta grant_{-1}$$

$$(.091) \quad (.125) \qquad (.131) \qquad (.235)$$

$$[.088] \quad [.111] \qquad [.128] \qquad [.265]$$

$$R^2 = .037$$

where the usual standard errors are in parentheses and the robust standard errors are in brackets. We report  $R^2$  here because it has a useful interpretation: it measures the amount of variation in the growth in the scrap rate that is explained by  $\Delta grant$  and  $\Delta grant_{-1}$  (and d89). The estimates on grant and  $grant_{-1}$  are fairly similar to the fixed effects estimates, although grant is now statistically more significant than  $grant_{-1}$ . The usual F test for joint significance of  $\Delta grant$  and  $\Delta grant_{-1}$  is 1.53 with p-value = .222.