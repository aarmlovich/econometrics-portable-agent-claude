# Linear Models: OLS and 2SLS

> Pages: 560-564

We begin by obtaining conditions under which estimation of the population model by 2SLS using the selected sample is consistent for the population parameters. These


{561}------------------------------------------------

results are of interest in their own right, but we will also apply them to several specific models later in the chapter.

We assume that there is a population represented by the random vector ðx; y; zÞ, where x is a 1 K vector of explanatory variables, y is the scalar response variable, and z is a 1 L vector of instruments.

The population model is the standard single-equation linear model with possibly endogenous explanatory variables:

$$y = \beta_1 + \beta_2 x_2 + \dots + \beta_K x_K + u \tag{17.3}$$

$$\mathbf{E}(u\,|\,\mathbf{z}) = 0\tag{17.4}$$

where we take x<sup>1</sup> 11 for notational simplicity. The sense in which the instruments z are exogenous, given in assumption (17.4), is stronger than we need for 2SLS to be consistent when using a random sample from the population. With random sampling, the zero correlation condition Eðz<sup>0</sup> uÞ ¼ 0 is sufficient. If we could obtain a random sample from the population, equation (17.3) could be estimated by 2SLS under the condition rank½Eðz<sup>0</sup> xÞ ¼ K.

A leading special case is z ¼ x, so that the explanatory variables are exogenous and equation (17.3) is a model of the conditional expectation Eðy j xÞ:

$$E(y | \mathbf{x}) = \beta_1 + \beta_2 x_2 + \dots + \beta_K x_K$$
 (17.5)

But our general treatment allows elements of x to be correlated with u.

Rather than obtaining a random sample—that is, a sample representative of the population—we only use data points that satisfy certain conditions. Let s be a binary selection indicator representing a random draw from the population. By definition, s ¼ 1 if we use the draw in the estimation, and s ¼ 0 if we do not. Usually, we do not use observations when s ¼ 0 because data on at least some elements of ðx; y; zÞ are unobserved—because of survey design, nonresponse, or incidental truncation.

The key assumption underlying the validity of 2SLS on selected sample is

$$E(u \mid \mathbf{z}, s) = 0 \tag{17.6}$$

There are some important cases where assumption (17.6) necessarily follows from assumption (17.4). If s is a deterministic function of z, then Eðu j z;sÞ ¼ Eðu j zÞ. Such cases arise when selection is a fixed rule involving only the exogenous variables z. Also, if selection is independent of ðz; uÞ—a sufficient condition is that selection is independent of ðx; y; zÞ—then Eðu j z;sÞ ¼ Eðu j zÞ.

In estimating equation (17.3), we apply 2SLS to the observations for which s ¼ 1. To study the properties of the 2SLS estimator on the selected sample, let

{562}------------------------------------------------

 $\{(\mathbf{x}_i, y_i, \mathbf{z}_i, s_i): i = 1, 2, \dots, N\}$  denote a random sample from the *population*. We use observation i if  $s_i = 1$ , but not if  $s_i = 0$ . Therefore, we do not actually have N observations to use in the estimation; in fact, we do not even need to know N.

The 2SLS estimator using the selected sample can be expressed as

$$\hat{\boldsymbol{\beta}} = \left[ \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{x}_i \right)' \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{z}_i \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{x}_i \right) \right]^{-1}$$

$$\times \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{x}_i \right)' \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{z}_i \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{y}_i \right)$$

Substituting  $y_i = \mathbf{x}_i \boldsymbol{\beta} + u_i$  gives

$$\hat{\boldsymbol{\beta}} = \boldsymbol{\beta} + \left[ \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{x}_i \right)' \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{z}_i \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{x}_i \right) \right]^{-1}$$

$$\times \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{x}_i \right)' \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{z}_i \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} s_i \mathbf{z}_i' \mathbf{u}_i \right)$$

$$(17.7)$$

By assumption,  $E(u_i | \mathbf{z}_i, s_i) = 0$ , and so  $E(s_i \mathbf{z}_i' u_i) = \mathbf{0}$  by iterated expectations. [In the case where s is a function of  $\mathbf{z}$ , this result shows why assumption (17.4) cannot be replaced with  $E(\mathbf{z}'u) = \mathbf{0}$ .] Now the law of large numbers applies to show that plim  $\hat{\boldsymbol{\beta}} = \boldsymbol{\beta}$ , at least under a modification of the rank condition. We summarize with a theorem:

THEOREM 17.1 (Consistency of 2SLS under Sample Selection): In model (17.3), assume that  $E(u^2) < \infty$ ,  $E(x_j^2) < \infty$ , j = 1, ..., K, and  $E(z_j^2) < \infty$ , j = 1, ..., L. Maintain assumption (17.6) and, in addition, assume

$$rank E(\mathbf{z}'\mathbf{z} | s = 1) = L \tag{17.8}$$

$$\operatorname{rank} E(\mathbf{z}'\mathbf{x} \mid s=1) = K \tag{17.9}$$

Then the 2SLS estimator using the selected sample is consistent for  $\beta$  and  $\sqrt{N}$ -asymptotically normal. Further, if  $E(u^2 | \mathbf{z}, s) = \sigma^2$ , then the usual asymptotic variance of the 2SLS estimator is valid.

Equation (17.7) essentially proves the consistency result. Showing that the usual 2SLS asymptotic variance matrix is valid requires two steps. First, under the homo-

{563}------------------------------------------------

skedasticity assumption in the population, the usual iterated expectations argument gives  $E(su^2\mathbf{z}'\mathbf{z}) = \sigma^2 E(s\mathbf{z}'\mathbf{z})$ . This equation can be used to show that Avar  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})$  =  $\sigma^2 \{E(s\mathbf{x}'\mathbf{z})[E(s\mathbf{z}'\mathbf{z})]^{-1}E(s\mathbf{z}'\mathbf{x})\}^{-1}$ . The second step is to show that the usual 2SLS estimator of  $\sigma^2$  is consistent. This fact can be seen as follows. Under the homoskedasticity assumption,  $E(su^2) = E(s)\sigma^2$ , where E(s) is just the fraction of the subpopulation in the overall population. The estimator of  $\sigma^2$  (without degrees-of-freedom adjustment) is

$$\left(\sum_{i=1}^{N} s_i\right)^{-1} \sum_{i=1}^{N} s_i \hat{\boldsymbol{u}}_i^2 \tag{17.10}$$

since  $\sum_{i=1}^{N} s_i$  is simply the number of observations in the selected sample. Removing the "~" from  $u_i^2$  and applying the law of large numbers gives  $N^{-1} \sum_{i=1}^{N} s_i \stackrel{p}{\to} E(s)$  and  $N^{-1} \sum_{i=1}^{N} s_i u_i^2 \stackrel{p}{\to} E(su^2) = E(s)\sigma^2$ . Since the  $N^{-1}$  terms cancel, expression (17.10) converges in probability to  $\sigma^2$ .

If s is a function only of **z**, or s is independent of  $(\mathbf{z}, u)$ , and  $\mathrm{E}(u^2 \mid \mathbf{z}) = \sigma^2$ —that is, if the homoskedasticity assumption holds in the original population—then  $\mathrm{E}(u^2 \mid \mathbf{z}, s) = \sigma^2$ . Without the homoskedasticity assumption we would just use the heteroskedasticity-robust standard errors, just as if a random sample were available with heteroskedasticity present in the population model.

When  $\mathbf{x}$  is exogenous and we apply OLS on the selected sample, Theorem 17.1 implies that we can select the sample on the basis of the explanatory variables. Selection based on y or on endogenous elements of  $\mathbf{x}$  is not allowed because then  $\mathrm{E}(u \mid \mathbf{z}, s) \neq \mathrm{E}(u)$ .

Example 17.4 (Nonrandomly Missing IQ Scores): As an example of how Theorem 17.1 can be applied, consider the analysis in Griliches, Hall, and Hausman (1978) (GHH). The structural equation of interest is

$$\log(wage) = \mathbf{z}_1 \boldsymbol{\delta}_1 + abil + v, \qquad \mathrm{E}(v \mid \mathbf{z}_1, abil, IQ) = 0$$

and we assume that IQ is a valid proxy for *abil* in the sense that  $abil = \theta_1 IQ + e$  and  $E(e | \mathbf{z}_1, IQ) = 0$  (see Section 4.3.2). Write

$$\log(wage) = \mathbf{z}_1 \boldsymbol{\delta}_1 + \theta_1 IQ + u \tag{17.11}$$

where u = v + e. Under the assumptions made,  $E(u | \mathbf{z}_1, IQ) = 0$ . It follows immediately from Theorem 17.1 that, if we choose the sample excluding all people with IQs below a fixed value, then OLS estimation of equation (17.11) will be consistent. This problem is not quite the one faced by GHH. Instead, GHH noticed that the

{564}------------------------------------------------

probability of IQ missing was higher at lower IQs (because people were reluctant to give permission to obtain IQ scores). A simple way to model this situation is s ¼ 1 if IQ þ rb0, s ¼ 0 if IQ þ r < 0, where r is an unobserved random variable. If r is redundant in the structural equation and in the proxy variable equation for IQ, that is, if Eðv j z1; abil;IQ;rÞ ¼ 0 and Eðe j z1;IQ;rÞ ¼ 0, then Eðu j z1;IQ;rÞ ¼ 0. Since s is a function of IQ and r, it follows immediately that Eðu j z1;IQ;sÞ ¼ 0. Therefore, using OLS on the sample for which IQ is observed yields consistent estimators.

If r is correlated with either v or e, Eðu j z1;IQ;sÞ 0 EðuÞ in general, and OLS estimation of equation (17.11) using the selected sample would not consistently estimate *d*<sup>1</sup> and y1. Therefore, even though IQ is exogenous in the population equation (17.11), the sample selection is not exogenous. In Section 17.4.2 we cover a method that can be used to correct for sample selection bias.

Theorem 17.1 has other useful applications. Suppose that x is exogenous in equation (17.3) and that s is a nonrandom function of ðx; vÞ, where v is a variable not appearing in equation (17.3). If ðu; vÞ is independent of x, then Eðu j x; vÞ ¼ Eðu j vÞ, and so

$$E(y | \mathbf{x}) = \mathbf{x}\boldsymbol{\beta} + E(u | \mathbf{x}, v) = \mathbf{x}\boldsymbol{\beta} + E(u | v)$$

If we make an assumption about the functional form of Eðu j vÞ, for example, Eðu j vÞ ¼ gv, then we can write

$$y = \mathbf{x}\boldsymbol{\beta} + \gamma v + e, \qquad \mathbf{E}(e \mid \mathbf{x}, v) = 0 \tag{17.12}$$

where e ¼ u Eðu j vÞ. Because s is just a function of ðx; vÞ, Eðe j x; v;sÞ ¼ 0, and so *b* and g can be estimated consistently by the OLS regression y on x, v, using the selected sample. Effectively, including v in the regression on the selected subsample eliminates the sample selection problem and allows us to consistently estimate *b*. [Incidentally, because v is independent of x, we would not have to include it in equation (17.3) to consistently estimate *b* if we had a random sample from the population. However, including v would result in an asymptotically more efficient estimator of *b* when Varðy j x; vÞ is homoskedastic. See Problem 4.5.] In Section 17.5 we will see how equation (17.12) can be implemented.