# Time-Invariant Covariates

> Pages: 713-717

With time-invariant covariates, each random draw from the population consists of information on fðy1; c1Þ; ... ;ðyM; cMÞ; xg. We assume that a parametric hazard function is specified as lðt; x; *y*Þ, where *y* is the vector of unknown parameters. Let T denote the time until exit from the initial state. While we do not fully observe T, either we know which interval it falls into, or we know whether it was censored in a

{714}------------------------------------------------

particular interval. This knowledge is enough to obtain the probability that  $y_m$  takes on the value unity given  $(y_{m-1}, \ldots, y_1)$ ,  $(c_m, \ldots, c_1)$ , and  $\mathbf{x}$ . In fact, by definition this probability depends only on  $y_{m-1}$ ,  $c_m$ , and  $\mathbf{x}$ , and only two combinations yield probabilities that are not identically zero or one. These probabilities are

$$P(y_m = 0 \mid y_{m-1} = 0, \mathbf{x}, c_m = 0)$$
(20.38)

$$P(y_m = 1 | y_{m-1} = 0, \mathbf{x}, c_m = 0), \qquad m = 1, \dots, M$$
 (20.39)

(We define  $y_0 \equiv 0$  so that these equations hold for all  $m \ge 1$ .) To compute these probabilities in terms of the hazard for T, we assume that the duration is conditionally independent of censoring:

$$T$$
 is independent of  $c_1, \ldots, c_M$ , given  $\mathbf{x}$  (20.40)

This assumption allows the censoring to depend on  $\mathbf{x}$  but rules out censoring that depends on unobservables, after conditioning on  $\mathbf{x}$ . Condition (20.40) holds for fixed censoring or completely randomized censoring. (It may not hold if censoring is due to nonrandom attrition.) Under assumption (20.40) we have, from equation (20.9),

$$P(y_{m} = 1 \mid y_{m-1} = 0, \mathbf{x}, c_{m} = 0) = P(a_{m-1} \le T < a_{m} \mid T \ge a_{m-1}, \mathbf{x})$$

$$= 1 - \exp\left[-\int_{a_{m-1}}^{a_{m}} \lambda(s; \mathbf{x}, \boldsymbol{\theta}) ds\right] \equiv 1 - \alpha_{m}(\mathbf{x}, \boldsymbol{\theta})$$
(20.41)

for  $m = 1, 2, \ldots, M$ , where

$$\alpha_m(\mathbf{x}, \boldsymbol{\theta}) \equiv \exp\left[-\int_{a_{m-1}}^{a_m} \lambda(s; \mathbf{x}, \boldsymbol{\theta}) \, ds\right]$$
 (20.42)

Therefore.

$$P(y_m = 0 | y_{m-1} = 0, \mathbf{x}, c_m = 0) = \alpha_m(\mathbf{x}, \boldsymbol{\theta})$$
(20.43)

We can use these probabilities to construct the likelihood function. If, for observation i, uncensored exit occurs in interval  $m_i$ , the likelihood is

$$\left[\prod_{h=1}^{m_i-1} \alpha_h(\mathbf{x}_i, \boldsymbol{\theta})\right] \left[1 - \alpha_{m_i}(\mathbf{x}_i, \boldsymbol{\theta})\right]$$
(20.44)

The first term represents the probability of remaining in the initial state for the first  $m_i - 1$  intervals, and the second term is the (conditional) probability that T falls into interval  $m_i$ . [Because an uncensored duration must have  $m_i \le M$ , expression (20.44)

{715}------------------------------------------------

at most depends on a1ðxi; *y*Þ; ... ; aMðxi; *y*Þ.] If the duration is censored in interval mi, we know only that exit did not occur in the first mi 1 intervals, and the likelihood consists of only the first term in expression (20.44).

If di is a censoring indicator equal to one if duration i is uncensored, the log likelihood for observation i can be written as

$$\sum_{h=1}^{m_i-1} \log[\alpha_h(\mathbf{x}_i, \boldsymbol{\theta})] + d_i \log[1 - \alpha_{m_i}(\mathbf{x}_i, \boldsymbol{\theta})]$$
(20.45)

The log likelihood for the entire sample is obtained by summing expression (20.45) across all i ¼ 1; ... ; N. Under the assumptions made, this log likelihood represents the density of ðy1; ... ; yMÞ given ðc1; ... ; cMÞ and x, and so the conditional maximum likelihood theory covered in Chapter 13 applies directly. The various ways of estimating asymptotic variances and computing test statistics are available.

To implement conditional MLE, we must specify a hazard function. One hazard function that has become popular because of its flexibility is a piecewise-constant proportional hazard: for m ¼ 1; ... ; M,

$$\lambda(t; \mathbf{x}, \boldsymbol{\theta}) = \kappa(\mathbf{x}, \boldsymbol{\beta}) \lambda_m, \qquad a_{m-1} \le t < a_m$$
(20.46)

where kðx; *b*Þ > 0 [and typically kðx; *b*Þ ¼ expðx*b*Þ]. This specification allows the hazard to be different (albeit constant) over each time interval. The parameters to be estimated are *b* and *l*, where the latter is the vector of lm, m ¼ 1; ... ; M. {Because durations in ½aM; yÞ are censored at aM, we cannot estimate the hazard over the interval ½aM; yÞ.} As an example, if we have unemployment duration measured in weeks, the hazard can be different in each week. If the durations are sparse, we might assume a different hazard rate for every two or three weeks (this assumption places restrictions on the lm). With the piecewise-constant hazard and kðx; *b*Þ ¼ expðx*b*Þ, for m ¼ 1; ... ; M, we have

$$\alpha_m(\mathbf{x}, \boldsymbol{\theta}) \equiv \exp[-\exp(\mathbf{x}\boldsymbol{\beta})\lambda_m(a_m - a_{m-1})] \tag{20.47}$$

Remember, the am are known constants (often am ¼ m) and not parameters to be estimated. Usually the l<sup>m</sup> are unrestricted, in which case x does not contain an intercept.

The piecewise-constant hazard implies that the duration distribution is discontinuous at the endpoints, whereas in our discussion in Section 20.2, we assumed that the duration had a continuous distribution. A piecewise-continuous distribution causes no real problems, and the log likelihood is exactly as specified previously. Alternatively, as in Han and Hausman (1990) and Meyer (1990), we can assume that T

{716}------------------------------------------------

has a proportional hazard as in equation (20.16) with continuous baseline hazard, l0ð-Þ. Then, we can estimate *b* along with the parameters

$$\int_{a_{m-1}}^{a_m} \lambda_0(s) ds, \qquad m = 1, 2, \dots, M$$

In practice, the approaches are the same, and it is easiest to just assume a piecewiseconstant proportional hazard, as in equation (20.46).

Once the l<sup>m</sup> have been estimated along with *b*, an estimated hazard function is easily plotted: graph ^l<sup>m</sup> at the midpoint of the interval ½am1; amÞ, and connect the points.

Without covariates, maximum likelihood estimation of the l<sup>m</sup> leads to a wellknown estimator of the survivor function. Rather than derive the MLE of the survivor function, it is easier to motivate the estimator from the representation of the survivor function as a product of conditional probabilities. For m ¼ 1; ... ; M, the survivor function at time am can be written as

$$S(a_m) = P(T > a_m) = \prod_{r=1}^{m} P(T > a_r \mid T > a_{r-1})$$
(20.48)

[Because a<sup>0</sup> ¼ 0 and PðT > 0Þ ¼ 1, the r ¼ 1 term on the right-hand side of equation (20.48) is simply PðT > a1Þ.] Now, for each r ¼ 1; 2; ... ; M, let Nr denote the number of people in the risk set for interval r: Nr is the number of people who have neither left the initial state nor been censored at time ar1, which is the beginning of interval r. Therefore, N<sup>1</sup> is the number of individuals in the initial random sample; N<sup>2</sup> is the number of individuals who did not exit the initial state in the first interval, less the number of individuals censored in the first interval; and so on. Let Er be the number of people observed to leave in the rth interval—that is, in the interval ½ar<sup>1</sup>; arÞ. A consistent estimator of PðT > ar j T > ar1Þ is ðNr ErÞ=Nr, r ¼ 1; 2; ... ; M. [We must use the fact that the censoring is ignorable in the sense of assumption (20.40), so that there is no sample selection bias in using only the uncensored observations.] It follows from equation (20.48) that a consistent estimator of the survivor function at time am is

$$\hat{S}(a_m) = \prod_{r=1}^{m} [(N_r - E_r)/N_r], \qquad m = 1, 2, \dots, M$$
(20.49)

This is the Kaplan-Meier estimator of the survivor function (at the points a1; a2; ... ; aM). Lancaster (1990, Section 8.2) contains a proof that maximum likelihood estimation of the l<sup>m</sup> (without covariates) leads to the Kaplan-Meier estimator of the

{717}------------------------------------------------

survivor function. If there are no censored durations before time am, S^ðamÞ is simply the fraction of people who have not left the initial state at time am, which is obviously consistent for PðT > amÞ ¼ SðamÞ.

In the general model, we do not need to assume a proportional hazard specification within each interval. For example, we could assume a log-logistic hazard within each interval, with different parameters for each m. Because the hazard in such cases does not depend on the covariates multiplicatively, we must plug in values of x in order to plot the hazard. Sueyoshi (1995) studies such models in detail.

If the intervals ½am<sup>1</sup>; amÞ are coarser than the data—for example, unemployment is measured in weeks, but we choose ½am<sup>1</sup>; amÞ to be four weeks for all m—then we can specify nonconstant hazards within each interval. The piecewise-constant hazard corresponds to an exponential distribution within each interval. But we could specify, say, a Weibull distribution within each interval. See Sueyoshi (1995) for details.