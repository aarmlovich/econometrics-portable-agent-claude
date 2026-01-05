# **10.14.** Suppose that we have the unobserved effects model

> Pages: 309-310

$$y_{it} = \alpha + \mathbf{x}_{it}\boldsymbol{\beta} + \mathbf{z}_i\boldsymbol{\gamma} + h_i + u_{it}$$

where the  $\mathbf{x}_{it}(1 \times K)$  are time-varying, the  $\mathbf{z}_{i}(1 \times M)$  are time-constant,  $\mathrm{E}(u_{it} \mid \mathbf{x}_{i}, \mathbf{z}_{i}, h_{i}) = 0$ ,  $t = 1, \ldots, T$ , and  $\mathrm{E}(h_{i} \mid \mathbf{x}_{i}, \mathbf{z}_{i}) = 0$ . Let  $\sigma_{h}^{2} = \mathrm{Var}(h_{i})$  and  $\sigma_{u}^{2} = \mathrm{Var}(u_{it})$ . If we estimate  $\boldsymbol{\beta}$  by fixed effects, we are estimating the equation  $y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + c_{i} + u_{it}$ , where  $c_{i} = \alpha + \mathbf{z}_{i}\boldsymbol{\gamma} + h_{i}$ .

- a. Find  $\sigma_c^2 \equiv \text{Var}(c_i)$ . Show that  $\sigma_c^2$  is at least as large as  $\sigma_h^2$ , and usually strictly larger.
- b. Explain why estimation of the model by fixed effects will lead to a larger estimated variance of the unobserved effect than if we estimate the model by random effects. Does this result make intuitive sense?

{310}------------------------------------------------

This chapter continues our treatment of linear, unobserved effects panel data models. We first cover estimation of models where the strict exogeneity Assumption FE.1 fails but sequential moment conditions hold. A simple approach to consistent estimation involves differencing combined with instrumental variables methods. We also cover models with individual slopes, where unobservables can interact with explanatory variables, and models where some of the explanatory variables are assumed to be orthogonal to the unobserved effect while others are not.

The final section in this chapter briefly covers some non-panel-data settings where unobserved effects models and panel data estimation methods can be used.