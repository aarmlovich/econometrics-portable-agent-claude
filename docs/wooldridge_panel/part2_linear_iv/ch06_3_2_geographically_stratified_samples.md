# Geographically Stratified Samples

> Pages: 146-153

Various kinds of stratified sampling, where units in the sample are represented with different frequencies than they are in the population, are also common in the social sciences. We treat general kinds of stratification in Chapter 17. Here, we discuss some issues that arise with geographical stratification, where random samples are taken from separate geographical units.

If the geographically stratified sample can be treated as being independent but not identically distributed, no substantive modifications are needed to apply the previous econometric methods. However, it is prudent to allow different intercepts across strata, and even different slopes in some cases. For example, if people are sampled from states in the United States, it is often important to include state dummy variables to allow for systematic differences in the response and explanatory variables across states.

If we are interested in the effects of variables measured at the strata level, and the individual observations are correlated because of unobserved strata effects, estimation and inference are much more complicated. A model with strata-level covariates and within-strata correlation is

$$y_{is} = \mathbf{x}_{is}\boldsymbol{\beta} + \mathbf{z}_{s}\boldsymbol{\gamma} + q_{s} + e_{is} \tag{6.34}$$

where i is for individual and s is for stratum. The covariates in xis change with the individual, while z<sup>s</sup> changes only at the strata level. That is, there is correlation in the covariates across individuals within the same stratum. The variable qs is an unobserved stratum effect. We would typically assume that the observations are independently distributed across strata, that the eis are independent across i, and that 

{147}------------------------------------------------

Eðeis j Xs; zs; qsÞ ¼ 0 for all i and s—where X<sup>s</sup> is the set of explanatory variables for all units in stratum s—and qs is an unobserved stratum effect.

The presence of the unobservable qs induces correlation in the composite error uis ¼ qs þ eis within each stratum. If we are interested in the coefficients on the individual-specific variables, that is, *b*, then there is a simple solution: include stratum dummies along with xis. That is, we estimate the model yis ¼ a<sup>s</sup> þ xis*b* þ eis by OLS, where a<sup>s</sup> is the stratum-specific intercept.

Things are more interesting when we want to estimate *g*. The OLS estimators of *b* and *g* in the regression of yis on xis, z<sup>s</sup> are still unbiased if Eðqs j Xs; zsÞ ¼ 0, but consistency and asymptotic normality are tricky, because, with a small number of strata and many observations within each stratum, the asymptotic analysis makes sense only if the number of observations within each stratum grows, usually with the number of strata fixed. Because the observations within a stratum are correlated, the usual law of large numbers and central limit theorem cannot be applied. By means of a simulation study, Moulton (1990) shows that ignoring the within-group correlation when obtaining standard errors for ^*g* can be very misleading. Moulton also gives some corrections to the OLS standard errors, but it is not clear what kind of asymptotic analysis justifies them.

If the strata are, say, states in the United States, and we are interested in the effect of state-level policy variables on economic behavior, one way to proceed is to use state-level data on all variables. This avoids the within-stratum correlation in the composite error in equation (6.34). A drawback is that state policies that can be taken as exogenous at the individual level are often endogenous at the aggregate level. However, if z<sup>s</sup> in equation (6.34) contains policy variables, perhaps we should question whether these would be uncorrelated with qs. If qs and z<sup>s</sup> are correlated, OLS using individual-level data would be biased and inconsistent.

Related issues arise when aggregate-level variables are used as instruments in equations describing individual behavior. For example, in a birth weight equation, Currie and Cole (1993) use measures of state-level AFDC benefits as instruments for individual women's participation in AFDC. (Therefore, the binary endogenous explanatory variable is at the individual level, while the instruments are at the state level.) If state-level AFDC benefits are exogenous in the birth weight equation, and AFDC participation is sufficiently correlated with state benefit levels—a question that can be checked using the first-stage regression—then the IV approach will yield a consistent estimator of the effect of AFDC participation on birth weight.

Moffitt (1996) discusses assumptions under which using aggregate-level IVs yields consistent estimators. He gives the example of using observations on workers from two cities to estimate the impact of job training programs. In each city, some people

{148}------------------------------------------------

received some job training while others did not. The key element in xis is a job training indicator. If, say, city A exogenously offered more job training slots than city B, a city dummy variable can be used as an IV for whether each worker received training. See Moffitt (1996) and Problem 5.13b for an interpretation of such estimators.

If there are unobserved group effects in the error term, then at a minimum, the usual 2SLS standard errors will be inappropriate. More problematic is that aggregatelevel variables might be correlated with qs. In the birth weight example, the level of AFDC benefits might be correlated with unobserved health care quality variables that are in qs. In the job training example, city A may have spent more on job training because its workers are, on average, less productive than the workers in city B. Unfortunately, controlling for qs by putting in strata dummies and applying 2SLS does not work: by definition, the instruments only vary across strata—not within strata—and so *b* in equation (6.34) would be unidentified. In the job training example, we would put in a dummy variable for city of residence as an explanatory variable, and therefore we could not use this dummy variable as an IV for job training participation: we would be short one instrument.

#### 6.3.3 Spatial Dependence

As the previous subsection suggests, cross section data that are not the result of independent sampling can be difficult to handle. Spatial correlation, or, more generally, spatial dependence, typically occurs when cross section units are large relative to the population, such as when data are collected at the county, state, province, or country level. Outcomes from adjacent units are likely to be correlated. If the correlation arises mainly through the explanatory variables (as opposed to unobservables), then, practically speaking, nothing needs to be done (although the asymptotic analysis can be complicated). In fact, sometimes covariates for one county or state appear as explanatory variables in the equation for neighboring units, as a way of capturing spillover effects. This fact in itself causes no real difficulties.

When the unobservables are correlated across nearby geographical units, OLS can still have desirable properties—often unbiasedness, consistency, and asymptotic normality can be established—but the asymptotic arguments are not nearly as unified as in the random sampling case, and estimating asymptotic variances becomes difficult.

# 6.3.4 Cluster Samples

Cluster sampling is another case where cross section observations are correlated, but it is somewhat easier to handle. The key is that we randomly sample a large number of clusters, and each cluster consists of relatively few units (compared with the overall sample size). While we allow the units within each cluster to be correlated, we assume 

{149}------------------------------------------------

independence across clusters. An example is studying teenage peer effects using a large sample of neighborhoods (the clusters) with relatively few teenagers per neighborhood. Or, using siblings in a large sample of families. The asymptotic analysis is with fixed cluster sizes with the number of clusters getting large. As we will see in Section 11.5, handling within-cluster correlation in this context is relatively straightforward. In fact, when the explanatory variables are exogenous, OLS is consistent and asymptotically normal, but the asymptotic variance matrix needs to be adjusted. The same holds for 2SLS.

#### Problems

- 6.1. a. In Problem 5.4d, test the null hypothesis that educ is exogenous.
- b. Test the the single overidentifying restriction in this example.
- 6.2. In Problem 5.8b, test the null hypothesis that educ and IQ are exogenous in the equation estimated by 2SLS.
- 6.3. Consider a model for individual data to test whether nutrition affects productivity (in a developing country):

$$log(\textit{produc}) = \delta_0 + \delta_1 exper + \delta_2 exper^2 + \delta_3 educ + \alpha_1 calories + \alpha_2 \textit{protein} + u_1$$
 (6.35)

where produc is some measure of worker productivity, calories is caloric intake per day, and protein is a measure of protein intake per day. Assume here that exper, exper2, and educ are all exogenous. The variables calories and protein are possibly correlated with u<sup>1</sup> (see Strauss and Thomas, 1995, for discussion). Possible instrumental variables for calories and protein are regional prices of various goods such as grains, meats, breads, dairy products, and so on.

- a. Under what circumstances do prices make good IVs for calories and proteins? What if prices reflect quality of food?
- b. How many prices are needed to identify equation (6.35)?
- c. Suppose we have M prices, p1; ... ; pM. Explain how to test the null hypothesis that calories and protein are exogenous in equation (6.35).
- 6.4. Consider a structural linear model with unobserved variable q:

$$y = \mathbf{x}\boldsymbol{\beta} + q + v, \qquad \mathbf{E}(v \mid \mathbf{x}, q) = 0$$

{150}------------------------------------------------

Suppose, in addition, that  $E(q | \mathbf{x}) = \mathbf{x} \boldsymbol{\delta}$  for some  $K \times 1$  vector  $\boldsymbol{\delta}$ ; thus, q and  $\mathbf{x}$  are possibly correlated.

- a. Show that  $E(y | \mathbf{x})$  is linear in  $\mathbf{x}$ . What consequences does this fact have for tests of functional form to detect the presence of q? Does it matter how strongly q and  $\mathbf{x}$  are correlated? Explain.
- b. Now add the assumptions  $\operatorname{Var}(v \mid \mathbf{x}, q) = \sigma_v^2$  and  $\operatorname{Var}(q \mid \mathbf{x}) = \sigma_q^2$ . Show that  $\operatorname{Var}(y \mid \mathbf{x})$  is constant. [Hint:  $\operatorname{E}(qv \mid \mathbf{x}) = 0$  by iterated expectations.] What does this fact imply about using tests for heteroskedasticity to detect omitted variables?
- c. Now write the equation as  $y = \mathbf{x}\boldsymbol{\beta} + u$ , where  $E(\mathbf{x}'u) = \mathbf{0}$  and  $Var(u \mid \mathbf{x}) = \sigma^2$ . If  $E(u \mid \mathbf{x}) \neq E(u)$ , argue that an LM test of the form (6.28) will detect "heteroskedasticity" in u, at least in large samples.
- **6.5.** a. Verify equation (6.29) under the assumptions  $E(u \mid \mathbf{x}) = 0$  and  $E(u^2 \mid \mathbf{x}) = \sigma^2$ .
- b. Show that, under the additional assumption (6.27),

$$E[(u_i^2 - \sigma^2)^2 (\mathbf{h}_i - \boldsymbol{\mu}_h)'(\mathbf{h}_i - \boldsymbol{\mu}_h)] = \eta^2 E[(\mathbf{h}_i - \boldsymbol{\mu}_h)'(\mathbf{h}_i - \boldsymbol{\mu}_h)]$$
  
where  $\eta^2 = E[(u^2 - \sigma^2)^2]$ .

- c. Explain why parts a and b imply that the LM statistic from regression (6.28) has a limiting  $\chi_O^2$  distribution.
- d. If condition (6.27) does not hold, obtain a consistent estimator of  $\mathrm{E}[(u_i^2-\sigma^2)^2(\mathbf{h}_i-\boldsymbol{\mu}_h)'(\mathbf{h}_i-\boldsymbol{\mu}_h)]$ . Show how this leads to the heterokurtosis-robust test for heteroskedasticity.
- **6.6.** Using the test for heteroskedasticity based on the auxiliary regression  $\hat{u}^2$  on  $\hat{y}$ ,  $\hat{y}^2$ , test the  $\log(wage)$  equation in Example 6.4 for heteroskedasticity. Do you detect heteroskedasticity at the 5 percent level?
- **6.7.** For this problem use the data in HPRICE.RAW, which is a subset of the data used by Kiel and McClain (1995). The file contains housing prices and characteristics for two years, 1978 and 1981, for homes sold in North Andover, Massachusetts. In 1981 construction on a garbage incinerator began. Rumors about the incinerator being built were circulating in 1979, and it is for this reason that 1978 is used as the base year. By 1981 it was very clear that the incinerator would be operating soon.
- a. Using the 1981 cross section, estimate a bivariate, constant elasticity model relating housing price to distance from the incinerator. Is this regression appropriate for determining the causal effects of incinerator on housing prices? Explain.
- b. Pooling the two years of data, consider the model


{151}------------------------------------------------

$$\log(price) = \delta_0 + \delta_1 y 81 + \delta_2 \log(dist) + \delta_3 y 81 \cdot \log(dist) + u$$

If the incinerator has a negative effect on housing prices for homes closer to the incinerator, what sign is d3? Estimate this model and test the null hypothesis that building the incinerator had no effect on housing prices.

- c. Add the variables log(intst), ½logðintstÞ<sup>2</sup> , log(area), log(land ), age, age2, rooms, baths to the model in part b, and test for an incinerator effect. What do you conclude?
- 6.8. The data in FERTIL1.RAW are a pooled cross section on more than a thousand U.S. women for the even years between 1972 and 1984, inclusive; the data set is similar to the one used by Sander (1992). These data can be used to study the relationship between women's education and fertility.
- a. Use OLS to estimate a model relating number of children ever born to a woman (kids) to years of education, age, region, race, and type of environment reared in. You should use a quadratic in age and should include year dummies. What is the estimated relationship between fertility and education? Holding other factors fixed, has there been any notable secular change in fertility over the time period?
- b. Reestimate the model in part a, but use motheduc and fatheduc as instruments for educ. First check that these instruments are sufficiently partially correlated with educ. Test whether educ is in fact exogenous in the fertility equation.
- c. Now allow the effect of education to change over time by including interaction terms such as y74educ, y76educ, and so on in the model. Use interactions of time dummies and parents' education as instruments for the interaction terms. Test that there has been no change in the relationship between fertility and education over time.
- 6.9. Use the data in INJURY.RAW for this question.
- a. Using the data for Kentucky, reestimate equation (6.33) adding as explanatory variables male, married, and a full set of industry- and injury-type dummy variables. How does the estimate on afchngehighearn change when these other factors are controlled for? Is the estimate still statistically significant?
- b. What do you make of the small R-squared from part a? Does this mean the equation is useless?
- c. Estimate equation (6.33) using the data for Michigan. Compare the estimate on the interaction term for Michigan and Kentucky, as well as their statistical significance.
- 6.10. Consider a regression model with interactions and squares of some explanatory variables: Eðy j xÞ ¼ z*b*, where z contains a constant, the elements of x, and quadratics and interactions of terms in x.

{152}------------------------------------------------

a. Let  $\mu = E(\mathbf{x})$  be the population mean of  $\mathbf{x}$ , and let  $\overline{\mathbf{x}}$  be the sample average based on the N available observations. Let  $\hat{\boldsymbol{\beta}}$  be the OLS estimator of  $\boldsymbol{\beta}$  using the N observations on y and  $\mathbf{z}$ . Show that  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})$  and  $\sqrt{N}(\overline{\mathbf{x}} - \boldsymbol{\mu})$  are asymptotically uncorrelated. [Hint: Write  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})$  as in equation (4.8), and ignore the  $o_p(1)$  term. You will need to use the fact that  $E(u | \mathbf{x}) = 0$ .]

b. In the model of Problem 4.8, use part a to argue that

$$\operatorname{Avar}(\hat{\alpha}_1) = \operatorname{Avar}(\tilde{\alpha}_1) + \beta_3^2 \operatorname{Avar}(\bar{x}_2) = \operatorname{Avar}(\tilde{\alpha}_1) + \beta_3^2 (\sigma_2^2/N)$$

where  $\alpha_1 = \beta_1 + \beta_3 \mu_2$ ,  $\tilde{\alpha}_1$  is the estimator of  $\alpha_1$  if we knew  $\mu_2$ , and  $\sigma_2^2 = \text{Var}(x_2)$ .

- c. How would you obtain the correct asymptotic standard error of  $\hat{\alpha}_1$ , having run the regression in Problem 4.8d? [Hint: The standard error you get from the regression is really  $se(\tilde{\alpha}_1)$ . Thus you can square this to estimate  $Avar(\tilde{\alpha}_1)$ , then use the preceding formula. You need to estimate  $\sigma_2^2$ , too.]
- d. Apply the result from part c to the model in Problem 4.8; in particular, find the corrected asymptotic standard error for  $\hat{\alpha}_1$ , and compare it with the uncorrected one from Problem 4.8d. (Both can be nonrobust to heteroskedasticity.) What do you conclude?
- **6.11.** The following wage equation represents the populations of working people in 1978 and 1985:

$$\log(wage) = \beta_0 + \delta_0 y85 + \beta_1 educ + \delta_1 y85 \cdot educ + \beta_2 exper$$
$$+ \beta_2 exper^2 + \beta_4 union + \beta_5 female + \delta_5 y85 \cdot female + u$$

where the explanatory variables are standard. The variable *union* is a dummy variable equal to one if the person belongs to a union and zero otherwise. The variable *y85* is a dummy variable equal to one if the observation comes from 1985 and zero if it comes from 1978. In the file CPS78\_85.RAW there are 550 workers in the sample in 1978 and a different set of 534 people in 1985.

- a. Estimate this equation and test whether the return to education has changed over the seven-year period.
- b. What has happened to the gender gap over the period?
- c. Wages are measured in nominal dollars. What coefficients would change if we measure wage in 1978 dollars in both years? [Hint: Use the fact that for all 1985 observations,  $\log(wage_i/P85) = \log(wage_i) \log(P85)$ , where P85 is the common deflator; P85 = 1.65 according to the Consumer Price Index.]
- d. Is there evidence that the variance of the error has changed over time?

{153}------------------------------------------------

- e. With wages measured nominally, and holding other factors fixed, what is the estimated increase in nominal wage for a male with 12 years of education? Propose a regression to obtain a confidence interval for this estimate. (Hint: You must replace y85·educ with something else.)
- **6.12.** In the linear model  $y = \mathbf{x}\boldsymbol{\beta} + u$ , assume that Assumptions 2SLS.1 and 2SLS.3 hold with  $\mathbf{w}$  in place of  $\mathbf{z}$ , where  $\mathbf{w}$  contains all nonredundant elements of  $\mathbf{x}$  and  $\mathbf{z}$ . Further, assume that the rank conditions hold for OLS and 2SLS. Show that

$$\operatorname{Avar}[\sqrt{N}(\hat{\pmb{\beta}}_{2\mathrm{SLS}} - \hat{\pmb{\beta}}_{\mathrm{OLS}})] = \operatorname{Avar}[\sqrt{N}(\hat{\pmb{\beta}}_{2\mathrm{SLS}} - \pmb{\beta})] - \operatorname{Avar}[\sqrt{N}(\hat{\pmb{\beta}}_{\mathrm{OLS}} - \pmb{\beta})]$$

[Hint: First,  $\operatorname{Avar}[\sqrt{N}(\hat{\pmb{\beta}}_{2SLS} - \hat{\pmb{\beta}}_{OLS})] = \mathbf{V}_1 + \mathbf{V}_2 - (\mathbf{C} + \mathbf{C}')$ , where  $\mathbf{V}_1 = \operatorname{Avar}[\sqrt{N}(\hat{\pmb{\beta}}_{2SLS} - \pmb{\beta})]$ ,  $\mathbf{V}_2 = \operatorname{Avar}[\sqrt{N}(\hat{\pmb{\beta}}_{OLS} - \pmb{\beta})]$ , and  $\mathbf{C}$  is the asymptotic covariance between  $\sqrt{N}(\hat{\pmb{\beta}}_{2SLS} - \pmb{\beta})$  and  $\sqrt{N}(\hat{\pmb{\beta}}_{OLS} - \pmb{\beta})$ . You can stack the formulas for the 2SLS and OLS estimators and show that  $\mathbf{C} = \sigma^2[\mathbf{E}(\mathbf{x}^*/\mathbf{x}^*)]^{-1}\mathbf{E}(\mathbf{x}^*/\mathbf{x})[\mathbf{E}(\mathbf{x}'\mathbf{x})]^{-1} = \sigma^2[\mathbf{E}(\mathbf{x}'\mathbf{x})]^{-1} = \mathbf{V}_2$ . To show the second equality, it will be helpful to use  $\mathbf{E}(\mathbf{x}^*/\mathbf{x}) = \mathbf{E}(\mathbf{x}^*/\mathbf{x}^*)$ .]