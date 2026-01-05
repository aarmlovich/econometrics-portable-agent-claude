# 1. Run a multivariate regression

> Pages: 379-391

$$\nabla_{\delta}\tilde{m}_i \text{ on } \nabla_{\beta}\tilde{m}_i, \qquad i = 1, 2, \dots, N$$
 (12.74)

and save the  $1 \times Q$  vector residuals, say  $\tilde{\mathbf{r}}_i$ . Then, for each i, form  $\tilde{u}_i \tilde{\mathbf{r}}_i$ . (That is, multiply  $\tilde{u}_i$  by each element of  $\tilde{\mathbf{r}}_i$ .)

2.  $LM = N - SSR_0 = NR_0^2$  from the regression

1 on 
$$\tilde{u}_i \tilde{\mathbf{r}}_i$$
,  $i = 1, 2, \dots, N$  (12.75)

where SSR<sub>0</sub> is the usual sum of squared residuals. This step produces a statistic that has a limiting  $\chi_Q^2$  distribution whether or not Assumption NLS.3 holds. See Wooldridge (1991a) for more discussion.

We can illustrate the heteroskedasticity-robust test using the preceding exponential model. Regression (12.74) is the same as regressing each of  $(\mathbf{x}_i\tilde{\boldsymbol{\beta}})^2\tilde{m}_i$  and  $(\mathbf{x}_i\tilde{\boldsymbol{\beta}})^3\tilde{m}_i$  onto  $\mathbf{x}_i\tilde{m}_i$ , and saving the residuals  $\tilde{r}_{i1}$  and  $\tilde{r}_{i2}$ , respectively (N each). Then, regression (12.75) is simply 1 on  $\tilde{u}_i\tilde{r}_{i1}$ ,  $\tilde{u}_i\tilde{r}_{i2}$ . The number of regressors in the final regression of the robust test is always the same as the degrees of freedom of the test.

Finally, these procedures are easily modified for WNLS. Simply multiply both  $\tilde{u}_i$  and  $\nabla_{\theta}\tilde{m}_i$  by  $1/\sqrt{\tilde{h}_i}$ , where the variance estimates  $\tilde{h}_i$  are based on the null model (so we use a  $\sim$  rather than a  $\wedge$ ). The nonrobust LM statistic that maintains Assumption WNLS.3 is obtained as in regression (12.72). The robust form, which allows  $\operatorname{Var}(y \mid \mathbf{x}) \neq \sigma_0^2 h(\mathbf{x}, \gamma_0)$ , follows exactly as in regressions (12.74) and (12.75).

The invariance issue for the score statistic is somewhat complicated, but several results are known. First, it is easy to see that the outer product form of the statistic is invariant to differentiable reparameterizations. Write  $\phi = \mathbf{g}(\theta)$  as a twice continuously differentiable, invertible reparameterization; thus the  $P \times P$  Jacobian of  $\mathbf{g}$ ,

{380}------------------------------------------------

 $\mathbf{G}(\boldsymbol{\theta})$ , is nonsingular for all  $\boldsymbol{\theta} \in \mathbf{\Theta}$ . The objective function in terms of  $\boldsymbol{\phi}$  is  $q^g(\mathbf{w}, \boldsymbol{\phi})$ , and we must have  $q^g[\mathbf{w}, \mathbf{g}(\boldsymbol{\theta})] = q(\mathbf{w}, \boldsymbol{\theta})$  for all  $\boldsymbol{\theta} \in \mathbf{\Theta}$ . Differentiating and transposing gives  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta}) = \mathbf{G}(\boldsymbol{\theta})'\mathbf{s}^g[\mathbf{w}, \mathbf{g}(\boldsymbol{\theta})]$ , where  $\mathbf{s}^g(\mathbf{w}, \boldsymbol{\phi})$  is the score of  $q^g[\mathbf{w}, \boldsymbol{\phi}]$ . If  $\tilde{\boldsymbol{\phi}}$  is the restricted estimator of  $\boldsymbol{\phi}$ , then  $\tilde{\boldsymbol{\phi}} = \mathbf{g}(\tilde{\boldsymbol{\theta}})$ , and so, for each observation i,  $\tilde{\mathbf{s}}_i^g = (\tilde{\mathbf{G}}')^{-1}\tilde{\mathbf{s}}_i$ . Plugging this equation into the LM statistic in equation (12.69), with  $\tilde{\mathbf{M}}$  chosen as the outer product form, shows that the statistic based on  $\tilde{\mathbf{s}}_i^g$  is identical to that based on  $\tilde{\mathbf{s}}_i$ .

Score statistics based on the estimated Hessian are not generally invariant to reparameterization because they can involve second derivatives of the function  $\mathbf{g}(\boldsymbol{\theta})$ ; see Davidson and MacKinnon (1993, Section 13.6) for details. However, when  $\mathbf{w}$  partitions as  $(\mathbf{x}, \mathbf{y})$ , score statistics based on the expected Hessian (conditional on  $\mathbf{x}$ ),  $\mathbf{A}(\mathbf{x}, \boldsymbol{\theta})$ , are often invariant. In Chapter 13 we will see that this is always the case for conditional maximum likelihood estimation. Invariance also holds for NLS and WNLS for both the usual and robust LM statistics because any reparameterization comes through the conditional mean. Predicted values and residuals are invariant to reparameterization, and the statistics obtained from regressions (12.72) and (12.75) only involve the residuals and first derivatives of the conditional mean function. As in the usual outer product LM statistic, the Jacobian in the first derivative cancels out.

# 12.6.3 Tests Based on the Change in the Objective Function

When both the restricted and unrestricted models are easy to estimate, a test based on the change in the objective function can greatly simplify the mechanics of obtaining a test statistic: we only need to obtain the value of the objective function with and without the restrictions imposed. However, the computational simplicity comes at a price in terms of robustness. Unlike the Wald and score tests, a test based on the change in the objective function *cannot* be made robust to general failure of assumption (12.53). Therefore, throughout this subsection we assume that the generalized information matrix equality holds. Because the minimized objective function is invariant with respect to any reparameterization, the test statistic is invariant.

In the context of two-step estimators, we must also assume that  $\hat{\gamma}$  has no effect on the asymptotic distribution of the M-estimator. That is, we maintain assumption (12.37) when nuisance parameter estimates appear in the objective function (see Problem 12.8).

We first consider the case where  $\sigma_o^2 = 1$ , so that  $\mathbf{B}_o = \mathbf{A}_o$ . Using a second-order Taylor expansion,

$$\sum_{i=1}^{N} q(\mathbf{w}_i, \tilde{\boldsymbol{\theta}}) - \sum_{i=1}^{N} q(\mathbf{w}_i, \hat{\boldsymbol{\theta}}) = \sum_{i=1}^{N} \mathbf{s}_i(\hat{\boldsymbol{\theta}}) + (1/2)(\tilde{\boldsymbol{\theta}} - \hat{\boldsymbol{\theta}})' \left(\sum_{i=1}^{N} \ddot{\mathbf{H}}_i\right)(\tilde{\boldsymbol{\theta}} - \hat{\boldsymbol{\theta}})$$


{391}------------------------------------------------

where the error  $u_i$  is *independent* of  $\mathbf{x}_i$ , we first compute the NLS estimate  $\hat{\boldsymbol{\theta}}$  and the NLS residuals,  $\hat{u}_i = y_i - m(\mathbf{x}_i, \hat{\boldsymbol{\theta}}), i = 1, 2, \dots, N$ . Then, using the procedure described for the nonparametric bootstrap, a bootstrap sample of residuals,  $\{\hat{u}_i^{(b)}: i = 1, 2, \dots, N\}$ , is obtained, and we compute  $y_i^{(b)} = m(\mathbf{x}_i, \hat{\boldsymbol{\theta}}) + \hat{u}_i^{(b)}$ . Using the generated data  $\{(\mathbf{x}_i, y_i^{(b)}): i = 1, 2, \dots, N\}$ , we compute the NLS estimate,  $\hat{\boldsymbol{\theta}}^{(b)}$ . This procedure is called the **nonparametric residual bootstrap**. (We resample the residuals and use these to generate a sample on the dependent variable, but we do not resample the conditioning variables,  $\mathbf{x}_i$ .) If the model is nonlinear in  $\boldsymbol{\theta}$ , this method can be computationally demanding because we want  $\boldsymbol{B}$  to be several hundred, if not several thousand. Nonetheless, such procedures are becoming more and more feasible as computational speed increases. When  $u_i$  has zero conditional mean  $[E(u_i | \mathbf{x}_i) = 0]$  but is heteroskedastic  $[Var(u_i | \mathbf{x}_i)$  depends on  $\mathbf{x}_i]$ , alternative sampling methods, in particular the **wild bootstrap**, can be used to obtain heteroskedastic-consistent standard errors. See, for example, Horowitz (in press).

For certain test statistics, the bootstrap can be shown to improve upon the approximation provided by the first-order asymptotic theory that we treat in this book. A detailed treatment of the bootstrap, including discussions of when it works and when it does not, is given in Horowitz (in press).