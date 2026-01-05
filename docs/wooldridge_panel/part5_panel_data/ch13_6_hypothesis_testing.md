# Hypothesis Testing

> Pages: 408-409

Given the asymptotic standard errors, it is easy to form asymptotic t statistics for testing single hypotheses. These t statistics are asymptotically distributed as standard normal.

The three tests covered in Chapter 12 are immediately applicable to the MLE case. Since the information matrix equality holds when the density is correctly specified, we need only consider the simplest forms of the test statistics. The Wald statistic is given in equation (12.63), and the conditions sufficient for it to have a limiting chi-square distribution are discussed in Section 12.6.1.

Define the log-likelihood function for the entire sample by  $\mathcal{L}(\theta) \equiv \sum_{i=1}^{N} \ell_i(\theta)$ . Let  $\hat{\theta}$  be the unrestricted estimator, and let  $\tilde{\theta}$  be the estimator with the Q nonredundant constraints imposed. Then, under the regularity conditions discussed in Section 12.6.3, the **likelihood ratio (LR) statistic**,

$$LR \equiv 2[\mathcal{L}(\hat{\boldsymbol{\theta}}) - \mathcal{L}(\tilde{\boldsymbol{\theta}})] \tag{13.35}$$

is distributed asymptotically as  $\chi_Q^2$  under  $H_0$ . As with the Wald statistic, we cannot use LR as approximately  $\chi_Q^2$  when  $\theta_0$  is on the boundary of the parameter set. The LR statistic is very easy to compute once the restricted and unrestricted models have been estimated, and the LR statistic is invariant to reparameterizing the conditional density.

The score or LM test is based on the restricted estimation only. Let  $\mathbf{s}_i(\tilde{\boldsymbol{\theta}})$  be the  $P \times 1$  score of  $\ell_i(\boldsymbol{\theta})$  evaluated at the restricted estimates  $\tilde{\boldsymbol{\theta}}$ . That is, we compute the partial derivatives of  $\ell_i(\boldsymbol{\theta})$  with respect to each of the P parameters, but then we

{409}------------------------------------------------

evaluate this vector of partials at the restricted estimates. Then, from Section 12.6.2 and the information matrix equality, the statistics

$$\left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right)' \left(-\sum_{i=1}^{N} \tilde{\mathbf{H}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right), \qquad \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right)' \left(\sum_{i=1}^{N} \tilde{\mathbf{A}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right), \qquad \text{and}$$

$$\left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right)' \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i} \tilde{\mathbf{s}}_{i}'\right)^{-1} \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right)$$

$$(13.36)$$

have limiting  $\chi_Q^2$  distributions under  $H_0$ . As we know from Section 12.6.2, the first statistic is not invariant to reparameterizations, but the outer product statistic is. In addition, using the conditional information matrix equality, it can be shown that the LM statistic based on  $\tilde{\mathbf{A}}_i$  is invariant to reparameterization. Davidson and MacKinnon (1993, Section 13.6) show invariance in the case of unconditional maximum likelihood. Invariance holds in the more general conditional ML setup, with  $\mathbf{x}_i$  containing any conditioning variables; see Problem 13.5. We have already used the expected Hessian form of the LM statistic for nonlinear regression in Section 12.6.2. We will use it in several applications in Part IV, including binary response models and Poisson regression models. In these examples, the statistic can be computed conveniently using auxiliary regressions based on weighted residuals.

Because the unconditional information matrix equality holds, we know from Section 12.6.4 that the three classical statistics have the same limiting distribution under local alternatives. Therefore, either small-sample considerations, invariance, or computational issues must be used to choose among the statistics.