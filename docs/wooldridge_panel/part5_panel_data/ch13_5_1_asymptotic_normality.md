# Asymptotic Normality

> Pages: 403-408

We can derive the limiting distribution of the MLE by applying Theorem 12.3. We will have to assume the regularity conditions there; in particular, we assume that  $\theta_0$  is in the interior of  $\Theta$ , and  $\ell_i(\theta)$  is twice continuously differentiable on the interior of  $\Theta$ .

The score of the  $\log$  likelihood for observation i is simply

$$\mathbf{s}_{i}(\boldsymbol{\theta}) \equiv \nabla_{\boldsymbol{\theta}} \ell_{i}(\boldsymbol{\theta})' = \left(\frac{\partial \ell_{i}}{\partial \theta_{1}}(\boldsymbol{\theta}), \frac{\partial \ell_{i}}{\partial \theta_{2}}(\boldsymbol{\theta}), \dots, \frac{\partial \ell_{i}}{\partial \theta_{P}}(\boldsymbol{\theta})\right)'$$
(13.17)

a  $P \times 1$  vector as in Chapter 12.

Example 13.1 (continued): For the probit case,  $\theta$  is  $K \times 1$  and

$$\nabla_{\theta} \ell_i(\boldsymbol{\theta}) = y_i \left[ \frac{\phi(\mathbf{x}_i \boldsymbol{\theta}) \mathbf{x}_i}{\Phi(\mathbf{x}_i \boldsymbol{\theta})} \right] - (1 - y_i) \left\{ \frac{\phi(\mathbf{x}_i \boldsymbol{\theta}) \mathbf{x}_i}{[1 - \Phi(\mathbf{x}_i \boldsymbol{\theta})]} \right\}$$

Transposing this equation, and using a little algebra, gives

{404}------------------------------------------------

$$\mathbf{s}_{i}(\boldsymbol{\theta}) = \frac{\phi(\mathbf{x}_{i}\boldsymbol{\theta})\mathbf{x}_{i}^{\prime}[y_{i} - \Phi(\mathbf{x}_{i}\boldsymbol{\theta})]}{\Phi(\mathbf{x}_{i}\boldsymbol{\theta})[1 - \Phi(\mathbf{x}_{i}\boldsymbol{\theta})]}$$
(13.18)

Recall that  $\mathbf{x}'_i$  is a  $K \times 1$  vector.

Example 13.2 (continued): The score for the Poisson case, where  $\theta$  is again  $K \times 1$ , is

$$\mathbf{s}_{i}(\boldsymbol{\theta}) = -\exp(\mathbf{x}_{i}\boldsymbol{\theta})\mathbf{x}_{i}' + y_{i}\mathbf{x}_{i}' = \mathbf{x}_{i}'[y_{i} - \exp(\mathbf{x}_{i}\boldsymbol{\theta})]$$
(13.19)

In the vast majority of cases, the score of the log-likelihood function has an important zero conditional mean property:

$$\mathbf{E}[\mathbf{s}_i(\boldsymbol{\theta}_0) \mid \mathbf{x}_i] = \mathbf{0} \tag{13.20}$$

In other words, when we evaluate the  $P \times 1$  score at  $\theta_0$ , and take its expectation with respect to  $f(\cdot | \mathbf{x}_i; \theta_0)$ , the expectation is zero. Under condition (13.20),  $\mathrm{E}[\mathbf{s}_i(\theta_0)] = \mathbf{0}$ , which was a key condition in deriving the asymptotic normality of the M-estimator in Chapter 12.

To show condition (13.20) generally, let  $E_{\theta}[\cdot | \mathbf{x}_i]$  denote conditional expectation with respect to the density  $f(\cdot | \mathbf{x}_i; \boldsymbol{\theta})$  for any  $\boldsymbol{\theta} \in \boldsymbol{\Theta}$ . Then, by definition,

$$E_{\theta}[\mathbf{s}_{i}(\boldsymbol{\theta}) | \mathbf{x}_{i}] = \int_{\mathcal{A}} \mathbf{s}(\mathbf{y}, \mathbf{x}_{i}, \boldsymbol{\theta}) f(\mathbf{y} | \mathbf{x}_{i}; \boldsymbol{\theta}) \nu(d\mathbf{y})$$

If integration and differentation can be interchanged on  $int(\Theta)$ —that is, if

$$\nabla_{\theta} \left( \int_{\mathscr{Y}} f(\mathbf{y} \mid \mathbf{x}_i; \boldsymbol{\theta}) \nu(d\mathbf{y}) \right) = \int_{\mathscr{Y}} \nabla_{\theta} f(\mathbf{y} \mid \mathbf{x}_i; \boldsymbol{\theta}) \nu(d\mathbf{y})$$
(13.21)

for all  $\mathbf{x}_i \in \mathcal{X}$ ,  $\boldsymbol{\theta} \in \text{int}(\boldsymbol{\Theta})$ —then

$$\mathbf{0} = \int_{\mathcal{U}} \nabla_{\theta} f(\mathbf{y} \mid \mathbf{x}_i; \boldsymbol{\theta}) \nu(d\mathbf{y})$$
 (13.22)

since  $\int_{\mathscr{Y}} f(\mathbf{y} | \mathbf{x}_i; \boldsymbol{\theta}) v(d\mathbf{y})$  is unity for all  $\boldsymbol{\theta}$ , and therefore the partial derivatives with respect to  $\boldsymbol{\theta}$  must be identically zero. But the right-hand side of equation (13.22) can be written as  $\int_{\mathscr{Y}} [\nabla_{\boldsymbol{\theta}} \ell(\mathbf{y}, \mathbf{x}_i, \boldsymbol{\theta})] f(\mathbf{y} | \mathbf{x}_i; \boldsymbol{\theta}) v(d\mathbf{y})$ . Putting in  $\boldsymbol{\theta}_0$  for  $\boldsymbol{\theta}$  and transposing yields condition (13.20).

Example 13.1 (continued): Define  $u_i \equiv y_i - \Phi(\mathbf{x}_i \boldsymbol{\theta}_0) = y_i - \mathrm{E}(y_i | \mathbf{x}_i)$ . Then

$$\mathbf{s}_i(\boldsymbol{\theta}_{\text{o}}) = \frac{\phi(\mathbf{x}_i \boldsymbol{\theta}_{\text{o}}) \mathbf{x}_i' u_i}{\Phi(\mathbf{x}_i \boldsymbol{\theta}_{\text{o}}) [1 - \Phi(\mathbf{x}_i \boldsymbol{\theta}_{\text{o}})]}$$

and, since  $E(u_i | \mathbf{x}_i) = 0$ , it follows that  $E[\mathbf{s}_i(\boldsymbol{\theta}_0) | \mathbf{x}_i] = \mathbf{0}$ .

{405}------------------------------------------------

Example 13.2 (continued): Define  $u_i \equiv y_i - \exp(\mathbf{x}_i \boldsymbol{\theta}_0)$ . Then  $\mathbf{s}_i(\boldsymbol{\theta}_0) = \mathbf{x}_i' u_i$  and so  $\mathrm{E}[\mathbf{s}_i(\boldsymbol{\theta}_0) \mid \mathbf{x}_i] = \mathbf{0}$ .

Assuming that  $\ell_i(\theta)$  is twice continuously differentiable on the interior of  $\Theta$ , let the Hessian for observation i be the  $P \times P$  matrix of second partial derivatives of  $\ell_i(\theta)$ :

$$\mathbf{H}_{i}(\boldsymbol{\theta}) \equiv \nabla_{\theta} \mathbf{s}_{i}(\boldsymbol{\theta}) = \nabla_{\theta}^{2} \ell_{i}(\boldsymbol{\theta}) \tag{13.23}$$

The Hessian is a symmetric matrix that generally depends on  $(\mathbf{x}_i, \mathbf{y}_i)$ . Since MLE is a maximization problem, the expected value of  $\mathbf{H}_i(\boldsymbol{\theta}_o)$  is negative definite. Thus, to apply the theory in Chapter 12, we define

$$\mathbf{A}_{o} \equiv -\mathbf{E}[\mathbf{H}_{i}(\boldsymbol{\theta}_{o})] \tag{13.24}$$

which is generally a positive definite matrix when  $\theta_o$  is identified. Under standard regularity conditions, the asymptotic normality of the CMLE follows from Theorem 12.3:  $\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_o) \stackrel{a}{\sim} \text{Normal}(\mathbf{0}, \mathbf{A}_o^{-1}\mathbf{B}_o\mathbf{A}_o^{-1})$ , where  $\mathbf{B}_o \equiv \text{Var}[\mathbf{s}_i(\boldsymbol{\theta}_o)] \equiv \mathrm{E}[\mathbf{s}_i(\boldsymbol{\theta}_o)\mathbf{s}_i(\boldsymbol{\theta}_o)']$ . It turns out that this general form of the asymptotic variance matrix is too complicated. We now show that  $\mathbf{B}_o = \mathbf{A}_o$ .

We must assume enough smoothness such that the following interchange of integral and derivative is valid (see Newey and McFadden, 1994, Section 5.1, for the case of unconditional MLE):

$$\nabla_{\theta} \left( \int_{\mathcal{Y}} \mathbf{s}_{i}(\boldsymbol{\theta}) f(\mathbf{y} \mid \mathbf{x}_{i}; \boldsymbol{\theta}) \nu(d\mathbf{y}) \right) = \int_{\mathcal{Y}} \nabla_{\theta} [\mathbf{s}_{i}(\boldsymbol{\theta}) f(\mathbf{y} \mid \mathbf{x}_{i}; \boldsymbol{\theta})] \nu(d\mathbf{y})$$
(13.25)

Then, taking the derivative of the identity

$$\int_{\mathcal{Y}} \mathbf{s}_i(\boldsymbol{\theta}) f(\mathbf{y} \,|\, \mathbf{x}_i; \boldsymbol{\theta}) \nu(d\mathbf{y}) \equiv \mathbf{E}_{\boldsymbol{\theta}} [\mathbf{s}_i(\boldsymbol{\theta}) \,|\, \mathbf{x}_i] = \mathbf{0}, \qquad \boldsymbol{\theta} \in \mathrm{int}(\boldsymbol{\Theta})$$

and using equation (13.25), gives, for all  $\theta \in \text{int}(\Theta)$ ,

$$-\mathrm{E}_{\theta}[\mathbf{H}_{i}(\boldsymbol{\theta}) \,|\, \mathbf{x}_{i}] = \mathrm{Var}_{\theta}[\mathbf{s}_{i}(\boldsymbol{\theta}) \,|\, \mathbf{x}_{i}]$$

where the indexing by  $\theta$  denotes expectation and variance when  $f(\cdot | \mathbf{x}_i; \theta)$  is the density of  $\mathbf{y}_i$  given  $\mathbf{x}_i$ . When evaluated at  $\theta = \theta_0$  we get a very important equality:

$$-\mathbb{E}[\mathbf{H}_{i}(\boldsymbol{\theta}_{o}) \mid \mathbf{x}_{i}] = \mathbb{E}[\mathbf{s}_{i}(\boldsymbol{\theta}_{o})\mathbf{s}_{i}(\boldsymbol{\theta}_{o})' \mid \mathbf{x}_{i}]$$
(13.26)

where the expectation and variance are with respect to the true conditional distribution of  $\mathbf{y}_i$  given  $\mathbf{x}_i$ . Equation (13.26) is called the **conditional information matrix equality (CIME)**. Taking the expectation of equation (13.26) (with respect to the

{406}------------------------------------------------

distribution of  $\mathbf{x}_i$ ) and using the law of iterated expectations gives

$$-\mathrm{E}[\mathbf{H}_{i}(\boldsymbol{\theta}_{\mathrm{o}})] = \mathrm{E}[\mathbf{s}_{i}(\boldsymbol{\theta}_{\mathrm{o}})\mathbf{s}_{i}(\boldsymbol{\theta}_{\mathrm{o}})'] \tag{13.27}$$

or  $A_o = B_o$ . This relationship is best thought of as the unconditional information matrix equality (UIME).

THEOREM 13.2 (Asymptotic Normality of CMLE): Let the conditions of Theorem 13.1 hold. In addition, assume that (a)  $\theta_o \in \operatorname{int}(\Theta)$ ; (b) for each  $(\mathbf{y}, \mathbf{x}) \in \mathscr{Y} \times \mathscr{X}$ ,  $\ell(\mathbf{y}, \mathbf{x}, \cdot)$  is twice continuously differentiable on  $\operatorname{int}(\Theta)$ ; (c) the interchanges of derivative and integral in equations (13.21) and (13.25) hold for all  $\theta \in \operatorname{int}(\Theta)$ ; (d) the elements of  $\nabla_{\theta}^2 \ell(\mathbf{y}, \mathbf{x}, \theta)$  are bounded in absolute value by a function  $b(\mathbf{y}, \mathbf{x})$  with finite expectation; and (e)  $\mathbf{A}_o$  defined by expression (13.24) is positive definite. Then

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) \stackrel{d}{\to} \text{Normal}(\mathbf{0}, \mathbf{A}_{o}^{-1})$$
 (13.28)

and therefore

$$Avar(\hat{\boldsymbol{\theta}}) = \mathbf{A}_0^{-1}/N \tag{13.29}$$

In standard applications, the log likelihood has many continuous partial derivatives, although there are examples where it does not. Some examples also violate the interchange of the integral and derivative in equation (13.21) or (13.25), such as when the conditional support of  $\mathbf{y}_i$  depends on the parameters  $\boldsymbol{\theta}_0$ . In such cases we cannot expect the CMLE to have a limiting normal distribution; it may not even converge at the rate  $\sqrt{N}$ . Some progress has been made for specific models when the support of the distribution depends on unknown parameters; see, for example, Donald and Paarsch (1996).

# 13.5.2 Estimating the Asymptotic Variance

Estimating Avar( $\hat{\theta}$ ) requires estimating  $A_o$ . From the equalities derived previously, there are at least three possible estimators of  $A_o$  in the CMLE context. In fact, under slight extensions of the regularity conditions in Theorem 13.2, each of the matrices

$$N^{-1} \sum_{i=1}^{N} -\mathbf{H}_{i}(\hat{\boldsymbol{\theta}}), \qquad N^{-1} \sum_{i=1}^{N} \mathbf{s}_{i}(\hat{\boldsymbol{\theta}}) \mathbf{s}_{i}(\hat{\boldsymbol{\theta}})', \qquad \text{and} \qquad N^{-1} \sum_{i=1}^{N} \mathbf{A}(\mathbf{x}_{i}, \hat{\boldsymbol{\theta}})$$
(13.30)

converges to  $A_o = B_o$ , where

$$\mathbf{A}(\mathbf{x}_i, \boldsymbol{\theta}_0) \equiv -\mathbf{E}[\mathbf{H}(\mathbf{y}_i, \mathbf{x}_i, \boldsymbol{\theta}_0) \,|\, \mathbf{x}_i] \tag{13.31}$$

{407}------------------------------------------------

Thus,  $Avar(\hat{\theta})$  can be taken to be any of the three matrices

$$\left[ -\sum_{i=1}^{N} \mathbf{H}_{i}(\hat{\boldsymbol{\theta}}) \right]^{-1}, \qquad \left[ \sum_{i=1}^{N} \mathbf{s}_{i}(\hat{\boldsymbol{\theta}}) \mathbf{s}_{i}(\hat{\boldsymbol{\theta}})' \right]^{-1}, \qquad \text{or} \qquad \left[ \sum_{i=1}^{N} \mathbf{A}(\mathbf{x}_{i}, \hat{\boldsymbol{\theta}}) \right]^{-1}$$
(13.32)

and the asymptotic standard errors are the square roots of the diagonal elements of any of the matrices. We discussed each of these estimators in the general M-estimator case in Chapter 12, but a brief review is in order. The first estimator, based on the Hessian of the log likelihood, requires computing second derivatives and is not guaranteed to be positive definite. If the estimator is not positive definite, standard errors of some linear combinations of the parameters will not be well defined.

The second estimator in equation (13.32), based on the outer product of the score, is always positive definite (whenever the inverse exists). This simple estimator was proposed by Berndt, Hall, Hall, and Hausman (1974). Its primary drawback is that it can be poorly behaved in even moderate sample sizes, as we discussed in Section 12.6.2.

If the conditional expectation  $\mathbf{A}(\mathbf{x}_i, \boldsymbol{\theta}_0)$  is in closed form (as it is in some leading cases) or can be simulated—as discussed in Porter (1999)—then the estimator based on  $\mathbf{A}(\mathbf{x}_i, \hat{\boldsymbol{\theta}})$  has some attractive features. First, it often depends only on first derivatives of a conditional mean or conditional variance function. Second, it is positive definite when it exists because of the conditional information matrix equality (13.26). Third, this estimator has been found to have significantly better finite sample properties than the outer product of the score estimator in some situations where  $\mathbf{A}(\mathbf{x}_i, \boldsymbol{\theta}_0)$  can be obtained in closed form.

*Example 13.1 (continued):* The Hessian for the probit log-likelihood is a mess. Fortunately,  $E[\mathbf{H}_i(\boldsymbol{\theta}_0) | \mathbf{x}_i]$  has a fairly simple form. Taking the derivative of equation (13.18) and using the product rule gives

$$\mathbf{H}_{i}(\boldsymbol{\theta}) = -\frac{\{\phi(\mathbf{x}_{i}\boldsymbol{\theta})\}^{2}\mathbf{x}_{i}^{\prime}\mathbf{x}_{i}}{\Phi(\mathbf{x}_{i}\boldsymbol{\theta})[1 - \Phi(\mathbf{x}_{i}\boldsymbol{\theta})]} + [y_{i} - \Phi(\mathbf{x}_{i}\boldsymbol{\theta})]\mathbf{L}(\mathbf{x}_{i}\boldsymbol{\theta})$$

where  $\mathbf{L}(\mathbf{x}_i\boldsymbol{\theta})$  is a  $K \times K$  complicated function of  $\mathbf{x}_i\boldsymbol{\theta}$  that we need not find explicitly. Now, when we evaluate this expression at  $\boldsymbol{\theta}_0$  and note that  $E\{[y_i - \Phi(\mathbf{x}_i\boldsymbol{\theta}_0)]\mathbf{L}(\mathbf{x}_i\boldsymbol{\theta}_0) \mid \mathbf{x}_i\} = [E(y_i \mid \mathbf{x}_i) - \Phi(\mathbf{x}_i\boldsymbol{\theta}_0)]\mathbf{L}(\mathbf{x}_i\boldsymbol{\theta}_0) = \mathbf{0}$ , we have

$$-\mathrm{E}[\mathbf{H}_{i}(\boldsymbol{\theta}_{\mathrm{o}}) \mid \mathbf{x}_{i}] = \mathbf{A}_{i}(\boldsymbol{\theta}_{\mathrm{o}}) = \frac{\{\phi(\mathbf{x}_{i}\boldsymbol{\theta}_{\mathrm{o}})\}^{2} \mathbf{x}_{i}^{\prime} \mathbf{x}_{i}}{\Phi(\mathbf{x}_{i}\boldsymbol{\theta}_{\mathrm{o}})[1 - \Phi(\mathbf{x}_{i}\boldsymbol{\theta}_{\mathrm{o}})]}$$

Thus,  $Avar(\hat{\theta})$  in probit analysis is

{408}------------------------------------------------

$$\left(\sum_{i=1}^{N} \frac{\{\phi(\mathbf{x}_{i}\hat{\boldsymbol{\theta}})\}^{2} \mathbf{x}_{i}' \mathbf{x}_{i}}{\Phi(\mathbf{x}_{i}\hat{\boldsymbol{\theta}})[1 - \Phi(\mathbf{x}_{i}\hat{\boldsymbol{\theta}})]}\right)^{-1}$$
(13.33)

which is always positive definite when the inverse exists. Note that  $\mathbf{x}_{i}'\mathbf{x}_{i}$  is a  $K \times K$  matrix for each i.

Example 13.2 (continued): For the Poisson model with exponential conditional mean,  $\mathbf{H}_i(\boldsymbol{\theta}) = -\exp(\mathbf{x}_i \boldsymbol{\theta}) \mathbf{x}_i' \mathbf{x}_i$ . In this example, the Hessian does not depend on  $y_i$ , so there is no distinction between  $\mathbf{H}_i(\boldsymbol{\theta}_0)$  and  $\mathrm{E}[\mathbf{H}_i(\boldsymbol{\theta}_0) \mid \mathbf{x}_i]$ . The positive definite estimate of  $\mathrm{Avar}(\hat{\boldsymbol{\theta}})$  is simply

$$\left[\sum_{i=1}^{N} \exp(\mathbf{x}_i \hat{\boldsymbol{\theta}}) \mathbf{x}_i' \mathbf{x}_i\right]^{-1}$$
(13.34)