# The Linear Panel Data Model, Revisited

> Pages: 182-186

We now study the linear panel data model in more detail. Having data over time for the same cross section units is useful for several reasons. For one, it allows us to look at dynamic relationships, something we cannot do with a single cross section. A panel data set also allows us to control for unobserved cross section heterogeneity, but we will not exploit this feature of panel data until Chapter 10.

{183}------------------------------------------------

# 7.8.1 Assumptions for Pooled OLS

We now summarize the properties of pooled OLS and feasible GLS for the linear panel data model

$$y_t = \mathbf{x}_t \boldsymbol{\beta} + u_t, \qquad t = 1, 2, \dots, T \tag{7.66}$$

As always, when we need to indicate a particular cross section observation we include an i subscript, such as yit.

This model may appear overly restrictive because *b* is the same in each time period. However, by appropriately choosing xit, we can allow for parameters changing over time. Also, even though we write xit, some of the elements of xit may not be timevarying, such as gender dummies when i indexes individuals, or industry dummies when i indexes firms, or state dummies when i indexes cities.

Example 7.6 (Wage Equation with Panel Data): Suppose we have data for the years 1990, 1991, and 1992 on a cross section of individuals, and we would like to estimate the effect of computer usage on individual wages. One possible static model is

$$\log(wage_{it}) = \theta_0 + \theta_1 d9I_t + \theta_2 d9I_t + \delta_1 computer_{it} + \delta_2 educ_{it} + \delta_3 exper_{it} + \delta_4 female_i + u_{it}$$
(7.67)

where d91t and d92t are dummy indicators for the years 1991 and 1992 and computerit is a measure of how much person i used a computer during year t. The inclusion of the year dummies allows for aggregate time effects of the kind discussed in the Section 7.2 examples. This equation contains a variable that is constant across t, femalei, as well as variables that can change across i and t, such as educit and experit. The variable educit is given a t subscript, which indicates that years of education could change from year to year for at least some people. It could also be the case that educit is the same for all three years for every person in the sample, in which case we could remove the time subscript. The distinction between variables that are timeconstant is not very important here; it becomes much more important in Chapter 10.

As a general rule, with large N and small T it is a good idea to allow for separate intercepts for each time period. Doing so allows for aggregate time effects that have the same influence on yit for all i.

Anything that can be done in a cross section context can also be done in a panel data setting. For example, in equation (7.67) we can interact femalei with the time dummy variables to see whether productivity of females has changed over time, or we 

{184}------------------------------------------------

can interact  $educ_{it}$  and  $computer_{it}$  to allow the return to computer usage to depend on level of education.

The two assumptions sufficient for pooled OLS to consistently estimate  $\beta$  are as follows:

ASSUMPTION POLS.1:  $E(\mathbf{x}_t'u_t) = 0, t = 1, 2, \dots, T.$ 

ASSUMPTION POLS.2: rank $\left[\sum_{t=1}^{T} E(\mathbf{x}_{t}'\mathbf{x}_{t})\right] = K$ .

Remember, Assumption POLS.1 says nothing about the relationship between  $\mathbf{x}_s$  and  $u_t$  for  $s \neq t$ . Assumption POLS.2 essentially rules out perfect linear dependencies among the explanatory variables.

To apply the usual OLS statistics from the pooled OLS regression across i and t, we need to add homoskedasticity and no serial correlation assumptions. The weakest forms of these assumptions are the following:

ASSUMPTION POLS.3: (a) 
$$E(u_t^2 \mathbf{x}_t' \mathbf{x}_t) = \sigma^2 E(\mathbf{x}_t' \mathbf{x}_t)$$
,  $t = 1, 2, ..., T$ , where  $\sigma^2 = E(u_t^2)$  for all  $t$ ; (b)  $E(u_t u_s \mathbf{x}_s' \mathbf{x}_s) = \mathbf{0}$ ,  $t \neq s$ ,  $t, s = 1, ..., T$ .

The first part of Assumption POLS.3 is a fairly strong homoskedasticity assumption; sufficient is  $E(u_t^2 | \mathbf{x}_t) = \sigma^2$  for all t. This means not only that the conditional variance does not depend on  $\mathbf{x}_t$ , but also that the unconditional variance is the same in every time period. Assumption POLS.3b essentially restricts the conditional covariances of the errors across different time periods to be zero. In fact, since  $\mathbf{x}_t$  almost always contains a constant, POLS.3b requires at a minimum that  $E(u_t u_s) = 0$ ,  $t \neq s$ . Sufficient for POLS.3b is  $E(u_t u_s | \mathbf{x}_t, \mathbf{x}_s) = 0$ ,  $t \neq s$ ,  $t, s = 1, \ldots, T$ .

It is important to remember that Assumption POLS.3 implies more than just a certain form of the *unconditional* variance matrix of  $\mathbf{u} = (u_1, \dots, u_T)'$ . Assumption POLS.3 implies  $\mathrm{E}(\mathbf{u}_i \mathbf{u}_i') = \sigma^2 \mathbf{I}_T$ , which means that the unconditional variances are constant and the unconditional covariances are zero, but it also effectively restricts the *conditional* variances and covariances.

THEOREM 7.7 (Large Sample Properties of Pooled OLS): Under Assumptions POLS.1 and POLS.2, the pooled OLS estimator is consistent and asymptotically normal. If Assumption POLS.3 holds in addition, then  $\operatorname{Avar}(\hat{\pmb{\beta}}) = \sigma^2 [\operatorname{E}(\mathbf{X}_i'\mathbf{X}_i)]^{-1}/N$ , so that the appropriate estimator of  $\operatorname{Avar}(\hat{\pmb{\beta}})$  is

$$\hat{\sigma}^{2}(\mathbf{X}'\mathbf{X})^{-1} = \hat{\sigma}^{2} \left( \sum_{i=1}^{N} \sum_{t=1}^{T} \mathbf{x}'_{it} \mathbf{x}_{it} \right)^{-1}$$
(7.68)

where  $\hat{\sigma}^2$  is the usual OLS variance estimator from the pooled regression

{185}------------------------------------------------

$$y_{it}$$
 on  $\mathbf{x}_{it}$ ,  $t = 1, 2, \dots, T, \ i = 1, \dots, N$  (7.69)

It follows that the usual t statistics and F statistics from regression (7.69) are approximately valid. Therefore, the F statistic for testing Q linear restrictions on the  $K \times 1$  vector  $\beta$  is

$$F = \frac{(SSR_r - SSR_{ur})}{SSR_{ur}} \cdot \frac{(NT - K)}{O}$$
(7.70)

where  $SSR_{ur}$  is the sum of squared residuals from regression (7.69), and  $SSR_r$  is the regression using the *NT* observations with the restrictions imposed.

Why is a simple pooled OLS analysis valid under Assumption POLS.3? It is easy to show that Assumption POLS.3 implies that  $\mathbf{B} = \sigma^2 \mathbf{A}$ , where  $\mathbf{B} \equiv \sum_{t=1}^{T} \sum_{s=1}^{T} \mathrm{E}(u_t u_s \mathbf{x}_t' \mathbf{x}_s)$ , and  $\mathbf{A} \equiv \sum_{t=1}^{T} \mathrm{E}(\mathbf{x}_t' \mathbf{x}_t)$ . For the panel data case, these are the matrices that appear in expression (7.21).

For computing the pooled OLS estimates and standard statistics, it does not matter how the data are ordered. However, if we put lags of any variables in the equation, it is easiest to order the data in the same way as is natural for studying asymptotic properties: the first T observations should be for the first cross section unit (ordered chronologically), the next T observations are for the next cross section unit, and so on. This procedure gives NT rows in the data set ordered in a very specific way.

Example 7.7 (Effects of Job Training Grants on Firm Scrap Rates): Using the data from JTRAIN1.RAW (Holzer, Block, Cheatham, and Knott, 1993), we estimate a model explaining the firm scrap rate in terms of grant receipt. We can estimate the equation for 54 firms and three years of data (1987, 1988, and 1989). The first grants were given in 1988. Some firms in the sample in 1989 received a grant only in 1988, so we allow for a one-year-lagged effect:

$$\log(\hat{s}crap_{it}) = .597 - .239 \, d88_t - .497 \, d89_t + .200 \, grant_{it} + .049 \, grant_{i,t-1}$$

$$(.203) \quad (.311) \quad (.338) \quad (.338) \quad (.436)$$

$$N = 54, \qquad T = 3, \qquad R^2 = .0173$$

where we have put i and t subscripts on the variables to emphasize which ones change across firm or time. The R-squared is just the usual one computed from the pooled OLS regression.

In this equation, the estimated grant effect has the wrong sign, and neither the current nor lagged grant variable is statistically significant. When a lag of  $log(scrap_{it})$  is added to the equation, the estimates are notably different. See Problem 7.9.

{186}------------------------------------------------