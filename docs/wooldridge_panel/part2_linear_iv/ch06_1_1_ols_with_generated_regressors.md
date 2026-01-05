# OLS with Generated Regressors

> Pages: 129-132

We often need to draw on results for OLS estimation when one or more of the regressors have been estimated from a first-stage procedure. To illustrate the issues, consider the model

$$y = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + \gamma q + u$$
 (6.1)

We observe x1; ... ; xK , but q is unobserved. However, suppose that q is related to observable data through the function q ¼ fðw; *d*Þ, where f is a known function and w is a vector of observed variables, but the vector of parameters *d* is unknown (which is why q is not observed). Often, but not always, q will be a linear function of w and *d*. Suppose that we can consistently estimate *d*, and let ^*d* be the estimator. For each observation <sup>i</sup>, <sup>q</sup>^<sup>i</sup> <sup>¼</sup> <sup>f</sup>ðwi; ^*d*<sup>Þ</sup> effectively estimates qi. Pagan (1984) calls <sup>q</sup>^<sup>i</sup> <sup>a</sup> generated regressor. It seems reasonable that, replacing qi with q^<sup>i</sup> in running the OLS regression

$$y_i \text{ on } 1, x_{i1}, x_{i2}, \dots, x_{ik}, \hat{q}_i, \qquad i = 1, \dots, N$$
 (6.2)

should produce consistent estimates of all parameters, including g. The question is, What assumptions are sufficient?

While we do not cover the asymptotic theory needed for a careful proof until Chapter 12 (which treats nonlinear estimation), we can provide some intuition here. Because plim ^*d* ¼ *d*, by the law of large numbers it is reasonable that

$$N^{-1} \sum_{i=1}^{N} \hat{q}_i u_i \xrightarrow{p} E(q_i u_i), \qquad N^{-1} \sum_{i=1}^{N} x_{ij} \hat{q}_i \xrightarrow{p} E(x_{ij} q_i)$$

From this relation it is easily shown that the usual OLS assumption in the population that u is uncorrelated with ðx1; x2; ... ; xK ; qÞ—suffices for the two-step procedure to be consistent (along with the rank condition of Assumption OLS.2 applied to the expanded vector of explanatory variables). In other words, for consistency, replacing qi with q^<sup>i</sup> in an OLS regression causes no problems.

Things are not so simple when it comes to inference: the standard errors and test statistics obtained from regression (6.2) are generally invalid because they ignore the sampling variation in ^*d*. Since ^*d* is also obtained using data—usually the same sample of data—uncertainty in the estimate should be accounted for in the second step. Nevertheless, there is at least one important case where the sampling variation of ^*d* can be ignored, at least asymptotically: if

{130}------------------------------------------------

$$E[\nabla_{\delta} f(\mathbf{w}, \boldsymbol{\delta})' u] = \mathbf{0} \tag{6.3}$$

$$\gamma = 0 \tag{6.4}$$

then the  $\sqrt{N}$ -limiting distribution of the OLS estimators from regression (6.2) is the *same* as the OLS estimators when q replaces  $\hat{q}$ . Condition (6.3) is implied by the zero conditional mean condition

$$\mathbf{E}(u\,|\,\mathbf{x},\mathbf{w}) = 0\tag{6.5}$$

which usually holds in generated regressor contexts.

We often want to test the null hypothesis  $H_0$ :  $\gamma = 0$  before including  $\hat{q}$  in the final regression. Fortunately, the usual t statistic on  $\hat{q}$  has a limiting standard normal distribution under  $H_0$ , so it can be used to test  $H_0$ . It simply requires the usual homoskedasticity assumption,  $E(u^2 | \mathbf{x}, q) = \sigma^2$ . The heteroskedasticity-robust statistic works if heteroskedasticity is present in u under  $H_0$ .

Even if condition (6.3) holds, if  $\gamma \neq 0$ , then an adjustment is needed for the asymptotic variances of *all* OLS estimators that are due to estimation of  $\delta$ . Thus, standard t statistics, F statistics, and LM statistics will not be asymptotically valid when  $\gamma \neq 0$ . Using the methods of Chapter 3, it is not difficult to derive an adjustment to the usual variance matrix estimate that accounts for the variability in  $\hat{\delta}$  (and also allows for heteroskedasticity). It is *not* true that replacing  $q_i$  with  $\hat{q}_i$  simply introduces heteroskedasticity into the error term; this is not the correct way to think about the generated regressors issue. Accounting for the fact that  $\hat{\delta}$  depends on the same random sample used in the second-stage estimation is much different from having heteroskedasticity in the error. Of course, we might want to use a heteroskedasticity-robust standard error for testing  $H_0$ :  $\gamma = 0$  because heteroskedasticity in the population error u can always be a problem. However, just as with the usual OLS standard error, this is generally justified only under  $H_0$ :  $\gamma = 0$ .

A general formula for the asymptotic variance of 2SLS in the presence of generated regressors is given in the appendix to this chapter; this covers OLS with generated regressors as a special case. A general framework for handling these problems is given in Newey (1984) and Newey and McFadden (1994), but we must hold off until Chapter 14 to give a careful treatment.

#### **6.1.2 2SLS with Generated Instruments**

In later chapters we will need results on 2SLS estimation when the instruments have been estimated in a preliminary stage. Write the population model as


{131}------------------------------------------------

$$y = \mathbf{x}\boldsymbol{\beta} + u \tag{6.6}$$

$$\mathbf{E}(\mathbf{z}'u) = \mathbf{0} \tag{6.7}$$

where  $\mathbf{x}$  is a  $1 \times K$  vector of explanatory variables and  $\mathbf{z}$  is a  $1 \times L$  ( $L \ge K$ ) vector of intrumental variables. Assume that  $\mathbf{z} = \mathbf{g}(\mathbf{w}, \lambda)$ , where  $\mathbf{g}(\cdot, \lambda)$  is a known function but  $\lambda$  needs to be estimated. For each i, define the **generated instruments**  $\hat{\mathbf{z}}_i \equiv \mathbf{g}(\mathbf{w}_i, \hat{\lambda})$ . What can we say about the 2SLS estimator when the  $\hat{\mathbf{z}}_i$  are used as instruments?

By the same reasoning for OLS with generated regressors, consistency follows under weak conditions. Further, under conditions that are met in many applications, we can ignore the fact that the instruments were estimated in using 2SLS for inference. Sufficient are the assumptions that  $\hat{\lambda}$  is  $\sqrt{N}$ -consistent for  $\lambda$  and that

$$E[\nabla_{\lambda} \mathbf{g}(\mathbf{w}, \lambda)' u] = \mathbf{0} \tag{6.8}$$

Under condition (6.8), which holds when  $E(u | \mathbf{w}) = 0$ , the  $\sqrt{N}$ -asymptotic distribution of  $\hat{\boldsymbol{\beta}}$  is the *same* whether we use  $\lambda$  or  $\hat{\lambda}$  in constructing the instruments. This fact greatly simplifies calculation of asymptotic standard errors and test statistics. Therefore, if we have a choice, there are practical reasons for using 2SLS with generated instruments rather than OLS with generated regressors. We will see some examples in Part IV.

One consequence of this discussion is that, if we add the 2SLS homoskedasticity assumption (2SLS.3), the usual 2SLS standard errors and test statistics are asymptotically valid. If Assumption 2SLS.3 is violated, we simply use the heteroskedasticity-robust standard errors and test statistics. Of course, the finite sample properties of the estimator using  $\hat{\mathbf{z}}_i$  as instruments could be notably different from those using  $\mathbf{z}_i$  as instruments, especially for small sample sizes. Determining whether this is the case requires either more sophisticated asymptotic approximations or simulations on a case-by-case basis.

# **6.1.3** Generated Instruments and Regressors

We will encounter examples later where some instruments and some regressors are estimated in a first stage. Generally, the asymptotic variance needs to be adjusted because of the generated regressors, although there are some special cases where the usual variance matrix estimators are valid. As a general example, consider the model

$$y = \mathbf{x}\boldsymbol{\beta} + \gamma f(\mathbf{w}, \boldsymbol{\delta}) + u, \qquad \mathbf{E}(u \,|\, \mathbf{z}, \mathbf{w}) = 0$$

and we estimate  $\delta$  in a first stage. If  $\gamma = 0$ , then the 2SLS estimator of  $(\beta', \gamma)'$  in the equation

{132}------------------------------------------------

$$y_i = \mathbf{x}_i \boldsymbol{\beta} + \gamma \hat{f}_i + error_i$$

using instruments  $(\mathbf{z}_i, \hat{f}_i)$ , has a limiting distribution that does not depend on the limiting distribution of  $\sqrt{N}(\hat{\boldsymbol{\delta}} - \boldsymbol{\delta})$  under conditions (6.3) and (6.8). Therefore, the usual 2SLS t statistic for  $\hat{\gamma}$ , or its heteroskedsticity-robust version, can be used to test  $H_0$ :  $\gamma = 0$ .