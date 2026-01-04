

{71}------------------------------------------------

Because E(u)=0,  $\sigma^2$  is also equal to Var(u). Assumption OLS.3 is the weakest form of the homoskedasticity assumption. If we write out the  $K\times K$  matrices in Assumption OLS.3 element by element, we see that Assumption OLS.3 is equivalent to assuming that the squared error,  $u^2$ , is uncorrelated with each  $x_j$ ,  $x_j^2$ , and all cross products of the form  $x_jx_k$ . By the law of iterated expectations, sufficient for Assumption OLS.3 is  $E(u^2\,|\,\mathbf{x})=\sigma^2$ , which is the same as  $Var(u\,|\,\mathbf{x})=\sigma^2$  when  $E(u\,|\,\mathbf{x})=0$ . The constant conditional variance assumption for u given  $\mathbf{x}$  is the easiest to interpret, but it is stronger than needed.

THEOREM 4.2 (Asymptotic Normality of OLS): Under Assumptions OLS.1–OLS.3,

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \stackrel{a}{\sim} \text{Normal}(0, \sigma^2 \mathbf{A}^{-1})$$
 (4.9)

*Proof:* From equation (4.8) and definition of **B**, it follows from Lemma 3.7 and Corollary 3.2 that

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \stackrel{a}{\sim} \text{Normal}(0, \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-1})$$

Under Assumption OLS.3,  $\mathbf{B} = \sigma^2 \mathbf{A}$ , which proves the result.

Practically speaking, equation (4.9) allows us to treat  $\hat{\boldsymbol{\beta}}$  as approximately normal with mean  $\boldsymbol{\beta}$  and variance  $\sigma^2[\mathrm{E}(\mathbf{x}'\mathbf{x})]^{-1}/N$ . The usual estimator of  $\sigma^2$ ,  $\hat{\sigma}^2 \equiv \mathrm{SSR}/(N-K)$ , where  $\mathrm{SSR} = \sum_{i=1}^N \hat{u}_i^2$  is the OLS sum of squared residuals, is easily shown to be consistent. (Using N or N-K in the denominator does not affect consistency.) When we also replace  $\mathrm{E}(\mathbf{x}'\mathbf{x})$  with the sample average  $N^{-1}\sum_{i=1}^N \mathbf{x}_i'\mathbf{x}_i = (\mathbf{X}'\mathbf{X}/N)$ , we get

$$\operatorname{Avar}(\hat{\boldsymbol{\beta}}) = \hat{\sigma}^2 (\mathbf{X}'\mathbf{X})^{-1} \tag{4.10}$$

The right-hand side of equation (4.10) should be familiar: it is the usual OLS variance matrix estimator under the classical linear model assumptions. The bottom line of Theorem 4.2 is that, under Assumptions OLS.1–OLS.3, the usual OLS standard errors, t statistics, and F statistics are asymptotically valid. Showing that the F statistic is approximately valid is done by deriving the Wald test for linear restrictions of the form  $\mathbf{R}\boldsymbol{\beta} = \mathbf{r}$  (see Chapter 3). Then the F statistic is simply a degrees-of-freedom-adjusted Wald statistic, which is where the F distribution (as opposed to the chisquare distribution) arises.

# 4.2.3 Heteroskedasticity-Robust Inference

If Assumption OLS.1 fails, we are in potentially serious trouble, as OLS is not even consistent. In the next chapter we discuss the important method of instrumental variables that can be used to obtain consistent estimators of  $\beta$  when Assumption

{72}------------------------------------------------

OLS.1 fails. Assumption OLS.2 is also needed for consistency, but there is rarely any reason to examine its failure.

Failure of Assumption OLS.3 has less serious consequences than failure of Assumption OLS.1. As we have already seen, Assumption OLS.3 has nothing to do with consistency of  $\hat{\beta}$ . Further, the proof of asymptotic normality based on equation (4.8) is still valid without Assumption OLS.3, but the final asymptotic variance is different. We have assumed OLS.3 for deriving the limiting distribution because it implies the asymptotic validity of the usual OLS standard errors and test statistics. All regression packages assume OLS.3 as the default in reporting statistics.

Often there are reasons to believe that Assumption OLS.3 might fail, in which case equation (4.10) is no longer a valid estimate of even the asymptotic variance matrix. If we make the zero conditional mean assumption (4.3), one solution to violation of Assumption OLS.3 is to specify a model for Var(y|x), estimate this model, and apply weighted least squares (WLS): for observation i,  $y_i$  and every element of  $x_i$ (including unity) are divided by an estimate of the conditional standard deviation  $[Var(y_i | \mathbf{x}_i)]^{1/2}$ , and OLS is applied to the weighted data (see Wooldridge, 2000a, Chapter 8, for details). This procedure leads to a different estimator of  $\beta$ . We discuss WLS in the more general context of nonlinear regression in Chapter 12. Lately, it has become more popular to estimate  $\beta$  by OLS even when heteroskedasticity is suspected but to adjust the standard errors and test statistics so that they are valid in the presence of arbitrary heteroskedasticity. Since these standard errors are valid whether or not Assumption OLS.3 holds, this method is much easier than a weighted least squares procedure. What we sacrifice is potential efficiency gains from weighted least squares (WLS) (see Chapter 14). But, efficiency gains from WLS are guaranteed only if the model for  $Var(y|\mathbf{x})$  is correct. Further, WLS is generally inconsistent if  $E(u | \mathbf{x}) \neq 0$  but Assumption OLS.1 holds, so WLS is inappropriate for estimating linear projections. Especially with large sample sizes, the presence of heteroskedasticity need not affect one's ability to perform accurate inference using OLS. But we need to compute standard errors and test statistics appropriately.

The adjustment needed to the asymptotic variance follows from the proof of Theorem 4.2: without OLS.3, the asymptotic variance of  $\hat{\boldsymbol{\beta}}$  is  $\operatorname{Avar}(\hat{\boldsymbol{\beta}}) = \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-1}/N$ , where the  $K \times K$  matrices  $\mathbf{A}$  and  $\mathbf{B}$  were defined earlier. We already know how to consistently estimate  $\mathbf{A}$ . Estimation of  $\mathbf{B}$  is also straightforward. First, by the law of large numbers,  $N^{-1}\sum_{i=1}^N u_i^2 \mathbf{x}_i' \mathbf{x}_i \stackrel{p}{\to} \mathrm{E}(u^2 \mathbf{x}' \mathbf{x}) = \mathbf{B}$ . Now, since the  $u_i$  are not observed, we replace  $u_i$  with the OLS residual  $\hat{u}_i = y_i - \mathbf{x}_i \hat{\boldsymbol{\beta}}$ . This leads to the consistent estimator  $\hat{\mathbf{B}} \equiv N^{-1}\sum_{i=1}^N \hat{u}_i^2 \mathbf{x}_i' \mathbf{x}_i$ . See White (1984) and Problem 4.5.

The heteroskedasticity-robust variance matrix estimator of  $\hat{\beta}$  is  $\hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1}/N$  or, after cancellations,

{73}------------------------------------------------

$$\operatorname{Avar}(\hat{\boldsymbol{\beta}}) = (\mathbf{X}'\mathbf{X})^{-1} \left( \sum_{i=1}^{N} \hat{u}_{i}^{2} \mathbf{x}_{i}' \mathbf{x}_{i} \right) (\mathbf{X}'\mathbf{X})^{-1}$$
(4.11)

This matrix was introduced in econometrics by White (1980b), although some attribute it to either Eicker (1967) or Huber (1967), statisticians who discovered robust variance matrices. The square roots of the diagonal elements of equation (4.11) are often called the **White standard errors** or **Huber standard errors**, or some hyphenated combination of the names Eicker, Huber, and White. It is probably best to just call them **heteroskedasticity-robust standard errors**, since this term describes their purpose. Remember, these standard errors are asymptotically valid in the presence of any kind of heteroskedasticity, including homoskedasticity.

Robust standard errors are often reported in applied cross-sectional work, especially when the sample size is large. Sometimes they are reported along with the usual OLS standard errors; sometimes they are presented in place of them. Several regression packages now report these standard errors as an option, so it is easy to obtain heteroskedasticity-robust standard errors.

Sometimes, as a degrees-of-freedom correction, the matrix in equation (4.11) is multiplied by N/(N-K). This procedure guarantees that, if the  $\hat{u}_i^2$  were constant across i (an unlikely event in practice, but the strongest evidence of homoskedasticity possible), then the usual OLS standard errors would be obtained. There is some evidence that the degrees-of-freedom adjustment improves finite sample performance. There are other ways to adjust equation (4.11) to improve its small-sample properties—see, for example, MacKinnon and White (1985)—but if N is large relative to K, these adjustments typically make little difference.

Once standard errors are obtained, *t* statistics are computed in the usual way. These are robust to heteroskedasticity of unknown form, and can be used to test single restrictions. The *t* statistics computed from heteroskedasticity robust standard errors are **heteroskedasticity-robust** *t* **statistics**. Confidence intervals are also obtained in the usual way.

When Assumption OLS.3 fails, the usual F statistic is not valid for testing multiple linear restrictions, even asymptotically. Some packages allow robust testing with a simple command, while others do not. If the hypotheses are written as

$$\mathbf{H_0: R\beta = r} \tag{4.12}$$

where **R** is  $Q \times K$  and has rank  $Q \leq K$ , and **r** is  $Q \times 1$ , then the heteroskedasticity-robust Wald statistic for testing equation (4.12) is

$$W = (\mathbf{R}\hat{\boldsymbol{\beta}} - \mathbf{r})'(\mathbf{R}\hat{\mathbf{V}}\mathbf{R}')^{-1}(\mathbf{R}\hat{\boldsymbol{\beta}} - \mathbf{r})$$
(4.13)

{74}------------------------------------------------

where  $\hat{\mathbf{V}}$  is given in equation (4.11). Under  $\mathbf{H}_0$ ,  $W \stackrel{a}{\sim} \chi_Q^2$ . The Wald statistic can be turned into an approximate  $\mathscr{F}_{Q,N-K}$  random variable by dividing it by Q (and usually making the degrees-of-freedom adjustment to  $\hat{\mathbf{V}}$ ). But there is nothing wrong with using equation (4.13) directly.

## 4.2.4 Lagrange Multiplier (Score) Tests

In the partitioned model

$$y = \mathbf{x}_1 \boldsymbol{\beta}_1 + \mathbf{x}_2 \boldsymbol{\beta}_2 + u \tag{4.14}$$

under Assumptions OLS.1–OLS.3, where  $\mathbf{x}_1$  is  $1 \times K_1$  and  $\mathbf{x}_2$  is  $1 \times K_2$ , we know that the hypothesis  $\mathbf{H}_0$ :  $\boldsymbol{\beta}_2 = \mathbf{0}$  is easily tested (asymptotically) using a standard F test. There is another approach to testing such hypotheses that is sometimes useful, especially for computing heteroskedasticity-robust tests and for nonlinear models.

Let  $\hat{\beta}_1$  be the estimator of  $\beta_1$  under the null hypothesis  $H_0$ :  $\beta_2 = 0$ ; this is called the estimator from the **restricted model**. Define the restricted OLS residuals as  $\tilde{u}_i = y_i - \mathbf{x}_{i1}\tilde{\boldsymbol{\beta}}_1$ , i = 1, 2, ..., N. Under  $H_0$ ,  $\mathbf{x}_{i2}$  should be, up to sample variation, uncorrelated with  $\tilde{u}_i$  in the sample. The Lagrange multiplier or score principle is based on this observation. It turns out that a valid test statistic is obtained as follows: Run the OLS regression

$$\tilde{\boldsymbol{u}} \text{ on } \mathbf{x}_1, \mathbf{x}_2$$
 (4.15)

(where the observation index i has been suppressed). Assuming that  $\mathbf{x}_1$  contains a constant (that is, the null model contains a constant), let  $R_u^2$  denote the usual R-squared from the regression (4.15). Then the **Lagrange multiplier (LM)** or **score statistic** is  $LM \equiv NR_u^2$ . These names come from different features of the constrained optimization problem; see Rao (1948), Aitchison and Silvey (1958), and Chapter 12. Because of its form, LM is also referred to as an **N-R-squared test**. Under  $H_0$ ,  $LM \stackrel{a}{\sim} \chi_{K_2}^2$ , where  $K_2$  is the number of restrictions being tested. If  $NR_u^2$  is sufficiently large, then  $\tilde{u}$  is significantly correlated with  $\mathbf{x}_2$ , and the null hypothesis will be rejected.

It is important to include  $\mathbf{x}_1$  along with  $\mathbf{x}_2$  in regression (4.15). In other words, the OLS residuals from the null model should be regressed on *all* explanatory variables, even though  $\tilde{\mathbf{u}}$  is orthogonal to  $\mathbf{x}_1$  in the sample. If  $\mathbf{x}_1$  is excluded, then the resulting statistic generally does *not* have a chi-square distribution when  $\mathbf{x}_2$  and  $\mathbf{x}_1$  are correlated. If  $\mathbf{E}(\mathbf{x}_1'\mathbf{x}_2) = \mathbf{0}$ , then we can exclude  $\mathbf{x}_1$  from regression (4.15), but this orthogonality rarely holds in applications. If  $\mathbf{x}_1$  does not include a constant,  $R_u^2$  should be the **uncentered R-squared**: the total sum of squares in the denominator is obtained

{75}------------------------------------------------

without demeaning the dependent variable,  $\tilde{u}$ . When  $\mathbf{x}_1$  includes a constant, the usual centered *R*-squared and uncentered *R*-squared are identical because  $\sum_{i=1}^{N} \tilde{u}_i = 0$ .

Example 4.1 (Wage Equation for Married, Working Women): Consider a wage equation for married, working women:

$$\log(wage) = \beta_0 + \beta_1 exper + \beta_2 exper^2 + \beta_3 educ$$

$$+ \beta_4 age + \beta_5 kidslt6 + \beta_6 kidsge6 + u$$
(4.16)

where the last three variables are the woman's age, number of children less than six, and number of children at least six years of age, respectively. We can test whether, after the productivity variables experience and education are controlled for, women are paid differently depending on their age and number of children. The F statistic for the hypothesis  $H_0$ :  $\beta_4 = 0, \beta_5 = 0, \beta_6 = 0$  is  $F = [(R_{ur}^2 - R_r^2)/(1 - R_{ur}^2)] \cdot [(N - 7)/3]$ , where  $R_{ur}^2$  and  $R_r^2$  are the unrestricted and restricted R-squareds; under  $H_0$  (and homoskedasticity),  $F \sim \mathscr{F}_{3,N-7}$ . To obtain the LM statistic, we estimate the equation without age, kidslt6, and kidsge6; let  $\tilde{u}$  denote the OLS residuals. Then, the LM statistic is  $NR_u^2$  from the regression  $\tilde{u}$  on 1, exper,  $exper^2$ , educ, age, kidslt6, and kidsge6, where the 1 denotes that we include an intercept. Under  $H_0$  and homoskedasticity,  $NR_u^2 \stackrel{\alpha}{\sim} \chi_3^2$ .

Using the data on the 428 working, married women in MROZ.RAW (from Mroz, 1987), we obtain the following estimated equation:

$$\log(\hat{w}age) = -.421 + .040 \ exper - .00078 \ exper^2 + .108 \ educ$$

$$(.317) \quad (.013) \quad (.00040) \quad (.014)$$

$$[.316] \quad [.015] \quad [.00041] \quad [.014]$$

$$- .0015 \ age - .061 \ kidslt6 - .015 \ kidsge6, \qquad R^2 = .158$$

$$(.0053) \quad (.089) \quad (.028)$$

$$[.0059] \quad [.105] \quad [.029]$$

where the quantities in brackets are the heteroskedasticity-robust standard errors. The F statistic for joint significance of age, kidslt6, and kidsge6 turns out to be about .24, which gives p-value  $\approx$  .87. Regressing the residuals  $\tilde{u}$  from the restricted model on all exogenous variables gives an R-squared of .0017, so LM = 428(.0017) = .728, and p-value  $\approx$  .87. Thus, the F and LM tests give virtually identical results.

The test from regression (4.15) maintains Assumption OLS.3 under  $H_0$ , just like the usual F test. It turns out to be easy to obtain a heteroskedasticity-robust LM

{76}------------------------------------------------

statistic. To see how to do so, let us look at the formula for the LM statistic from regression (4.15) in more detail. After some algebra we can write

$$LM = \left(N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{r}}_{i}' \tilde{\mathbf{u}}_{i}\right)' \left(\tilde{\sigma}^{2} N^{-1} \sum_{i=1}^{N} \hat{\mathbf{r}}_{i}' \hat{\mathbf{r}}_{i}\right)^{-1} \left(N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{r}}_{i}' \tilde{\mathbf{u}}_{i}\right)$$

where  $\tilde{\sigma}^2 \equiv N^{-1} \sum_{i=1}^N \tilde{u}_i^2$  and each  $\hat{\mathbf{r}}_i$  is a  $1 \times K_2$  vector of OLS residuals from the (multivariate) regression of  $\mathbf{x}_{i2}$  on  $\mathbf{x}_{i1}$ , i = 1, 2, ..., N. This statistic is not robust to heteroskedasticity because the matrix in the middle is not a consistent estimator of the asymptotic variance of  $(N^{-1/2} \sum_{i=1}^N \hat{\mathbf{r}}_i' \tilde{u}_i)$  under heteroskedasticity. Following the reasoning in Section 4.2.3, a heteroskedasticity-robust statistic is

$$LM = \left(N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{r}}_{i}' \tilde{u}_{i}\right)' \left(N^{-1} \sum_{i=1}^{N} \tilde{u}_{i}^{2} \hat{\mathbf{r}}_{i}' \hat{\mathbf{r}}_{i}\right)^{-1} \left(N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{r}}_{i}' \tilde{u}_{i}\right)$$
$$= \left(\sum_{i=1}^{N} \hat{\mathbf{r}}_{i}' \tilde{u}_{i}\right)' \left(\sum_{i=1}^{N} \tilde{u}_{i}^{2} \hat{\mathbf{r}}_{i}' \hat{\mathbf{r}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \hat{\mathbf{r}}_{i}' \tilde{u}_{i}\right)$$

Dropping the *i* subscript, this is easily obtained, as  $N - SSR_0$  from the OLS regression (without an intercept)

$$1 \text{ on } \tilde{\boldsymbol{u}} \cdot \hat{\mathbf{r}} \tag{4.17}$$

where  $\tilde{u} \cdot \hat{\mathbf{r}} = (\tilde{u} \cdot \hat{r}_1, \tilde{u} \cdot \hat{r}_2, \dots, \tilde{u} \cdot \hat{r}_{K_2})$  is the  $1 \times K_2$  vector obtained by multiplying  $\tilde{u}$  by each element of  $\hat{\mathbf{r}}$  and SSR<sub>0</sub> is just the usual sum of squared residuals from regression (4.17). Thus, we first regress each element of  $\mathbf{x}_2$  onto all of  $\mathbf{x}_1$  and collect the residuals in  $\hat{\mathbf{r}}$ . Then we form  $\tilde{u} \cdot \hat{\mathbf{r}}$  (observation by observation) and run the regression in (4.17);  $N - \text{SSR}_0$  from this regression is distributed asymptotically as  $\chi^2_{K_2}$ . (Do not be thrown off by the fact that the dependent variable in regression (4.17) is unity for each observation; a nonzero sum of squared residuals is reported when you run OLS without an intercept.) For more details, see Davidson and MacKinnon (1985, 1993) or Wooldridge (1991a, 1995b).

Example 4.1 (continued): To obtain the heteroskedasticity-robust LM statistic for  $H_0$ :  $\beta_4 = 0, \beta_5 = 0, \beta_6 = 0$  in equation (4.16), we estimate the restricted model as before and obtain  $\tilde{u}$ . Then, we run the regressions (1) age on 1, exper, exper<sup>2</sup>, educ; (2) kidslt6 on 1, exper, exper<sup>2</sup>, educ; (3) kidsge6 on 1, exper, exper<sup>2</sup>, educ; and obtain the residuals  $\hat{r}_1$ ,  $\hat{r}_2$ , and  $\hat{r}_3$ , respectively. The LM statistic is  $N - SSR_0$  from the regression 1 on  $\tilde{u} \cdot \hat{r}_1$ ,  $\tilde{u} \cdot \hat{r}_2$ ,  $\tilde{u} \cdot \hat{r}_3$ , and  $N - SSR_0 \stackrel{a}{\sim} \chi_3^2$ .

{77}------------------------------------------------

When we apply this result to the data in MROZ.RAW we get LM = .51, which is very small for a  $\chi_3^2$  random variable: p-value  $\approx .92$ . For comparison, the heteroskedasticity-robust Wald statistic (scaled by Stata\* to have an approximate F distribution) also yields p-value  $\approx .92$ .

#### 4.3 OLS Solutions to the Omitted Variables Problem

### 4.3.1 OLS Ignoring the Omitted Variables

Because it is so prevalent in applied work, we now consider the omitted variables problem in more detail. A model that assumes an additive effect of the omitted variable is

$$E(y \mid x_1, x_2, \dots, x_K, q) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + \gamma q$$
(4.18)

where q is the omitted factor. In particular, we are interested in the  $\beta_j$ , which are the partial effects of the observed explanatory variables holding the other explanatory variables constant, *including* the unobservable q. In the context of this additive model, there is no point in allowing for more than one unobservable; any omitted factors are lumped into q. Henceforth we simply refer to q as the omitted variable.

A good example of equation (4.18) is seen when y is log(wage) and q includes ability. If  $x_K$  denotes a measure of education,  $\beta_K$  in equation (4.18) measures the partial effect of education on wages controlling for—or holding fixed—the level of ability (as well as other observed characteristics). This effect is most interesting from a policy perspective because it provides a causal interpretation of the return to education:  $\beta_K$  is the expected proportionate increase in wage if someone from the working population is exogenously given another year of education.

Viewing equation (4.18) as a structural model, we can always write it in error form

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + \gamma q + v \tag{4.19}$$

$$E(v | x_1, x_2, \dots, x_K, q) = 0 (4.20)$$

where v is the **structural error**. One way to handle the nonobservability of q is to put it into the error term. In doing so, nothing is lost by assuming E(q) = 0 because an intercept is included in equation (4.19). Putting q into the error term means we rewrite equation (4.19) as

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + u \tag{4.21}$$

{78}------------------------------------------------

$$u \equiv \gamma q + v \tag{4.22}$$

The error u in equation (4.21) consists of two parts. Under equation (4.20), v has zero mean and is uncorrelated with x1; x2; ... ; xK (and q). By normalization, q also has zero mean. Thus, EðuÞ ¼ 0. However, u is uncorrelated with x1; x2; ... ; xK if and only if q is uncorrelated with each of the observable regressors. If q is correlated with any of the regressors, then so is u, and we have an endogeneity problem. We cannot expect OLS to consistently estimate any bj. Although Eðu j xÞ 0EðuÞ in equation (4.21), the b<sup>j</sup> do have a structural interpretation because they appear in equation (4.19).

It is easy to characterize the plims of the OLS estimators when the omitted variable is ignored; we will call this the OLS omitted variables inconsistency or OLS omitted variables bias (even though the latter term is not always precise). Write the linear projection of q onto the observable explanatory variables as

$$q = \delta_0 + \delta_1 x_1 + \dots + \delta_K x_K + r \tag{4.23}$$

where, by definition of a linear projection, EðrÞ ¼ 0, Covðxj;rÞ ¼ 0, j ¼ 1; 2; ... ; K. Then we can easily infer the plim of the OLS estimators from regressing y onto 1; x1; ... ; xK by finding an equation that does satisfy Assumptions OLS.1 and OLS.2. Plugging equation (4.23) into equation (4.19) and doing simple algrebra gives

$$y = (\beta_0 + \gamma \delta_0) + (\beta_1 + \gamma \delta_1)x_1 + (\beta_2 + \gamma \delta_2)x_2 + \dots + (\beta_K + \gamma \delta_K)x_K + v + \gamma r$$

Now, the error v þ gr has zero mean and is uncorrelated with each regressor. It follows that we can just read off the plim of the OLS estimators from the regression of y on 1; <sup>x</sup>1; ... ; xK : plim ^b<sup>j</sup> <sup>¼</sup> <sup>b</sup><sup>j</sup> <sup>þ</sup> gdj. Sometimes it is assumed that most of the <sup>d</sup><sup>j</sup> are zero. When the correlation between q and a particular variable, say xK , is the focus, a common (usually implicit) assumption is that all d<sup>j</sup> in equation (4.23) except the intercept and coefficient on xK are zero. Then plim ^b<sup>j</sup> <sup>¼</sup> <sup>b</sup>j, <sup>j</sup> <sup>¼</sup> <sup>1</sup>; ... ; <sup>K</sup> 1, and

$$plim \hat{\beta}_K = \beta_K + \gamma [Cov(x_K, q) / Var(x_K)]$$
(4.24)

[since d<sup>K</sup> ¼ CovðxK ; qÞ=VarðxK Þ in this case]. This formula gives us a simple way to determine the sign, and perhaps the magnitude, of the inconsistency in ^b<sup>K</sup> . If <sup>g</sup> <sup>&</sup>gt; <sup>0</sup> and xK and q are positively correlated, the asymptotic bias is positive. The other combinations are easily worked out. If xK has substantial variation in the population relative to the covariance between xK and q, then the bias can be small. In the general case of equation (4.23), it is difficult to sign d<sup>K</sup> because it measures a partial correlation. It is for this reason that d<sup>j</sup> ¼ 0, j ¼ 1; ... ; K 1 is often maintained for determining the likely asymptotic bias in ^b<sup>K</sup> when only xK is endogenous.

{79}------------------------------------------------

Example 4.2 (Wage Equation with Unobserved Ability): Write a structural wage equation explicitly as

$$\log(wage) = \beta_0 + \beta_1 exper + \beta_2 exper^2 + \beta_3 educ + \gamma abil + v$$

where v has the structural error property  $\mathrm{E}(v \mid exper, educ, abil) = 0$ . If abil is uncorrelated with exper and  $exper^2$  once educ has been partialed out—that is,  $abil = \delta_0 + \delta_3 educ + r$  with r uncorrelated with exper and  $exper^2$ —then  $\mathrm{plim}\ \hat{\beta}_3 = \beta_3 + \gamma \delta_3$ . Under these assumptions the coefficients on exper and  $exper^2$  are consistently estimated by the OLS regression that omits ability. If  $\delta_3 > 0$  then  $\mathrm{plim}\ \hat{\beta}_3 > \beta_3$  (because  $\gamma > 0$  by definition), and the return to education is likely to be overestimated in large samples.

## 4.3.2 The Proxy Variable-OLS Solution

Omitted variables bias can be eliminated, or at least mitigated, if a **proxy variable** is available for the unobserved variable q. There are two formal requirements for a proxy variable for q. The first is that the proxy variable should be **redundant** (sometimes called **ignorable**) in the structural equation. If z is a proxy variable for q, then the most natural statement of redundancy of z in equation (4.18) is

$$E(y \mid \mathbf{x}, q, z) = E(y \mid \mathbf{x}, q) \tag{4.25}$$

Condition (4.25) is easy to interpret: z is irrelevant for explaining y, in a conditional mean sense, once  $\mathbf{x}$  and q have been controlled for. This assumption on a proxy variable is virtually always made (sometimes only implicitly), and it is rarely controversial: the only reason we bother with z in the first place is that we cannot get data on q. Anyway, we cannot get very far without condition (4.25). In the wage-education example, let q be ability and z be IQ score. By definition it is ability that affects wage: IQ would not matter if true ability were known.

Condition (4.25) is somewhat stronger than needed when unobservables appear additively as in equation (4.18); it suffices to assume that v in equation (4.19) is simply uncorrelated with z. But we will focus on condition (4.25) because it is natural, and because we need it to cover models where q interacts with some observed covariates.

The second requirement of a good proxy variable is more complicated. We require that the correlation between the omitted variable q and each  $x_j$  be zero once we partial out z. This is easily stated in terms of a linear projection:

$$L(q | 1, x_1, \dots, x_K, z) = L(q | 1, z)$$
(4.26)

It is also helpful to see this relationship in terms of an equation with an unobserved error. Write q as a linear function of z and an error term as

{80}------------------------------------------------

$$q = \theta_0 + \theta_1 z + r \tag{4.27}$$

where, by definition, EðrÞ ¼ 0 and Covðz;rÞ ¼ 0 because y<sup>0</sup> þ y1z is the linear projection of q on 1, z. If z is a reasonable proxy for q, y<sup>1</sup> 0 0 (and we usually think in terms of y<sup>1</sup> > 0). But condition (4.26) assumes much more: it is equivalent to

$$Cov(x_j, r) = 0, j = 1, 2, ..., K$$

This condition requires z to be closely enough related to q so that once it is included in equation (4.27), the xj are not partially correlated with q.

Before showing why these two proxy variable requirements do the trick, we should head off some possible confusion. The definition of proxy variable here is not universal. While a proxy variable is always assumed to satisfy the redundancy condition (4.25), it is not always assumed to have the second property. In Chapter 5 we will use the notion of an indicator of q, which satisfies condition (4.25) but not the second proxy variable assumption.

To obtain an estimable equation, replace q in equation (4.19) with equation (4.27) to get

$$y = (\beta_0 + \gamma \theta_0) + \beta_1 x_1 + \dots + \beta_K x_K + \gamma \theta_1 z + (\gamma r + v)$$

$$\tag{4.28}$$

Under the assumptions made, the composite error term u 1gr þ v is uncorrelated with xj for all j; redundancy of z in equation (4.18) means that z is uncorrelated with v and, by definition, z is uncorrelated with r. It follows immediately from Theorem 4.1 that the OLS regression y on 1; x1; x2; ... ; xK , z produces consistent estimators of ðb<sup>0</sup> þ gy0Þ; b1; b2; ... ; b<sup>K</sup> , and gy1. Thus, we can estimate the partial effect of each of the xj in equation (4.18) under the proxy variable assumptions.

When z is an imperfect proxy, then r in equation (4.27) is correlated with one or more of the xj. Generally, when we do not impose condition (4.26) and write the linear projection as

$$q = \theta_0 + \rho_1 x_1 + \dots + \rho_K x_K + \theta_1 z + r$$

the proxy variable regression gives plim ^b<sup>j</sup> <sup>¼</sup> <sup>b</sup><sup>j</sup> <sup>þ</sup> grj. Thus, OLS with an imperfect proxy is inconsistent. The hope is that the r<sup>j</sup> are smaller in magnitude than if z were omitted from the linear projection, and this can usually be argued if z is a reasonable proxy for q.

If including z induces substantial collinearity, it might be better to use OLS without the proxy variable. However, in making these decisions we must recognize that including z reduces the error variance if y<sup>1</sup> 0 0: Varðgr þ vÞ < Varðgq þ vÞ because VarðrÞ < VarðqÞ, and v is uncorrelated with both r and q. Including a proxy variable can actually reduce asymptotic variances as well as mitigate bias.