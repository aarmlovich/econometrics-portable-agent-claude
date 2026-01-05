# Setup for Panel Data

> Pages: 412-420

For panel data applications we let y denote a T 1 vector, with generic element yt. Thus, y<sup>i</sup> is a T 1 random draw vector from the cross section, with tth element yit. As always, we are thinking of T small relative to the cross section sample size. With a

{413}------------------------------------------------

slight notational change we can replace yit with, say, a G-vector for each t, an extension that allows us to cover general systems of equations with panel data.

For some vector x<sup>t</sup> containing any set of observable variables, let Dðyt j xtÞ denote the distribution of yt given xt. The key assumption is that we have a correctly specified model for the density of yt given xt; call it ftðyt j xt; *y*Þ, t ¼ 1; 2; ... ; T. The vector x<sup>t</sup> can contain anything, including conditioning variables zt, lags of these, and lagged values of y. The vector *y* consists of all parameters appearing in ft for any t; some or all of these may appear in the density for every t, and some may appear only in the density for a single time period.

What distinguishes partial likelihood from maximum likelihood is that we do not assume that

$$\prod_{t=1}^{T} \mathbf{D}(y_{it} \mid \mathbf{x}_{it}) \tag{13.43}$$

is a conditional distribution of the vector y<sup>i</sup> given some set of conditioning variables. In other words, even though ftðyt j xt; *y*oÞ is the correct density for yit given xit for each t, the product of these is not (necessarily) the density of y<sup>i</sup> given some conditioning variables. Usually, we specify ftðyt j xt; *y*Þ because it is the density of interest for each t.

We define the partial log likelihood for each observation i as

$$\ell_i(\boldsymbol{\theta}) \equiv \sum_{t=1}^{T} \log f_t(y_{it} | \mathbf{x}_{it}; \boldsymbol{\theta})$$
 (13.44)

which is the sum of the log likelihoods across t. What makes partial likelihood methods work is that *y*<sup>o</sup> maximizes the expected value of equation (13.44) provided we have the densities ftðyt j xt; *y*Þ correctly specified.

By the Kullback-Leibler information inequality, *y*<sup>o</sup> maximizes E½log ftðyit j xit; *y*Þ over Y for each t, so *y*<sup>o</sup> also maximizes the sum of these over t. As usual, identification requires that *y*<sup>o</sup> be the unique maximizer of the expected value of equation (13.44). It is sufficient that *y*<sup>o</sup> uniquely maximizes E½log ftðyit j xit; *y*Þ for each t, but this assumption is not necessary.

The partial maximum likelihood estimator (PMLE) ^*y* solves

$$\max_{\boldsymbol{\theta} \in \mathbf{\Theta}} \sum_{i=1}^{N} \sum_{t=1}^{T} \log f_t(y_{it} | \mathbf{x}_{it}; \boldsymbol{\theta})$$
 (13.45)

and this problem is clearly an M-estimator problem (where the asymptotics are with fixed T and N ! y). Therefore, from Theorem 12.2, the partial MLE is generally consistent provided *y*<sup>o</sup> is identified.

{414}------------------------------------------------

It is also clear that the partial MLE will be asymptotically normal by Theorem 12.3 in Section 12.3. However, unless

$$p_{o}(\mathbf{y} \mid \mathbf{z}) = \prod_{t=1}^{T} f_{t}(y_{t} \mid \mathbf{x}_{t}; \boldsymbol{\theta}_{o})$$
(13.46)

for some subvector  $\mathbf{z}$  of  $\mathbf{x}$ , we cannot apply the conditional information matrix equality. A more general asymptotic variance estimator of the type covered in Section 12.5.1 is needed, and we provide such estimators in the next two subsections.

It is useful to discuss at a general level why equation (13.46) does not necessarily hold in a panel data setting. First, suppose  $\mathbf{x}_t$  contains only contemporaneous conditioning variables,  $\mathbf{z}_t$ ; in particular,  $\mathbf{x}_t$  contains no lagged dependent variables. Then we can always write

$$p_{o}(\mathbf{y} \mid \mathbf{z}) = p_{1}^{o}(y_{1} \mid \mathbf{z}) \cdot p_{2}^{o}(y_{2} \mid y_{1}, \mathbf{z}) \cdots p_{t}^{o}(y_{t} \mid y_{t-1}, y_{t-2}, \dots, y_{1}, \mathbf{z}) \cdots$$
$$p_{T}^{o}(y_{T} \mid y_{T-1}, y_{T-2}, \dots, y_{1}, \mathbf{z})$$

where  $p_t^{o}(y_t|y_{t-1}, y_{t-2}, ..., y_1, \mathbf{z})$  is the true conditional density of  $y_t$  given  $y_{t-1}, y_{t-2}, ..., y_1$  and  $\mathbf{z} = (\mathbf{z}_1, ..., \mathbf{z}_T)$ . (For t = 1,  $p_1^{o}$  is the density of  $y_1$  given  $\mathbf{z}$ .) For equation (13.46) to hold, we should have

$$p_t^{o}(y_t | y_{t-1}, y_{t-2}, \dots, y_1, \mathbf{z}) = f_t(y_t | \mathbf{z}_t; \boldsymbol{\theta}_{o}), \quad t = 1, \dots, T$$

which requires that, once  $\mathbf{z}_t$  is conditioned on, neither past lags of  $y_t$  nor elements of  $\mathbf{z}$  from any other time period—past or future—appear in the conditional density  $p_t^{\text{o}}(y_t | y_{t-1}, y_{t-2}, \dots, y_1, \mathbf{z})$ . Generally, this requirement is very strong, as it requires a combination of strict exogeneity of  $\mathbf{z}_t$  and the absense of dynamics in  $p_t^{\text{o}}$ .

Equation (13.46) is more likely to hold when  $\mathbf{x}_t$  contains lagged dependent variables. In fact, if  $\mathbf{x}_t$  contains only lagged values of  $y_t$ , then

$$p_{o}(\mathbf{y}) = \prod_{t=1}^{T} f_{t}(y_{t} | \mathbf{x}_{t}; \boldsymbol{\theta}_{o})$$

holds if  $f_t(y_t | \mathbf{x}_t; \boldsymbol{\theta}_0) = p_t^o(y_t | y_{t-1}, y_{t-2}, \dots, y_1)$  for all t (where  $p_1^o$  is the unconditional density of  $y_1$ ), so that all dynamics are captured by  $f_t$ . When  $\mathbf{x}_t$  contains some variables  $\mathbf{z}_t$  in addition to lagged  $y_t$ , equation (13.46) requires that the parametric density captures all of the dynamics—that is, that all lags of  $y_t$  and  $\mathbf{z}_t$  have been properly accounted for in  $f(y_t | \mathbf{x}_t, \boldsymbol{\theta}_0)$ —and strict exogeneity of  $\mathbf{z}_t$ .

In most treatments of maximum likelihood estimation of dynamic models containing additional exogenous variables, the strict exogeneity assumption is main-

{415}------------------------------------------------

tained, often implicitly by taking  $\mathbf{z}_t$  to be nonrandom. In Chapter 7 we saw that strict exogeneity played no role in getting consistent, asymptotically normal estimators in linear panel data models by pooled OLS, and the same is true here. We also allow models where the dynamics have been incompletely specified.

Example 13.3 (Probit with Panel Data): To illustrate the previous discussion, we consider estimation of a panel data binary choice model. The idea is that, for each unit i in the population (individual, firm, and so on) we have a binary outcome,  $y_{ii}$ , for each of T time periods. For example, if t represents a year, then  $y_{it}$  might indicate whether a person was arrested for a crime during year t.

Consider the model in latent variable form:

$$y_{it}^* = \mathbf{x}_{it}\boldsymbol{\theta}_0 + e_{it}$$

$$y_{it} = \mathbf{1}[y_{it}^* > 0]$$

$$e_{it} | \mathbf{x}_{it} \sim \text{Normal}(0, 1)$$

$$(13.47)$$

The vector  $\mathbf{x}_{it}$  might contain exogenous variables  $\mathbf{z}_{it}$ , lags of these, and even lagged  $y_{it}$  (not lagged  $y_{it}^*$ ). Under the assumptions in model (13.47), we have, for each t,  $P(y_{it} = 1 | \mathbf{x}_{it}) = \Phi(\mathbf{x}_{it}\theta_0)$ , and the density of  $y_{it}$  given  $\mathbf{x}_{it} = \mathbf{x}_t$  is  $f(y_t | \mathbf{x}_t) = [\Phi(\mathbf{x}_t\theta_0)]^{y_t}[1 - \Phi(\mathbf{x}_t\theta_0)]^{1-y_t}$ .

The partial log likelihood for a cross section observation i is

$$\ell_i(\boldsymbol{\theta}) = \sum_{t=1}^{T} \left\{ y_{it} \log \Phi(\mathbf{x}_{it}\boldsymbol{\theta}) + (1 - y_{it}) \log[1 - \Phi(\mathbf{x}_{it}\boldsymbol{\theta})] \right\}$$
(13.48)

and the partial MLE in this case—which simply maximizes  $\ell_i(\theta)$  summed across all i—is the **pooled probit estimator**. With T fixed and  $N \to \infty$ , this estimator is consistent and  $\sqrt{N}$ -asymptotically normal without any assumptions other than identification and standard regularity conditions.

It is very important to know that the pooled probit estimator works without imposing additional assumptions on  $\mathbf{e}_i = (e_{i1}, \dots, e_{iT})'$ . When  $\mathbf{x}_{it}$  contains only exogenous variables  $\mathbf{z}_{it}$ , it would be standard to assume that

$$e_{it}$$
 is independent of  $\mathbf{z}_i \equiv (\mathbf{z}_{i1}, \mathbf{z}_{i2}, \dots, \mathbf{z}_{iT}), \qquad t = 1, \dots, T$  (13.49)

This is the natural strict exogeneity assumption (and is much stronger than simply assuming that  $e_{it}$  and  $\mathbf{z}_{it}$  are independent for each t). The crime example can illustrate how strict exogeneity might fail. For example, suppose that  $\mathbf{z}_{it}$  measures the amount of time the person has spent in prison prior to the current year. An arrest this year  $(y_{it} = 1)$  certainly has an effect on expected future values of  $\mathbf{z}_{it}$ , so that assumption

{416}------------------------------------------------

(13.49) is almost certainly false. Fortunately, we do not need assumption (13.49) to apply partial likelihood methods.

A second standard assumption is that the eit, t ¼ 1; 2; ... ; T are serially independent. This is especially restrictive in a static model. If we maintain this assumption in addition to assumption (13.49), then equation (13.46) holds (because the yit are then independent conditional on zi) and the partial MLE is a conditional MLE.

To relax the assumption that the yit are conditionally independent, we can allow the eit to be correlated across t (still assuming that no lagged dependent variables appear). A common assumption is that e<sup>i</sup> has a multivariate normal distribution with a general correlation matrix. Under this assumption, we can write down the joint distribution of y<sup>i</sup> given zi, but it is complicated, and estimation is very computationally intensive (for recent discussions, see Keane, 1993, and Hajivassilou and Ruud, 1994). We will cover a special case, the random effects probit model, in Chapter 15.

A nice feature of the partial MLE is that ^*y* will be consistent and asymptotically normal even if the eit are arbitrarily serially correlated. This result is entirely analogous to using pooled OLS in linear panel data models when the errors have arbitrary serial correlation.

When xit contains lagged dependent variables, model (13.47) provides a way of examining dynamic behavior. Or, perhaps yi;t<sup>1</sup> is included in xit as a proxy for unobserved factors, and our focus is on on policy variables in zit. For example, if yit is a binary indicator of employment, yi;t<sup>1</sup> might be included as a control when studying the effect of a job training program (which may be a binary element of zit) on the employment probability; this method controls for the fact that participation in job training this year might depend on employment last year, and it captures the fact that employment status is persistent. In any case, provided Pðyit ¼ 1 j xitÞ follows a probit, the pooled probit estimator is consistent and asymptotically normal. The dynamics may or may not be correctly specified (more on this topic later), and the zit need not be strictly exogenous (so that whether someone participates in job training in year t can depend on the past employment history).

# 13.8.2 Asymptotic Inference

The most important practical difference between conditional MLE and partial MLE is in the computation of asymptotic standard errors and test statistics. In many cases, including the pooled probit estimator, the pooled Poisson estimator (see Problem 13.6), and many other pooled procedures, standard econometrics packages can be used to compute the partial MLEs. However, except under certain assumptions, the usual standard errors and test statistics reported from a pooled analysis are not valid.

{417}------------------------------------------------

This situation is entirely analogous to the linear model case in Section 7.8 when the errors are serially correlated.

Estimation of the asymptotic variance of the partial MLE is not difficult. In fact, we can combine the M-estimation results from Section 12.5.1 and the results of Section 13.5 to obtain valid estimators.

From Theorem 12.3, we have Avar  $\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = \mathbf{A}_{o}^{-1}\mathbf{B}_{o}\mathbf{A}_{o}^{-1}$ , where

$$\mathbf{A}_{o} = -\mathrm{E}[\nabla_{\theta}^{2}\ell_{i}(\boldsymbol{\theta}_{o})] = -\sum_{t=1}^{T}\mathrm{E}[\nabla_{\theta}^{2}\ell_{it}(\boldsymbol{\theta}_{o})] = \sum_{t=1}^{T}\mathrm{E}[\mathbf{A}_{it}(\boldsymbol{\theta}_{o})]$$

$$\mathbf{B}_{o} = \mathrm{E}[\mathbf{s}_{i}(\boldsymbol{\theta}_{o})\mathbf{s}_{i}(\boldsymbol{\theta}_{o})'] = \mathrm{E}\left\{\left[\sum_{t=1}^{T}\mathbf{s}_{it}(\boldsymbol{\theta}_{o})\right]\left[\sum_{t=1}^{T}\mathbf{s}_{it}(\boldsymbol{\theta}_{o})\right]'\right\}$$

$$\mathbf{A}_{it}(\boldsymbol{\theta}_{0}) = -\mathbf{E}[\nabla_{\theta}^{2}\ell_{it}(\boldsymbol{\theta}_{0}) \mid \mathbf{x}_{it}]$$

$$\mathbf{s}_{it}(\boldsymbol{\theta}) = \nabla_{\boldsymbol{\theta}} \ell_{it}(\boldsymbol{\theta})'$$

There are several important features of these formulas. First, the matrix  $\mathbf{A}_o$  is just the sum across t of minus the expected Hessian. Second, the matrix  $\mathbf{B}_o$  generally depends on the correlation between the scores at different time periods:  $\mathbf{E}[\mathbf{s}_{it}(\boldsymbol{\theta}_o)\mathbf{s}_{ir}(\boldsymbol{\theta}_o)']$ ,  $t \neq r$ . Third, for each t, the conditional information matrix equality holds:

$$\mathbf{A}_{it}(\boldsymbol{\theta}_{o}) = \mathbf{E}[\mathbf{s}_{it}(\boldsymbol{\theta}_{o})\mathbf{s}_{it}(\boldsymbol{\theta}_{o})' \mid \mathbf{x}_{it}]$$

However, in general,  $-E[\mathbf{H}_i(\boldsymbol{\theta}_o) | \mathbf{x}_i] \neq E[\mathbf{s}_i(\boldsymbol{\theta}_o)\mathbf{s}_i(\boldsymbol{\theta}_o)' | \mathbf{x}_i]$  and, more importantly,  $\mathbf{B}_o \neq \mathbf{A}_o$ . Thus, to perform inference in the context of partial MLE, we generally need separate estimates of  $\mathbf{A}_o$  and  $\mathbf{B}_o$ . Given the structure of the partial MLE, these are easy to obtain. Three possibilities for  $\mathbf{A}_o$  are

$$N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} -\nabla_{\theta}^{2} \ell_{it}(\hat{\boldsymbol{\theta}}), \qquad N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} \mathbf{A}_{it}(\hat{\boldsymbol{\theta}}), \qquad \text{and}$$

$$N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} \mathbf{s}_{it}(\hat{\boldsymbol{\theta}}) \mathbf{s}_{it}(\hat{\boldsymbol{\theta}})'$$
(13.50)

The validity of the second of these follows from a standard iterated expectations argument, and the last of these follows from the conditional information matrix equality for each t. In most cases, the second estimator is preferred when it is easy to compute.

Since  $\mathbf{B}_{o}$  depends on  $\mathrm{E}[\mathbf{s}_{it}(\boldsymbol{\theta}_{o})\mathbf{s}_{it}(\boldsymbol{\theta}_{o})']$  as well as cross product terms, there are also at least three estimators available for  $\mathbf{B}_{o}$ . The simplest is

{418}------------------------------------------------

$$N^{-1} \sum_{i=1}^{N} \hat{\mathbf{s}}_{i} \hat{\mathbf{s}}_{i}' = N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} \hat{\mathbf{s}}_{it} \hat{\mathbf{s}}_{it}' + N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} \sum_{r \neq t} \hat{\mathbf{s}}_{ir} \hat{\mathbf{s}}_{it}'$$
(13.51)

where the second term on the right-hand side accounts for possible serial correlation in the score. The first term on the right-hand side of equation (13.51) can be replaced by one of the other two estimators in equation (13.50). The asymptotic variance of  $\hat{\boldsymbol{\theta}}$  is estimated, as usual, by  $\hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1}/N$  for the chosen estimators  $\hat{\mathbf{A}}$  and  $\hat{\mathbf{B}}$ . The asymptotic standard errors come directly from this matrix, and Wald tests for linear and nonlinear hypotheses can be obtained directly. The robust score statistic discussed in Section 12.6.2 can also be used. When  $\mathbf{B}_0 \neq \mathbf{A}_0$ , the likelihood ratio statistic computed after pooled estimation is *not* valid.

Because the CIME holds for each t,  $\mathbf{B}_0 = \mathbf{A}_0$  when the scores evaluated at  $\theta_0$  are serially uncorrelated, that is, when

$$\mathbf{E}[\mathbf{s}_{it}(\boldsymbol{\theta}_{0})\mathbf{s}_{ir}(\boldsymbol{\theta}_{0})'] = \mathbf{0}, \qquad t \neq r$$
(13.52)

When the score is serially uncorrelated, inference is very easy: the usual MLE statistics computed from the pooled estimation, including likelihood ratio statistics, are asymptotically valid. Effectively, we can ignore the fact that a time dimension is present. The estimator of  $\text{Avar}(\hat{\boldsymbol{\theta}})$  is just  $\hat{\mathbf{A}}^{-1}/N$ , where  $\hat{\mathbf{A}}$  is one of the matrices in equation (13.50).

Example 13.3 (continued): For the pooled probit example, a simple, general estimator of the asymptotic variance is

$$\left[\sum_{i=1}^{N}\sum_{t=1}^{T}\mathbf{A}_{it}(\hat{\boldsymbol{\theta}})\right]^{-1}\left[\sum_{i=1}^{N}\mathbf{s}_{i}(\hat{\boldsymbol{\theta}})\mathbf{s}_{i}(\hat{\boldsymbol{\theta}})'\right]\left[\sum_{i=1}^{N}\sum_{t=1}^{T}\mathbf{A}_{it}(\hat{\boldsymbol{\theta}})\right]^{-1}$$
(13.53)

where

$$\mathbf{A}_{it}(\hat{\boldsymbol{\theta}}) = \frac{\{\phi(\mathbf{x}_{it}\hat{\boldsymbol{\theta}})\}^2 \mathbf{x}_{it}' \mathbf{x}_{it}}{\Phi(\mathbf{x}_{it}\hat{\boldsymbol{\theta}})[1 - \Phi(\mathbf{x}_{it}\hat{\boldsymbol{\theta}})]}$$

and

$$\mathbf{s}_{i}(\boldsymbol{\theta}) = \sum_{t=1}^{T} \mathbf{s}_{it}(\boldsymbol{\theta}) = \sum_{t=1}^{T} \frac{\phi(\mathbf{x}_{it}\boldsymbol{\theta})\mathbf{x}'_{it}[y_{it} - \Phi(\mathbf{x}_{it}\boldsymbol{\theta})]}{\Phi(\mathbf{x}_{it}\boldsymbol{\theta})[1 - \Phi(\mathbf{x}_{it}\boldsymbol{\theta})]}$$

The estimator (13.53) contains cross product terms of the form  $\mathbf{s}_{it}(\hat{\boldsymbol{\theta}})\mathbf{s}_{ir}(\hat{\boldsymbol{\theta}})'$ ,  $t \neq r$ , and so it is fully robust. If the score is serially uncorrelated, then the usual probit standard errors and test statistics from the pooled estimation are valid. We will

{419}------------------------------------------------

discuss a sufficient condition for the scores to be serially uncorrelated in the next subsection.

#### 13.8.3 Inference with Dynamically Complete Models

There is a very important case where condition (13.52) holds, in which case all statistics obtained by treating  $\ell_i(\theta)$  as a standard log likelihood are valid. For any definition of  $\mathbf{x}_t$ , we say that  $\{f_t(y_t | \mathbf{x}_t; \theta_0): t = 1, ..., T\}$  is a **dynamically complete conditional density** if

$$f_t(y_t | \mathbf{x}_t; \boldsymbol{\theta}_0) = p_t^{o}(y_t | \mathbf{x}_t, y_{t-1}, \mathbf{x}_{t-1}, y_{t-2}, \dots, y_1, \mathbf{x}_1), \qquad t = 1, \dots, T$$
 (13.54)

In other words,  $f_t(y_t | \mathbf{x}_t; \boldsymbol{\theta}_0)$  must be the conditional density of  $y_t$  given  $\mathbf{x}_t$  and the entire past of  $(\mathbf{x}_t, y_t)$ .

When  $\mathbf{x}_t = \mathbf{z}_t$  for contemporaneous exogenous variables, equation (13.54) is very strong: it means that, once  $\mathbf{z}_t$  is controlled for, no past values of  $\mathbf{z}_t$  or  $y_t$  appear in the conditional density  $p_t^o(y_t | \mathbf{z}_t, y_{t-1}, \mathbf{z}_{t-1}, y_{t-2}, \dots, y_1, \mathbf{z}_1)$ . When  $\mathbf{x}_t$  contains  $\mathbf{z}_t$  and some lags—similar to a finite distributed lag model—then equation (13.54) is perhaps more reasonable, but it still assumes that lagged  $y_t$  has no effect on  $y_t$  once current and lagged  $\mathbf{z}_t$  are controlled for. That assumption (13.54) can be false is analogous to the omnipresence of serial correlation in static and finite distributed lag regression models. One important feature of dynamic completeness is that it does not require strict exogeneity of  $\mathbf{z}_t$  [since only current and lagged  $\mathbf{x}_t$  appear in equation (13.54)].

Dynamic completeness is more likely to hold when  $\mathbf{x}_t$  contains lagged dependent variables. The issue, then, is whether enough lags of  $y_t$  (and  $\mathbf{z}_t$ ) have been included in  $\mathbf{x}_t$  to fully capture the dynamics. For example, if  $\mathbf{x}_t \equiv (\mathbf{z}_t, y_{t-1})$ , then equation (13.54) means that, along with  $\mathbf{z}_t$ , only one lag of  $y_t$  is needed to capture all of the dynamics.

Showing that condition (13.52) holds under dynamic completeness is easy. First, for each t,  $E[\mathbf{s}_{it}(\boldsymbol{\theta}_0) | \mathbf{x}_{it}] = \mathbf{0}$ , since  $f_t(y_t | \mathbf{x}_t; \boldsymbol{\theta}_0)$  is a correctly specified conditional density. But then, under assumption (13.54),

$$E[\mathbf{s}_{it}(\boldsymbol{\theta}_{o}) | \mathbf{x}_{it}, y_{i,t-1}, \dots, y_{i1}, \mathbf{x}_{i1}] = \mathbf{0}$$
(13.55)

Now consider the expected value in condition (13.52) for r < t. Since  $\mathbf{s}_{ir}(\theta_0)$  is a function of  $(\mathbf{x}_{ir}, y_{ir})$ , which is in the conditioning set (13.55), the usual iterated expectations argument shows that condition (13.52) holds. It follows that, under dynamic completeness, the usual maximum likelihood statistics from the pooled estimation are asymptotically valid. This result is completely analogous to pooled OLS

{420}------------------------------------------------

under dynamic completeness of the conditional mean and homoskedasticity (see Section 7.8).

If the panel data probit model is dynamically complete, any software package that does standard probit can be used to obtain valid standard errors and test statistics, provided the response probability satisfies Pðyit ¼ 1 j xitÞ ¼ Pðyit ¼ 1 j xit; yi;t<sup>1</sup>; x<sup>i</sup>;t<sup>1</sup>; ...Þ. Without dynamic completeness the standard errors and test statistics generally need to be adjusted for serial dependence.

Since dynamic completeness affords nontrivial simplifications, does this fact mean that we should always include lagged values of exogenous and dependent variables until equation (13.54) appears to be satisfied? Not necessarily. Static models are sometimes desirable even if they neglect dynamics. For example, suppose that we have panel data on individuals in an occupation where pay is determined partly by cumulative productivity. (Professional athletes and college professors are two examples.) An equation relating salary to the productivity measures, and possibly demographic variables, is appropriate. Nothing implies that the equation would be dynamically complete; in fact, past salary could help predict current salary, even after controlling for observed productivity. But it does not make much sense to include past salary in the regression equation. As we know from Chapter 10, a reasonable approach is to include an unobserved effect in the equation, and this does not lead to a model with complete dynamics. See also Section 13.9.

We may wish to test the null hypothesis that the density is dynamically complete. White (1994) shows how to test whether the score is serially correlated in a pure time series setting. A similar approach can be used with panel data. A general test for dynamic misspecification can be based on the limiting distribution of (the vectorization of )

$$N^{-1/2} \sum_{i=1}^{N} \sum_{t=2}^{T} \hat{\mathbf{s}}_{it} \hat{\mathbf{s}}'_{i,t-1}$$

where the scores are evaluated at the partial MLE. Rather than derive a general statistic here, we will study tests of dynamic completeness in particular applications later (see particularly Chapters 15, 16, and 19).