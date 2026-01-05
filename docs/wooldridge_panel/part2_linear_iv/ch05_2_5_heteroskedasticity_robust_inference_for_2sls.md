# Heteroskedasticity-Robust Inference for 2SLS

> Pages: 115-120

Assumption 2SLS.3 can be restrictive, so we should have a variance matrix estimator that is robust in the presence of heteroskedasticity of unknown form. As usual, we need to estimate **B** along with **A**. Under Assumptions 2SLS.1 and 2SLS.2 only,  $Avar(\hat{\beta})$  can be estimated as

$$(\hat{\mathbf{X}}'\hat{\mathbf{X}})^{-1} \left( \sum_{i=1}^{N} \hat{u}_i^2 \hat{\mathbf{x}}_i' \hat{\mathbf{x}}_i \right) (\hat{\mathbf{X}}'\hat{\mathbf{X}})^{-1}$$

$$(5.34)$$

Sometimes this matrix is multiplied by N/(N-K) as a degrees-of-freedom adjustment. This heteroskedasticity-robust estimator can be used anywhere the estimator  $\hat{\sigma}^2(\hat{\mathbf{X}}'\hat{\mathbf{X}})^{-1}$  is. In particular, the square roots of the diagonal elements of the matrix (5.34) are the heteroskedasticity-robust standard errors for 2SLS. These can be used to construct (asymptotic) t statistics in the usual way. Some packages compute these standard errors using a simple command. For example, using Stata®, rounded to three decimal places the heteroskedasticity-robust standard error for *educ* in Example 5.3 is .022, which is the same as the usual standard error rounded to three decimal places. The robust standard error for *exper* is .015, somewhat higher than the nonrobust one (.013).

Sometimes it is useful to compute a robust standard error that can be computed with any regression package. Wooldridge (1995b) shows how this procedure can be carried out using an auxiliary linear regression for each parameter. Consider computing the robust standard error for  $\hat{\beta}_j$ . Let "se( $\hat{\beta}_j$ )" denote the standard error computed using the usual variance matrix (5.27); we put this in quotes because it is no longer appropriate if Assumption 2SLS.3 fails. The  $\hat{\sigma}$  is obtained from equation (5.26), and  $\hat{u}_i$  are the 2SLS residuals from equation (5.25). Let  $\hat{r}_{ij}$  be the residuals from the regression

$$\hat{x}_{ij}$$
 on  $\hat{x}_{i1}, \hat{x}_{i2}, \dots, \hat{x}_{i,j-1}, \hat{x}_{i,j+1}, \dots, \hat{x}_{iK}, \qquad i = 1, 2, \dots, N$ 

and define  $\hat{m}_j \equiv \sum_{i=1}^N \hat{r}_{ij}\hat{u}_i$ . Then, a heteroskedasticity-robust standard error of  $\hat{\beta}_j$  can be tabulated as

$$\operatorname{se}(\hat{\beta}_i) = [N/(N-K)]^{1/2} [\operatorname{"se}(\hat{\beta}_i)"/\hat{\sigma}]^2 / (\hat{m}_i)^{1/2}$$
(5.35)

Many econometrics packages compute equation (5.35) for you, but it is also easy to compute directly.

{116}------------------------------------------------

To test multiple linear restrictions using the Wald approach, we can use the usual statistic but with the matrix (5.34) as the estimated variance. For example, the heteroskedasticity-robust version of the test in Example 5.4 gives F = .25; asymptotically, F can be treated as an  $\mathcal{F}_{2,422}$  variate. The asymptotic p-value is .781.

The Lagrange multiplier test for omitted variables is easily made heteroskedasticity-robust. Again, consider the model (5.28) with the null (5.29), but this time without the homoskedasticity assumptions. Using the notation from before, let  $\hat{\mathbf{r}}_i \equiv (\hat{r}_{i1}, \hat{r}_{i2}, \dots, \hat{r}_{iK_2})$  be the  $1 \times K_2$  vectors of residuals from the multivariate regression  $\hat{\mathbf{x}}_{i2}$  on  $\hat{\mathbf{x}}_{i1}$ ,  $i = 1, 2, \dots, N$ . (Again, this procedure can be carried out by regressing each element of  $\hat{\mathbf{x}}_{i2}$  on all of  $\hat{\mathbf{x}}_{i1}$ .) Then, for each observation, form the  $1 \times K_2$  vector  $\tilde{u}_i \cdot \hat{r}_i \equiv (\tilde{u}_i \cdot \hat{r}_{i1}, \dots, \tilde{u}_i \cdot \hat{r}_{iK_2})$ . Then, the robust LM test is  $N - \mathrm{SSR}_0$  from the regression 1 on  $\tilde{u}_i \cdot \hat{r}_{i1}, \dots, \tilde{u}_i \cdot \hat{r}_{iK_2}$ ,  $i = 1, 2, \dots, N$ . Under  $H_0, N - \mathrm{SSR}_0 \stackrel{a}{\sim} \chi_{K_2}^2$ . This procedure can be justified in a manner similar to the tests in the context of OLS. You are referred to Wooldridge (1995b) for details.

#### 5.2.6 Potential Pitfalls with 2SLS

When properly applied, the method of instrumental variables can be a powerful tool for estimating structural equations using nonexperimental data. Nevertheless, there are some problems that one can encounter when applying IV in practice.

One thing to remember is that, unlike OLS under a zero conditional mean assumption, IV methods are never unbiased when at least one explanatory variable is endogenous in the model. In fact, under standard distributional assumptions, the expected value of the 2SLS estimator does not even exist. As shown by Kinal (1980), in the case when all endogenous variables have homoskedastic normal distributions with expectations linear in the exogenous variables, the number of moments of the 2SLS estimator that exist is one less than the number of overidentifying restrictions. This finding implies that when the number of instruments equals the number of explanatory variables, the IV estimator does not have an expected value. This is one reason we rely on large-sample analysis to justify 2SLS.

Even in large samples IV methods can be ill-behaved if the instruments are weak. Consider the simple model  $y = \beta_0 + \beta_1 x_1 + u$ , where we use  $z_1$  as an instrument for  $x_1$ . Assuming that  $Cov(z_1, x_1) \neq 0$ , the plim of the IV estimator is easily shown to be

$$p\lim \hat{\beta}_1 = \beta_1 + \text{Cov}(z_1, u) / \text{Cov}(z_1, x_1)$$
(5.36)

When  $Cov(z_1, u) = 0$  we obtain the consistency result from earlier. However, if  $z_1$  has some correlation with u, the IV estimator is, not surprisingly, inconsistent. Rewrite equation (5.36) as

$$plim \hat{\beta}_1 = \beta_1 + (\sigma_u/\sigma_{x_1})[Corr(z_1, u)/Corr(z_1, x_1)]$$

$$(5.37)$$

{117}------------------------------------------------

where  $\operatorname{Corr}(\cdot,\cdot)$  denotes correlation. From this equation we see that if  $z_1$  and u are correlated, the inconsistency in the IV estimator gets arbitrarily large as  $\operatorname{Corr}(z_1,x_1)$  gets close to zero. Thus seemingly small correlations between  $z_1$  and u can cause severe inconsistency—and therefore severe finite sample bias—if  $z_1$  is only weakly correlated with  $x_1$ . In such cases it may be better to just use OLS, even if we only focus on the inconsistency in the estimators: the plim of the OLS estimator is generally  $\beta_1 + (\sigma_u/\sigma_{x_1}) \operatorname{Corr}(x_1,u)$ . Unfortunately, since we cannot observe u, we can never know the size of the inconsistencies in IV and OLS. But we should be concerned if the correlation between  $z_1$  and  $x_1$  is weak. Similar considerations arise with multiple explanatory variables and instruments.

Another potential problem with applying 2SLS and other IV procedures is that the 2SLS standard errors have a tendency to be "large." What is typically meant by this statement is either that 2SLS coefficients are statistically insignificant or that the 2SLS standard errors are much larger than the OLS standard errors. Not suprisingly, the magnitudes of the 2SLS standard errors depend, among other things, on the quality of the instrument(s) used in estimation.

For the following discussion we maintain the standard 2SLS Assumptions 2SLS.1–2SLS.3 in the model

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + u \tag{5.38}$$

Let  $\beta$  be the vector of 2SLS estimators using instruments  $\mathbf{z}$ . For concreteness, we focus on the asymptotic variance of  $\hat{\beta}_K$ . Technically, we should study Avar  $\sqrt{N}(\hat{\beta}_K - \beta_K)$ , but it is easier to work with an expression that contains the same information. In particular, we use the fact that

$$Avar(\hat{\beta}_K) \approx \frac{\sigma^2}{\hat{SSR}_K}$$
 (5.39)

where  $\hat{SSR}_K$  is the sum of squared residuals from the regression

$$\hat{x}_K \text{ on } 1, \ \hat{x}_1, \dots, \hat{x}_{K-1}$$
 (5.40)

(Remember, if  $x_j$  is exogenous for any j, then  $\hat{x}_j = x_j$ .) If we replace  $\sigma^2$  in regression (5.39) with  $\hat{\sigma}^2$ , then expression (5.39) is the usual 2SLS variance estimator. For the current discussion we are interested in the behavior of  $\hat{SSR}_K$ .

From the definition of an R-squared, we can write

$$\hat{SSR}_K = \hat{SST}_K (1 - \hat{R}_K^2) \tag{5.41}$$

where  $\hat{SST}_K$  is the total sum of squares of  $\hat{x}_K$  in the sample,  $\hat{SST}_K = \sum_{i=1}^N (\hat{x}_{iK} - \bar{\hat{x}}_K)$ , and  $\hat{R}_K^2$  is the *R*-squared from regression (5.40). In the context of OLS, the term

{118}------------------------------------------------

 $(1 - \hat{R}_K^2)$  in equation (5.41) is viewed as a measure of multicollinearity, whereas  $\hat{SST}_K$  measures the total variation in  $\hat{x}_K$ . We see that, in addition to traditional multicollinearity, 2SLS can have an additional source of large variance: the total variation in  $\hat{x}_K$  can be small.

When is  $\hat{SST}_K$  small? Remember,  $\hat{x}_K$  denotes the fitted values from the regression

$$x_K ext{ on } \mathbf{z}$$
 (5.42)

Therefore,  $\hat{SST}_K$  is the *same* as the explained sum of squares from the regression (5.42). If  $x_K$  is only weakly related to the IVs, then the explained sum of squares from regression (5.42) can be quite small, causing a large asymptotic variance for  $\hat{\beta}_K$ . If  $x_K$  is highly correlated with  $\mathbf{z}$ , then  $\hat{SST}_K$  can be almost as large as the total sum of squares of  $x_K$  and  $\hat{SST}_K$ , and this fact reduces the 2SLS variance estimate.

When  $x_K$  is exogenous—whether or not the other elements of  $\mathbf{x}$  are— $\hat{SST}_K = SST_K$ . While this total variation can be small, it is determined only by the sample variation in  $\{x_{iK}: i=1,2,\ldots,N\}$ . Therefore, for exogenous elements appearing among  $\mathbf{x}$ , the quality of instruments has no bearing on the size of the total sum of squares term in equation (5.41). This fact helps explain why the 2SLS estimates on exogenous explanatory variables are often much more precise than the coefficients on endogenous explanatory variables.

In addition to making the term  $\hat{SST}_K$  small, poor quality of instruments can lead to  $\hat{R}_K^2$  close to one. As an illustration, consider a model in which  $x_K$  is the only endogenous variable and there is one instrument  $z_1$  in addition to the exogenous variables  $(1, x_1, \ldots, x_{K-1})$ . Therefore,  $\mathbf{z} \equiv (1, x_1, \ldots, x_{K-1}, z_1)$ . (The same argument works for multiple instruments.) The fitted values  $\hat{x}_K$  come from the regression

$$x_K \text{ on } 1, x_1, \dots, x_{K-1}, z_1$$
 (5.43)

Because all other regressors are exogenous (that is, they are included in  $\mathbf{z}$ ),  $\hat{R}_K^2$  comes from the regression

$$\hat{x}_K \text{ on } 1, x_1, \dots, x_{K-1}$$
 (5.44)

Now, from basic least squares mechanics, if the coefficient on  $z_1$  in regression (5.43) is exactly zero, then the *R*-squared from regression (5.44) is exactly unity, in which case the 2SLS estimator does not even exist. This outcome virtually never happens, but  $z_1$  could have little explanatory value for  $x_K$  once  $x_1, \ldots, x_{K-1}$  have been controlled for, in which case  $\hat{R}_K^2$  can be close to one. Identification, which only has to do with whether we can consistently estimate  $\beta$ , requires only that  $z_1$  appear with nonzero coefficient in the population analogue of regression (5.43). But if the explanatory power of  $z_1$  is weak, the asymptotic variance of the 2SLS estimator can be quite

{119}------------------------------------------------

large. This is another way to illustrate why nonzero correlation between  $x_K$  and  $z_1$  is not enough for 2SLS to be effective: the *partial* correlation is what matters for the asymptotic variance.

As always, we must keep in mind that there are no absolute standards for determining when the denominator of equation (5.39) is "large enough." For example, it is quite possible that, say,  $x_K$  and  $\mathbf{z}$  are only weakly linearly related but the sample size is sufficiently large so that the term  $\hat{\mathbf{SST}}_K$  is large enough to produce a small enough standard error (in the sense that confidence intervals are tight enough to reject interesting hypotheses). Provided there is some linear relationship between  $x_K$  and  $\mathbf{z}$  in the population,  $\hat{\mathbf{SST}}_K \stackrel{p}{\to} \infty$  as  $N \to \infty$ . Further, in the preceding example, if the coefficent  $\theta_1$  on  $z_1$  in the population regression (5.4) is different from zero, then  $\hat{R}_K^2$  converges in probability to a number less than one; asymptotically, multicollinearity is not a problem.

We are in a difficult situation when the 2SLS standard errors are so large that nothing is significant. Often we must choose between a possibly inconsistent estimator that has relatively small standard errors (OLS) and a consistent estimator that is so imprecise that nothing interesting can be concluded (2SLS). One approach is to use OLS unless we can reject exogeneity of the explanatory variables. We show how to test for endogeneity of one or more explanatory variables in Section 6.2.1.

There has been some important recent work on the finite sample properties of 2SLS that emphasizes the potentially large *biases* of 2SLS, even when sample sizes seem to be quite large. Remember that the 2SLS estimator is never unbiased (provided one has at least one truly endogenous variable in x). But we hope that, with a very large sample size, we need only weak instruments to get an estimator with small bias. Unfortunately, this hope is not fulfilled. For example, Bound, Jaeger, and Baker (1995) show that in the setting of Angrist and Krueger (1991) the 2SLS estimator can be expected to behave quite poorly, an alarming finding because Angrist and Krueger use 300,000 to 500,000 observations! The problem is that the instruments—representing quarters of birth and various interactions of these with year of birth and state of birth—are very weak, and they are too numerous relative to their contribution in explaining years of education. One lesson is that, even with a very large sample size and zero correlation between the instruments and error, we should not use too many overidentifying restrictions.

Staiger and Stock (1997) provide a theoretical analysis of the 2SLS estimator with weak instruments and conclude that, even with large sample sizes, instruments that have small partial correlation with an endogenous explanatory variable can lead to substantial biases in 2SLS. One lesson that comes out of the Staiger-Stock work is

{120}------------------------------------------------

that we should always compute the F statistic from the first-stage regression (or the t statistic with a single instrumental variable). Staiger and Stock (1997) provide some guidelines about how large this F statistic should be (equivalently, how small the pvalue should be) for 2SLS to have acceptable properties.