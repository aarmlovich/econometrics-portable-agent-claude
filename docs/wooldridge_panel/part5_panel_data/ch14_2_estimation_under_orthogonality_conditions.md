# Estimation under Orthogonality Conditions

> Pages: 437-439

In Chapter 8 we saw how linear systems of equations can be estimated by GMM under certain orthogonality conditions. In general applications, the moment conditions (14.1) almost always arise from assumptions that disturbances are uncorrelated with exogenous variables. For a  $G \times 1$  vector  $\mathbf{r}(\mathbf{w}_i, \boldsymbol{\theta})$  and a  $G \times L$  matrix  $\mathbf{Z}_i$ , assume that  $\boldsymbol{\theta}_0$  satisfies

$$E[\mathbf{Z}_{i}^{\prime}\mathbf{r}(\mathbf{w}_{i},\boldsymbol{\theta}_{o})] = \mathbf{0} \tag{14.22}$$

The vector function  $\mathbf{r}(\mathbf{w}_i, \boldsymbol{\theta})$  can be thought of as a **generalized residual function**. The matrix  $\mathbf{Z}_i$  is usually called the **matrix of instruments**. Equation (14.22) is a special case of equation (14.1) with  $\mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}) \equiv \mathbf{Z}_i' \mathbf{r}(\mathbf{w}_i, \boldsymbol{\theta})$ . In what follows, write  $\mathbf{r}_i(\boldsymbol{\theta}) \equiv \mathbf{r}(\mathbf{w}_i, \boldsymbol{\theta})$ .

Identification requires that  $\theta_0$  be the only  $\theta \in \Theta$  such that equation (14.22) holds. Condition e of the asymptotic normality result Theorem 14.2 requires that rank  $\mathrm{E}[\mathbf{Z}_i'\nabla_\theta\mathbf{r}_i(\theta_0)] = P$  (necessary is  $L \geq P$ ). Thus, while  $\mathbf{Z}_i$  must be orthogonal to  $\mathbf{r}_i(\theta_0)$ ,  $\mathbf{Z}_i$  must be sufficiently correlated with the  $G \times P$  Jacobian,  $\nabla_\theta\mathbf{r}_i(\theta_0)$ . In the linear case where  $\mathbf{r}(\mathbf{w}_i, \theta) = \mathbf{y}_i - \mathbf{X}_i\theta$ , this requirement reduces to  $\mathrm{E}(\mathbf{Z}_i'\mathbf{X}_i)$  having full column rank, which is simply Assumption SIV.2 in Chapter 8.

Given the instruments  $\mathbf{Z}_i$ , the efficient estimator can be obtained as in Section 14.1. A preliminary estimator  $\hat{\boldsymbol{\theta}}$  is usually obtained with

$$\hat{\mathbf{\Xi}} \equiv \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{Z}_{i} \right)^{-1} \tag{14.23}$$

so that  $\hat{\hat{\theta}}$  solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{r}_{i}(\boldsymbol{\theta}) \right]' \left[ N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{Z}_{i} \right]^{-1} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{r}_{i}(\boldsymbol{\theta}) \right]$$
(14.24)

{438}------------------------------------------------

The solution to problem (14.24) is called the **nonlinear system 2SLS estimator**; it is an example of a **nonlinear instrumental variables estimator**.

From Section 14.1, we know that the nonlinear system 2SLS estimator is guaranteed to be the efficient GMM estimator if for some  $\sigma_0^2 > 0$ ,

$$\mathrm{E}[\mathbf{Z}_{i}^{\prime}\mathbf{r}_{i}(\boldsymbol{\theta}_{\mathrm{o}})\mathbf{r}_{i}(\boldsymbol{\theta}_{\mathrm{o}})^{\prime}\mathbf{Z}_{i}] = \sigma_{\mathrm{o}}^{2}\mathrm{E}(\mathbf{Z}_{i}^{\prime}\mathbf{Z}_{i})$$

Generally, this is a strong assumption. Instead, we can obtain the minimum chi-square estimator by obtaining

$$\hat{\mathbf{\Lambda}} = N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{r}_{i} (\hat{\boldsymbol{\theta}}) \mathbf{r}_{i} (\hat{\boldsymbol{\theta}})' \mathbf{Z}_{i}$$
(14.25)

and using this in expression (14.17).

In some cases more structure is available that leads to a three-stage least squares estimator. In particular, suppose that

$$E[\mathbf{Z}_{i}'\mathbf{r}_{i}(\boldsymbol{\theta}_{o})\mathbf{r}_{i}(\boldsymbol{\theta}_{o})'\mathbf{Z}_{i}] = E(\mathbf{Z}_{i}'\boldsymbol{\Omega}_{o}\mathbf{Z}_{i})$$
(14.26)

where  $\Omega_0$  is the  $G \times G$  matrix

$$\mathbf{\Omega}_{o} = \mathrm{E}[\mathbf{r}_{i}(\boldsymbol{\theta}_{o})\mathbf{r}_{i}(\boldsymbol{\theta}_{o})'] \tag{14.27}$$

When  $E[\mathbf{r}_i(\boldsymbol{\theta}_o)] = \mathbf{0}$ , as is almost always the case under assumption (14.22),  $\Omega_o$  is the variance matrix of  $\mathbf{r}_i(\boldsymbol{\theta}_o)$ . As in Chapter 8, assumption (14.26) is a kind of system homoskedasticity assumption.

By iterated expectations, a sufficient condition for assumption (14.26) is

$$E[\mathbf{r}_{i}(\boldsymbol{\theta}_{o})\mathbf{r}_{i}(\boldsymbol{\theta}_{o})' \mid \mathbf{Z}_{i}] = \mathbf{\Omega}_{o}$$
(14.28)

However, assumption (14.26) can hold in cases where assumption (14.28) does not. If assumption (14.26) holds, then  $\Lambda_o$  can be estimated as

$$\hat{\mathbf{\Lambda}} = N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{\Omega}} \mathbf{Z}_{i}$$
 (14.29)

where

$$\hat{\mathbf{\Omega}} = N^{-1} \sum_{i=1}^{N} \mathbf{r}_i(\hat{\boldsymbol{\theta}}) \mathbf{r}_i(\hat{\boldsymbol{\theta}})$$
(14.30)

and  $\hat{\theta}$  is a preliminary estimator. The resulting GMM estimator is usually called the **nonlinear 3SLS (N3SLS) estimator**. The name is a holdover from the traditional

{439}------------------------------------------------

3SLS estimator in linear systems of equations; there are not really three estimation steps. We should remember that nonlinear 3SLS is generally inefficient when assumption (14.26) fails.

The Wald statistic and the QLR statistic can be computed as in Section 14.1. In addition, a score statistic is sometimes useful. Let  $\tilde{\theta}$  be a preliminary inefficient estimator with Q restrictions imposed. The estimator  $\tilde{\theta}$  would usually come from problem (14.24) subject to the restrictions  $\mathbf{c}(\theta) = \mathbf{0}$ . Let  $\tilde{\Lambda}$  be the estimated weighting matrix from equation (14.25) or (14.29), based on  $\tilde{\theta}$ . Let  $\tilde{\theta}$  be the minimum chisquare estimator using weighting matrix  $\tilde{\Lambda}^{-1}$ . Then the score statistic is based on the limiting distribution of the score of the unrestricted objective function evaluated at the restricted estimates, properly standardized:

$$\left[ N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}^{\prime} \nabla_{\theta} \mathbf{r}_{i}(\tilde{\boldsymbol{\theta}}) \right]^{\prime} \tilde{\mathbf{\Lambda}}^{-1} \left[ N^{-1/2} \sum_{i=1}^{N} \mathbf{Z}_{i}^{\prime} \mathbf{r}_{i}(\tilde{\boldsymbol{\theta}}) \right]$$
(14.31)

Let  $\tilde{\mathbf{s}}_i \equiv \tilde{\mathbf{G}}'\tilde{\mathbf{A}}^{-1}\mathbf{Z}_i'\tilde{\mathbf{r}}_i$ , where  $\tilde{\mathbf{G}}$  is the first matrix in expression (14.31), and let  $\mathbf{s}_i^o \equiv \mathbf{G}_o'\mathbf{A}_o^{-1}\mathbf{Z}_i'\mathbf{r}_i^o$ . Then, following the proof in Section 12.6.2, it can be shown that equation (12.67) holds with  $\mathbf{A}_o \equiv \mathbf{G}_o'\mathbf{A}_o^{-1}\mathbf{G}_o$ . Further, since  $\mathbf{B}_o = \mathbf{A}_o$  for the minimum chisquare estimator, we obtain

$$LM = \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right)' \tilde{\mathbf{A}}^{-1} \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right) / N$$
(14.32)

where  $\tilde{\mathbf{A}} = \tilde{\mathbf{G}}'\tilde{\mathbf{A}}^{-1}\tilde{\mathbf{G}}$ . Under  $\mathbf{H}_0$  and the usual regularity conditions, LM has a limiting  $\chi_Q^2$  distribution.