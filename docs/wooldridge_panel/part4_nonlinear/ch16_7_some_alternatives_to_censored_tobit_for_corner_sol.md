# Some Alternatives to Censored Tobit for Corner Solution Outcomes

> Pages: 545-547

In corner solution applications, an important limitation of the standard Tobit model is that a single mechanism determines the choice between y ¼ 0 versus y > 0 and the amount of y given y > 0. In particular, qPðy > 0 j xÞ=qxj and qEðy j x; y > 0Þ=qxj have the same sign. In fact, in Section 16.2 we showed that the relative effects of continuous explanatory variables on Pðy > 0 j xÞ and Eðy j x; y > 0Þ are identical. Alternatives to censored Tobit have been suggested to allow the initial decision of y > 0 versus y ¼ 0 to be separate from the decision of how much y given that y > 0. These are often called hurdle models or two-tiered models. The hurdle or first tier is whether or not to choose positive y. For example, in the charitable contributions example, family characteristics may differently affect the decision to contribute at all and the decision on how much to contribute.

A simple two-tiered model for a corner solution variable is

$$\mathbf{P}(y=0\,|\,\mathbf{x}) = 1 - \Phi(\mathbf{x}\gamma) \tag{16.37}$$

$$\log(y) \mid (\mathbf{x}, y > 0) \sim \text{Normal}(\mathbf{x}\boldsymbol{\beta}, \sigma^2)$$
 (16.38)

{546}------------------------------------------------

The first equation dictates the probability that y is zero or positive, and equation (16.38) says that, conditional on y > 0,  $y \mid \mathbf{x}$  follows a *lognormal distribution*. If we define w = 1[y > 0] and use

$$f(y | \mathbf{x}) = \mathbf{P}(w = 0 | \mathbf{x}) f(y | \mathbf{x}, w = 0) + \mathbf{P}(w = 1 | \mathbf{x}) f(y | \mathbf{x}, w = 1)$$

we obtain

$$f(y | \mathbf{x}) = 1[y = 0][1 - \Phi(\mathbf{x}y)] + 1[y > 0]\Phi(\mathbf{x}y)\phi[\{\log(y) - \mathbf{x}\beta\}/\sigma]/(y\sigma)$$

since  $P[y > 0 | \mathbf{x}] = \Phi(\mathbf{x}y)$  and  $\phi[\{\log(y) - \mathbf{x}\boldsymbol{\beta}\}/\sigma]/(y\sigma)$  is the density of a lognormal random variable. For maximum likelihood analysis, a better way to write the density is

$$f(y \mid \mathbf{x}; \boldsymbol{\theta}) = [1 - \Phi(\mathbf{x}\boldsymbol{\gamma})]^{1[y=0]} \{\Phi(\mathbf{x}\boldsymbol{\gamma})\phi[\{\log(y) - \mathbf{x}\boldsymbol{\beta}\}/\sigma]/(y\sigma)\}^{1[y>0]}$$

for  $y \ge 0$ . If there are no restrictions on  $\gamma$ ,  $\beta$ , and  $\sigma^2$ , then the MLEs are easy to obtain: the log-likelihood function for observation i is

$$\ell_i(\boldsymbol{\theta}) = 1[y_i = 0] \log[1 - \Phi(\mathbf{x}\boldsymbol{\gamma})] + 1[y_i > 0] \{\log \Phi(\mathbf{x}_i\boldsymbol{\gamma}) - \log(y_i) - \frac{1}{2}\log(\sigma^2) - \frac{1}{2}\log(2\pi) - \frac{1}{2}[\log(y_i) - \mathbf{x}_i\boldsymbol{\beta}]^2/\sigma^2\}$$

The MLE of  $\gamma$  is simply the probit estimator using w = 1[y > 0] as the binary response. The MLE of  $\beta$  is just the OLS estimator from the regression  $\log(y)$  on  $\mathbf{x}$  using those observations for which y > 0. A consistent estimator of  $\hat{\sigma}$  is the usual standard error from this regression. Estimation is very simple because we *assume* that, conditional on y > 0,  $\log(y)$  follows a classical linear model. The expectations  $\mathrm{E}(y|\mathbf{x},y>0)$  and  $\mathrm{E}(y|\mathbf{x})$  are easy to obtain using properties of the lognormal distribution:

$$E(y | \mathbf{x}, y > 0) = \exp(\mathbf{x}\boldsymbol{\beta} + \sigma^2/2), \qquad E(y | \mathbf{x}) = \Phi(\mathbf{x}\boldsymbol{\gamma}) \exp(\mathbf{x}\boldsymbol{\beta} + \sigma^2/2)$$

and these are easily estimated given  $\hat{\beta}$ ,  $\hat{\sigma}^2$ , and  $\hat{\gamma}$ .

We cannot obtain the Tobit model as a special case of the model (16.37) and (16.38) by imposing parameter restrictions, and this inability makes it difficult to test the Tobit model against equations (16.37) and (16.38). Vuong (1989) suggests a general *model selection test* that can be applied to choose the best-fitting model when the models are nonnested. Essentially, Vuong shows how to test whether one log-likelihood value is significantly greater than another, where the null is that they have the same expected value.

Cragg (1971) suggests a different two-tiered model which, unlike equations (16.37) and (16.38), nests the usual Tobit model. Cragg uses the truncated normal distribution in place of the lognormal distribution:

{547}------------------------------------------------

$$f(y \mid \mathbf{x}, y > 0) = [\Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)]^{-1} \{ \phi[(y - \mathbf{x}\boldsymbol{\beta})/\sigma]/\sigma \}, \qquad y > 0$$

where the term ½Fðx*b*=sÞ<sup>1</sup> ensures that the density integrates to unity over y > 0. The density of y given x becomes

$$f(y \mid \mathbf{x}; \boldsymbol{\theta}) = [1 - \Phi(\mathbf{x}\boldsymbol{\gamma})]^{1[y=0]} \{ \Phi(\mathbf{x}\boldsymbol{\gamma}) [\Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)]^{-1} [\phi(\{y - \mathbf{x}\boldsymbol{\beta}\}/\sigma)/\sigma] \}^{1[y>0]}$$

This equation is easily seen to yield the standard censored Tobit density when *g* ¼ *b*=s. Fin and Schmidt (1984) derive the LM test of this restriction, which allows the Tobit model to be tested against Cragg's more general alternative. Problem 16.7 asks you to derive the conditional expectations associated with Cragg's model. It is legitimate to choose between Cragg's model and the lognormal model in equation (16.38) by using the value of the log-likelihood function. Vuong's (1989) approach can be used to determine whether the difference in log likelihoods is statistically significant.

If we are interested primarily in Eðy j xÞ, then we can model Eðy j xÞ directly and use a least squares approach. We discussed the drawbacks of using linear regression methods in Section 16.1. Nevertheless, a linear model for Eðy j xÞ might give good estimates on the partial effects for x near its mean value.

In Section 16.1 we also mentioned the possibility of modeling Eðy j xÞ as an exponential function and using NLS or a quasi-MLE procedure (see Chapter 19) without any further assumptions about the distribution of y given x. If a model for Pðy ¼ 0 j xÞ is added, then we can obtain Eðy j x; y > 0Þ ¼ expðx*b*Þ=½1 Pðy ¼ 0 j xÞ. Such methods are not common in applications, but this neglect could be partly due to confusion about which quantities are of interest for corner solution outcomes.

# 16.8 Applying Censored Regression to Panel Data and Cluster Samples

We now cover Tobit methods for panel data and cluster samples. The treatment is very similar to that for probit models in Section 15.8, and so we make it brief.