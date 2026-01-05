# Efficiency of MLE

> Pages: 449-453

Students of econometrics are often told that the maximum likelihood estimator is "efficient." Unfortunately, in the context of conditional MLE from Chapter 13, the statement of efficiency is usually ambiguous; Manski (1988, Chapter 8) is a notable exception. Theorem 14.3 allows us to state precisely the class of estimators in which the conditional MLE is relatively efficient. As in Chapter 13, we let  $E_{\theta}(\cdot | \mathbf{x})$  denote the expectation with respect to the conditional density  $f(\mathbf{y} | \mathbf{x}; \theta)$ .

Consider the class of estimators solving the first-order condition

$$N^{-1} \sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_i, \hat{\boldsymbol{\theta}}) \equiv \mathbf{0}$$
 (14.58)

where the  $P \times 1$  function  $\mathbf{g}(\mathbf{w}, \boldsymbol{\theta})$  such that

$$E_{\theta}[\mathbf{g}(\mathbf{w}, \boldsymbol{\theta}) \mid \mathbf{x}] = \mathbf{0}, \quad \text{all } \mathbf{x} \in \mathcal{X}, \quad \text{all } \boldsymbol{\theta} \in \boldsymbol{\Theta}$$
 (14.59)

In other words, the class of estimators is indexed by functions g satisfying a zero conditional moment restriction. We assume the standard regularity conditions from Chapter 12; in particular,  $g(w, \cdot)$  is continuously differentiably on the interior of  $\Theta$ .

As we showed in Section 13.7, functions  $\mathbf{g}$  satisfying condition (14.59) generally have the property

$$-\mathrm{E}[\nabla_{\theta}\mathbf{g}(\mathbf{w}, \boldsymbol{\theta}_{o}) \,|\, \mathbf{x}] = \mathrm{E}[\mathbf{g}(\mathbf{w}, \boldsymbol{\theta}_{o})\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o})' \,|\, \mathbf{x}]$$

{450}------------------------------------------------

where sðw; *y*Þ is the score of log fðy j x; *y*Þ (as always, we must impose certain regularity conditons on g and log f ). If we take the expectation of both sides with respect to x, we obtain condition (14.57) with r ¼ 1, A<sup>t</sup> ¼ E½'<sup>y</sup> gðw; *y*oÞ-, and s<sup>t</sup> ðwÞ ¼ sðw; *y*oÞ. It follows from Theorem 14.3 that the conditional MLE is efficient in the class of estimators solving equation (14.58), where gðÞ satisfies condition (14.59) and appropriate regularity conditions. Recall from Section 13.5.1 that the asymptotic variance of the (centered and standardized) CMLE is fE½sðw; *y*oÞsðw; *y*oÞ 0 g<sup>1</sup> . This is an example of an efficiency bound because no estimator of the form (14.58) under condition (14.59) can have an asymptotic variance smaller than fE½sðw; *y*oÞsðw; *y*oÞ 0 g<sup>1</sup> (in the matrix sense). When an estimator from this class has the same asymptotic variance as the CMLE, we way it achieves the efficiency bound.

It is important to see that the efficiency of the conditional MLE in the class of estimators solving equation (14.58) under condition (14.59) does not require x to be ancillary for *y*o: except for regularity conditions, the distribution of x is essentially unrestricted, and could depend on *y*o. Conditional MLE simply ignores information on *y*<sup>o</sup> that might be contained in the distribution of x, but so do all other estimators that are based on condition (14.59).

By choosing x to be empty, we conclude that the unconditional MLE is efficient in the class of estimators based on equation (14.58) with Ey½gðw; *y*Þ- ¼ 0, all *y* A Y. This is a very broad class of estimators, including all of the estimators requiring condition (14.59): if a function g satisfies condition (14.59), it has zero unconditional mean, too. Consequently, the unconditional MLE is generally more efficient than the conditional MLE. This efficiency comes at the price of having to model the joint density of ðy; xÞ, rather than just the conditional density of y given x. And, if our model for the density of x is incorrect, the unconditional MLE generally would be inconsistent.

When is CMLE as efficient as unconditional MLE for estimating *y*o? Assume that the model for the joint density of ðx; yÞ can be expressed as fðy j x; *y*Þhðx; *d*Þ, where *y* is the parameter vector of interest, and hðx; *d*oÞ is the marginal density of x for some vector *d*o. Then, if *d* does not depend on *y* in the sense that 'yhðx; *d*Þ ¼ 0 for all x and *d*, x is ancillary for *y*o. In fact, the CMLE is identical to the unconditional MLE. If *d* depends on *y*, the term '<sup>y</sup> log½hðx; *d*Þ generally contains information for estimating *y*o, and unconditional MLE will be more efficient than CMLE.

# 14.5.3 Efficient Choice of Instruments under Conditional Moment Restrictions

We can also apply Theorem 14.3 to find the optimal set of instrumental variables under general conditional moment restrictions. For a G 1 vector rðwi; *y*Þ, where w<sup>i</sup> A R<sup>M</sup>, *y*<sup>o</sup> is said to satisfy conditional moment restrictions if

$$\mathbf{E}[\mathbf{r}(\mathbf{w}_i, \boldsymbol{\theta}_0) \mid \mathbf{x}_i] = \mathbf{0} \tag{14.60}$$


{451}------------------------------------------------

where x<sup>i</sup> A R<sup>K</sup> is a subvector of wi. Under assumption (14.60), the matrix Z<sup>i</sup> appearing in equation (14.22) can be any function of xi. For a given matrix Zi, we obtain the efficient GMM estimator by using the efficient weighting matrix. However, unless Z<sup>i</sup> is the optimal set of instruments, we can generally obtain a more efficient estimator by adding any nonlinear function of x<sup>i</sup> to Zi. Because the list of potential IVs is endless, it is useful to characterize the optimal choice of Zi.

The solution to this problem is now pretty well known, and it can be obtained by applying Theorem 14.3. Let

$$\mathbf{\Omega}_{o}(\mathbf{x}_{i}) \equiv \text{Var}[\mathbf{r}(\mathbf{w}_{i}, \boldsymbol{\theta}_{o}) \mid \mathbf{x}_{i}]$$
(14.61)

be the G G conditional variance of rið*y*oÞ given xi, and define

$$\mathbf{R}_{o}(\mathbf{x}_{i}) \equiv \mathrm{E}[\nabla_{\theta} \mathbf{r}(\mathbf{w}_{i}, \boldsymbol{\theta}_{o}) \,|\, \mathbf{x}_{i}] \tag{14.62}$$

Problem 14.3 asks you to verify that the optimal choice of instruments is

$$\mathbf{Z}^*(\mathbf{x}_i) \equiv \mathbf{\Omega}_{o}(\mathbf{x}_i)^{-1} \mathbf{R}_{o}(\mathbf{x}_i)$$
 (14.63)

The optimal instrument matrix is always G P, and so the efficient method of moments estimator solves

$$\sum_{i=1}^{N} \mathbf{Z}^*(\mathbf{x}_i)' \mathbf{r}_i(\hat{\boldsymbol{\theta}}) = \mathbf{0}$$

There is no need to use a weighting matrix. Incidentally, by taking gðw; *y*Þ 1 Z ðxÞ 0 rðw; *y*Þ, we obtain a function g satisfying condition (14.59). From our discussion in Section 14.5.2, it follows immediately that the conditional MLE is no less efficient than the optimal IV estimator.

In practice, Z ðxiÞ is never a known function of xi. In some cases the function RoðxiÞ is a known function of x<sup>i</sup> and *y*<sup>o</sup> and can be easily estimated; this statement is true of linear SEMs under conditional mean assumptions (see Chapters 8 and 9) and of multivariate nonlinear regression, which we cover later in this subsection. Rarely do moment conditions imply a parametric form for WoðxiÞ, but sometimes homoskedasticity is assumed:

$$E[\mathbf{r}_i(\boldsymbol{\theta}_o)\mathbf{r}_i(\boldsymbol{\theta}_o) \mid \mathbf{x}_i] = \mathbf{\Omega}_o$$
 (14.64)

and W<sup>o</sup> is easily estimated as in equation (14.30) given a preliminary estimate of *y*o. Since both WoðxiÞ and RoðxiÞ must be estimated, we must know the asymptotic properties of GMM with generated instruments. Under conditional moment restrictions, generated instruments have no effect on the asymptotic variance of the GMM estimator. Thus, if the matrix of instruments is Zðxi; *g*oÞ for some unknown parame

{452}------------------------------------------------

ter vector  $\gamma_o$ , and  $\hat{\gamma}$  is an estimator such that  $\sqrt{N}(\hat{\gamma} - \gamma_o) = O_p(1)$ , then the GMM estimator using the generated instruments  $\hat{\mathbf{Z}}_i \equiv \mathbf{Z}(\mathbf{x}_i, \hat{\gamma})$  has the same limiting distribution as the GMM estimator using instruments  $\mathbf{Z}(\mathbf{x}_i, \gamma_o)$  (using any weighting matrix). This result follows from a mean value expansion, using the fact that the derivative of each element of  $\mathbf{Z}(\mathbf{x}_i, \gamma)$  with respect to  $\gamma$  is orthogonal to  $\mathbf{r}_i(\boldsymbol{\theta}_o)$  under condition (14.60):

$$N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{Z}}_{i}' \mathbf{r}_{i}(\hat{\boldsymbol{\theta}}) = N^{-1/2} \sum_{i=1}^{N} \mathbf{Z}_{i}(\gamma_{o})' \mathbf{r}_{i}(\boldsymbol{\theta}_{o})$$

$$+ \mathbf{E}[\mathbf{Z}_{i}(\gamma_{o})' \mathbf{R}_{o}(\mathbf{x}_{i})] \sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) + o_{o}(1)$$
(14.65)

The right-hand side of equation (14.65) is identical to the expansion with  $\hat{\mathbf{Z}}_i$  replaced with  $\mathbf{Z}_i(\gamma_0)$ .

Assuming now that  $\mathbf{Z}_i(\gamma_0)$  is the matrix of efficient instruments, the asymptotic variance of the efficient estimator is

Avar 
$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = \left\{ \mathbb{E}[\mathbf{R}_{o}(\mathbf{x}_{i})' \boldsymbol{\Omega}_{o}(\mathbf{x}_{i})^{-1} \mathbf{R}_{o}(\mathbf{x}_{i})] \right\}^{-1}$$
 (14.66)

as can be seen from Section 14.1 by noting that  $\mathbf{G}_o = \mathrm{E}[\mathbf{R}_o(\mathbf{x}_i)'\mathbf{\Omega}_o(\mathbf{x}_i)^{-1}\mathbf{R}_o(\mathbf{x}_i)]$  and  $\mathbf{\Lambda}_o = \mathbf{G}_o^{-1}$  when the instruments are given by equation (14.63).

Equation (14.66) is another example of an efficiency bound, this time under the conditional moment restrictions (14.54). What we have shown is that any GMM estimator has variance matrix that differs from equation (14.66) by a positive semi-definite matrix. Chamberlain (1987) has shown more: *any* estimator that uses only condition (14.60) and satisfies regularity conditions has variance matrix no smaller than equation (14.66).

Estimation of  $\mathbf{R}_{o}(\mathbf{x}_{i})$  generally requires nonparametric methods. Newey (1990) describes one approach. Essentially, regress the elements of  $\nabla_{\theta} \mathbf{r}_{i}(\hat{\boldsymbol{\theta}})$  on polynomial functions of  $\mathbf{x}_{i}$  (or other functions with good approximating properties), where  $\hat{\boldsymbol{\theta}}$  is an initial estimate of  $\boldsymbol{\theta}_{o}$ . The fitted values from these regressions can be used as the elements of  $\hat{\mathbf{R}}_{i}$ . Other nonparametric approaches are available. See Newey (1990, 1993) for details. Unfortunately, we need a fairly large sample size in order to apply such methods effectively.

As an example of finding the optimal instruments, consider the problem of estimating a conditional mean for a vector  $\mathbf{y}_i$ :

$$E(\mathbf{y}_i \mid \mathbf{x}_i) = \mathbf{m}(\mathbf{x}_i, \boldsymbol{\theta}_0) \tag{14.67}$$

Then the residual function is  $\mathbf{r}(\mathbf{w}_i, \boldsymbol{\theta}) \equiv \mathbf{y}_i - \mathbf{m}(\mathbf{x}_i, \boldsymbol{\theta})$  and  $\Omega_o(\mathbf{x}_i) = \mathrm{Var}(\mathbf{y}_i \mid \mathbf{x}_i)$ ; therefore, the optimal instruments are  $\mathbf{Z}_o(\mathbf{x}_i) \equiv \Omega_o(\mathbf{x}_i)^{-1} \nabla_{\boldsymbol{\theta}} \mathbf{m}(\mathbf{x}_i, \boldsymbol{\theta}_o)$ . This is an im-

{453}------------------------------------------------

portant example where  $\mathbf{R}_{o}(\mathbf{x}_{i}) = -\nabla_{\theta} \mathbf{m}(\mathbf{x}_{i}, \boldsymbol{\theta}_{o})$  is a known function of  $\mathbf{x}_{i}$  and  $\boldsymbol{\theta}_{o}$ . If the homoskedasticity assumption

$$Var(\mathbf{y}_i \mid \mathbf{x}_i) = \mathbf{\Omega}_0 \tag{14.68}$$

holds, then the efficient estimator is easy to obtain. First, let  $\hat{\boldsymbol{\theta}}$  be the multivariate nonlinear least squares (MNLS) estimator, which solves  $\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \sum_{i=1}^{N} [\mathbf{y}_i - \mathbf{m}(\mathbf{x}_i, \boldsymbol{\theta})]' \cdot [\mathbf{y}_i - \mathbf{m}(\mathbf{x}_i, \boldsymbol{\theta})]$ . As discussed in Problem 12.11, the MNLS estimator is generally consistent and  $\sqrt{N}$ -asymptotic normal. Define the residuals  $\hat{\mathbf{u}}_i \equiv \mathbf{y}_i - \mathbf{m}(\mathbf{x}_i, \hat{\boldsymbol{\theta}})$ , and define a consistent estimator of  $\Omega_0$  by  $\hat{\Omega} = N^{-1} \sum_{i=1}^{N} \hat{\mathbf{u}}_i \hat{\mathbf{u}}_i'$ . An efficient estimator,  $\hat{\boldsymbol{\theta}}$ , solves

$$\sum_{i=1}^{N} \nabla_{\theta} \mathbf{m}(\mathbf{x}_{i}, \hat{\hat{\boldsymbol{\theta}}})' \hat{\boldsymbol{\Omega}}^{-1}[\mathbf{y}_{i} - \mathbf{m}(\mathbf{x}_{i}, \hat{\boldsymbol{\theta}})] = \mathbf{0}$$

and the asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_0)$  is  $\{E[\nabla_{\theta} \mathbf{m}_i(\boldsymbol{\theta}_0)' \boldsymbol{\Omega}_0^{-1} \nabla_{\theta} \mathbf{m}_i(\boldsymbol{\theta}_0)]\}^{-1}$ . An asymptotically equivalent estimator is the nonlinear SUR estimator described in Problem 12.7. In either case, the estimator of  $Avar(\hat{\boldsymbol{\theta}})$  under assumption (14.68) is

$$\operatorname{Avar}(\hat{\boldsymbol{\theta}}) = \left[\sum_{i=1}^{N} \nabla_{\theta} \mathbf{m}_{i}(\hat{\boldsymbol{\theta}})' \hat{\boldsymbol{\Omega}}^{-1} \nabla_{\theta} \mathbf{m}_{i}(\hat{\boldsymbol{\theta}})\right]^{-1}$$

Because the nonlinear SUR estimator is a two-step M-estimator and  $\mathbf{B}_o = \mathbf{A}_o$  (in the notation of Chapter 12), the simplest forms of tests statistics are valid. If assumption (14.68) fails, the nonlinear SUR estimator is consistent, but robust inference should be used because  $\mathbf{A}_o \neq \mathbf{B}_o$ . And, the estimator is no longer efficient.