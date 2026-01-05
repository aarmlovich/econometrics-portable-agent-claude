# Lagrange Multiplier (Score) Tests

> Pages: 74-77

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