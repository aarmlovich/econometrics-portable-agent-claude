# Exogenous Explanatory Variables

> Pages: 579-585

We now consider the case where the selection equation is of the censored Tobit form. The population model is

$$y_1 = \mathbf{x}_1 \boldsymbol{\beta}_1 + u_1 \tag{17.32}$$

$$y_2 = \max(0, \mathbf{x}\boldsymbol{\delta}_2 + v_2) \tag{17.33}$$

where  $(\mathbf{x}, y_2)$  is always observed in the population but  $y_1$  is observed only when  $y_2 > 0$ . A standard example occurs when  $y_1$  is the log of the hourly wage offer and  $y_2$  is weekly or annual hours of labor supply.

ASSUMPTION 17.3: (a)  $(\mathbf{x}, y_2)$  is always observed in the population, but  $y_1$  is observed only when  $y_2 > 0$ ; (b)  $(u_1, v_2)$  is independent of  $\mathbf{x}$ ; (c)  $v_2 \sim \text{Normal}(0, \tau_2^2)$ ; and (d)  $E(u_1 | v_2) = \gamma_1 v_2$ .

These assumptions are very similar to the assumptions for a probit selection equation. The only difference is that  $v_2$  now has an unknown variance, since  $y_2$  is a censored as opposed to binary variable.

Amemiya (1985) calls equations (17.32) and (17.33) the **type III Tobit model**, but we emphasize that equation (17.32) is the structural population equation of interest and that equation (17.33) simply determines when  $y_1$  is observed. In the labor economics example, we are interested in the wage offer equation, and equation (17.33) is a reduced-form hours equation. It makes no sense to define  $y_1$  to be, say, zero, just because we do not observe  $y_1$ .

{580}------------------------------------------------

The starting point is equation (17.21), just as in the probit selection case. Now define the selection indicator as  $s_2 = 1$  if  $y_2 > 0$ , and  $s_2 = 0$  otherwise. Since  $s_2$  is a function of  $\mathbf{x}$  and  $v_2$ , it follows immediately that

$$\mathbf{E}(y_1 \mid \mathbf{x}, v_2, s_2) = \mathbf{x}_1 \boldsymbol{\beta}_1 + \gamma_1 v_2 \tag{17.34}$$

This equation means that, if we could observe  $v_2$ , then an OLS regression of  $y_1$  on  $\mathbf{x}_1$ ,  $v_2$  using the selected subsample would consistently estimate  $(\boldsymbol{\beta}_1, \gamma_1)$ , as we discussed in Section 17.2.1. While  $v_2$  cannot be observed when  $y_2 = 0$  (because when  $y_2 = 0$ , we only know that  $v_2 \leq -\mathbf{x}\boldsymbol{\delta}_2$ ), for  $y_2 > 0$ ,  $v_2 = y_2 - \mathbf{x}\boldsymbol{\delta}_2$ . Thus, if we knew  $\boldsymbol{\delta}_2$ , we would know  $v_2$  whenever  $y_2 > 0$ . It seems reasonable that, because  $\boldsymbol{\delta}_2$  can be consistently estimated by Tobit on the whole sample, we can replace  $v_2$  with consistent estimates.

*Procedure 17.3:* (a) Estimate equation (17.33) by standard Tobit using all N observations. For  $y_{i2} > 0$  (say  $i = 1, 2, ..., N_1$ ), define

$$\hat{v}_{i2} = y_{i2} - \mathbf{x}_i \hat{\boldsymbol{\delta}}_2 \tag{17.35}$$

(b) Using observations for which  $y_{i2} > 0$ , estimate  $\beta_1$ ,  $\gamma_1$  by the OLS regression

$$y_{i1} \text{ on } \mathbf{x}_{i1}, \hat{v}_{i2} \quad i = 1, 2, \dots, N_1$$
 (17.36)

This regression produces consistent,  $\sqrt{N}$ -asymptotically normal estimators of  $\beta_1$  and  $\gamma_1$  under Assumption 17.3.

The statistic to test for selectivity bias is just the usual t statistic on  $\hat{v}_{i2}$  in regression (17.36). This was suggested by Vella (1992). Wooldridge (1998) showed that this procedure also solves the selection problem when  $\gamma_1 \neq 0$ .

It seems likely that there is an efficiency gain over Procedure 17.1. If  $v_2$  were known and we could use regression (17.36) for the entire population, there would definitely be an efficiency gain: the error variance is reduced by conditioning on  $v_2$  along with  $\mathbf{x}$ , and there would be no heteroskedasticity in the population. See Problem 4.5.

Unlike in the probit selection case,  $\mathbf{x}_1 = \mathbf{x}$  causes no problems here:  $v_2$  always has separate variation from  $\mathbf{x}_1$  because of variation in  $y_2$ . We do not need to rely on the nonlinearity of the inverse Mills ratio.

Example 17.8 (Wage Offer Equation for Married Women): We now apply Procedure 17.3 to the wage offer equation for married women in Example 17.6. (We assume education is exogenous.) The only difference is that the first-step estimation is Tobit, rather than probit, and we include the Tobit residuals as the additional


{581}------------------------------------------------

explanatory variables, not the inverse Mills ratio. In regression (17.36), the coefficient on  $\hat{v}_2$  is -.000053 (se = .000041), which is somewhat more evidence of a sample selection problem, but we still do not reject the null hypothesis  $H_0$ :  $\gamma_1 = 0$  at even the 15 percent level against a two-sided alternative. Further, the coefficient on *educ* is .103 (se = .015), which is not much different from the OLS and Heckit estimates. (Again, we use the usual OLS standard error.) When we include all exogenous variables in the wage offer equation, the estimates from Procedure 17.3 are much more stable than the Heckit estimates. For example, the coefficient on *educ* becomes .093 (se = .016), which is comparable to the OLS estimates discussed in Example 17.6.

For partial maximum likelihood estimation, we assume that  $(u_1, v_2)$  is jointly normal, and we use the density for  $f(y_2 | \mathbf{x})$  for the entire sample and the conditional density  $f(y_1 | \mathbf{x}, y_2, s_2 = 1) = f(y_1 | \mathbf{x}, y_2)$  for the selected sample. This approach is fairly straightforward because, when  $y_2 > 0$ ,  $y_1 | \mathbf{x}, y_2 \sim \text{Normal}[\mathbf{x}_1 \boldsymbol{\beta}_1 + y_1(y_2 - \mathbf{x}\boldsymbol{\delta}_2), \eta_1^2]$ , where  $\eta_1^2 = \sigma_1^2 - \sigma_{12}^2/\tau_2^2$ ,  $\sigma_1^2 = \text{Var}(u_1)$ , and  $\sigma_{12} = \text{Cov}(u_1, v_2)$ . The log likelihood for observation i is

$$\ell_i(\boldsymbol{\theta}) = s_{i2} \log f(y_{i1} | \mathbf{x}_i, y_{i2}; \boldsymbol{\theta}) + \log f(y_{i2} | \mathbf{x}_i; \boldsymbol{\delta}_2, \tau_2^2)$$
(17.37)

where  $f(y_{i1} | \mathbf{x}_i, y_{i2}; \boldsymbol{\theta})$  is the Normal $[\mathbf{x}_{i1}\boldsymbol{\beta}_1 + \gamma_1(y_{i2} - \mathbf{x}_i\boldsymbol{\delta}_2), \eta_1^2]$  distribution, evaluated at  $y_{i1}$ , and  $f(y_{i2} | \mathbf{x}_i; \boldsymbol{\delta}_2, \tau_2^2)$  is the standard censored Tobit density [see equation (16.19)]. As shown in Problem 13.7, the usual MLE theory can be used even though the log-likelihood function is not based on a true conditional density.

It is possible to obtain sample selection corrections and tests for various other nonlinear models when the selection rule is of the Tobit form. For example, suppose that the binary variable  $y_1$  given  $\mathbf{z}$  follows a probit model, but it is observed only when  $y_2 > 0$ . A valid test for selection bias is to include the Tobit residuals,  $\hat{v}_2$ , in a probit of  $y_1$  on  $\mathbf{z}$ ,  $\hat{v}_2$  using the selected sample; see Vella (1992). This procedure also produces consistent estimates (up to scale), as can be seen by applying the maximum likelihood results in Section 17.2.2 along with two-step estimation results.

Honoré, Kyriazidou, and Udry (1997) show how to estimate the parameters of the type III Tobit model without making distributional assumptions.

# 17.5.2 Endogenous Explanatory Variables

We explicitly consider the case of a single endogenous explanatory variable, as in Section 17.4.2. We use equations (17.25) and (17.26), and, in place of equation (17.27), we have a Tobit selection equation:

$$y_3 = \max(0, \mathbf{z}\boldsymbol{\delta}_3 + v_3) \tag{17.38}$$

{582}------------------------------------------------

ASSUMPTION 17.4: (a)  $(\mathbf{z}, y_3)$  is always observed,  $(y_1, y_2)$  is observed when  $y_3 > 0$ ; (b)  $(u_1, v_3)$  is independent of  $\mathbf{z}$ ; (c)  $v_3 \sim \text{Normal}(0, \tau_3^2)$ ; (d)  $E(u_1 | v_3) = \gamma_1 v_3$ ; and (e)  $E(\mathbf{z}'v_2) = \mathbf{0}$  and, writing  $\mathbf{z}\boldsymbol{\delta}_2 = \mathbf{z}_1\boldsymbol{\delta}_{21} + \mathbf{z}_2\boldsymbol{\delta}_{22}$ ,  $\boldsymbol{\delta}_{22} \neq \mathbf{0}$ .

Again, these assumptions are very similar to those used with a probit selection mechanism.

To derive an estimating equation, write

$$y_1 = \mathbf{z}_1 \delta_1 + \alpha_1 y_2 + \gamma_1 v_3 + e_1 \tag{17.39}$$

where  $e_1 \equiv u_1 - \mathrm{E}(u_1 \mid v_3)$ . Since  $(e_1, v_3)$  is independent of **z** by Assumption 17.4b,  $\mathrm{E}(e_1 \mid \mathbf{z}, v_3) = 0$ . From Theorem 17.1, if  $v_3$  were observed, we could estimate equation (17.39) by 2SLS on the selected sample using instruments  $(\mathbf{z}, v_3)$ . As before, we can estimate  $v_3$  when  $v_3 > 0$ , since  $\delta_3$  can be consistently estimated by Tobit of  $v_3$  on **z** (using the entire sample).

*Procedure 17.4:* (a) Obtain  $\hat{\boldsymbol{\delta}}_3$  from Tobit of  $y_3$  on **z** using all observations. Obtain the Tobit residuals  $\hat{v}_{i3} = y_{i3} - \mathbf{z}_i \hat{\boldsymbol{\delta}}_3$  for  $y_{i3} > 0$ .

(b) Using the selected subsample, estimate the equation

$$y_{i1} = \mathbf{z}_{i1}\boldsymbol{\delta}_1 + \alpha_1 y_{i2} + \gamma_1 \hat{v}_{i3} + error_i \tag{17.40}$$

by 2SLS, using instruments  $(\mathbf{z}_i, \hat{v}_{i3})$ . The estimators are  $\sqrt{N}$ -consistent and asymptotically normal under Assumption 17.4.

Comments similar to those after Procedure 17.2 hold here as well. Strictly speaking, identification really requires that  $\mathbf{z}_2$  appear in the linear projection of  $y_2$  onto  $\mathbf{z}_1$ ,  $\mathbf{z}_2$ , and  $v_3$  in the selected subpopulation. The null of no selection bias is tested using the 2SLS t statistic (or maybe its heteroskedasticity-robust version) on  $\hat{v}_{i3}$ . When  $y_1 \neq 0$ , standard errors should be corrected using two-step methods.

As in the case with a probit selection equation, the endogenous variable  $y_2$  can be continuous, discrete, censored, and so on. Extending the method to multiple endogenous explanatory variables is straightforward. The only restriction is the usual one for linear models: we need enough instruments to identify the structural equation. See Problem 17.6 for an application to the Mroz data.

An interesting special case of model (17.25), (17.26), and (17.38) is when  $y_2 = y_3$ . Actually, because we only use observations for which  $y_3 > 0$ ,  $y_2 = y_3^*$  is also allowed, where  $y_3^* = \mathbf{z}\delta_3 + v_3$ . Either way, the variable that determines selection also appears in the structural equation. This special case could be useful when sample selection is caused by a corner solution outcome on  $y_3$  (in which case  $y_2 = y_3$  is

{583}------------------------------------------------

natural) or because  $y_3^*$  is subject to data censoring (in which case  $y_2 = y_3^*$  is more realistic). An example of the former occurs when  $y_3$  is hours worked and we assume hours appears in the wage offer function. As a data-censoring example, suppose that  $y_1$  is a measure of growth in an infant's weight starting from birth and that we observe  $y_1$  only if the infant is brought into a clinic within three months. Naturally, birth weight depends on age, and so  $y_3^*$ —length of time between the first and second measurements, which has quantitiative meaning—appears as an explanatory variable in the equation for  $y_1$ . We have a data-censoring problem for  $y_3^*$ , which causes a sample selection problem for  $y_1$ . In this case, we would estimate a censored regression model for  $y_3$  [or, possibly,  $\log(y_3)$ ] to account for the data censoring. We would include the residuals  $\hat{v}_{i3} = y_{i3} - \mathbf{z}_i\hat{\delta}_3$  in equation (17.40) for the noncensored observations. As our extra instrument we might use distance from the child's home to the clinic.

#### 17.6 Estimating Structural Tobit Equations with Sample Selection

We briefly show how a structural Tobit model can be estimated using the methods of the previous section. As an example, consider the structural labor supply model

$$\log(w^{\mathrm{o}}) = \mathbf{z}_1 \boldsymbol{\beta}_1 + u_1 \tag{17.41}$$

$$h = \max[0, \mathbf{z}_2 \boldsymbol{\beta}_2 + \alpha_2 \log(w^{\circ}) + u_2]$$
 (17.42)

This system involves simultaneity and sample selection because we observe  $w^{o}$  only if h > 0.

The general form of the model is

$$y_1 = \mathbf{z}_1 \boldsymbol{\beta}_1 + u_1 \tag{17.43}$$

$$y_2 = \max(0, \mathbf{z}_2 \boldsymbol{\beta}_2 + \alpha_2 y_1 + u_2) \tag{17.44}$$

ASSUMPTION 17.5: (a)  $(\mathbf{z}, y_2)$  is always observed;  $y_1$  is observed when  $y_2 > 0$ ; (b)  $(u_1, u_2)$  is independent of  $\mathbf{z}$  with a zero-mean bivariate normal distribution; and (c)  $\mathbf{z}_1$  contains at least one element whose coefficient is different from zero that is not in  $\mathbf{z}_2$ .

As always, it is important to see that equations (17.43) and (17.44) constitute a model describing a population. If  $y_1$  were always observed, then equation (17.43) could be estimated by OLS. If, in addition,  $u_1$  and  $u_2$  were uncorrelated, equation (17.44) could be estimated by censored Tobit. Correlation between  $u_1$  and  $u_2$  could be handled by the methods of Section 16.6.2. Now, we require new methods, whether or not  $u_1$  and  $u_2$  are uncorrelated, because  $y_1$  is not observed when  $y_2 = 0$ .

{584}------------------------------------------------

The restriction in Assumption 17.5c is needed to identify the structural parameters  $(\beta_2, \alpha_2)$   $(\beta_1$  is always identified). To see that this condition is needed, and for finding the reduced form for  $y_2$ , it is useful to introduce the latent variable

$$y_2^* \equiv \mathbf{z}_2 \beta_2 + \alpha_2 y_1 + u_2 \tag{17.45}$$

so that  $y_2 = \max(0, y_2^*)$ . If equations (17.43) and (17.45) make up the system of interest—that is, if  $y_1$  and  $y_2^*$  are always observed—then  $\beta_1$  is identified without further restrictions, but identification of  $\alpha_2$  and  $\beta_2$  requires exactly Assumption 17.5c. This turns out to be sufficient even when  $y_2$  follows a Tobit model and we have nonrandom sample selection.

The reduced form for  $y_2^*$  is  $y_2^* = \mathbf{z}\delta_2 + v_2$ . Therefore, we can write the reduced form of equation (17.44) as

$$y_2 = \max(0, \mathbf{z}\boldsymbol{\delta}_2 + v_2). \tag{17.46}$$

But then equations (17.43) and (17.46) constitute the model we studied in Section 17.5.1. The vector  $\delta_2$  is consistently estimated by Tobit, and  $\beta_1$  is estimated as in Procedure 17.3. The only remaining issue is how to estimate the structural parameters of equation (17.44),  $\alpha_2$  and  $\beta_2$ . In the labor supply case, these are the labor supply parameters.

Assuming identification, estimation of  $(\alpha_2, \beta_2)$  is fairly straightforward after having estimated  $\beta_1$ . To see this point, write the reduced form of  $y_2$  in terms of the structural parameters as

$$y_2 = \max[0, \mathbf{z}_2 \boldsymbol{\beta}_2 + \alpha_2(\mathbf{z}_1 \boldsymbol{\beta}_1) + v_2]$$
 (17.47)

Under joint normality of  $u_1$  and  $u_2$ ,  $v_2$  is normally distributed. Therefore, if  $\beta_1$  were known,  $\beta_2$  and  $\alpha_2$  could be estimated by standard Tobit using  $\mathbf{z}_2$  and  $\mathbf{z}_1\beta_1$  as regressors. Operationalizing this procedure requires replacing  $\beta_1$  with its consistent estimator. Thus, using all observations,  $\beta_2$  and  $\alpha_2$  are estimated from the Tobit equation

$$y_{i2} = \max[0, \mathbf{z}_{i2}\boldsymbol{\beta}_2 + \alpha_2(\mathbf{z}_{i1}\hat{\boldsymbol{\beta}}_1) + error_i]$$
(17.48)

To summarize, we have the following:

*Procedure 17.5:* (a) Use Procedure 17.3 to obtain  $\hat{\beta}_1$ .

(b) Obtain  $\hat{\beta}_2$  and  $\hat{\alpha}_2$  from the Tobit in equation (17.48).

In applying this procedure, it is important to note that the explanatory variable in equation (17.48) is  $\mathbf{z}_{i1}\hat{\boldsymbol{\beta}}_1$  for all *i*. These are *not* the fitted values from regression (17.36), which depend on  $\hat{v}_{i2}$ . Also, it may be tempting to use  $y_{i1}$  in place of  $\mathbf{z}_{i1}\hat{\boldsymbol{\beta}}_1$  for

{585}------------------------------------------------

that part of the sample for which yi<sup>1</sup> is observed. This approach is not a good idea: the estimators are inconsistent in this case.

The estimation in equation (17.48) makes it clear that the procedure fails if z<sup>1</sup> does not contain at least one variable not in <sup>z</sup>2. If <sup>z</sup><sup>1</sup> is a subset of <sup>z</sup>2, then <sup>z</sup><sup>i</sup><sup>1</sup> ^*b*<sup>1</sup> is a linear combination of zi2, and so perfect multicollinearity will exist in equation (17.48).

Estimating Avarða^2; ^*b*2<sup>Þ</sup> is even messier than estimating Avar<sup>ð</sup> ^*b*1Þ, since <sup>ð</sup>a^2; ^*b*2<sup>Þ</sup> comes from a three-step procedure. Often just the usual Tobit standard errors and test statistics reported from equation (17.48) are used, even though these are not strictly valid. By setting the problem up as a large GMM problem, as illustrated in Chapter 14, correct standard errors and test statistics can be obtained.

Under Assumption 17.5, a full maximum likelihood approach is possible. In fact, the log-likelihood function can be constructed from equations (17.43) and (17.47), and it has a form very similar to equation (17.37). The only difference is that nonlinear restrictions are imposed automatically on the structural parameters. In addition to making it easy to obtain valid standard errors, MLE is desirable because it allows us to estimate s<sup>2</sup> <sup>2</sup> ¼ Varðu2Þ, which is needed to estimate average partial effects in equation (17.44).

In examples such as labor supply, it is not clear where the elements of z<sup>1</sup> that are not in z<sup>2</sup> might come from. One possibility is a union binary variable, if we believe that union membership increases wages (other factors accounted for) but has no effect on labor supply once wage and other factors have been controlled for. This approach would require knowing union status for people whether or not they are working in the period covered by the survey. In some studies past experience is assumed to affect wage—which it certainly does—and is assumed not to appear in the labor supply function, a tenuous assumption.