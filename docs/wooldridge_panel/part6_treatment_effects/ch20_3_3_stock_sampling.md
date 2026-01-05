# Stock Sampling

> Pages: 706-709

Flow data with right censoring are common, but other sampling schemes are also used. With **stock sampling** we randomly sample from individuals that are in the initial state at a given point in time. The population is again individuals who enter the initial state during a specified interval, [0,b]. However, rather than observe a random sample of people flowing into the initial state, we can only obtain a random sample of individuals that are in the initial state at time b. In addition to the possibility of right censoring, we may also face the problem of **left censoring**, which occurs when some or all of the starting times,  $a_i$ , are not observed. For now, we assume that (1) we observe the starting times  $a_i$  for all individuals we sample at time b and (2) we can follow sampled individuals for a certain length of time after we observe them at time b. We also allow for right censoring.

In the unemployment duration example, where the population comprises workers who became unemployed at some point during 1998, stock sampling would occur if we randomly sampled from workers who were unemployed during the last week of 1998. This kind of sampling causes a clear sample selection problem: we necessarily exclude from our sample any individual whose unemployment spell ended before the last week of 1998. Because these spells were necessarily shorter than a year, we cannot just assume that the missing observations are randomly missing.

The sample selection problem caused by stock sampling is essentially the same situation we faced in Section 17.3, where we covered the truncated regression model. Therefore, we will call this the **left truncation** problem. Kiefer (1988) calls it **length-biased sampling**.

{707}------------------------------------------------

Under the assumptions that we observe the  $a_i$  and can observe some spells past the sampling date b, left truncation is fairly easy to deal with. With the exception of replacing flow sampling with stock sampling, we make the same assumptions as in Section 20.3.2.

To account for the truncated sampling, we must modify the density in equation (20.23) to reflect the fact that part of the population is systematically omitted from the sample. Let  $(a_i, c_i, \mathbf{x}_i, t_i)$  denote a random draw from the population of all spells starting in [0,b]. We observe this vector if and only if the person is still in the initial state at time b, that is, if and only if  $a_i + t_i^* \ge b$  or  $t_i^* \ge b - a_i$ , where  $t_i^*$  is the true duration. But, under the conditional independence assumption (20.22),

$$P(t_i^* \ge b - a_i \,|\, a_i, c_i, \mathbf{x}_i) = 1 - F(b - a_i \,|\, \mathbf{x}_i; \boldsymbol{\theta})$$
(20.29)

where  $F(\cdot | \mathbf{x}_i; \boldsymbol{\theta})$  is the cdf of  $t_i^*$  given  $\mathbf{x}_i$ , as before. The correct conditional density function is obtained by dividing equation (20.23) by equation (20.29). In Problem 20.5 you are asked to adapt the arguments in Section 17.3 to also allow for right censoring. The log-likelihood function can be written as

$$\sum_{i=1}^{N} \left\{ d_i \log[f(t_i | \mathbf{x}_i; \boldsymbol{\theta})] + (1 - d_i) \log[1 - F(t_i | \mathbf{x}_i; \boldsymbol{\theta})] - \log[1 - F(b - a_i | \mathbf{x}_i; \boldsymbol{\theta})] \right\}$$
(20.30)

where, again,  $t_i = c_i$  when  $d_i = 0$ . Unlike in the case of flow sampling, with stock sampling both the starting dates,  $a_i$ , and the length of the sampling interval, b, appear in the conditional likelihood function. Their presence makes it clear that specifying the interval [0, b] is important for analyzing stock data. [Lancaster (1990, p. 183) essentially derives equation (20.30) under a slightly different sampling scheme; see also Lancaster (1979).]

Equation (20.30) has an interesting implication. If observation i is right censored at calendar date b—that is, if we do not follow the spell after the initial data collection—then the censoring time is  $c_i = b - a_i$ . Because  $d_i = 0$  for censored observations, the log likelihood for such an observation is  $\log[1 - F(c_i | \mathbf{x}_i; \boldsymbol{\theta})] - \log[1 - F(b - a_i | \mathbf{x}_i; \boldsymbol{\theta})] = 0$ . In other words, observations that are right censored at the data collection time provide no information for estimating  $\boldsymbol{\theta}$ , at least when we use equation (20.30). Consequently, the log likelihood in equation (20.30) does not identify  $\boldsymbol{\theta}$  if all units are right censored at the interview date: equation (20.30) is identically zero. The intuition for why equation (20.30) fails in this case is fairly clear: our data consist only of  $(a_i, \mathbf{x}_i)$ , and equation (20.30) is a log likelihood that is conditional on  $(a_i, \mathbf{x}_i)$ . Effectively, there is no random response variable.

{708}------------------------------------------------

Even when we censor all observed durations at the interview date, we can still estimate *y*, provided—at least in a parametric context—we specify a model for the conditional distribution of the starting times, Dðai j xiÞ. (This is essentially the problem analyzed by Nickell, 1979.) We are still assuming that we observe the ai. So, for example, we randomly sample from the pool of people unemployed in the last week of 1998 and find out when their unemployment spells began (along with covariates). We do not follow any spells past the interview date. (As an aside, if we sample unemployed people during the last week of 1998, we are likely to obtain some observations where spells began before 1998. For the population we have specified, these people would simply be discarded. If we want to include people whose spells began prior to 1998, we need to redefine the interval. For example, if durations are measured in weeks and if we want to consider durations beginning in the five-year period prior to the end of 1998, then b ¼ 260.)

For concreteness, we assume that Dðai j xiÞ is continuous on ½0; b with density kð j xi; *h*Þ. Let si denote a sample selection indicator, which is unity if we observe random draw i, that is, if t <sup>i</sup> b b ai. Estimation of *y* (and *h*) can proceed by applying CMLE to the density of ai conditional on x<sup>i</sup> and si ¼ 1. [Note that this is the only density we can hope to estimate, as our sample only consists of observations ðai; xiÞ when si ¼ 1.] This density is informative for *y* even if *h* is not functionally related to *y* (as would typically be assumed) because there are some durations that started and ended in ½0; b; we simply do not observe them. Knowing something about the starting time distribution gives us information about the duration distribution. (In the context of flow sampling, when *h* is not functionally related to *y*, the density of ai given x<sup>i</sup> is uninformative for estimating *y*; in other words, ai is ancillary for *y*.)

In Problem 20.6 you are asked to show that the density of ai conditional on observing ðai; xiÞ is

$$p(a \mid \mathbf{x}_i, s_i = 1) = k(a \mid \mathbf{x}_i; \boldsymbol{\eta})[1 - F(b - a \mid \mathbf{x}_i; \boldsymbol{\theta})]/P(s_i = 1 \mid \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\eta})$$
(20.31)

0 < a < b, where

$$P(s_i = 1 \mid \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\eta}) = \int_0^b [1 - F(b - \omega \mid \mathbf{x}_i; \boldsymbol{\theta})] k(\omega \mid \mathbf{x}_i; \boldsymbol{\eta}) d\omega$$
 (20.32)

[Lancaster (1990, Section 8.3.3) essentially obtains the right-hand side of equation (20.31) but uses the notion of backward recurrence time. The argument in Problem 20.6 is more straightforward because it is based on a standard truncation argument.] Once we have specified the duration cdf, F, and the starting time density, k, we can use conditional MLE to estimate *y* and *h*: the log likelihood for observation i is just the log of equation (20.31), evaluated at ai. If we assume that ai is independent of

{709}------------------------------------------------

 $\mathbf{x}_i$  and has a uniform distribution on [0,b], the estimation simplifies somewhat; see Problem 20.6. Allowing for a discontinuous starting time density  $k(\cdot \mid \mathbf{x}_i; \boldsymbol{\eta})$  does not materially affect equation (20.31). For example, if the interval [0,1] represents one year, we might want to allow different entry rates over the different seasons. This would correspond to a uniform distribution over each subinterval that we choose.

We now turn to the problem of left censoring, which arises with stock sampling when we do not actually know when any spell began. In other words, the  $a_i$  are not observed, and therefore neither are the true durations,  $t_i^*$ . However, we assume that we can follow spells after the interview date. Without right censoring, this assumption means we can observe the time in the current spell since the interview date, say,  $r_i$ , which we can write as  $r_i = t_i^* + a_i - b$ . We still have a left truncation problem because we only observe  $r_i$  when  $t_i^* > b - a_i$ , that is, when  $r_i > 0$ . The general approach is the same as with the earlier problems: we obtain the density of the variable that we can at least partially observe,  $r_i$  in this case, conditional on observing  $r_i$ . Problem 20.8 asks you to fill in the details, accounting also for possible right censoring.

We can easily combine stock sampling and flow sampling. For example, in the case that we observe the starting times,  $a_i$ , suppose that, at time m < b, we sample a stock of individuals already in the initial state. In addition to following spells of individuals already in the initial state, suppose we can randomly sample individuals flowing into the initial state between times m and b. Then we follow all the individuals appearing in the sample, at least until right censoring. For starting dates after m ( $a_i \ge m$ ), there is no truncation, and so the log likelihood for these observations is just as in equation (20.24). For  $a_i < m$ , the log likelihood is identical to equation (20.30) except that m replaces b. Other combinations are easy to infer from the preceding results.