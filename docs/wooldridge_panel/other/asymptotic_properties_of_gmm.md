# Asymptotic Properties of GMM

> Pages: 432-437

Let  $\{\mathbf{w}_i \in \mathbb{R}^M : i = 1, 2, ...\}$  denote a set of independent, identically distributed random vectors, where some feature of the distribution of  $\mathbf{w}_i$  is indexed by the  $P \times 1$ parameter vector  $\boldsymbol{\theta}$ . The assumption of identical distribution is mostly for notational convenience; the following methods apply to independently pooled cross sections without modification.

We assume that for some function  $\mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}) \in \mathbb{R}^L$ , the parameter  $\boldsymbol{\theta}_0 \in \boldsymbol{\Theta} \subset \mathbb{R}^P$  satisfies the moment assumptions

$$E[\mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}_{o})] = 0 \tag{14.1}$$

As we saw in the linear case, where  $\mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta})$  was of the form  $\mathbf{Z}_i'(\mathbf{y}_i - \mathbf{X}_i \boldsymbol{\theta})$ , a minimal requirement for these moment conditions to identify  $\theta_0$  is  $L \ge P$ . If L = P, then the analogy principle suggests estimating  $\theta_0$  by setting the sample counterpart,  $N^{-1} \sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta})$ , to zero. In the linear case, this step leads to the instrumental variables estimator [see equation (8.22)]. When L > P, we can choose  $\hat{\theta}$  to make the sample average close to zero in an appropriate metric. A generalized method of **moments (GMM)** estimator,  $\hat{\theta}$ , minimizes a quadratic form in  $\sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_i, \theta)$ :

$$\min_{\boldsymbol{\theta} \in \mathbf{\Theta}} \left[ \sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}) \right]' \hat{\mathbf{\Xi}} \left[ \sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}) \right]$$
(14.2)

where  $\hat{\Xi}$  is an  $L \times L$  symmetric, positive semidefinite weighting matrix.

Consistency of the GMM estimator follows along the lines of consistency of the M-estimator in Chapter 12. Under standard moment conditions,  $N_{i}^{-1} \sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_{i}, \boldsymbol{\theta})$ satisfies the uniform law of large numbers (see Theorem 12.1). If,  $\hat{\Xi} \xrightarrow{p} \Xi_{o}$ , where  $\Xi_{o}$ is an  $L \times L$  positive definite matrix, then the random function

{433}------------------------------------------------

$$Q_N(\boldsymbol{\theta}) \equiv \left[ N^{-1} \sum_{i=1}^N \mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}) \right]' \hat{\mathbf{\Xi}} \left[ N^{-1} \sum_{i=1}^N \mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}) \right]$$
(14.3)

converges uniformly in probability to

$$\{ \mathbf{E}[\mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta})] \}^{\prime} \mathbf{\Xi}_{o} \{ \mathbf{E}[\mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta})] \}$$
(14.4)

Because  $\Xi_0$  is positive definite,  $\theta_0$  uniquely minimizes expression (14.4). For completeness, we summarize with a theorem containing regularity conditions:

THEOREM 14.1 (Consistency of GMM): Assume that (a)  $\Theta$  is compact; (b) for each  $\theta \in \Theta$ ,  $\mathbf{g}(\cdot, \theta)$  is Borel measurable on  $\mathcal{W}$ ; (c) for each  $\mathbf{w} \in \mathcal{W}$ ,  $\mathbf{g}(\mathbf{w}, \cdot)$  is continuous on  $\Theta$ ; (d)  $|g_j(\mathbf{w}, \theta)| \le b(\mathbf{w})$  for all  $\theta \in \Theta$  and  $j = 1, \ldots, L$ , where  $b(\cdot)$  is a nonnegative function on  $\mathcal{W}$  such that  $\mathrm{E}[b(\mathbf{w})] < \infty$ ; (e)  $\hat{\Xi} \stackrel{p}{\to} \Xi_0$ , an  $L \times L$  positive definite matrix; and (f)  $\theta_0$  is the unique solution to equation (14.1). Then a random vector  $\hat{\theta}$  exists that solves problem (14.2), and  $\hat{\theta} \stackrel{p}{\to} \theta_0$ .

If we assume only that  $\Xi_0$  is positive semidefinite, then we must directly assume that  $\theta_0$  is the unique minimizer of expression (14.4). Occasionally this generality is useful, but we will not need it.

Under the assumption that  $\mathbf{g}(\mathbf{w},\cdot)$  is continuously differentiable on  $\mathrm{int}(\mathbf{\Theta})$ ,  $\boldsymbol{\theta}_0 \in \mathrm{int}(\mathbf{\Theta})$ , and other standard regularity conditions, we can easily derive the limiting distribution of the GMM estimator. The first-order condition for  $\hat{\boldsymbol{\theta}}$  can be written as

$$\left[\sum_{i=1}^{N} \nabla_{\theta} \mathbf{g}(\mathbf{w}_{i}, \hat{\boldsymbol{\theta}})\right]' \hat{\mathbf{\Xi}} \left[\sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_{i}, \hat{\boldsymbol{\theta}})\right] \equiv \mathbf{0}$$
(14.5)

Define the  $L \times P$  matrix

$$\mathbf{G}_{o} \equiv \mathrm{E}[\nabla_{\theta} \mathbf{g}(\mathbf{w}_{i}, \boldsymbol{\theta}_{o})] \tag{14.6}$$

which we assume to have full rank P. This assumption essentially means that the moment conditions (14.1) are nonredundant. Then, by the WLLN and CLT,

$$N^{-1} \sum_{i=1}^{N} \nabla_{\theta} \mathbf{g}(\mathbf{w}_{i}, \boldsymbol{\theta}_{o}) \stackrel{p}{\to} \mathbf{G}_{o} \quad \text{and} \quad N^{-1/2} \sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_{i}, \boldsymbol{\theta}_{o}) = O_{p}(1)$$
 (14.7)

respectively. Let  $\mathbf{g}_i(\boldsymbol{\theta}) \equiv \mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta})$ . A mean value expansion of  $\sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_i, \hat{\boldsymbol{\theta}})$  about  $\boldsymbol{\theta}_0$ , appropriate standardizations by the sample size, and replacing random averages with their plims gives

$$\mathbf{0} = \mathbf{G}_{o}^{\prime} \mathbf{\Xi}_{o} N^{-1/2} \sum_{i=1}^{N} \mathbf{g}_{i}(\boldsymbol{\theta}_{o}) + \mathbf{A}_{o} \sqrt{N} (\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) + o_{p}(1)$$
(14.8)

{434}------------------------------------------------

where

$$\mathbf{A}_{o} \equiv \mathbf{G}_{o}^{\prime} \mathbf{\Xi}_{o} \mathbf{G}_{o} \tag{14.9}$$

Since  $A_0$  is positive definite under the given assumptions, we have

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = -\mathbf{A}_{o}^{-1}\mathbf{G}_{o}'\boldsymbol{\Xi}_{o}N^{-1/2}\sum_{i=1}^{N}\mathbf{g}_{i}(\boldsymbol{\theta}_{o}) + o_{p}(1) \xrightarrow{d} \text{Normal}(\mathbf{0}, \mathbf{A}_{o}^{-1}\mathbf{B}_{o}\mathbf{A}_{o}^{-1})$$
(14.10)

where

$$\mathbf{B}_{o} \equiv \mathbf{G}_{o}^{\prime} \mathbf{\Xi}_{o} \mathbf{\Lambda}_{o} \mathbf{\Xi}_{o} \mathbf{G}_{o} \tag{14.11}$$

and

$$\mathbf{\Lambda}_{o} \equiv \mathrm{E}[\mathbf{g}_{i}(\boldsymbol{\theta}_{o})\mathbf{g}_{i}(\boldsymbol{\theta}_{o})'] = \mathrm{Var}[\mathbf{g}_{i}(\boldsymbol{\theta}_{o})] \tag{14.12}$$

Expression (14.10) gives the influence function representation for the GMM estimator, and it also gives the limiting distribution of the GMM estimator. We summarize with a theorem, which is essentially given by Newey and McFadden (1994, Theorem 3.4):

THEOREM 14.2 (Asymptotic Normality of GMM): In addition to the assumptions in Theorem 14.1, assume that (a)  $\theta_0$  is in the interior of  $\Theta$ ; (b)  $\mathbf{g}(\mathbf{w}, \cdot)$  is continuously differentiable on the interior of  $\Theta$  for all  $\mathbf{w} \in \mathcal{W}$ ; (c) each element of  $\mathbf{g}(\mathbf{w}, \theta_0)$  has finite second moment; (d) each element of  $\nabla_{\theta} \mathbf{g}(\mathbf{w}, \theta)$  is bounded in absolute value by a function  $b(\mathbf{w})$ , where  $\mathrm{E}[b(\mathbf{w})] < \infty$ ; and (e)  $\mathbf{G}_0$  in expression (14.6) has rank P. Then expression (14.10) holds, and so  $\mathrm{Avar}(\hat{\boldsymbol{\theta}}) = \mathbf{A}_0^{-1} \mathbf{B}_0 \mathbf{A}_0^{-1} / N$ .

Estimating the asymptotic variance of the GMM estimator is easy once  $\hat{\theta}$  has been obtained. A consistent estimator of  $\Lambda_0$  is given by

$$\hat{\mathbf{\Lambda}} \equiv N^{-1} \sum_{i=1}^{N} \mathbf{g}_{i}(\hat{\boldsymbol{\theta}}) \mathbf{g}_{i}(\hat{\boldsymbol{\theta}})'$$
(14.13)

and Avar( $\hat{\boldsymbol{\theta}}$ ) is estimated as  $\hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1}/N$ , where

$$\hat{\mathbf{A}} \equiv \hat{\mathbf{G}}' \hat{\mathbf{\Xi}} \hat{\mathbf{G}}, \qquad \hat{\mathbf{B}} \equiv \hat{\mathbf{G}}' \hat{\mathbf{\Xi}} \hat{\mathbf{A}} \hat{\mathbf{\Xi}} \hat{\mathbf{G}} \tag{14.14}$$

and

$$\hat{\mathbf{G}} \equiv N^{-1} \sum_{i=1}^{N} \nabla_{\theta} \mathbf{g}_{i}(\hat{\boldsymbol{\theta}})$$
 (14.15)

{435}------------------------------------------------

As in the linear case in Section 8.3.3, an optimal weighting matrix exists for the given moment conditions:  $\hat{\Xi}$  should be a consistent estimator of  $\Lambda_o^{-1}$ . When  $\Xi_o = \Lambda_o^{-1}$ ,  $\mathbf{B}_o = \mathbf{A}_o$  and Avar  $\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_o) = (\mathbf{G}_o' \Lambda_o^{-1} \mathbf{G}_o)^{-1}$ . Thus the difference in asymptotic variances between the general GMM estimator and the estimator with plim  $\hat{\Xi} = \Lambda_o^{-1}$  is

$$(\mathbf{G}_{o}^{\prime}\mathbf{\Xi}_{o}\mathbf{G}_{o})^{-1}(\mathbf{G}_{o}^{\prime}\mathbf{\Xi}_{o}\mathbf{\Lambda}_{o}\mathbf{\Xi}_{o}\mathbf{G}_{o})(\mathbf{G}_{o}^{\prime}\mathbf{\Xi}_{o}\mathbf{G}_{o})^{-1} - (\mathbf{G}_{o}^{\prime}\mathbf{\Lambda}_{o}^{-1}\mathbf{G}_{o})^{-1}$$
(14.16)

This expression can be shown to be positive semidefinite using the same argument as in Chapter 8 (see Problem 8.5).

In order to obtain an asymptotically efficient GMM estimator we need a preliminary estimator of  $\theta_0$  in order to obtain  $\hat{\Lambda}$ . Let  $\hat{\theta}$  be such an estimator, and define  $\hat{\Lambda}$  as in expression (14.13) but with  $\hat{\theta}$  in place of  $\hat{\theta}$ . Then, an efficient GMM estimator [given the function  $\mathbf{g}(\mathbf{w}, \boldsymbol{\theta})$ ] solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \left[ \sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}) \right]' \hat{\mathbf{\Lambda}}^{-1} \left[ \sum_{i=1}^{N} \mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}) \right]$$
(14.17)

and its asymptotic variance is estimated as

$$\operatorname{Avar}(\hat{\boldsymbol{\theta}}) = (\hat{\mathbf{G}}'\hat{\boldsymbol{\Lambda}}^{-1}\hat{\mathbf{G}})^{-1}/N \tag{14.18}$$

As in the linear case, an optimal GMM estimator is called the **minimum chi-square estimator** because

$$\left[N^{-1/2}\sum_{i=1}^{N}\mathbf{g}_{i}(\hat{\boldsymbol{\theta}})\right]'\hat{\boldsymbol{\Lambda}}^{-1}\left[\sum_{i=1}^{N}N^{-1/2}\mathbf{g}_{i}(\hat{\boldsymbol{\theta}})\right]$$
(14.19)

has a limiting chi-square distribution with L-P degrees of freedom under the conditions of Theorem 14.2. Therefore, the value of the objective function (properly standardized by the sample size) can be used as a test of any overidentifying restrictions in equation (14.1) when L > P. If statistic (14.19) exceeds the relevant critical value in a  $\chi^2_{L-P}$  distribution, then equation (14.1) must be rejected: at least some of the moment conditions are not supported by the data. For the linear model, this is the same statistic given in equation (8.49).

As always, we can test hypotheses of the form  $H_0$ :  $\mathbf{c}(\theta_0) = \mathbf{0}$ , where  $\mathbf{c}(\theta)$  is a  $Q \times 1$  vector,  $Q \leq P$ , by using the Wald approach and the appropriate variance matrix estimator. A statistic based on the difference in objective functions is also available if the minimum chi-square estimator is used so that  $\mathbf{B}_0 = \mathbf{A}_0$ . Let  $\tilde{\boldsymbol{\theta}}$  denote the solution to problem (14.17) subject to the restrictions  $\mathbf{c}(\theta) = \mathbf{0}$ , and let  $\hat{\boldsymbol{\theta}}$  denote the unrestricted estimator solving problem (14.17); importantly, these both use the same weighting

{436}------------------------------------------------

matrix  $\hat{\mathbf{A}}^{-1}$ . Typically,  $\hat{\mathbf{A}}$  is obtained from a first-stage, unrestricted estimator. Assuming that the constraints can be written in implicit form and satisfy the conditions discussed in Section 12.6.2, the **GMM distance statistic** (or **GMM criterion function statistic**) has a limiting  $\chi_O^2$  distribution:

$$\left\{ \left[ \sum_{i=1}^{N} \mathbf{g}_{i}(\tilde{\boldsymbol{\theta}}) \right]' \hat{\boldsymbol{\Lambda}}^{-1} \left[ \sum_{i=1}^{N} \mathbf{g}_{i}(\tilde{\boldsymbol{\theta}}) \right] - \left[ \sum_{i=1}^{N} \mathbf{g}_{i}(\hat{\boldsymbol{\theta}}) \right]' \hat{\boldsymbol{\Lambda}}^{-1} \left[ \sum_{i=1}^{N} \mathbf{g}_{i}(\hat{\boldsymbol{\theta}}) \right] \right\} / N \stackrel{d}{\to} \chi_{Q}^{2}$$
(14.20)

When applied to linear GMM problems, we obtain the statistic in equation (8.45). One nice feature of expression (14.20) is that it is invariant to reparameterization of the null hypothesis, just as the quasi-LR statistic is invariant for M-estimation. Therefore, we might prefer statistic (14.20) over the Wald statistic (8.48) for testing nonlinear restrictions in linear models. Of course, the computation of expression (14.20) is more difficult because we would actually need to carry out estimation subject to nonlinear restrictions.

A nice application of the GMM methods discussed in this section is two-step estimation procedures, which arose in Chapters 6, 12, and 13. Suppose that the estimator  $\hat{\theta}$ —it could be an M-estimator or a GMM estimator—depends on a first-stage estimator,  $\hat{\gamma}$ . A unified approach to obtaining the asymptotic variance of  $\hat{\theta}$  is to stack the first-order conditions for  $\hat{\theta}$  and  $\hat{\gamma}$  into the same function  $\mathbf{g}(\cdot)$ . This is always possible for the estimators encountered in this book. For example, if  $\hat{\gamma}$  is an M-estimator solving  $\sum_{i=1}^{N} \mathbf{s}(\mathbf{w}_i, \hat{\gamma}) = \mathbf{0}$ , and  $\hat{\theta}$  is a two-step M-estimator solving

$$\sum_{i=1}^{N} \mathbf{h}(\mathbf{w}_i, \hat{\boldsymbol{\theta}}; \hat{\boldsymbol{\gamma}})] = \mathbf{0}$$
 (14.21)

then we can obtain the asymptotic variance of  $\hat{\theta}$  by defining

$$\mathbf{g}(\mathbf{w}, \boldsymbol{\theta}, \boldsymbol{\gamma}) = \begin{bmatrix} \mathbf{h}(\mathbf{w}, \boldsymbol{\theta}; \boldsymbol{\gamma}) \\ \mathbf{s}(\mathbf{w}, \boldsymbol{\gamma}) \end{bmatrix}$$

and applying the GMM formulas. The first-order condition for the full GMM problem reproduces the first-order conditions for each estimator separately.

In general, either  $\hat{\gamma}$ ,  $\hat{\theta}$ , or both might themselves be GMM estimators. Then, stacking the orthogonality conditions into one vector can simplify the derivation of the asymptotic variance of the second-step estimator  $\hat{\theta}$  while also ensuring efficient estimation when the optimal weighting matrix is used.

Finally, sometimes we want to know whether adding additional moment conditions does not improve the efficiency of the minimum chi-square estimator. (Adding

{437}------------------------------------------------

additional moment conditions can never reduce asymptotic efficiency, provided an efficient weighting matrix is used.) In other words, if we start with equation (14.1) but add new moments of the form  $E[\mathbf{h}(\mathbf{w}, \boldsymbol{\theta}_o)] = 0$ , when does using the extra moment conditions yield the same asymptotic variance as the original moment conditions? Breusch, Qian, Schmidt, and Wyhowski (1999) prove some general redundancy results for the minimum chi-square estimator. Qian and Schmidt (1999) study the problem of adding moment conditions that do not depend on unknown parameters, and they characterize when such moment conditions improve efficiency.