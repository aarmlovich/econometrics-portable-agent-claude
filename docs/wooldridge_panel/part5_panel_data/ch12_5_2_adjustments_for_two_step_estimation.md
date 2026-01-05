# Adjustments for Two-Step Estimation

> Pages: 372-373

In the case of the two-step M-estimator, we may or may not need to adjust the asymptotic variance. If assumption (12.37) holds, estimation is very simple. The most general estimators are expressions (12.48) and (12.49), where  $\hat{\mathbf{s}}_i$ ,  $\hat{\mathbf{H}}_i$ , and  $\hat{\mathbf{A}}_i$  depend on  $\hat{\boldsymbol{\gamma}}$ , but we only compute derivatives with respect to  $\boldsymbol{\theta}$ .

In some cases under assumption (12.37), the analogue of assumption (12.53) holds (with  $\gamma_o = \text{plim } \hat{\gamma}$  appearing in **H** and **s**). If so, the simpler estimators (12.54) and (12.55) are available. In Problem 12.4 you are asked to show this result for weighted NLS when  $\text{Var}(y \mid \mathbf{x}) = \sigma_o^2 h(\mathbf{x}, \gamma_o)$  and  $\gamma_o = \text{plim } \hat{\gamma}$ . The natural third assumption for WNLS is that the variance function is correctly specified:

ASSUMPTION WNLS.3: For some  $\gamma_o \in \Gamma$  and  $\sigma_o^2$ ,  $Var(y | \mathbf{x}) = \sigma_o^2 h(\mathbf{x}, \gamma_o)$ . Further,  $\sqrt{N}(\hat{\mathbf{y}} - \gamma_o) = O_p(1)$ .

Under Assumption WNLS.3, the asymptotic variance of the WNLS estimator is estimated as

$$\hat{\sigma}^2 \left( \sum_{i=1}^N (\nabla_{\theta} \hat{m}_i' \nabla_{\theta} \hat{m}_i) / \hat{h}_i \right)^{-1} \tag{12.59}$$

where  $\hat{h}_i = h(\mathbf{x}_i, \hat{\mathbf{y}})$  and  $\hat{\sigma}^2$  is as in equation (12.57) except that the residual  $\hat{u}_i$  is replaced with the **standardized residual**,  $\hat{u}_i/\sqrt{\hat{h}_i}$ . The sum in expression (12.59) is simply the outer product of the weighted gradients,  $\nabla_{\theta} \hat{m}_i/\sqrt{\hat{h}_i}$ . Thus the NLS formulas can be used but with all quantities weighted by  $1/\sqrt{\hat{h}_i}$ . It is important to remember that expression (12.59) is not valid without Assumption WNLS.3.

When assumption (12.37) is violated, the asymptotic variance estimator of  $\hat{\theta}$  must account for the asymptotic variance of  $\hat{\gamma}$ ; we must estimate equation (12.41). We already know how to consistently estimate  $\mathbf{A}_0$ : use expression (12.42) or (12.44) where  $\hat{\gamma}$  is also plugged in. Estimation of  $\mathbf{D}_0$  is also straightforward. First, we need to estimate  $\mathbf{F}_0$ . An estimator that is always available is

$$\hat{\mathbf{F}} = N^{-1} \sum_{i=1}^{N} \nabla_{\gamma} \mathbf{s}_{i}(\hat{\boldsymbol{\theta}}; \hat{\boldsymbol{\gamma}})$$
(12.60)

In cases with conditioning variables, such as nonlinear least squares, a simpler estimator can be obtained by computing  $E[\nabla_{\gamma} \mathbf{s}(\mathbf{w}_i, \boldsymbol{\theta}_0, \gamma^*) | \mathbf{x}_i]$ , replacing  $(\boldsymbol{\theta}_0, \gamma^*)$  with  $(\hat{\boldsymbol{\theta}}, \hat{\gamma})$ , and using this in place of  $\nabla_{\gamma} \mathbf{s}_i(\hat{\boldsymbol{\theta}}; \hat{\gamma})$ . Next, replace  $\mathbf{r}_i(\gamma^*)$  with  $\hat{\mathbf{r}}_i \equiv \mathbf{r}_i(\hat{\gamma})$ . Then

{373}------------------------------------------------

$$\hat{\mathbf{D}} \equiv N^{-1} \sum_{i=1}^{N} \hat{\mathbf{g}}_i \hat{\mathbf{g}}_i' \tag{12.61}$$

is consistent for  $\mathbf{D}_{o}$ , where  $\hat{\mathbf{g}}_{i} = \hat{\mathbf{s}}_{i} + \hat{\mathbf{F}}\hat{\mathbf{r}}_{i}$ . The asymptotic variance of the two-step M-estimator can be obtained as in expression (12.48) or (12.49), but where  $\hat{\mathbf{s}}_{i}$  is replaced with  $\hat{\mathbf{g}}_{i}$ .