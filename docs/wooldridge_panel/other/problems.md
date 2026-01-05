# Problems

> Pages: 721-726

- 20.1. Use the data in RECID.RAW for this problem.
- a. Using the covariates in Table 20.1, estimate equation (20.26) by censored Tobit. Verify that the log-likelihood value is 1,597.06.
- b. Plug in the mean values for priors, tserved, educ, and age, and the values workprg ¼ 0, felon ¼ 1, alcohol ¼ 1, drugs ¼ 1, black ¼ 0, and married ¼ 0, and plot the estimated hazard for the lognormal distribution. Describe what you find.
- c. Using only the uncensored observations, perform an OLS regression of log(durat) on the covariates in Table 20.1. Compare the estimates on tserved and alcohol with those from part a. What do you conclude?
- d. Now compute an OLS regression using all data—that is, treat the censored observations as if they are uncensored. Compare the estimates on tserved and alcohol from those in parts a and c.
- 20.2. Use the data in RECID.RAW to answer these questions:

{722}------------------------------------------------

716 Chapter 20

a. To the Weibull model, add the variables super (¼1 if release from prison was supervised) and rules (number of rules violations while in prison). Do the coeffi cient estimates on these new variables have the expected signs? Are they statistically significant?

- b. Add super and rules to the lognormal model, and answer the same questions as in part a.
- c. Compare the estimated effects of the rules variable on the expected duration for the Weibull and lognormal models. Are they practically different?
- 20.3. Consider the case of flow sampling, as in Section 20.3.2, but suppose that all durations are censored: di ¼ 1, i ¼ 1; ... ; N.
- a. Write down the log-likelihood function when all durations are censored.
- b. Find the special case of the Weibull distribution in part a.
- c. Consider the Weibull case where x<sup>i</sup> only contains a constant, so that Fðt; a; bÞ ¼ 1 exp½expðbÞt<sup>a</sup>. Show that the Weibull log likelihood cannot be maximized for real numbers ^b and a^.
- d. From part c, what do you conclude about estimating duration models from flow data when all durations are right censored?
- e. If the duration distribution is continuous, ci > b > 0 for some constant b, and Pðt <sup>i</sup> < tÞ > 0 for all t > 0, is it likely, in a large random sample, to find that all durations have been censored?
- 20.4. Suppose that, in the context of flow sampling, we observe covariates xi, the censoring time ci, and the binary indicator di (¼1 if the observation is uncensored). We never observe t i .
- a. Show that the conditional likelihood function has the binary response form. What is the binary ''response''?
- b. Use the Weibull model to demonstrate the following when we only observe whether durations are censored: if the censoring times ci are constant, the parameters *b* and a are not identified. [Hint: Consider the same case as in Problem 20.3c, and show that the log likelihood depends only on the constant expðbÞc<sup>a</sup>, where c is the common censoring time.]
- c. Use the lognormal model to argue that, provided the ci vary across i in the population, the parameters are generally identified. [Hint: In the binary response model, what is the coefficient on logðciÞ?]

{723}------------------------------------------------

Duration Analysis 717

20.5. In this problem you are to derive the log likelihood in equation (20.30). Assume that ci > b ai for all i, so that we always observe part of each spell after the sampling date, b. In what follows, we supress the parameter vector, *y*.

- a. For b ai < t < ci, show that Pðt <sup>i</sup> at j xi; ai; ci;si ¼ 1Þ¼½Fðt j xiÞFðbai j xiÞ= ½1 Fðb ai j xiÞ.
- b. Use part a to obtain the density of t <sup>i</sup> conditional on ðxi; ai; ci;si ¼ 1Þ for b ai < t < ci.
- c. Show that Pðti ¼ ci j xi; ai; ci;si ¼ 1Þ¼½1 Fðci j xiÞ=½1 Fðb ai j xiÞ.
- d. Explain why parts b and c lead to equation (20.30).
- 20.6. Consider the problem of stock sampling where we do not follow spells after the sampling date, b, as described in Section 20.3.3. Let Fð j xiÞ denote the cdf of t i given xi, and let kð j xiÞ denote the continuous density of ai given xi. We drop dependence on the parameters for most of the derivations. Assume that t <sup>i</sup> and ai are independent conditional on xi.
- a. Let si denote a selection indicator, so that si ¼ 1ðt <sup>i</sup> b b aiÞ. For any 0 < a < b, show that

$$P(a_i \le a, s_i = 1 \mid \mathbf{x}_i) = \int_0^a k(\omega \mid \mathbf{x}_i) [1 - F(b - \omega \mid \mathbf{x}_i)] d\omega$$

- b. Derive equation (20.32). {Hint: Pðsi ¼ 1 j xiÞ ¼ Eðsi j xiÞ ¼ E½Eðsi j ai; xiÞ j xi, and Eðsi j ai; xiÞ ¼ Pðt <sup>i</sup> bb ai j xiÞ.}
- c. For 0 < a < b, what is the cdf of ai given x<sup>i</sup> and si ¼ 1? Now derive equation (20.31).
- d. Take b ¼ 1, and assume that the starting time distribution is uniform on ½0; 1 (independent of xi). Find the density (20.31) in this case.
- e. For the setup in part d, assume that the duration cdf has the Weibull form, 1 exp½expðxi*b*Þt<sup>a</sup>. What is the log likelihood for observation i?
- 20.7. Consider the original stock sampling problem that we covered in Section 20.3.3. There, we derived the log likelihood (20.30) by conditioning on the starting times, ai. This approach is convenient because we do not have to specify a distribution for the starting times. But suppose we have an acceptable model for kð j xi; *h*Þ, the (continuous) density of ai given xi. Further, we maintain assumption (20.22) and assume Dðai j ci; xiÞ ¼ Dðai j xiÞ.
- a. Show that the log-likelihood function conditional on xi, which accounts for truncation, is

{724}------------------------------------------------

718 Chapter 20

$$\sum_{i=1}^{N} \{d_i \log[f(t_i \mid \mathbf{x}_i; \boldsymbol{\theta})] + (1 - d_i) \log[1 - F(t_i \mid \mathbf{x}_i; \boldsymbol{\theta})] + \log[k(a_i \mid \mathbf{x}_i; \boldsymbol{\eta})] - \log[P(s_i = 1 \mid \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\eta})]\}$$
(20.56)

where  $P(s_i = 1 | \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\eta})$  is given in equation (20.32).

- b. Discuss the trade-offs in using equation (20.30) or the log likelihood in (20.56).
- **20.8.** In the context of stock sampling, where we are interested in the population of durations starting in [0,b], suppose that we interview at date b, as usual, but we do not observe any starting times. {This assumption raises the issue of how we know individual i's starting time is in the specified interval, [0,b]. We assume that the interval is defined to make this condition true for all i.} Let  $r_i^* = a_i + t_i^* b$ , which can be interpreted as the calendar date at which the spell ends minus the interview date. Even without right censoring, we observe  $r_i^*$  only if  $r_i^* > 0$ , in which case  $r_i^*$  is simply the time in the spell since the interview date, b. Assume that  $t_i^*$  and  $a_i$  are independent conditional on  $\mathbf{x}_i$ .
- a. Show that for r > 0, the density of  $r_i^*$  given  $\mathbf{x}_i$  is

$$h(r \mid \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\eta}) \equiv \int_0^b k(\boldsymbol{u} \mid \mathbf{x}_i; \boldsymbol{\eta}) f(r + b - \boldsymbol{u} \mid \mathbf{x}_i; \boldsymbol{\theta}) d\boldsymbol{u}$$

where, as before,  $k(a | \mathbf{x}_i; \boldsymbol{\eta})$  is the density of  $a_i$  given  $\mathbf{x}_i$  and  $f(t | \mathbf{x}_i; \boldsymbol{\theta})$  is the duration density.

- b. Let q > 0 be a fixed censoring time after the interview date, and define  $r_i = \min(r_i^*, q)$ . Find  $P(r_i = q \mid \mathbf{x}_i)$  in terms of the *cdf* of  $r_i^*$ , say,  $H(r \mid \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\eta})$ .
- c. Use parts a and b, along with equation (20.32), to show that the log likelihood conditional on observing  $(r_i, \mathbf{x}_i)$  is

$$d_{i} \log[h(r_{i} | \mathbf{x}_{i}; \boldsymbol{\theta}, \boldsymbol{\eta})] + (1 - d_{i}) \log[1 - H(r_{i} | \mathbf{x}_{i}; \boldsymbol{\theta}, \boldsymbol{\eta})]$$

$$-\log \left\{ \int_{0}^{b} [1 - F(b - \boldsymbol{\omega} | \mathbf{x}_{i}; \boldsymbol{\theta})] k(\boldsymbol{\omega} | \mathbf{x}_{i}; \boldsymbol{\eta}) d\boldsymbol{\omega} \right\}$$
(20.57)

where  $d_i = 1$  if observation *i* has not been right censored.

- d. Simplify the log likelihood from part c when b = 1 and  $k(a | \mathbf{x}_i; \boldsymbol{\eta})$  is the uniform density on [0, 1].
- **20.9.** Consider the Weibull model with multiplicative heterogeneity, as in equation (20.33), where  $v_i$  takes on only two values,  $1/\rho$  and 0, with probabilities  $\rho$  and  $1-\rho$ ,

{725}------------------------------------------------

Duration Analysis 719

respectively, where 0 < r < 1. This parameterization imposes the normalization EðviÞ ¼ 1. You can think of a situation where there are only two types of people, type A ðvi ¼ 0Þ and type B ðvi ¼ 1=rÞ.

- a. Show that, as the difference between the two types grows, the probability of being type B must shrink to zero.
- b. Find the cdf of t <sup>i</sup> given xi.
- c. Find the log-likelihood function for observation i in terms of a, *b*, and r.
- 20.10. Let 0 < a<sup>1</sup> < a<sup>2</sup> < --- < aM<sup>1</sup> < aM be a positive, increasing set of constants, and let T be a nonnegative random variable with PðT > 0Þ ¼ 1.
- a. Show that, for any m ¼ 1; ... ; M, PðT > amÞ ¼ PðT > am j T > am1ÞPðT > am1Þ.
- b. Use part a to prove equation (20.48).

{726}------------------------------------------------