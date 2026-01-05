# Dynamic Unobserved Effects Models

> Pages: 502-505

Dynamic models that also contain unobserved effects are important in testing theories and evaluating policies. Here we cover one class of models that illustrates the important points for general dynamic models and is of considerable interest in its own right.

Suppose we date our observations starting at t ¼ 0, so that yi<sup>0</sup> is the first observation on y. For t ¼ 1; ... ; T we are interested in the dynamic unobserved effects model

$$P(y_{it} = 1 \mid y_{i,t-1}, \dots, y_{i0}, \mathbf{z}_i, c_i) = G(\mathbf{z}_{it}\boldsymbol{\delta} + \rho y_{i,t-1} + c_i)$$
(15.74)

where zit is a vector of contemporaneous explanatory variables, z<sup>i</sup> ¼ ðzi1; ... ; ziT Þ, and G can be the probit or logit function. There are several important points about this model. First, the zit are assumed to satisfy a strict exogeneity assumption (conditional on ci), since z<sup>i</sup> appears in the conditioning set on the left-hand side of equation (15.74), but only zit appears on the right-hand side. Second, the probability of success at time t is allowed to depend on the outcome in t 1 as well as unobserved heterogeneity, ci. We saw the linear version in Section 11.1.1. Of particular interest is the hypothesis H0: r ¼ 0. Under this null, the response probability at time t does not depend on past outcomes once ci (and zi) have been controlled for. Even if r ¼ 0, Pðyit ¼ 1 j yi;t<sup>1</sup>; ziÞ 0Pðyit ¼ 1 j ziÞ owing to the presence of ci. But economists are interested in whether there is state dependence—that is, r 00 in equation (15.74) after controlling for the unobserved heterogeneity, ci.

We might also be interested in the effects of zt, as it may contain policy variables. Then, equation (15.74) simply captures the fact that, in addition to an unobserved effect, behavior may depend on past observed behavior.

How can we estimate *d* and r in equation (15.74), in addition to quantities such as average partial effects? First, we can always write

$$f(y_1, y_2, ..., y_T | y_0, \mathbf{z}, c; \boldsymbol{\beta}) = \prod_{t=1}^T f(y_t | y_{t-1}, ..., y_1, y_0, \mathbf{z}_t, c; \boldsymbol{\beta})$$

$$= \prod_{t=1}^T G(\mathbf{z}_t \boldsymbol{\delta} + \rho y_{t-1} + c)^{y_t} [1 - G(\mathbf{z}_t \boldsymbol{\delta} + \rho y_{t-1} + c)]^{1-y_t}$$
(15.75)

With fixed-T asymptotics, this density, because of the unobserved effect c, does not allow us to construct a log-likelihood function that can be used to estimate *b* consistently. Just as in the case with strictly exogenous explanatory variables, treating the

{503}------------------------------------------------

ci as parameters to be estimated does not result in consistent estimators of *d* and r as N ! y. In fact, the simulations in Heckman (1981) show that the incidental parameters problem is even more severe in dynamic models. What we should do is integrate out the unobserved effect c, as we discussed generally in Section 13.9.2.

Our need to integrate c out of the distribution raises the issue of how we treat the initial observations, yi0; this is usually called the initial conditions problem. One possibility is to treat each yi<sup>0</sup> as a nonstochastic starting position for each i. Then, if ci is assumed to be independent of z<sup>i</sup> (as in a pure random effects environment), equation (15.75) can be integrated against the density of c to obtain the density of ðy1; y2; ... ; yTÞ given z; this density also depends on y<sup>0</sup> through fðy<sup>1</sup> j y0; c; z1; *b*Þ. We can then apply conditional MLE. Although treating the yi<sup>0</sup> as nonrandom simplifies estimation, it is undesirable because it effectively means that ci and yi<sup>0</sup> are independent, a very strong assumption.

Another possibility is to first specify a density for yi<sup>0</sup> given ðzi; ciÞ and to multiply this density by equation (15.75) to obtain fðy0; y1; y2; ... ; yT j z; c; *b*; *g*Þ. Next, a density for ci given z<sup>i</sup> can be specified. Finally, fðy0; y1; y2; ... ; yT j z; c; *b*; *g*Þ is integrated against the density hðc j z; *a*Þ to obtain the density of ðyi0; yi1; yi2; ... ; yiT Þ given zi. This density can then be used in an MLE analysis. The problem with this approach is that finding the density of yi<sup>0</sup> given ðzi; ciÞ is very difficult, if not impossible, even if the process is assumed to be in equilibrium. For discussion, see Hsiao (1986, Section 7.4).

Heckman (1981) suggests approximating the conditional density of yi<sup>0</sup> given ðzi; ciÞ and then specifying a density for ci given zi. For example, we might assume that yi<sup>0</sup> follows a probit model with success probability Fðh þ zi*p* þ gciÞ and specify the density of ci given z<sup>i</sup> as normal. Once these two densities are given, they can be multiplied by equation (15.75), and c can be integrated out to approximate the density of ðyi0; yi1; yi2; ... ; yiT Þ given zi; see Hsiao (1986, Section 7.4).

Heckman's (1981) approach attempts to find or approximate the joint distribution of ðyi0; yi1; yi2; ... ; yiTÞ given zi. We discussed an alternative approach in Section 13.9.2: obtain the joint distribution of ðyi1; yi2; ... ; yiTÞ conditional on ðyi0; ziÞ. This allows us to remain agnostic about the distribution of yi<sup>0</sup> given ðzi; ciÞ, which is the primary source of difficulty in Heckman's approach. If we can find the density of ðyi1; yi2; ... ; yiT Þ given ðyi0; ziÞ, in terms of *b* and other parameters, then we can use standard conditional maximum likelihood methods: we are simply conditioning on yi<sup>0</sup> in addition to zi. It is important to see that using the density of ðyi1; yi2; ... ; yiT Þ given ðyi0; ziÞ is not the same as treating yi<sup>0</sup> as nonrandom. Indeed, the model with ci independent of yi0, given zi, is a special case.

{504}------------------------------------------------

To obtain  $f(y_1, y_2, ..., y_T | y_{i0}, \mathbf{z}_i)$ , we need to propose a density for  $c_i$  given  $(y_{i0}, \mathbf{z}_i)$ . This approach is very much like Chamberlain's (1980) approach to static probit models with unobserved effects, except that we now condition on  $y_{i0}$  as well. [Since the density of  $c_i$  given  $\mathbf{z}_i$  is not restricted by the specification (15.75), our choice of the density of  $c_i$  given  $(y_{i0}, \mathbf{z}_i)$  is not logically restricted in any way.] Given a density  $h(c | y_0, \mathbf{z}; \gamma)$ , which depends on a vector of parameters  $\gamma$ , we have

$$f(y_1, y_2, ..., y_T | y_0, \mathbf{z}, \boldsymbol{\theta}) = \int_{-\infty}^{\infty} f(y_1, y_2, ..., y_T | y_0, \mathbf{z}, c; \boldsymbol{\beta}) h(c | y_0, \mathbf{z}; \boldsymbol{\gamma}) dc$$

See Property CD.2 in Chapter 13. The integral can be replaced with a weighted average if the distribution of c is discrete. When  $G = \Phi$  in the model (15.74)—the leading case—a very convenient choice for  $h(c \mid y_0, \mathbf{z}; \gamma)$  is  $\operatorname{Normal}(\psi + \xi_0 y_{i0} + \mathbf{z}_i \boldsymbol{\xi}, \sigma_a^2)$ , which follows by writing  $c_i = \psi + \xi_0 y_{i0} + \mathbf{z}_i \boldsymbol{\xi} + a_i$ , where  $a_i \sim \operatorname{Normal}(0, \sigma_a^2)$  and independent of  $(y_{i0}, \mathbf{z}_i)$ . Then we can write

$$y_{it} = 1[\psi + \mathbf{z}_{it}\boldsymbol{\delta} + \rho y_{i,t-1} + \xi_0 y_{i0} + \mathbf{z}_i \boldsymbol{\xi} + a_i + e_{it} > 0]$$

so that  $y_{it}$  given  $(y_{i,t-1}, \dots, y_{i0}, \mathbf{z}_i, a_i)$  follows a probit model and  $a_i$  given  $(y_{i0}, \mathbf{z}_i)$  is distributed as Normal $(0, \sigma_a^2)$ . Therefore, the density of  $(y_{i1}, \dots, y_{iT})$  given  $(y_{i0}, \mathbf{z}_i)$  has exactly the form in equation (15.64), where  $\mathbf{x}_{it} = (1, \mathbf{z}_{it}, y_{i,t-1}, y_{i0}, \mathbf{z}_i)$  and with a and  $\sigma_a$  replacing c and  $\sigma_c$ , respectively. Conveniently, this result means that we can use standard random effects probit software to estimate  $\psi$ ,  $\delta$ ,  $\rho$ ,  $\xi_0$ ,  $\xi$ , and  $\sigma_a^2$ : we simply expand the list of explanatory variables to include  $y_{i0}$  and  $\mathbf{z}_i$  in each time period. (The approach that treats  $y_{i0}$  and  $\mathbf{z}_i$  as fixed omits  $y_{i0}$  and  $\mathbf{z}_i$  in each time period.) It is simple to test  $H_0$ :  $\rho = 0$ , which means there is no state dependence once we control for an unobserved effect.

Average partial effects can be estimated as in Chamberlain's unobserved effects probit model: for given values of  $\mathbf{z}_t(\mathbf{z}^o)$  and  $y_{t-1}(y_{-1}^o)$ ,  $\mathrm{E}[\Phi(\mathbf{z}^o\boldsymbol{\delta}+\rho y_{-1}^o+c_i)]$  is consistently estimated by  $N^{-1}\sum_{i=1}^N\Phi(\hat{\psi}_a+\mathbf{z}^o\hat{\boldsymbol{\delta}}_a+\hat{\rho}_ay_{-1}^o+\hat{\xi}_{a0}y_{i0}+\mathbf{z}_i\hat{\boldsymbol{\xi}}_a)$ , where the a subscript denotes multiplication by  $(1+\hat{\sigma}_a^2)^{-1/2}$ , and  $\hat{\psi}$ ,  $\hat{\boldsymbol{\delta}}$ ,  $\hat{\rho}$ ,  $\hat{\boldsymbol{\xi}}$ , and  $\hat{\sigma}_a^2$  are the conditional MLEs. See Wooldridge (2000e) for additional details. A mean value expansion can be used to obtain asymptotic standard errors for the APEs, or a bootstrapping approach, as described in Section 12.8.2, can be used.

# 15.8.5 Semiparametric Approaches

Under strict exogeneity of the explanatory variables, it is possible to consistently estimate  $\beta$  up to scale under very weak assumptions. Manski (1987) derives an objective function that identifies  $\beta$  up to scale in the T=2 case when  $e_{i1}$  and  $e_{i2}$  in the

{505}------------------------------------------------

model (15.66) are identically distributed conditional on  $(\mathbf{x}_{i1}, \mathbf{x}_{i2}, c_i)$  and  $\mathbf{x}_{it}$  is strictly exogenous. The estimator is the maximum score estimator applied to the differences  $\Delta y_i$  and  $\Delta \mathbf{x}_i$ . As in the cross-sectional case, it is not known how to estimate the average response probabilities.

Honoré and Kyriazidou (2000a) show how to estimate the parameters in the unobserved effects logit model with a lagged dependent variable and strictly exogenous explanatory variables without making distributional assumptions about the unobserved effect. Unfortunately, the estimators, which are consistent and asymptotically normal, do not generally converge at the usual  $\sqrt{N}$  rate. In addition, as with many semiparametric approaches, discrete explanatory variables such as time dummies are ruled out, and it is not possible to estimate the average partial effects. See also Arellano and Honoré (in press).