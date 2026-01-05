# 19.10. Use the data in PATENT.RAW for this exercise.

> Pages: 689-696

- a. Estimate a pooled Poisson regression model relating patents to lsales ¼ logðsalesÞ and current and four lags of lrnd ¼ logð1 þ rndÞ, where we add one before taking the log to account for the fact that rnd is zero for some firms in some years. Use an exponential mean function and include a full set of year dummies. Which lags of lrnd are significant using the usual Poisson MLE standard errors?
- b. Give two reasons why the usual Poisson MLE standard errors from part a might be invalid.
- c. Obtain s^ for the pooled Poisson estimation. Using the GLM standard errors (but without an adjustment for possible serial dependence), which lags of lrnd are significant?
- d. Obtain the QLR statistic for joint significance of lags one through four of lrnd. (Be careful here; you must use the same set of years in estimating the restricted version of the model.) How does it compare to the usual LR statistic?
- e. Compute the standard errors that are robust to an arbitrary conditional variance and serial dependence. How do they compare with the standard errors from parts a and c?
- f. What is the estimated long-run elasticity of expected patents with respect to R&D spending? (Ignore the fact that one has been added to the R&D numbers before taking the log.) Obtain a fully robust standard error for the long-run elasticity.
- g. Now use the fixed effects Poisson estimator, and compare the estimated lag coefficients to those from the pooled Poisson analysis. Estimate the long-run elasticity, and obtain its standard error. (Assume that the full set of FEP assumptions hold.)

{690}------------------------------------------------

- **19.11.** a. For a random draw *i* from the cross section, assume that (1) for each time period t,  $y_{it} | \mathbf{x}_i, c_i \sim \text{Poisson}(c_i m_{it})$ , where  $c_i > 0$  is unobserved heterogeneity and  $m_{it} > 0$  is typically a function of only  $\mathbf{x}_{it}$ ; and (2)  $(y_{i1}, \dots, y_{iT})$  are independent conditional on  $(\mathbf{x}_i, c_i)$ . Derive the density of  $(y_{i1}, \dots, y_{iT})$  conditional on  $(\mathbf{x}_i, c_i)$ .
- b. To the assumptions from part a, add the assumption that  $c_i | \mathbf{x}_i \sim \text{Gamma}(\delta, \delta)$ , so that  $E(c_i) = 1$  and  $Var(c_i) = 1/\delta$ . {The density of  $c_i$  is  $h(c) = [\delta^{\delta}/\Gamma(\delta)]c^{\delta-1} \exp(-\delta c)$ , where  $\Gamma(\delta)$  is the gamma function.} Let  $s = y_1 + \cdots + y_T$  and  $M_i = m_{i1} + \cdots + m_{iT}$ . Show that the density of  $(y_{i1}, \ldots, y_{iT})$  given  $\mathbf{x}_i$  is

$$\left(\prod_{t=1}^{T} m_{it}^{y_t}/y_t!\right) [\delta^{\delta}/\Gamma(\delta)] [\Gamma(M_i+s)/(M_i+\delta)^{(s+\delta)}]$$

[Hint: The easiest way to show this result is to turn the integral into one involving a  $Gamma(s + \delta, M_i + \delta)$  density and a multiplicative term. Naturally, the density must integrate to unity, and so what is left over is the density we seek.]

- **19.12.** For a random draw *i* from the cross section, assume that (1) for each *t*,  $y_{it} | \mathbf{x}_i, c_i \sim \text{Gamma}(m_{it}, 1/c_i)$ , where  $c_i > 0$  is unobserved heterogeneity and  $m_{it} > 0$ ; and (2)  $(y_{i1}, \ldots, y_{iT})$  are independent conditional on  $(\mathbf{x}_i, c_i)$ . The gamma distribution is parameterized so that  $E(y_{it} | \mathbf{x}_i, c_i) = c_i m_{it}$  and  $Var(y_{it} | \mathbf{x}_i, c_i) = c_i^2 m_{it}$ .
- a. Let  $s_i = y_{i1} + \cdots + y_{iT}$ . Show that the density of  $(y_{i1}, y_{i2}, \dots, y_{iT})$  conditional on  $(s_i, \mathbf{x}_i, c_i)$  is

$$f(y_1, \dots, y_T \mid s_i, \mathbf{x}_i, c_i) = \left[ \Gamma(m_{i1} + \dots + m_{iT}) / \prod_{t=1}^T \Gamma(m_{it}) \right] \times \left[ \left( \prod_{t=1}^T y_t^{m_{it}-1} \right) / s_i^{\{(m_{i1} + \dots + m_{iT}) - 1\}} \right]$$

where  $\Gamma(\cdot)$  is the gamma function. Note that the density does not depend on  $c_i$ . {Hint: If  $Y_1, \ldots, Y_T$  are independent random variables and  $S = Y_1 + \cdots + Y_T$ , the joint density of  $Y_1, \ldots, Y_T$  given S = s is  $f_1(y_1) \cdots f_{T-1}(y_{T-1}) f_T(s - y_1 - \cdots - y_{T-1}) / g(s)$ , where g(s) is the density of S. When  $Y_t$  has a Gamma $(\alpha_t, \lambda)$  distribution for each t, so that  $f_t(y_t) = [\lambda^{\alpha_t}/\Gamma(\alpha_t)] y_t^{(\alpha_t-1)} \exp(-\lambda y_t)$ ,  $S \sim \text{Gamma}(\alpha_1 + \cdots + \alpha_T, \lambda)$ .}

b. Let  $m_t(\mathbf{x}_i, \boldsymbol{\beta})$  be a parametric function for  $m_{it}$ —for example,  $\exp(\mathbf{x}_{it}\boldsymbol{\beta})$ . Write down the log-likelihood function for observation *i*. The conditional MLE in this case is called the **fixed effects gamma estimator**.


{691}------------------------------------------------

#### 20.1 Introduction

Some response variables in economics come in the form of a duration, which is the time elapsed until a certain event occurs. A few examples include weeks unemployed, months spent on welfare, days until arrest after incarceration, and quarters until an Internet firm files for bankruptcy.

The recent literature on duration analysis is quite rich. In this chapter we focus on the developments that have been used most often in applied work. In addition to providing a rigorous introduction to modern duration analysis, this chapter should prepare you for more advanced treatments, such as Lancaster's (1990) monograph.

Duration analysis has its origins in what is typically called survival analysis, where the duration of interest is survival time of a subject. In survival analysis we are interested in how various treatments or demographic characteristics affect survival times. In the social sciences, we are interested in any situation where an individual or family, or firm, and so on—begins in an initial state and is either observed to exit the state or is censored. (We will discuss the exact nature of censoring in Sections 20.3 and 20.4.) The calendar dates on which units enter the initial state do not have to be the same. (When we introduce covariates in Section 20.2.2, we note how dummy variables for different calendar dates can be included in the covariates, if necessary, to allow for systematic differences in durations by starting date.)

Traditional duration analysis begins by specifying a population distribution for the duration, usually conditional on some explanatory variables (covariates) observed at the beginning of the duration. For example, for the population of people who became unemployed during a particular period, we might observe education levels, experience, marital status—all measured when the person becomes unemployed—wage on prior job, and a measure of unemployment benefits. Then we specify a distribution for the unemployment duration conditional on the covariates. Any reasonable distribution reflects the fact that an unemployment duration is nonnegative. Once a complete conditional distribution has been specified, the same maximum likelihood methods that we studied in Chapter 16 for censored regression models can be used. In this framework, we are typically interested in estimating the effects of the covariates on the expected duration.

Recent treatments of duration analysis tend to focus on the hazard function. The hazard function allows us to approximate the probability of exiting the initial state within a short interval, conditional on having survived up to the starting time of the interval. In econometric applications, hazard functions are usually conditional on some covariates. An important feature for policy analysis is allowing the hazard function to depend on covariates that change over time.

{692}------------------------------------------------

In Section 20.2 we define and discuss hazard functions, and we settle certain issues involved with introducing covariates into hazard functions. In Section 20.3 we show how censored regression models apply to standard duration models with single-cycle flow data, when all covariates are time constant. We also discuss the most common way of introducing unobserved heterogeneity into traditional duration analysis. Given parametric assumptions, we can test for duration dependence—which means that the probability of exiting the initial state depends on the length of time in the state—as well as for the presence of unobserved heterogeneity.

In Section 20.4 we study methods that allow flexible estimation of a hazard function, both with time-constant and time-varying covariates. We assume that we have grouped data; this term means that durations are observed to fall into fixed intervals (often weekly or monthly intervals) and that any time-varying covariates are assumed to be constant within an interval. We focus attention on the case with two states, with everyone in the population starting in the initial state, and single-cycle data, where each person either exits the initial state or is censored before exiting. We also show how heterogeneity can be included when the covariates are strictly exogenous.

We touch on some additional issues in Section 20.5.

# 20.2 Hazard Functions

The hazard function plays a central role in modern duration analysis. In this section, we discuss various features of the hazard function, both with and without covariates, and provide some examples.

#### 20.2.1 Hazard Functions without Covariates

Often in this chapter it is convenient to distinguish random variables from particular outcomes of random variables. Let T b 0 denote the duration, which has some distribution in the population; t denotes a particular value of T. (As with any econometric analysis, it is important to be very clear about the relevant population, a topic we consider in Section 20.3.) In survival analysis, T is the length of time a subject lives. Much of the current terminology in duration analysis comes from survival applications. For us, T is the time at which a person (or family, firm, and so on) leaves the initial state. For example, if the initial state is unemployment, T would be the time, measured in, say, weeks, until a person becomes employed.

The cumulative distribution function (cdf ) of T is defined as

$$F(t) = P(T \le t), \qquad t \ge 0 \tag{20.1}$$

{693}------------------------------------------------

The survivor function is defined as SðtÞ 11 FðtÞ ¼ PðT > tÞ, and this is the probability of ''surviving'' past time t. We assume in the rest of this section that T is continuous—and, in fact, has a differentiable cdf—because this assumption simplifies statements of certain probabilities. Discreteness in observed durations can be viewed as a consequence of the sampling scheme, as we discuss in Section 20.4. Denote the

density of 
$$T$$
 by  $f(t) = \frac{dF}{dt}(t)$ .  
For  $h > 0$ ,

$$P(t \le T < t + h \mid T \ge t) \tag{20.2}$$

is the probabilty of leaving the initial state in the interval ½t; t þ hÞ given survival up until time t. The hazard function for T is defined as

$$\lambda(t) = \lim_{h \downarrow 0} \frac{P(t \le T < t + h \mid T \ge t)}{h}$$
 (20.3)

For each t, lðtÞ is the instantaneous rate of leaving per unit of time. From equation (20.3) it follows that, for ''small'' h,

$$P(t \le T < t + h \mid T \ge t) \approx \lambda(t)h \tag{20.4}$$

Thus the hazard function can be used to approximate a conditional probability in much the same way that the height of the density of T can be used to approximate an unconditional probability.

Example 20.1 (Unemployment Duration): If T is length of time unemployed, measured in weeks, then lð20Þ is (approximately) the probability of becoming employed between weeks 20 and 21. The phrase ''becoming employed'' reflects the fact that the person was unemployed up through week 20. That is, lð20Þ is roughly the probability of becoming employed between weeks 20 and 21, conditional on having been unemployed through week 20.

Example 20.2 (Recidivism Duration): Suppose T is the number of months before a former prisoner is arrested for a crime. Then lð12Þ is roughly the probability of being arrested during the 13th month, conditional on not having been arrested during the first year.

We can express the hazard function in terms of the density and cdf very simply. First, write

$$P(t \le T < t + h \mid T \ge t) = P(t \le T < t + h)/P(T \ge t) = \frac{F(t + h) - F(t)}{1 - F(t)}$$

{694}------------------------------------------------

When the cdf is differentiable, we can take the limit of the right-hand side, divided by h, as h approaches zero from above:

$$\lambda(t) = \lim_{h \downarrow 0} \frac{F(t+h) - F(t)}{h} \cdot \frac{1}{1 - F(t)} = \frac{f(t)}{1 - F(t)} = \frac{f(t)}{S(t)}$$
(20.5)

Because the derivative of S(t) is -f(t), we have

$$\lambda(t) = -\frac{d \log S(t)}{\mathrm{d}t} \tag{20.6}$$

and, using F(0) = 0, we can integrate to get

$$F(t) = 1 - \exp\left[-\int_0^t \lambda(s) \, ds\right], \qquad t \ge 0 \tag{20.7}$$

Straightforward differentiation of equation (20.7) gives the density of T as

$$f(t) = \lambda(t) \exp\left[-\int_0^t \lambda(s) \, ds\right] \tag{20.8}$$

Therefore, all probabilities can be computed using the hazard function. For example, for points  $a_1 < a_2$ ,

$$P(T \ge a_2 \mid T \ge a_1) = \frac{1 - F(a_2)}{1 - F(a_1)} = \exp\left[-\int_{a_1}^{a_2} \lambda(s) \, ds\right]$$

and

$$P(a_1 \le T < a_2 \mid T \ge a_1) = 1 - \exp\left[-\int_{a_1}^{a_2} \lambda(s) \, ds\right]$$
 (20.9)

This last expression is especially useful for constructing the log-likelihood functions needed in Section 20.4.

The shape of the hazard function is of primary interest in many empirical applications. In the simplest case, the hazard function is constant:

$$\lambda(t) = \lambda, \qquad \text{all } t \ge 0 \tag{20.10}$$

This function means that the process driving T is *memoryless*: the probability of exit in the next interval does not depend on how much time has been spent in the initial state. From equation (20.7), a constant hazard implies

$$F(t) = 1 - \exp(-\lambda t) \tag{20.11}$$

{695}------------------------------------------------

which is the cdf of the exponential distribution. Conversely, if T has an exponential distribution, it has a constant hazard.

When the hazard function is not constant, we say that the process exhibits duration dependence. Assuming that lð-Þ is differentiable, there is positive duration dependence at time t if dlðtÞ=dt > 0; if dlðtÞ=dt > 0 for all t > 0, then the process exhibits positive duration dependence. With positive duration dependence, the probability of exiting the initial state increases the longer one is in the initial state. If the derivative is negative, then there is negative duration dependence.

Example 20.3 (Weibull Distribution): If T has a Weibull distribution, its cdf is given by FðtÞ ¼ 1 expðgt<sup>a</sup>Þ, where g and a are nonnegative parameters. The density is fðtÞ ¼ gat<sup>a</sup><sup>1</sup> expðgt<sup>a</sup>Þ. By equation (20.5), the hazard function is

$$\lambda(t) = f(t)/S(t) = \gamma \alpha t^{\alpha - 1} \tag{20.12}$$

When a ¼ 1, the Weibull distribution reduces to the exponential with l ¼ g. If a > 1, the hazard is monotonically increasing, so the hazard everywhere exhibits positive duration dependence; for a < 1, the hazard is monotonically decreasing. Provided we think the hazard is monotonically increasing or decreasing, the Weibull distribution is a relatively simple way to capture duration dependence.

We often want to specify the hazard directly, in which case we can use equation (20.7) to determine the duration distribution.

Example 20.4 (Log-Logistic Hazard Function): The log-logistic hazard function is specified as

$$\lambda(t) = \frac{\gamma \alpha t^{\alpha - 1}}{1 + \gamma t^{\alpha}} \tag{20.13}$$

where g and a are positive parameters. When a ¼ 1, the hazard is monotonically decreasing from g at t ¼ 0 to zero as t ! y; when a < 1, the hazard is also monotonically decreasing to zero as t ! y, but the hazard is unbounded as t approaches zero. When a > 1, the hazard is increasing until t ¼ ½ða 1Þ=g 1a , and then it decreases to zero.

Straightforward integration gives

$$\int_0^t \lambda(s) ds = \log(1 + \gamma t^{\alpha}) = -\log[(1 + \gamma t^{\alpha})^{-1}]$$

so that, by equation (20.7),

{696}------------------------------------------------

$$F(t) = 1 - (1 + \gamma t^{\alpha})^{-1}, \qquad t \ge 0$$
(20.14)

Differentiating with respect to t gives

$$f(t) = \gamma \alpha t^{\alpha - 1} (1 + \gamma t^{\alpha})^{-2}$$

Using this density, it can be shown that Y 1logðTÞ has density gðyÞ ¼ a exp½aðy mÞ=f1 þ exp½aðy mÞg<sup>2</sup> , where m ¼ a<sup>1</sup> logðgÞ is the mean of Y. In other words, logðTÞ has a logistic distribution with mean m and variance p<sup>2</sup>=ð3a<sup>2</sup>Þ (hence the name ''log-logistic'').