# 15.8. Use the data set BWGHT.RAW for this problem.

> Pages: 521-526

- a. Define a binary variable, smokes, if the woman smokes during pregnancy. Estimate a probit model relating smokes to motheduc, white, and logðfamincÞ. At white ¼ 0 and faminc evaluated at the average in the sample, what is the estimated difference in the probability of smoking for a woman with 16 years of education and one with 12 years of education?
- b. Do you think faminc is exogenous in the smoking equation? What about motheduc?
- c. Assume that motheduc and white are exogenous in the probit from part a. Also assume that fatheduc is exogenous to this equation. Estimate the reduced form for logðfamincÞ to see if fatheduc is partially correlated with logðfamincÞ.
- d. Test the null hypothesis that logðfamincÞ is exogenous in the probit from part a.
- 15.9. Assume that the binary variable y follows a linear probability model.
- a. Write down the log-likelihood function for observation i.
- b. Why might maximum likelihood estimation of the LPM be difficult?

{522}------------------------------------------------

- c. Assuming that you can estimate the LPM by MLE, explain why it is valid, as a model selection device, to compare the log likelihood from the LPM with that from logit or probit.
- 15.10. Suppose you wish to use goodness-of-fit measures to compare the LPM with a model such as logit or probit, after estimating the LPM by ordinary least squares. The usual R-squared from OLS estimation measures the proportion of the variance in y that is explained by P^ðy ¼ 1 j xÞ ¼ x ^*b*.
- a. Explain how to obtain a comparable R-squared measured for the general index model Pðy ¼ 1 j xÞ ¼ Gðx*b*Þ.
- b. Compute the R-squared measures using the data in CRIME.RAW, where the dependent variable is arr86 and the explanatory variables are pcnv, pcnv2, avgsen, tottime, ptime86, ptime862, inc86, inc862, black, hispan, and born60. Are the Rsquareds substantially different?
- 15.11. List assumptions under which the pooled probit estimator is a conditional MLE based on the distribution of y<sup>i</sup> given xi, where y<sup>i</sup> is the T 1 vector of binary outcomes and x<sup>i</sup> is the vector of all explanatory variables across all T time periods.
- 15.12. Find Pðyi<sup>1</sup> ¼ 1; yi<sup>2</sup> ¼ 0; yi<sup>3</sup> ¼ 0 j xi; ci; ni ¼ 1Þ in the fixed effects logit model with T ¼ 3.
- 15.13. Suppose that you have a control group, A, and a treatment group, B, and two periods of data. Between the two years, a new policy is implemented that affects group B; see Section 6.3.1.
- a. If your outcome variable is binary (for example, an employment indicator), and you have no covariates, how would you estimate the effect of the policy?
- b. If you have covariates, write down a probit model that allows you to estimate the effect of the policy change. Explain in detail how you would estimate this effect.
- c. How would you get an asymptotic 95 percent confidence interval for the estimate in part b?
- 15.14. Use the data in PENSION.RAW for this example.
- a. Estimate a linear model for pctstck, where the explanatory variables are choice, age, educ, female, black, married, finc25; ... ; finc101, wealth89, and prftshr. Why might you compute heteroskedasticity-robust standard errors?
- b. The sample contains separate observations for some husband-wife pairs. Compute standard errors of the estimates from the model in part a that account for the cluster

{523}------------------------------------------------

correlation within family. (These should also be heteroskedasticity-robust.) Do the standard errors differ much from the usual OLS standard errors, or from the heteroskedasticity-robust standard errors?

- c. Estimate the model from part a by ordered probit. Estimate Eðpctstck j xÞ for a single, nonblack female with 12 years of education who is 60 years old. Assume she has net worth (in 1989) equal to \$150,000 and earns \$45,000 a year, and her plan is not profit sharing. Compare this with the estimate of Eðpctstck j xÞ from the linear model.
- d. If you want to choose between the linear model and ordered probit based on how well each estimates Eðy j xÞ, how would you proceed?
- 15.15. Suppose that you are hired by a university to estimate the effect of drug usage on college grade point average of undergraduates. The survey data given to you had students choose a range of grade point averages: less than 1.0, 1.0 to 1.5, and so on, with the last interval being 3.5 to 4.0. You have data on family background variables, drug usage, and standardized test scores such as the SAT or ACT. What approach would you use? Provide enough detail so that someone can implement your suggested method.
- 15.16. Let wtpi denote the willingness of person i from a population to pay for a new public project, such as a new park or the widening of an existing highway. You are interested in the effects of various socioeconomic variables on wtp, and you specify the population model wtp ¼ x*b* þ u, where x is 1 K and Eðu j xÞ ¼ 0. Rather than observe wtpi, each person in the sample is presented with a cost of the project, ri. At this cost the person either favors or does not favor the project. Let yi ¼ 1 if person i favors the project and zero otherwise.
- a. Assume that yi ¼ 1 if and only if wtpi > ri. If ui is independent of ðxi;riÞ and is distributed as Normalð0; s<sup>2</sup>Þ, find Pðyi ¼ 1 j xi;riÞ. In particular, show that this probability follows a probit model with parameters depending on *b* and s.
- b. Let *g*^ be the K 1 vector of estimates on x, and let ^d be the coefficient on ri, from the probit of yi on xi, ri. Given these estimates, how would you estimate *b* and s?
- c. How would you estimate *b* and s directly?
- d. Now suppose ui is independent of ðxi;riÞ with cdf Gð ; *d*Þ, where *d* is an R 1 vector of parameters. Write down the log likelihood for observation i as a function of *b* and *d*.
- e. Does it make sense to compare the estimates of *b* for different choices of Gð ; *d*Þ in part d? Explain.

{524}------------------------------------------------

- **15.17.** Let  $y_1, y_2, \ldots, y_G$  be a set of discrete outcomes representing a population. These could be outcomes for the same individual, family, firm, and so on. Some entries could be binary outcomes, others might be ordered outcomes. For a vector of conditioning variables  $\mathbf{x}$  and unobserved heterogeneity c, assume that  $y_1, y_2, \ldots, y_G$  are independent conditional on  $(\mathbf{x}, c)$ , where  $f_g(\cdot | \mathbf{x}, c; \gamma_0^g)$  is the density of  $y_g$  given  $(\mathbf{x}, c)$ , where  $\gamma_0^g$  is a  $P_g$ -vector of parameters. For example, if  $y_1$  is a binary outcome,  $f_1(\cdot | \mathbf{x}, c; \gamma_0^1)$  might represent a probit model with response probability  $\Phi(\mathbf{x}\gamma_0^1 + c)$ .
- a. Write down the density of  $\mathbf{y} = (y_1, y_2, \dots, y_G)$  given  $(\mathbf{x}, c)$ .
- b. Let  $h(\cdot | \mathbf{x}; \boldsymbol{\delta}_0)$  be the density of c given  $\mathbf{x}$ , where  $\boldsymbol{\delta}_0$  is a vector of parameters. Find the density of  $\mathbf{y}$  given  $\mathbf{x}$ . Are the  $y_a$  independent conditional on  $\mathbf{x}$ ? Explain.
- c. Find the log likelihood for any random draw  $(\mathbf{x}_i, \mathbf{y}_i)$ .
- **15.18.** Consider Chamberlain's random effects probit model under assumptions (15.60) and (15.61), but replace assumption (15.67) with
- $c_i \mid \mathbf{x}_i \sim \text{Normal}[\psi + \overline{\mathbf{x}}_i \xi, \sigma_a^2 \exp(\overline{\mathbf{x}}_i \lambda)]$
- so that  $c_i$  given  $\overline{\mathbf{x}}_i$  has exponential heteroskedasticity.
- a. Find  $P(y_{it} = 1 \mid \mathbf{x}_i, a_i)$ , where  $a_i = c_i E(c_i \mid \mathbf{x}_i)$ . Does this probability differ from the probability under assumption (15.67)? Explain.
- b. Derive the log-likelihood function by first finding the density of  $(y_{i1}, \ldots, y_{iT})$  given  $\mathbf{x}_i$ . Does it have similarities with the log-likelihood function under assumption (15.67)?
- c. Assuming you have estimated  $\boldsymbol{\beta}$ ,  $\psi$ ,  $\boldsymbol{\xi}$ ,  $\sigma_a^2$ , and  $\boldsymbol{\lambda}$  by CMLE, how would you estimate the average partial effects? {Hint: First show that  $E[\Phi(\mathbf{x}^{\circ}\boldsymbol{\beta} + \psi + \overline{\mathbf{x}}_i\boldsymbol{\xi} + a_i) \mid \mathbf{x}_i] = \Phi(\{\mathbf{x}^{\circ}\boldsymbol{\beta} + \psi + \overline{\mathbf{x}}_i\boldsymbol{\xi}\}/\{1 + \sigma_a^2 \exp(\overline{\mathbf{x}}_i\boldsymbol{\lambda})\}^{1/2})$ , and then use the appropriate average across i.}
- **15.19.** Use the data in KEANE.RAW for this question, and restrict your attention to black men who are in the sample all 11 years.
- a. Use pooled probit to estimate the model  $P(employ_{i,t-1}) = \Phi(\delta_0 + pemploy_{i,t-1})$ . What assumption is needed to ensure that the usual standard errors and test statistics from pooled probit are asymptotically valid?
- b. Estimate  $P(employ_t = 1 | employ_{t-1} = 1)$  and  $P(employ_t = 1 | employ_{t-1} = 0)$ . Explain how you would obtain standard errors of these estimates.
- c. Add a full set of year dummies to the analysis in part a, and estimate the probabilities in part b for 1987. Are there important differences with the estimates in part b?

{525}------------------------------------------------

d. Now estimate a dynamic unobserved effects model using the method described in Section 15.8.4. In particular, add  $employ_{i,81}$  as an additional explanatory variable, and use random effects probit software. Use a full set of year dummies.

- e. Is there evidence of state dependence, conditional on  $c_i$ ? Explain.
- f. Average the estimated probabilities across  $employ_{i,81}$  to get the average partial effect for 1987. Compare the estimates with the effects estimated in part c.
- **15.20.** A nice feature of the Rivers and Vuong (1988) approach to estimating probit models with endogenous explanatory variables—see Section 15.7.2—is that it immediately extends to models containing any nonlinear functions of the endogenous explanatory variables. Suppose that the model is

$$y_1^* = \mathbf{z}_1 \boldsymbol{\delta}_1 + \mathbf{g}(y_2) \boldsymbol{a}_1 + u_1$$

along with equations (15.40) and (15.41) and the assumption that  $(u_1, v_2)$  is independent of **z** and bivariate normal. Here,  $\mathbf{g}(y_2)$  is a row vector of functions of  $y_2$ ; for example,  $\mathbf{g}(y_2) = (y_2, y_2^2)$ . Show that

$$P(y_1 = 1 | \mathbf{z}, v_2) = \Phi\{ [\mathbf{z}_1 \boldsymbol{\delta}_1 + \mathbf{g}(y_2) \boldsymbol{a}_1 + \theta_1 v_2] / (1 - \rho_1^2)^{1/2} \}$$

so that Procedure 15.1 goes through with the minor notational change that  $\mathbf{g}(y_2)$  replaces  $y_2$  in step b; step a is unchanged.

{526}------------------------------------------------