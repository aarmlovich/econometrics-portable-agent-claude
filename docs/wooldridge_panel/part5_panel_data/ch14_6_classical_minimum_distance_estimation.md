# Classical Minimum Distance Estimation

> Pages: 453-457

We end this chapter with a brief treatment of classical minimum distance (CMD) estimation. This method has features in common with GMM, and often it is a convenient substitute for GMM.

Suppose that the  $P \times 1$  parameter vector of interest,  $\theta_0$ , which often consists of parameters from a structural model, is known to be related to an  $S \times 1$  vector of reduced form parameters,  $\pi_0$ , where S > P. In particular,  $\pi_0 = \mathbf{h}(\theta_0)$  for a known, continuously differentiable function  $\mathbf{h} : \mathbb{R}^P \to \mathbb{R}^S$ , so that  $\mathbf{h}$  maps the structural parameters into the reduced form parameters.

CMD estimation of  $\theta_0$  entails first estimating  $\pi_0$  by  $\hat{\pi}$ , and then choosing an estimator  $\hat{\theta}$  of  $\theta_0$  by making the distance between  $\hat{\pi}$  and  $\mathbf{h}(\hat{\theta})$  as small as possible. As with GMM estimation, we use a weighted Euclidean measure of distance. While a

{454}------------------------------------------------

CMD estimator can be defined for any positive semidefinite weighting matrix, we consider only the efficient CMD estimator given our choice of  $\hat{\pi}$ . As with efficient GMM, the CMD estimator that uses the efficient weighting matrix is also called the minimum chi-square estimator.

Assuming that for an  $S \times S$  positive definite matrix  $\Xi_0$ 

$$\sqrt{N}(\hat{\boldsymbol{\pi}} - \boldsymbol{\pi}_{\text{o}}) \stackrel{a}{\sim} \text{Normal}(\boldsymbol{0}, \boldsymbol{\Xi}_{\text{o}})$$
 (14.69)

it turns out that an efficient CMD estimator solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \{ \hat{\boldsymbol{\pi}} - \mathbf{h}(\boldsymbol{\theta}) \}' \hat{\boldsymbol{\Xi}}^{-1} \{ \hat{\boldsymbol{\pi}} - \mathbf{h}(\boldsymbol{\theta}) \}$$
 (14.70)

where  $\text{plim}_{N\to\infty} \hat{\Xi} = \Xi_0$ . In other words, an efficient weighting matrix is the inverse of any consistent estimator of Avar  $\sqrt{N}(\hat{\pi} - \pi_0)$ .

We can easily derive the asymptotic variance of  $\sqrt{N}(\hat{\theta} - \theta_o)$ . The first-order condition for  $\hat{\theta}$  is

$$\mathbf{H}(\hat{\boldsymbol{\theta}})'\hat{\mathbf{\Xi}}^{-1}\{\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})\} \equiv \mathbf{0} \tag{14.71}$$

where  $\mathbf{H}(\theta) \equiv \nabla_{\theta} \mathbf{h}(\theta)$  is the  $S \times P$  Jacobian of  $\mathbf{h}(\theta)$ . Since  $\mathbf{h}(\theta_0) = \pi_0$  and

$$\sqrt{N}\{\mathbf{h}(\hat{\boldsymbol{\theta}}) - \mathbf{h}(\boldsymbol{\theta}_{o})\} = \mathbf{H}(\boldsymbol{\theta}_{o})\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) + o_{p}(1)$$

by a standard mean value expansion about  $\theta_0$ , we have

$$\mathbf{0} = \mathbf{H}(\hat{\boldsymbol{\theta}})'\hat{\mathbf{\Xi}}^{-1}\{\sqrt{N}(\hat{\boldsymbol{\pi}} - \boldsymbol{\pi}_{o}) - \mathbf{H}(\boldsymbol{\theta}_{o})\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o})\} + o_{p}(1)$$
(14.72)

Because  $\mathbf{H}(\cdot)$  is continuous and  $\hat{\boldsymbol{\theta}} \stackrel{p}{\to} \boldsymbol{\theta}_{o}$ ,  $\mathbf{H}(\hat{\boldsymbol{\theta}}) = \mathbf{H}(\boldsymbol{\theta}_{o}) + o_{p}(1)$ ; by assumption  $\hat{\boldsymbol{\Xi}} = \boldsymbol{\Xi}_{o} + o_{p}(1)$ . Therefore,

$$\mathbf{H}(\boldsymbol{\theta}_{\mathrm{o}})'\mathbf{\Xi}_{\mathrm{o}}^{-1}\mathbf{H}(\boldsymbol{\theta}_{\mathrm{o}})\sqrt{N}(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{\mathrm{o}}) = \mathbf{H}(\boldsymbol{\theta}_{\mathrm{o}})'\mathbf{\Xi}_{\mathrm{o}}^{-1}\sqrt{N}(\hat{\boldsymbol{\pi}}-\boldsymbol{\pi}_{\mathrm{o}}) + o_{p}(1)$$

By assumption (14.69) and the asymptotic equivalence lemma,

$$\mathbf{H}(\boldsymbol{\theta}_{o})'\mathbf{\Xi}_{o}^{-1}\mathbf{H}(\boldsymbol{\theta}_{o})\sqrt{N}(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o})\overset{a}{\sim}\mathrm{Normal}[\mathbf{0},\mathbf{H}(\boldsymbol{\theta}_{o})'\mathbf{\Xi}_{o}^{-1}\mathbf{H}(\boldsymbol{\theta}_{o})]$$

and so

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) \stackrel{a}{\sim} \text{Normal}[\mathbf{0}, (\mathbf{H}_{o}'\mathbf{\Xi}_{o}^{-1}\mathbf{H}_{o})^{-1}]$$
 (14.73)

provided that  $\mathbf{H}_o \equiv \mathbf{H}(\theta_o)$  has full-column rank P, as will generally be the case when  $\theta_o$  is identified and  $\mathbf{h}(\cdot)$  contains no redundancies. The appropriate estimator of  $\mathbf{Avar}(\hat{\boldsymbol{\theta}})$  is

$$\operatorname{Avar}(\hat{\boldsymbol{\theta}}) \equiv (\hat{\mathbf{H}}'\hat{\mathbf{\Xi}}^{-1}\hat{\mathbf{H}})^{-1}/N = (\hat{\mathbf{H}}'[\operatorname{Avar}(\hat{\boldsymbol{\pi}})]^{-1}\hat{\mathbf{H}})^{-1}$$
(14.74)

{455}------------------------------------------------

The proof that  $\hat{\Xi}^{-1}$  is the optimal weighting matrix in expression (14.70) is very similar to the derivation of the optimal weighting matrix for GMM. (It can also be shown by applying Theorem 14.3.) We will simply call the efficient estimator the CMD estimator, where it is understood that we are using the efficient weighting matrix.

There is another efficiency issue that arises when more than one  $\sqrt{N}$ -asymptotically normal estimator for  $\pi_0$  is available: Which estimator of  $\pi_0$  should be used? Let  $\hat{\boldsymbol{\theta}}$  be the estimator based on  $\hat{\boldsymbol{\pi}}$ , and let  $\tilde{\boldsymbol{\theta}}$  be the estimator based on another estimator,  $\tilde{\boldsymbol{\pi}}$ . You are asked to show in Problem 14.6 that Avar  $\sqrt{N}(\tilde{\boldsymbol{\theta}}-\boldsymbol{\theta}_0)$  – Avar  $\sqrt{N}(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_0)$  is p.s.d. whenever Avar  $\sqrt{N}(\tilde{\boldsymbol{\pi}}-\boldsymbol{\pi}_0)$  – Avar  $\sqrt{N}(\tilde{\boldsymbol{\pi}}-\boldsymbol{\pi}_0)$  is p.s.d. In other words, we should use the most efficient estimator of  $\boldsymbol{\theta}_0$ .

A test of overidentifying restrictions is immediately available after estimation, because, under the null hypothesis  $\pi_0 = \mathbf{h}(\theta_0)$ ,

$$N[\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})]' \hat{\boldsymbol{\Xi}}^{-1}[\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})] \stackrel{a}{\sim} \chi_{S-P}^{2}$$
(14.75)

To show this result, we use

$$\begin{split} \sqrt{N}[\hat{\boldsymbol{\pi}} - \boldsymbol{h}(\hat{\boldsymbol{\theta}})] &= \sqrt{N}(\hat{\boldsymbol{\pi}} - \boldsymbol{\pi}_{o}) - \boldsymbol{H}_{o}\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) + o_{p}(1) \\ &= \sqrt{N}(\hat{\boldsymbol{\pi}} - \boldsymbol{\pi}_{o}) - \boldsymbol{H}_{o}(\boldsymbol{H}_{o}'\boldsymbol{\Xi}_{o}^{-1}\boldsymbol{H}_{o})^{-1}\boldsymbol{H}_{o}'\boldsymbol{\Xi}_{o}^{-1}\sqrt{N}(\hat{\boldsymbol{\pi}} - \boldsymbol{\pi}_{o}) + o_{p}(1) \\ &= [\boldsymbol{I}_{S} - \boldsymbol{H}_{o}(\boldsymbol{H}_{o}'\boldsymbol{\Xi}_{o}^{-1}\boldsymbol{H}_{o})^{-1}\boldsymbol{H}_{o}'\boldsymbol{\Xi}_{o}^{-1}]\sqrt{N}(\hat{\boldsymbol{\pi}} - \boldsymbol{\pi}_{o}) + o_{p}(1) \end{split}$$

Therefore, up to  $o_p(1)$ ,

$$\mathbf{\Xi}_{o}^{-1/2}\sqrt{N}\{\hat{\boldsymbol{\pi}}-\mathbf{h}(\hat{\boldsymbol{\theta}})\}=[\mathbf{I}_{S}-\mathbf{\Xi}_{o}^{-1/2}\mathbf{H}_{o}(\mathbf{H}_{o}'\mathbf{\Xi}_{o}^{-1}\mathbf{H}_{o})^{-1}\mathbf{H}_{o}'\mathbf{\Xi}_{o}^{-1/2}]\mathscr{L}\equiv\mathbf{M}_{o}\mathscr{L}$$

where  $\mathscr{Z} \equiv \Xi_o^{-1/2} \sqrt{N} (\hat{\boldsymbol{\pi}} - \boldsymbol{\pi}_o) \stackrel{d}{\to} \text{Normal}(\mathbf{0}, \mathbf{I}_S)$ . But  $\mathbf{M}_o$  is a symmetric idempotent matrix with rank S - P, so  $\{\sqrt{N} [\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})]\}' \Xi_o^{-1} \{\sqrt{N} [\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})]\} \stackrel{a}{\sim} \chi_{S-P}^2$ . Because  $\hat{\boldsymbol{\Xi}}$  is consistent for  $\boldsymbol{\Xi}_o$ , expression (14.75) follows from the asymptotic equivalence lemma. The statistic can also be expressed as

$$\{\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})\}'[\operatorname{Avar}(\hat{\boldsymbol{\pi}})]^{-1}\{\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})\}$$
(14.76)

Testing restrictions on  $\theta_0$  is also straightforward, assuming that we can express the restrictions as  $\theta_0 = \mathbf{d}(\boldsymbol{a}_0)$  for an  $R \times 1$  vector  $\boldsymbol{a}_0$ , R < P. Under these restrictions,  $\boldsymbol{\pi}_0 = \mathbf{h}[\mathbf{d}(\boldsymbol{a}_0)] \equiv \mathbf{g}(\boldsymbol{a}_0)$ . Thus,  $\boldsymbol{a}_0$  can be estimated by minimum distance by solving problem (14.70) with  $\boldsymbol{a}$  in place of  $\boldsymbol{\theta}$  and  $\mathbf{g}(\boldsymbol{a})$  in place of  $\mathbf{h}(\boldsymbol{\theta})$ . The *same* estimator  $\hat{\boldsymbol{\Xi}}$  should be used in both minimization problems. Then it can be shown (under interiority and differentiability) that

{456}------------------------------------------------

$$N[\hat{\boldsymbol{\pi}} - \mathbf{g}(\hat{\boldsymbol{a}})]' \hat{\boldsymbol{\Xi}}^{-1}[\hat{\boldsymbol{\pi}} - \mathbf{g}(\hat{\boldsymbol{a}})] - N[\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})]' \hat{\boldsymbol{\Xi}}^{-1}[\hat{\boldsymbol{\pi}} - \mathbf{h}(\hat{\boldsymbol{\theta}})] \stackrel{a}{\sim} \chi_{P-R}^2$$
(14.77)

when the restrictions on  $\theta_0$  are true.

To illustrate the application of CMD estimation, we reconsider Chamberlain's (1982, 1984) approach to linear, unobserved effects panel data models. (See Section 11.3.2 for the GMM approach.) The key equations are

$$y_{it} = \psi + \mathbf{x}_{i1}\lambda_1 + \dots + \mathbf{x}_{it}(\boldsymbol{\beta} + \lambda_t) + \dots + \mathbf{x}_{iT}\lambda_T + v_{it}$$
(14.78)

where

$$E(v_{it}) = 0, \quad E(\mathbf{x}_i'v_{it}) = \mathbf{0}, \qquad t = 1, 2, \dots, T$$
 (14.79)

(For notational simplicity we do not index the true parameters by "o".) Equation (14.78) embodies the restrictions on the "structural" parameters  $\theta \equiv (\psi, \lambda'_1, \dots, \lambda'_T, \beta')'$ , a  $(1 + TK + K) \times 1$  vector. To apply CMD, write

$$y_{it} = \pi_{t0} + \mathbf{x}_i \boldsymbol{\pi}_t + v_{it}, \qquad t = 1, \dots, T$$

so that the vector  $\boldsymbol{\pi}$  is  $T(1+TK)\times 1$ . When we impose the restrictions,

$$\pi_{t0} = \psi, \, \pi_t = [\lambda_1', \lambda_2', \dots, (\beta + \lambda_t)', \dots, \lambda_T']', \qquad t = 1, \dots, T$$

Therefore, we can write  $\pi = \mathbf{H}\boldsymbol{\theta}$  for a  $(T + T^2K) \times (1 + TK + K)$  matrix **H**. When T = 2,  $\pi$  can be written with restrictions imposed as  $\pi = (\psi, \boldsymbol{\beta}' + \lambda_1', \lambda_2', \psi, \lambda_1', \boldsymbol{\beta}' + \lambda_2')'$ , and so

$$\mathbf{H} = \begin{bmatrix} 1 & \mathbf{0} & \mathbf{0} & \mathbf{0} \\ \mathbf{0} & \mathbf{I}_K & \mathbf{0} & \mathbf{I}_K \\ \mathbf{0} & \mathbf{0} & \mathbf{I}_K & \mathbf{0} \\ 1 & \mathbf{0} & \mathbf{0} & \mathbf{0} \\ \mathbf{0} & \mathbf{I}_K & \mathbf{0} & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & \mathbf{I}_K & \mathbf{I}_K \end{bmatrix}$$

The CMD estimator can be obtained in closed form, once we have  $\hat{\pi}$ ; see Problem 14.7 for the general case.

How should we obtain  $\hat{\pi}$ , the vector of estimates without the restrictions imposed? There is really only one way, and that is OLS for each time period. Condition (14.79) ensures that OLS is consistent and  $\sqrt{N}$ -asymptotically normal. Why not use a system method, in particular, SUR? For one thing, we cannot generally assume that  $\mathbf{v}_i$  satisfies the requisite homoskedasticity assumption that ensures that SUR is more efficient than OLS equation by equation; see Section 11.3.2. Anyway, because the same

{457}------------------------------------------------

regressors appear in each equation and no restrictions are imposed on the  $\pi_t$ , OLS and SUR are identical. Procedures that might use nonlinear functions of  $\mathbf{x}_i$  as instruments are not allowed under condition (14.79).

The estimator  $\hat{\Xi}$  of Avar  $\sqrt{N}(\hat{\pi} - \pi)$  is the robust asymptotic variance for system OLS from Chapter 7:

$$\hat{\mathbf{\Xi}} \equiv \left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{X}_{i}\right)^{-1} \left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{v}}_{i} \hat{\mathbf{v}}_{i}' \mathbf{X}_{i}\right) \left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{X}_{i}\right)^{-1}$$
(14.80)

where  $\mathbf{X}_i = \mathbf{I}_T \otimes (1, \mathbf{x}_i)$  is  $T \times (T + T^2 K)$  and  $\hat{\mathbf{v}}_i$  is the vector of OLS residuals; see also equation (7.26).

Given the linear model with an additive unobserved effect, the overidentification test statistic (14.75) in Chamberlain's setup is a test of the strict exogeneity assumption. Essentially, it is a test of whether the leads and lags of  $\mathbf{x}_t$  appearing in each time period are due to a time-constant unobserved effect  $c_i$ . The number of overidentifying restrictions is  $(T + T^2K) - (1 + TK + K)$ . Perhaps not surprisingly, the minimum distance approach to estimating  $\boldsymbol{\theta}$  is asymptotically equivalent to the GMM procedure we described in Section 11.3.2, as can be reasoned from the work of Angrist and Newey (1991).

One hypothesis of interest concerning  $\theta$  is that  $\lambda_t = 0$ , t = 1, ..., T. Under this hypothesis, the random effects assumption that the unobserved effect  $c_i$  is uncorrelated with  $\mathbf{x}_{it}$  for all t holds. We discussed a test of this assumption in Chapter 10. A more general test is available in the minimum distance setting. First, estimate  $\mathbf{a} \equiv (\psi, \mathbf{\beta}')'$  by minimum distance, using  $\hat{\boldsymbol{\pi}}$  and  $\hat{\boldsymbol{\Xi}}$  in equation (14.80). Second, compute the test statistic (14.77). Chamberlain (1984) gives an empirical example.

Minimum distance methods can be applied to more complicated panel data models, including some of the duration models that we cover in Chapter 20. (See Han and Hausman, 1990.) Van der Klaauw (1996) uses minimum distance estimation in a complicated dynamic model of labor force participation and marital status.