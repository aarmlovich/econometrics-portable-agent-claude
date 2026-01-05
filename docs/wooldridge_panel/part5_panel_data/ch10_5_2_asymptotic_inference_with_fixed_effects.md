# Asymptotic Inference with Fixed Effects

> Pages: 281-284

Without further assumptions the FE estimator is not necessarily the most efficient estimator based on Assumption FE.1. The next assumption ensures that FE is efficient.

ASSUMPTION FE.3: 
$$E(\mathbf{u}_i \mathbf{u}_i' \mid \mathbf{x}_i, c_i) = \sigma_u^2 \mathbf{I}_T$$
.

Assumption FE.3 is identical to Assumption RE.3a. Since  $E(\mathbf{u}_i | \mathbf{x}_i, c_i) = \mathbf{0}$  by Assumption FE.1, Assumption FE.3 is the same as saying  $Var(\mathbf{u}_i | \mathbf{x}_i, c_i) = \sigma_u^2 \mathbf{I}_T$  if Assumption FE.1 also holds. As with Assumption RE.3a, it is useful to think of Assumption FE.3 as having two parts. The first is that  $E(\mathbf{u}_i\mathbf{u}_i' | \mathbf{x}_i, c_i) = E(\mathbf{u}_i\mathbf{u}_i')$ , which is standard in system estimation contexts [see equation (7.50)]. The second is that the unconditional variance matrix  $E(\mathbf{u}_i\mathbf{u}_i')$  has the special form  $\sigma_u^2\mathbf{I}_T$ . This implies that the idiosyncratic errors  $u_{it}$  have a constant variance across t and are serially uncorrelated, just as in assumptions (10.28) and (10.29).

{282}------------------------------------------------

Assumption FE.3, along with Assumption FE.1, implies that the *unconditional* variance matrix of the composite error  $\mathbf{v}_i = c_i \mathbf{j}_T + \mathbf{u}_i$  has the random effects form. However, without Assumption RE.3b,  $\mathrm{E}(\mathbf{v}_i \mathbf{v}_i' | \mathbf{x}_i) \neq \mathrm{E}(\mathbf{v}_i \mathbf{v}_i')$ . While this result matters for inference with the RE estimator, it has no bearing on a fixed effects analysis.

It is not obvious that Assumption FE.3 has the desired consequences of ensuring efficiency of fixed effects and leading to simple computation of standard errors and test statistics. Consider the demeaned equation (10.46). Normally, for pooled OLS to be relatively efficient, we require that the  $\{\ddot{u}_{it}: t=1,2,\ldots,T\}$  be homoskedastic across t and serially uncorrelated. The variance of  $\ddot{u}_{it}$  can be computed as

$$E(\ddot{u}_{it}^{2}) = E[(u_{it} - \bar{u}_{i})^{2}] = E(u_{it}^{2}) + E(\bar{u}_{i}^{2}) - 2E(u_{it}\bar{u}_{i})$$

$$= \sigma_{u}^{2} + \sigma_{u}^{2}/T - 2\sigma_{u}^{2}/T = \sigma_{u}^{2}(1 - 1/T)$$
(10.51)

which verifies (unconditional) homoskedasticity across t. However, for  $t \neq s$ , the covariance between  $\ddot{u}_{it}$  and  $\ddot{u}_{is}$  is

$$E(\ddot{u}_{it}\ddot{u}_{is}) = E[(u_{it} - \bar{u}_i)(u_{is} - \bar{u}_i)] = E(u_{it}u_{is}) - E(u_{it}\bar{u}_i) - E(u_{is}\bar{u}_i) + E(\bar{u}_i^2)$$

$$= 0 - \sigma_u^2/T - \sigma_u^2/T + \sigma_u^2/T = -\sigma_u^2/T < 0$$

Combining this expression with the variance in equation (10.51) gives, for all  $t \neq s$ ,

$$\operatorname{Corr}(\ddot{\boldsymbol{u}}_{it}, \ddot{\boldsymbol{u}}_{is}) = -1/(T-1) \tag{10.52}$$

which shows that the time-demeaned errors  $\ddot{u}_{it}$  are negatively serially correlated. (As T gets large, the correlation tends to zero.)

It turns out that, because of the nature of time demeaning, the serial correlation in the  $\ddot{u}_{it}$  under Assumption FE.3 causes only minor complications. To find the asymptotic variance of  $\hat{\beta}_{FE}$ , write

$$\sqrt{N}(\hat{\boldsymbol{\beta}}_{FE} - \boldsymbol{\beta}) = \left(N^{-1} \sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \ddot{\mathbf{X}}_{i}\right)^{-1} \left(N^{-1/2} \sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \mathbf{u}_{i}\right)$$

where we have used the important fact that  $\ddot{\mathbf{X}}_i'\ddot{\mathbf{u}}_i = \mathbf{X}_i'\mathbf{Q}_T\mathbf{u}_i = \ddot{\mathbf{X}}_i'\mathbf{u}_i$ . Under Assumption FE.3,  $\mathrm{E}(\mathbf{u}_i\mathbf{u}_i' | \ddot{\mathbf{X}}_i) = \sigma_u^2\mathbf{I}_T$ . From the system OLS analysis in Chapter 7 it follows that

$$\sqrt{N}(\hat{\boldsymbol{\beta}}_{FE} - \boldsymbol{\beta}) \sim \text{Normal}(\boldsymbol{0}, \sigma_u^2 [\text{E}(\ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i)]^{-1})$$

and so

$$\operatorname{Avar}(\hat{\boldsymbol{\beta}}_{FE}) = \sigma_u^2 [\operatorname{E}(\ddot{\mathbf{X}}_i' \ddot{\mathbf{X}}_i)]^{-1} / N \tag{10.53}$$

{283}------------------------------------------------

Given a consistent estimator  $\hat{\sigma}_u^2$  of  $\sigma_u^2$ , equation (10.53) is easily estimated by also replacing  $E(\ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i)$  with its sample analogue  $N^{-1}\sum_{i=1}^N\ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i$ :

$$Avar(\hat{\beta}_{FE}) = \hat{\sigma}_u^2 \left( \sum_{i=1}^N \ddot{\mathbf{X}}_i' \ddot{\mathbf{X}}_i \right)^{-1} = \hat{\sigma}_u^2 \left( \sum_{i=1}^N \sum_{t=1}^T \ddot{\mathbf{x}}_{it}' \ddot{\mathbf{x}}_{it} \right)^{-1}$$
(10.54)

The asymptotic standard errors of the fixed effects estimates are obtained as the square roots of the diagonal elements of the matrix (10.54).

Expression (10.54) is very convenient because it looks just like the usual OLS variance matrix estimator that would be reported from the pooled OLS regression (10.48). However, there is one catch, and this comes in obtaining the estimator  $\hat{\sigma}_u^2$  of  $\sigma_u^2$ . The errors in the transformed model are  $\ddot{u}_{it}$ , and these errors are what the OLS residuals from regression (10.48) estimate. Since  $\sigma_u^2$  is the variance of  $u_{it}$ , we must use a little care.

To see how to estimate  $\sigma_u^2$ , we use equation (10.51) summed across t:  $\sum_{t=1}^T \mathrm{E}(\ddot{u}_{it}^2) = (T-1)\sigma_u^2$ , and so  $[N(T-1)]^{-1}\sum_{i=1}^N \sum_{t=1}^T \mathrm{E}(\ddot{u}_{it}^2) = \sigma_u^2$ . Now, define the **fixed effects residuals** as

$$\hat{\mathbf{u}}_{it} = \ddot{\mathbf{y}}_{it} - \ddot{\mathbf{x}}_{it}\hat{\boldsymbol{\beta}}_{FE}, \qquad t = 1, 2, \dots, T; i = 1, 2, \dots, N$$
 (10.55)

which are simply the OLS residuals from the pooled regression (10.48). Then a consistent estimator of  $\sigma_u^2$  under Assumptions FE.1–FE.3 is

$$\hat{\sigma}_{y}^{2} = SSR/[N(T-1) - K] \tag{10.56}$$

where SSR =  $\sum_{i=1}^{N} \sum_{t=1}^{T} \hat{u}_{it}^2$ . The subtraction of K in the denominator of equation (10.56) does not matter asymptotically, but it is standard to make such a correction. In fact, under Assumptions FE.1–FE.3, it can be shown that  $\hat{\sigma}_u^2$  is actually an unbiased estimator of  $\sigma_u^2$  conditional on  $\mathbf{X}$  (and therefore unconditionally as well).

Pay careful attention to the denominator in equation (10.56). This is not the degrees of freedom that would be obtained from regression (10.48). In fact, the usual variance estimate from regression (10.48) would be SSR/(NT-K), which has a probability limit less than  $\sigma_u^2$  as N gets large. The difference between SSR/(NT-K) and equation (10.56) can be substantial when T is small.

The upshot of all this is that the usual standard errors reported from the regression (10.48) will be too small on average because they use the incorrect estimate of  $\sigma_u^2$ . Of course, computing equation (10.56) directly is pretty trivial. But, if a standard regression package is used after time demeaning, it is perhaps easiest to adjust the usual standard errors directly. Since  $\hat{\sigma}_u$  appears in the standard errors, each standard error

{284}------------------------------------------------

is simply multiplied by the factor  $\{(NT - K)/[N(T - 1) - K]\}^{1/2}$ . As an example, if N = 500, T = 3, and K = 10, the correction factor is about 1.227.

If an econometrics package has an option for explicitly obtaining fixed effects estimates using panel data,  $\sigma_u^2$  will be properly estimated, and you do not have to worry about adjusting the standard errors. Many software packages also compute an estimate of  $\sigma_c^2$ , which is useful to determine how large the variance of the unobserved component is to the variance of the idiosyncratic component. Given  $\hat{\boldsymbol{\beta}}_{FE}$ ,  $\hat{\sigma}_v^2 = (NT - K^{-1}) \sum_{i=1}^{N} \sum_{t=1}^{T} (y_{it} - \mathbf{x}_{tt} \hat{\boldsymbol{\beta}}_{FE})^2$  is a consistent estimator of  $\sigma_v^2 = \sigma_c^2 + \sigma_u^2$ , and so a consistent estimator of  $\sigma_c^2$  is  $\hat{\sigma}_v^2 - \hat{\sigma}_u^2$ . (See Problem 10.14 for a discussion of why the estimated variance of the unobserved effect in a fixed effects analysis is generally larger than that for a random effects analysis.)

Example 10.5 (FE Estimation of the Effects of Job Training Grants): Using the data in JTRAIN1.RAW, we estimate the effect of job training grants using the fixed effects estimator. The variable *union* has been dropped because it does not vary over time for any of the firms in the sample. The estimated equation with standard errors is

$$\log(\hat{s}crap) = -.080 \ d88 - .247 \ d89 - .252 \ grant - .422 \ grant_{-1}$$

$$(.109) \qquad (.133) \qquad (.151) \qquad (.210)$$

Compared with the random effects, the grant is estimated to have a larger effect, both contemporaneously and lagged one year. The t statistics are also somewhat more significant with fixed effects.

Under Assumptions FE.1–FE.3, multiple restrictions are most easily tested using an F statistic, provided the degrees of freedom are appropriately computed. Let  $SSR_{ur}$  be the unrestricted SSR from regression (10.48), and let  $SSR_r$  denote the restricted sum of squared residuals from a similar regression, but with Q restrictions imposed on  $\beta$ . Then

$$F = \frac{(SSR_r - SSR_{ur})}{SSR_{ur}} \cdot \frac{[N(T-1) - K]}{Q}$$

is approximately F distributed with Q and N(T-1)-K degrees of freedom. (The precise statement is that  $Q \cdot F \sim \chi_Q^2$  as  $N \to \infty$  under  $H_0$ .) When this equation is applied to Example 10.5, the F statistic for joint significance of grant and  $grant_{-1}$  is F=2.23, with p-value = .113.