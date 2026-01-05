# Derivations of Expected Values

> Pages: 530-536

In corner solution applications such as the charitable contributions example, interest centers on probabilities or expectations involving y. Most of the time we focus on the expected values Eðy j x; y > 0Þ and Eðy j xÞ.

Before deriving these expectations for the Tobit model, it is interesting to derive an inequality that bounds Eðy j xÞ from below. Since the function gðzÞ 1 maxð0; zÞ is convex, it follows from the conditional Jensen's inequality (see Appendix 2A) that Eðy j xÞ bmax½0; Eðy j xÞ. This condition holds when y has any distribution and for any form of Eðy j xÞ. If Eðy j xÞ ¼ x*b*, then

$$E(y \mid \mathbf{x}) \ge \max(0, \mathbf{x}\boldsymbol{\beta}) \tag{16.7}$$

which is always nonnegative. Equation (16.7) shows that Eðy j xÞ is bounded from below by the larger of zero and x*b*.

When u is independent of x and has a normal distribution, we can find an explicit expression for Eðy j xÞ. We first derive Pðy > 0 j xÞ and Eðy j x; y > 0Þ, which are of interest in their own right. Then, we use the law of iterated expectations to obtain Eðy j xÞ:

$$E(y \mid \mathbf{x}) = P(y = 0 \mid \mathbf{x}) \cdot 0 + P(y > 0 \mid \mathbf{x}) \cdot E(y \mid \mathbf{x}, y > 0)$$
  
=  $P(y > 0 \mid \mathbf{x}) \cdot E(y \mid \mathbf{x}, y > 0)$  (16.8)

Deriving Pðy > 0 j xÞ is easy. Define the binary variable w ¼ 1 if y > 0, w ¼ 0 if y ¼ 0. Then w follows a probit model:

$$P(w = 1 \mid \mathbf{x}) = P(y^* > 0 \mid \mathbf{x}) = P(u > -\mathbf{x}\boldsymbol{\beta} \mid \mathbf{x})$$
$$= P(u/\sigma > -\mathbf{x}\boldsymbol{\beta}/\sigma) = \Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)$$
(16.9)

One implication of equation (16.9) is that *g* 1*b*=s, but not *b* and s separately, can be consistently estimated from a probit of w on x.

To derive Eðy j x; y > 0Þ, we need the following fact about the normal distribution: if z @Normalð0; 1Þ, then, for any constant c,

$$E(z | z > c) = \frac{\phi(c)}{1 - \Phi(c)}$$


{531}------------------------------------------------

where  $\phi(\cdot)$  is the standard normal density function. {This is easily shown by noting that the density of z given z > c is  $\phi(z)/[1 - \Phi(c)]$ , z > c, and then integrating  $z\phi(z)$  from c to  $\infty$ .} Therefore, if  $u \sim \text{Normal}(0, \sigma^2)$ , then

$$E(u \mid u > c) = \sigma E\left(\frac{u}{\sigma} \mid \frac{u}{\sigma} > \frac{c}{\sigma}\right) = \sigma \left[\frac{\phi(c/\sigma)}{1 - \Phi(c/\sigma)}\right]$$

We can use this equation to find  $E(y | \mathbf{x}, y > 0)$  when y follows a Tobit model:

$$E(y \mid \mathbf{x}, y > 0) = \mathbf{x}\boldsymbol{\beta} + E(u \mid u > -\mathbf{x}\boldsymbol{\beta}) = \mathbf{x}\boldsymbol{\beta} + \sigma \left[ \frac{\phi(\mathbf{x}\boldsymbol{\beta}/\sigma)}{\Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)} \right]$$
(16.10)

since  $1 - \Phi(-\mathbf{x}\boldsymbol{\beta}/\sigma) = \Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)$ . Although it is not obvious from looking at equation (16.10), the right-hand side is positive for any values of  $\mathbf{x}$  and  $\boldsymbol{\beta}$ ; this statement must be true by equations (16.7) and (16.8).

For any c the quantity  $\lambda(c) \equiv \phi(c)/\Phi(c)$  is called the **inverse Mills ratio**. Thus,  $\mathrm{E}(y \mid \mathbf{x}, y > 0)$  is the sum of  $\mathbf{x}\boldsymbol{\beta}$  and  $\sigma$  times the inverse Mills ratio evaluated at  $\mathbf{x}\boldsymbol{\beta}/\sigma$ . If  $x_j$  is a continuous explanatory variable, then

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x}, y > 0)}{\partial x_i} = \beta_j + \beta_j \left[ \frac{\mathrm{d}\lambda}{\mathrm{d}c} (\mathbf{x}\boldsymbol{\beta}/\sigma) \right]$$

assuming that  $x_j$  is not functionally related to other regressors. By differentiating  $\lambda(c) = \phi(c)/\Phi(c)$ , it can be shown that  $\frac{\mathrm{d}\lambda}{\mathrm{d}c}(c) = -\lambda(c)[c+\lambda(c)]$ , and therefore

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x}, y > 0)}{\partial x_i} = \beta_j \{ 1 - \lambda (\mathbf{x} \boldsymbol{\beta} / \sigma) [\mathbf{x} \boldsymbol{\beta} / \sigma + \lambda (\mathbf{x} \boldsymbol{\beta} / \sigma)] \}$$
(16.11)

This equation shows that the partial effect of  $x_j$  on  $E(y | \mathbf{x}, y > 0)$  is not entirely determined by  $\beta_j$ ; there is an adjustment factor multiplying  $\beta_j$ , the term in  $\{\cdot\}$ , that depends on  $\mathbf{x}$  through the index  $\mathbf{x}\boldsymbol{\beta}/\sigma$ . We can use the fact that if  $z \sim \text{Normal}(0,1)$ , then  $\text{Var}(z | z > -c) = 1 - \lambda(c)[c + \lambda(c)]$  for any  $c \in \mathbb{R}$ , which implies that the adjustment factor in equation (16.11), call it  $\theta(\mathbf{x}\boldsymbol{\beta}/\sigma) = \{1 - \lambda(\mathbf{x}\boldsymbol{\beta}/\sigma)[\mathbf{x}\boldsymbol{\beta}/\sigma + \lambda(\mathbf{x}\boldsymbol{\beta}/\sigma)]\}$ , is strictly between zero and one. Therefore, the sign of  $\beta_j$  is the same as the sign of the partial effect of  $x_j$ .

Other functional forms are easily handled. Suppose that  $x_1 = \log(z_1)$  (and that this is the only place  $z_1$  appears in  $\mathbf{x}$ ). Then

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x}, y > 0)}{\partial z_1} = (\beta_1/z_1)\theta(\mathbf{x}\boldsymbol{\beta}/\sigma)$$
(16.12)

{532}------------------------------------------------

where  $\beta_1$  now denotes the coefficient on  $\log(z_1)$ . Or, suppose that  $x_1 = z_1$  and  $x_2 = z_1^2$ . Then

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x}, y > 0)}{\partial z_1} = (\beta_1 + 2\beta_2 z_1)\theta(\mathbf{x}\boldsymbol{\beta}/\sigma)$$

where  $\beta_1$  is the coefficient on  $z_1$  and  $\beta_2$  is the coefficient on  $z_1^2$ . Interaction terms are handled similarly. Generally, we compute the partial effect of  $\mathbf{x}\boldsymbol{\beta}$  with respect to the variable of interest and multiply this by the factor  $\theta(\mathbf{x}\boldsymbol{\beta}/\sigma)$ .

All of the usual economic quantities such as elasticities can be computed. The elasticity of y with respect to  $x_1$ , conditional on y > 0, is

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x}, y > 0)}{\partial x_1} \cdot \frac{x_1}{\mathbf{E}(y \mid \mathbf{x}, y > 0)} \tag{16.13}$$

and equations (16.11) and (16.10) can be used to find the elasticity when  $x_1$  appears in levels form. If  $z_1$  appears in logarithmic form, the elasticity is obtained simply as  $\partial \log E(y | \mathbf{x}, y > 0) / \partial \log(z_1)$ .

If  $x_1$  is a binary variable, the effect of interest is obtained as the difference between  $E(y | \mathbf{x}, y > 0)$  with  $x_1 = 1$  and  $x_1 = 0$ . Other discrete variables (such as number of children) can be handled similarly.

We can also compute  $E(y | \mathbf{x})$  from equation (16.8):

$$E(y | \mathbf{x}) = P(y > 0 | \mathbf{x}) \cdot E(y | \mathbf{x}, y > 0)$$

$$= \Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)[\mathbf{x}\boldsymbol{\beta} + \sigma\lambda(\mathbf{x}\boldsymbol{\beta}/\sigma)] = \Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)\mathbf{x}\boldsymbol{\beta} + \sigma\phi(\mathbf{x}\boldsymbol{\beta}/\sigma)$$
(16.14)

We can find the partial derivatives of  $E(y | \mathbf{x})$  with respect to continuous  $x_j$  using the chain rule. In examples where y is some quantity chosen by individuals (labor supply, charitable contributions, life insurance), this derivative accounts for the fact that some people who start at y = 0 may switch to y > 0 when  $x_j$  changes. Formally,

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_j} = \frac{\partial \mathbf{P}(y > 0 \mid \mathbf{x})}{\partial x_j} \cdot \mathbf{E}(y \mid \mathbf{x}, y > 0) + \mathbf{P}(y > 0 \mid \mathbf{x}) \cdot \frac{\partial \mathbf{E}(y \mid \mathbf{x}, y > 0)}{\partial x_j}$$
(16.15)

This decomposition is attributed to McDonald and Moffitt (1980). Because  $P(y > 0 \mid \mathbf{x}) = \Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)$ ,  $\partial P(y > 0 \mid \mathbf{x})/\partial x_j = (\beta_j/\sigma)\phi(\mathbf{x}\boldsymbol{\beta}/\sigma)$ . If we plug this along with equation (16.11) into equation (16.15), we get a remarkable simplification:

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_i} = \Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)\beta_j \tag{16.16}$$

The estimated scale factor for a given  $\mathbf{x}$  is  $\Phi(\mathbf{x}\hat{\boldsymbol{\beta}}/\hat{\sigma})$ . This scale factor has a very interesting interpretation:  $\Phi(\mathbf{x}\hat{\boldsymbol{\beta}}/\hat{\sigma}) = \hat{\mathbf{P}}(y > 0 \,|\, \mathbf{x})$ ; that is,  $\Phi(\mathbf{x}\hat{\boldsymbol{\beta}}/\hat{\sigma})$  is the estimated

{533}------------------------------------------------

probability of observing a positive response given x. If Fðx ^*b*=s^Þ is close to one, then it is unlikely we observe yi ¼ 0 when x<sup>i</sup> ¼ x, and the adjustment factor becomes unimportant. In practice, a single adjustment factor is obtained as Fðx ^*b*=s^Þ, where x denotes the vector of mean values. If the estimated probability of a positive response is close to one at the sample means of the covariates, the adjustment factor can be ignored. In most interesting Tobit applications, Fðx ^*b*=s^Þ is notably less than unity.

For discrete variables or for large changes in continuous variables, we can compute the difference in Eðy j xÞ at different values of x. [Incidentally, equations (16.11) and (16.16) show that s is not a ''nuisance parameter,'' as it is sometimes called in Tobit applications: s plays a crucial role in estimating the partial effects of interest in corner solution applications.]

Equations (16.9), (16.11), and (16.14) show that, for continuous variables xj and xh, the relative partial effects on Pðy > 0 j xÞ, Eðy j x; y > 0Þ, and Eðy j xÞ are all equal to bj=b<sup>h</sup> (assuming that b<sup>h</sup> 00). This fact can be a limitation of the Tobit model, something we take up further in Section 16.7.

By taking the log of equation (16.8) and differentiating, we see that the elasticity (or semielasticity) of Eðy j xÞ with respect to any xj is simply the sum of the elasticities (or semielasticities) of Fðx*b*=sÞ and Eðy j x; y > 0Þ, each with respect to xj.

# 16.3 Inconsistency of OLS

We can use the previous expectation calculations to show that OLS using the entire sample or OLS using the subsample for which yi > 0 are both (generally) inconsistent estimators of *b*. First consider OLS using the subsample with strictly positive yi. From equation (16.10) we can write

$$y_i = \mathbf{x}_i \boldsymbol{\beta} + \sigma \lambda (\mathbf{x}_i \boldsymbol{\beta} / \sigma) + e_i \tag{16.17}$$

$$E(e_i \mid \mathbf{x}_i, y_i > 0) = 0 \tag{16.18}$$

which implies that Eðei j xi; li; yi > 0Þ ¼ 0, where l<sup>i</sup> 1 lðxi*b*=sÞ. It follows that if we run OLS of yi on x<sup>i</sup> using the sample for which yi > 0, we effectively omit the variable li. Correlation between l<sup>i</sup> and x<sup>i</sup> in the selected subpopulation results in inconsistent estimation of *b*.

The inconsistency of OLS restricted to the subsample with yi > 0 is especially unfortunate in the case of true data censoring. Restricting the sample to yi > 0 means we are only using the data on uncensored observations. In the wealth top coding example, this restriction means we drop all people whose wealth is at least \$200,000. In a duration application—see Problem 16.1 and Chapter 20—it would mean using 

{534}------------------------------------------------

only observations with uncensored durations. It would be convenient if OLS using only the uncensored observations were consistent for  $\beta$ , but such is not the case.

From equation (16.14) it is also pretty clear that regressing  $y_i$  on  $\mathbf{x}_i$  using all of the data will not consistently estimate  $\boldsymbol{\beta}$ :  $\mathrm{E}(y | \mathbf{x})$  is nonlinear in  $\mathbf{x}$ ,  $\boldsymbol{\beta}$ , and  $\sigma$ , so it would be a fluke if a linear regression consistently estimated  $\boldsymbol{\beta}$ .

There are some interesting theoretical results about how the slope coefficients in  $\beta$  can be estimated up to scale using one of the two OLS regressions that we have discussed. Therefore, each OLS coefficient is inconsistent by the *same* multiplicative factor. This fact allows us—both in data-censoring applications and corner solution applications—to estimate the relative effects of any two explanatory variables. The assumptions made to derive such results are very restrictive, and they generally rule out discrete and other discontinuous regressors. [Multivariate normality of  $(\mathbf{x}, y^*)$  is sufficient.] The arguments, which rely on linear projections, are elegant—see, for example, Chung and Goldberger (1984)—but such results have questionable practical value.

The previous discussion does not mean a linear regression of  $y_i$  on  $\mathbf{x}_i$  is uninformative. Remember that, whether or not the Tobit model holds, we can always write the linear projection of y on  $\mathbf{x}$  as  $\mathbf{L}(y | \mathbf{x}) = \mathbf{x} \mathbf{y}$  for  $y = [\mathbf{E}(\mathbf{x}'\mathbf{x})]^{-1}\mathbf{E}(\mathbf{x}'y)$ , under the mild restriction that all second moments are finite. It is possible that  $y_i$  approximates the effect of  $x_i$  on  $\mathbf{E}(y | \mathbf{x})$  when  $\mathbf{x}$  is near its population mean. Similarly, a linear regression of  $y_i$  on  $\mathbf{x}_i$ , using only observations with  $y_i > 0$ , might approximate the partial effects on  $\mathbf{E}(y | \mathbf{x}, y > 0)$  near the mean values of the  $x_j$ . Such issues have not been fully explored in corner solution applications of the Tobit model.

#### 16.4 Estimation and Inference with Censored Tobit

Let  $\{(\mathbf{x}_i, y_i): i = 1, 2, \dots N\}$  be a random sample following the censored Tobit model. To use maximum likelihood, we need to derive the density of  $y_i$  given  $\mathbf{x}_i$ . We have already shown that  $f(0 | \mathbf{x}_i) = P(y_i = 0 | \mathbf{x}_i) = 1 - \Phi(\mathbf{x}_i \boldsymbol{\beta}/\sigma)$ . Further, for y > 0,  $P(y_i \le y | \mathbf{x}_i) = P(y_i^* \le y | \mathbf{x}_i)$ , which implies that

$$f(y | \mathbf{x}_i) = f^*(y | \mathbf{x}_i), \quad \text{all } y > 0$$

where  $f^*(\cdot | \mathbf{x}_i)$  denotes the density of  $y_i^*$  given  $\mathbf{x}_i$ . (We use y as the dummy argument in the density.) By assumption,  $y_i^* | \mathbf{x}_i \sim \text{Normal}(\mathbf{x}_i \boldsymbol{\beta}, \sigma^2)$ , so

$$f^*(y | \mathbf{x}_i) = \frac{1}{\sigma} \phi[(y - \mathbf{x}_i \boldsymbol{\beta})/\sigma], \qquad -\infty < y < \infty$$

{535}------------------------------------------------

(As in recent chapters, we will use  $\beta$  and  $\sigma^2$  to denote the true values as well as dummy arguments in the log-likelihood function and its derivatives.) We can write the density for  $y_i$  given  $\mathbf{x}_i$  compactly using the indicator function  $1[\cdot]$  as

$$f(\mathbf{y} \mid \mathbf{x}_i) = \left\{1 - \Phi(\mathbf{x}_i \boldsymbol{\beta}/\sigma)\right\}^{1[\mathbf{y}=0]} \left\{ (1/\sigma)\phi[(\mathbf{y} - \mathbf{x}_i \boldsymbol{\beta})/\sigma] \right\}^{1[\mathbf{y}>0]}$$
(16.19)

where the density is zero for y < 0. Let  $\theta = (\beta', \sigma^2)'$  denote the  $(K + 1) \times 1$  vector of parameters. The conditional log likelihood is

$$\ell_i(\boldsymbol{\theta}) = 1[y_i = 0] \log[1 - \Phi(\mathbf{x}_i \boldsymbol{\beta}/\sigma)] + 1[y_i > 0] \{\log \phi[(y_i - \mathbf{x}_i \boldsymbol{\beta})/\sigma] - \log(\sigma^2)/2\}$$
(16.20)

Apart from a constant that does not affect the maximization, equation (16.20) can be written as

$$1[y_i = 0] \log[1 - \Phi(\mathbf{x}_i \boldsymbol{\beta}/\sigma)] - 1[y_i > 0] \{(y_i - \mathbf{x}_i \boldsymbol{\beta})^2 / 2\sigma^2 + \log(\sigma^2) / 2\}$$

Therefore,

$$\partial \ell_i(\boldsymbol{\theta})/\partial \boldsymbol{\beta} = -1[y_i = 0]\phi(\mathbf{x}_i\boldsymbol{\beta}/\sigma)\mathbf{x}_i/[1 - \Phi(\mathbf{x}_i\boldsymbol{\beta}/\sigma)] + 1[y_i > 0](y_i - \mathbf{x}_i\boldsymbol{\beta})\mathbf{x}_i/\sigma^2$$
(16.21)

$$\partial \ell_i(\boldsymbol{\theta})/\partial \sigma^2 = 1[y_i = 0]\phi(\mathbf{x}_i\boldsymbol{\beta}/\sigma)(\mathbf{x}_i\boldsymbol{\beta})/\{2\sigma^2[1 - \Phi(\mathbf{x}_i\boldsymbol{\beta}/\sigma)]\}$$
$$+1[y_i > 0]\{(y_i - \mathbf{x}_i\boldsymbol{\beta})^2/(2\sigma^4) - 1/(2\sigma^2)\}$$
(16.22)

The second derivatives are complicated, but all we need is  $\mathbf{A}(\mathbf{x}_i, \boldsymbol{\theta}) \equiv -\mathbb{E}[\mathbf{H}_i(\boldsymbol{\theta}) \,|\, \mathbf{x}_i]$ . After tedious calculations it can be shown that

$$\mathbf{A}(\mathbf{x}_i, \boldsymbol{\theta}) = \begin{bmatrix} a_i \mathbf{x}_i' \mathbf{x}_i & b_i \mathbf{x}_i' \\ b_i \mathbf{x}_i & c_i \end{bmatrix}$$
(16.23)

where

$$a_{i} = -\sigma^{-2} \{ \mathbf{x}_{i} \gamma \phi_{i} - [\phi_{i}^{2}/(1 - \Phi_{i})] - \Phi_{i} \}$$

$$b_{i} = \sigma^{-3} \{ (\mathbf{x}_{i} \gamma)^{2} \phi_{i} + \phi_{i} - [(\mathbf{x}_{i} \gamma) \phi_{i}^{2}/(1 - \Phi_{i})] \} / 2$$

$$c_{i} = -\sigma^{-4} \{ (\mathbf{x}_{i} \gamma)^{3} \phi_{i} + (\mathbf{x}_{i} \gamma) \phi_{i} - [(\mathbf{x}_{i} \gamma) \phi_{i}^{2}/(1 - \Phi_{i})] - 2\Phi_{i} \} / 4$$

 $\gamma = \beta/\sigma$ , and  $\phi_i$  and  $\Phi_i$  are evaluated at  $\mathbf{x}_i \gamma$ . This matrix is used in equation (13.32) to obtain the estimate of Avar $(\hat{\boldsymbol{\theta}})$ . See Amemiya (1973) for details.

Testing is easily carried out in a standard MLE framework. Single exclusion restrictions are tested using asymptotic t statistics once  $\hat{\beta}_j$  and its asymptotic standard error have been obtained. Multiple exclusion restrictions are easily tested using the LR statistic, and some econometrics packages routinely compute the Wald statistic.

{536}------------------------------------------------

If the unrestricted model has so many variables that computation becomes an issue, the LM statistic is an attractive alternative.

The Wald statistic is the easiest to compute for testing nonlinear restrictions on *b*, just as in binary response analysis, because the unrestricted model is just standard Tobit.