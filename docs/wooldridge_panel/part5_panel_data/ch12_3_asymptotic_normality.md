# Asymptotic Normality

> Pages: 360-364

Under additional assumptions on the objective function, we can also show that M-estimators are asymptotically normally distributed (and converge at the rate  $\sqrt{N}$ ). It turns out that continuity over the parameter space does not ensure asymptotic normality. We will assume more than is needed because all of the problems we cover in this book have objective functions with many continuous derivatives.

The simplest asymptotic normality proof proceeds as follows. Assume that  $\theta_0$  is in the interior of  $\Theta$ , which means that  $\Theta$  must have nonempty interior; this assumption is true in most applications. Then, since  $\hat{\theta} \stackrel{p}{\to} \theta_0$ ,  $\hat{\theta}$  is in the interior of  $\Theta$  with probability approaching one. If  $q(\mathbf{w}, \cdot)$  is continuously differentiable on the interior of  $\Theta$ , then (with probability approaching one)  $\hat{\theta}$  solves the first-order condition

$$\sum_{i=1}^{N} \mathbf{s}(\mathbf{w}_i, \hat{\boldsymbol{\theta}}) = \mathbf{0} \tag{12.14}$$

where  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta})$  is the  $P \times 1$  vector of partial derivatives of  $q(\mathbf{w}, \boldsymbol{\theta})$ :  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta})' = [\partial q(\mathbf{w}, \boldsymbol{\theta})/\partial \theta_1, \partial q(\mathbf{w}, \boldsymbol{\theta})/\partial \theta_2, \dots, \partial q(\mathbf{w}, \boldsymbol{\theta})/\partial \theta_P]$ . [Or,  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta})$  is the transpose of the gradient of  $q(\mathbf{w}, \boldsymbol{\theta})$ .] We call  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta})$  the **score of the objective function**,  $q(\mathbf{w}, \boldsymbol{\theta})$ . While condition (12.14) can only be guaranteed to hold with probability approaching one, usually it holds exactly; at any rate, we will drop the qualifier, as it does not affect the derivation of the limiting distribution.

If  $q(\mathbf{w}, \cdot)$  is twice continuously differentiable, then each row of the left-hand side of equation (12.14) can be expanded about  $\theta_0$  in a mean-value expansion:

$$\sum_{i=1}^{N} \mathbf{s}(\mathbf{w}_{i}, \hat{\boldsymbol{\theta}}) = \sum_{i=1}^{N} \mathbf{s}(\mathbf{w}_{i}, \boldsymbol{\theta}_{o}) + \left(\sum_{i=1}^{N} \ddot{\mathbf{H}}_{i}\right) (\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o})$$
(12.15)


{361}------------------------------------------------

The notation  $\ddot{\mathbf{H}}_i$  denotes the  $P \times P$  Hessian of the objective function,  $q(\mathbf{w}_i, \boldsymbol{\theta})$ , with respect to  $\boldsymbol{\theta}$ , but with each row of  $\mathbf{H}(\mathbf{w}_i, \boldsymbol{\theta}) \equiv \partial^2 q(\mathbf{w}_i, \boldsymbol{\theta})/\partial \boldsymbol{\theta} \partial \boldsymbol{\theta}' \equiv \nabla_{\boldsymbol{\theta}}^2 q(\mathbf{w}_i, \boldsymbol{\theta})$  evaluated at a different mean value. Each of the P mean values is on the line segment between  $\boldsymbol{\theta}_0$  and  $\hat{\boldsymbol{\theta}}$ . We cannot know what these mean values are, but we do know that each must converge in probability to  $\boldsymbol{\theta}_0$  (since each is "trapped" between  $\hat{\boldsymbol{\theta}}$  and  $\boldsymbol{\theta}_0$ ).

Combining equations (12.14) and (12.15) and multiplying through by  $1/\sqrt{N}$  gives

$$\mathbf{0} = N^{-1/2} \sum_{i=1}^{N} \mathbf{s}(\mathbf{w}_i, \boldsymbol{\theta}_{\text{o}}) + \left( N^{-1} \sum_{i=1}^{N} \ddot{\mathbf{H}}_i \right) \sqrt{N} (\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{\text{o}})$$

Now, we can apply Lemma 12.1 to get  $N^{-1}\sum_{i=1}^N\ddot{\mathbf{H}}_i\stackrel{p}{\to}\mathrm{E}[\mathbf{H}(\mathbf{w},\boldsymbol{\theta}_\mathrm{o})]$  (under some moment conditions). If  $\mathbf{A}_\mathrm{o}\equiv\mathrm{E}[\mathbf{H}(\mathbf{w},\boldsymbol{\theta}_\mathrm{o})]$  is nonsingular, then  $N^{-1}\sum_{i=1}^N\ddot{\mathbf{H}}_i$  is nonsingular w.p.a.1 and  $(N^{-1}\sum_{i=1}^N\ddot{\mathbf{H}}_i)^{-1}\stackrel{p}{\to}\mathbf{A}_\mathrm{o}^{-1}$ . Therefore, we can write

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = \left(N^{-1} \sum_{i=1}^{N} \ddot{\mathbf{H}}_{i}\right)^{-1} \left[-N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\boldsymbol{\theta}_{o})\right]$$

where  $\mathbf{s}_i(\boldsymbol{\theta}_o) \equiv \mathbf{s}(\mathbf{w}_i, \boldsymbol{\theta}_o)$ . As we will show,  $\mathrm{E}[\mathbf{s}_i(\boldsymbol{\theta}_o)] = \mathbf{0}$ . Therefore,  $N^{-1/2} \sum_{i=1}^N \mathbf{s}_i(\boldsymbol{\theta}_o)$  generally satisfies the central limit theorem because it is the average of i.i.d. random vectors with zero mean, multiplied by the usual  $\sqrt{N}$ . Since  $\mathrm{o}_p(1) \cdot \mathrm{O}_p(1) = \mathrm{o}_p(1)$ , we have

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = \mathbf{A}_{o}^{-1} \left[ -N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\boldsymbol{\theta}_{o}) \right] + o_{p}(1)$$
(12.16)

This is an important equation. It shows that  $\sqrt{N}(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_o)$  inherits its limiting distribution from the average of the scores, evaluated at  $\boldsymbol{\theta}_o$ . The matrix  $\mathbf{A}_o^{-1}$  simply acts as a linear transformation. If we absorb this linear transformation into  $\mathbf{s}_i(\boldsymbol{\theta}_o)$ , we can write

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = N^{-1/2} \sum_{i=1}^{N} \mathbf{r}_{i}(\boldsymbol{\theta}_{o}) + o_{p}(1)$$
(12.17)

where  $\mathbf{r}_i(\boldsymbol{\theta}_o) \equiv -\mathbf{A}_o^{-1}\mathbf{s}_i(\boldsymbol{\theta}_o)$ ; this is sometimes called the **influence function representation** of  $\hat{\boldsymbol{\theta}}$ , where  $\mathbf{r}(\mathbf{w}, \boldsymbol{\theta})$  is the influence function.

Equation (12.16) [or (12.17)] allows us to derive the **first-order asymptotic distribution** of  $\hat{\theta}$ . Higher order representations attempt to reduce the error in the  $o_p(1)$  term in equation (12.16); such derivations are much more complicated than equation (12.16) and are beyond the scope of this book.

{362}------------------------------------------------

We have essentially proven the following result:

THEOREM 12.3 (Asymptotic Normality of M-estimators): In addition to the assumptions in Theorem 12.2, assume (a)  $\theta_o$  is in the interior of  $\Theta$ ; (b)  $\mathbf{s}(\mathbf{w}, \cdot)$  is continuously differentiable on the interior of  $\Theta$  for all  $\mathbf{w} \in \mathcal{W}$ ; (c) Each element of  $\mathbf{H}(\mathbf{w}, \boldsymbol{\theta})$  is bounded in absolute value by a function  $b(\mathbf{w})$ , where  $E[b(\mathbf{w})] < \infty$ ; (d)  $\mathbf{A}_o \equiv E[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_o)]$  is positive definite; (e)  $E[\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_o)] = \mathbf{0}$ ; and (f) each element of  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_o)$  has finite second moment.

Then

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) \xrightarrow{d} \text{Normal}(0, \mathbf{A}_{o}^{-1}\mathbf{B}_{o}\mathbf{A}_{o}^{-1})$$
 (12.18)

where

$$\mathbf{A}_{o} \equiv \mathrm{E}[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_{o})] \tag{12.19}$$

and

$$\mathbf{B}_{o} \equiv \mathrm{E}[\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})'] = \mathrm{Var}[\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})] \tag{12.20}$$

Thus.

Avar 
$$\hat{\boldsymbol{\theta}} = \mathbf{A}_{o}^{-1} \mathbf{B}_{o} \mathbf{A}_{o}^{-1} / N$$
 (12.21)

Theorem 12.3 implies asymptotic normality of most of the estimators we study in the remainder of the book. A leading example that is not covered by Theorem 12.3 is the LAD estimator. Even if  $m(\mathbf{x}, \theta)$  is twice continuously differentiable in  $\theta$ , the objective function for each i,  $q(\mathbf{w}_i, \theta) \equiv |y_i - m(\mathbf{x}_i, \theta)|$ , is not twice continuously differentiable because the absolute value function is nondifferentiable at zero. By itself, this limitation is a minor nuisance. More importantly, by any reasonable definition, the Hessian of the LAD objective function is the zero matrix in the leading case of a linear conditional median function, and this fact violates assumption d of Theorem 12.3. It turns out that the LAD estimator *is* generally  $\sqrt{N}$ -asymptotically normal, but Theorem 12.3 cannot be applied. Newey and McFadden (1994) contains results that can be used.

A key component of Theorem 12.3 is that the score evaluated at  $\theta_0$  has expected value zero. In many applications, including NLS, we can show this result directly. But it is also useful to know that it holds in the abstract M-estimation framework, at least if we can interchange the expectation and the derivative. To see this point, note that, if  $\theta_0$  is in the interior of  $\Theta$ , and  $E[q(\mathbf{w}, \theta)]$  is differentiable for  $\theta \in$  int  $\Theta$ , then

$$\nabla_{\theta} \mathbf{E}[q(\mathbf{w}, \boldsymbol{\theta})]|_{\boldsymbol{\theta} = \boldsymbol{\theta}_{\alpha}} = \mathbf{0} \tag{12.22}$$

{363}------------------------------------------------

where '<sup>y</sup> denotes the gradient with respect to *y*. Now, if the derivative and expectations operator can be interchanged (which is the case quite generally), then equation (12.22) implies

$$E[\nabla_{\theta}q(\mathbf{w}, \boldsymbol{\theta}_{o})] = E[\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})] = \mathbf{0}$$
(12.23)

A similar argument shows that, in general, E½Hðw; *y*oÞ is positive semidefinite. If *y*<sup>o</sup> is identified, E½Hðw; *y*oÞ is positive definite.

For the remainder of this chapter, it is convenient to divide the original NLS objective function by two:

$$q(\mathbf{w}, \boldsymbol{\theta}) = [y - m(\mathbf{x}, \boldsymbol{\theta})]^2 / 2 \tag{12.24}$$

The score of equation (12.24) can be written as

$$\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}) = -\nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta})'[y - m(\mathbf{x}, \boldsymbol{\theta})]$$
(12.25)

where 'ymðx; *y*Þ is the 1 P gradient of mðx; *y*Þ, and therefore 'ymðx; *y*Þ <sup>0</sup> is P 1. We can show directly that this expression has an expected value of zero at *y* ¼ *y*<sup>o</sup> by showing that expected value of sðw; *y*oÞ conditional on x is zero:

$$E[\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o}) \mid \mathbf{x}] = -\nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta})'[E(y \mid \mathbf{x}) - m(\mathbf{x}, \boldsymbol{\theta}_{o})] = \mathbf{0}$$
(12.26)

The variance of sðw; *y*oÞ is

$$\mathbf{B}_{o} \equiv \mathrm{E}[\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})'] = \mathrm{E}[u^{2}\nabla_{\theta}m(\mathbf{x}, \boldsymbol{\theta}_{o})'\nabla_{\theta}m(\mathbf{x}, \boldsymbol{\theta}_{o})]$$
(12.27)

where the error u 1y mðx; *y*oÞ is the difference between y and Eðy j xÞ. The Hessian of qðw; *y*Þ is

$$\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}) = \nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta})' \nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}) - \nabla_{\theta}^{2} m(\mathbf{x}, \boldsymbol{\theta}) [y - m(\mathbf{x}, \boldsymbol{\theta})]$$
(12.28)

where '<sup>2</sup> <sup>y</sup>mðx; *y*Þ is the P P Hessian of mðx; *y*Þ with respect to *y*. To find the expected value of Hðw; *y*Þ at *y* ¼ *y*o, we first find the expectation conditional on x. When evaluated at *y*o, the second term in equation (12.28) is '<sup>2</sup> <sup>y</sup>mðx; *y*oÞu, and it therefore has a zero mean conditional on x [since Eðu j xÞ ¼ 0]. Therefore,

$$E[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_{o}) | \mathbf{x}] = \nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}_{o})' \nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}_{o})$$
(12.29)

Taking the expected value of equation (12.29) over the distribution of x gives

$$\mathbf{A}_{o} = \mathrm{E}[\nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}_{o})' \nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}_{o})] \tag{12.30}$$

This matrix plays a fundamental role in nonlinear regression. When *y*<sup>o</sup> is identified, A<sup>o</sup> is generally positive definite. In the linear case mðx; *y*Þ ¼ x*y*, A<sup>o</sup> ¼ Eðx<sup>0</sup> xÞ. In the

{364}------------------------------------------------

exponential case  $m(\mathbf{x}, \boldsymbol{\theta}) = \exp(\mathbf{x}\boldsymbol{\theta})$ ,  $\mathbf{A}_o = \mathrm{E}[\exp(2\mathbf{x}\boldsymbol{\theta}_o)\mathbf{x}'\mathbf{x}]$ , which is generally positive definite whenever  $\mathrm{E}(\mathbf{x}'\mathbf{x})$  is. In the example  $m(\mathbf{x}, \boldsymbol{\theta}) = \theta_1 + \theta_2 x_2 + \theta_3 x_3^{\theta_4}$  with  $\theta_{o3} = 0$ , it is easy to show that matrix (12.30) has rank less than four.

For nonlinear regression,  $\mathbf{A}_o$  and  $\mathbf{B}_o$  are similar in that they both depend on  $\nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}_o)' \nabla_{\theta} m(\mathbf{x}, \boldsymbol{\theta}_o)$ . Generally, though, there is no simple relationship between  $\mathbf{A}_o$  and  $\mathbf{B}_o$  because the latter depends on the distribution of  $u^2$ , the squared population error. In Section 12.5 we will show that a homoskedasticity assumption implies that  $\mathbf{B}_o$  is proportional to  $\mathbf{A}_o$ .