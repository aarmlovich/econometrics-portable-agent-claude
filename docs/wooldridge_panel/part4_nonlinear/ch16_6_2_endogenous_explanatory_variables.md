# Endogenous Explanatory Variables

> Pages: 539-542

Suppose we now allow one of the variables in the Tobit model to be endogenous. The model is

$$y_1 = \max(0, \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1) \tag{16.26}$$

$$y_2 = \mathbf{z}\delta_2 + v_2 = \mathbf{z}_1\delta_{21} + \mathbf{z}_2\delta_{22} + v_2 \tag{16.27}$$

where ðu1; v2Þ are zero-mean normally distributed, independent of z. If u<sup>1</sup> and v<sup>2</sup> are correlated, then y<sup>2</sup> is endogenous. For identification we need the usual rank condition *d*<sup>22</sup> 00; Eðz<sup>0</sup> zÞ is assumed to have full rank, as always.

If equation (16.26) represents a data-censoring problem, we are interested, as always, in the parameters, *d*<sup>1</sup> and a1, as these are the parameters of interest in the uncensored population model. For corner solution outcomes, the quantities of interest are more subtle. However, when the endogeneity of y<sup>2</sup> is due to omitted variables or simultaneity, the parameters we need to estimate to obtain average partial effects are *d*1, a1, 

{540}------------------------------------------------

and  $\sigma_1^2 = \text{Var}(u_1)$ . The reasoning is just as for the probit model in Section 15.7.2. Holding other factors fixed, the difference in  $y_1$  when  $y_2$  changes from  $\bar{y}_2$  to  $\bar{y}_2 + 1$  is

$$\max[0, \overline{\mathbf{z}}_1 \boldsymbol{\delta}_1 + \alpha_1(\overline{y}_2 + 1) + u_1] - \max[0, \overline{\mathbf{z}}_1 \boldsymbol{\delta}_1 + \alpha_1 \overline{y}_2 + u_1]$$

Averaging this expression across the distribution of  $u_1$  gives differences in expectations that have the form (16.14), with  $\mathbf{x} = [\overline{\mathbf{z}}_1, (\overline{y}_2 + 1)]$  in the first case,  $\mathbf{x} = (\overline{\mathbf{z}}_1, \overline{y}_2)$  in the second, and  $\sigma = \sigma_1$ . Importantly, unlike in the data censoring case, we need to estimate  $\sigma_1^2$  in order to estimate the partial effects of interest (the APEs).

Before estimating this model by maximum likelihood, a procedure that requires obtaining the distribution of  $(y_1, y_2)$  given  $\mathbf{z}$ , it is convenient to have a two-step procedure that also delivers a simple test for the endogeneity of  $y_2$ . Smith and Blundell (1986) propose a two-step procedure that is analogous to the Rivers-Vuong method (see Section 15.7.2) for binary response models. Under bivariate normality of  $(u_1, v_2)$ , we can write

$$u_1 = \theta_1 v_2 + e_1 \tag{16.28}$$

where  $\theta_1 = \eta_1/\tau_2^2$ ,  $\eta_1 = \text{Cov}(u_1, v_2)$ ,  $\tau_2^2 = \text{Var}(v_2)$ , and  $e_1$  is independent of  $v_2$  with a zero-mean normal distribution and variance, say,  $\tau_1^2$ . Further, because  $(u_1, v_2)$  is independent of  $\mathbf{z}$ ,  $e_1$  is independent of  $(\mathbf{z}, v_2)$ . Now, plugging equation (16.28) into equation (16.26) gives

$$y_1 = \max(0, \mathbf{z}_1 \delta_1 + \alpha_1 y_2 + \theta_1 v_2 + e_1)$$
 (16.29)

where  $e_1 | \mathbf{z}, v_2 \sim \text{Normal}(0, \tau_1^2)$ . It follows that, if we knew  $v_2$ , we would just estimate  $\delta_1$ ,  $\alpha_1$ ,  $\theta_1$ , and  $\tau_1^2$  by standard censored Tobit. We do not observe  $v_2$  because it depends on the unknown vector  $\delta_2$ . However, we can easily estimate  $\delta_2$  by OLS in a first stage. The Smith-Blundell procedure is as follows:

Procedure 16.1: (a) Estimate the reduced form of  $y_2$  by OLS; this step gives  $\hat{\delta}_2$ . Define the reduced-form OLS residuals as  $\hat{v}_2 = y_2 - z\hat{\delta}_2$ .

(b) Estimate a standard Tobit of  $y_1$  on  $\mathbf{z}_1$ ,  $y_2$ , and  $\hat{v}_2$ . This step gives consistent estimators of  $\delta_1$ ,  $\alpha_1$ ,  $\theta_1$ , and  $\tau_1^2$ .

The usual t statistic on  $\hat{v}_2$  reported by Tobit provides a simple test of the null  $H_0$ :  $\theta_1 = 0$ , which says that  $y_2$  is exogenous. Further, under  $\theta_1 = 0$ ,  $e_1 = u_1$ , and so normality of  $v_2$  plays no role: as a *test* for endogeneity of  $y_2$ , the Smith-Blundell approach is valid without any distributional assumptions on the reduced form of  $y_2$ .

Example 16.4 (Testing Exogeneity of Education in the Hours Equation): As an illustration, we test for endogeneity of educ in the reduced-form hours equation in Example 16.3. We assume that motheduc, fatheduc, and huseduc are exogenous in the hours


{541}------------------------------------------------

equation, and so these are valid instruments for *educ*. We first obtain  $\hat{v}_2$  as the OLS residuals from estimating the reduced form for *educ*. When  $\hat{v}_2$  is added to the Tobit model in Example 16.3 (without *unem* and *city*), its coefficient is 39.88 with t statistic = .91. Thus, there is little evidence that *educ* is endogenous in the equation. The test is valid under the null hypothesis that *educ* is exogenous even if *educ* does not have a conditional normal distribution.

When  $\theta_1 \neq 0$ , the second-stage Tobit standard errors and test statistics are not asymptotically valid because  $\hat{\delta}_2$  has been used in place of  $\delta_2$ . Smith and Blundell (1986) contain formulas for correcting the asymptotic variances; these can be derived using the formulas for two-step M-estimators in Chapter 12. It is easily seen that joint normality of  $(u_1, v_2)$  is not absolutely needed for the procedure to work. It suffices that  $u_1$  conditional on  $\mathbf{z}$  and  $v_2$  is distributed as Normal $(\theta_1 v_2, \tau_1^2)$ . Still, this is a fairly restrictive assumption.

When  $\theta_1 \neq 0$ , the Smith-Blundell procedure does not allow us to estimate  $\sigma_1^2$ , which is needed to estimate average partial effects in corner solution outcomes. Nevertheless, we can obtain consistent estimates of the average partial effects by using methods similar to those in the probit case. Using the same reasoning in Section 15.7.2, the APEs are obtained by computing derivatives or differences of

$$\mathbf{E}_{v_2}[m(\mathbf{z}_1\boldsymbol{\delta}_1 + \alpha_1 y_2 + \theta_1 v_2, \tau_1^2)] \tag{16.30}$$

where  $m(z, \sigma^2) \equiv \Phi(z/\sigma)z + \sigma\phi(z/\sigma)$  and  $E_{v_2}[\cdot]$  denotes expectation with respect to the distribution of  $v_2$ . Using the same argument as in Section 16.6.1, expression (16.30) can be written as  $m(\mathbf{z}_1\boldsymbol{\delta}_1 + \alpha_1y_2, \theta_1^2\tau_2^2 + \tau_1^2)$ . Therefore, consistent estimators of the APEs are obtained by taking, with respect to elements of  $(\mathbf{z}_1, y_2)$ , derivatives or differences of

$$m(\mathbf{z}_1\hat{\boldsymbol{\delta}}_1 + \hat{\alpha}_1 y_2, \hat{\theta}_1^2 \hat{\tau}_2^2 + \hat{\tau}_1^2)$$
 (16.31)

where all estimates except  $\hat{\tau}_2^2$  come from step b of the Smith-Blundell procedure;  $\hat{\tau}_2^2$  is simply the usual estimate of the error variance from the first-stage OLS regression. As in the case of probit, obtaining standard errors for the APEs based on expression (16.31) and the delta method would be quite complicated. An alternative procedure, where  $m(\mathbf{z}_1\hat{\boldsymbol{\delta}}_1 + \hat{\alpha}_1 y_2 + \hat{\theta}_1\hat{v}_{i2}, \hat{\tau}_1^2)$  is averaged across i, is also consistent, but it does not exploit the normality of  $v_2$ .

A full maximum likelihood approach avoids the two-step estimation problem. The joint distribution of  $(y_1, y_2)$  given **z** is most easily found by using

$$f(y_1, y_2 | \mathbf{z}) = f(y_1 | y_2, \mathbf{z}) f(y_2 | \mathbf{z})$$
(16.32)

{542}------------------------------------------------

just as for the probit case in Section 15.7.2. The density  $f(y_2 | \mathbf{z})$  is Normal $(\mathbf{z}\boldsymbol{\delta}_2, \tau_2^2)$ . Further, from equation (16.29),  $y_1$  given  $(y_2, \mathbf{z})$  follows a Tobit with latent mean

$$\mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + \theta_1 v_2 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + (\eta_1 / \tau_2^2)(y_2 - \mathbf{z} \boldsymbol{\delta}_2)$$

and variance  $\tau_1^2 = \sigma_1^2 - (\eta_1^2/\tau_2^2)$ , where  $\sigma_1^2 = \text{Var}(u_1)$ ,  $\tau_2^2 = \text{Var}(v_2)$ , and  $\eta_1 = \text{Cov}(u_1, v_2)$ . Taking the log of equation (16.32), the log-likelihood function for each i is easily constructed as a function of the parameters  $(\delta_1, \alpha_1, \delta_2, \sigma_1^2, \tau_2^2, \eta_1)$ . The usual coditional maximum likelihood theory can be used for constructing standard errors and test statistics.

Once the MLE has been obtained, we can easily test the null hypothesis of exogeneity of  $y_2$  by using the t statistic for  $\hat{\theta}_1$ . Because the MLE can be computationally more difficult than the Smith-Blundell procedure, it makes sense to use the Smith-Blundell procedure to test for endogeneity before obtaining the MLE.

If  $y_2$  is a binary variable, then the Smith-Blundell assumptions cannot be expected to hold. Taking equation (16.26) as the structural equation, we could add

$$y_2 = 1[\mathbf{z}\mathbf{\pi}_2 + v_2 > 0] \tag{16.33}$$

and assume that  $(u_1, v_2)$  has a zero-mean normal distribution and is independent of  $\mathbf{z}$ ;  $v_2$  is standard normal, as always. Equation (16.32) can be used to obtain the log likelihood for each i. Since  $y_2$  given  $\mathbf{z}$  is probit, its density is easy to obtain:  $f(y_2 | \mathbf{z}) = \Phi(\mathbf{z}\boldsymbol{\pi}_2)^{y_2}[1 - \Phi(\mathbf{z}\boldsymbol{\pi}_2)]^{1-y_2}$ . The hard part is obtaining the conditional density  $f(y_1 | y_2, \mathbf{z})$ , which is done first for  $y_2 = 0$  and then for  $y_2 = 1$ ; see Problem 16.6. Similar comments hold if  $y_2$  given  $\mathbf{z}$  follows a standard Tobit model.