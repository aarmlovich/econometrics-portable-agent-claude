# **6.2.1** Testing for Endogeneity

> Pages: 132-136

We start with the linear model and a single possibly endogenous variable. For notational clarity we now denote the dependent variable by  $y_1$  and the potentially endogenous explanatory variable by  $y_2$ . As in all 2SLS contexts,  $y_2$  can be continuous or binary, or it may have continuous and discrete characteristics; there are no restrictions. The population model is

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1 \tag{6.9}$$

where  $\mathbf{z}_1$  is  $1 \times L_1$  (including a constant),  $\boldsymbol{\delta}_1$  is  $L_1 \times 1$ , and  $u_1$  is the unobserved disturbance. The set of all exogenous variables is denoted by the  $1 \times L$  vector  $\mathbf{z}$ , where  $\mathbf{z}_1$  is a strict subset of  $\mathbf{z}$ . The maintained exogeneity assumption is

$$\mathbf{E}(\mathbf{z}'u_1) = \mathbf{0} \tag{6.10}$$

It is important to keep in mind that condition (6.10) is assumed throughout this section. We also assume that equation (6.9) is identified when  $E(y_2u_1) \neq 0$ , which requires that  $\mathbf{z}$  have at least one element not in  $\mathbf{z}_1$  (the order condition); the rank condition is that at least one element of  $\mathbf{z}$  not in  $\mathbf{z}_1$  is partially correlated with  $y_2$  (after netting out  $\mathbf{z}_1$ ). Under these assumptions, we now wish to test the null hypothesis that  $y_2$  is actually exogenous.

Hausman (1978) suggested comparing the OLS and 2SLS estimators of  $\beta_1 \equiv (\delta'_1, \alpha_1)'$  as a formal test of endogeneity: if  $y_2$  is uncorrelated with  $u_1$ , the OLS and 2SLS estimators should differ only by sampling error. This reasoning leads to the **Hausman test** for endogeneity.

{133}------------------------------------------------

The original form of the statistic turns out to be cumbersome to compute because the matrix appearing in the quadratic form is singular, except when no exogenous variables are present in equation (6.9). As pointed out by Hausman (1978, 1983), there is a regression-based form of the test that turns out to be asymptotically equivalent to the original form of the Hausman test. In addition, it extends easily to other situations, including some nonlinear models that we cover in Chapters 15, 16, and 19.

To derive the regression-based test, write the linear projection of  $y_2$  on z in error form as

$$y_2 = \mathbf{z}\mathbf{\pi}_2 + v_2 \tag{6.11}$$

$$\mathbf{E}(\mathbf{z}'v_2) = \mathbf{0} \tag{6.12}$$

where  $\pi_2$  is  $L \times 1$ . Since  $u_1$  is uncorrelated with  $\mathbf{z}$ , it follows from equations (6.11) and (6.12) that  $y_2$  is endogenous if and only if  $\mathrm{E}(u_1v_2) \neq 0$ . Thus we can test whether the structural error,  $u_1$ , is correlated with the reduced form error,  $v_2$ . Write the linear projection of  $u_1$  onto  $v_2$  in error form as

$$u_1 = \rho_1 v_2 + e_1 \tag{6.13}$$

where  $\rho_1 = \mathrm{E}(v_2u_1)/\mathrm{E}(v_2^2)$ ,  $\mathrm{E}(v_2e_1) = 0$ , and  $\mathrm{E}(\mathbf{z}'e_1) = \mathbf{0}$  (since  $u_1$  and  $v_2$  are each orthogonal to  $\mathbf{z}$ ). Thus,  $y_2$  is exogenous if and only if  $\rho_1 = 0$ .

Plugging equation (6.13) into equation (6.9) gives the equation

$$y_1 = \mathbf{z}_1 \delta_1 + \alpha_1 y_2 + \rho_1 v_2 + e_1 \tag{6.14}$$

The key is that  $e_1$  is uncorrelated with  $\mathbf{z}_1$ ,  $y_2$ , and  $v_2$  by construction. Therefore, a test of  $\mathbf{H}_0$ :  $\rho_1=0$  can be done using a standard t test on the variable  $v_2$  in an OLS regression that includes  $\mathbf{z}_1$  and  $y_2$ . The problem is that  $v_2$  is not observed. Nevertheless, the reduced form parameters  $\pi_2$  are easily estimated by OLS. Let  $\hat{v}_2$  denote the OLS residuals from the first-stage reduced form regression of  $y_2$  on  $\mathbf{z}$ —remember that  $\mathbf{z}$  contains all exogenous variables. If we replace  $v_2$  with  $\hat{v}_2$  we have the equation

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + \rho_1 \hat{v}_2 + error \tag{6.15}$$

and  $\delta_1$ ,  $\alpha_1$ , and  $\rho_1$  can be consistently estimated by OLS. Now we can use the results on generated regressors in Section 6.1.1: the usual OLS t statistic for  $\hat{\rho}_1$  is a valid test of  $H_0$ :  $\rho_1 = 0$ , provided the homoskedasticity assumption  $E(u_1^2 | \mathbf{z}, y_2) = \sigma_1^2$  is satisfied under  $H_0$ . (Remember,  $y_2$  is exogenous under  $H_0$ .) A heteroskedasticity-robust t statistic can be used if heteroskedasticity is suspected under  $H_0$ .

{134}------------------------------------------------

As shown in Problem 5.1, the OLS estimates of  $\delta_1$  and  $\alpha_1$  from equation (6.15) are in fact *identical* to the 2SLS estimates. This fact is convenient because, along with being computationally simple, regression (6.15) allows us to compare the *magnitudes* of the OLS and 2SLS estimates in order to determine whether the differences are *practically* significant, rather than just finding statistically significant evidence of endogeneity of  $y_2$ . It also provides a way to verify that we have computed the statistic correctly.

We should remember that the OLS standard errors that would be reported from equation (6.15) are not valid unless  $\rho_1 = 0$ , because  $\hat{v}_2$  is a generated regressor. In practice, if we reject  $H_0$ :  $\rho_1 = 0$ , then, to get the appropriate standard errors and other test statistics, we estimate equation (6.9) by 2SLS.

Example 6.1 (Testing for Endogeneity of Education in a Wage Equation): Consider the wage equation

$$\log(wage) = \delta_0 + \delta_1 exper + \delta_2 exper^2 + \alpha_1 educ + u_1$$
(6.16)

for working women, where we believe that *educ* and  $u_1$  may be correlated. The instruments for *educ* are parents' education and husband's education. So, we first regress *educ* on 1, *exper*, *exper*<sup>2</sup>, *motheduc*, *fatheduc*, and *huseduc* and obtain the residuals,  $\hat{v}_2$ . Then we simply include  $\hat{v}_2$  along with unity, *exper*, *exper*<sup>2</sup>, and *educ* in an OLS regression and obtain the *t* statistic on  $\hat{v}_2$ . Using the data in MROZ.RAW gives the result  $\hat{\rho}_1 = .047$  and  $t_{\hat{\rho}_1} = 1.65$ . We find evidence of endogeneity of *educ* at the 10 percent significance level against a two-sided alternative, and so 2SLS is probably a good idea (assuming that we trust the instruments). The correct 2SLS standard errors are given in Example 5.3.

Rather than comparing the OLS and 2SLS estimates of a particular linear combination of the parameters—as the original Hausman test does—it often makes sense to compare just the estimates of the parameter of interest, which is usually  $\alpha_1$ . If, under  $H_0$ , Assumptions 2SLS.1–2SLS.3 hold with  $\mathbf{w}$  replacing  $\mathbf{z}$ , where  $\mathbf{w}$  includes all nonredundant elements in  $\mathbf{x}$  and  $\mathbf{z}$ , obtaining the test is straightforward. Under these assumptions it can be shown that  $\operatorname{Avar}(\hat{\alpha}_{1,2SLS} - \hat{\alpha}_{1,OLS}) = \operatorname{Avar}(\hat{\alpha}_{1,2SLS}) - \operatorname{Avar}(\hat{\alpha}_{1,OLS})$ . [This conclusion essentially holds because of Theorem 5.3; Problem 6.12 asks you to show this result formally. Hausman (1978), Newey and McFadden (1994, Section 5.3), and Section 14.5.1 contain more general treatments.] Therefore, the Hausman t statistic is simply  $(\hat{\alpha}_{1,2SLS} - \hat{\alpha}_{1,OLS})/\{[\operatorname{se}(\hat{\alpha}_{1,2SLS})]^2 - [\operatorname{se}(\hat{\alpha}_{1,OLS})]^2\}^{1/2}$ , where the standard errors are the usual ones computed under homoskedasticity. The denominator in the t statistic is the standard error of  $(\hat{\alpha}_{1,2SLS} - \hat{\alpha}_{1,OLS})$ . If there is

{135}------------------------------------------------

heteroskedasticity under  $H_0$ , this standard error is invalid because the asymptotic variance of the difference is no longer the difference in asymptotic variances.

Extending the regression-based Hausman test to several potentially endogenous explanatory variables is straightforward. Let  $\mathbf{y}_2$  denote a  $1 \times G_1$  vector of possible endogenous variables in the population model

$$y_1 = \mathbf{z}_1 \delta_1 + \mathbf{y}_2 a_1 + u_1, \qquad \mathbf{E}(\mathbf{z}' u_1) = \mathbf{0}$$
 (6.17)

where  $a_1$  is now  $G_1 \times 1$ . Again, we assume the rank condition for 2SLS. Write the reduced form as  $\mathbf{y}_2 = \mathbf{z}\Pi_2 + \mathbf{v}_2$ , where  $\Pi_2$  is  $L \times G_1$  and  $\mathbf{v}_2$  is the  $1 \times G_1$  vector of population reduced form errors. For a generic observation let  $\hat{\mathbf{v}}_2$  denote the  $1 \times G_1$  vector of OLS residuals obtained from each reduced form. (In other words, take each element of  $\mathbf{y}_2$  and regress it on  $\mathbf{z}$  to obtain the RF residuals; then collect these in the row vector  $\hat{\mathbf{v}}_2$ .) Now, estimate the model

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \mathbf{y}_2 \boldsymbol{a}_1 + \hat{\mathbf{v}}_2 \boldsymbol{\rho}_1 + error \tag{6.18}$$

and do a standard F test of  $H_0$ :  $\rho_1 = \mathbf{0}$ , which tests  $G_1$  restrictions in the unrestricted model (6.18). The restricted model is obtained by setting  $\rho_1 = \mathbf{0}$ , which means we estimate the original model (6.17) by OLS. The test can be made robust to heteroskedasticity in  $u_1$  (since  $u_1 = e_1$  under  $H_0$ ) by applying the heteroskedasticity-robust Wald statistic in Chapter 4. In some regression packages, such as Stata®, the robust test is implemented as an F-type test.

An alternative to the F test is an LM-type test. Let  $\hat{u}_1$  be the OLS residuals from the regression  $y_1$  on  $\mathbf{z}_1$ ,  $\mathbf{y}_2$  (the residuals obtained under the null that  $\mathbf{y}_2$  is exogenous). Then, obtain the usual R-squared (assuming that  $\mathbf{z}_1$  contains a constant), say  $R_u^2$ , from the regression

$$\hat{\boldsymbol{u}}_1 \text{ on } \mathbf{z}_1, \mathbf{y}_2, \hat{\mathbf{v}}_2 \tag{6.19}$$

and use  $NR_u^2$  as asymptotically  $\chi_{G_1}^2$ . This test again maintains homoskedasticity under  $H_0$ . The test can be made heteroskedasticity-robust using the method described in equation (4.17): take  $\mathbf{x}_1 = (\mathbf{z}_1, \mathbf{y}_2)$  and  $\mathbf{x}_2 = \hat{\mathbf{v}}_2$ . See also Wooldridge (1995b).

Example 6.2 (Endogeneity of Education in a Wage Equation, continued): We add the interaction term black·educ to the log(wage) equation estimated by Card (1995); see also Problem 5.4. Write the model as

$$\log(wage) = \alpha_1 e duc + \alpha_2 b lack \cdot e duc + \mathbf{z_1} \boldsymbol{\delta}_1 + u_1 \tag{6.20}$$

where  $\mathbf{z}_1$  contains a constant, exper, exper<sup>2</sup>, black, smsa, 1966 regional dummy variables, and a 1966 SMSA indicator. If educ is correlated with  $u_1$ , then we also expect

{136}------------------------------------------------

blackeduc to be correlated with u1. If nearc4, a binary indicator for whether a worker grew up near a four-year college, is valid as an instrumental variable for educ, then a natural instrumental variable for blackeduc is blacknearc4. Note that blacknearc4 is uncorrelated with u<sup>1</sup> under the conditional mean assumption Eðu<sup>1</sup> j zÞ ¼ 0, where z contains all exogenous variables.

The equation estimated by OLS is

$$\log(\hat{w}age) = 4.81 + .071 \ educ + .018 \ black \cdot educ - .419 \ black + \cdots$$

$$(0.75) \quad (.004) \quad (.006) \quad (.079)$$

Therefore, the return to education is estimated to be about 1.8 percentage points higher for blacks than for nonblacks, even though wages are substantially lower for blacks at all but unrealistically high levels of education. (It takes an estimated 23.3 years of education before a black worker earns as much as a nonblack worker.)

To test whether educ is exogenous we must test whether educ and blackeduc are uncorrelated with u1. We do so by first regressing educ on all instrumental variables: those elements in z<sup>1</sup> plus nearc4 and blacknearc4. (The interaction blacknearc4 should be included because it might be partially correlated with educ.) Let v^<sup>21</sup> be the OLS residuals from this regression. Similarly, regress blackeduc on z1, nearc4, and blacknearc4, and save the residuals v^22. By the way, the fact that the dependent variable in the second reduced form regression, blackeduc, is zero for a large fraction of the sample has no bearing on how we test for endogeneity.

Adding v^<sup>21</sup> and v^<sup>22</sup> to the OLS regression and computing the joint F test yields F ¼ 0:54 and p-value ¼ 0.581; thus we do not reject exogeneity of educ and blackeduc.

Incidentally, the reduced form regressions confirm that educ is partially correlated with nearc4 (but not blacknearc4) and blackeduc is partially correlated with blacknearc4 (but not nearc4). It is easily seen that these findings mean that the rank condition for 2SLS is satisfied—see Problem 5.15c. Even though educ does not appear to be endogenous in equation (6.20), we estimate the equation by 2SLS:

$$\log(\hat{w}age) = 3.84 + .127 \ educ + .011 \ black \cdot educ - .283 \ black + \cdots$$

$$(0.97) \quad (.057) \quad (.040) \quad (.506)$$

The 2SLS point estimates certainly differ from the OLS estimates, but the standard errors are so large that the 2SLS and OLS estimates are not statistically different.