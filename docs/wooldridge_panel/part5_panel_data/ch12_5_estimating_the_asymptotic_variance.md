# Estimating the Asymptotic Variance

> Pages: 367-372

#### 12.5.1 Estimation without Nuisance Parameters

We first consider estimating the asymptotic variance of  $\hat{\boldsymbol{\theta}}$  in the case where there are no nuisance parameters. This task requires consistently estimating the matrices  $\mathbf{A}_o$  and  $\mathbf{B}_o$ . One thought is to solve for the expected values of  $\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_o)$  and  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_o) \cdot \mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_o)'$  over the distribution of  $\mathbf{w}$ , and then to plug in  $\hat{\boldsymbol{\theta}}$  for  $\boldsymbol{\theta}_o$ . When we have completely specified the distribution of  $\mathbf{w}$ , obtaining closed-form expressions for  $\mathbf{A}_o$  and  $\mathbf{B}_o$  is, in principle, possible. However, except in simple cases, it would be difficult. More importantly, we rarely specify the entire distribution of  $\mathbf{w}$ . Even in a maximum

{368}------------------------------------------------

likelihood setting,  $\mathbf{w}$  is almost always partitioned into two parts: a set of endogenous variables,  $\mathbf{y}$ , and conditioning variables,  $\mathbf{x}$ . Rarely do we wish to specify the distribution of  $\mathbf{x}$ , and so the expected values needed to obtain  $\mathbf{A}_0$  and  $\mathbf{B}_0$  are not available.

We can always estimate  $A_o$  consistently by taking away the expectation and replacing  $\theta_o$  with  $\hat{\theta}$ . Under regularity conditions that ensure uniform converge of the Hessian, the estimator

$$N^{-1} \sum_{i=1}^{N} \mathbf{H}(\mathbf{w}_i, \hat{\boldsymbol{\theta}}) \equiv N^{-1} \sum_{i=1}^{N} \hat{\mathbf{H}}_i$$
 (12.42)

is consistent for  $A_o$ , by Lemma 12.1. The advantage of the estimator (12.42) is that it is always available in problems with a twice continuously differentiable objective function. The drawbacks are that it requires calculation of the second derivatives—a nontrivial task for some problems—and it is not guaranteed to be positive definite, or even positive semidefinite, for the particular sample we are working with. As we will see shortly, in some cases the asymptotic variance of  $\sqrt{N}(\hat{\theta} - \theta_o)$  is proportional to  $A_o^{-1}$ , in which case using the estimator (12.42) to estimate  $A_o$  can result in a nonpositive definite variance matrix estimator. Without a positive definite variance matrix estimator, some asymptotic standard errors need not even be defined, and test statistics that have limiting chi-square distributions could actually be negative.

In most econometric applications, more structure is available that allows a different estimator. Suppose we can partition  $\mathbf{w}$  into  $\mathbf{x}$  and  $\mathbf{y}$ , and that  $\boldsymbol{\theta}_0$  indexes some feature of the distribution of  $\mathbf{y}$  given  $\mathbf{x}$  (such as the conditional mean or, in the case of maximum likelihood, the conditional distribution). Define

$$\mathbf{A}(\mathbf{x}, \boldsymbol{\theta}_{o}) \equiv \mathbf{E}[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_{o}) \,|\, \mathbf{x}] \tag{12.43}$$

While  $\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_{o})$  is generally a function of  $\mathbf{x}$  and  $\mathbf{y}$ ,  $\mathbf{A}(\mathbf{x}, \boldsymbol{\theta}_{o})$  is a function only of  $\mathbf{x}$ . By the law of iterated expectations,  $\mathrm{E}[\mathbf{A}(\mathbf{x}, \boldsymbol{\theta}_{o})] = \mathrm{E}[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_{o})] = \mathbf{A}_{o}$ . From Lemma 12.1 and standard regularity conditions it follows that

$$N^{-1} \sum_{i=1}^{N} \mathbf{A}(\mathbf{x}_i, \hat{\boldsymbol{\theta}}) \equiv N^{-1} \sum_{i=1}^{N} \hat{\mathbf{A}}_i \stackrel{p}{\to} \mathbf{A}_o$$
 (12.44)

The estimator (12.44) of  $\mathbf{A}_o$  is useful in cases where  $\mathrm{E}[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_o) \,|\, \mathbf{x}]$  can be obtained in closed form or is easily approximated. In some leading cases, including NLS and certain maximum likelihood problems,  $\mathbf{A}(\mathbf{x}, \boldsymbol{\theta}_o)$  depends only on the first derivatives of the conditional mean function.

When the estimator (12.44) is available, it is usually the case that  $\theta_0$  actually minimizes  $E[q(\mathbf{w}, \theta) | \mathbf{x}]$  for any value of  $\mathbf{x}$ ; this is easily seen to be the case for NLS from

{369}------------------------------------------------

equation (12.4). Under assumptions that allow the interchange of derivative and expectation, this result implies that  $\mathbf{A}(\mathbf{x}, \boldsymbol{\theta}_0)$  is positive semidefinite. The expected value of  $\mathbf{A}(\mathbf{x}, \boldsymbol{\theta}_0)$  over the distribution of  $\mathbf{x}$  is positive definite provided  $\boldsymbol{\theta}_0$  is identified. Therefore, the estimator (12.44) is usually positive definite in the sample; as a result, it is more attractive than the estimator (12.42).

Obtaining a positive semidefinite estimator of  $\mathbf{B}_0$  is straightforward. By Lemma 12.1, under standard regularity conditions we have

$$N^{-1} \sum_{i=1}^{N} \mathbf{s}(\mathbf{w}_{i}, \hat{\boldsymbol{\theta}}) \mathbf{s}(\mathbf{w}_{i}, \hat{\boldsymbol{\theta}})' \equiv N^{-1} \sum_{i=1}^{N} \hat{\mathbf{s}}_{i} \hat{\mathbf{s}}_{i}' \stackrel{p}{\to} \mathbf{B}_{o}$$

$$(12.45)$$

Combining the estimator (12.45) with the consistent estimators for  $\mathbf{A}_o$ , we can consistently estimate Avar  $\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_o)$  by

$$\operatorname{Avar}\sqrt{N}(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o}) = \hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1} \tag{12.46}$$

where  $\hat{\mathbf{A}}$  is one of the estimators (12.42) or (12.44). The asymptotic standard errors are obtained from the matrix

$$\hat{\mathbf{V}} \equiv \text{Avar}(\hat{\boldsymbol{\theta}}) = \hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1}/N \tag{12.47}$$

which can be expressed as

$$\left(\sum_{i=1}^{N} \hat{\mathbf{H}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \hat{\mathbf{s}}_{i} \hat{\mathbf{s}}_{i}'\right) \left(\sum_{i=1}^{N} \hat{\mathbf{H}}_{i}\right)^{-1}$$

$$(12.48)$$

or

$$\left(\sum_{i=1}^{N} \hat{\mathbf{A}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \hat{\mathbf{s}}_{i} \hat{\mathbf{s}}_{i}'\right) \left(\sum_{i=1}^{N} \hat{\mathbf{A}}_{i}\right)^{-1}$$

$$(12.49)$$

depending on the estimator used for  $A_o$ . Expressions (12.48) and (12.49) are both at least positive semidefinite when they are well defined.

In the case of nonlinear least squares, the estimator of  $A_0$  in equation (12.44) is always available and always used:

$$\sum_{i=1}^{N} \hat{\mathbf{A}}_i = \sum_{i=1}^{N} 
abla_{ heta} \hat{m}_i' 
abla_{ heta} \hat{m}_i$$

where  $\nabla_{\theta} \hat{m}_i \equiv \nabla_{\theta} m(\mathbf{x}_i, \hat{\boldsymbol{\theta}})$  for every observation *i*. Also, the estimated score for NLS can be written as

{370}------------------------------------------------

$$\hat{\mathbf{s}}_i = -\nabla_\theta \hat{\mathbf{m}}_i'[y_i - m(\mathbf{x}_i, \hat{\boldsymbol{\theta}})] = -\nabla_\theta \hat{\mathbf{m}}_i' \hat{\boldsymbol{u}}_i \tag{12.50}$$

where the **nonlinear least squares residuals**,  $\hat{u}_i$ , are defined as

$$\hat{\boldsymbol{u}}_i \equiv y_i - m(\mathbf{x}_i, \hat{\boldsymbol{\theta}}) \tag{12.51}$$

The estimated asymptotic variance of the NLS estimator is

$$\operatorname{Avar}(\hat{\boldsymbol{\theta}}) = \left(\sum_{i=1}^{N} \nabla_{\theta} \hat{\boldsymbol{m}}_{i}' \nabla_{\theta} \hat{\boldsymbol{m}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \hat{\boldsymbol{u}}_{i}^{2} \nabla_{\theta} \hat{\boldsymbol{m}}_{i}' \nabla_{\theta} \hat{\boldsymbol{m}}_{i}\right) \left(\sum_{i=1}^{N} \nabla_{\theta} \hat{\boldsymbol{m}}_{i}' \nabla_{\theta} \hat{\boldsymbol{m}}_{i}\right)^{-1}$$
(12.52)

This is called the **heteroskedasticity-robust variance matrix estimator for NLS** because it places no restrictions on  $Var(y | \mathbf{x})$ . It was first proposed by White (1980a). [Sometimes the expression is multiplied by N/(N-P) as a degrees-of-freedom adjustment, where P is the dimension of  $\theta$ .] As always, the asymptotic standard error of each element of  $\hat{\theta}$  is the square root of the appropriate diagonal element of matrix (12.52).

As a specific example, suppose that  $m(\mathbf{x}, \boldsymbol{\theta}) = \exp(\mathbf{x}\boldsymbol{\theta})$ . Then  $\nabla_{\theta}\hat{m}_{i}'\nabla_{\theta}\hat{m}_{i} = \exp(2\mathbf{x}_{i}\hat{\boldsymbol{\theta}})\mathbf{x}_{i}'\mathbf{x}_{i}$ , which has dimension  $K \times K$ . We can plug this equation into expression (12.52) along with  $\hat{u}_{i} = y_{i} - \exp(\mathbf{x}_{i}\hat{\boldsymbol{\theta}})$ .

In many contexts, including nonlinear least squares and certain quasi-likelihood methods, the asymptotic variance estimator can be simplified under additional assumptions. For our purposes, we state the assumption as follows: For some  $\sigma_0^2 > 0$ ,

$$E[\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})'] = \sigma_{o}^{2}E[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_{o})]$$
(12.53)

This assumption simply says that the expected outer product of the score, evaluated at  $\theta_o$ , is proportional to the expected value of the Hessian (evaluated at  $\theta_o$ ):  $\mathbf{B}_o = \sigma_o^2 \mathbf{A}_o$ . Shortly we will provide an assumption under which assumption (12.53) holds for NLS. In the next chapter we will show that assumption (12.53) holds for  $\sigma_o^2 = 1$  in the context of maximum likelihood with a correctly specified conditional density. For reasons we will see in Chapter 13, we refer to assumption (12.53) as the **generalized information matrix equality (GIME)**.

LEMMA 12.2: Under regularity conditions of the type contained in Theorem 12.3 and assumption (12.53),  $\operatorname{Avar}(\hat{\boldsymbol{\theta}}) = \sigma_{\rm o}^2 \mathbf{A}_{\rm o}^{-1}/N$ . Therefore, under assumption (12.53), the asymptotic variance of  $\hat{\boldsymbol{\theta}}$  can be estimated as

$$\hat{\mathbf{V}} = \hat{\boldsymbol{\sigma}}^2 \left( \sum_{i=1}^N \hat{\mathbf{H}}_i \right)^{-1} \tag{12.54}$$


{371}------------------------------------------------

or

$$\hat{\mathbf{V}} = \hat{\boldsymbol{\sigma}}^2 \left( \sum_{i=1}^N \hat{\mathbf{A}}_i \right)^{-1} \tag{12.55}$$

where  $\hat{\mathbf{H}}_i$  and  $\hat{\mathbf{A}}_i$  are defined as before, and  $\hat{\sigma}^2 \stackrel{p}{\rightarrow} \sigma_0^2$ .

In the case of nonlinear regression, the parameter  $\sigma_0^2$  is the variance of y given x, or equivalently  $Var(u \mid x)$ , under homoskedasticity:

ASSUMPTION NLS.3: 
$$Var(y | \mathbf{x}) = Var(u | \mathbf{x}) = \sigma_o^2$$
.

Under Assumption NLS.3, we can show that assumption (12.53) holds with  $\sigma_0^2 = \text{Var}(y \mid \mathbf{x})$ . First, since  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_0) \mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_0)' = u^2 \nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}_0)' \nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}_0)$ , it follows that

$$E[\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})' | \mathbf{x}] = E(u^{2} | \mathbf{x})\nabla_{\theta}m(\mathbf{x}, \boldsymbol{\theta}_{o})'\nabla_{\theta}m(\mathbf{x}, \boldsymbol{\theta}_{o})$$

$$= \sigma_{o}^{2}\nabla_{\theta}m(\mathbf{x}, \boldsymbol{\theta}_{o})'\nabla_{\theta}m(\mathbf{x}, \boldsymbol{\theta}_{o})$$
(12.56)

under Assumptions NLS.1 and NLS.3. Taking the expected value with respect to  $\mathbf{x}$  gives equation (12.53).

Under Assumption NLS.3, a simplified estimator of the asymptotic variance of the NLS estimator exists from equation (12.55). Let

$$\hat{\sigma}^2 = \frac{1}{(N-P)} \sum_{i=1}^{N} \hat{u}_i^2 = SSR/(N-P)$$
 (12.57)

where the  $\hat{u}_i$  are the NLS residuals (12.51) and SSR is the sum of squared NLS residuals. Using Lemma 12.1,  $\hat{\sigma}^2$  can be shown to be consistent very generally. The subtraction of P in the denominator of equation (12.57) is an adjustment that is thought to improve the small sample properties of  $\hat{\sigma}^2$ .

Under Assumptions NLS.1-NLS.3, the asymptotic variance of the NLS estimator is estimated as

$$\hat{\sigma}^2 \left( \sum_{i=1}^N \nabla_{\theta} \hat{\boldsymbol{m}}_i' \nabla_{\theta} \hat{\boldsymbol{m}}_i \right)^{-1} \tag{12.58}$$

This is the default asymptotic variance estimator for NLS, but it is valid only under homoskedasticity; the estimator (12.52) is valid with or without Assumption NLS.3. For an exponential regression function, expression (12.58) becomes  $\hat{\sigma}^2(\sum_{i=1}^N \exp(2\mathbf{x}_i\hat{\boldsymbol{\theta}})\mathbf{x}_i'\mathbf{x}_i)^{-1}$ .

{372}------------------------------------------------