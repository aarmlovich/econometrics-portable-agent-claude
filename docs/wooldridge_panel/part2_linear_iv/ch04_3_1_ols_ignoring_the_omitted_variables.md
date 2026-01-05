# OLS Ignoring the Omitted Variables

> Pages: 77-79

Because it is so prevalent in applied work, we now consider the omitted variables problem in more detail. A model that assumes an additive effect of the omitted variable is

$$E(y \mid x_1, x_2, \dots, x_K, q) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + \gamma q$$
(4.18)

where q is the omitted factor. In particular, we are interested in the  $\beta_j$ , which are the partial effects of the observed explanatory variables holding the other explanatory variables constant, *including* the unobservable q. In the context of this additive model, there is no point in allowing for more than one unobservable; any omitted factors are lumped into q. Henceforth we simply refer to q as the omitted variable.

A good example of equation (4.18) is seen when y is log(wage) and q includes ability. If  $x_K$  denotes a measure of education,  $\beta_K$  in equation (4.18) measures the partial effect of education on wages controlling for—or holding fixed—the level of ability (as well as other observed characteristics). This effect is most interesting from a policy perspective because it provides a causal interpretation of the return to education:  $\beta_K$  is the expected proportionate increase in wage if someone from the working population is exogenously given another year of education.

Viewing equation (4.18) as a structural model, we can always write it in error form

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + \gamma q + v \tag{4.19}$$

$$E(v | x_1, x_2, \dots, x_K, q) = 0 (4.20)$$

where v is the **structural error**. One way to handle the nonobservability of q is to put it into the error term. In doing so, nothing is lost by assuming E(q) = 0 because an intercept is included in equation (4.19). Putting q into the error term means we rewrite equation (4.19) as

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + u \tag{4.21}$$

{78}------------------------------------------------

$$u \equiv \gamma q + v \tag{4.22}$$

The error u in equation (4.21) consists of two parts. Under equation (4.20), v has zero mean and is uncorrelated with x1; x2; ... ; xK (and q). By normalization, q also has zero mean. Thus, EðuÞ ¼ 0. However, u is uncorrelated with x1; x2; ... ; xK if and only if q is uncorrelated with each of the observable regressors. If q is correlated with any of the regressors, then so is u, and we have an endogeneity problem. We cannot expect OLS to consistently estimate any bj. Although Eðu j xÞ 0EðuÞ in equation (4.21), the b<sup>j</sup> do have a structural interpretation because they appear in equation (4.19).

It is easy to characterize the plims of the OLS estimators when the omitted variable is ignored; we will call this the OLS omitted variables inconsistency or OLS omitted variables bias (even though the latter term is not always precise). Write the linear projection of q onto the observable explanatory variables as

$$q = \delta_0 + \delta_1 x_1 + \dots + \delta_K x_K + r \tag{4.23}$$

where, by definition of a linear projection, EðrÞ ¼ 0, Covðxj;rÞ ¼ 0, j ¼ 1; 2; ... ; K. Then we can easily infer the plim of the OLS estimators from regressing y onto 1; x1; ... ; xK by finding an equation that does satisfy Assumptions OLS.1 and OLS.2. Plugging equation (4.23) into equation (4.19) and doing simple algrebra gives

$$y = (\beta_0 + \gamma \delta_0) + (\beta_1 + \gamma \delta_1)x_1 + (\beta_2 + \gamma \delta_2)x_2 + \dots + (\beta_K + \gamma \delta_K)x_K + v + \gamma r$$

Now, the error v þ gr has zero mean and is uncorrelated with each regressor. It follows that we can just read off the plim of the OLS estimators from the regression of y on 1; <sup>x</sup>1; ... ; xK : plim ^b<sup>j</sup> <sup>¼</sup> <sup>b</sup><sup>j</sup> <sup>þ</sup> gdj. Sometimes it is assumed that most of the <sup>d</sup><sup>j</sup> are zero. When the correlation between q and a particular variable, say xK , is the focus, a common (usually implicit) assumption is that all d<sup>j</sup> in equation (4.23) except the intercept and coefficient on xK are zero. Then plim ^b<sup>j</sup> <sup>¼</sup> <sup>b</sup>j, <sup>j</sup> <sup>¼</sup> <sup>1</sup>; ... ; <sup>K</sup> 1, and

$$plim \hat{\beta}_K = \beta_K + \gamma [Cov(x_K, q) / Var(x_K)]$$
(4.24)

[since d<sup>K</sup> ¼ CovðxK ; qÞ=VarðxK Þ in this case]. This formula gives us a simple way to determine the sign, and perhaps the magnitude, of the inconsistency in ^b<sup>K</sup> . If <sup>g</sup> <sup>&</sup>gt; <sup>0</sup> and xK and q are positively correlated, the asymptotic bias is positive. The other combinations are easily worked out. If xK has substantial variation in the population relative to the covariance between xK and q, then the bias can be small. In the general case of equation (4.23), it is difficult to sign d<sup>K</sup> because it measures a partial correlation. It is for this reason that d<sup>j</sup> ¼ 0, j ¼ 1; ... ; K 1 is often maintained for determining the likely asymptotic bias in ^b<sup>K</sup> when only xK is endogenous.

{79}------------------------------------------------

Example 4.2 (Wage Equation with Unobserved Ability): Write a structural wage equation explicitly as

$$\log(wage) = \beta_0 + \beta_1 exper + \beta_2 exper^2 + \beta_3 educ + \gamma abil + v$$

where v has the structural error property  $\mathrm{E}(v \mid exper, educ, abil) = 0$ . If abil is uncorrelated with exper and  $exper^2$  once educ has been partialed out—that is,  $abil = \delta_0 + \delta_3 educ + r$  with r uncorrelated with exper and  $exper^2$ —then  $\mathrm{plim}\ \hat{\beta}_3 = \beta_3 + \gamma \delta_3$ . Under these assumptions the coefficients on exper and  $exper^2$  are consistently estimated by the OLS regression that omits ability. If  $\delta_3 > 0$  then  $\mathrm{plim}\ \hat{\beta}_3 > \beta_3$  (because  $\gamma > 0$  by definition), and the return to education is likely to be overestimated in large samples.