# Time-Varying Covariates

> Pages: 717-720

Deriving the log likelihood is more complicated with time-varying covariates, especially when we do not assume that the covariates are strictly exogenous. Nevertheless, we will show that, if the covariates are constant within each time interval ½am<sup>1</sup>; amÞ, the form of the log likelihood is the same as expression (20.45), provided x<sup>i</sup> is replaced with xim in interval m.

For the population, let x1; x2; ... ; x<sup>M</sup> denote the outcomes of the covariates in each of the M time intervals, where we assume that the covariates are constant within an interval. This assumption is clearly an oversimplification, but we cannot get very far without it (and it reflects how data sets with time-varying covariates are usually constructed). When the covariates are internal and are not necessarily defined after exit from the initial state, the definition of the covariates in the time intervals is irrelevant; but it is useful to list covariates for all M time periods.

We assume that the hazard at time t conditional on the covariates up through time t depends only on the covariates at time t. If past values of the covariates matter, they can simply be included in the covariates at time t. The conditional independence assumption on the censoring indicators is now stated as

$$D(T | T \ge a_{m-1}, \mathbf{x}_m, c_m) = D(T | T \ge a_{m-1}, \mathbf{x}_m), \qquad m = 1, \dots, M$$
(20.50)

This assumption allows the censoring decision to depend on the covariates during the time interval (as well as past covariates, provided they are either included in x<sup>m</sup> or do not affect the distribution of T given xm). Under this assumption, the probability of exit (without censoring) is

{718}------------------------------------------------

$$P(y_{m} = 1 \mid y_{m-1} = 0, \mathbf{x}_{m}, c_{m} = 0) = P(a_{m-1} \leq T < a_{m} \mid T \geq a_{m-1}, \mathbf{x}_{m})$$

$$= 1 - \exp\left[-\int_{a_{m-1}}^{a_{m}} \lambda(s; \mathbf{x}_{m}, \boldsymbol{\theta}) ds\right] \equiv 1 - \alpha_{m}(\mathbf{x}_{m}, \boldsymbol{\theta})$$
(20.51)

We can use equation (20.51), along with  $P(y_m = 0 \mid y_{m-1} = 0, \mathbf{x}_m, c_m = 0) = \alpha_m(\mathbf{x}_m, \boldsymbol{\theta})$ , to build up a partial log likelihood for person *i*. As we discussed in Section 13.8, this is only a partial likelihood because we are not necessarily modeling the joint distribution of  $(y_1, \ldots, y_M)$  given  $\{(\mathbf{x}_1, c_1), \ldots, (c_M, \mathbf{x}_M)\}$ .

For someone censored in interval m, the information on the duration is contained in  $y_{i1} = 0, \dots, y_{i,m-1} = 0$ . For someone who truly exits in interval m, there is additional information in  $y_{im} = 1$ . Therefore, the partial log likelihood is given by expression (20.45), but, to reflect the time-varying covariates,  $\alpha_h(\mathbf{x}_i, \boldsymbol{\theta})$  is replaced by  $\alpha_h(\mathbf{x}_{ih}, \boldsymbol{\theta})$  and  $\alpha_{m_i}(\mathbf{x}_i, \boldsymbol{\theta})$  is replaced by  $\alpha_{m_i}(\mathbf{x}_{i,m_i}, \boldsymbol{\theta})$ .

Each term in the partial log likelihood represents the distribution of  $y_m$  given  $(y_{m-1},\ldots,y_1)$ ,  $(\mathbf{x}_m,\ldots,\mathbf{x}_1)$ , and  $(c_m,\ldots,c_1)$ . [Most of the probabilities in this conditional distribution are either zero or one; only the probabilities that depend on  $\theta$  are shown in expression (20.45).] Therefore, the density is *dynamically complete*, in the terminology of Section 13.8.3. As shown there, the usual maximum likelihood variance matrix estimators and statistics are asymptotically valid, even though we need not have the full conditional distribution of  $\mathbf{y}$  given  $(\mathbf{x}, \mathbf{c})$ . This result would change if, for some reason, we chose not to include past covariates when in fact they affect the current probability of exit even after conditioning on the current covariates. Then the robust forms of the statistics covered in Section 13.8 should be used. In most duration applications we want dynamic completeness.

If the covariates are strictly exogenous and if the censoring is strictly exogenous, then the partial likelihood is the full conditional likelihood. The precise strict exogeneity assumption is

$$D(T | T \ge a_{m-1}, \mathbf{x}, \mathbf{c}) = D(T | T \ge a_{m-1}, \mathbf{x}_m), \qquad m = 1, \dots, M$$
(20.52)

where  $\mathbf{x}$  is the vector of covariates across all time periods and  $\mathbf{c}$  is the vector of censoring indicators. There are two parts to this assumption. Ignoring the censoring, assumption (20.52) means that neither future nor past covariates appear in the hazard, once current covariates are controlled for. The second implication of assumption (20.52) is that the censoring is also strictly exogenous.

With time-varying covariates, the hazard specification

$$\lambda(t; \mathbf{x}_m, \boldsymbol{\theta}) = \kappa(\mathbf{x}_m, \boldsymbol{\beta}) \lambda_m, \qquad a_{m-1} \le t < a_m$$
 (20.53)

{719}------------------------------------------------

m = 1, ..., M, is still attractive. It implies that the covariates have a multiplicative effect in each time interval, and it allows the baseline hazard—the part common to all members of the population—to be flexible.

Meyer (1990) essentially uses the specification (20.53) to estimate the effect of unemployment insurance on unemployment spells. McCall (1994) shows how to allow for time-varying coefficients when  $\kappa(\mathbf{x}_m, \boldsymbol{\beta}) = \exp(\mathbf{x}_m \boldsymbol{\beta})$ . In other words,  $\boldsymbol{\beta}$  is replaced with  $\boldsymbol{\beta}_m$ ,  $m = 1, \dots, M$ .

#### 20.4.3 Unobserved Heterogeneity

We can also add unobserved heterogeneity to hazards specified for grouped data, even if we have time-varying covariates. With time-varying covariates and unobserved heterogeneity, it is difficult to relax the strict exogeneity assumption. Also, with single-spell data, we cannot allow general correlation between the unobserved heterogeneity and the covariates. Therefore, we assume that the covariates are strictly exogenous conditional on unobserved heterogeneity *and* that the unobserved heterogeneity is independent of the covariates.

The precise assumptions are given by equation (20.52) but where unobserved heterogeneity, v, appears in both conditioning sets. In addition, we assume that v is independent of  $(\mathbf{x}, \mathbf{c})$  (which is a further sense in which the censoring is exogenous).

In the leading case of the piecewise-constant baseline hazard, equation (20.53) becomes

$$\lambda(t; v, \mathbf{x}_m, \boldsymbol{\theta}) = v\kappa(\mathbf{x}_m, \boldsymbol{\beta})\lambda_m, \qquad a_{m-1} \le t < a_m$$
(20.54)

where v > 0 is a continuously distributed heterogeneity term. Using the same reasoning as in Sections 20.4.1 and 20.4.2, the density of  $(y_{i1}, \ldots, y_{iM})$  given  $(v_i, \mathbf{x}_i, \mathbf{c}_i)$  is

$$\left[\prod_{h=1}^{m_i-1} \alpha_h(v_i, \mathbf{x}_{ih}, \boldsymbol{\theta})\right] \left[1 - \alpha_{m_i}(v_i, \mathbf{x}_{i, m_i}, \boldsymbol{\theta})\right]^{d_i}$$
(20.55)

where  $d_i = 1$  if observation i is uncensored. Because expression (20.55) depends on the unobserved heterogeneity,  $v_i$ , we cannot use it directly to consistently estimate  $\theta$ . However, because  $v_i$  is independent of  $(\mathbf{x}_i, \mathbf{c}_i)$ , with density  $g(v; \delta)$ , we can integrate expression (20.55) against  $g(\cdot; \delta)$  to obtain the density of  $(y_{i1}, \ldots, y_{iM})$  given  $(\mathbf{x}_i, \mathbf{c}_i)$ . This density depends on the observed data— $(m_i, d_i, \mathbf{x}_i)$ —and the parameters  $\theta$  and  $\delta$ . From this density, we construct the conditional log likelihood for observation i, and we can obtain the conditional MLE, just as in other nonlinear models with unobserved heterogeneity—see Chapters 15, 16, and 19. Meyer (1990) assumes that the distribution of  $v_i$  is gamma, with unit mean, and obtains the log-likelihood function

{720}------------------------------------------------

in closed form. McCall (1994) analyzes a heterogeneity distribution that contains the gamma as a special case.

It is possible to consistently estimate *b* and *l* without specifying a parametric form for the heterogeneity distribution; this approach results in a semiparametric maximum likelihood estimator. Heckman and Singer (1984) first showed how to perform this method with a Weibull baseline hazard, and Meyer (1990) proved consistency when the hazard has the form (20.54). The estimated heterogeneity distribution is discrete and, in practice, has relatively few mass points. The consistency argument works by allowing the number of mass points to increase with the sample size. Computation is a difficult issue, and the asymptotic distribution of the semiparametric maximum likelihood estimator has not been worked out.