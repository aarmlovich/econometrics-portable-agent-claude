# Testing in Binary Response Index Models

> Pages: 470-472

Any of the three tests from general MLE analysis—the Wald, LR, or LM test—can be used to test hypotheses in binary response contexts. Since the tests are all asymptotically equivalent under local alternatives, the choice of statistic usually depends on computational simplicity (since finite sample comparisons must be limited in scope). In the following subsections we discuss some testing situations that often arise in binary choice analysis, and we recommend particular tests for their computational advantages.

#### 15.5.1 Testing Multiple Exclusion Restrictions

Consider the model

$$P(y = 1 \mid \mathbf{x}, \mathbf{z}) = G(\mathbf{x}\boldsymbol{\beta} + \mathbf{z}\boldsymbol{\gamma})$$
 (15.21)


{471}------------------------------------------------

where  $\mathbf{x}$  is  $1 \times K$  and  $\mathbf{z}$  is  $1 \times Q$ . We wish to test the null hypothesis  $\mathbf{H}_0$ :  $\gamma = \mathbf{0}$ , so we are testing Q exclusion restrictions. The elements of  $\mathbf{z}$  can be functions of  $\mathbf{x}$ , such as quadratics and interactions—in which case the test is a pure functional form test. Or, the  $\mathbf{z}$  can be additional explanatory variables. For example,  $\mathbf{z}$  could contain dummy variables for occupation or region. In any case, the form of the test is the same.

Some packages, such as Stata, compute the Wald statistic for exclusion restrictions using a simple command following estimation of the general model. This capability makes it very easy to test multiple exclusion restrictions, provided the dimension of  $(\mathbf{x}, \mathbf{z})$  is not so large as to make probit estimation difficult.

The likelihood ratio statistic is also easy to use. Let  $\mathcal{L}_{ur}$  denote the value of the log-likelihood function from probit of y on  $\mathbf{x}$  and  $\mathbf{z}$  (the unrestricted model), and let  $\mathcal{L}_r$  denote the value of the likelihood function from probit of y on  $\mathbf{x}$  (the restricted model). Then the likelihood ratio test of  $\mathbf{H}_0$ :  $\mathbf{\gamma} = \mathbf{0}$  is simply  $2(\mathcal{L}_{ur} - \mathcal{L}_r)$ , which has an asymptotic  $\chi_Q^2$  distribution under  $\mathbf{H}_0$ . This is analogous to the usual F statistic in OLS analysis of a linear model.

The score or LM test is attractive if the unrestricted model is difficult to estimate. In this section, let  $\hat{\beta}$  denote the *restricted* estimator of  $\beta$ , that is, the probit or logit estimator with  $\mathbf{z}$  excluded from the model. The LM statistic using the estimated expected hessian,  $\hat{\mathbf{A}}_i$  [see equation (15.20) and Section 12.6.2], can be shown to be numerically identical to the following: (1) Define  $\hat{\mathbf{u}}_i \equiv y_i - G(\mathbf{x}_i\hat{\boldsymbol{\beta}})$ ,  $\hat{G}_i \equiv G(\mathbf{x}_i\hat{\boldsymbol{\beta}})$ , and  $\hat{g}_i \equiv g(\mathbf{x}_i\hat{\boldsymbol{\beta}})$ . These are all obtainable after estimating the model without  $\mathbf{z}$ . (2) Use all N observations to run the auxiliary OLS regression

$$\frac{\hat{u}_i}{\sqrt{\hat{G}_i(1-\hat{G}_i)}} \text{ on } \frac{\hat{g}_i}{\sqrt{\hat{G}_i(1-\hat{G}_i)}} \mathbf{x}_i, \qquad \frac{\hat{g}_i}{\sqrt{\hat{G}_i(1-\hat{G}_i)}} \mathbf{z}_i$$

$$(15.22)$$

The LM statistic is equal to the explained sum of squares from this regression. A test that is asymptotically (but not numerically) equivalent is  $NR_u^2$ , where  $R_u^2$  is the uncentered R-squared from regression (15.22).

The LM procedure is rather easy to remember. The term  $\hat{g}_i \mathbf{x}_i$  is the gradient of the mean function  $G(\mathbf{x}_i \boldsymbol{\beta} + \mathbf{z}_i \boldsymbol{\gamma})$  with respect to  $\boldsymbol{\beta}$ , evaluated at  $\boldsymbol{\beta} = \hat{\boldsymbol{\beta}}$  and  $\boldsymbol{\gamma} = \mathbf{0}$ . Similarly,  $\hat{g}_i \mathbf{z}_i$  is the gradient of  $G(\mathbf{x}_i \boldsymbol{\beta} + \mathbf{z}_i \boldsymbol{\gamma})$  with respect to  $\boldsymbol{\gamma}$ , again evaluated at  $\boldsymbol{\beta} = \hat{\boldsymbol{\beta}}$  and  $\boldsymbol{\gamma} = \mathbf{0}$ . Finally, under  $H_0: \boldsymbol{\gamma} = \mathbf{0}$ , the conditional variance of  $u_i$  given  $(\mathbf{x}_i, \mathbf{z}_i)$  is  $G(\mathbf{x}_i \boldsymbol{\beta})[1 - G(\mathbf{x}_i \boldsymbol{\beta})]$ ; therefore,  $[\hat{G}_i(1 - \hat{G}_i)]^{1/2}$  is an estimate of the conditional standard deviation of  $u_i$ . The dependent variable in regression (15.22) is often called a **standardized residual** because it is an estimate of  $u_i/[G_i(1 - G_i)]^{1/2}$ , which has unit conditional (and unconditional) variance. The regressors are simply the gradient of the conditional mean function with respect to both sets of parameters, evaluated under

{472}------------------------------------------------

 $H_0$ , and weighted by the estimated inverse conditional standard deviation. The first set of regressors in regression (15.22) is  $1 \times K$  and the second set is  $1 \times Q$ .

Under H<sub>0</sub>,  $LM \sim \chi_Q^2$ . The LM approach can be an attractive alternative to the LR statistic if **z** has large dimension, since with many explanatory variables probit can be difficult to estimate.

#### 15.5.2 Testing Nonlinear Hypotheses about $\beta$

For testing nonlinear restrictions on  $\beta$  in equation (15.8), the Wald statistic is computationally the easiest because the unrestricted estimator of  $\beta$ , which is just probit or logit, is easy to obtain. Actually imposing nonlinear restrictions in estimation—which is required to apply the score or likelihood ratio methods—can be difficult. However, we must also remember that the Wald statistic for testing nonlinear restrictions is not invariant to reparameterizations, whereas the LM and LR statistics are. (See Sections 12.6 and 13.6; for the LM statistic, we would always use the expected Hessian.)

Let the restrictions on  $\beta$  be given by  $H_0$ :  $\mathbf{c}(\beta) = \mathbf{0}$ , where  $\mathbf{c}(\beta)$  is a  $Q \times 1$  vector of possibly nonlinear functions satisfying the differentiability and rank requirements from Chapter 13. Then, from the general MLE analysis, the Wald statistic is simply

$$W = \mathbf{c}(\hat{\boldsymbol{\beta}})' [\nabla_{\beta} \mathbf{c}(\hat{\boldsymbol{\beta}}) \hat{\mathbf{V}} \nabla_{\beta} \mathbf{c}(\hat{\boldsymbol{\beta}})']^{-1} \mathbf{c}(\hat{\boldsymbol{\beta}})$$
(15.23)

where  $\hat{\mathbf{V}}$  is given in equation (15.20) and  $\nabla_{\beta} \mathbf{c}(\hat{\boldsymbol{\beta}})$  is the  $Q \times K$  Jacobian of  $\mathbf{c}(\boldsymbol{\beta})$  evaluated at  $\hat{\boldsymbol{\beta}}$ .