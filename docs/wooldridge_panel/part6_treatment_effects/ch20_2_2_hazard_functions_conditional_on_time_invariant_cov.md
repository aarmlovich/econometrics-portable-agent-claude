# Hazard Functions Conditional on Time-Invariant Covariates

> Pages: 696-699

Usually in economics we are interested in hazard functions conditional on a set of covariates or regressors. When these do not change over time—as is often the case given the way many duration data sets are collected—then we simply define the hazard (and all other features of T ) conditional on the covariates. Thus, the conditional hazard is

$$\lambda(t; \mathbf{x}) = \lim_{h \downarrow 0} \frac{\mathbf{P}(t \le T < t + h \mid T \ge t, \mathbf{x})}{h}$$

where x is a vector of explanatory variables. All of the formulas from the previous subsection continue to hold provided the cdf and density are defined conditional on x. For example, if the conditional cdf Fðj xÞ is differentiable, we have

$$\lambda(t; \mathbf{x}) = \frac{f(t \mid \mathbf{x})}{1 - F(t \mid \mathbf{x})}$$
(20.15)

where fð j xÞ is the density of T given x. Often we are interested in the partial effects of the xj on lðt; xÞ, which are defined as partial derivatives for continuous xj and as differences for discrete xj.

If the durations start at different calendar dates—which is usually the case—we can include indicators for different starting dates in the covariates. These allow us to control for seasonal differences in duration distributions.

An especially important class of models with time-invariant regressors consists of proportional hazard models. A proportional hazard can be written as

$$\lambda(t; \mathbf{x}) = \kappa(\mathbf{x})\lambda_0(t) \tag{20.16}$$

where kð-Þ > 0 is a nonnegative function of x and l0ðtÞ > 0 is called the baseline hazard. The baseline hazard is common to all units in the population; individual hazard functions differ proportionately based on a function kðxÞ of observed covariates.

{697}------------------------------------------------

Typically, kð-Þ is parameterized as kðxÞ ¼ expðx*b*Þ, where *b* is a vector of parameters. Then

$$\log \lambda(t; \mathbf{x}) = \mathbf{x}\boldsymbol{\beta} + \log \lambda_0(t) \tag{20.17}$$

and b<sup>j</sup> measures the semielasticity of the hazard with respect to xj. [If xj is the log of an underlying variable, say xj ¼ logðzjÞ, b<sup>j</sup> is the elasticity of the hazard with respect to zj.]

Occasionally we are interested only in how the covariates shift the hazard function, in which case estimation of l<sup>0</sup> is not necessary. Cox (1972) obtained a partial maximum likelihood estimator for *b* that does not require estimating l0ð-Þ. We discuss Cox's approach briefly in Section 20.5. In economics, much of the time we are interested in the shape of the baseline hazard. We discuss estimation of proportional hazard models with a flexible baseline hazard in Section 20.4.

If in the Weibull hazard function (20.12) we replace g with expðx*b*Þ, where the first element of x is unity, we obtain a proportional hazard model with l0ðtÞ 1 at<sup>a</sup>1. However, if we replace g in equation (20.13) with expðx*b*Þ—which is the most common way of introducing covariates into the log-logistic model—we do not obtain a hazard with the proportional hazard form.

Example 20.1 (continued): If T is an unemployment duration, x might contain education, labor market experience, marital status, race, and number of children, all measured at the beginning of the unemployment spell. Policy variables in x might reflect the rules governing unemployment benefits, where these are known before each person's unemployment duration.

Example 20.2 (continued): To explain the length of time before arrest after release from prison, the covariates might include participation in a work program while in prison, years of education, marital status, race, time served, and past number of convictions.

# 20.2.3 Hazard Functions Conditional on Time-Varying Covariates

Studying hazard functions is more complicated when we wish to model the effects of time-varying covariates on the hazard function. For one thing, it makes no sense to specify the distribution of the duration T conditional on the covariates at only one time period. Nevertheless, we can still define the appropriate conditional probabilities that lead to a conditional hazard function.

Let xðtÞ denote the vector of regressors at time t; again, this is the random vector describing the population. For t b0, let XðtÞ, t b0, denote the covariate path up

{698}------------------------------------------------

through time t: XðtÞ 1fxðsÞ: 0a satg. Following Lancaster (1990, Chapter 2), we define the conditional hazard function at time t by

$$\lambda[t; \mathbf{X}(t)] = \lim_{h \downarrow 0} \frac{P[t \le T < t + h \mid T \ge t, \mathbf{X}(t+h)]}{h}$$
(20.18)

assuming that this limit exists. A discussion of assumptions that ensure existence of equation (20.18) is well beyond the scope of this book; see Lancaster (1990, Chapter 2). One case where this limit exists very generally occurs when T is continuous and, for each t, xðt þ hÞ is constant for all h A ½0; hðtÞ for some function hðtÞ > 0. Then we can replace Xðt þ hÞ with XðtÞ in equation (20.18) [because Xðt þ hÞ ¼ XðtÞ for h sufficiently small]. For reasons we will see in Section 20.4, we must assume that timevarying covariates are constant over the interval of observation (such as a week or a month), anyway, in which case there is no problem in defining equation (20.18).

For certain purposes, it is important to know whether time-varying covariates are strictly exogenous. With the hazard defined as in equation (20.18), Lancaster (1990, Definition 2.1) provides a definition that rules out feedback from the duration to future values of the covariates. Specifically, if Xðt; t þ hÞ denotes the covariate path from time t to t þ h, then Lancaster's strict exogeneity condition is

$$P[X(t, t+h) | T \ge t + h, X(t)] = P[X(t, t+h) | X(t)]$$
(20.19)

for all t b0, h > 0. Actually, when condition (20.19) holds, Lancaster says fxðtÞ: t > 0g is ''exogenous.'' We prefer the name ''strictly exogenous'' because condition (20.19) is closely related to the notions of strict exogeneity that we have encountered throughout this book. Plus, it is important to see that condition (20.19) has nothing to do with contemporaneous endogeneity: by definition, the covariates are sequentially exogenous (see Section 11.1.1) because, by specifying l½t; XðtÞ, we are conditioning on current and past covariates.

Equation (20.19) applies to covariates whose entire path is well-defined whether or not the agent is in the initial state. One such class of covariates, called external covariates by Kalbfleisch and Prentice (1980), has the feature that the covariate path is independent of whether any particular agent has or has not left the initial state. In modeling time until arrest, these covariates might include law enforcement per capita in the person's city of residence or the city unemployment rate.

Other covariates are not external to each agent but have paths that are still defined after the agent leaves the initial state. For example, marital status is well-defined before and after someone is arrested, but it is possibly related to whether someone has been arrested. Whether marital status satisfies condition (20.19) is an empirical issue.

{699}------------------------------------------------

The definition of strict exogeneity in condition (20.19) cannot be applied to timevarying covariates whose path is not defined once the agent leaves the initial state. Kalbfleisch and Prentice (1980) call these internal covariates. Lancaster (1990, p. 28) gives the example of job tenure duration, where a time-varying covariate is wage paid on the job: if a person leaves the job, it makes no sense to define the future wage path in that job. As a second example, in modeling the time until a former prisoner is arrested, a time-varying covariate at time t might be wage income in the previous month, t 1. If someone is arrested and reincarcerated, it makes little sense to define future labor income.

It is pretty clear that internal covariates cannot satisfy any reasonable strict exogeneity assumption. This fact will be important in Section 20.4 when we discuss estimation of duration models with unobserved heterogeneity and grouped duration data. We will actually use a slightly different notion of strict exogeneity that is directly relevant for conditional maximum likelihood estimation. Nevertheless, it is in the same spirit as condition (20.19).

With time-varying covariates there is not, strictly speaking, such a thing as a proportional hazard model. Nevertheless, it has become common in econometrics to call a hazard of the form

$$\lambda[t; \mathbf{x}(t)] = \kappa[\mathbf{x}(t)]\lambda_0(t) \tag{20.20}$$

a proportional hazard with time-varying covariates. The function multiplying the baseline hazard is usually k½xðtÞ ¼ exp½xðtÞ*b*; for notational reasons, we show this depending only on xðtÞ and not on past covariates [which can always be included in xðtÞ]. We will discuss estimation of these models, without the strict exogeneity assumption, in Section 20.4.2. In Section 20.4.3, when we multiply equation (20.20) by unobserved heterogeneity, strict exogeneity becomes very important.

The log-logistic hazard is also easily modified to have time-varying covariates. One way to include time-varying covariates parametrically is

$$\lambda[t; \mathbf{x}(t)] = \exp[\mathbf{x}(t)\boldsymbol{\beta}]\alpha t^{\alpha-1}/\{1 + \exp[\mathbf{x}(t)\boldsymbol{\beta}]t^{\alpha}\}$$

We will see how to estimate a and *b* in Section 20.4.2.