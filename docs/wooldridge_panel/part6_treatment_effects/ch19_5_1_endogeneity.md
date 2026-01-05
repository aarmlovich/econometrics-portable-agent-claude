# Endogeneity

> Pages: 670-675

We approach the problem of endogenous explanatory variables from an omitted variables perspective. Let y<sup>1</sup> be the nonnegative, in principle unbounded variable to be explained, and let z and y<sup>2</sup> be observable explanatory variables (of dimension 1 L and 1 G1, respectively). Let c<sup>1</sup> be an unobserved latent variable (or unobserved heterogeneity). We assume that the (structural) model of interest is an omitted variables model of exponential form, written in the population as

$$E(y_1 \mid \mathbf{z}, \mathbf{y}_2, c_1) = \exp(\mathbf{z}_1 \boldsymbol{\delta}_1 + \mathbf{y}_2 \boldsymbol{\gamma}_1 + c_1)$$
(19.37)

where z<sup>1</sup> is a 1 L<sup>1</sup> subset of z containing unity; thus, the model (19.37) incorporates some exclusion restrictions. On the one hand, the elements in z are assumed to be exogenous in the sense that they are independent of c1. On the other hand, y<sup>2</sup> and c<sup>1</sup> are allowed to be correlated, so that y<sup>2</sup> is potentially endogenous.

To use a quasi-likelihood approach, we assume that y<sup>2</sup> has a linear reduced form satisfying certain assumptions. Write

$$\mathbf{y}_2 = \mathbf{z}\mathbf{\Pi}_2 + \mathbf{v}_2 \tag{19.38}$$

where P<sup>2</sup> is an L G<sup>1</sup> matrix of reduced form parameters and v<sup>2</sup> is a 1 G<sup>1</sup> vector of reduced form errors. We assume that the rank condition for identification holds, which requires the order condition L - L<sup>1</sup> bG1. In addition, we assume that ðc1; v2Þ is independent of z, and that

$$c_1 = \mathbf{v}_2 \boldsymbol{\rho}_1 + e_1 \tag{19.39}$$

where e<sup>1</sup> is independent of v<sup>2</sup> (and necessarily of z). (We could relax the independence assumptions to some degree, but we cannot just assume that v<sup>2</sup> is uncorrelated with z


{671}------------------------------------------------

and that  $e_1$  is uncorrelated with  $\mathbf{v}_2$ .) It is natural to assume that  $\mathbf{v}_2$  has zero mean, but it is convenient to assume that  $\mathrm{E}[\exp(e_1)] = 1$  rather than  $\mathrm{E}(e_1) = 0$ . This assumption is without loss of generality whenever a constant appears in  $\mathbf{z}_1$ , which should almost always be the case.

If  $(c_1, \mathbf{v}_2)$  has a multivariate normal distribution, then the representation in equation (19.39) under the stated assumptions always holds. We could also extend equation (19.39) by putting other functions of  $\mathbf{v}_2$  on the right-hand side, such as squares and cross products, but we do not show these explicitly. Note that  $\mathbf{y}_2$  is exogenous if and only if  $\rho_1 = \mathbf{0}$ .

Under the maintained assumptions, we have

$$E(y_1 | \mathbf{z}, \mathbf{y}_2, \mathbf{v}_2) = \exp(\mathbf{z}_1 \boldsymbol{\delta}_1 + \mathbf{y}_2 \mathbf{y}_1 + \mathbf{v}_2 \boldsymbol{\rho}_1)$$
(19.40)

and this equation suggests a strategy for consistently estimating  $\delta_1$ ,  $\gamma_1$ , and  $\rho_1$ . If  $\mathbf{v}_2$  were observed, we could simply use this regression function in one of the QMLE earlier methods (for example, Poisson, two-step negative binomial, or exponential). Because these methods consistently estimate correctly specified conditional means, we can immediately conclude that the QMLEs would be consistent. [If  $y_1$  conditional on  $(\mathbf{z}, \mathbf{y}_2, c_1)$  has a Poisson distribution with mean in equation (19.37), then the distribution of  $y_1$  given  $(\mathbf{z}, \mathbf{y}_2, \mathbf{v}_2)$  has overdispersion of the type (19.28), so the two-step negative binomial estimator might be preferred in this context.]

To operationalize this procedure, the unknown quantities  $\mathbf{v}_2$  must be replaced with estimates. Let  $\hat{\mathbf{\Pi}}_2$  be the  $L \times G_1$  matrix of OLS estimates from the first-stage estimation of equation (19.38); these are consistent estimates of  $\mathbf{\Pi}_2$ . Define  $\hat{\mathbf{v}}_2 = \mathbf{y}_2 - \mathbf{z}\hat{\mathbf{\Pi}}_2$  (where the observation subscript is suppressed). Then estimate the exponential regression model using regressors  $(\mathbf{z}_1, \mathbf{y}_2, \hat{\mathbf{v}}_2)$  by one of the QMLEs. The estimates  $(\hat{\boldsymbol{\delta}}_1, \hat{\boldsymbol{\gamma}}_1, \hat{\boldsymbol{\rho}}_1)$  from this procedure are consistent using standard arguments from two-step estimation in Chapter 12.

This method is similar in spirit to the methods we saw for binary response (Chapter 15) and censored regression models (Chapter 16). There is one difference: here, we do not need to make distributional assumptions about  $y_1$  or  $y_2$ . However, we do assume that the reduced-form errors  $v_2$  are independent of z. In addition, we assume that  $c_1$  and  $v_2$  are linearly related with  $e_1$  in equation (19.39) independent of  $v_2$ . Later we will show how to relax these assumptions using a method of moments approach.

Because  $\hat{\mathbf{v}}_2$  depends on  $\hat{\mathbf{\Pi}}_2$ , the variance matrix estimators for  $\hat{\boldsymbol{\delta}}_1$ ,  $\hat{\boldsymbol{\gamma}}_1$ , and  $\hat{\boldsymbol{\rho}}_1$  should generally be adjusted to account for this dependence, as described in Sections 12.5.2 and 14.1. Using the results from Section 12.5.2, it can be shown that estimation of  $\mathbf{\Pi}_2$  does not affect the asymptotic variance of the QMLEs when  $\boldsymbol{\rho}_1 = \mathbf{0}$ , just as we saw

{672}------------------------------------------------

when testing for endogeneity in probit and Tobit models. Therefore, testing for endogeneity of  $\mathbf{y}_2$  is relatively straightforward: simply test  $\mathbf{H}_0$ :  $\boldsymbol{\rho}_1 = \mathbf{0}$  using a Wald or LM statistic. When  $G_1 = 1$ , the most convenient statistic is probably the t statistic on  $\hat{v}_2$ , with the fully robust form being the most preferred (but the GLM form is also useful). The LM test for omitted variables is convenient when  $G_1 > 1$  because it can be computed after estimating the null model ( $\boldsymbol{\rho}_1 = \mathbf{0}$ ) and then doing a variable addition test for  $\hat{\mathbf{v}}_2$ . The test has  $G_1$  degrees of freedom in the chi-square distribution.

There is a final comment worth making about this test. The null hypothesis is the same as  $E(y_1 | \mathbf{z}, \mathbf{y}_2) = \exp(\mathbf{z}_1 \boldsymbol{\delta}_1 + \mathbf{y}_2 \boldsymbol{\gamma}_1)$ . The test for endogeneity of  $\mathbf{y}_2$  simply looks for whether a particular linear combination of  $\mathbf{y}_2$  and  $\mathbf{z}$  appears in this conditional expectation. For the purposes of getting a limiting chi-square distribution, it does not matter where the linear combination  $\hat{\mathbf{v}}_2$  comes from. In other words, under the null hypothesis none of the assumptions we made about  $(c_1, \mathbf{v}_2)$  need to hold:  $\mathbf{v}_2$  need not be independent of  $\mathbf{z}$ , and  $e_1$  in equation (19.39) need not be independent of  $\mathbf{v}_2$ . Therefore, as a test, this procedure is very robust, and it can be applied when  $\mathbf{v}_2$  contains binary, count, or other discrete variables. Unfortunately, if  $\mathbf{v}_2$  is endogenous, the correction does not work without something like the assumptions made previously.

Example 19.2 (Is Education Endogenous in the Fertility Equation?): We test for endogeneity of educ in Example 19.1. The IV for educ is a binary indicator for whether the woman was born in the first half of the year (frsthalf), which we assume is exogenous in the fertility equation. In the reduced-form equation for educ, the coefficient on frsthalf is -.636 (se =.104), and so there is a significant negative partial relationship between years of schooling and being born in the first half of the year.

When we add the first-stage residuals,  $\hat{v}_2$ , to the Poisson regression, its coefficient is .025, and its GLM standard error is .028. Therefore, there is little evidence against the null hypothesis that *educ* is exogenous. The coefficient on *educ* actually becomes larger in magnitude (-.046), but it is much less precisely estimated.

Mullahy (1997) has shown how to estimate exponential models when some explanatory variables are endogenous without making assumptions about the reduced form of  $\mathbf{y}_2$ . This approach is especially attractive for dummy endogenous and other discrete explanatory variables, where the linearity in equation (19.39) coupled with independence of  $\mathbf{z}$  and  $\mathbf{v}_2$  is unrealistic. To sketch Mullahy's approach, write  $\mathbf{x}_1 = (\mathbf{z}_1, \mathbf{y}_2)$  and  $\boldsymbol{\beta}_1 = (\boldsymbol{\delta}_1', \boldsymbol{\gamma}_1')'$ . Then, under the model (19.37), we can write

$$y_1 \exp(-\mathbf{x}_1 \boldsymbol{\beta}_1) = \exp(c_1)a_1, \qquad E(a_1 | \mathbf{z}, \mathbf{y}_2, c_1) = 1$$
 (19.41)

{673}------------------------------------------------

If we assume that c<sup>1</sup> is independent of z—a standard assumption concerning unobserved heterogeneity and exogenous variables—and use the normalization E½expðc1Þ ¼ 1, we have the conditional moment restriction

$$E[y_1 \exp(-\mathbf{x}_1 \boldsymbol{\beta}_1) | \mathbf{z}] = 1 \tag{19.42}$$

Because y1, x1, and z are all observable, condition (19.42) can be used as the basis for generalized method of moments estimation. The function gðy1; y2; z1; *b*1Þ 1 y<sup>1</sup> expðx1*b*1Þ - 1, which depends on observable data and the parameters, is uncorrelated with any function of z (at the true value of *b*1). GMM estimation can be used as in Section 14.2 once a vector of instrumental variables has been chosen.

An important feature of Mullahy's approach is that no assumptions, other than the standard rank condition for identification in nonlinear models, are made about the distribution of y<sup>2</sup> given z: we need not assume the existence of a linear reduced form for y<sup>2</sup> with errors independent of z. Mullahy's procedure is computationally more difficult, and testing for endogeneity in his framework is harder than in the QMLE approach. Therefore, we might first use the two-step quasi-likelihood method proposed earlier for testing, and if endogeneity seems to be important, Mullahy's GMM estimator can be implemented. See Mullahy (1997) for details and an empirical example.

# 19.5.2 Sample Selection

It is also possible to test and correct for sample selection in exponential regression models. The case where selection is determined by the dependent variable being above or below a known threshold requires full maximum likelihood methods using a truncated count distribution; you are referred to the book by Cameron and Trivedi (1998). Here, we assume that sample selection is related to an unobservable in the population model

$$\mathbf{E}(y_1 \mid \mathbf{x}, c_1) = \exp(\mathbf{x}_1 \boldsymbol{\beta}_1 + c_1) \tag{19.43}$$

where x<sup>1</sup> is a 1 K<sup>1</sup> vector of exogenous variables containing a constant, and c<sup>1</sup> is an unobserved random variable. The full set of exogenous variables is x, and c<sup>1</sup> is independent of x. Therefore, if a random sample on ðx1; y1Þ were available, *b*<sup>1</sup> could be consistently estimated by a Poisson regression of y<sup>1</sup> on x<sup>1</sup> (or by some other QMLE) under the normalization E½expðc1Þ ¼ 1.

A sample selection problem arises when a random sample on ðx1; y1Þ from the relevant population is not available. Let y<sup>2</sup> denote a binary selection indicator, which is unity if ðx1; y1Þ is observed and zero otherwise. We assume that y<sup>2</sup> is determined by y<sup>2</sup> ¼ 1½x2*d*<sup>2</sup> þ v<sup>2</sup> > 0, where 1½ is the indicator function, x<sup>2</sup> is a subset of x (typi

{674}------------------------------------------------

cally,  $\mathbf{x}_2 = \mathbf{x}$ ), and  $v_2$  is unobserved. This is a standard sample selection mechanism, where  $v_2$  and  $\mathbf{x}_2$  must be observable for all units in the population.

In this setting, sample selection bias arises when  $v_2$  is correlated with  $c_1$ . In particular, if we write equation (19.43) with a multiplicative error,  $y_1 = \exp(\mathbf{x}_1 \boldsymbol{\beta}_1 + c_1)a_1$ , with  $\mathrm{E}(a_1 \mid \mathbf{x}, c_1) = 1$  by definition, we also assume that  $\mathrm{E}(a_1 \mid \mathbf{x}, c_1, v_2) = \mathrm{E}(a_1) = 1$ . In other words, selection may be correlated with  $c_1$  but not  $a_1$ . This model is similar to the linear model with sample selection in Section 17.4.1 where the error in the regression equation can be decomposed into two parts, one that is correlated with  $v_2$  ( $v_1$ ) and one that is not ( $v_1$ ).

To derive a simple correction, assume that  $(c_1, v_2)$  is independent of  $\mathbf{x}$  and bivariate normal with zero mean;  $v_2$  also has a unit variance, so that  $y_2$  given  $\mathbf{x}$  follows a probit model. These assumptions imply that  $\mathrm{E}[\exp(c_1) \,|\, \mathbf{x}, v_2] = \mathrm{E}[\exp(c_1) \,|\, v_2] = \exp(\rho_0 + \rho_1 v_2)$  for parameters  $\rho_0$  and  $\rho_1$ . Provided  $\mathbf{x}_1$  contains a constant, we can use the normalization  $\exp(\rho_0) = 1$ , and we do so in what follows. Then  $\mathrm{E}(y_1 \,|\, \mathbf{x}, v_2) = \exp(\mathbf{x}_1 \boldsymbol{\beta}_1 + \rho_1 v_2)$ , and so by iterated expectations,

$$E(y_1 | \mathbf{x}, y_2 = 1) = \exp(\mathbf{x}_1 \boldsymbol{\beta}_1) g(\mathbf{x}_2 \boldsymbol{\delta}_2, \rho_1)$$
(19.44)

where  $g(\mathbf{x}_2\boldsymbol{\delta}_2,\rho_1) \equiv \mathrm{E}[\exp(\rho_1v_2)\,|\,v_2>-\mathbf{x}_2\boldsymbol{\delta}_2]$ . By integrating the function  $\exp(\rho_1v_2)$  against the truncated standard normal density conditional on  $v_2>-\mathbf{x}_2\boldsymbol{\delta}_2$ , it can be shown that  $g(\mathbf{x}_2\boldsymbol{\delta}_2,\rho_1)=\exp(\rho_1^2)\Phi(\rho_1+\mathbf{x}_2\boldsymbol{\delta}_2)/\Phi(\mathbf{x}_2\boldsymbol{\delta}_2)$ , where  $\Phi(\cdot)$  is the standard normal cdf.

Given equation (19.44), we can apply a two-step method similar to Heckman's (1976) method for linear models that we covered in Chapter 17. First, run a probit of  $y_2$  on  $\mathbf{x}_2$  using the entire sample. Let  $\hat{\boldsymbol{\delta}}_2$  be the probit estimator of  $\boldsymbol{\delta}_2$ . Next, on the selected subsample for which  $(y_1, \mathbf{x}_1)$  is observed, use a QMLE analysis with conditional mean function  $\exp(\mathbf{x}_1\boldsymbol{\beta}_1)g(\mathbf{x}_2\hat{\boldsymbol{\delta}}_2, \rho_1)$  to estimate  $\boldsymbol{\beta}_1$  and  $\rho_1$ . If  $\rho_1 \neq 0$ , then, as usual, the asymptotic variance of  $\hat{\boldsymbol{\beta}}_1$  and  $\hat{\rho}_1$  should be adjusted for estimation of  $\boldsymbol{\delta}_2$ .

Testing  $\rho_1 = 0$  is simple if we use the robust score test. This requires the derivative of the mean function with respect to  $\rho_1$ , evaluated at  $\rho_1 = 0$ . But  $\partial g(\mathbf{x}_2 \boldsymbol{\delta}_2, 0)/\partial \rho_1 = \lambda(\mathbf{x}_2 \boldsymbol{\delta}_2)$ , where  $\lambda(\cdot)$  is the usual inverse Mills ratio that appears in linear sample selection contexts. Thus the derivative of the mean function with respect to  $\rho_1$ , evaluated at all estimates under the null, is simply  $\exp(\mathbf{x}_1\hat{\boldsymbol{\beta}}_1)\lambda(\mathbf{x}_2\hat{\boldsymbol{\delta}}_2)$ . This result gives the following procedure to test for sample selection: (1) let  $\hat{\boldsymbol{\beta}}_1$  be a QMLE (for example, the Poisson) using the selected sample, and define  $\hat{y}_{i1} \equiv \exp(\mathbf{x}_{i1}\hat{\boldsymbol{\beta}}_1)$ ,  $\hat{u}_{i1} \equiv y_{i1} - \hat{y}_{i1}$ , and  $\tilde{u}_{i1} \equiv \hat{u}_{i1}/\sqrt{\hat{y}_{i1}}$  for all i in the selected sample; (2) obtain  $\hat{\boldsymbol{\delta}}_2$  from the probit of  $y_2$  onto  $\mathbf{x}_2$ , using the entire sample; denote the estimated inverse Mills ratio for each observation i by  $\hat{\lambda}_{i2}$ ; and (3) regress  $\tilde{u}_{i1}$  onto  $\sqrt{\hat{y}_{i1}}\mathbf{x}_{i1}$ ,  $\sqrt{\hat{y}_{i1}}\hat{\lambda}_{i2}$  using the selected sample, and use  $N_1R_u^2$  as asymptotically  $\chi_1^2$ , where  $N_1$  is the number of observations

{675}------------------------------------------------

in the selected sample. This approach assumes that the GLM assumption holds under  $H_0$ . For the fully robust test, first regress  $\sqrt{\hat{y}_{i1}}\hat{\lambda}_{i2}$  onto  $\sqrt{\hat{y}_{i1}}\mathbf{x}_{i1}$  using the selected sample and save the residuals,  $\tilde{r}_{i1}$ ; then regress 1 on  $\tilde{u}_{i1}\tilde{r}_{i1}$ ,  $i=1,2,\ldots,N_1$ , and use  $N_1$  – SSR as asymptotically  $\chi_1^2$ .

#### 19.6 Panel Data Methods

In this final section, we discuss estimation of panel data models, primarily focusing on count data. Our main interest is in models that contain unobserved effects, but we initially cover pooled estimation when the model does not explicitly contain an unobserved effect.

The pioneering work in unobserved effects count data models was done by Hausman, Hall, and Griliches (1984) (HHG), who were interested in explaining patent applications by firms in terms of spending on research and development. HHG developed random and fixed effects models under full distributional assumptions. Wooldridge (1999a) has shown that one of the approaches suggested by HHG, which is typically called the **fixed effects Poisson model**, has some nice robustness properties. We will study those here.

Other count panel data applications include (with response variable in parentheses) Rose (1990) (number of airline accidents), Papke (1991) (number of firm births in an industry), Downes and Greenstein (1996) (number of private schools in a public school district), and Page (1995) (number of housing units shown to individuals). The time series dimension in each of these studies allows us to control for unobserved heterogeneity in the cross section units, and to estimate certain dynamic relationships.

As with the rest of the book, we explicitly consider the case with N large relative to T, as the asymptotics hold with T fixed and  $N \to \infty$ .