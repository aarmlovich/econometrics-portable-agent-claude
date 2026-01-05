# Models under Sequential Moment Restrictions

> Pages: 310-316

In Chapter 10 all the estimation methods we studied assumed that the explanatory variables were strictly exogenous (conditional on an unobserved effect in the case of fixed effects and first differencing). As we saw in the examples in Section 10.2.3, strict exogeneity rules out certain kinds of feedback from yit to future values of xit. Generally, random effects, fixed effects, and first differencing are inconsistent if an explanatory variable in some time period is correlated with uit. While the size of the inconsistency might be small—something we will investigate further—in other cases it can be substantial. Therefore, we should have general ways of obtaining consistent estimators as N ! y with T fixed when the explanatory variables are not strictly exogenous.

The model of interest can still be written as

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + c_i + u_{it}, \qquad t = 1, 2, \dots, T$$
 (11.1)

but, in addition to allowing ci and xit to be arbitrarily correlated, we now allow uit to be correlated with future values of the explanatory variables, ðx<sup>i</sup>;tþ<sup>1</sup>; x<sup>i</sup>;tþ<sup>2</sup>; ... ; xiT Þ. We saw in Example 10.3 that uit and xi;tþ<sup>1</sup> must be correlated because xi;tþ<sup>1</sup> ¼ yit. Nevertheless, there are many models, including the AR(1) model, for which it is reasonable to assume that uit is uncorrelated with current and past values of xit. Following Chamberlain (1992b), we introduce sequential moment restrictions:

$$E(u_{it} | \mathbf{x}_{it}, \mathbf{x}_{i,t-1}, \dots, \mathbf{x}_{i1}, c_i) = 0, \qquad t = 1, 2, \dots, T$$
(11.2)

When assumption (11.2) holds, we will say that the xit are sequentially exogenous conditional on the unobserved effect.


{311}------------------------------------------------

Given model (11.1), assumption (11.2) is equivalent to

$$E(y_{it} | \mathbf{x}_{it}, \mathbf{x}_{i,t-1}, \dots, \mathbf{x}_{i1}, c_i) = E(y_{it} | \mathbf{x}_{it}, c_i) = \mathbf{x}_{it}\boldsymbol{\beta} + c_i$$

$$(11.3)$$

which makes it clear what sequential exogeneity implies about the explanatory variables: after xit and ci have been controlled for, no past values of xit affect the expected value of yit. This condition is more natural than the strict exogeneity assumption, which requires conditioning on future values of xit as well.

Example 11.1 (Dynamic Unobserved Effects Model): An AR(1) model with additional explanatory variables is

$$y_{it} = \mathbf{z}_{it} \mathbf{y} + \rho_1 y_{i,t-1} + c_i + u_{it}$$
 (11.4)

and so xit 1 ðzit; yi;t1Þ. Therefore, ðxit; xi;t<sup>1</sup>; ... ; xi1Þ¼ðzit; yi;t<sup>1</sup>; zi;t<sup>1</sup>; ... ; zi1; yi0Þ, and the sequential exogeneity assumption (11.3) requires

$$E(y_{it} | \mathbf{z}_{it}, y_{i,t-1}, \mathbf{z}_{i,t-1}, \dots, \mathbf{z}_{i1}, y_{i0}, c_i) = E(y_{it} | \mathbf{z}_{it}, y_{i,t-1}, c_i)$$

$$= \mathbf{z}_{it} \gamma + \rho_1 y_{i,t-1} + c_i$$
(11.5)

An interesting hypothesis in this model is H0: r<sup>1</sup> ¼ 0, which means that, after unobserved heterogeneity, ci, has been controlled for (along with current and past zit), yi;t<sup>1</sup> does not help to predict yit. When r<sup>1</sup> 0 0, we say that fyitg exhibits state dependence: the current state depends on last period's state, even after controlling for ci and ðzit; ... ; zi1Þ.

In this example, assumption (11.5) is an example of dynamic completeness conditional on ci; we covered the unconditional version of dynamic completeness in Section 7.8.2. It means that one lag of yit is sufficient to capture the dynamics in the conditional expectation; neither further lags of yit nor lags of zit are important once ðzit; yi;t<sup>1</sup>; ciÞ have been controlled for. In general, if xit contains yi;t1, then assumption (11.3) implies dynamic completeness conditional on ci.

Assumption (11.3) does not require that z<sup>i</sup>;tþ<sup>1</sup> ... ; ziT be uncorrelated with uit, so that feedback is allowed from yit to ðz<sup>i</sup>;tþ<sup>1</sup>; ... ; ziT Þ. If we think that zis is uncorrelated with uit for all s, then additional orthogonality conditions can be used. Finally, we do not need to restrict the value of r<sup>1</sup> in any way because we are doing fixed-T asymptotics; the arguments from Section 7.8.3 are also valid here.

Example 11.2 (Static Model with Feedback): Consider a static panel data model

$$y_{it} = \mathbf{z}_{it}\mathbf{y} + \delta w_{it} + c_i + u_{it} \tag{11.6}$$

where zit is strictly exogenous and wit is sequentially exogenous:

{312}------------------------------------------------

$$E(u_{it} | \mathbf{z}_i, w_{it}, w_{i,t-1}, \dots, w_{i1}, c_i) = 0$$
(11.7)

However,  $w_{it}$  is influenced by past  $y_{it}$ , as in this case:

$$w_{it} = \mathbf{z}_{it}\boldsymbol{\xi} + \rho_1 y_{i,t-1} + \psi c_i + r_{it}$$
(11.8)

For example, let  $y_{it}$  be per capita condom sales in city i during year t, and let  $w_{it}$  be the HIV infection rate for year t. Model (11.6) can be used to test whether condom usage is influenced by the spread of HIV. The unobserved effect  $c_i$  contains city-specific unobserved factors that can affect sexual conduct, as well as the incidence of HIV. Equation (11.8) is one way of capturing the fact that the spread of HIV is influenced by past condom usage. Generally, if  $E(r_{i,t+1}u_{it}) = 0$ , it is easy to show that  $E(w_{i,t+1}u_{it}) = \rho_1 E(y_{it}u_{it}) = \rho_1 E(u_{it}^2) > 0$  under equations (11.7) and (11.8), and so strict exogeneity fails unless  $\rho_1 = 0$ .

Lagging variables that are thought to violate strict exogeneity can mitigate but does not usually solve the problem. Suppose we use  $w_{i,t-1}$  in place of  $w_{it}$  in equation (11.6) because we think  $w_{it}$  might be correlated with  $u_{it}$ . For example, let  $y_{it}$  be the percentage of flights canceled by airline i during year t, and let  $w_{i,t-1}$  be airline profits during the previous year. In this case  $\mathbf{x}_{i,t+1} = (\mathbf{z}_{i,t+1}, w_{it})$ , and so  $\mathbf{x}_{i,t+1}$  is correlated with  $u_{it}$ ; this fact results in failure of strict exogeneity. In the airline example this issue may be important: poor airline performance this year (as measured by canceled flights) can affect profits in subsequent years. Nevertheless, the sequential exogeneity condition (11.2) is reasonable.

Keane and Runkle (1992) argue that panel data models for testing rational expectations using individual-level data generally do not satisfy the strict exogeneity requirement. But they do satisfy sequential exogeneity: in fact, in the conditioning set in assumption (11.2), we can include all variables observed at time t-1.

What happens if we apply the standard fixed effects estimator when the strict exogeneity assumption fails? Generally,

$$\operatorname{plim}(\hat{\boldsymbol{\beta}}_{FE}) = \boldsymbol{\beta} + \left[ T^{-1} \sum_{t=1}^{T} \operatorname{E}(\ddot{\mathbf{x}}_{it}' \ddot{\mathbf{x}}_{it}) \right]^{-1} \left[ T^{-1} \sum_{t=1}^{T} \operatorname{E}(\ddot{\mathbf{x}}_{it}' u_{it}) \right]$$

where  $\ddot{\mathbf{x}}_{it} = \mathbf{x}_{it} - \overline{\mathbf{x}}_i$ , as in Chapter 10 (*i* is a random draw from the cross section). Now, under sequential exogeneity,  $\mathrm{E}(\ddot{\mathbf{x}}_{it}'u_{it}) = \mathrm{E}[(\mathbf{x}_{it} - \overline{\mathbf{x}}_i)'u_{it}] = -\mathrm{E}(\overline{\mathbf{x}}_iu_{it})$  because  $\mathrm{E}(\mathbf{x}_{it}'u_{it}) = \mathbf{0}$ , and so  $T^{-1}\sum_{t=1}^{T}\mathrm{E}(\ddot{\mathbf{x}}_{it}'u_{it}) = -T^{-1}\sum_{t=1}^{T}\mathrm{E}(\overline{\mathbf{x}}_{i}u_{it}) = -\mathrm{E}(\overline{\mathbf{x}}_{i}\bar{u}_{i})$ . We can bound the size of the inconsistency as a function of *T* if we assume that the time series process is appropriately stable and weakly dependent. Under such assumptions,  $T^{-1}\sum_{t=1}^{T}\mathrm{E}(\ddot{\mathbf{x}}_{it}'\ddot{\mathbf{x}}_{it})$  is bounded. Further,  $\mathrm{Var}(\overline{\mathbf{x}}_{i})$  and  $\mathrm{Var}(\bar{u}_{i})$  are of order  $T^{-1}$ . By the

{313}------------------------------------------------

Cauchy-Schwartz inequality (for example, Davidson, 1994, Chapter 9),  $|E(\bar{x}_{ij}\bar{u}_i)| \le [Var(\bar{x}_{ij})Var(\bar{u}_i)]^{1/2} = O(T^{-1})$ . Therefore, under bounded moments and weak dependence assumptions, the inconsistency from using fixed effects when the strict exogeneity assumption fails is of order  $T^{-1}$ . With large T the bias may be minimal. See Hamilton (1994) and Wooldridge (1994) for general discussions of weak dependence for time series processes.

Hsiao (1986, Section 4.2) works out the inconsistency in the FE estimator for the AR(1) model. The key stability condition sufficient for the bias to be of order  $T^{-1}$  is  $|\rho_1| < 1$ . However, for  $\rho_1$  close to unity, the bias in the FE estimator can be sizable, even with fairly large T. Generally, if the process  $\{\mathbf{x}_{it}\}$  has very persistent elements—which is often the case in panel data sets—the FE estimator can have substantial bias.

If our choice were between fixed effects and first differencing, we would tend to prefer fixed effects because, when T > 2, FE can have less bias as  $N \to \infty$ . To see this point, write

$$p\lim(\hat{\boldsymbol{\beta}}_{FD}) = \boldsymbol{\beta} + \left[ T^{-1} \sum_{t=1}^{T} E(\Delta \mathbf{x}'_{tt} \Delta \mathbf{x}_{it}) \right]^{-1} \left[ T^{-1} \sum_{t=1}^{T} E(\Delta \mathbf{x}'_{tt} \Delta u_{it}) \right]$$
(11.9)

If  $\{\mathbf{x}_{it}\}$  is weakly dependent, so is  $\{\Delta \mathbf{x}_{it}\}$ , and so the first average in equation (11.9) is bounded as a function of T. (In fact, under stationarity, this average does not depend on T.) Under assumption (11.2), we have

$$E(\Delta \mathbf{x}'_{it}\Delta u_{it}) = E(\mathbf{x}'_{it}u_{it}) + E(\mathbf{x}'_{i,t-1}u_{i,t-1}) - E(\mathbf{x}'_{i,t-1}u_{it}) - E(\mathbf{x}'_{it}u_{i,t-1}) = -E(\mathbf{x}'_{it}u_{i,t-1})$$

which is generally different from zero. Under stationarity,  $E(\mathbf{x}'_{it}u_{i,t-1})$  does not depend on t, and so the second average in equation (11.9) is constant. This result shows not only that the FD estimator is inconsistent, but also that its inconsistency does not depend on T. As we showed previously, the time demeaning underlying FE results in its bias being on the order of  $T^{-1}$ . But we should caution that this analysis assumes that the original series,  $\{(\mathbf{x}_{it}, y_{it}): t = 1, ..., T\}$ , is weakly dependent. Without this assumption, the inconsistency in the FE estimator cannot be shown to be of order  $T^{-1}$ .

If we make certain assumptions, we do not have to settle for estimators that are inconsistent with fixed T. A general approach to estimating equation (11.1) under assumption (11.2) is to use a transformation to remove  $c_i$ , but then search for instrumental variables. The FE transformation can be used provided that strictly exogenous instruments are available (see Problem 11.9). For models under sequential exogeneity assumptions, first differencing is more attractive.

{314}------------------------------------------------

First differencing equation (11.1) gives

$$\Delta y_{it} = \Delta \mathbf{x}_{it} \boldsymbol{\beta} + \Delta u_{it}, \qquad t = 2, 3, \dots, T$$
(11.10)

Now, under assumption (11.2),

$$E(\mathbf{x}'_{is}u_{it}) = 0, \qquad s = 1, 2, \dots, t$$
 (11.11)

Assumption (11.11) implies the orthogonality conditions

$$E(\mathbf{x}'_{is}\Delta u_{it}) = 0, \qquad s = 1, 2, \dots, t - 1$$
 (11.12)

so at time t we can use x<sup>o</sup> <sup>i</sup>;t<sup>1</sup> as potential instruments for Dxit, where

$$\mathbf{x}_{it}^o \equiv (\mathbf{x}_{i1}, \mathbf{x}_{i2}, \dots, \mathbf{x}_{it}) \tag{11.13}$$

The fact that x<sup>o</sup> <sup>i</sup>;t<sup>1</sup> is uncorrelated with Duit opens up a variety of estimation procedures. For example, a simple estimator uses Dxi;t<sup>1</sup> as the instruments for Dxit: EðDx<sup>0</sup> <sup>i</sup>;t1DuitÞ ¼ 0 under assumption (11.12), and the rank condition rank EðDx<sup>0</sup> <sup>i</sup>;t1DxitÞ ¼ K is usually reasonable. Then, the equation

$$\Delta y_{it} = \Delta \mathbf{x}_{it} \boldsymbol{\beta} + \Delta u_{it}, \qquad t = 3, \dots, T$$
 (11.14)

can be estimated by pooled 2SLS using instruments Dxi;t1. This choice of instruments loses an additional time period. If T ¼ 3, estimation of equation (11.14) becomes 2SLS on a cross section: ðxi<sup>2</sup> xi1Þ is used as instruments for ðxi<sup>3</sup> xi2Þ. When T > 3, equation (11.14) is a pooled 2SLS procedure. There is a set of assumptions—the sequential exogeneity analogues of Assumptions FD.1–FD.3 under which the usual 2SLS statistics obtained from the pooled 2SLS estimation are valid; see Problem 11.8 for details. With Dxi;t<sup>1</sup> as the instruments, equation (11.14) is just identified.

Rather than use changes in lagged xit as instruments, we can use lagged levels of xit. For example, choosing ðxi;t<sup>1</sup>; xi;t2Þ as instruments at time t is no less efficient than the procedure that uses Dx<sup>i</sup>;t1, as the latter is a linear combination of the former. It also gives K overidentifying restrictions that can be used to test assumption (11.2). (There will be fewer than K if xit contains time dummies.)

When T ¼ 2, *b* may be poorly identified. The equation is Dyi<sup>2</sup> ¼ Dx<sup>i</sup>2*b* þ Dui2, and, under assumption (11.2), x<sup>i</sup><sup>1</sup> is uncorrelated with Dui2. This is a cross section equation that can be estimated by 2SLS using x<sup>i</sup><sup>1</sup> as instruments for Dxi2. The estimator in this case may have a large asymptotic variance because the correlations between xi1, the levels of the explanatory variables, and the differences Dx<sup>i</sup><sup>2</sup> ¼ x<sup>i</sup><sup>2</sup> x<sup>i</sup><sup>1</sup> are often small. Of course, whether the correlation is sufficient to yield small enough standard errors depends on the application.

{315}------------------------------------------------

Even with large T, the available IVs may be poor in the sense that they are not highly correlated with  $\Delta \mathbf{x}_{it}$ . As an example, consider the AR(1) model (11.4) without  $\mathbf{z}_{it}$ :  $y_{it} = \rho_1 y_{i,t-1} + c_i + u_{it}$ ,  $\mathbf{E}(u_{it} \mid y_{i,t-1}, \ldots, y_{i0}, c_i) = 0$ ,  $t = 1, 2, \ldots, T$ . Differencing to eliminate  $c_i$  gives  $\Delta y_{it} = \rho_1 \Delta y_{i,t-1} + \Delta u_{it}$ ,  $t \geq 2$ . At time t, all elements of  $(y_{i,t-2},\ldots,y_{i0})$  are IV candidates because  $\Delta u_{it}$  is uncorrelated with  $y_{i,t-h}$ ,  $h \geq 2$ . Anderson and Hsiao (1982) suggested pooled IV with instruments  $y_{i,t-2}$  or  $\Delta y_{i,t-2}$ , whereas Arellano and Bond (1991) proposed using the entire set of instruments in a GMM procedure. Now, suppose that  $\rho_1 = 1$  and, in fact, there is no unobserved effect. Then  $\Delta y_{i,t-1}$  is uncorrelated with any variable dated at time t-2 or earlier, and so the elements of  $(y_{i,t-2},\ldots,y_{i0})$  cannot be used as IVs for  $\Delta y_{i,t-1}$ . What this conclusion shows is that we cannot use IV methods to test  $H_0$ :  $\rho_1 = 1$  in the absence of an unobserved effect.

Even if  $\rho_1 < 1$ , IVs from  $(y_{i,t-2}, \dots, y_{i0})$  tend to be weak if  $\rho_1$  is close to one. Recently, Arellano and Bover (1995) and Ahn and Schmidt (1995) suggested additional orthogonality conditions that improve the efficiency of the GMM estimator, but these are nonlinear in the parameters. (In Chapter 14 we will see how to use these kinds of moment restrictions.) Blundell and Bond (1998) obtained additional linear moment restrictions in the levels equation  $y_{it} = \rho_1 y_{i,t-1} + v_{it}$ ,  $v_{it} = c_i + u_{it}$ . The additional restrictions are based on  $y_{i0}$  being drawn from a steady-state distribution, and they are especially helpful in improving the efficiency of GMM for  $\rho_1$  close to one. (Actually, the Blundell-Bond orthogonality conditions are valid under weaker assumptions.) See also Hahn (1999). Of course, when  $\rho_1 = 1$ , it makes no sense to assume that there is a steady-state distribution. In Chapter 13 we cover conditional maximum likelihood methods that can be applied to the AR(1) model.

A general feature of pooled 2SLS procedures where the dimension of the IVs is constant across t is that they do not use all the instruments available in each time period; therefore, they cannot be expected to be efficient. The optimal procedure is to use expression (11.13) as the instruments at time t in a GMM procedure. Write the system of equations as

$$\Delta \mathbf{y}_i = \Delta \mathbf{X}_i \boldsymbol{\beta} + \Delta \mathbf{u}_i \tag{11.15}$$

using the same definitions as in Section 10.6. Define the matrix of instruments as

$$\mathbf{Z}_{i} = \begin{pmatrix} \mathbf{x}_{i1}^{o} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\ \mathbf{0} & \mathbf{x}_{i2}^{o} & \mathbf{0} & \cdots & \mathbf{0} \\ \vdots & & & \vdots \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{x}_{i:T-1}^{o} \end{pmatrix}$$
(11.16)

where  $\mathbf{x}_{it}^{o}$  is defined in expression (11.13). Note that  $\mathbf{Z}_{i}$  has T-1 rows to correspond

{316}------------------------------------------------

with the T-1 time periods in the system (11.15). Since each row contains different instruments, different instruments are used for different time periods.

Efficient estimation of  $\beta$  now proceeds in the GMM framework from Chapter 8 with instruments (11.16). Without further assumptions, the unrestricted weighting matrix should be used. In most applications there is a reasonable set of assumptions under which

$$E(\mathbf{Z}_i'\mathbf{e}_i\mathbf{e}_i'\mathbf{Z}_i) = E(\mathbf{Z}_i'\Omega\mathbf{Z}_i) \tag{11.17}$$

where  $\mathbf{e}_i \equiv \Delta \mathbf{u}_i$  and  $\Omega \equiv \mathrm{E}(\mathbf{e}_i \mathbf{e}_i')$ . Recall from Chapter 8 that assumption (11.17) is the assumption under which the GMM 3SLS estimator is the asymptotically efficient GMM estimator (see Assumption SIV.5). The full GMM analysis is not much more difficult. The traditional form of 3SLS estimator that first transforms the instruments should not be used because it is not consistent under assumption (11.2).

As a practical matter, the column dimension of  $\mathbf{Z}_i$  can be very large, making GMM estimation difficult. In addition, GMM estimators—including 2SLS and 3SLS—using many overidentifying restrictions are known to have poor finite sample properties (see, for example, Tauchen, 1986; Altonji and Segal, 1996; and Ziliak, 1997). In practice, it may be better to use a couple of lags rather than lags back to t = 1.

Example 11.3 (Testing for Persistence in County Crime Rates): We use the data in CORNWELL.RAW to test for state dependence in county crime rates, after allowing for unobserved county effects. Thus, the model is equation (11.4) with  $y_{it} \equiv \log(crmrte_{it})$  but without any other explanatory variables. As instruments for  $\Delta y_{i,t-1}$ , we use  $(y_{i,t-2}, y_{i,t-3})$ . Further, so that we do not have to worry about correcting the standard error for possible serial correlation in  $\Delta u_{it}$ , we use just the 1986–1987 differenced equation. The F statistic for joint significance of  $y_{i,t-2}, y_{i,t-3}$  in the reduced form for  $\Delta y_{i,t-1}$  yields p-value = .023, although the R-squared is only .083. The 2SLS estimates of the first-differenced equation are

$$\Delta \log(c\hat{r}mrte) = .065 + .212 \Delta \log(crmrte)_{-1}, \qquad N = 90$$
(.040) (.497)

so that we cannot reject  $H_0$ :  $\rho_1 = 0$  (t = .427).