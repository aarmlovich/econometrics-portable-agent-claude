# Binomial Regression Models

> Pages: 666-668

Sometimes we wish to analyze count data conditional on a known upper bound. For example, Thomas, Strauss, and Henriques (1990) study child mortality within families conditional on number of children ever born. Another example takes the dependent variable,  $y_i$ , to be the number of adult children in family i who are high school graduates; the known upper bound,  $n_i$ , is the number of children in family i. By conditioning on  $n_i$  we are, presumably, treating it as exogenous.

Let  $\mathbf{x}_i$  be a set of exogenous variables. A natural starting point is to assume that  $y_i$  given  $(n_i, \mathbf{x}_i)$  has a binomial distribution, denoted Binomial  $[n_i, p(\mathbf{x}_i, \boldsymbol{\beta})]$ , where  $p(\mathbf{x}_i, \boldsymbol{\beta})$  is a function bounded between zero and one. Usually,  $y_i$  is viewed as the sum of  $n_i$  independent Bernoulli (zero-one) random variables, and  $p(\mathbf{x}_i, \boldsymbol{\beta})$  is the (conditional) probability of success on each trial.

The binomial assumption is too restrictive for all applications. The presence of an unobserved effect would invalidate the binomial assumption (after the effect is integrated out). For example, when  $y_i$  is the number of children in a family graduating from high school, unobserved family effects may play an important role.

{667}------------------------------------------------

As in the case of unbounded support, we assume that the conditional mean is correctly specified:

$$E(y_i | \mathbf{x}_i, n_i) = n_i p(\mathbf{x}_i, \boldsymbol{\beta}) \equiv m_i(\boldsymbol{\beta})$$
(19.32)

This formulation ensures that  $E(y_i | \mathbf{x}_i, n_i)$  is between zero and  $n_i$ . Typically,  $p(\mathbf{x}_i, \boldsymbol{\beta}) = G(\mathbf{x}_i \boldsymbol{\beta})$ , where  $G(\cdot)$  is a cumulative distribution function, such as the standard normal or logistic function.

Given a parametric model  $p(\mathbf{x}, \boldsymbol{\beta})$ , the binomial quasi-log likelihood for observation i is

$$\ell_i(\boldsymbol{\beta}) = y_i \log[p(\mathbf{x}_i, \boldsymbol{\beta})] + (n_i - y_i) \log[1 - p(\mathbf{x}_i, \boldsymbol{\beta})]$$
(19.33)

and the binomial QMLE is obtained by maximizing the sum of  $\ell_i(\beta)$  over all N observations. From the results of GMT (1984a), the conditional mean parameters are consistently estimated under assumption (19.32) only. This conclusion follows from the general M-estimation results after showing that the true value of  $\beta$  maximizes the expected value of equation (19.33) under assumption (19.32) only.

The binomial GLM variance assumption is

$$\operatorname{Var}(y_i | \mathbf{x}_i, n_i) = \sigma^2 n_i p(\mathbf{x}_i, \boldsymbol{\beta}) [1 - p(\mathbf{x}_i, \boldsymbol{\beta})] = \sigma^2 v_i(\boldsymbol{\beta})$$
(19.34)

which generalizes the nominal binomial assumption with  $\sigma^2 = 1$ . [McCullagh and Nelder (1989, Section 4.5) discuss a model that leads to assumption (19.34) with  $\sigma^2 > 1$ . But underdispersion is also possible.] Even the GLM assumption can fail if the binary outcomes comprising  $y_i$  are not independent conditional on  $(\mathbf{x}_i, n_i)$ . Therefore, it makes sense to use the fully robust asymptotic variance estimator for the binomial OMLE.

Owing to the structure of LEF densities, and given our earlier analysis of the Poisson and negative binomial cases, it is straightforward to describe the econometric analysis for the binomial QMLE: simply take  $\hat{m}_i \equiv n_i p(\mathbf{x}_i, \hat{\boldsymbol{\beta}})$ ,  $\hat{u}_i \equiv y_i - \hat{m}_i$ ,  $\nabla_{\beta} \hat{m}_i \equiv n_i \nabla_{\beta} \hat{p}_i$ , and  $\hat{v}_i \equiv n_i \hat{p}_i (1 - \hat{p}_i)$  in equations (19.31). An estimator of  $\sigma^2$  under assumption (19.34) is also easily obtained: replace  $\hat{m}_i$  in equation (19.15) with  $\hat{v}_i$ . The structure of asymptotic variances and score tests is identical.

# 19.4 Other QMLES in the Linear Exponential Family

Sometimes we want to use a quasi-MLE analysis for other kinds of response variables. We will consider two here. The **exponential regression model** is well suited to strictly positive, roughly continuous responses. **Fractional logit regression** can be used when the response variable takes on values in the unit interval.

{668}------------------------------------------------

#### **19.4.1 Exponential Regression Models**

Just as in the Poisson regression model, in an exponential regression model we specify a conditional mean function,  $m(\mathbf{x}, \boldsymbol{\beta})$ . However, we now use the exponential quasilog likelihood function,  $\ell_i(\boldsymbol{\beta}) = -y_i/m(\mathbf{x}_i, \boldsymbol{\beta}) - \log[m(\mathbf{x}_i, \boldsymbol{\beta})]$ . [The "exponential" in "exponential regression model" refers to the quasi-likelihood used, and not to the mean function  $m(\mathbf{x}, \boldsymbol{\beta})$ .] The most popular choice of  $m(\mathbf{x}, \boldsymbol{\beta})$  happens to be  $\exp(\mathbf{x}\boldsymbol{\beta})$ .

The results of GMT (1984a) imply that, provided the conditional mean is correctly specified, the exponential QMLE consistently estimates the conditional mean parameters. Thus the exponential QMLE enjoys the same robustness properties as the Poisson QMLE.

The GLM variance assumption for exponential regression is

$$Var(y \mid \mathbf{x}) = \sigma^2 [E(y \mid \mathbf{x})]^2$$
(19.35)

When  $\sigma^2 = 1$ , assumption (19.35) gives the variance-mean relationship for the exponential distribution. Under assumption (19.35),  $\sigma$  is the **coefficient of variation**: it is the ratio of the conditional standard deviation of y to its conditional mean.

Whether or not assumption (19.35) holds, an asymptotic variance matrix can be estimated. The fully robust form is expression (19.14), but, in defining the score and expected Hessian, the residuals and gradients are weighted by  $1/\hat{m}_i$  rather than  $\hat{m}_i^{-1/2}$ . Under assumption (19.35), a valid estimator is

$$\hat{\boldsymbol{\sigma}}^2 \left( \sum_{i=1}^N \nabla_{\!\beta} \hat{\boldsymbol{m}}_i' \nabla_{\!\beta} \hat{\boldsymbol{m}}_i / \hat{\boldsymbol{v}}_i \right)^{-1}$$

where  $\hat{\sigma}^2 = N^{-1} \sum_{i=1}^N \hat{u}_i^2 / \hat{m}_i^2$  and  $\hat{v}_i = \hat{m}_i^2$ . Score tests and quasi-likelihood ratio tests can be computed just as in the Poisson case. Most statistical packages implement exponential regression with an exponential mean function; it is sometimes called the **gamma regression model** because the exponential distribution is a special case of the gamma distribution.