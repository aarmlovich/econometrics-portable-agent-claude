# Reporting the Results

> Pages: 536-539

For data censoring applications, the quantities of interest are the ^b<sup>j</sup> and their standard errors. (We might use these to compute elasticities, and so on.) We interpret the estimated model as if there were no data-censoring problem, because the population model is a linear conditional mean. The value of the log-likelihood function should be reported for any estimated model because of its role in obtaining likelihood ratio statistics. We can test for omitted variables, including nonlinear functions of already included variables, using either t tests or LR tests. All of these rely on the homoskedastic normal assumption in the underlying population.

For corner solution applications, the same statistics can be reported, and, in addition, we should report estimated partial effects on Eðy j x; y > 0Þ and Eðy j xÞ. The formulas for these are given in Section 16.2, where *b* and s are replaced with their MLEs. Because these estimates depend on x, we must decide at what values of x to report the partial effects or elasticities. As with probit, the average values of x can be used, or, if some elements of x are qualitative variables, we can assign them values of particular interest. For the important elements of x, the partial effects or elasticities can be estimated at a range of values, holding the other elements fixed. For example, if x<sup>1</sup> is price, then we can compute equation (16.11) or (16.16), or the corresponding elasticities, for low, medium, and high prices, while keeping all other elements fixed. If x<sup>1</sup> is a dummy variable, then we can obtain the difference in estimates with x<sup>1</sup> ¼ 1 and x<sup>1</sup> ¼ 0, holding all other elements of x fixed. Standard errors of these estimates can be obtained by the delta method, although the calculations can be tedious.

Example 16.3 (Annual Hours Equation for Married Women): We use the Mroz (1987) data (MROZ.RAW ) to estimate a reduced form annual hours equation for married women. The equation is a reduced form because we do not include hourly wage offer as an explanatory variable. The hourly wage offer is unlikely to be exogenous, and, just as importantly, we cannot observe it when hours ¼ 0. We will show how to deal with both these issues in Chapter 17. For now, the explanatory variables are the same ones appearing in the labor force participation probit in Example 15.2.

Of the 753 women in the sample, 428 worked for a wage outside the home during the year; 325 of the women worked zero hours. For the women who worked positive

{537}------------------------------------------------

Table 16.1 OLS and Tobit Estimation of Annual Hours Worked

<table><tbody><tr><th colspan="4">Dependent Variable: hours</th></tr><tr><th>Independent Variable</th><th>Linear (OLS)</th><th>Tobit (MLE)</th><th></th></tr><tr><td>nwifeinc</td><td>3.45<br/>(2.54)</td><td>8.81<br/>(4.46)</td><td></td></tr><tr><td>educ</td><td>28.76<br/>(12.95)</td><td>80.65<br/>(21.58)</td><td></td></tr><tr><td>exper</td><td>65.67<br/>(9.96)</td><td>131.56<br/>(17.28)</td><td></td></tr><tr><td>exper2</td><td>.700<br/>(.325)</td><td>1.86<br/>(0.54)</td><td></td></tr><tr><td>age</td><td>30.51<br/>(4.36)</td><td>54.41<br/>(7.42)</td><td></td></tr><tr><td>kidslt6</td><td>442.09<br/>(58.85)</td><td>894.02<br/>(111.88)</td><td></td></tr><tr><td>kidsge6</td><td>32.78<br/>(23.18)</td><td>16.22<br/>(38.64)</td><td></td></tr><tr><td>constant</td><td>1,330.48<br/>(270.78)</td><td>965.31<br/>(446.44)</td><td></td></tr><tr><td>Log-likelihood value</td><td>—</td><td>3,819.09</td><td></td></tr><tr><td>R-squared</td><td>.266</td><td>.275</td><td></td></tr><tr><td>s^</td><td>750.18</td><td>1,122.02</td><td></td></tr></tbody></table>

hours, the range is fairly broad, ranging from 12 to 4,950. Thus, annual hours worked is a reasonable candidate for a Tobit model. We also estimate a linear model (using all 753 observations) by OLS. The results are in Table 16.1.

Not surprisingly, the Tobit coefficient estimates are the same sign as the corresponding OLS estimates, and the statistical significance of the estimates is similar. (Possible exceptions are the coefficients on nwifeinc and kidsge6, but the t statistics have similar magnitudes.) Second, though it is tempting to compare the magnitudes of the OLS estimates and the Tobit estimates, such comparisons are not very informative. We must not think that, because the Tobit coefficient on kidslt6 is roughly twice that of the OLS coefficient, the Tobit model somehow implies a much greater response of hours worked to young children.

We can multiply the Tobit estimates by the adjustment factors in equations (16.11) and (16.16), evaluated at the estimates and the mean values of the xj (but where we square exper rather than use the average of the exper<sup>2</sup> <sup>i</sup> Þ, to obtain the partial effects on the conditional expectations. The factor in equation (16.11) is about .451. For example, conditional on hours being positive, a year of education (starting from the mean values of all variables) is estimated to increase expected hours by about 

{538}------------------------------------------------

 $.451(80.65) \approx 36.4$  hours. Using the approximation for one more young child gives a fall in expected hours by about  $(.451)(894.02) \approx 403.2$ . Of course, this figure does not make sense for a woman working less than 403.2 hours. It would be better to estimate the expected values at two different values of *kidslt6* and form the difference, rather than using the calculus approximation.

The factor in equation (16.16), again evaluated at the mean values of the  $x_j$ , is about .645. This result means that the estimated probability of a woman being in the workforce, at the mean values of the covariates, is about .645. Therefore, the magnitudes of the effects of each  $x_j$  on expected *hours*—that is, when we account for people who initially do not work, as well as those who are initially working—is larger than when we condition on *hours* > 0. We can multiply the Tobit coefficients, at least those on roughly continuous explanatory variables, by .645 to make them roughly comparable to the OLS estimates in the first column. In most cases the estimated Tobit effect at the mean values are significantly above the corresponding OLS estimate. For example, the Tobit effect of one more year of education is about .645(80.65)  $\approx$  52.02, which is well above the OLS estimate of 28.76.

We have reported an *R*-squared for both the linear regression model and the Tobit model. The *R*-squared for OLS is the usual one. For Tobit, the *R*-squared is the square of the correlation coefficient between  $y_i$  and  $\hat{y}_i$ , where  $\hat{y}_i = \Phi(\mathbf{x}_i\hat{\boldsymbol{\beta}}/\hat{\sigma})\mathbf{x}_i\hat{\boldsymbol{\beta}} + \hat{\sigma}\phi(\mathbf{x}_i\hat{\boldsymbol{\beta}}/\hat{\sigma})$  is the estimate of  $E(y | \mathbf{x} = \mathbf{x}_i)$ . This statistic is motivated by the fact that the usual *R*-squared for OLS is equal to the squared correlation between the  $y_i$  and the OLS fitted values.

Based on the *R*-squared measures, the Tobit conditional mean function fits the hours data somewhat better, although the difference is not overwhelming. However, we should remember that the Tobit estimates are not chosen to maximize an *R*-squared—they maximize the log-likelihood function—whereas the OLS estimates produce the highest *R*-squared given the linear functional form for the conditional mean.

When two additional variables, the local unemployment rate and a binary city indicator, are included, the log likelihood becomes about -3,817.89. The likelihood ratio statistic is about 2(3,819.09 - 3,817.89) = 2.40. This is the outcome of a  $\chi^2$  variate under H<sub>0</sub>, and so the *p*-value is about .30. Therefore, these two variables are jointly insignificant.

#### 16.6 Specification Issues in Tobit Models

# 16.6.1 Neglected Heterogeneity

Suppose that we are initially interested in the model

$$y = \max(0, \mathbf{x}\boldsymbol{\beta} + \gamma q + u), \qquad u \mid \mathbf{x}, q \sim \text{Normal}(0, \sigma^2)$$
 (16.24)

{539}------------------------------------------------

where q is an unobserved variable that is assumed to be independent of x and has a Normalð0; t<sup>2</sup>Þ distribution. It follows immediately that

$$y = \max(0, \mathbf{x}\boldsymbol{\beta} + v), \qquad v \mid \mathbf{x} \sim \text{Normal}(0, \sigma^2 + \gamma^2 \tau^2)$$
 (16.25)

Thus, y conditional on x follows a Tobit model, and Tobit of y on x consistently estimates *b* and h<sup>2</sup> 1s<sup>2</sup> þ g<sup>2</sup>t2. In data-censoring cases we are interested in *b*; g is of no use without observing q, and g cannot be estimated anyway. We have shown that heterogeneity independent of x and normally distributed has no important consequences in data-censoring examples.

Things are more complicated in corner solution examples because, at least initially, we are interested in Eðy j x; qÞ or Eðy j x; q; y > 0Þ. As we discussed in Sections 2.2.5 and 15.7.1, we are often interested in the average partial effects (APEs), where, say, Eðy j x; qÞ is averaged over the population distribution of q, and then derivatives or differences with respect to elements of x are obtained. From Section 2.2.5 we know that when the heterogeneity is independent of x, the APEs are obtained by finding Eðy j xÞ [or Eðy j x; y > 0Þ]. Naturally, these conditional means come from the distribution of y given x. Under the preceding assumptions, it is exactly this distribution that Tobit of y on x estimates. In other words, we estimate the desired quantities the APEs—by simply ignoring the heterogeneity. This is the same conclusion we reached for the probit model in Section 15.7.1.

If q is not normal, then these arguments do not carry over because y given x does not follow a Tobit model. But the flavor of the argument does. A more difficult issue arises when q and x are correlated, and we address this in the next subsection.