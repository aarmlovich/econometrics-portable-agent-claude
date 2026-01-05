# Testing Classical Hypotheses

> Pages: 212-214

Testing hypotheses after GMM estimation is straightforward. Let  $\hat{\boldsymbol{\beta}}$  denote a GMM estimator, and let  $\hat{\mathbf{V}}$  denote its estimated asymptotic variance. Although the following analysis can be made more general, in most applications we use an optimal GMM estimator. Without Assumption SIV.5, the weighting matrix would be expression (8.32) and  $\hat{\mathbf{V}}$  would be as in expression (8.33). This can be used for computing t statistics by obtaining the asymptotic standard errors (square roots of the diagonal elements of  $\hat{\mathbf{V}}$ ). Wald statistics of linear hypotheses of the form  $H_0$ :  $\mathbf{R}\boldsymbol{\beta} = \mathbf{r}$ , where  $\mathbf{R}$  is a  $Q \times K$  matrix with rank Q, are obtained using the same statistic we have already seen several times. Under Assumption SIV.5 we can use the 3SLS estimator and its asymptotic variance estimate in equation (8.41). For testing general system hypotheses we would probably not use the 2SLS estimator because its asymptotic variance is more complicated unless we make very restrictive assumptions.

An alternative method for testing linear restrictions uses a statistic based on the difference in the GMM objective function with and without the restrictions imposed. To apply this statistic, we must assume that the GMM estimator uses the optimal weighting matrix, so that  $\hat{\mathbf{W}}$  consistently estimates  $[\operatorname{Var}(\mathbf{Z}_i'\mathbf{u}_i)]^{-1}$ . Then, from Lemma 3.8,

$$\left(N^{-1/2} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{u}_{i}\right)' \hat{\mathbf{W}} \left(N^{-1/2} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{u}_{i}\right) \stackrel{a}{\sim} \chi_{L}^{2}$$

$$(8.44)$$

since  $\mathbf{Z}_i'\mathbf{u}_i$  is an  $L \times 1$  vector with zero mean and variance  $\Lambda$ . If  $\hat{\mathbf{W}}$  does not consistently estimate  $[\operatorname{Var}(\mathbf{Z}_i'\mathbf{u}_i)]^{-1}$ , then result (8.44) is false, and the following method does not produce an asymptotically chi-square statistic.

{213}------------------------------------------------

Let  $\hat{\beta}$  again be the GMM estimator, using optimal weighting matrix  $\hat{\mathbf{W}}$ , obtained without imposing the restrictions. Let  $\tilde{\beta}$  be the GMM estimator using the *same* weighting matrix  $\hat{\mathbf{W}}$  but obtained with the Q linear restrictions imposed. The restricted estimator can always be obtained by estimating a linear model with K-Q rather than K parameters. Define the unrestricted and restricted residuals as  $\hat{\mathbf{u}}_i \equiv \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}}$  and  $\tilde{\mathbf{u}}_i \equiv \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}}$ , respectively. It can be shown that, under  $H_0$ , the GMM distance statistic has a limiting chi-square distribution:

$$\left[ \left( \sum_{i=1}^{N} \mathbf{Z}_{i}' \tilde{\mathbf{u}}_{i} \right)' \hat{\mathbf{W}} \left( \sum_{i=1}^{N} \mathbf{Z}_{i}' \tilde{\mathbf{u}}_{i} \right) - \left( \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{u}}_{i} \right)' \hat{\mathbf{W}} \left( \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{u}}_{i} \right) \right] / N \stackrel{a}{\sim} \chi_{Q}^{2}$$
(8.45)

See, for example, Hansen (1982) and Gallant (1987). The GMM distance statistic is simply the difference in the criterion function (8.23) evaluated at the restricted and unrestricted estimates, divided by the sample size, N. For this reason, expression (8.45) is called a **criterion function statistic**. Because constrained minimization cannot result in a smaller objective function than unconstrained minimization, expression (8.45) is always nonnegative and usually strictly positive.

Under Assumption SIV.5 we can use the 3SLS estimator, in which case expression (8.45) becomes

$$\left(\sum_{i=1}^{N} \mathbf{Z}_{i}'\tilde{\mathbf{u}}_{i}\right)' \left(\sum_{i=1}^{N} \mathbf{Z}_{i}'\hat{\mathbf{\Omega}}\mathbf{Z}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \mathbf{Z}_{i}'\tilde{\mathbf{u}}_{i}\right) - \left(\sum_{i=1}^{N} \mathbf{Z}_{i}'\hat{\mathbf{u}}_{i}\right)' \left(\sum_{i=1}^{N} \mathbf{Z}_{i}'\hat{\mathbf{\Omega}}\mathbf{Z}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \mathbf{Z}_{i}'\hat{\mathbf{u}}_{i}\right)$$

$$(8.46)$$

where  $\hat{\Omega}$  would probably be computed using the 2SLS residuals from estimating the unrestricted model. The division by N has disappeared because of the definition of  $\hat{\mathbf{W}}$ ; see equation (8.35).

Testing nonlinear hypotheses is easy once the unrestricted estimator  $\hat{\beta}$  has been obtained. Write the null hypothesis as

$$\mathbf{H}_0: \mathbf{c}(\boldsymbol{\beta}) = \mathbf{0} \tag{8.47}$$

where  $\mathbf{c}(\boldsymbol{\beta}) \equiv [c_1(\boldsymbol{\beta}), c_2(\boldsymbol{\beta}), \dots, c_Q(\boldsymbol{\beta})]'$  is a  $Q \times 1$  vector of functions. Let  $\mathbf{C}(\boldsymbol{\beta})$  denote the  $Q \times K$  Jacobian of  $\mathbf{c}(\boldsymbol{\beta})$ . Assuming that rank  $\mathbf{C}(\boldsymbol{\beta}) = Q$ , the Wald statistic is

$$W = \mathbf{c}(\hat{\boldsymbol{\beta}})'(\hat{\mathbf{C}}\hat{\mathbf{V}}\hat{\mathbf{C}}')^{-1}\mathbf{c}(\hat{\boldsymbol{\beta}})$$
(8.48)

where  $\hat{\mathbf{C}} \equiv \mathbf{C}(\hat{\boldsymbol{\beta}})$  is the Jacobian evaluated at the GMM estimate  $\hat{\boldsymbol{\beta}}$ . Under  $H_0$ , the Wald statistic has an asymptotic  $\chi_O^2$  distribution.

{214}------------------------------------------------