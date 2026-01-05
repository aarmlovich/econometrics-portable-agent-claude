# Testing for the Presence of an Unobserved Effect

> Pages: 276-281

If the standard random effects assumptions RE.1–RE.3 hold but the model does not actually contain an unobserved effect, pooled OLS is efficient and all associated pooled OLS statistics are asymptotically valid. The absence of an unobserved effect is statistically equivalent to  $H_0$ :  $\sigma_c^2 = 0$ .

To test  $H_0$ :  $\sigma_c^2 = 0$ , we can use the simple test for AR(1) serial correlation covered in Chapter 7 [see equation (7.77)]. The AR(1) test is valid because the errors  $v_{it}$  are serially uncorrelated under the null  $H_0$ :  $\sigma_c^2 = 0$  (and we are assuming that  $\{\mathbf{x}_{it}\}$  is strictly exogenous). However, a better test is based directly on the estimator of  $\sigma_c^2$  in equation (10.37).

Breusch and Pagan (1980) derive a statistic using the Lagrange multiplier principle in a likelihood setting (something we cover in Chapter 13). We will not derive the Breusch and Pagan statistic because we are not assuming any particular distribution for the  $v_{it}$ . Instead, we derive a similar test that has the advantage of being valid for any distribution of  $\mathbf{v}_i$  and only states that the  $v_{it}$  are uncorrelated under the null. (In particular, the statistic is valid for heteroskedasticity in the  $v_{it}$ .)

From equation (10.37), we base a test of H<sub>0</sub>:  $\sigma_c^2 = 0$  on the null asymptotic distribution of

$$N^{-1/2} \sum_{i=1}^{N} \sum_{t=1}^{T-1} \sum_{s=t+1}^{T} \hat{v}_{it} \hat{v}_{is}$$
 (10.39)

which is essentially the estimator  $\hat{\sigma}_c^2$  scaled up by  $\sqrt{N}$ . Because of strict exogeneity, this statistic has the same limiting distribution (as  $N \to \infty$  with fixed T) when we replace the pooled OLS residuals  $\hat{v}_{it}$  with the errors  $v_{it}$  (see Problem 7.4). For any distribution of the  $v_{it}$ ,  $N^{-1/2} \sum_{i=1}^{N} \sum_{t=1}^{T-1} \sum_{s=t+1}^{T} v_{it}v_{is}$  has a limiting normal distribution (under the null that the  $v_{it}$  are serially uncorrelated) with variance

{277}------------------------------------------------

 $E(\sum_{t=1}^{T-1} \sum_{s=t+1}^{T} v_{it}v_{is})^2$ . We can estimate this variance in the usual way (take away the expectation, average across i, and replace  $v_{it}$  with  $\hat{v}_{it}$ ). When we put expression (10.39) over its asymptotic standard error we get the statistic

$$\frac{\sum_{i=1}^{N} \sum_{t=1}^{T-1} \sum_{s=t+1}^{T} \hat{v}_{it} \hat{v}_{is}}{\left[\sum_{i=1}^{N} \left(\sum_{t=1}^{T-1} \sum_{s=t+1}^{T} \hat{v}_{it} \hat{v}_{is}\right)^{2}\right]^{1/2}}$$
(10.40)

Under the null hypothesis that the  $v_{it}$  are serially uncorrelated, this statistic is distributed asymptotically as standard normal. Unlike the Breusch-Pagan statistic, with expression (10.40) we can reject H<sub>0</sub> for *negative* estimates of  $\sigma_c^2$ , although negative estimates are rare in practice (unless we have already differenced the data, something we discuss in Section 10.6).

The statistic in expression (10.40) can detect many kinds of serial correlation in the composite error  $v_{it}$ , and so a rejection of the null should not be interpreted as implying that the random effects error structure *must* be true. Finding that the  $v_{it}$  are serially uncorrelated is not very surprising in applications, especially since  $\mathbf{x}_{it}$  cannot contain lagged dependent variables for the methods in this chapter.

It is probably more interesting to test for serial correlation in the  $\{u_{it}\}$ , as this is a test of the random effects form of  $\Omega$ . Baltagi and Li (1995) obtain a test under normality of  $c_i$  and  $\{u_{it}\}$ , based on the Lagrange multiplier principle. In Section 10.7.2, we discuss a simpler test for serial correlation in  $\{u_{it}\}$  using a pooled OLS regression on transformed data, which does not rely on normality.

#### 10.5 Fixed Effects Methods

# 10.5.1 Consistency of the Fixed Effects Estimator

Again consider the linear unobserved effects model for T time periods:

$$y_{ii} = \mathbf{x}_{it}\boldsymbol{\beta} + c_i + u_{it}, \qquad t = 1, \dots, T \tag{10.41}$$

The random effects approach to estimating  $\beta$  effectively puts  $c_i$  into the error term, under the assumption that  $c_i$  is orthogonal to  $\mathbf{x}_{it}$ , and then accounts for the implied serial correlation in the composite error  $v_{it} = c_i + u_{it}$  using a GLS analysis. In many applications the whole point of using panel data is to allow for  $c_i$  to be arbitrarily correlated with the  $\mathbf{x}_{it}$ . A fixed effects analysis achieves this purpose explicitly.

The T equations in the model (10.41) can be written as

$$\mathbf{y}_i = \mathbf{X}_i \boldsymbol{\beta} + c_i \mathbf{j}_T + \mathbf{u}_i \tag{10.42}$$

{278}------------------------------------------------

where j<sup>T</sup> is still the T 1 vector of ones. As usual, equation (10.42) represents a single random draw from the cross section.

The first fixed effects (FE) assumption is strict exogeneity of the explanatory variables conditional on ci:

ASSUMPTION FE.1: 
$$E(u_{it} | \mathbf{x}_i, c_i) = 0, t = 1, 2, ..., T.$$

This assumption is identical to the first part of Assumption RE.1. Thus, we maintain strict exogeneity of fxit: t ¼ 1; ... ; Tg conditional on the unobserved effect. The key difference is that we do not assume RE.1b. In other words, for fixed effects analysis, Eðci j xiÞ is allowed to be any function of xi.

By relaxing RE.1b we can consistently estimate partial effects in the presence of time-constant omitted variables that can be arbitrarily related to the observables xit. Therefore, fixed effects analysis is more robust than random effects analysis. As we suggested in Section 10.1, this robustness comes at a price: without further assumptions, we cannot include time-constant factors in xit. The reason is simple: if ci can be arbitrarily correlated with each element of xit, there is no way to distinguish the effects of time-constant observables from the time-constant unobservable ci. When analyzing individuals, factors such as gender or race cannot be included in xit. For analyzing firms, industry cannot be included in xit unless industry designation changes over time for at least some firms. For cities, variables describing fixed city attributes, such as whether or not the city is near a river, cannot be included in xit.

The fact that xit cannot include time-constant explanatory variables is a drawback in certain applications, but when the interest is only on time-varying explanatory variables, it is convenient not to have to worry about modeling time-constant factors that are not of direct interest.

In panel data analysis the term ''time-varying explanatory variables'' means that each element of xit varies over time for some cross section units. Often there are elements of xit that are constant across time for a subset of the cross section. For example, if we have a panel of adults and one element of xit is education, we can allow education to be constant for some part of the sample. But we must have education changing for some people in the sample.

As a general specification, let d2t; ... ; dTt denote time period dummies so that dst ¼ 1 if s ¼ t, and zero otherwise (often these are defined in terms of specific years, such as d88t, but at this level we call them time period dummies). Let z<sup>i</sup> be a vector of time-constant observables, and let wit be a vector of time-varying variables. Suppose yit is determined by

{279}------------------------------------------------

$$y_{it} = \theta_1 + \theta_2 d2_t + \dots + \theta_T dT_t + \mathbf{z}_i \gamma_1 + d2_t \mathbf{z}_i \gamma_2$$

$$+ \dots + dT_t \mathbf{z}_i \gamma_T + \mathbf{w}_{it} \boldsymbol{\delta} + c_i + u_{it}$$

$$(10.43)$$

$$E(u_{it} | \mathbf{z}_i, \mathbf{w}_{i1}, \mathbf{w}_{i2}, \dots, \mathbf{w}_{iT}, c_i) = 0, \qquad t = 1, 2, \dots, T$$
(10.44)

We hope that this model represents a causal relationship, where the conditioning on  $c_i$  allows us to control for unobserved factors that are time constant. Without further assumptions, the intercept  $\theta_1$  cannot be identified and the vector  $\gamma_1$  on  $\mathbf{z}_i$  cannot be identified, because  $\theta_1 + \mathbf{z}_i \gamma_1$  cannot be distinguished from  $c_i$ . Note that  $\theta_1$  is the intercept for the base time period, t = 1, and  $\gamma_1$  measures the effects of  $\mathbf{z}_i$  on  $y_{it}$  in period t = 1. Even though we cannot identify the effects of the  $\mathbf{z}_i$  in any particular time period,  $\gamma_2, \gamma_3, \ldots, \gamma_T$  are identified, and therefore we can estimate the differences in the partial effects on time-constant variables relative to a base period. In particular, we can test whether the effects of time-constant variables have changed over time. As a specific example, if  $y_{it} = \log(wage_{it})$  and one element of  $\mathbf{z}_i$  is a female binary variable, then we can estimate how the gender gap has changed over time, even though we cannot estimate the gap in any particular time period.

The idea for estimating  $\beta$  under Assumption FE.1 is to transform the equations to eliminate the unobserved effect  $c_i$ . When at least two time periods are available, there are several transformations that accomplish this purpose. In this section we study the **fixed effects transformation**, also called the **within transformation**. The FE transformation is obtained by first averaging equation (10.41) over t = 1, ..., T to get the cross section equation

$$\bar{y}_i = \bar{\mathbf{x}}_i \boldsymbol{\beta} + c_i + \bar{u}_i \tag{10.45}$$

where  $\bar{y}_i = T^{-1} \sum_{t=1}^T y_{it}$ ,  $\bar{\mathbf{x}}_i = T^{-1} \sum_{t=1}^T \mathbf{x}_{it}$ , and  $\bar{u}_i = T^{-1} \sum_{t=1}^T u_{it}$ . Subtracting equation (10.45) from equation (10.41) for each t gives the FE transformed equation,

$$y_{it} - \bar{y}_i = (\mathbf{x}_{it} - \bar{\mathbf{x}}_i)\boldsymbol{\beta} + u_{it} - \bar{u}_i$$

or

$$\ddot{\mathbf{y}}_{it} = \ddot{\mathbf{x}}_{it}\boldsymbol{\beta} + \ddot{\boldsymbol{u}}_{it}, \qquad t = 1, 2, \dots, T \tag{10.46}$$

where  $\ddot{y}_{it} \equiv y_{it} - \bar{y}_i$ ,  $\ddot{\mathbf{x}}_{it} \equiv \mathbf{x}_{it} - \bar{\mathbf{x}}_i$ , and  $\ddot{\mathbf{u}}_{it} \equiv u_{it} - \bar{u}_i$ . The time demeaning of the original equation has removed the individual specific effect  $c_i$ .

With  $c_i$  out of the picture, it is natural to think of estimating equation (10.46) by pooled OLS. Before investigating this possibility, we must remember that equation (10.46) is an *estimating* equation: the interpretation of  $\beta$  comes from the (structural) conditional expectation  $E(y_{it} | \mathbf{x}_i, c_i) = E(y_{it} | \mathbf{x}_{it}, c_i) = \mathbf{x}_{it} \boldsymbol{\beta} + c_i$ .

{280}------------------------------------------------

To see whether pooled OLS estimation of equation (10.46) will be consistent, we need to show that the key pooled OLS assumption (Assumption POLS.1 from Chapter 7) holds in equation (10.46). That is,

$$\mathbf{E}(\ddot{\mathbf{x}}_{it}'\ddot{\mathbf{u}}_{it}) = \mathbf{0}, \qquad t = 1, 2, \dots, T \tag{10.47}$$

For each t, the left-hand side of equation (10.47) can be written as  $E[(\mathbf{x}_{it} - \bar{\mathbf{x}}_i)'(u_{it} - \bar{u}_i)]$ . Now, under Assumption FE.1,  $u_{it}$  is uncorrelated with  $\mathbf{x}_{is}$ , for all  $s, t = 1, 2, \ldots, T$ . It follows that  $u_{it}$  and  $\bar{u}_i$  are uncorrelated with  $\mathbf{x}_{it}$  and  $\bar{\mathbf{x}}_i$  for  $t = 1, 2, \ldots, T$ . Therefore, assumption (10.47) holds under Assumption FE.1, and so pooled OLS applied to equation (10.46) can be expected to produce consistent estimators. We can actually say a lot more than condition (10.47): under Assumption FE.1,  $E(\ddot{u}_{it} | \mathbf{x}_i) = E(u_{it} | \mathbf{x}_i) - E(\bar{u}_i | \mathbf{x}_i) = 0$ , which in turn implies that  $E(\ddot{u}_{it} | \ddot{\mathbf{x}}_{i1}, \ldots, \ddot{\mathbf{x}}_{iT}) = 0$ , since each  $\ddot{\mathbf{x}}_{it}$  is just a function of  $\mathbf{x}_i = (\mathbf{x}_{i1}, \ldots, \mathbf{x}_{iT})$ . This result shows that the  $\ddot{\mathbf{x}}_{it}$  satisfy the conditional expectation form of the strict exogeneity assumption in the model (10.46). Among other things, this conclusion implies that the fixed effects estimator of  $\boldsymbol{\beta}$  that we will derive is actually unbiased under Assumption FE.1.

It is important to see that assumption (10.47) fails if we try to relax the strict exogeneity assumption to something weaker, such as  $E(\mathbf{x}'_{it}u_{it}) = \mathbf{0}$ , all t, because this assumption does not ensure that  $\mathbf{x}_{is}$  is uncorrelated with  $u_{it}$ ,  $s \neq t$ .

The fixed effects (FE) estimator, denoted by  $\hat{\beta}_{FE}$ , is the pooled OLS estimator from the regression

$$\ddot{y}_{it}$$
 on  $\ddot{\mathbf{x}}_{it}$ ,  $t = 1, 2, \dots, T; i = 1, 2, \dots, N$  (10.48)

The FE estimator is simple to compute once the time demeaning has been carried out. Some econometrics packages have special commands to carry out fixed effects estimation (and commands to carry out the time demeaning for all i). It is also fairly easy to program this estimator in matrix-oriented languages.

To study the FE estimator a little more closely, write equation (10.46) for all time periods as

$$\ddot{\mathbf{y}}_i = \ddot{\mathbf{X}}_i \boldsymbol{\beta} + \ddot{\mathbf{u}}_i \tag{10.49}$$

where  $\ddot{\mathbf{y}}_i$  is  $T \times 1$ ,  $\ddot{\mathbf{X}}_i$  is  $T \times K$ , and  $\ddot{\mathbf{u}}_i$  is  $T \times 1$ . This set of equations can be obtained by premultiplying equation (10.42) by a **time-demeaning matrix**. Define  $\mathbf{Q}_T \equiv \mathbf{I}_T - \mathbf{j}_T (\mathbf{j}_T' \mathbf{j}_T)^{-1} \mathbf{j}_T'$ , which is easily seen to be a  $T \times T$  symmetric, idempotent matrix with rank T - 1. Further,  $\mathbf{Q}_T \mathbf{j}_T = \mathbf{0}$ ,  $\mathbf{Q}_T \mathbf{y}_i = \ddot{\mathbf{y}}_i$ ,  $\mathbf{Q}_T \mathbf{X}_i = \ddot{\mathbf{X}}_i$ , and  $\mathbf{Q}_T \mathbf{u}_i = \ddot{\mathbf{u}}_i$ , and so premultiplying equation (10.42) by  $\mathbf{Q}_T$  gives the demeaned equations (10.49).


{281}------------------------------------------------

In order to ensure that the FE estimator is well behaved asymptotically, we need a standard rank condition on the matrix of time-demeaned explanatory variables:

Assumption FE.2: 
$$\operatorname{rank}\left(\sum_{t=1}^{T} \mathrm{E}(\ddot{\mathbf{x}}_{it}'\ddot{\mathbf{x}}_{it})\right) = \operatorname{rank}[\mathrm{E}(\ddot{\mathbf{X}}_{i}'\ddot{\mathbf{X}}_{i})] = K.$$

If  $\mathbf{x}_{it}$  contains an element that does not vary over time for any i, then the corresponding element in  $\ddot{\mathbf{x}}_{it}$  is identically zero for all t and any draw from the cross section. Since  $\ddot{\mathbf{X}}_i$  would contain a column of zeros for all i, Assumption FE.2 could not be true. Assumption FE.2 shows explicitly why time-constant variables are not allowed in fixed effects analysis (unless they are interacted with time-varying variables, such as time dummies).

The fixed effects estimator can be expressed as

$$\hat{\boldsymbol{\beta}}_{FE} = \left(\sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \ddot{\mathbf{X}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \ddot{\mathbf{y}}_{i}\right) = \left(\sum_{i=1}^{N} \sum_{t=1}^{T} \ddot{\mathbf{x}}_{it}' \ddot{\mathbf{x}}_{it}\right)^{-1} \left(\sum_{i=1}^{N} \sum_{t=1}^{T} \ddot{\mathbf{x}}_{it}' \ddot{\mathbf{y}}_{it}\right)$$
(10.50)

It is also called the **within estimator** because it uses the time variation within each cross section. The **between estimator**, which uses only variation between the cross section observations, is the OLS estimator applied to the time-averaged equation (10.45). This estimator is not consistent under Assumption FE.1 because  $E(\bar{\mathbf{x}}_i'c_i)$  is not necessarily zero. The between estimator is consistent under Assumption RE.1 and a standard rank condition, but it effectively discards the time series information in the data set. It is more efficient to use the random effects estimator.

Under Assumption FE.1 and the finite sample version of Assumption FE.2, namely, rank( $\ddot{\mathbf{X}}'\ddot{\mathbf{X}}$ ) = K,  $\hat{\boldsymbol{\beta}}_{FE}$  can be shown to be *unbiased* conditional on  $\mathbf{X}$ .