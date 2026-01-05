# Asymptotic Normality of 2SLS

> Pages: 109-111

The asymptotic normality of  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})$  follows from the asymptotic normality of  $N^{-1/2} \sum_{i=1}^{N} \mathbf{z}_i' u_i$ , which follows from the central limit theorem under Assumption 2SLS.1 and mild finite second-moment assumptions. The asymptotic variance is simplest under a homoskedasticity assumption:

{110}------------------------------------------------

ASSUMPTION 2SLS.3:  $E(u^2\mathbf{z}'\mathbf{z}) = \sigma^2 E(\mathbf{z}'\mathbf{z})$ , where  $\sigma^2 = E(u^2)$ .

This assumption is the same as Assumption OLS.3 except that the vector of instruments appears in place of **x**. By the usual LIE argument, sufficient for Assumption 2SLS.3 is the assumption

$$E(u^2 \mid \mathbf{z}) = \sigma^2 \tag{5.23}$$

which is the same as  $Var(u | \mathbf{z}) = \sigma^2$  if  $E(u | \mathbf{z}) = 0$ . [When  $\mathbf{x}$  contains endogenous elements, it makes no sense to make assumptions about  $Var(u | \mathbf{x})$ .]

THEOREM 5.2 (Asymptotic Normality of 2SLS): Under Assumptions 2SLS.1–2SLS.3,  $\sqrt{N}(\hat{\pmb{\beta}}-\beta)$  is asymptotically normally distributed with mean zero and variance matrix

$$\sigma^{2}\left\{\mathrm{E}(\mathbf{x}'\mathbf{z})[\mathrm{E}(\mathbf{z}'\mathbf{z})]^{-1}\mathrm{E}(\mathbf{z}'\mathbf{x})\right\}^{-1}$$
(5.24)

The proof of Theorem 5.2 is similar to Theorem 4.2 for OLS and is therefore omitted. The matrix in expression (5.24) is easily estimated using sample averages. To estimate  $\sigma^2$  we will need appropriate estimates of the  $u_i$ . Define the **2SLS residuals** as

$$\hat{\mathbf{u}}_i = y_i - \mathbf{x}_i \hat{\boldsymbol{\beta}}, \qquad i = 1, 2, \dots, N \tag{5.25}$$

Note carefully that these residuals are *not* the residuals from the second-stage OLS regression that can be used to obtain the 2SLS estimates. The residuals from the second-stage regression are  $y_i - \hat{\mathbf{x}}_i \hat{\boldsymbol{\beta}}$ . Any 2SLS software routine will compute equation (5.25) as the 2SLS residuals, and these are what we need to estimate  $\sigma^2$ .

Given the 2SLS residuals, a consistent (though not unbiased) estimator of  $\sigma^2$  under Assumptions 2SLS.1–2SLS.3 is

$$\hat{\sigma}^2 \equiv (N - K)^{-1} \sum_{i=1}^{N} \hat{u}_i^2 \tag{5.26}$$

Many regression packages use the degrees of freedom adjustment N-K in place of N, but this usage does not affect the consistency of the estimator.

The  $K \times K$  matrix

$$\hat{\sigma}^2 \left( \sum_{i=1}^N \hat{\mathbf{x}}_i' \hat{\mathbf{x}}_i \right)^{-1} = \hat{\sigma}^2 (\hat{\mathbf{X}}' \hat{\mathbf{X}})^{-1}$$
(5.27)

is a valid estimator of the asymptotic variance of  $\hat{\beta}$  under Assumptions 2SLS.1–2SLS.3. The (asymptotic) standard error of  $\hat{\beta}_j$  is just the square root of the *j*th diagonal element of matrix (5.27). Asymptotic confidence intervals and *t* statistics are obtained in the usual fashion.


{111}------------------------------------------------

Example 5.3 (Parents' and Husband's Education as IVs): We use the data on the 428 working, married women in MROZ.RAW to estimate the wage equation (5.12). We assume that experience is exogenous, but we allow educ to be correlated with u. The instruments we use for educ are motheduc, fatheduc, and huseduc. The reduced form for educ is

$$educ = \delta_0 + \delta_1 exper + \delta_2 exper^2 + \theta_1 motheduc + \theta_2 fatheduc + \theta_3 huseduc + r$$

Assuming that *motheduc*, *fatheduc*, and *huseduc* are exogenous in the log(wage) equation (a tenuous assumption), equation (5.12) is identified if at least one of  $\theta_1$ ,  $\theta_2$ , and  $\theta_3$  is nonzero. We can test this assumption using an F test (under homoskedasticity). The F statistic (with 3 and 422 degrees of freedom) turns out to be 104.29, which implies a p-value of zero to four decimal places. Thus, as expected, educ is fairly strongly related to motheduc, fatheduc, and huseduc. (Each of the three t statistics is also very significant.)

When equation (5.12) is estimated by 2SLS, we get the following:

$$log(\hat{w}age) = -.187 + .043 \ exper - .00086 \ exper^2 + .080 \ educ$$

$$(.285) \ (.013) \ (.00040) \ (.022)$$

where standard errors are in parentheses. The 2SLS estimate of the return to education is about 8 percent, and it is statistically significant. For comparison, when equation (5.12) is estimated by OLS, the estimated coefficient on *educ* is about .107 with a standard error of about .014. Thus, the 2SLS estimate is notably below the OLS estimate and has a larger standard error.