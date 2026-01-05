# Heteroskedasticity and Nonnormality in the Latent Variable Model

> Pages: 542-545

As in the case of probit, both heteroskedasticity and nonnormality result in the Tobit estimator  $\hat{\boldsymbol{\beta}}$  being inconsistent for  $\boldsymbol{\beta}$ . This inconsistency occurs because the derived density of y given  $\mathbf{x}$  hinges crucially on  $y^* \mid \mathbf{x} \sim \text{Normal}(\mathbf{x}\boldsymbol{\beta}, \sigma^2)$ . This nonrobustness of the Tobit estimator shows that data censoring can be very costly: in the absence of censoring  $(y = y^*)$ ,  $\boldsymbol{\beta}$  could be consistently estimated under  $E(u \mid \mathbf{x}) = 0$  [or even  $E(\mathbf{x}'u) = 0$ ].

In corner solution applications, we must remember that the presence of heteroskedasticity or nonnormality in the latent variable model entirely changes the functional forms for  $E(y | \mathbf{x}, y > 0)$  and  $E(y | \mathbf{x})$ . Therefore, it does not make sense to focus only on the inconsistency in estimating  $\boldsymbol{\beta}$ . We should study how departures from the homoskedastic normal assumption affect the estimated partial derivatives of the conditional mean functions. Allowing for heteroskedasticity or nonnormality in

{543}------------------------------------------------

the latent variable model can be useful for generalizing functional form in corner solution applications, and it should be viewed in that light.

Specification tests can be based on the score approach, where the standard Tobit model is nested in a more general alternative. Tests for heteroskedasticity and non-normality in the latent variable equation are easily constructed if the outer product of the form statistic (see Section 13.6) is used. A useful test for heteroskedasticity is obtained by assuming  $Var(u | \mathbf{x}) = \sigma^2 \exp(\mathbf{z}\boldsymbol{\delta})$ , where  $\mathbf{z}$  is a  $1 \times Q$  subvector of  $\mathbf{x}$  ( $\mathbf{z}$  does not include a constant). The Q restrictions  $H_0$ :  $\boldsymbol{\delta} = \mathbf{0}$  can be tested using the LM statistic. The partial derivatives of the log likelihood  $\ell_i(\boldsymbol{\beta}, \sigma^2, \boldsymbol{\delta})$  with respect to  $\boldsymbol{\beta}$  and  $\sigma^2$ , evaluated at  $\boldsymbol{\delta} = \mathbf{0}$ , are given exactly as in equations (16.21) and (16.22). Further, we can show that  $\partial \ell_i/\partial \boldsymbol{\delta} = \sigma^2 \mathbf{z}_i(\partial \ell_i/\partial \sigma^2)$ . Thus the outer product of the score statistic is  $N - SSR_0$  from the regression

1 on 
$$\partial \hat{\ell}_i / \partial \boldsymbol{\beta}$$
,  $\partial \hat{\ell}_i / \partial \sigma^2$ ,  $\hat{\boldsymbol{\sigma}}^2 \mathbf{z}_i (\partial \hat{\ell}_i / \partial \sigma^2)$ ,  $i = 1, \dots, N$ 

where the derivatives are evaluated at the Tobit estimates (the restricted estimates) and  $SSR_0$  is the usual sum of squared residuals. Under  $H_0$ ,  $N-SSR_0 \stackrel{a}{\sim} \chi_Q^2$ . Unfortunately, as we discussed in Section 13.6, the outer product form of the statistic can reject much too often when the null hypothesis is true. If maximum likelihood estimation of the alternative model is possible, the likelihood ratio statistic is a preferable alternative.

We can also construct tests of nonnormality that only require standard Tobit estimation. The most convenient of these are derived as conditional moment tests, which we discussed in Section 13.7. See Pagan and Vella (1989).

It is not too difficult to estimate Tobit models with u heteroskedastic if a test reveals such a problem. For data-censoring applications, it makes sense to directly compare the estimates of  $\beta$  from standard Tobit and Tobit with heteroskedasticity. But when  $E(y | \mathbf{x}, y > 0)$  and  $E(y | \mathbf{x})$  are of interest, we should look at estimates of these expectations with and without heteroskedasticity. The partial effects on  $E(y | \mathbf{x}, y > 0)$  and  $E(y | \mathbf{x})$  could be similar even though the estimates of  $\beta$  might be very different.

As a rough idea of the appropriateness of the Tobit model, we can compare the probit estimates, say  $\hat{\gamma}$ , to the Tobit estimate of  $\gamma = \beta/\sigma$ , namely,  $\hat{\beta}/\hat{\sigma}$ . These will never be identical, but they should not be statistically different. Statistically significant sign changes are indications of misspecification. For example, if  $\hat{\gamma}_j$  is positive and significant but  $\hat{\beta}_j$  is negative and perhaps significant, the Tobit model is probably misspecified.

As an illustration, in Example 15.2, we obtained the probit coefficient on *nwifeinc* as -.012, and the coefficient on *kidslt6* was -.868. When we divide the corresponding

{544}------------------------------------------------

Tobit coefficients by  $\hat{\sigma} = 1{,}122.02$ , we obtain about -.0079 and -.797, respectively. Though the estimates differ somewhat, the signs are the same and the magnitudes are similar.

It is possible to form a Hausman statistic as a quadratic form in  $(\hat{\gamma} - \hat{\beta}/\hat{\sigma})$ , but obtaining the appropriate asymptotic variance is somewhat complicated. (See Ruud, 1984, for a formal discussion of this test.) Section 16.7 discusses more flexible models that may be needed for corner solution outcomes.

#### 16.6.4 Estimation under Conditional Median Restrictions

It is possible to  $\sqrt{N}$ -consistently estimate  $\beta$  without assuming a particular distribution for u and without even assuming that u and x are independent. Consider again the latent variable model, but where the *median* of u given x is zero:

$$y^* = \mathbf{x}\boldsymbol{\beta} + u, \qquad \text{Med}(u \,|\, \mathbf{x}) = 0 \tag{16.34}$$

This equation implies that  $\operatorname{Med}(y^* | \mathbf{x}) = \mathbf{x}\boldsymbol{\beta}$ , so that the median of  $y^*$  is linear in  $\mathbf{x}$ . If the distribution of u given  $\mathbf{x}$  is symmetric about zero, then the conditional expectation and conditional median of  $y^*$  coincide, in which case there is no ambiguity about what we would like to estimate in the case of data censoring. If  $y^*$  given  $\mathbf{x}$  is asymmetric, the median and mean can be very different.

A well-known result in probability says that, if g(y) is a nondecreasing function, then Med[g(y)] = g[Med(y)]. (The same property does *not* hold for the expected value.) Then, because  $y = \max(0, y^*)$  is a nondecreasing function,

$$Med(y \mid \mathbf{x}) = \max[0, Med(y^* \mid \mathbf{x})] = \max(0, \mathbf{x}\boldsymbol{\beta})$$
(16.35)

Importantly, equation (16.35) holds under assumption (16.34) only; no further distributional assumptions are needed. In Chapter 12 we noted that the analogy principle leads to least absolute deviations as the appropriate method for estimating the parameters in a conditional median. Therefore, assumption (16.35) suggests estimating  $\beta$  by solving

$$\min_{\boldsymbol{\beta}} \sum_{i=1}^{N} |y_i - \max(0, \mathbf{x}_i \boldsymbol{\beta})| \tag{16.36}$$

This estimator was suggested by Powell (1984) for the censored Tobit model. Since  $q(\mathbf{w}, \boldsymbol{\beta}) \equiv |y - \max(0, \mathbf{x}\boldsymbol{\beta})|$  is a continuous function of  $\boldsymbol{\beta}$ , consistency of Powell's estimator follows from Theorem 12.2 under an appropriate identification assumption. Establishing  $\sqrt{N}$ -asymptotic normality is much more difficult because the objective function is not twice continuously differentiable with nonsingular Hessian. Powell (1984, 1994) and Newey and McFadden (1994) contain applicable theorems.

{545}------------------------------------------------

Powell's method also applies to corner solution applications, but the difference between the conditional median of y and its conditional expectations becomes crucial. As shown in equation (16.35), Medðy j xÞ does not depend on the distribution of u given x, whereas Eðy j xÞ and Eðy j x; y > 0Þ do. Further, the median and mean functions have different shapes. The conditional median of y is zero for x*b* a 0, and it is linear in x for x*b* > 0. (One implication of this fact is that, when using the median for predicting y, the prediction is exact when x<sup>i</sup> ^*<sup>b</sup>* <sup>a</sup> 0 and yi <sup>¼</sup> 0.) By contrast, the conditional expectation Eðy j xÞ is never zero and is everywhere a nonlinear function of x. In the standard Tobit specification we can also estimate Eðy j x; y > 0Þ and various probabilities. By its nature, the LAD approach does not allow us to do so. We cannot resolve the issue about whether the median or mean is more relevant for determining the effects of the xj on y. It depends on the context and is somewhat a matter of taste.

In some cases a quantile other than the median is of interest. Buchinsky and Hahn (1998) show how to estimate the parameters in a censored quantile regression model. It is also possible to estimate Eðy j xÞ and Eðy j x; y > 0Þ without specifying the distribution of u given x using semiparametric methods similar to those used to estimate index binary choice models without specifying the index function G. See Powell (1994) for a summary.