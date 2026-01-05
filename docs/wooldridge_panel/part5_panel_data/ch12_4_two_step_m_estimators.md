# Two-Step M-Estimators

> Pages: 364

Sometimes applications of M-estimators involve a first-stage estimation (an example is OLS with generated regressors, as in Chapter 6). Let  $\hat{\gamma}$  be a preliminary estimator, usually based on the random sample  $\{\mathbf{w}_i: i=1,2,\ldots,N\}$ . Where this estimator comes from must be vague at this point.

A two-step M-estimator  $\hat{\theta}$  of  $\theta_0$  solves the problem

$$\min_{\boldsymbol{\theta} \in \mathbf{\Theta}} \sum_{i=1}^{N} q(\mathbf{w}_i, \boldsymbol{\theta}; \hat{\boldsymbol{\gamma}})$$
 (12.31)

where q is now defined on  $\mathcal{W} \times \Theta \times \Gamma$ , and  $\Gamma$  is a subset of  $\mathbb{R}^J$ . We will see several examples of two-step M-estimators in the applications in Part IV. An example of a two-step M-estimator is the **weighted nonlinear least squares (WNLS) estimator**, where the weights are estimated in a first stage. The WNLS estimator solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \frac{1}{2} \sum_{i=1}^{N} [y_i - m(\mathbf{x}_i, \boldsymbol{\theta})]^2 / h(\mathbf{x}_i, \hat{\boldsymbol{\gamma}})$$
(12.32)

where the weighting function,  $h(\mathbf{x}, \gamma)$ , depends on the explanatory variables and a parameter vector. As with NLS,  $m(\mathbf{x}, \theta)$  is a model of  $E(y | \mathbf{x})$ . The function  $h(\mathbf{x}, \gamma)$  is chosen to be a model of  $Var(y | \mathbf{x})$ . The estimator  $\hat{y}$  comes from a problem used to estimate the conditional variance. We list the key assumptions needed for WNLS to have desirable properties here, but several of the derivations are left for the problems.

ASSUMPTION WNLS.1: Same as Assumption NLS.1.