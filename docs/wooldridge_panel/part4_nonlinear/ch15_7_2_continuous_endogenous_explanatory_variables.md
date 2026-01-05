# Continuous Endogenous Explanatory Variables

> Pages: 481-486

We now explicitly allow for the case where one of the explanatory variables is correlated with the error term in the latent variable model. One possibility is to estimate a linear probability model by 2SLS. This procedure is relatively easy and might provide a good estimate of the average effect.

If we want to estimate a probit model with an endogenous explanatory variables, we must make some fairly strong assumptions. In this section we consider the case of a continuous endogenous explanatory variable.

Write the model as

$$y_1^* = \mathbf{z}_1 \delta_1 + \alpha_1 y_2 + u_1 \tag{15.39}$$

$$y_2 = \mathbf{z}_1 \delta_{21} + \mathbf{z}_2 \delta_{22} + v_2 = \mathbf{z} \delta_2 + v_2 \tag{15.40}$$

$$y_1 = 1[y_1^* > 0] (15.41)$$

where ðu1; v2Þ has a zero mean, bivariate normal distribution and is independent of z. Equation (15.39), along with equation (15.41), is the structural equation; equation (15.40) is a reduced form for y2, which is endogenous if u<sup>1</sup> and v<sup>2</sup> are correlated. If u<sup>1</sup> and v<sup>2</sup> are independent, there is no endogeneity problem. Because v<sup>2</sup> is normally distributed, we are assuming that y<sup>2</sup> given z is normal; thus y<sup>2</sup> should have features of a normal random variable. (For example, y<sup>2</sup> should not be a discrete variable.)

{482}------------------------------------------------

The model is applicable when  $y_2$  is correlated with  $u_1$  because of omitted variables or measurement error. It can also be applied to the case where  $y_2$  is determined jointly with  $y_1$ , but with a caveat. If  $y_1$  appears on the right-hand side in a linear structural equation for  $y_2$ , then the reduced form for  $y_2$  cannot be found with  $v_2$  having the stated properties. However, if  $y_1^*$  appears in a linear structural equation for  $y_2$ , then  $y_2$  has the reduced form given by equation (15.40); see Maddala (1983, Chapter 7) for further discussion.

The normalization that gives the parameters in equation (15.39) an average partial effect interpretation, at least in the omitted variable and simultaneity contexts, is  $Var(u_1) = 1$ , just as in a probit model with all explanatory variables exogenous. To see this point, consider the outcome on  $y_1$  at two different outcomes of  $y_2$ , say  $\bar{y}_2$  and  $\bar{y}_2 + 1$ . Holding the observed exogenous factors fixed at  $\bar{z}_1$ , and holding  $u_1$  fixed, the difference in responses is

$$1[\overline{\mathbf{z}}_1\boldsymbol{\delta}_1 + \alpha_1(\overline{y}_2 + 1) + u_1 \ge 0] - 1[\overline{\mathbf{z}}_1\boldsymbol{\delta}_1 + \alpha_1\overline{y}_2 + u_1 \ge 0]$$

(This difference can take on the values -1, 0, and 1.) Because  $u_1$  is unobserved, we cannot estimate the difference in responses for a given population unit. Nevertheless, if we average across the distribution of  $u_1$ , which is Normal(0, 1), we obtain

$$\Phi[\overline{\mathbf{z}}_1\boldsymbol{\delta}_1 + \alpha_1(\overline{y}_2 + 1)] - \Phi(\overline{\mathbf{z}}_1\boldsymbol{\delta}_1 + \alpha_1\overline{y}_2)$$

Therefore,  $\delta_1$  and  $\alpha_1$  are the parameters appearing in the APE. [Alternatively, if we begin by allowing  $\sigma_1^2 = \text{Var}(u_1) > 0$  to be unrestricted, the APE would depend on  $\delta_1/\sigma_1$  and  $\alpha_1/\sigma_1$ , and so we should just rescale  $u_1$  to have unit variance. The variance and slope parameters are not separately identified, anyway.] The proper normalization for  $\text{Var}(u_1)$  should be kept in mind, as two-step procedures, which we cover in the following paragraphs, only consistently estimate  $\delta_1$  and  $\alpha_1$  up to scale; we have to do a little more work to obtain estimates of the APE. If  $y_2$  is a mismeasured variable, we apparently cannot estimate the APE of interest: we would like to estimate the change in the response probability due to a change in  $y_2^*$ , but, without further assumptions, we can only estimate the effect of changing  $y_2$ .

The most useful two-step approach is due to Rivers and Vuong (1988), as it leads to a simple test for endogeneity of  $y_2$ . To derive the procedure, first note that, under joint normality of  $(u_1, v_2)$ , with  $Var(u_1) = 1$ , we can write

$$u_1 = \theta_1 v_2 + e_1 \tag{15.42}$$

where  $\theta_1 = \eta_1/\tau_2^2$ ,  $\eta_1 = \text{Cov}(v_2, u_1)$ ,  $\tau_2^2 = \text{Var}(v_2)$ , and  $e_1$  is independent of **z** and  $v_2$  (and therefore of  $v_2$ ). Because of joint normality of  $(u_1, v_2)$ ,  $e_1$  is also normally

{483}------------------------------------------------

distributed with  $E(e_1) = 0$  and  $Var(e_1) = Var(u_1) - \eta_1^2/\tau_2^2 = 1 - \rho_1^2$ , where  $\rho_1 = Corr(v_2, u_1)$ . We can now write

$$y_1^* = \mathbf{z}_1 \delta_1 + \alpha_1 y_2 + \theta_1 v_2 + e_1 \tag{15.43}$$

$$e_1 \mid \mathbf{z}, y_2, v_2 \sim \text{Normal}(0, 1 - \rho_1^2)$$
 (15.44)

A standard calculation shows that

$$P(y_1 = 1 | \mathbf{z}, y_2, v_2) = \Phi[(\mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + \theta_1 v_2)/(1 - \rho_1^2)^{1/2}]$$

Assuming for the moment that we observe  $v_2$ , then probit of  $y_1$  on  $\mathbf{z}_1$ ,  $y_2$ , and  $v_2$  consistently estimates  $\boldsymbol{\delta}_{\rho 1} \equiv \boldsymbol{\delta}_1/(1-\rho_1^2)^{1/2}$ ,  $\alpha_{\rho 1} \equiv \alpha_1/(1-\rho_1^2)^{1/2}$ , and  $\theta_{\rho 1} \equiv \theta_1/(1-\rho_1^2)^{1/2}$ . Notice that because  $\rho_1^2 < 1$ , each scaled coefficient is greater than its unscaled counterpart unless  $y_2$  is exogenous  $(\rho_1 = 0)$ .

Since we do not know  $\delta_2$ , we must first estimate it, as in the following procedure:

*Procedure 15.1:* (a) Run the OLS regression  $y_2$  on **z** and save the residuals  $\hat{v}_2$ .

(b) Run the probit  $y_1$  on  $\mathbf{z}_1$ ,  $y_2$ ,  $\hat{v}_2$  to get consistent estimators of the scaled coefficients  $\delta_{\rho 1}$ ,  $\alpha_{\rho 1}$ , and  $\theta_{\rho 1}$ .

A nice feature of Procedure 15.1 is that the usual probit t statistic on  $\hat{v}_2$  is a valid test of the null hypothesis that  $y_2$  is exogenous, that is,  $H_0$ :  $\theta_1 = 0$ . If  $\theta_1 \neq 0$ , the usual probit standard errors and test statistics are not strictly valid, and we have only estimated  $\delta_1$  and  $\alpha_1$  up to scale. The asymptotic variance of the two-step estimator can be derived using the M-estimator results in Section 12.5.2; see also Rivers and Vuong (1988).

Under  $H_0$ :  $\theta_1 = 0$ ,  $e_1 = u_1$ , and so the distribution of  $v_2$  plays no role under the null. Therefore, the *test* of exogeneity is valid without assuming normality or homoskedasticity of  $v_2$ , and it can be applied very broadly, even if  $v_2$  is a binary variable. Unfortunately, if  $v_2$  and  $v_1$  are correlated, normality of  $v_2$  is crucial.

Example 15.3 (Testing for Exogeneity of Education in the Women's LFP Model): We test the null hypothesis that educ is exogenous in the married women's labor force participation equation. We first obtain the reduced form residuals,  $\hat{v}_2$ , from regressing educ on all exogenous variables, including motheduc, fatheduc, and huseduc. Then, we add  $\hat{v}_2$  to the probit from Example 15.2. The t statistic on  $\hat{v}_2$  is only .867, which is weak evidence against the null hypothesis that educ is exogenous. As always, this conclusion hinges on the assumption that the instruments for educ are themselves exogenous.

Even when  $\theta_1 \neq 0$ , it turns out that we can consistently estimate the average partial effects after the two-stage estimation. We simply apply the results from Section 2.2.5.

{484}------------------------------------------------

To see how, write  $y_1 = 1[\mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1 > 0]$ , where, in the notation of Section 2.2.5,  $q \equiv u_1$ ,  $\mathbf{x} \equiv (\mathbf{z}_1, y_2)$ , and  $\mathbf{w} \equiv v_2$  (a scalar in this case). Because  $y_1$  is a deterministic function of  $(\mathbf{z}_1, y_2, u_1)$ ,  $v_2$  is trivially redundant in  $E(y_1 | \mathbf{z}_1, y_2, u_1)$ , and so equation (2.34) holds. Further, as we have already used,  $u_1$  given  $(\mathbf{z}_1, y_2, v_2)$  is independent of  $(\mathbf{z}_1, y_2)$ , and so equation (2.33) holds as well. It follows from Section 2.2.5 that the APEs are obtained by taking derivatives (or differences) of

$$E_{v_2}[\Phi(\mathbf{z}_1 \delta_{\rho 1} + \alpha_{\rho 1} y_2 + \theta_{\rho 1} v_2)]$$
 (15.45)

where we still use the  $\rho$  subscript to denote the scaled coefficients. But we computed exactly this kind of expectation in Section 15.7.1. The same reasoning gives

$$\mathbf{E}_{v}, [\Phi(\mathbf{z}_{1}\boldsymbol{\delta}_{\theta 1} + \alpha_{\theta 1}y_{2} + \theta_{\theta 1}v_{2})] = \Phi(\mathbf{z}_{1}\boldsymbol{\delta}_{\theta 1} + \alpha_{\theta 1}y_{2})$$

where  $\delta_{\theta 1} \equiv \delta_{\rho 1}/(\theta_{\rho 1}^2 \tau_2^2 + 1)^{1/2}$  and  $\alpha_{\theta 1} \equiv \alpha_{\rho 1}/(\theta_{\rho 1}^2 \tau_2^2 + 1)^{1/2}$ , where  $\tau_2^2 = \text{Var}(v_2)$ . Therefore, for any  $(\mathbf{z}_1, y_2)$ , a consistent estimator of expression (15.45) is

$$\Phi(\mathbf{z}_1 \hat{\boldsymbol{\delta}}_{\theta 1} + \hat{\alpha}_{\theta 1} y_2) \tag{15.46}$$

where  $\hat{\delta}_{\theta 1} \equiv \hat{\delta}_{\rho 1}/(\hat{\theta}_{\rho 1}^2\hat{\tau}_2^2+1)^{1/2}$  and  $\hat{\alpha}_{\theta 1} \equiv \hat{\alpha}_{\rho 1}/(\hat{\theta}_{\rho 1}^2\hat{\tau}_2^2+1)^{1/2}$ . Note that  $\hat{\tau}_2^2$  is the usual error variance estimator from the first-stage regression of  $y_2$  on z. Expression (15.46) implies a very simple way to obtain the estimated APEs after the second-stage probit. We simply divide each coefficient by the factor  $(\hat{\theta}_{\rho 1}^2\hat{\tau}_2^2+1)^{1/2}$  before computing derivatives or differences with respect to the elements of  $(z_1, y_2)$ . Unfortunately, because the APEs depend on the parameters in a complicated way—and the asymptotic variance of  $(\hat{\delta}'_{\rho 1}, \hat{\alpha}_{\rho 1}, \hat{\theta}_{\rho 1})'$  is already complicated because of the two-step estimation—standard errors for the APEs would be very difficult to come by using the delta method.

An alternative method for estimating the APEs does not exploit the normality assumption for  $v_2$ . By the usual uniform weak law of large numbers argument—see Lemma 12.1—a consistent estimator of expression (15.45) for any  $(\mathbf{z}_1, y_2)$  is obtained by replacing unknown parameters by consistent estimators:

$$N^{-1} \sum_{i=1}^{N} \Phi(\mathbf{z}_{1} \hat{\boldsymbol{\delta}}_{\rho 1} + \hat{\alpha}_{\rho 1} y_{2} + \hat{\theta}_{\rho 1} \hat{v}_{i2})$$
(15.47)

where the  $\hat{v}_{i2}$  are the first-stage OLS residuals from regressing  $y_{i2}$  on  $\mathbf{z}_i$ , i = 1, ..., N. This approach provides a different strategy for estimating APEs: simply compute partial effects with respect to  $\mathbf{z}_1$  and  $y_2$  after the second-stage estimation, but then average these across the  $\hat{v}_{i2}$  in the sample.

Rather than use a two-step procedure, we can estimate equations (15.39)–(15.41) by conditional maximum likelihood. To obtain the joint distribution of  $(y_1, y_2)$ ,

{485}------------------------------------------------

conditional on z, recall that

$$f(y_1, y_2 | \mathbf{z}) = f(y_1 | y_2, \mathbf{z}) f(y_2 | \mathbf{z})$$
(15.48)

(see Property CD.2 in Appendix 13A). Since  $y_2 | \mathbf{z} \sim \text{Normal}(\mathbf{z}\boldsymbol{\delta}_2, \tau_2^2)$ , the density  $f(y_2 | \mathbf{z})$  is easy to write down. We can also derive the conditional density of  $y_1$  given  $(y_2, \mathbf{z})$ . Since  $v_2 = y_2 - \mathbf{z}\boldsymbol{\delta}_2$  and  $y_1 = 1[y_1^* > 0]$ ,

$$P(y_1 = 1 \mid y_2, \mathbf{z}) = \Phi \left[ \frac{\mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + (\rho_1 / \tau_2)(y_2 - \mathbf{z} \boldsymbol{\delta}_2)}{(1 - \rho_1^2)^{1/2}} \right]$$
(15.49)

where we have used the fact that  $\theta_1 = \rho_1/\tau_2$ .

Let w denote the term in inside  $\Phi(\cdot)$  in equation (15.49). Then we have derived

$$f(y_1, y_2 | \mathbf{z}) = \{\Phi(w)\}^{y_1} \{1 - \Phi(w)\}^{1 - y_1} (1/\tau_2) \phi[(y_2 - \mathbf{z}\boldsymbol{\delta}_2)/\tau_2]$$

and so the log likelihood for observation i (apart from terms not depending on the parameters) is

$$y_{i1} \log \Phi(w_i) + (1 - y_{i1}) \log[1 - \Phi(w_i)] - \frac{1}{2} \log(\tau_2^2) - \frac{1}{2} (y_{i2} - \mathbf{z}_i \delta_2)^2 / \tau_2^2$$
 (15.50)

where we understand that  $w_i$  depends on the parameters  $(\delta_1, \alpha_1, \rho_1, \delta_2, \tau_2)$ :

$$w_i \equiv [\mathbf{z}_{i1}\boldsymbol{\delta}_1 + \alpha_1 y_{i2} + (\rho_1/\tau_2)(y_{i2} - \mathbf{z}_i\boldsymbol{\delta}_2)]/(1 - \rho_1^2)^{1/2}$$

Summing expression (15.50) across all i and maximizing with respect to all parameters gives the MLEs of  $\delta_1$ ,  $\alpha_1$ ,  $\rho_1$ ,  $\delta_2$ ,  $\tau_2^2$ . The general theory of conditional MLE applies, and so standard errors can be obtained using the estimated Hessian, the estimated expected Hessian, or the outer product of the score.

Maximum likelihood estimation has some decided advantages over two-step procedures. First, MLE is more efficient than any two-step procedure. Second, we get direct estimates of  $\delta_1$  and  $\alpha_1$ , the parameters of interest for computing partial effects. Evans, Oates, and Schwab (1992) study peer effects on teenage behavior using the full MLE.

Testing that  $y_2$  is exogenous is easy once the MLE has been obtained: just test  $H_0$ :  $\rho_1 = 0$  using an asymptotic t test. We could also use a likelihood ratio test.

The drawback with the MLE is computational. Sometimes it can be difficult to get the iterations to converge, as  $\hat{\rho}_1$  sometimes tends toward 1 or -1.

Comparing the Rivers-Vuong approach to the MLE shows that the former is a **limited information procedure**. Essentially, Rivers and Vuong focus on  $f(y_1 | y_2, \mathbf{z})$ , where they replace the unknown  $\delta_2$  with the OLS estimator  $\hat{\delta}_2$  (and they ignore the rescaling problem by taking  $e_1$  in equation (15.43) to have unit variance). MLE esti-

{486}------------------------------------------------

mates the parameters using the information in fðy<sup>1</sup> j y2; zÞ and fðy<sup>2</sup> j zÞ simultaneously. For the initial test of whether y<sup>2</sup> is exogenous, the Rivers-Vuong approach has significant computational advantages. If exogeneity is rejected, it is probably worth doing MLE.

Another benefit of the maximum likelihood approach for this and related problems is that it forces discipline on us in coming up with consistent estimation procedures and correct standard errors. It is easy to abuse two-step procedures if we are not careful in deriving estimating equations. With MLE, although it can be difficult to derive joint distributions of the endogenous variables given the exogenous variables, we know that, if the underlying distributional assumptions hold, consistent and effi cient estimators are obtained.