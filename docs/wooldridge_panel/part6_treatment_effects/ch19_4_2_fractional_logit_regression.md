# Fractional Logit Regression

> Pages: 668-670

Quasi-likelihood methods are also available when y is a variable restricted to the unit interval, [0,1]. {By rescaling, we can cover the case where y is restricted to the interval [a,b] for known constants a < b. The transformation is (y-a)/(b-a).} Examples include fraction of income contributed to charity, fraction of weekly hours spent working, proportion of a firm's total capitalization accounted for by debt capital, and high school graduation rates. In some cases, each  $y_i$  might be obtained by dividing a count variable by an upper bound,  $n_i$ .

{669}------------------------------------------------

Given explanatory variables  $\mathbf{x}$ , a linear model for  $\mathrm{E}(y | \mathbf{x})$  has the same strengths and weaknesses as the linear probability model for binary y. When y is *strictly* between zero and one, a popular alternative is to assume that the **log-odds transformation**,  $\log[y/(1-y)]$ , has a conditional expectation of the form  $\mathbf{x}\boldsymbol{\beta}$ . The motivation for using  $\log[y/(1-y)]$  as a dependent variable in a linear model is that  $\log[y/(1-y)]$  ranges over all real values as y ranges between zero and one. This approach leads to estimation of  $\boldsymbol{\beta}$  by OLS. Unfortunately, using the log-odds transformation has two drawbacks. First, it cannot be used directly if y takes on the boundary values, zero and one. While we can always use adjustments for the boundary values, such adjustments are necessarily arbitrary. Second, even if y is strictly inside the unit interval,  $\boldsymbol{\beta}$  is difficult to interpret: without further assumptions, it is not possible to recover an estimate of  $\mathrm{E}(y | \mathbf{x})$ , and with further assumptions, it is still nontrivial to estimate  $\mathrm{E}(y | \mathbf{x})$ . See Papke and Wooldridge (1996) and Problem 19.8 for further discussion.

An approach that avoids both these problems is to model  $E(y | \mathbf{x})$  as a logistic function:

$$E(y \mid \mathbf{x}) = \exp(\mathbf{x}\boldsymbol{\beta})/[1 + \exp(\mathbf{x}\boldsymbol{\beta})]$$
(19.36)

This model ensures that predicted values for y are in (0,1) and that the effect of any  $x_j$  on  $E(y | \mathbf{x})$  diminishes as  $\mathbf{x}\boldsymbol{\beta} \to \infty$ . Just as in the binary logit model,  $\partial E(y | \mathbf{x})/\partial x_j = \beta_j g(\mathbf{x}\boldsymbol{\beta})$ , where  $g(z) = \exp(z)/[1 + \exp(z)]^2$ . In applications, the partial effects should be evaluated at the  $\hat{\beta}_j$  and interesting values of  $\mathbf{x}$ . Plugging in the sample averages,  $\overline{\mathbf{x}}$ , makes the partial effects from equation (19.36) roughly comparable to the coefficients from a linear regression for  $E(y | \mathbf{x})$ :  $\hat{\gamma}_j \approx \hat{\beta}_j g(\overline{\mathbf{x}}\hat{\boldsymbol{\beta}})$ , where the  $\hat{\gamma}_j$  are the OLS estimates from the linear regression of y on  $\mathbf{x}$ .

Given equation (19.36), one approach to estimating  $\beta$  is nonlinear least squares, as we discussed in Chapter 12. However, the assumption that implies relative efficiency of NLS—namely,  $\text{Var}(y | \mathbf{x}) = \sigma^2$ —is unlikely to hold for fractional y. A method that is just as robust [in the sense that it consistently estimates  $\beta$  under assumption (19.36) only] is quasi-MLE, where the quasi-likelihood function is the binary choice log likelihood. Therefore, quasi-log likelihood for observation i is exactly as in equation (15.17) [with  $G(\cdot)$  the logistic function], although  $y_i$  can be any value in [0, 1]. The mechanics of obtaining  $\hat{\beta}$  are identical to the binary response case.

Inference is complicated by the fact that the binary response density cannot be the actual density of y given  $\mathbf{x}$ . Generally, a fully robust variance matrix estimator and test statistics should be obtained. These are gotten by applying the formulas for the binomial case with  $n_i \equiv 1$  and  $p(\mathbf{x}, \boldsymbol{\beta}) \equiv \exp(\mathbf{x}\boldsymbol{\beta})/[1 + \exp(\mathbf{x}\boldsymbol{\beta})]$ . The GLM assumption for fractional logit regression is given in assumption (19.34) with  $n_i = 1$ . See

{670}------------------------------------------------

Papke and Wooldridge (1996) for more details, as well as suggestions for specification tests and for an application to participation rates in 401(k) pension plans.