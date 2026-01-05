# Negative Binomial Regression Models

> Pages: 664-666

The Poisson regression model nominally maintains assumption (19.2) but retains some asymptotic efficiency under assumption (19.3). A popular alternative to the Poisson QMLE is full maximum likelihood analysis of the NegBin I model of Cameron and Trivedi (1986). NegBin I is a particular parameterization of the negative binomial distribution. An important restriction in the NegBin I model is that it implies assumption (19.3) with s<sup>2</sup> > 1, so that there cannot be underdispersion. (We drop the ''o'' subscript in this section for notational simplicity.) Typically, NegBin I is parameterized through the mean parameters *b* and an additional parameter, h<sup>2</sup> > 0, where s<sup>2</sup> ¼ 1 þ h2. On the one hand, when *b* and h<sup>2</sup> are estimated jointly, the maximum likelihood estimators are generally inconsistent if the NegBin I assumption fails. On the other hand, if the NegBin I distribution holds, then the NegBin I MLE is more efficient than the Poisson QMLE (this conclusion follows from Section 14.5.2). Still, under assumption (19.3), the Poisson QMLE is more efficient than an estimator that requires only the conditional mean to be correctly specified for consistency. On balance, because of its robustness, the Poisson QMLE has the edge over NegBin I for estimating the parameters of the conditional mean. If conditional probabilities need to be estimated, then a more flexible model is probably warranted.

Other count data distributions imply a conditional variance other than assumption (19.3). A leading example is the NegBin II model of Cameron and Trivedi (1986). The NegBin II model can be derived from a model of unobserved heterogeneity in a Poisson model. Specifically, let ci > 0 be unobserved heterogeneity, and assume that

$$y_i | \mathbf{x}_i, c_i \sim \text{Poisson}[c_i m(\mathbf{x}_i, \boldsymbol{\beta})]$$

If we further assume that ci is independent of x<sup>i</sup> and has a gamma distribution with unit mean and VarðciÞ ¼ h2, then the distribution of yi given x<sup>i</sup> can be shown to be negative binomial, with conditional mean and variance

$$E(y_i | \mathbf{x}_i) = m(\mathbf{x}_i, \boldsymbol{\beta}), \tag{19.27}$$

$$\operatorname{Var}(y_i \mid \mathbf{x}_i) = \operatorname{E}[\operatorname{Var}(y_i \mid \mathbf{x}_i, c_i) \mid \mathbf{x}_i] + \operatorname{Var}[\operatorname{E}(y_i \mid \mathbf{x}_i, c_i) \mid \mathbf{x}_i]$$

$$= m(\mathbf{x}_i, \boldsymbol{\beta}) + \eta^2 [m(\mathbf{x}_i, \boldsymbol{\beta})]^2$$
(19.28)

so that the conditional variance of yi given x<sup>i</sup> is a quadratic in the conditional mean. Because we can write equation (19.28) as Eðyi j xiÞ½1 þ h2Eðyi j xiÞ, NegBin II also

{665}------------------------------------------------

implies overdispersion, but where the amount of overdispersion increases with  $E(y_i | \mathbf{x}_i)$ .

The log-likelihood function for observation i is

$$\ell_{i}(\boldsymbol{\beta}, \eta^{2}) = \eta^{-2} \log \left[ \frac{\eta^{-2}}{\eta^{-2} + m(\mathbf{x}_{i}, \boldsymbol{\beta})} \right] + y_{i} \log \left[ \frac{m(\mathbf{x}_{i}, \boldsymbol{\beta})}{\eta^{-2} + m(\mathbf{x}_{i}, \boldsymbol{\beta})} \right] + \log \left[ \Gamma(y_{i} + \eta^{-2}) / \Gamma(\eta^{-2}) \right]$$

$$(19.29)$$

where  $\Gamma(\cdot)$  is the gamma function defined for r > 0 by  $\Gamma(r) = \int_0^\infty z^{r-1} \exp(-z) dz$ .

You are referred to Cameron and Trivedi (1986) for details. The parameters  $\beta$  and  $\eta^2$  can be jointly estimated using standard maximum likelihood methods.

It turns out that, for fixed  $\eta^2$ , the log likelihood in equation (19.29) is in the linear exponential family; see GMT (1984a). Therefore, if we fix  $\eta^2$  at any positive value, say  $\bar{\eta}^2$ , and estimate  $\beta$  by maximizing  $\sum_{i=1}^N \ell_i(\beta, \bar{\eta}^2)$  with respect to  $\beta$ , then the resulting QMLE is consistent under the conditional mean assumption (19.27) *only*: for fixed  $\eta^2$ , the negative binomial QMLE has the same robustness properties as the Poisson QMLE. (Notice that when  $\eta^2$  is fixed, the term involving the gamma function in equation (19.29) does not affect the QMLE.)

The structure of the asymptotic variance estimators and test statistics is very similar to the Poisson regression case. Let

$$\hat{v}_i = \hat{m}_i + \bar{\eta}^2 \hat{m}_i^2 \tag{19.30}$$

be the estimated nominal variance for the given value  $\bar{\eta}^2$ . We simply weight the residuals  $\hat{u}_i$  and gradient  $\nabla_{\beta}\hat{m}_i$  by  $1/\sqrt{\bar{v}_i}$ :

$$\tilde{u}_i = \hat{u}_i / \sqrt{\hat{v}_i}, \qquad \nabla_{\beta} \tilde{m}_i = \nabla_{\beta} \hat{m}_i / \sqrt{\hat{v}_i}$$
(19.31)

For example, under conditions (19.27) and (19.28), a valid estimator of Avar( $\hat{\beta}$ ) is

$$\left(\sum_{i=1}^N \nabla_{\!\beta} \hat{\boldsymbol{m}}_i' \nabla_{\!\beta} \hat{\boldsymbol{m}}_i/\hat{\boldsymbol{v}}_i\right)^{\!-1}$$

If we drop condition (19.28), the estimator in expression (19.14) should be used but with the standardized residuals and gradients given by equation (19.31). Score statistics are modified in the same way.

When  $\eta^2$  is set to unity, we obtain the **geometric QMLE**. A better approach is to replace  $\eta^2$  by a first-stage estimate, say  $\hat{\eta}^2$ , and then estimate  $\beta$  by two-step QMLE. As we discussed in Chapters 12 and 13, sometimes the asymptotic distribution of the first-stage estimator needs to be taken into account. A nice feature of the two-step

{666}------------------------------------------------

QMLE in this context is that the key condition, assumption (12.37), can be shown to hold under assumption (19.27). Therefore, we can ignore the first-stage estimation of  $\eta^2$ .

Under assumption (19.28), a consistent estimator of  $\eta^2$  is easy to obtain, given an initial estimator of  $\boldsymbol{\beta}$  (such as the Poisson QMLE or the geometric QMLE). Given  $\hat{\boldsymbol{\beta}}$ , form  $\hat{\boldsymbol{m}}_i$  and  $\hat{\boldsymbol{u}}_i$  as the usual fitted values and residuals. One consistent estimator of  $\eta^2$  is the coefficient on  $\hat{\boldsymbol{m}}_i^2$  in the regression (through the origin) of  $\hat{\boldsymbol{u}}_i^2 - \hat{\boldsymbol{m}}_i$  on  $\hat{\boldsymbol{m}}_i^2$ ; this is the estimator suggested by Gourieroux, Monfort, and Trognon (1984b) and Cameron and Trivedi (1986). An alternative estimator of  $\eta^2$ , which is closely related to the GLM estimator of  $\sigma^2$  suggested in equation (19.15), is a weighted least squares estimate, which can be obtained from the OLS regression  $\tilde{\boldsymbol{u}}_i^2 - 1$  on  $\hat{\boldsymbol{m}}_i$ , where the  $\tilde{\boldsymbol{u}}_i$  are residuals  $\hat{\boldsymbol{u}}_i$  weighted by  $\hat{\boldsymbol{m}}_i^{-1/2}$ . The resulting two-step estimator of  $\boldsymbol{\beta}$  is consistent under assumption (19.7) only, so it is just as robust as the Poisson QMLE. It makes sense to use fully robust standard errors and test statistics. If assumption (19.3) holds, the Poisson QMLE is asymptotically more efficient; if assumption (19.28) holds, the two-step negative binomial estimator is more efficient. Notice that neither variance assumption contains the other as a special case for all parameter values; see Wooldridge (1997c) for additional discussion.

The variance specification tests discussed in Section 19.2.5 can be extended to the negative binomial QMLE; see Wooldridge (1991b).