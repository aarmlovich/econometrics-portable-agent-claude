# **20.3.4** Unobserved Heterogeneity

> Pages: 709-713

One way to obtain more general duration models is to introduce unobserved heterogeneity into fairly simple duration models. In addition, we sometimes want to test for duration dependence conditional on observed covariates *and* unobserved heterogeneity. The key assumptions used in most models that incorporate unobserved heterogeneity are that (1) the heterogeneity is *independent* of the observed covariates, as well as starting times and censoring times; (2) the heterogeneity has a distribution known up to a finite number of parameters; and (3) the heterogeneity enters the hazard function multiplicatively. We will make these assumptions. In the context of single-spell flow data, it is difficult to relax any of these assumptions. (In the special case of a lognormal duration distribution, we can relax assumption 1 by using Tobit methods with endogenous explanatory variables; see Section 16.6.2.)

{710}------------------------------------------------

Before we cover the general case, it is useful to cover an example due to Lancaster (1979). For a random draw i from the population, a Weibull hazard function conditional on observed covariates  $\mathbf{x}_i$  and unobserved heterogeneity  $v_i$  is

$$\lambda(t; \mathbf{x}_i, v_i) = v_i \exp(\mathbf{x}_i \boldsymbol{\beta}) \alpha t^{\alpha - 1}$$
(20.33)

where  $x_{i1} \equiv 1$  and  $v_i > 0$ . [Lancaster (1990) calls equation (20.33) a conditional hazard, because it conditions on the unobserved heterogeneity  $v_i$ . Technically, almost all hazards in econometrics are conditional because we almost always condition on observed covariates.] Notice how  $v_i$  enters equation (20.33) multiplicatively. To identify the parameters  $\alpha$  and  $\beta$  we need a normalization on the distribution of  $v_i$ ; we use the most common,  $E(v_i) = 1$ . This implies that, for a given vector  $\mathbf{x}$ , the average hazard is  $\exp(\mathbf{x}\boldsymbol{\beta})\alpha t^{\alpha-1}$ . An interesting hypothesis is  $H_0$ :  $\alpha = 1$ , which means that, conditional on  $\mathbf{x}_i$  and  $v_i$ , there is no duration dependence.

In the general case where the cdf of  $t_i^*$  given  $(\mathbf{x}_i, v_i)$  is  $F(t | \mathbf{x}_i, v_i; \boldsymbol{\theta})$ , we can obtain the distribution of  $t_i^*$  given  $\mathbf{x}_i$  by integrating out the unobserved effect. Because  $v_i$  and  $\mathbf{x}_i$  are independent, the cdf of  $t_i^*$  given  $\mathbf{x}_i$  is

$$G(t \mid \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\rho}) = \int_0^\infty F(t \mid \mathbf{x}_i, v; \boldsymbol{\theta}) h(v; \boldsymbol{\rho}) dv$$
 (20.34)

where, for concreteness, the density of  $v_i$ ,  $h(\cdot; \boldsymbol{\rho})$ , is assumed to be continuous and depends on the unknown parameters  $\boldsymbol{\rho}$ . From equation (20.34) the density of  $t_i^*$  given  $\mathbf{x}_i$ ,  $g(t | \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\rho})$ , is easily obtained. We can now use the methods of Sections 20.3.2 and 20.3.3. For flow data, the log-likelihood function is as in equation (20.24), but with  $G(t | \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\rho})$  replacing  $F(t | \mathbf{x}_i; \boldsymbol{\theta})$  and  $g(t | \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\rho})$  replacing  $f(t | \mathbf{x}_i; \boldsymbol{\theta})$ . We should assume that  $D(t_i^* | \mathbf{x}_i, v_i, a_i, c_i) = D(t_i^* | \mathbf{x}_i, v_i)$  and  $D(v_i | \mathbf{x}_i, a_i, c_i) = D(v_i)$ ; these assumptions ensure that the key condition (20.22) holds. The methods for stock sampling described in Section 20.3.3 also apply to the integrated cdf and density.

If we assume **gamma-distributed heterogeneity**—that is,  $v_i \sim \text{Gamma}(\delta, \delta)$ , so that  $E(v_i) = 1$  and  $Var(v_i) = 1/\delta$ —we can find the distribution of  $t_i^*$  given  $\mathbf{x}_i$  for a broad class of hazard functions with multiplicative heterogeneity. Suppose that the hazard function is  $\lambda(t; \mathbf{x}_i, v_i) = v_i \kappa(t; \mathbf{x}_i)$ , where  $\kappa(t; \mathbf{x}) > 0$  (and need not have the proportional hazard form). For simplicity, we suppress the dependence of  $\kappa(\cdot; \cdot)$  on unknown parameters. From equation (20.7), the cdf of  $t_i^*$  given  $(\mathbf{x}_i, v_i)$  is

$$F(t \mid \mathbf{x}_i, v_i) = 1 - \exp\left[-v_i \int_0^t \kappa(s; \mathbf{x}_i) \, ds\right] \equiv 1 - \exp\left[-v_i \xi(t; \mathbf{x}_i)\right]$$
(20.35)

where  $\xi(t; \mathbf{x}_i) \equiv \int_0^t \kappa(s; \mathbf{x}_i) ds$ . We can obtain the cdf of  $t_i^*$  given  $\mathbf{x}_i$  by using equation (20.34). The density of  $v_i$  is  $h(v) = \delta^{\delta} v^{\delta - 1} \exp(-\delta v) / \Gamma(\delta)$ , where  $\operatorname{Var}(v_i) = 1/\delta$  and


{711}------------------------------------------------

Gð-Þ is the gamma function. Let x<sup>i</sup> 1xðt; xiÞ for given t. Then

$$\int_{0}^{\infty} \exp(-\xi_{i}v)\delta^{\delta}v^{\delta-1} \exp(-\delta v)/\Gamma(\delta) dv$$

$$= \left[\delta/(\delta+\xi_{i})\right]^{\delta} \int_{0}^{\infty} (\delta+\xi_{i})^{\delta}v^{\delta-1} \exp[-(\delta+\xi_{i})v]/\Gamma(\delta) dv$$

$$= \left[\delta/(\delta+\xi_{i})\right]^{\delta} = (1+\xi_{i}/\delta)^{-\delta}$$

where the second-to-last equality follows because the integrand is the Gamma ðd; d þ xiÞ density and must integrate to unity. Now we use equation (20.34):

$$G(t \mid \mathbf{x}_i) = 1 - [1 + \xi(t; \mathbf{x}_i)/\delta]^{-\delta}$$
(20.36)

Taking the derivative of equation (20.36) with respect to t, using the fact that kðt; xiÞ is the derivative of xðt; xiÞ, yields the density of t <sup>i</sup> given x<sup>i</sup> as

$$g(t \mid \mathbf{x}_i) = \kappa(t; \mathbf{x}_i) [1 + \xi(t; \mathbf{x}_i)/\delta]^{-(\delta - 1)}$$
(20.37)

The function kðt; xÞ depends on parameters *y*, and so gðt j xÞ should be gðt j x; *y*; dÞ. With censored data the vector *y* can be estimated along with d by using the loglikelihood function in equation (20.24) (again, with G replacing F ).

With the Weibull hazard in equation (20.33), xðt; xÞ ¼ expðx*b*Þt<sup>a</sup>, which leads to a very tractable analysis when plugged into equations (20.36) and (20.37); the resulting duration distribution is called the Burr distribution. In the log-logistic case with kðt; xÞ ¼ expðx*b*Þat<sup>a</sup>1½1 þ expðx*b*Þt<sup>a</sup> 1 , xðt; xÞ ¼ log½1 þ expðx*b*Þt<sup>a</sup>. These equations can be plugged into the preceding formulas for a maximum likelihood analysis.

Before we end this section, we should recall why we might want to explicitly introduce unobserved heterogeneity when the heterogeneity is assumed to be independent of the observed covariates. The strongest case is seen when we are interested in testing for duration dependence conditional on observed covariates and unobserved heterogeneity, where the unobserved heterogeneity enters the hazard multiplicatively. As carefully exposited by Lancaster (1990, Section 10.2), ignoring multiplicative heterogeneity in the Weibull model results in asymptotically underestimating a. Therefore, we could very well conclude that there is negative duration dependence conditional on x, whereas there is no duration dependence ða ¼ 1Þ conditional on x and v.

In a general sense, it is somewhat heroic to think we can distinguish between duration dependence and unobserved heterogeneity when we observe only a single cycle for each agent. The problem is simple to describe: because we can only estimate the distribution of T given x, we cannot uncover the distribution of T given ðx; vÞ unless

{712}------------------------------------------------

we make extra assumptions, a point Lancaster (1990, Section 10.1) illustrates with an example. Therefore, we cannot tell whether the hazard describing T given ðx; vÞ exhibits duration dependence. But, when the hazard has the proportional hazard form lðt; x; vÞ ¼ vkðxÞl0ðtÞ, it is possible to identify the function kð-Þ and the baseline hazard l0ð-Þ quite generally (along with the distribution of v). See Lancaster (1990, Section 7.3) for a presentation of the results of Elbers and Ridder (1982). Recently, Horowitz (1999) has demonstrated how to nonparametrically estimate the baseline hazard and the distribution of the unobserved heterogeneity under fairly weak assumptions.

When interest centers on how the observed covariates affect the mean duration, explicitly modeling unobserved heterogeneity is less compelling. Adding unobserved heterogeneity to equation (20.26) does not change the mean effects; it merely changes the error distribution. Without censoring, we would probably estimate *b* in equation (20.26) by OLS (rather than MLE) so that the estimators would be robust to distributional misspecification. With censoring, to perform maximum likelihood, we must know the distribution of t <sup>i</sup> given xi, and this depends on the distribution of vi when we explicitly introduce unobserved heterogeneity. But introducing unobserved heterogeneity is indistinguishable from simply allowing a more flexible duration distribution.

# 20.4 Analysis of Grouped Duration Data

Continuously distributed durations are, strictly speaking, rare in social science applications. Even if an underlying duration is properly viewed as being continuous, measurements are necessarily discrete. When the measurements are fairly precise, it is sensible to treat the durations as continuous random variables. But when the measurements are coarse—such as monthly, or perhaps even weekly—it can be important to account for the discreteness in the estimation.

Grouped duration data arise when each duration is only known to fall into a certain time interval, such as a week, a month, or even a year. For example, unemployment durations are often measured to the nearest week. In Example 20.2 the time until next arrest is measured to the nearest month. Even with grouped data we can generally estimate the parameters of the duration distribution.

The approach we take here to analyzing grouped data summarizes the information on staying in the initial state or exiting in each time interval in a sequence of binary outcomes. (Kiefer, 1988; Han and Hausman, 1990; Meyer, 1990; Lancaster, 1990; McCall, 1994; and Sueyoshi, 1995, all take this approach.) In effect, we have a panel data set where each cross section observation is a vector of binary responses, along

{713}------------------------------------------------

with covariates. In addition to allowing us to treat grouped durations, the panel data approach has at least two additional advantages. First, in a proportional hazard specification, it leads to easy methods for estimating flexible hazard functions. Second, because of the sequential nature of the data, time-varying covariates are easily introduced.

We assume flow sampling so that we do not have to address the sample selection problem that arises with stock sampling. We divide the time line into M þ 1 intervals, ½0; a1Þ; ½a1; a2Þ; ... ; ½aM<sup>1</sup>; aMÞ; ½aM; yÞ, where the am are known constants. For example, we might have a<sup>1</sup> ¼ 1; a<sup>2</sup> ¼ 2; a<sup>3</sup> ¼ 3, and so on, but unequally spaced intervals are allowed. The last interval, ½aM; yÞ, is chosen so that any duration falling into it is censored at aM: no observed durations are greater than aM. For a random draw from the population, let cm be a binary censoring indicator equal to unity if the duration is censored in interval m, and zero otherwise. Notice that cm ¼ 1 implies cmþ<sup>1</sup> ¼ 1: if the duration was censored in interval m, it is still censored in interval m þ 1. Because durations lasting into the last interval are censored, cMþ<sup>1</sup> 1 1. Similarly, ym is a binary indicator equal to unity if the duration ends in the mth interval and zero otherwise. Thus, ymþ<sup>1</sup> ¼ 1 if ym ¼ 1. If the duration is censored in interval m ðcm ¼ 1Þ, we set ym 11 by convention.

As in Section 20.3, we allow individuals to enter the initial state at different calendar times. In order to keep the notation simple, we do not explicitly show the conditioning on these starting times, as the starting times play no role under flow sampling when we assume that, conditional on the covariates, the starting times are independent of the duration and any unobserved heterogeneity. If necessary, startingtime dummies can be included in the covariates.

For each person i, we observe ðyi1; ci1Þ; ... ;ðyiM; ciMÞ, which is a balanced panel data set. To avoid confusion with our notation for a duration (T for the random variable, t for a particular outcome on T ), we use m to index the time intervals. The string of binary indicators for any individual is not unrestricted: we must observe a string of zeros followed by a string of ones. The important information is the interval in which yim becomes unity for the first time, and whether that represents a true exit from the initial state or censoring.