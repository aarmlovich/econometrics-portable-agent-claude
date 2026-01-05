# Pooled QMLE

> Pages: 675-677

As with the linear case, we begin by discussing pooled estimation after specifying a model for a conditional mean. Let  $\{(\mathbf{x}_t, y_t): t = 1, 2, ..., T\}$  denote the time series observations for a random draw from the cross section population. We assume that, for some  $\boldsymbol{\beta}_0 \in \mathcal{B}$ ,

$$E(y_t | \mathbf{x}_t) = m(\mathbf{x}_t, \boldsymbol{\beta}_0), \qquad t = 1, 2, \dots, T$$
(19.45)

This assumption simply means that we have a correctly specified parametric model for  $E(y_t | \mathbf{x}_t)$ . For notational convenience only, we assume that the function m itself does not change over time. Relaxing this assumption just requires a notational

{676}------------------------------------------------

change, or we can include time dummies in  $\mathbf{x}_t$ . For  $y_t \ge 0$  and unbounded from above, the most common conditional mean is  $\exp(\mathbf{x}_t\boldsymbol{\beta})$ . There is no restriction on the time dependence of the observations under assumption (19.45), and  $\mathbf{x}_t$  can contain any observed variables. For example, a static model has  $\mathbf{x}_t = \mathbf{z}_t$ , where  $\mathbf{z}_t$  is dated contemporaneously with  $y_t$ . A finite distributed lag has  $\mathbf{x}_t$  containing lags of  $\mathbf{z}_t$ . Strict exogeneity of  $(\mathbf{x}_1, \dots, \mathbf{x}_T)$ , that is,  $\mathrm{E}(y_t | \mathbf{x}_1, \dots, \mathbf{x}_T) = \mathrm{E}(y_t | \mathbf{x}_t)$ , is not assumed. In particular,  $\mathbf{x}_t$  can contain lagged dependent variables, although how these might appear in nonlinear models is not obvious (see Wooldridge, 1997c, for some possibilities). A limitation of model (19.45) is that it does not explicitly incorporate an unobserved effect.

For each i = 1, 2, ..., N,  $\{(\mathbf{x}_{it}, y_{it}): t = 1, 2, ..., T\}$  denotes the time series observations for cross section unit i. We assume random sampling from the cross section.

One approach to estimating  $\beta_0$  is pooled nonlinear least squares, which was introduced in Problem 12.6. When y is a count variable, a Poisson QMLE can be used. This approach is completely analogous to pooled probit and pooled Tobit estimation with panel data. Note, however, that we are not assuming that the Poisson distribution is true.

For each *i* the quasi-log likelihood for pooled Poisson estimation is (up to additive constants)

$$\ell_i(\boldsymbol{\beta}) = \sum_{t=1}^{T} \{ y_{it} \log[m(\mathbf{x}_{it}, \boldsymbol{\beta})] - m(\mathbf{x}_{it}, \boldsymbol{\beta}) \} \equiv \sum_{t=1}^{T} \ell_{it}(\boldsymbol{\beta})$$
(19.46)

The **pooled Poisson QMLE** then maximizes the sum of  $\ell_i(\beta)$  across i = 1, ..., N. Consistency and asymptotic normality of this estimator follows from the Chapter 12 results, once we use the fact that  $\beta_0$  maximizes  $E[\ell_i(\beta)]$ ; this follows from GMT (1984a). Thus pooled Poisson estimation is robust in the sense that it consistently estimates  $\beta_0$  under assumption (19.45) only.

Without further assumptions we must be careful in estimating the asymptotic variance of  $\hat{\boldsymbol{\beta}}$ . Let  $\mathbf{s}_i(\boldsymbol{\beta})$  be the  $P \times 1$  score of  $\ell_i(\boldsymbol{\beta})$ , which can be written as  $\mathbf{s}_i(\boldsymbol{\beta}) = \sum_{t=1}^T \mathbf{s}_{it}(\boldsymbol{\beta})$ , where  $\mathbf{s}_{it}(\boldsymbol{\beta})$  is the score of  $\ell_{it}(\boldsymbol{\beta})$ ; each  $\mathbf{s}_{it}(\boldsymbol{\beta})$  has the form (19.12) but with  $(\mathbf{x}_{it}, y_{it})$  in place of  $(\mathbf{x}_i, y_i)$ .

The asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}_{o})$  has the usual form  $\mathbf{A}_{o}^{-1}\mathbf{B}_{o}\mathbf{A}_{o}^{-1}$ , where  $\mathbf{A}_{o} \equiv \sum_{t=1}^{T} \mathrm{E}[\nabla_{\beta}m_{it}(\boldsymbol{\beta}_{o})'\nabla_{\beta}m_{it}(\boldsymbol{\beta}_{o})/m_{it}(\boldsymbol{\beta}_{o})]$  and  $\mathbf{B}_{o} \equiv \mathrm{E}[\mathbf{s}_{i}(\boldsymbol{\beta}_{o})\mathbf{s}_{i}(\boldsymbol{\beta}_{o})']$ . Consistent estimators are

$$\hat{\mathbf{A}} = N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} \nabla_{\beta} \hat{\mathbf{m}}'_{it} \nabla_{\beta} \hat{\mathbf{m}}_{it} / \hat{\mathbf{m}}_{it}$$
(19.47)

{677}------------------------------------------------

$$\hat{\mathbf{B}} = N^{-1} \sum_{i=1}^{N} \mathbf{s}_i(\hat{\boldsymbol{\beta}}) \mathbf{s}_i(\hat{\boldsymbol{\beta}})'$$
(19.48)

and we can use  $\hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1}/N$  for  $\mathrm{Avar}(\hat{\boldsymbol{\beta}})$ . This procedure is fully robust to the presence of serial correlation in the score and arbitrary conditional variances. It should be used in the construction of standard errors and Wald statistics. The quasi-LR statistic is not usually valid in this setup because of neglected time dependence and possible violations of the Poisson variance assumption.

If the conditional mean is dynamically complete in the sense that

$$E(y_t | \mathbf{x}_t, y_{t-1}, \mathbf{x}_{t-1}, \dots, y_1, \mathbf{x}_1) = E(y_t | \mathbf{x}_t)$$
(19.49)

then  $\{\mathbf{s}_{it}(\boldsymbol{\beta}_0): t=1,2,\ldots,T\}$  is serially uncorrelated. Consequently, under assumption (19.49), a consistent estimator of **B** is

$$\hat{\mathbf{B}} = N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} \mathbf{s}_{it} (\hat{\boldsymbol{\beta}}) \mathbf{s}_{it} (\hat{\boldsymbol{\beta}})'$$
(19.50)

Using this equation along with  $\hat{\mathbf{A}}$  produces the asymptotic variance that results from treating the observations as one long cross section, but without the Poisson or GLM variance assumptions. Thus, equation (19.50) affords a certain amount of robustness, but it requires the dynamic completeness assumption (19.49).

There are many other possibilities. If we impose the GLM assumption

$$\operatorname{Var}(y_{it} \mid \mathbf{x}_{it}) = \sigma_o^2 m(\mathbf{x}_{it}, \boldsymbol{\beta}_o), \qquad t = 1, 2, \dots, T$$
(19.51)

along with dynamic completeness, then  $Avar(\hat{\beta})$  can be estimated by

$$\hat{\sigma}^2 \left( \sum_{i=1}^N \sum_{t=1}^T \nabla_\beta \hat{\boldsymbol{m}}_{it}' \nabla_\beta \hat{\boldsymbol{m}}_{it} / \hat{\boldsymbol{m}}_{it} \right)^{-1} \tag{19.52}$$

where  $\hat{\sigma}^2 = (NT - P)^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} \tilde{u}_{it}^2$ ,  $\tilde{u}_{it} = \hat{u}_{it} / \sqrt{\hat{m}_{it}}$ , and  $\hat{u}_{it} = y_{it} - m_{it}(\hat{\beta})$ . This estimator results in a standard GLM analysis on the pooled data.