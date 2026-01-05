# Maximum Likelihood Estimation with Censored Flow Data

> Pages: 701-706

For a random draw i from the population, let ai A ½0; b denote the time at which individual i enters the initial state (the ''starting time''), let t <sup>i</sup> denote the length of time in the initial state (the duration), and let x<sup>i</sup> denote the vector of observed covariates. We assume that t <sup>i</sup> has a continuous conditional density fðt j xi; *y*Þ, t b0, where *y* is the vector of unknown parameters.

Without right censoring we would observe a random sample on ðai; t <sup>i</sup> ; xiÞ, and estimation would be a standard exercise in conditional maximum likelihood. To account for right censoring, we assume that the observed duration, ti, is obtained as

$$t_i = \min(t_i^*, c_i) \tag{20.21}$$

where ci is the censoring time for individual i. In some cases, ci is constant across i. For example, suppose t <sup>i</sup> is unemployment duration for person i, measured in weeks. If the sample design specifies that we follow each person for at most two years, at which point all people remaining unemployed after two years are censored, then c ¼ 104. If we have a fixed calendar date at which we stop tracking individuals, the censoring time differs by individual because the workers typically would become unemployed on different calendar dates. If b ¼ 1 year and we censor everyone at two years from the start of the study, the censoring times could range from 52 to 104 weeks.)

We assume that, conditional on the covariates, the true duration is independent of the starting point, ai, and the censoring time, ci:

{702}------------------------------------------------

$$D(t_i^* \mid \mathbf{x}_i, a_i, c_i) = D(t_i^* \mid \mathbf{x}_i)$$
(20.22)

where  $D(\cdot|\cdot)$  denotes conditional distribution. Assumption (20.22) clearly holds when  $a_i$  and  $c_i$  are constant for all i, but it holds under much weaker assumptions. Sometimes  $c_i$  is constant for all i, in which case assumption (20.22) holds when the duration is independent of the starting time, conditional on  $\mathbf{x}_i$ . If there are seasonal effects on the duration—for example, unemployment durations that start in the summer have a different expected length than durations that start at other times of the year—then we may have to put dummy variables for different starting dates in  $\mathbf{x}_i$  to ensure that assumption (20.22) holds. This approach would also ensure that assumption (20.22) holds when a fixed calendar date is used for censoring, implying that  $c_i$  is not constant across i. Assumption (20.22) holds for certain nonstandard censoring schemes, too. For example, if an element of  $\mathbf{x}_i$  is education, assumption (20.22) holds if, say, individuals with more education are censored more quickly.

Under assumption (20.22), the distribution of  $t_i^*$  given  $(\mathbf{x}_i, a_i, c_i)$  does not depend on  $(a_i, c_i)$ . Therefore, if the duration is not censored, the density of  $t_i = t_i^*$  given  $(\mathbf{x}_i, a_i, c_i)$  is simply  $f(t | \mathbf{x}_i; \boldsymbol{\theta})$ . The probability that  $t_i$  is censored is

$$\mathbf{P}(t_i^* \geq c_i \,|\, \mathbf{x}_i) = 1 - F(c_i \,|\, \mathbf{x}_i; \boldsymbol{\theta})$$

where  $F(t | \mathbf{x}_i; \boldsymbol{\theta})$  is the conditional cdf of  $t_i^*$  given  $\mathbf{x}_i$ . Letting  $d_i$  be a censoring indicator ( $d_i = 1$  if uncensored,  $d_i = 0$  if censored), the conditional likelihood for observation i can be written as

$$f(t_i \mid \mathbf{x}_i; \boldsymbol{\theta})^{d_i} [1 - F(t_i \mid \mathbf{x}_i; \boldsymbol{\theta})]^{(1-d_i)}$$
(20.23)

Importantly, neither the starting times,  $a_i$ , nor the length of the interval, b, plays a role in the analysis. [In fact, in the vast majority of treatments of flow data, b and  $a_i$  are not even introduced. However, it is important to know that the reason  $a_i$  is not relevant for the analysis of flow data is the conditional independence assumption in equation (20.22).] By contrast, the censoring times  $c_i$  do appear in the likelihood for censored observations because then  $t_i = c_i$ . Given data on  $(t_i, d_i, \mathbf{x}_i)$  for a random sample of size N, the maximum likelihood estimator of  $\theta$  is obtained by maximizing

$$\sum_{i=1}^{N} \{ d_i \log[f(t_i \mid \mathbf{x}_i; \boldsymbol{\theta})] + (1 - d_i) \log[1 - F(t_i \mid \mathbf{x}_i; \boldsymbol{\theta})] \}$$
 (20.24)

For the choices of  $f(\cdot | \mathbf{x}; \boldsymbol{\theta})$  used in practice, the conditional MLE regularity conditions—see Chapter 13—hold, and the MLE is  $\sqrt{N}$ -consistent and asymptotically normal. [If there is no censoring, the second term in expression (20.24) is simply dropped.]

{703}------------------------------------------------

Because the hazard function can be expressed as in equation (20.15), once we specify f , the hazard function can be estimated once we have the MLE, ^*y*. For example, the Weibull distribution with covariates has conditional density

$$f(t | \mathbf{x}_i; \boldsymbol{\theta}) = \exp(\mathbf{x}_i \boldsymbol{\beta}) \alpha t^{\alpha - 1} \exp[-\exp(\mathbf{x}_i \boldsymbol{\beta}) t^{\alpha}]$$
(20.25)

where x<sup>i</sup> contains unity as its first element for all i. [We obtain this density from Example 20.3 with g replaced by expðxi*b*Þ.] The hazard function in this case is simply lðt; xÞ ¼ expðx*b*Þata1.

Example 20.5 (Weibull Model for Recidivism Duration): Let durat be the length of time, in months, until an inmate is arrested after being released from prison. Although the duration is rounded to the nearest month, we treat durat as a continuous variable with a Weibull distribution. We are interested in how certain covariates affect the hazard function for recidivism, and also whether there is positive or negative duration dependence, once we have conditioned on the covariates. The variable workprg—a binary indicator for participation in a prison work program—is of particular interest.

The data in RECID.RAW, which comes from Chung, Schmidt, and Witte (1991), are flow data because it is a random sample of convicts released from prison during the period July 1, 1977, through June 30, 1978. The data are retrospective in that they were obtained by looking at records in April 1984, which served as the common censoring date. Because of the different starting times, the censoring times, ci, vary from 70 to 81 months. The results of the Weibull estimation are in Table 20.1.

In interpreting the estimates, we use equation (20.17). For small ^bj, we can multiply the coefficient by 100 to obtain the semielasticity of the hazard with respect to xj. (No covariates appear in logarithmic form, so there are no elasticities among the ^bj.) For example, if tserved increases by one month, the hazard shifts up by about 1.4 percent, and the effect is statistically significant. Another year of education reduces the hazard by about 2.3 percent, but the effect is insignificant at even the 10 percent level against a two-sided alternative.

The sign of the workprg coefficient is unexpected, at least if we expect the work program to have positive benefits after the inmates are released from prison. (The result is not statistically different from zero.) The reason could be that the program is ineffective or that there is self-selection into the program.

For large ^bj, we should exponentiate and subtract unity to obtain the proportionate change. For example, at any point in time, the hazard is about 100½expð:477Þ 1 ¼ 61:1 percent greater for someone with an alcohol problem than for someone without.

{704}------------------------------------------------

Table 20.1 Weibull Estimation of Criminal Recidivism

<table><tbody><tr><th>Explanatory<br/>Variable</th><th>Coefficient<br/>(Standard Error)</th><th></th></tr><tr><td>workprg</td><td>.091<br/>(.091)</td><td></td></tr><tr><td>priors</td><td>.089<br/>(.013)</td><td></td></tr><tr><td>tserved</td><td>.014<br/>(.002)</td><td></td></tr><tr><td>felon</td><td>.299<br/>(.106)</td><td></td></tr><tr><td>alcohol</td><td>.447<br/>(.106)</td><td></td></tr><tr><td>drugs</td><td>.281<br/>(.098)</td><td></td></tr><tr><td>black</td><td>.454<br/>(.088)</td><td></td></tr><tr><td>married</td><td>.152<br/>(.109)</td><td></td></tr><tr><td>educ</td><td>.023<br/>(.019)</td><td></td></tr><tr><td>age</td><td>.0037<br/>(.0005)</td><td></td></tr><tr><td>constant</td><td>3.402<br/>(0.301)</td><td></td></tr><tr><td>Observations</td><td>1,445</td><td></td></tr><tr><td>Log likelihood</td><td>1,633.03</td><td></td></tr><tr><td>a^</td><td>.806<br/>(.031)</td><td></td></tr></tbody></table>

The estimate of a is .806, and the standard error of a^ leads to a strong rejection of H0: a ¼ 1 against H0: a < 1. Therefore, there is evidence of negative duration dependence, conditional on the covariates. This means that, for a particular ex-convict, the instantaneous rate of being arrested decreases with the length of time out of prison. When the Weibull model is estimated without the covariates, a^ ¼ :770 (se ¼ :031), which shows slightly more negative duration dependence. This is a typical finding in applications of Weibull duration models: estimated a without covariate tends to be less than the estimate with covariates. Lancaster (1990, Section 10.2) contains a theoretical discussion based on unobserved heterogeneity.

When we are primarily interested in the effects of covariates on the expected duration (rather than on the hazard), we can apply a censored Tobit analysis to the

{705}------------------------------------------------

log of the duration. A Tobit analysis assumes that, for each random draw i,  $\log(t_i^*)$  given  $\mathbf{x}_i$  has a Normal( $\mathbf{x}_i \boldsymbol{\delta}, \sigma^2$ ) distribution, which implies that  $t_i^*$  given  $\mathbf{x}_i$  has a lognormal distribution. (The first element of  $\mathbf{x}_i$  is unity.) The hazard function for a lognormal distribution, conditional on  $\mathbf{x}$ , is  $\lambda(t;\mathbf{x}) = h[(\log t - \mathbf{x}\boldsymbol{\delta})/\sigma]/\sigma t$ , where  $h(z) \equiv \phi(z)/[1-\Phi(z)]$ ,  $\phi(\cdot)$  is the standard normal probability density function (pdf), and  $\Phi(\cdot)$  is the standard normal cdf. The lognormal hazard function is not monotonic and does not have the proportional hazard form. Nevertheless, the estimates of the  $\delta_j$  are easy to interpret because the model is equivalent to

$$\log(t_i^*) = \mathbf{x}_i \boldsymbol{\delta} + e_i \tag{20.26}$$

where  $e_i$  is independent of  $\mathbf{x}_i$  and normally distributed. Therefore, the  $\delta_j$  are semielasticities—or elasticities if the covariates are in logarithmic form—of the covariates on the *expected* duration.

The Weibull model can also be represented in regression form. When  $t_i^*$  given  $\mathbf{x}_i$  has density (20.25),  $\exp(\mathbf{x}_i\boldsymbol{\beta})(t_i^*)^{\alpha}$  is independent of  $\mathbf{x}_i$  and has a unit exponential distribution. Therefore, its natural log has a **type I extreme value distribution**; therefore, we can write  $\alpha \log(t_i^*) = -\mathbf{x}_i\boldsymbol{\beta} + u_i$ , where  $u_i$  is independent of  $\mathbf{x}_i$  and has density  $g(u) = \exp(u) \exp\{\exp(-u)\}$ . The mean of  $u_i$  is not zero, but, because  $u_i$  is independent of  $\mathbf{x}_i$ , we can write  $\log(t_i^*)$  exactly as in equation (20.26), where the slope coefficients are given by  $\delta_j = -\beta_j/\alpha$ , and the intercept is more complicated. Now,  $e_i$  does not have a normal distribution, but it is independent of  $\mathbf{x}_i$  with zero mean. Censoring can be handled by maximum likelihood estimation. The estimated coefficients can be compared with the censored Tobit estimates described previously to see if the estimates are sensitive to the distributional assumption.

In Example 20.5, we can obtain the Weibull estimates of the  $\delta_j$  as  $\hat{\delta}_j = -\hat{\beta}_j/\hat{\alpha}$ . (Some econometrics packages, such as Stata, allow direct estimation of the  $\delta_j$  and provide standard errors.) For example,  $\hat{\delta}_{drugs} = -.281/.806 \approx -.349$ . When the lognormal model is used, the coefficient on *drugs* is somewhat smaller in magnitude, about -.298. As another example,  $\hat{\delta}_{age} = .0046$  in the Weibull estimation and  $\hat{\delta}_{age} = .0039$  in the lognormal estimation. In both cases, the estimates have *t* statistics over six. For obtaining estimates on the expected duration, the Weibull and lognormal models give similar results. [Interestingly, the lognormal model fits the data notably better, with log likelihood = -1,597.06. This result is consistent with the findings of Chung, Schmidt, and Witte (1991).]

Sometimes we begin by specifying a parametric model for the hazard conditional on x and then use the formulas from Section 20.2 to obtain the cdf and density. This approach is easiest when the hazard leads to a tractable duration distribution, but there is no reason the hazard function must be of the proportional hazard form.

{706}------------------------------------------------

Example 20.6 (Log-Logistic Hazard with Covariates): A log-logistic hazard function with covariates is

$$\lambda(t; \mathbf{x}) = \exp(\mathbf{x}\boldsymbol{\beta})\alpha t^{\alpha - 1}/[1 + \exp(\mathbf{x}\boldsymbol{\beta})t^{\alpha}]$$
 (20.27)

where  $x_1 \equiv 1$ . From equation (20.14) with  $\gamma = \exp(\mathbf{x}\boldsymbol{\beta})$ , the cdf is

$$F(t \mid \mathbf{x}; \boldsymbol{\theta}) = 1 - [1 + \exp(\mathbf{x}\boldsymbol{\beta})t^{\alpha}]^{-1}, \qquad t \ge 0$$
(20.28)

The distribution of  $\log(t_i^*)$  given  $\mathbf{x}_i$  is logistic with mean  $-\alpha^{-1}\log\{\exp(\mathbf{x}\boldsymbol{\beta})\}=$  $-\alpha^{-1}\mathbf{x}\boldsymbol{\beta}$  and variance  $\pi^2/(3\alpha^2)$ . Therefore,  $\log(t_i^*)$  can be written as in equation (20.26) where  $e_i$  has a zero mean logistic distribution and is *independent* of  $\mathbf{x}_i$  and  $\boldsymbol{\delta}=-\alpha^{-1}\boldsymbol{\beta}$ . This is another example where the effects of the covariates on the mean duration can be obtained by an OLS regression when there is no censoring. With censoring, the distribution of  $e_i$  must be accounted for using the log likelihood in expression (20.24).