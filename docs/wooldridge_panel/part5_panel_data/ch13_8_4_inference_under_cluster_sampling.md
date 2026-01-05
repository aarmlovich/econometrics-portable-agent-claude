# Inference under Cluster Sampling

> Pages: 420-424

Partial MLE methods are also useful when using cluster samples. Suppose that, for each group or cluster g, fðyg j xg; *y*Þ is a correctly specified conditional density of yg given xg. Here, i indexes the cluster, and as before we assume a large number of clusters N and relatively small group sizes, Gi. The primary issue is that the yig might


{421}------------------------------------------------

be correlated within a cluster, possibly through unobserved cluster effects. A partial MLE of *y*<sup>o</sup> is defined exactly as in the panel data case, except that t is replaced with g and <sup>T</sup> is replaced with Gi for each <sup>i</sup>; for example, equation (13.44) becomes <sup>l</sup>ið*y*<sup>Þ</sup> <sup>1</sup> <sup>P</sup>Gi <sup>g</sup>¼<sup>1</sup> log fðyig j xig; *y*Þ. Obtaining the partial MLE is usually much easier than specifying (or deriving) the joint distribution of y<sup>i</sup> conditional on x<sup>i</sup> for each cluster i and employing MLE (which must recognize that the cluster observations cannot be identically distributed if the cluster sizes differ).

In addition to allowing the yig to be arbitrarily dependent within a cluster, the partial MLE does not require Dðyig j x<sup>i</sup>1; ... ; xiGi Þ ¼ Dðyig j xigÞ. But we need to compute the robust variance matrix estimator as in Section 13.8.2, along with robust test statistics. The quasi-likelihood ratio statistic is not valid unless Dðyig j xiÞ ¼ Dðyig j xigÞ and the yig are independent within each cluster, conditional on xi.

We can use partial MLE analysis to test for peer effects in cluster samples, as discussed briefly in Section 11.5 for linear models. For example, some elements of xig might be averages of explanatory variables for other units (say, people) in the cluster. Therefore, we might specify a model fgðyg j zg; wðgÞ; *y*Þ (for example, a probit model), where wðg<sup>Þ</sup> represents average characteristics of other people (or units) in the same cluster. The pooled partial MLE analysis is consistent and asymptotically normal, but the variance matrix must be corrected for additional within-cluster dependence.

# 13.9 Panel Data Models with Unobserved Effects

As we saw in Chapters 10 and 11, linear unobserved effects panel data models play an important role in modern empirical research. Nonlinear unobserved effects panel data models are becoming increasingly more important. Although we will cover particular models in Chapters 15, 16, and 19, it is useful to have a general treatment.

# 13.9.1 Models with Strictly Exogenous Explanatory Variables

For each i, let fðyit; xitÞ: t ¼ 1; 2; ... ; Tg be a random draw from the cross section, where yit and xit can both be vectors. Associated with each cross section unit i is unobserved heterogeneity, ci, which could be a vector. We assume interest lies in the distribution of yit given ðxit; ciÞ. The vector xit can contain lags of contemporaneous variables, say zit [for example, xit ¼ ðzit; z<sup>i</sup>;t<sup>1</sup>; z<sup>i</sup>;t<sup>2</sup>Þ, or even leads of zit [for example, xit ¼ ðzit; z<sup>i</sup>;tþ<sup>1</sup>Þ, but not lags of yit. Whatever the lag structure, we let t ¼ 1 denote the first time period available for estimation.

Let ftðy<sup>t</sup> j xt; c; *y*Þ denote a correctly specified density for each t. A key assumption on xit is analogous to the strict exogeneity assumption for linear unobserved effects 

{422}------------------------------------------------

models:  $\mathbf{D}(\mathbf{y}_{it} | \mathbf{x}_i, \mathbf{c}_i) = \mathbf{D}(\mathbf{y}_{it} | \mathbf{x}_{it}, \mathbf{c}_i)$ , which means that only contemporaneous  $\mathbf{x}_{it}$  matters once  $\mathbf{c}_i$  is also conditioned on. (Whether or not  $\mathbf{x}_{it}$  contains lagged  $\mathbf{z}_{it}$ , strict exogeneity conditional on  $\mathbf{c}_i$  rules out certain kinds of feedback from  $y_{it}$  to  $\mathbf{z}_{i,t+h}$ , h > 0.)

In many cases we want to allow  $\mathbf{c}_i$  and  $\mathbf{x}_i$  to be dependent. A general approach to estimating  $\boldsymbol{\theta}_0$  (and other quantities of interest) is to model the distribution of  $\mathbf{c}_i$  given  $\mathbf{x}_i$ . [In Chapters 15 and 19 we cover some important models where  $\boldsymbol{\theta}_0$  can be consistently estimated without making any assumptions about  $\mathbf{D}(\mathbf{c}_i \mid \mathbf{x}_i)$ .] Let  $h(\mathbf{c} \mid \mathbf{x}; \boldsymbol{\delta})$  be a correctly specified density for  $\mathbf{c}_i$  given  $\mathbf{x}_i = \mathbf{x}$ .

There are two common ways to proceed. First, we can make the additional assumption that, conditional on  $(\mathbf{x}_i, \mathbf{c}_i)$ , the  $\mathbf{y}_{it}$  are independent. Then, the joint density of  $(\mathbf{y}_{i1}, \dots, \mathbf{y}_{iT})$ , given  $(\mathbf{x}_i, \mathbf{c}_i)$ , is

$$\prod_{t=1}^{T} f_t(\mathbf{y}_t | \mathbf{x}_{it}, \mathbf{c}_i; \boldsymbol{\theta})$$

We cannot use this density directly to estimate  $\theta_0$  because we do not observe the outcomes  $\mathbf{c}_i$ . Instead, we can use the density of  $\mathbf{c}_i$  given  $\mathbf{x}_i$  to integrate out the dependence on  $\mathbf{c}$ . The density of  $\mathbf{y}_i$  given  $\mathbf{x}_i$  is

$$\int_{\mathbb{R}^J} \left[ \prod_{t=1}^T f_t(\mathbf{y}_t | \mathbf{x}_{it}, \mathbf{c}; \boldsymbol{\theta}_0) \right] h(\mathbf{c} | \mathbf{x}_i; \boldsymbol{\delta}_0) d\mathbf{c}$$
(13.56)

where J is the dimension of  $\mathbf{c}$  and  $h(\mathbf{c} \mid \mathbf{x}; \boldsymbol{\delta})$  is the correctly specified model for the density of  $\mathbf{c}_i$  given  $\mathbf{x}_i = \mathbf{x}$ . For concreteness, we assume that  $\mathbf{c}$  is a continuous random vector. For each i, the log-likelihood function is

$$\log \left\{ \int_{\mathbb{R}^{J}} \left[ \prod_{t=1}^{T} f_{t}(\mathbf{y}_{it} \mid \mathbf{x}_{it}, \mathbf{c}; \boldsymbol{\theta}_{o}) \right] h(\mathbf{c} \mid \mathbf{x}_{i}; \boldsymbol{\delta}_{o}) d\mathbf{c} \right\}$$
(13.57)

[It is important to see that expression (13.57) does not depend on the  $\mathbf{c}_i$ ;  $\mathbf{c}$  has been integrated out.] Assuming identification and standard regularity conditions, we can consistently estimate  $\theta_0$  and  $\delta_0$  by conditional MLE, where the asymptotics are for fixed T and  $N \to \infty$ . The CMLE is  $\sqrt{N}$ -asymptotically normal.

Another approach is often simpler and places no restrictions on the joint distribution of the  $\mathbf{y}_{it}$  [conditional on  $(\mathbf{x}_i, \mathbf{c}_i)$ ]. For each t, we can obtain the density of  $\mathbf{y}_{it}$  given  $\mathbf{x}_i$ :

$$\int_{\mathbb{R}^J} [f_t(\mathbf{y}_t \mid \mathbf{x}_{it}, \mathbf{c}; \boldsymbol{\theta}_{o})] h(\mathbf{c} \mid \mathbf{x}_i; \boldsymbol{\delta}_{o}) d\mathbf{c}$$

{423}------------------------------------------------

Now the problem becomes one of partial MLE. We estimate  $\theta_0$  and  $\delta_0$  by maximizing

$$\sum_{i=1}^{N} \sum_{t=1}^{T} \log \left\{ \int_{\mathbb{R}^{J}} [f_{t}(\mathbf{y}_{it} | \mathbf{x}_{it}, \mathbf{c}; \boldsymbol{\theta})] h(\mathbf{c} | \mathbf{x}_{i}; \boldsymbol{\delta}) d\mathbf{c} \right\}$$
(13.58)

(Actually, using PMLE,  $\theta_0$  and  $\delta_0$  are not always separately identified, although interesting functions of them are. We will see examples in Chapters 15 and 16.) Across time, the scores for each i will necessarily be serially correlated because the  $\mathbf{y}_{it}$  are dependent when we condition only on  $\mathbf{x}_i$ , and not also on  $\mathbf{c}_i$ . Therefore, we must make inference robust to serial dependence, as in Section 13.8.2. In Chapter 15, we will study both the conditional MLE and partial MLE approaches for unobserved effects probit models.

#### 13.9.2 Models with Lagged Dependent Variables

Now assume that we are interested in modeling  $D(\mathbf{y}_{it} | \mathbf{z}_{it}, \mathbf{y}_{i,t-1}, \mathbf{c}_i)$  where, for simplicity, we include only contemporaneous conditioning variables,  $\mathbf{z}_{it}$ , and only one lag of  $\mathbf{y}_{it}$ . Adding lags (or even leads) of  $\mathbf{z}_{it}$  or more lags of  $\mathbf{y}_{it}$  requires only a notational change.

A key assumption is that we have the dynamics correctly specified and that  $\mathbf{z}_i = \{\mathbf{z}_{i1}, \dots, \mathbf{z}_{iT}\}$  is appropriately strictly exogenous (conditional on  $\mathbf{c}_i$ ). These assumptions are both captured by

$$D(\mathbf{y}_{it} | \mathbf{z}_{it}, \mathbf{y}_{i,t-1}, \mathbf{c}_i) = D(\mathbf{y}_{it} | \mathbf{z}_i, \mathbf{y}_{i,t-1}, \dots, \mathbf{y}_{i0}, \mathbf{c}_i)$$
(13.59)

We assume that  $f_t(\mathbf{y}_t | \mathbf{z}_t, \mathbf{y}_{t-1}, \mathbf{c}; \boldsymbol{\theta})$  is a correctly specified density for the conditional distribution on the left-hand side of equation (13.59). Given strict exogeneity of  $\{\mathbf{z}_{it}: t=1,\ldots,T\}$  and dynamic completeness, the density of  $(\mathbf{y}_{i1},\ldots,\mathbf{y}_{iT})$  given  $(\mathbf{z}_i = \mathbf{z}, \mathbf{y}_{i0} = \mathbf{y}_0, \mathbf{c}_i = \mathbf{c})$  is

$$\prod_{t=1}^{T} f_t(\mathbf{y}_t | \mathbf{z}_t, \mathbf{y}_{t-1}, \mathbf{c}; \boldsymbol{\theta}_0)$$
(13.60)

(By convention,  $\mathbf{y}_{i0}$  is the first observation on  $\mathbf{y}_{it}$ .) Again, to estimate  $\boldsymbol{\theta}_{0}$ , we integrate  $\mathbf{c}$  out of this density. To do so, we specify a density for  $\mathbf{c}_{i}$  given  $\mathbf{z}_{i}$  and the initial value  $\mathbf{y}_{i0}$  (sometimes called the **initial condition**). Let  $h(\mathbf{c} \mid \mathbf{z}, \mathbf{y}_{0}; \boldsymbol{\delta})$  denote the model for this conditional density. Then, assuming that we have this model correctly specifed, the density of  $(\mathbf{y}_{i1}, \ldots, \mathbf{y}_{iT})$  given  $(\mathbf{z}_{i} = \mathbf{z}, \mathbf{y}_{i0} = \mathbf{y}_{0})$  is

$$\int_{\mathbb{R}^{J}} \left[ \prod_{t=1}^{T} f_{t}(\mathbf{y}_{t} | \mathbf{z}_{t}, \mathbf{y}_{t-1}, \mathbf{c}; \boldsymbol{\theta}_{o}) \right] h(\mathbf{c} | \mathbf{z}, \mathbf{y}_{0}; \boldsymbol{\delta}_{o}) d\mathbf{c}$$
(13.61)

{424}------------------------------------------------

which, for each i, leads to the log-likelihood function conditional on  $(\mathbf{z}_i, \mathbf{y}_{i0})$ :

$$\log \left\{ \int_{\mathbb{R}^{J}} \left[ \prod_{t=1}^{T} f_{t}(\mathbf{y}_{it} \mid \mathbf{z}_{it}, \mathbf{y}_{i,t-1}, \mathbf{c}; \boldsymbol{\theta}) \right] h(\mathbf{c} \mid \mathbf{z}_{i}, \mathbf{y}_{i0}; \boldsymbol{\delta}) d\mathbf{c} \right\}$$
(13.62)

We sum expression (13.62) across  $i=1,\ldots,N$  and maximize with respect to  $\boldsymbol{\theta}$  and  $\boldsymbol{\delta}$  to obtain the CMLEs. Provided all functions are sufficiently differentiable and identification holds, the conditional MLEs are consistent and  $\sqrt{N}$ -asymptotically normal, as usual. Because we have fully specified the conditional density of  $(\mathbf{y}_{i1},\ldots,\mathbf{y}_{iT})$  given  $(\mathbf{z}_i,\mathbf{y}_{i0})$ , the general theory of conditional MLE applies directly. [The fact that the distribution of  $\mathbf{y}_{i0}$  given  $\mathbf{z}_i$  would typically depend on  $\boldsymbol{\theta}_0$  has no bearing on the consistency of the CMLE. The fact that we are conditioning on  $\mathbf{y}_{i0}$ , rather than basing the analysis on  $\mathbf{D}(\mathbf{y}_{i0},\mathbf{y}_{i1},\ldots,\mathbf{y}_{iT}\,|\,\mathbf{z}_i)$ , means that we are generally sacrificing efficiency. But by conditioning on  $\mathbf{y}_{i0}$  we do not have to find  $\mathbf{D}(\mathbf{y}_{i0}\,|\,\mathbf{z}_i)$ , something which is very difficult if not impossible.] The asymptotic variance of  $(\hat{\boldsymbol{\theta}}',\hat{\boldsymbol{\delta}}')'$  can be estimated by any of the formulas in equation (13.32) (properly modified to account for estimation of  $\boldsymbol{\theta}_0$  and  $\boldsymbol{\delta}_0$ ).

A weakness of the CMLE approach is that we must specify a density for  $\mathbf{c}_i$  given  $(\mathbf{z}_i, \mathbf{y}_{i0})$ , but this is a price we pay for estimating dynamic, nonlinear models with unobserved effects. The alternative of treating the  $\mathbf{c}_i$  as parameters to estimate—which is, unfortunately, often labeled the "fixed effects" approach—does not lead to consistent estimation of  $\theta_0$ .

In any application, several issues need to be addressed. First, when are the parameters identified? Second, what quantities are we interested in? As we cannot observe  $\mathbf{c}_i$ , we typically want to average out  $\mathbf{c}_i$  when obtaining partial effects. Wooldridge (2000e) shows that average partial effects are generally identified under the assumptions that we have made. Finally, obtaining the CMLE can be very difficult computationally, as can be obtaining the asymptotic variance estimates in equation (13.32). If  $\mathbf{c}_i$  is a scalar, estimation is easier, but there is still a one-dimensional integral to approximate for each i. In Chapters 15, 16, and 19 we will see that, under reasonable assumptions, standard software can be used to estimate dynamic models with unobserved effects, including effects that are averaged across the distribution of heterogeneity. See also Problem 13.11 for application to a dynamic linear model.