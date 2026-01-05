# Pooled Tobit

> Pages: 547-559

As with binary response, it is easy to apply pooled Tobit methods to panel data or cluster samples. A panel data model is

$$y_{it} = \max(0, \mathbf{x}_{it}\boldsymbol{\beta} + u_{it}), \qquad t = 1, 2, \dots, T$$
 (16.39)

$$u_{it} \mid \mathbf{x}_{it} \sim \text{Normal}(0, \sigma^2)$$
 (16.40)

This model has several notable features. First, it does not maintain strict exogeneity of xit: uit is independent of xit, but the relationship between uit and xis, t 0s, is unspecified. As a result, xit could contain yi;t<sup>1</sup> or variables that are affected by 

{548}------------------------------------------------

feedback. A second important point is that the fuit: t ¼ 1; ... ; Tg are allowed to be serially dependent, which means that the yit can be dependent after conditioning on the explanatory variables. In short, equations (16.39) and (16.40) only specify a model for Dðyit j xitÞ, and xit can contain any conditioning variables (time dummies, interactions of time dummies with time-constant or time-varying variables, lagged dependent variables, and so on).

The pooled estimator maximizes the partial log-likelihood function

$$\sum_{i=1}^{N} \sum_{t=1}^{T} \ell_{it}(\boldsymbol{\beta}, \sigma^{2})$$

where litð*b*; s<sup>2</sup>Þ is the log-likelihood function given in equation (16.20). Computationally, we just apply Tobit to the data set as if it were one long cross section of size NT. However, without further assumptions, a robust variance matrix estimator is needed to account for serial correlation in the score across t; see Sections 13.8.2 and 15.8.1. Robust Wald and score statistics can be computed as in Section 12.6. The same methods work when each i represents a cluster and t is a unit within a cluster; see Section 15.8.6 for the probit case and Section 13.8.4 for the general case. With either panel data or cluster samples, the LR statistic based on the pooled Tobit estimation is not generally valid.

In the case that the panel data model is dynamically complete, that is,

$$\mathbf{D}(y_{it} \mid \mathbf{x}_{it}, y_{i,t-1}, \mathbf{x}_{i,t-1}, \ldots) = \mathbf{D}(y_{it} \mid \mathbf{x}_{it})$$
(16.41)

inference is considerably easier: all the usual statistics from pooled Tobit are valid, including likelihood ratio statistics. Remember, we are not assuming any kind of independence across t; in fact, xit can contain lagged dependent variables. It just works out that dynamic completeness leads to the same inference procedures one would use on independent cross sections; see the general treatment in Section 13.8.

A general test for dynamic completeness can be based on the scores ^sit, as mentioned in Section 13.8.3, but it is nice to have a simple test that can be computed from pooled Tobit estimation. Under assumption (16.41), variables dated at time t 1 and earlier should not affect the distribution of yit once xit is conditioned on. There are many possibilities, but we focus on just one here. Define ri;t<sup>1</sup> ¼ 1 if yi;t<sup>1</sup> ¼ 0 and ri;t<sup>1</sup> <sup>¼</sup> 0 if yi;t<sup>1</sup> <sup>&</sup>gt; 0. Further, define ^ui;t<sup>1</sup> <sup>1</sup> yi;t<sup>1</sup> <sup>x</sup><sup>i</sup>;t<sup>1</sup> ^*<sup>b</sup>* if yi;t<sup>1</sup> <sup>&</sup>gt; 0. Then estimate the following (artificial) model by pooled Tobit:

$$y_{it} = \max[0, \mathbf{x}_{it}\boldsymbol{\beta} + \gamma_1 r_{i,t-1} + \gamma_2 (1 - r_{i,t-1}) \hat{u}_{i,t-1} + error_{it}]$$

using time periods t ¼ 2; ... ; T, and test the joint hypothesis H0: g<sup>1</sup> ¼ 0, g<sup>2</sup> ¼ 0. Under the null of dynamic completeness, errorit ¼ uit, and the estimation of ui;t<sup>1</sup>

{549}------------------------------------------------

does not affect the limiting distribution of the Wald, LR, or LM tests. In computing either the LR or LM test it is important to drop the first time period in estimating the restricted model with  $\gamma_1 = \gamma_2 = 0$ . Since pooled Tobit is used to estimate both the restricted and unrestricted models, the LR test is fairly easy to obtain.

In some applications it may be important to allow interactions between time dummies and explanatory variables. We might also want to allow the variance of  $u_{it}$  to change over time. In data-censoring cases, where  $E(y_{it}^* | \mathbf{x}_{it}) = \mathbf{x}_{it}\boldsymbol{\beta}$  is of direct interest, allowing changing variances over time could give us greater confidence in the estimate of  $\boldsymbol{\beta}$ . If  $\sigma_t^2 = \text{Var}(u_{it})$ , a pooled approach still works, but  $\ell_{it}(\boldsymbol{\beta}, \sigma^2)$  becomes  $\ell_{it}(\boldsymbol{\beta}, \sigma_t^2)$ , and special software may be needed for estimation.

With true data censoring, it is tricky to allow for lagged dependent variables in  $\mathbf{x}_{it}$ , because we probably want a linear, AR(1) model for the unobserved outcome,  $y_{it}^*$ . But including  $y_{i,t-1}^*$  in  $\mathbf{x}_{it}$  is very difficult, because  $y_{i,t-1}^*$  is only partially observed. For corner solution applications, it makes sense to include functions of  $y_{i,t-1}$  in  $\mathbf{x}_{it}$ , and this approach is straightforward.

#### 16.8.2 Unobserved Effects Tobit Models under Strict Exogeneity

Another popular model for Tobit outcomes with panel data is the **unobserved effects Tobit model**. We can state this model as

$$y_{it} = \max(0, \mathbf{x}_{it}\boldsymbol{\beta} + c_i + u_{it}), \qquad t = 1, 2, \dots, T$$
 (16.42)

$$u_{it} \mid \mathbf{x}_i, c_i \sim \text{Normal}(0, \sigma_u^2)$$
 (16.43)

where  $c_i$  is the unobserved effect and  $\mathbf{x}_i$  contains  $\mathbf{x}_{it}$  for all t. Assumption (16.43) is a normality assumption, but it also implies that the  $\mathbf{x}_{it}$  are strictly exogenous conditional on  $c_i$ . As we have seen in several contexts, this assumption rules out certain kinds of explanatory variables.

If these equations represent a data-censoring problem, then  $\beta$  is of primary interest. In corner solution applications we must be careful to specify what is of interest. Consistent estimation of  $\beta$  and  $\sigma_u^2$  means we can estimate the partial effects of the elements of  $\mathbf{x}_t$  on  $\mathrm{E}(y_t|\mathbf{x}_t,c,y_t>0)$  and  $\mathrm{E}(y_t|\mathbf{x}_t,c)$  for given values of c, using equations (16.11) and (16.14). Under assumption (16.44), which follows, we can estimate  $\mathrm{E}(c_i)$  and evaluate the partial effects at the estimated mean value. We will also see how to estimate the average partial effects.

Rather than cover a standard random effects version, we consider a more general Chamberlain-like model that allows  $c_i$  and  $\mathbf{x}_i$  to be correlated. To this end, assume, just as in the probit case,

$$c_i \mid \mathbf{x}_i \sim \text{Normal}(\psi + \overline{\mathbf{x}}_i \xi, \sigma_a^2)$$
 (16.44)

{550}------------------------------------------------

where  $\sigma_a^2$  is the variance of  $a_i$  in the equation  $c_i = \psi + \overline{\mathbf{x}}_i \boldsymbol{\xi} + a_i$ . We could replace  $\overline{\mathbf{x}}_i$  with  $\mathbf{x}_i$  to be more general, but  $\overline{\mathbf{x}}_i$  has at most dimension K. (As usual,  $\mathbf{x}_{it}$  would not include a constant, and time dummies would be excluded from  $\overline{\mathbf{x}}_i$  because they are already in  $\mathbf{x}_{it}$ .) Under assumptions (16.42)–(16.44), we can write

$$y_{it} = \max(0, \psi + \mathbf{x}_{it}\boldsymbol{\beta} + \overline{\mathbf{x}}_{i}\boldsymbol{\xi} + a_{i} + u_{it})$$
(16.45)

$$u_{it} \mid \mathbf{x}_i, a_i \sim \text{Normal}(0, \sigma_u^2), \qquad t = 1, 2, \dots, T$$
 (16.46)

$$a_i \mid \mathbf{x}_i \sim \text{Normal}(0, \sigma_a^2)$$
 (16.47)

This formulation is very useful, especially if we assume that, conditional on  $(\mathbf{x}_i, a_i)$  [equivalently, conditional on  $(\mathbf{x}_i, c_i)$ ], the  $\{u_{it}\}$  are serially independent:

$$(u_{i1}, \dots, u_{iT})$$
 are independent given  $(\mathbf{x}_i, a_i)$  (16.48)

Under assumptions (16.45)–(16.47), we have the **random effects Tobit model** but with  $\overline{\mathbf{x}}_i$  as an additional set of time-constant explanatory variables appearing in each time period. Software that estimates a random effects Tobit model will provide  $\sqrt{N}$ -consistent estimates of  $\psi$ ,  $\boldsymbol{\beta}$ ,  $\boldsymbol{\xi}$ ,  $\sigma_u^2$ , and  $\sigma_a^2$ . We can easily test  $H_0$ :  $\boldsymbol{\xi} = \mathbf{0}$  as a test of the traditional Tobit random effects model.

In data-censoring applications, our interest lies in  $\beta$ , and so—under the maintained assumptions—adding  $\bar{\mathbf{x}}_i$  to the random effects Tobit model solves the unobserved heterogeneity problem.

If  $\mathbf{x}_{it}$  contains a time-constant variable, say,  $w_i$ , we will not be able to estimate its effect unless we assume that its coefficient in  $\boldsymbol{\xi}$  is zero. But we can still include  $w_i$  as an explanatory variable to reduce the error variance.

For corner solution applications, we can estimate either partial effects evaluated at E(c) or average partial effects (APEs). As in Section 16.6.2, it is convenient to define  $m(z, \sigma^2) \equiv \Phi(z/\sigma)z + \sigma\phi(z/\sigma)$ , so that  $E(y_t | \mathbf{x}, c) = m(\mathbf{x}_t\boldsymbol{\beta} + c, \sigma_u^2)$ . A consistent estimator of  $E(c_i)$  is  $\hat{\psi} + \overline{\mathbf{x}}\hat{\boldsymbol{\xi}}$ , where  $\overline{\mathbf{x}}$  is the sample average of the  $\overline{\mathbf{x}}_i$ , and so we can consistently estimate partial effects at the mean value by taking derivatives or differences of  $m(\hat{\psi} + \mathbf{x}_t\hat{\boldsymbol{\beta}} + \overline{\mathbf{x}}\hat{\boldsymbol{\xi}}, \hat{\sigma}_u^2)$  with respect to the elements of  $\mathbf{x}_t$ .

Estimating APEs is also relatively simple. APEs (at  $\mathbf{x}_t = \mathbf{x}^{\circ}$ ) are obtained by finding  $\mathrm{E}[m(\mathbf{x}^{\circ}\boldsymbol{\beta} + c_i, \sigma_u^2)]$  and then computing partial derivatives or changes with respect to elements of  $\mathbf{x}^{\circ}$ . Since  $c_i = \psi + \overline{\mathbf{x}}_i \boldsymbol{\xi} + a_i$ , we have, by iterated expectations,

$$E[m(\mathbf{x}^{\circ}\boldsymbol{\beta} + c_i, \sigma_u^2)] = E\{E[m(\psi + \mathbf{x}^{\circ}\boldsymbol{\beta} + \overline{\mathbf{x}}_i\boldsymbol{\xi} + a_i, \sigma_u^2) \mid \mathbf{x}_i]\}$$
(16.49)

where the first expectation is with respect to the distribution of  $c_i$ . Since  $a_i$  and  $\mathbf{x}_i$  are independent and  $a_i \sim \text{Normal}(0, \sigma_a^2)$ , the conditional expectation in equation (16.49) is obtained by integrating  $m(\psi + \mathbf{x}^{\circ}\boldsymbol{\beta} + \overline{\mathbf{x}}_i\boldsymbol{\xi} + a_i, \sigma_u^2)$  over  $a_i$  with respect to the


{551}------------------------------------------------

Normal $(0, \sigma_a^2)$  distribution. Since  $m(\psi + \mathbf{x}^{\circ}\boldsymbol{\beta} + \overline{\mathbf{x}}_i\boldsymbol{\xi} + a_i, \sigma_u^2)$  is obtained by integrating max $(0, \psi + \mathbf{x}^{\circ}\boldsymbol{\beta} + \overline{\mathbf{x}}_i\boldsymbol{\xi} + a_i + u_{it})$  with respect to  $u_{it}$  over the Normal $(0, \sigma_u^2)$  distribution, it follows that

$$E[m(\psi + \mathbf{x}^{\circ}\boldsymbol{\beta} + \overline{\mathbf{x}}_{i}\boldsymbol{\xi} + a_{i}, \sigma_{u}^{2}) \mid \mathbf{x}_{i}] = m(\psi + \mathbf{x}^{\circ}\boldsymbol{\beta} + \overline{\mathbf{x}}_{i}\boldsymbol{\xi}, \sigma_{a}^{2} + \sigma_{u}^{2})$$
(16.50)

Therefore, the expected value of equation (16.50) (with respect to the distribution of  $\overline{\mathbf{x}}_i$ ) is consistently estimated as

$$N^{-1} \sum_{i=1}^{N} m(\hat{\boldsymbol{\psi}} + \mathbf{x}^{\circ} \hat{\boldsymbol{\beta}} + \overline{\mathbf{x}}_{i} \hat{\boldsymbol{\xi}}, \hat{\sigma}_{a}^{2} + \hat{\sigma}_{u}^{2})$$

$$(16.51)$$

A similar argument works for  $E(y_t | \mathbf{x}, c, y_t > 0)$ : sum  $(\hat{\psi} + \mathbf{x}^o \hat{\beta} + \overline{\mathbf{x}}_i \hat{\xi}) + \hat{\sigma}_v \lambda [(\hat{\psi} + \mathbf{x}^o \hat{\beta} + \overline{\mathbf{x}}_i \hat{\xi})/\hat{\sigma}_v]$  in expression (16.51), where  $\lambda(\cdot)$  is the inverse Mills ratio and  $\hat{\sigma}_v^2 = \hat{\sigma}_a^2 + \hat{\sigma}_v^2$ .

We can relax assumption (16.48) and still obtain consistent,  $\sqrt{N}$ -asymptotically normal estimates of the APEs. In fact, under assumptions (16.45)–(16.47), we can write

$$y_{it} = \max(0, \psi + \mathbf{x}_{it}\boldsymbol{\beta} + \overline{\mathbf{x}}_{i}\boldsymbol{\xi} + v_{it})$$
(16.52)

$$v_{it} | \mathbf{x}_i \sim \text{Normal}(0, \sigma_v^2), \qquad t = 1, 2, \dots, T$$
 (16.53)

where  $v_{it} = a_i + u_{it}$ . Without further assumptions, the  $v_{it}$  are arbitrarily serially correlated, and so maximum likelihood analysis using the density of  $\mathbf{y}_i$  given  $\mathbf{x}_i$  would be computationally demanding. However, we can obtain  $\sqrt{N}$ -asymptotically normal estimators by a simple pooled Tobit procedure of  $y_{it}$  on 1,  $\mathbf{x}_{it}$ ,  $\overline{\mathbf{x}}_i$ ,  $t = 1, \ldots, T$ ,  $i = 1, \ldots, N$ . While we can only estimate  $\sigma_v^2$  from this procedure, it is all we need—along with  $\hat{\psi}$ ,  $\hat{\beta}$ , and  $\hat{\xi}$ —to obtain the average partial effects based on expression (16.51). The robust variance matrix for partial MLE derived in Section 13.8.2 should be used for standard errors and inference. A minimum distance approach, analogous to the probit case discussed in Section 15.8.2, is also available.

When we are interested only in  $\beta$ , such as in data-censoring cases or when we are interested in  $\text{Med}(y_t | \mathbf{x}, c) = \max(0, \mathbf{x}_t \boldsymbol{\beta} + c)$ , it is useful to have an estimator of  $\boldsymbol{\beta}$  that does not require distributional assumptions for  $u_{it}$  or  $c_i$ . Honoré (1992) uses a clever transformation that eliminates  $c_i$  and provides estimating equations for  $\boldsymbol{\beta}$ . See also Honoré and Kyriazidou (2000b) and Arellano and Honoré (in press).

#### 16.8.3 Dynamic Unobserved Effects Tobit Models

We now turn to a specific dynamic model

$$y_{it} = \max(0, \mathbf{z}_{it}\boldsymbol{\delta} + \rho_1 y_{i,t-1} + c_i + u_{it})$$
(16.54)

{552}------------------------------------------------

$$u_{it} \mid (\mathbf{z}_i, y_{i,t-1}, \dots, y_{i0}, c_i) \sim \text{Normal}(0, \sigma_u^2), \qquad t = 1, \dots, T$$
 (16.55)

We can embellish this model in many ways. For example, the lagged effect of  $y_{i,t-1}$  can depend on whether  $y_{i,t-1}$  is zero or greater than zero. Thus, we might replace  $\rho_1 y_{i,t-1}$  by  $\eta_1 r_{i,t-1} + \rho_1 (1 - r_{i,t-1}) y_{i,t-1}$ , where  $r_{it}$  is a binary variable equal to unity if  $y_{it} = 0$ . Or, we can let the variance of  $u_{it}$  change over time. The basic approach does not depend on the particular model.

The model in equation (16.54) is suitable only for corner solution applications. In data-censoring cases, it makes more sense to have a dynamic linear model  $y_{it}^* = \mathbf{z}_{it}\boldsymbol{\delta} + \rho_1 y_{i,t-1}^* + c_i + u_{it}$  and then to introduce the data-censoring mechanism for each time period. This approach leads to  $y_{i,t-1}^*$  in equation (16.54) and is considerably more difficult to handle.

The discussion in Section 15.8.4 about how to handle the initial value problem also holds here (see Section 13.9.2 for the general case). A fairly general and tractable approach is to specify a distribution for the unobserved effect,  $c_i$ , given the initial value,  $y_{i0}$ , and the exogenous variables in all time periods,  $\mathbf{z}_i$ . Let  $h(c \mid y_0, \mathbf{z}; \gamma)$  denote such a density. Then the joint density of  $(y_1, \dots, y_T)$  given  $(y_0, \mathbf{z})$  is

$$\int_{-\infty}^{\infty} \prod_{t=1}^{T} f(y_t | y_{t-1}, \dots y_1, y_0, \mathbf{z}, c; \boldsymbol{\theta}) h(c | y_0, \mathbf{z}; \gamma) dc$$
 (16.56)

where  $f(y_t | y_{t-1}, \dots, y_1, y_0, \mathbf{z}, c; \boldsymbol{\theta})$  is the censored-at-zero normal distribution with mean  $\mathbf{z}_t \boldsymbol{\delta} + \rho_1 y_{t-1} + c$  and variance  $\sigma_u^2$ . A natural specification for  $h(c | y_0, \mathbf{z}; \gamma)$  is Normal( $\psi + \xi_0 y_0 + \mathbf{z} \boldsymbol{\xi}, \sigma_a^2$ ), where  $\sigma_a^2 = \text{Var}(c | y_0, \mathbf{z})$ . This leads to a fairly straightforward procedure. To see why, write  $c_i = \psi + \xi_0 y_{i0} + \mathbf{z}_i \boldsymbol{\xi} + a_i$ , so that

$$y_{it} = \max(0, \psi + \mathbf{z}_{it}\boldsymbol{\delta} + \rho_1 y_{i,t-1} + \xi_0 y_{i0} + \mathbf{z}_i \boldsymbol{\xi} + a_i + u_{it})$$

where the distribution of  $a_i$  given  $(y_{i0}, \mathbf{z}_i)$  is Normal $(0, \sigma_a^2)$ , and assumption (16.55) holds with  $a_i$  replacing  $c_i$ . The density in expression (16.56) then has the same form as the random effects Tobit model, where the explanatory variables at time t are  $(\mathbf{z}_{it}, y_{i,t-1}, y_{i0}, \mathbf{z}_i)$ . The inclusion of the initial condition in each time period, as well as the entire vector  $\mathbf{z}_i$ , allows for the unobserved heterogeneity to be correlated with the initial condition and the strictly exogenous variables. Standard software can be used to test for state dependence  $(\rho_1 \neq 0)$ .

Average partial effects can be estimated by modification of the probit results in Section 15.8.4 and the formulas in Section 16.8.2. See Wooldridge (2000e) for details.

Honoré (1993a) obtains orthogonality conditions that can be used in a method of moments framework to estimate  $\delta$  and  $\rho_1$  in equation (16.54) without making distributional assumptions about  $c_i$ . The assumptions on  $u_{it}$  restrict the dependence across time but do not include distributional assumptions. Because no distributional

{553}------------------------------------------------

assumptions are made, partial effects on the conditional mean cannot be estimated using Honoré's approach.

#### **Problems**

**16.1.** Let  $t_i^*$  denote the duration of some event, such as unemployment, measured in continuous time. Consider the following model for  $t_i^*$ :

$$t_i^* = \exp(\mathbf{x}_i \boldsymbol{\beta} + u_i), \qquad u_i \mid \mathbf{x}_i \sim \text{Normal}(0, \sigma^2)$$
  
 $t_i = \min(t_i^*, c)$ 

where c > 0 is a known censoring constant.

- a. Find  $P(t_i = c \mid \mathbf{x}_i)$ , that is, the probability that the duration is censored. What happens as  $c \to \infty$ ?
- b. What is the density of  $\log(t_i)$  (given  $\mathbf{x}_i$ ) when  $t_i < c$ ? Now write down the full density of  $\log(t_i)$  given  $\mathbf{x}_i$ .
- c. Write down the log-likelihood function for observation i.
- d. Partition  $\beta$  into the  $K_1 \times 1$  and  $K_2 \times 1$  vectors  $\beta_1$  and  $\beta_2$ . How would you test  $H_0$ :  $\beta_2 = 0$ ? Be specific.
- e. Obtain the log-likelihood function if the censoring time is potentially different for each person, so that  $t_i = \min(t_i^*, c_i)$ , where  $c_i$  is observed for all i. Assume that  $u_i$  is independent of  $(\mathbf{x}_i, c_i)$ .
- **16.2.** In some occupations, such as major league baseball, salary floors exist. This situation can be described by the model

$$wage^* = \exp(\mathbf{x}\boldsymbol{\beta} + u), \qquad u \mid \mathbf{x} \sim \text{Normal}(0, \sigma^2)$$
  
 $wage = \max(c, wage^*)$ 

where c > 0 is the known salary floor (the minimum wage),  $wage^*$  is the person's true worth, and  $\mathbf{x}$  contains productivity and demographic variables.

- a. Show how to turn this into a standard censored Tobit model.
- b. Why is  $E(wage^* | \mathbf{x})$ , rather than  $E(wage^* | \mathbf{x}, wage^* > c)$  or  $E(wage | \mathbf{x})$ , of interest in this application?
- **16.3.** Suppose that, for a random draw  $(\mathbf{x}_i, y_i)$  from the population,  $y_i$  is a **doubly censored variable**:

{554}------------------------------------------------

$$y_i^* \mid \mathbf{x}_i \sim \text{Normal}(\mathbf{x}_i \boldsymbol{\beta}, \sigma^2)$$
  
 $y_i = a_1 \quad \text{if } y_i^* \le a_1$   
 $y_i = y_i^* \quad \text{if } a_1 < y_i^* < a_2$   
 $y_i = a_2 \quad \text{if } y_i^* \ge a_2$ 

where  $\mathbf{x}_i$  is  $1 \times K$ ,  $\boldsymbol{\beta}$  is  $K \times 1$ , and  $a_1 < a_2$  are known censoring constants. This may be a data-censoring problem—for example,  $y^*$  may be both top coded and bottom coded in a survey—in which case we are interested in  $\mathrm{E}(y_i^* | \mathbf{x}_i) = \mathbf{x}_i \boldsymbol{\beta}$ . Or,  $y_i$  may be the outcome of a constrained optimization problem with corners at  $a_1$  and  $a_2$ , such as when  $y_i$  is the proportion of person i's pension assets invested in the stock market, so that  $a_1 = 0$  and  $a_2 = 1$ .

- a. Find  $P(y = a_1 | \mathbf{x})$  and  $P(y = a_2 | \mathbf{x})$  in terms of the standard normal cdf,  $\mathbf{x}$ ,  $\boldsymbol{\beta}$ , and  $\sigma$ . For  $a_1 < y < a_2$ , find  $P(y \le y | \mathbf{x})$ , and use this to find the density of y given  $\mathbf{x}$  for  $a_1 < y < a_2$ .
- b. If  $z \sim \text{Normal}(0, 1)$ , it can be shown that  $E(z | c_1 < z < c_2) = \{\phi(c_1) \phi(c_2)\}/\{\Phi(c_2) \Phi(c_1)\}$  for  $c_1 < c_2$ . Use this fact to find  $E(y | \mathbf{x}, a_1 < y < a_2)$  and  $E(y | \mathbf{x})$ .
- c. Consider the following method for estimating  $\beta$ . Using only the uncensored observations, that is, observations for which  $a_1 < y_i < a_2$ , run the OLS regression of  $y_i$  on  $\mathbf{x}_i$ . Explain why this does not generally produce a consistent estimator of  $\beta$ .
- d. Write down the log-likelihood function for observation *i*; it should consist of three parts.
- e. For a corner solution, how would you estimate  $E(y | \mathbf{x}, a_1 < y < a_2)$  and  $E(y | \mathbf{x})$ ?
- f. Show that

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_j} = \{\Phi[(a_2 - \mathbf{x}\boldsymbol{\beta})/\sigma] - \Phi[(a_1 - \mathbf{x}\boldsymbol{\beta})/\sigma]\}\beta_j$$

Why is the scale factor multiplying  $\beta_j$  necessarily between zero and one?

- g. For a corner solution outcome, suppose you obtain  $\hat{\gamma}$  from a standard OLS regression of  $y_i$  on  $\mathbf{x}_i$ , using all observations. Would you compare  $\hat{\gamma}_j$  to the Tobit estimate,  $\hat{\beta}_j$ ? What would be a sensible comparison?
- h. For data censoring, how would the analysis change if  $a_1$  and  $a_2$  were replaced with  $a_{i1}$  and  $a_{i2}$ , respectively, where  $u_i$  is independent of  $(\mathbf{x}_i, a_{i1}, a_{i2})$ ?
- **16.4.** Use the data in JTRAIN1.RAW for this question.

{555}------------------------------------------------

a. Using only the data for 1988, estimate a linear equation relating *hrsemp* to log(*employ*), *union*, and *grant*. Compute the usual and heteroskedasticity-robust standard errors. Interpret the results.

- b. Out of the 127 firms with nonmissing data on all variables, how many have hrsemp = 0? Estimate the model from part a by Tobit. Find the estimated effect of grant on  $E(hrsemp \mid employ, union, grant, hrsemp > 0)$  at the average employment for the 127 firms and union = 1. What is the effect on  $E(hrsemp \mid employ, union, grant)$ ?
- c. Are log(*employ*) and *union* jointly significant in the Tobit model?
- d. In terms of goodness of fit for the conditional mean, do you prefer the linear model or Tobit model for estimating  $E(hrsemp \mid employ, union, grant)$ ?

#### **16.5.** Use the data set FRINGE.RAW for this question.

- a. Estimate a linear model by OLS relating *hrbens* to *exper*, *age*, *educ*, *tenure*, *married*, *male*, *white*, *nrtheast*, *nrthcen*, *south*, and *union*.
- b. Estimate a Tobit model relating the same variables from part a. Why do you suppose the OLS and Tobit estimates are so similar?
- c. Add exper<sup>2</sup> and tenure<sup>2</sup> to the Tobit model from part b. Should these be included?
- d. Are there significant differences in hourly benefits across industry, holding the other factors fixed?
- **16.6.** Consider a Tobit model with an endogenous binary explanatory variable:

$$y_1 = \max(0, \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1)$$
  
 $y_2 = 1[\mathbf{z} \boldsymbol{\delta}_2 + v_2 > 0]$ 

where  $(u_1, v_2)$  is independent of **z** with a bivariate normal distribution with mean zero and  $Var(v_2) = 1$ . If  $u_1$  and  $v_2$  are correlated,  $v_2$  is endogenous.

- a. Find the density of the latent variable,  $y_1^*$ , given  $(\mathbf{z}, y_2)$ . [Hint: As shown in Section 16.6.2, the density of  $y_1$  given  $(\mathbf{z}, v_2)$  is normal with mean  $\mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + \rho_1 v_2$  and variance  $\sigma_1^2 \rho_1^2$ , where  $\rho_1 = \text{Cov}(u_1, v_2)$ . Integrate against the density of  $v_2$  given  $(\mathbf{z}, y_2 = 1)$ , as in equation (15.55), and similarly for  $y_2 = 0$ .]
- b. Write down the log-likelihood function for the parameters  $\delta_1$ ,  $\alpha_1$ ,  $\sigma_1^2$ ,  $\delta_2$ , and  $\rho_1$  for observation *i*.
- **16.7.** Suppose that y given x follows Cragg's model from Section 16.7.
- a. Show that  $E(y | \mathbf{x}, y > 0) = \mathbf{x}\boldsymbol{\beta} + \sigma\lambda(\mathbf{x}\boldsymbol{\beta}/\sigma)$ , just as in the standard Tobit model.
- b. Use part a and equation (16.8) to find  $E(y | \mathbf{x})$ .

{556}------------------------------------------------

- c. Show that the elasticity of Eðy j xÞ with respect to, say, x1, is the sum of the elasticities of Pðy > 0 j xÞ and Eðy j x; y > 0Þ.
- 16.8. Consider three different approaches for modeling Eðy j xÞ when yb0 is a corner solution outcome: (1) Eðy j xÞ ¼ x*b*; (2) Eðy j xÞ ¼ expðx*b*Þ; and (3) y given x follows a Tobit model.
- a. How would you estimate models 1 and 2?
- b. Obtain three goodness-of-fit statistics that can be compared across models; each should measure how much sample variation in yi is explained by E^ðyi j xiÞ.
- c. Suppose, in your sample, yi > 0 for all i. Show that the OLS and Tobit estimates of *b* are identical. Does the fact that they are identical mean that the linear model for Eðy j xÞ and the Tobit model produce the same estimates of Eðy j xÞ? Explain.
- d. If y > 0 in the population, does a Tobit model make sense? What is a simple alternative to the three approaches listed at the beginning of this problem? What assumptions are sufficient for estimating Eðy j xÞ?
- 16.9. Let y be the percentage of annual income invested in a pension plan, and assume that a law caps this percentage at 10 percent. Thus, in a sample of data, we observe yi between zero and 10, with pileups at the end points.
- a. What model would you use for y?
- b. Explain the conceptual difference between the outcomes y ¼ 0 and y ¼ 10. In particular, which limit can be viewed as a form of data censoring?
- c. Suppose you want to ask, What is the effect on Eðy j xÞ if the cap were increased from 10 to 11? How would you estimate this? (Hint: Call the upper bound a2, and take a derivative.)
- d. If there are no observations at y ¼ 10, what does the estimated model reduce to?
- 16.10. Provide a careful derivation of equation (16.16). It will help to use the fact that dfðzÞ=dz ¼ zfðzÞ.
- 16.11. Let y be a corner solution response, and let Lðy j 1; xÞ ¼ g<sup>0</sup> þ x*g* be the linear projection of y onto an intercept and x, where x is 1 - K. If we use a random sample on ðx; yÞ to estimate g<sup>0</sup> and *g* by OLS, are the estimators inconsistent because of the corner solution nature of y? Explain.
- 16.12. Use the data in APPLE.RAW for this question. These are phone survey data, where each respondent was asked the amount of ''ecolabeled'' (or ''ecologically friendly'') apples he or she would purchase at given prices for both ecolabeled apples

{557}------------------------------------------------

and regular apples. The prices are cents per pound, and *ecolbs* and *reglbs* are both in pounds.

- a. For what fraction of the sample is  $ecolbs_i = 0$ ? Discuss generally whether ecolbs is a good candidate for a Tobit model.
- b. Estimate a linear regression model for *ecolbs*, with explanatory variables log(ecoprc), log(regprc), log(faminc), educ, hhsize, and  $num5\_17$ . Are the signs of the coefficient for log(ecoprc) and log(regprc) the expected ones? Interpret the estimated coefficient on log(ecoprc).
- c. Test the linear regression in part b for heteroskedasticity by running the regression  $\hat{u}^2$  on 1,  $ec\hat{o}lbs$ ,  $ec\hat{o}lbs^2$  and carrying out an F test. What do you conclude?
- d. Obtain the OLS fitted values. How many are negative?
- e. Now estimate a Tobit model for *ecolbs*. Are the signs and statistical significance of the explanatory variables the same as for the linear regression model? What do you make of the fact that the Tobit estimate on log(*ecoprc*) is about twice the size of the OLS estimate in the linear model?
- f. Obtain the estimated partial effect of log(ecoprc) for the Tobit model using equation (16.16), where the  $x_j$  are evaluated at the mean values. What is the estimated price elasticity (again, at the mean values of the  $x_i$ )?
- g. Reestimate the Tobit model dropping the variable log(regprc). What happens to the coefficient on log(ecoprc)? What kind of correlation does this result suggest between log(ecoprc) and log(regprc)?
- h. Reestimate the model from part e, but with *ecoprc* and *regprc* as the explanatory variables, rather than their natural logs. Which functional form do you prefer? (Hint: Compare log-likelihood functions.)
- **16.13.** Suppose that, in the context of an unobserved effects Tobit (or probit) panel data model, the mean of the unobserved effect,  $c_i$ , is related to the time average of *detrended*  $\mathbf{x}_{it}$ . Specifically,

$$c_i = \left[ (1/T) \sum_{t=1}^{T} (\mathbf{x}_{it} - \boldsymbol{\pi}_t) \right] \boldsymbol{\xi} + a_i$$

where  $\pi_t = \mathrm{E}(\mathbf{x}_{it})$ ,  $t = 1, \dots, T$ , and  $a_i \, | \, \mathbf{x}_i \sim \mathrm{Normal}(0, \sigma_a^2)$ . How does this extension of equation (16.44) affect estimation of the unobserved effects Tobit (or probit) model?

**16.14.** Consider the random effects Tobit model under assumptions (16.42), (16.43), and (16.48), but replace assumption (16.44) with

{558}------------------------------------------------

$$c_i \mid \mathbf{x}_i \sim \text{Normal}[\psi + \overline{\mathbf{x}}_i \boldsymbol{\xi}, \sigma_a^2 \exp(\overline{\mathbf{x}}_i \boldsymbol{\lambda})]$$

See Problem 15.18 for the probit case.

- a. What is the density of  $y_{it}$  given  $(\mathbf{x}_i, a_i)$ , where  $a_i = c_i \mathrm{E}(c_i | \mathbf{x}_i)$ ?
- b. Derive the log-likelihood function by first finding the density of  $(y_{i1}, \dots, y_{iT})$  given  $\mathbf{x}_i$ .
- c. Assuming you have estimated  $\beta$ ,  $\sigma_u^2$ ,  $\psi$ ,  $\xi$ ,  $\sigma_a^2$ , and  $\lambda$  by CMLE, how would you estimate the average partial effects?
- **16.15.** Explain why the Smith and Blundell (1986) procedure (Procedure 16.1 in Section 16.6.2) extends immediately to the model

$$y_1 = \max[0, \mathbf{z}_1 \boldsymbol{\delta}_1 + \mathbf{g}(y_2)\boldsymbol{\alpha}_1 + u_1]$$

where  $\mathbf{g}(y_2)$  is a row vector of functions of  $y_2$ , under equation (16.27) and the assumption that  $(u_1, v_2)$  is bivariate normal and independent of  $\mathbf{z}$ . (See Problem 15.20 for the probit case.)

{559}------------------------------------------------