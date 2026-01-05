# The Dummy Variable Regression

> Pages: 284-290

So far we have viewed the  $c_i$  as being unobservable random variables, and for most applications this approach gives the appropriate interpretation of  $\beta$ . Traditional

{285}------------------------------------------------

approaches to fixed effects estimation view the ci as parameters to be estimated along with *b*. In fact, if Assumption FE.2 is changed to its finite sample version, rankðX€ <sup>0</sup> X€Þ ¼ K, then the model under Assumptions FE.1–FE.3 satisfies the Gauss-Markov assumptions conditional on X.

If the ci are parameters to estimate, how would we estimate each ci along with *b* ? One possibility is to define N dummy variables, one for each cross section observation: dni ¼ 1 if n ¼ i, dni ¼ 0 if n0 i. Then, run the pooled OLS regression

$$y_{it}$$
 on  $dI_i, d2_i, \dots, dN_i, \mathbf{x}_{it}, \qquad t = 1, 2, \dots, T; i = 1, 2, \dots, N$  (10.57)

Then, c^<sup>1</sup> is the coefficient on d1i, c^<sup>2</sup> is the coefficient on d2i, and so on.

It is a nice exercise in least squares mechanics—in particular, partitioned regression (see Davidson and MacKinnon, 1993, Section 1.4)—to show that the estimator of *b* obtained from regression (10.57) is, in fact, the fixed effects estimator. This is why ^*b*FE is sometimes referred to as the dummy variable estimator. Also, the residuals from regression (10.57) are identical to the residuals from regression (10.48). One benefit of regression (10.57) is that it produces the appropriate estimate of s<sup>2</sup> <sup>u</sup> because it uses NT N K ¼ NðT 1Þ K as the degrees of freedom. Therefore, if it can be done, regression (10.57) is a convenient way to carry out fixed effects analysis under Assumptions FE.1–FE.3.

There is an important difference between the <sup>c</sup>^<sup>i</sup> and ^*b*FE. We already know that ^*b*FE is consistent with fixed T as N ! y. This is not the case with the c^i. Each time a new cross section observation is added, another ci is added, and information does not accumulate on the ci as N ! y. Each c^<sup>i</sup> is an unbiased estimator of ci when the ci are treated as parameters, at least if we maintain Assumption FE.1 and the finite sample analogue of Assumption FE.2. When we add Assumption FE.3, the Gauss-Markov assumptions hold (conditional on X ), and c^1; c^2; ... ; c^<sup>N</sup> are best linear unbiased conditional on X. (The c^<sup>i</sup> give practical examples of estimators that are unbiased but not consistent.)

Econometric software that employs fixed effects usually suppresses the ''estimates'' of the ci, although an overall intercept is often reported. The overall intercept is either for an arbitrary cross section unit or, more commonly, for the average of the c^<sup>i</sup> across i.

Sometimes it is useful to obtain the c^<sup>i</sup> even when regression (10.57) is infeasible. Using the OLS first-order conditions, each c^<sup>i</sup> can be shown to be

$$\hat{c}_i = \bar{y}_i - \bar{\mathbf{x}}_i \hat{\boldsymbol{\beta}}_{FE}, \qquad i = 1, 2, \dots, N$$
(10.58)

After obtaining the c^i, the sample average, sample standard deviation, and quantiles can be obtained to get some idea of how much heterogeneity is in the population.

{286}------------------------------------------------

(For example: Is the population distribution of ci spread out or tightly centered about its mean? Is the distribution symmetric?) With large T, the c^<sup>i</sup> can be precise enough to learn something about the distribution of ci. With small T, the c^<sup>i</sup> can contain substantial noise. Under the classical linear model assumptions (which require, in addition to Assumptions FE.1–FE.3, normality of the uit), we can test the equality of the ci using a standard F test for T of any size. [The degrees of freedom are N 1 and NðT 1Þ K.] Unfortunately, the properties of this test as N ! y with T fixed are unknown without the normality assumption.

Generally, we should view the fact that the dummy variable regression (10.57) produces ^*b*FE as the coefficient vector on <sup>x</sup>it as a coincidence. While there are other unobserved effects models where ''estimating'' the unobserved effects along with the vector *b* results in a consistent estimator of *b*, there are many cases where this approach leads to trouble. As we will see in Part IV, many nonlinear panel data models with unobserved effects suffer from an incidental parameters problem, where estimating the incidental parameters, ci, along with *b* produces an inconsistent estimator of *b*.

# 10.5.4 Serial Correlation and the Robust Variance Matrix Estimator

Recall that the FE estimator is consistent and asymptotically normal under Assumptions FE.1 and FE.2. But without Assumption FE.3, expression (10.54) gives an improper variance matrix estimator. While heteroskedasticity in uit is always a potential problem, serial correlation is likely to be more important in certain applications. When applying the FE estimator, it is important to remember that nothing rules out serial correlation in fuit: t ¼ 1; ... ; Tg. While it is true that the observed serial correlation in the composite errors, vit ¼ ci þ uit, is dominated by the presence of ci, there can also be serial correlation that dies out over time. Sometimes, fuitg can have very strong serial dependence, in which case the usual FE standard errors obtained from expression (10.54) can be very misleading. This possibility tends to be a bigger problem with large T. (As we will see, there is no reason to worry about serial correlation in uit when T ¼ 2.)

Testing the idiosyncratic errors, fuitg, for serial correlation is somewhat tricky. A key point is that we cannot estimate the uit; because of the time demeaning used in FE, we can only estimate the time-demeaned errors, u€it. As shown in equation (10.52), the time-demeaned errors are negatively correlated if the uit are uncorrelated. When T ¼ 2, u€<sup>i</sup><sup>1</sup> ¼ u€<sup>i</sup><sup>2</sup> for all i, and so there is perfect negative correlation. This result shows that for T ¼ 2 it is pointless to use the u€it to test for any kind of serial correlation pattern.

{287}------------------------------------------------

When  $T \ge 3$ , we can use equation (10.52) to determine if there is serial correlation in  $\{u_{it}\}$ . Naturally, we use the fixed effects residuals,  $\hat{u}_{it}$ . One simplification is obtained by applying Problem 7.4: we can ignore the estimation error in  $\beta$  in obtaining the asymptotic distribution of any test statistic based on sample covariances and variances. In other words, it is as if we are using the  $\ddot{u}_{it}$ , rather than the  $\hat{u}_{it}$ . The test is complicated by the fact that the  $\{\ddot{u}_{it}\}$  are serially correlated under the null hypothesis. There are two simple possibilities for dealing with this. First, we can just use any two time periods (say, the last two), to test equation (10.52) using a simple regression. In other words, run the regression

$$\hat{\boldsymbol{u}}_{iT}$$
 on  $\hat{\boldsymbol{u}}_{i,T-1}, \qquad i=1,\ldots,N$ 

and use  $\hat{\delta}$ , the coefficient on  $\hat{u}_{i,T-1}$ , along with its standard error, to test  $H_0$ :  $\delta = -1/(T-1)$ , where  $\delta = \operatorname{Corr}(\ddot{u}_{i,T-1},\ddot{u}_{iT})$ . Under Assumptions FE.1–FE.3, the usual t statistic has an asymptotic normal distribution. (It is trivial to make this test robust to heteroskedasticity.)

Alternatively, we can use more time periods if we make the t statistic robust to arbitrary serial correlation. In other words, run the pooled OLS regression

$$\hat{u}_{it}$$
 on  $\hat{u}_{i,t-1}$ ,  $t = 3, ..., T; i = 1, ..., N$ 

and use the fully robust standard error for pooled OLS; see equation (7.26). It may seem a little odd that we make a test for serial correlation robust to serial correlation, but this need arises because the null hypothesis is that the time-demeaned errors are serially correlated. This approach clearly does not produce an optimal test against, say, AR(1) correlation in the  $u_{it}$ , but it is very simple and may be good enough to indicate a problem.

If we find serial correlation, we should, at a minimum, adjust the asymptotic variance matrix estimator and test statistics. Fortunately, we can apply the results from Chapter 7 directly to obtain a fully robust asymptotic variance matrix estimator. Let  $\hat{\mathbf{u}}_i \equiv \ddot{\mathbf{y}}_i - \ddot{\mathbf{X}}_i \hat{\boldsymbol{\beta}}_{FE}$ , i = 1, 2, ..., N denote the  $T \times 1$  vectors fixed effects residuals. Applying equation (7.26), the robust variance matrix estimator of  $\hat{\boldsymbol{\beta}}_{FE}$  is

$$\operatorname{Ava\hat{\mathbf{r}}}(\hat{\boldsymbol{\beta}}_{FE}) = (\ddot{\mathbf{X}}'\ddot{\mathbf{X}})^{-1} \left( \sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \hat{\mathbf{u}}_{i} \hat{\mathbf{u}}_{i}' \ddot{\mathbf{X}}_{i} \right) (\ddot{\mathbf{X}}'\ddot{\mathbf{X}})^{-1}$$
(10.59)

which was suggested by Arellano (1987) and follows from the general results of White (1984, Chapter 6). The robust variance matrix estimator is valid in the presence of any heteroskedasticity or serial correlation in  $\{u_{it}: t = 1, ..., T\}$ , provided

{288}------------------------------------------------

that T is small relative to N. [Remember, equation (7.26) is justified for fixed T,  $N \to \infty$  asymptotics.] The robust standard errors are obtained as the square roots of the diagonal elements of the matrix (10.59), and matrix (10.59) can be used as the  $\hat{\mathbf{V}}$  matrix in constructing Wald statistics. Unfortunately, the sum of squared residuals form of the F statistic is no longer asymptotically valid when Assumption FE.3 fails.

Example 10.5 (continued): We now report the robust standard errors for the log(scrap) equation along with the usual FE standard errors:

$$\log(\hat{s}crap) = -.080 \ d88 - .247 \ d89 - .252 \ grant - .422 \ grant_{-1}$$

$$(.109) \qquad (.133) \qquad (.151) \qquad (.210)$$

$$[.096] \qquad [.193] \qquad [.140] \qquad [.276]$$

The robust standard error on grant is actually smaller than the usual standard error, while the robust standard error on  $grant_{-1}$  is larger than the usual one. As a result, the absolute value of the t statistic on  $grant_{-1}$  drops from about 2 to just over 1.5.

Remember, with fixed T as  $N \to \infty$ , the robust standard errors are just as valid asymptotically as the nonrobust ones when Assumptions FE.1–FE.3 hold. But the usual standard errors and test statistics may be better behaved under Assumptions FE.1–FE.3 if N is not very large relative to T, especially if  $u_{it}$  is normally distributed.

#### 10.5.5 Fixed Effects GLS

Recall that Assumption FE.3 can fail for two reasons. The first is that the conditional variance matrix does not equal the unconditional variance matrix:  $E(\mathbf{u}_i\mathbf{u}_i' | \mathbf{x}_i, c_i) \neq E(\mathbf{u}_i\mathbf{u}_i')$ . Even if  $E(\mathbf{u}_i\mathbf{u}_i' | \mathbf{x}_i, c_i) = E(\mathbf{u}_i\mathbf{u}_i')$ , the unconditional variance matrix may not be scalar:  $E(\mathbf{u}_i\mathbf{u}_i') \neq \sigma_u^2\mathbf{I}_T$ , which means either that the variance of  $u_{it}$  changes with t or, probably more importantly, that there is serial correlation in the idiosyncratic errors. The robust variance matrix (10.59) is valid in any case.

Rather than compute a robust variance matrix for the FE estimator, we can instead relax Assumption FE.3 to allow for an unrestricted, albeit constant, conditional covariance matrix. This is a natural route to follow if the robust standard errors of the fixed effects estimator are too large to be useful and if there is evidence of serial dependence or a time-varying variance in the  $u_{it}$ .

ASSUMPTION FEGLS.3:  $E(\mathbf{u}_i \mathbf{u}_i' | \mathbf{x}_i, c_i) = \Lambda$ , a  $T \times T$  positive definite matrix.

Under Assumption FEGLS.3,  $E(\ddot{\mathbf{u}}_i\ddot{\mathbf{u}}_i'|\ddot{\mathbf{x}}_i) = E(\ddot{\mathbf{u}}_i\ddot{\mathbf{u}}_i')$ . Further, using  $\ddot{\mathbf{u}}_i = \mathbf{Q}_T\mathbf{u}_i$ ,

$$E(\ddot{\mathbf{u}}_i\ddot{\mathbf{u}}_i') = \mathbf{Q}_T E(\mathbf{u}_i\mathbf{u}_i')\mathbf{Q}_T = \mathbf{Q}_T \Lambda \mathbf{Q}_T$$
(10.60)

{289}------------------------------------------------

which has rank T-1. The deficient rank in expression (10.60) causes problems for the usual approach to GLS, because the variance matrix cannot be inverted. One way to proceed is to use a *generalized inverse*. A much easier approach—and one that turns out to be algebraically identical—is to drop one of the time periods from the analysis. It can be shown (see Im, Ahn, Schmidt, and Wooldridge, 1999) that it does not matter which of these time periods is dropped: the resulting GLS estimator is the same.

For concreteness, suppose we drop time period T, leaving the equations

$$\ddot{y}_{i1} = \ddot{\mathbf{x}}_{i1} \boldsymbol{\beta} + \ddot{u}_{i1} 
\vdots 
\ddot{y}_{i,T-1} = \ddot{\mathbf{x}}_{i,T-1} \boldsymbol{\beta} + \ddot{u}_{i,T-1}$$
(10.61)

So that we do not have to introduce new notation, we write the system (10.61) as equation (10.49), with the understanding that now  $\ddot{\mathbf{y}}_i$  is  $(T-1) \times 1$ ,  $\ddot{\mathbf{X}}_i$  is  $(T-1) \times K$ , and  $\ddot{\mathbf{u}}_i$  is  $(T-1) \times 1$ . Define the  $(T-1) \times (T-1)$  positive definite matrix  $\mathbf{\Omega} \equiv \mathrm{E}(\ddot{\mathbf{u}}_i\ddot{\mathbf{u}}_i')$ . We do not need to make the dependence of  $\mathbf{\Omega}$  on  $\mathbf{\Lambda}$  and  $\mathbf{Q}_T$  explicit; the key point is that, if no restrictions are made on  $\mathbf{\Lambda}$ , then  $\mathbf{\Omega}$  is also unrestricted.

To estimate  $\Omega$ , we estimate  $\boldsymbol{\beta}$  by fixed effects in the first stage. After dropping the last time period for each i, define the  $(T-1) \times 1$  residuals  $\hat{\mathbf{u}}_i = \ddot{\mathbf{y}}_i - \ddot{\mathbf{X}}_i \hat{\boldsymbol{\beta}}_{FE}$ , i = 1, 2, ..., N. A consistent estimator of  $\Omega$  is

$$\hat{\mathbf{\Omega}} = N^{-1} \sum_{i=1}^{N} \hat{\mathbf{u}}_i \hat{\mathbf{u}}_i' \tag{10.62}$$

The fixed effects GLS (FEGLS) estimator is defined by

$$\hat{\boldsymbol{\beta}}_{FEGLS} = \left(\sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \hat{\mathbf{\Omega}}^{-1} \ddot{\mathbf{X}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \hat{\mathbf{\Omega}}^{-1} \ddot{\mathbf{y}}_{i}\right)$$

where  $\ddot{\mathbf{X}}_i$  and  $\ddot{\mathbf{y}}_i$  are defined with the last time period dropped. For consistency of FEGLS, we replace Assumption FE.2 with a new rank condition:

ASSUMPTION FEGLS.2: rank 
$$E(\ddot{\mathbf{X}}_{i}'\mathbf{\Omega}^{-1}\ddot{\mathbf{X}}_{i}) = K$$
.

Under Assumptions FE.1 and FEGLS.2, the FEGLS estimator is consistent. When we add Assumption FEGLS.3, the asymptotic variance is easy to estimate:

$$Avar(\hat{\boldsymbol{\beta}}_{FEGLS}) = \left(\sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \hat{\mathbf{\Omega}}^{-1} \ddot{\mathbf{X}}_{i}\right)^{-1}$$

{290}------------------------------------------------

The sum of squared residual statistics from FGLS can be used to test multiple restrictions. Note that G = T - 1 in the F statistic in equation (7.53).

The FEGLS estimator was proposed by Kiefer (1980) when the  $c_i$  are treated as parameters. As we just showed, the procedure consistently estimates  $\beta$  when we view  $c_i$  as random and allow it to be arbitrarily correlated with  $\mathbf{x}_{it}$ .

The FEGLS estimator is asymptotically no less efficient than the FE estimator under Assumption FEGLS.3, even when  $\mathbf{\Lambda} = \sigma_u^2 \mathbf{I}_T$ . Generally, if  $\mathbf{\Lambda} \neq \sigma_u^2 \mathbf{I}_T$ , FEGLS is more efficient than FE, but this conclusion relies on the large-N, fixed-T asymptotics. Unfortunately, because FEGLS still uses the fixed effects transformation to remove  $c_i$ , it can have large asymptotic standard errors if the matrices  $\ddot{\mathbf{X}}_i$  have columns close to zero.

Rather than allowing  $\Omega$  to be an unrestricted matrix, we can impose restrictions on  $\Lambda$  that imply  $\Omega$  has a restricted form. For example, Bhargava, Franzini, and Narendranatahn (1982) (BFN) assume that  $\{u_{it}\}$  follows a stable, homoskedastic AR(1) model. This assumption implies that  $\Omega$  depends on only three parameters,  $\sigma_c^2$ ,  $\sigma_u^2$ , and the AR coefficient,  $\rho$ , no matter how large T is. BFN obtain a transformation that eliminates the unobserved effect,  $c_i$ , and removes the serial correlation in  $u_{ii}$ . They also propose estimators of  $\rho$ , so that feasible GLS is possible. Modeling  $\{u_{it}\}$  as a specific time series process is attractive when N is not very large relative to T, as estimating an unrestricted covariance matrix for  $\ddot{\mathbf{u}}_i$  [the  $(T-1) \times 1$  vector of timedemeaned errors] without large N can lead to poor finite-sample performance of the FGLS estimator. However, the only general statements we can make concern fixed- $T, N \to \infty$  asymptotics. In this scenario, the FGLS estimator that uses unrestricted  $\Omega$  is no less asymptotically efficient than an FGLS estimator that puts restrictions on  $\Omega$ . And, if the restrictions on  $\Omega$  are incorrect, the estimator that imposes the restrictions is less asymptotically efficient. Therefore, on theoretical grounds, we prefer an estimator of the type in equation (10.62).