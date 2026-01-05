# **10.6.3** Testing for Serial Correlation

> Pages: 294-296

Under Assumption FD.3, the errors  $e_{it} \equiv \Delta u_{it}$  should be serially uncorrelated. We can easily test this assumption given the pooled OLS residuals from regression (10.65). Since the strict exogeneity assumption holds, we can apply the simple form of the test in Section 7.8. The regression is based on T-2 time periods:

{295}------------------------------------------------

$$\hat{e}_{it} = \hat{\rho}_1 \hat{e}_{i,t-1} + error_{it}, \qquad t = 3, 4, \dots, T; i = 1, 2, \dots, N$$
 (10.71)

The test statistic is the usual t statistic on r^1. With T ¼ 2 this test is not available, nor is it necessary. With T ¼ 3, regression (10.71) is just a cross section regression because we lose the t ¼ 1 and t ¼ 2 time periods.

If the idiosyncratic errors fuit: t ¼ 1; 2; ... ; Tg are uncorrelated to begin with, feit: t ¼ 2; 3; ... ; Tg will be autocorrelated. In fact, under Assumption FE.3 it is easily shown that Corrðeit; ei;t<sup>1</sup>Þ¼:5. In any case, a finding of significant serial correlation in the eit warrants computing the robust variance matrix for the FD estimator.

Example 10.6 (continued): We test for AR(1) serial correlation in the first-differenced equation by regressing e^it on e^i;t<sup>1</sup> using the year 1989. We get r^<sup>1</sup> ¼ :237 with t statistic ¼ 1.76. There is marginal evidence of positive serial correlation in the first differences Duit. Further, r^<sup>1</sup> ¼ :237 is very different from r<sup>1</sup> ¼ :5, which is implied by the standard random and fixed effects assumption that the uit are serially uncorrelated.

An alternative to computing robust standard errors and test statistics is to use an FDGLS analysis under the assumption that Eðeie<sup>0</sup> <sup>i</sup> j xiÞ is a constant ðT 1Þ ðT 1Þ matrix. We omit the details, as they are similar to the FEGLS case in Section 10.5.5. As with FEGLS, we could impose structure on Eðuiu<sup>0</sup> iÞ, such as a stable, homoskedastic AR(1) model, and then derive Eðeie<sup>0</sup> <sup>i</sup>Þ in terms of a small set of parameters.

# 10.6.4 Policy Analysis Using First Differencing

First differencing a structural equation with an unobserved effect is a simple yet powerful method of program evaluation. Many questions can be addressed by having a two-year panel data set with control and treatment groups available at two points in time.

In applying first differencing, we should difference all variables appearing in the structural equation to obtain the estimating equation, including any binary indicators indicating participation in the program. The estimates should be interpreted in the orginal equation because it allows us to think of comparing different units in the cross section at any point in time, where one unit receives the treatment and the other does not.

In one special case it does not matter whether the policy variable is differenced. Assume that T ¼ 2, and let progit denote a binary indicator set to one if person i was in the program at time t. For many programs, progi<sup>1</sup> ¼ 0 for all i: no one participated in the program in the initial time period. In the second time period, progi<sup>2</sup> is unity for those who participate in the program and zero for those who do not. In this one case, Dprogi ¼ progi2, and the first-differenced equation can be written as

{296}------------------------------------------------

$$\Delta y_{i2} = \theta_2 + \Delta \mathbf{z}_{i2} \gamma + \delta_1 prog_{i2} + \Delta u_{i2}$$
(10.72)

The effect of the policy can be obtained by regressing the change in y on the change in z and the policy indicator. When Dz<sup>i</sup><sup>2</sup> is omitted, the estimate of d<sup>1</sup> from equation (10.72) is the difference-in-differences (DID) estimator (see Problem 10.4): ^d<sup>1</sup> <sup>¼</sup> <sup>D</sup>ytreat <sup>D</sup>ycontrol . This is similar to the DID estimator from Section 6.3—see equation (6.32)—but there is an important difference: with panel data, the differences over time are for the same cross section units.

If some people participated in the program in the first time period, or if more than two periods are involved, equation (10.72) can give misleading answers. In general, the equation that should be estimated is

$$\Delta y_{it} = \xi_t + \Delta \mathbf{z}_{it} \mathbf{y} + \delta_1 \Delta prog_{it} + \Delta u_{it}$$
(10.73)

where the program participation indicator is differenced along with everything else, and the x<sup>t</sup> are new period intercepts. Example 10.6 is one such case. Extensions of the model, where progit appears in other forms, are discussed in Chapter 11.

# 10.7 Comparison of Estimators