# Robust Asymptotic Variance Matrix

> Pages: 188-191

Because Assumption POLS.3 can be restrictive, it is often useful to obtain a robust estimate of  $\text{Avar}(\hat{\beta})$  that is valid without Assumption POLS.3. We have already seen the general form of the estimator, given in matrix (7.26). In the case of panel data, this estimator is fully robust to arbitrary heteroskedasticity—conditional or unconditional—and arbitrary serial correlation across time (again, conditional or

{189}------------------------------------------------

unconditional). The residuals ^u<sup>i</sup> are the T 1 pooled OLS residuals for cross section observation i. Some statistical packages compute these very easily, although the command may be disguised. Whether a software package has this capability or whether it must be programmed by you, the data must be stored as described earlier: The ðyi; XiÞ should be stacked on top of one another for i ¼ 1; ... ; N.

# 7.8.5 Testing for Serial Correlation and Heteroskedasticity after Pooled OLS

Testing for Serial Correlation It is often useful to have a simple way to detect serial correlation after estimation by pooled OLS. One reason to test for serial correlation is that it should not be present if the model is supposed to be dynamically complete in the conditional mean. A second reason to test for serial correlation is to see whether we should compute a robust variance matrix estimator for the pooled OLS estimator.

One interpretation of serial correlation in the errors of a panel data model is that the error in each time period contains a time-constant omitted factor, a case we cover explicitly in Chapter 10. For now, we are simply interested in knowing whether or not the errors are serially correlated.

We focus on the alternative that the error is a first-order autoregressive process; this will have power against fairly general kinds of serial correlation. Write the AR(1) model as

$$u_t = \rho_1 u_{t-1} + e_t \tag{7.73}$$

where

$$E(e_t \mid \mathbf{x}_t, u_{t-1}, \mathbf{x}_{t-1}, u_{t-2}, \dots) = 0$$
(7.74)

Under the null hypothesis of no serial correlation, r<sup>1</sup> ¼ 0.

One way to proceed is to write the dynamic model under AR(1) serial correlation as

$$y_t = \mathbf{x}_t \boldsymbol{\beta} + \rho_1 u_{t-1} + e_t, \qquad t = 2, \dots, T$$
 (7.75)

where we lose the first time period due to the presence of ut-1. If we can observe the ut, it is clear how we should proceed: simply estimate equation (7.75) by pooled OLS (losing the first time period) and perform a t test on r^1. To operationalize this procedure, we replace the ut with the pooled OLS residuals. Therefore, we run the regression

$$y_{it} \text{ on } \mathbf{x}_{it}, \hat{\mathbf{u}}_{i,t-1}, \qquad t = 2, \dots, T, \ i = 1, \dots, N$$
 (7.76)

and do a standard t test on the coefficient of u^<sup>i</sup>;t-1. A statistic that is robust to arbitrary heteroskedasticity in Varðyt j xt; ut-<sup>1</sup>Þ is obtained by the usual heteroskedasticityrobust t statistic in the pooled regression. This includes Engle's (1982) ARCH model and any other form of static or dynamic heteroskedasticity.

{190}------------------------------------------------

Why is a t test from regression (7.76) valid? Under dynamic completeness, equation (7.75) satisfies Assumptions POLS.1–POLS.3 if we also assume that Varðyt j xt; ut-1Þ is constant. Further, the presence of the generated regressor u^<sup>i</sup>;t-<sup>1</sup> does not affect the limiting distribution of r^<sup>1</sup> under the null because r<sup>1</sup> ¼ 0. Verifying this claim is similar to the pure cross section case in Section 6.1.1.

A nice feature of the statistic computed from regression (7.76) is that it works whether or not x<sup>t</sup> is strictly exogenous. A different form of the test is valid if we assume strict exogeneity: use the t statistic on u^<sup>i</sup>;t-<sup>1</sup> in the regression

$$\hat{u}_{it} \text{ on } \hat{u}_{i,t-1}, \qquad t = 2, \dots, T, \ i = 1, \dots, N$$
 (7.77)

or its heteroskedasticity-robust form. That this test is valid follows by applying Problem 7.4 and the assumptions for pooled OLS with a lagged dependent variable.

Example 7.9 (Athletes' Grade Point Averages, continued): We apply the test from regression (7.76) because cumgpa cannot be strictly exogenous (GPA this term affects cumulative GPA after this term). We drop the variables spring and frstsem from regression (7.76), since these are identically unity and zero, respectively, in the spring semester. We obtain r^<sup>1</sup> ¼ :194 and tr^<sup>1</sup> ¼ 3:18, and so the null hypothesis is rejected. Thus there is still some work to do to capture the full dynamics. But, if we assume that we are interested in the conditional expectation implicit in the estimation, we are getting consistent estimators. This result is useful to know because we are primarily interested in the in-season effect, and the other variables are simply acting as controls. The presence of serial correlation means that we should compute standard errors robust to arbitrary serial correlation (and heteroskedasticity); see Problem 7.10.

Testing for Heteroskedasticity The primary reason to test for heteroskedasticity after running pooled OLS is to detect violation of Assumption POLS.3a, which is one of the assumptions needed for the usual statistics accompanying a pooled OLS regression to be valid. We assume throughout this section that Eðut j xtÞ ¼ 0, t ¼ 1; 2; ... ; T, which strengthens Assumption POLS.1 but does not require strict exogeneity. Then the null hypothesis of homoskedasticity can be stated as Eðu<sup>2</sup> <sup>t</sup> j xtÞ ¼ s2, t ¼ 1; 2; ... ; T.

Under H0, u<sup>2</sup> it is uncorrelated with any function of xit; let hit denote a 1 Q vector of nonconstant functions of xit. In particular, hit can, and often should, contain dummy variables for the different time periods.

From the tests for heteroskedasticity in Section 6.2.4. the following procedure is natural. Let u^<sup>2</sup> it denote the squared pooled OLS residuals. Then obtain the usual Rsquared, R<sup>2</sup> <sup>c</sup> , from the regression

$$\hat{u}_{it}^2 \text{ on } 1, \mathbf{h}_{it}, \qquad t = 1, \dots, T, \ i = 1, \dots, N$$
 (7.78)


{191}------------------------------------------------

The test statistic is  $NTR_c^2$ , which is treated as asymptotically  $\chi_Q^2$  under  $H_0$ . (Alternatively, we can use the usual F test of joint significance of  $\mathbf{h}_{it}$  from the pooled OLS regression. The degrees of freedom are Q and NT - K.) When is this procedure valid?

Using arguments very similar to the cross sectional tests from Chapter 6, it can be shown that the statistic has the same distribution if  $u_{it}^2$  replaces  $\hat{u}_{it}^2$ ; this fact is very convenient because it allows us to focus on the other features of the test. Effectively, we are performing a standard LM test of  $H_0$ :  $\delta = 0$  in the model

$$u_{it}^2 = \delta_0 + \mathbf{h}_{it}\boldsymbol{\delta} + a_{it}, \qquad t = 1, 2, \dots, T \tag{7.79}$$

This test requires that the errors  $\{a_{it}\}$  be appropriately serially uncorrelated and requires homoskedasticity; that is, Assumption POLS.3 must hold in equation (7.79). Therefore, the tests based on nonrobust statistics from regression (7.78) essentially require that  $E(a_{it}^2 | \mathbf{x}_{it})$  be constant—meaning that  $E(u_{it}^4 | \mathbf{x}_{it})$  must be constant under  $H_0$ . We also need a stronger homoskedasticity assumption;  $E(u_{it}^2 | \mathbf{x}_{it}, u_{i,t-1}, \mathbf{x}_{i,t-1}, \ldots) = \sigma^2$  is sufficient for the  $\{a_{it}\}$  in equation (7.79) to be appropriately serially uncorrelated.

A fully robust test for heteroskedasticity can be computed from the pooled regression (7.78) by obtaining a fully robust variance matrix estimator for  $\hat{\delta}$  [see equation (7.26)]; this can be used to form a robust Wald statistic.

Since violation of Assumption POLS.3a is of primary interest, it makes sense to include elements of  $\mathbf{x}_{it}$  in  $\mathbf{h}_{it}$ , and possibly squares and cross products of elements of  $\mathbf{x}_{it}$ . Another useful choice, covered in Chapter 6, is  $\hat{\mathbf{h}}_{it} = (\hat{y}_{it}, \hat{y}_{it}^2)$ , the pooled OLS fitted values and their squares. Also, Assumption POLS.3a requires the unconditional variances  $\mathbf{E}(u_{it}^2)$  to be the same across t. Whether they are can be tested directly by choosing  $\mathbf{h}_{it}$  to have T-1 time dummies.

If heteroskedasticity is detected but serial correlation is not, then the usual heteroskedasticity-robust standard errors and test statistics from the pooled OLS regression (7.69) can be used.