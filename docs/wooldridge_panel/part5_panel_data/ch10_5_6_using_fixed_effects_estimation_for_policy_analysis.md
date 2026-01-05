# Using Fixed Effects Estimation for Policy Analysis

> Pages: 290-291

There are other ways to interpret the fixed effects transformation to illustrate why fixed effects is useful for policy analysis and program evaluation. Consider the model

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + v_{it} = \mathbf{z}_{it}\boldsymbol{\gamma} + \delta w_{it} + v_{it}$$

where  $v_{it}$  may or may not contain an unobserved effect. Let  $w_{it}$  be the policy variable of interest; it could be continuous or discrete. The vector  $\mathbf{z}_{it}$  contains other controls that might be correlated with  $w_{it}$ , including time-period dummy variables.

As an exercise, you can show that sufficient for consistency of fixed effects, along with the rank condition FE.2, is


{291}------------------------------------------------

$$E[\mathbf{x}'_{it}(v_{it}-\bar{v}_i)]=\mathbf{0}, \qquad t=1,2,\ldots,T$$

This assumption shows that each element of xit, and in particular the policy variable wit, can be correlated with vi. What fixed effects requires for consistency is that wit be uncorrelated with deviations of vit from the average over the time period. So a policy variable, such as program participation, can be systematically related to the persistent component in the error vit as measured by vi. It is for this reason that FE is often superior to be pooled OLS or random effects for applications where participation in a program is determined by preprogram attributes that also affect yit.