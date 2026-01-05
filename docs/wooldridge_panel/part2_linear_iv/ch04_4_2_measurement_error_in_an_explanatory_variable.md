# Measurement Error in an Explanatory Variable

> Pages: 89-92

Traditionally, measurement error in an explanatory variable has been considered a much more important problem than measurement error in the response variable. This point was suggested by Example 4.2, and in this subsection we develop the general case.

We consider the model with a single explanatory measured with error:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K^* + v \tag{4.41}$$

where  $y, x_1, \ldots, x_{K-1}$  are observable but  $x_K^*$  is not. We assume at a minimum that v has zero mean and is uncorrelated with  $x_1, x_2, \ldots, x_{K-1}, x_K^*$ ; in fact, we usually have in mind the structural model  $\mathrm{E}(y | x_1, \ldots, x_{K-1}, x_K^*) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_K x_K^*$ . If  $x_K^*$  were observed, OLS estimation would produce consistent estimators. Instead, we have a measure of  $x_K^*$ ; call it  $x_K$ . A maintained assumption is that v is also uncorrelated with  $x_K$ . This follows under the redundancy assumption  $\mathrm{E}(y | x_1, \ldots, x_{K-1}, x_K^*, x_K) = \mathrm{E}(y | x_1, \ldots, x_{K-1}, x_K^*)$ , an assumption we used in the proxy variable solution to the omitted variable problem. This means that  $x_K$  has no effect on y once the other explanatory variables, including  $x_K^*$ , have been controlled for. Since  $x_K^*$  is assumed to be the variable that affects y, this assumption is uncontroversial.

The measurement error in the population is simply

$$e_K = x_K - x_K^* (4.42)$$

and this can be positive, negative, or zero. We assume that the average measurement error in the population is zero:  $E(e_K) = 0$ , which has no practical consequences because we include an intercept in equation (4.41). Since v is assumed to be uncorrelated with  $x_K^*$  and  $x_K$ , v is also uncorrelated with  $e_K$ .

We want to know the properties of OLS if we simply replace  $x_K^*$  with  $x_K$  and run the regression of y on  $1, x_1, x_2, \ldots, x_K$ . These depend crucially on the assumptions we make about the measurement error. An assumption that is almost always maintained is that  $e_K$  is uncorrelated with the explanatory variables not measured with error:  $E(x_i e_K) = 0, j = 1, \ldots, K - 1$ .

The key assumptions involve the relationship between the measurement error and  $x_K^*$  and  $x_K$ . Two assumptions have been the focus in the econometrics literature, and these represent polar extremes. The first assumption is that  $e_K$  is uncorrelated with the *observed* measure,  $x_K$ :

$$Cov(x_K, e_K) = 0 (4.43)$$

{90}------------------------------------------------

From equation (4.42), if assumption (4.43) is true, then  $e_K$  must be correlated with the unobserved variable  $x_K^*$ . To determine the properties of OLS in this case, we write  $x_K^* = x_K - e_K$  and plug this into equation (4.41):

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + (v - \beta_K e_K)$$
(4.44)

Now, we have assumed that v and  $e_K$  both have zero mean and are uncorrelated with each  $x_j$ , including  $x_K$ ; therefore,  $v - \beta_K e_K$  has zero mean and is uncorrelated with the  $x_j$ . It follows that OLS estimation with  $x_K$  in place of  $x_K^*$  produces consistent estimators of all of the  $\beta_j$  (assuming the standard rank condition Assumption OLS.2). Since v is uncorrelated with  $e_K$ , the variance of the error in equation (4.44) is  $Var(v - \beta_K e_K) = \sigma_v^2 + \beta_K^2 \sigma_{e_K}^2$ . Therefore, except when  $\beta_K = 0$ , measurement error increases the error variance, which is not a surprising finding and violates none of the OLS assumptions.

The assumption that  $e_K$  is uncorrelated with  $x_K$  is analogous to the proxy variable assumption we made in the Section 4.3.2. Since this assumption implies that OLS has all its nice properties, this is not usually what econometricians have in mind when referring to measurement error in an explanatory variable. The **classical errors-invariables** (CEV) assumption replaces assumption (4.43) with the assumption that the measurement error is uncorrelated with the *unobserved* explanatory variable:

$$Cov(x_K^*, e_K) = 0 (4.45)$$

This assumption comes from writing the observed measure as the sum of the true explanatory variable and the measurement error,  $x_K = x_K^* + e_K$ , and then assuming the two components of  $x_K$  are uncorrelated. (This has nothing to do with assumptions about v; we are always maintaining that v is uncorrelated with  $x_K^*$  and  $x_K$ , and therefore with  $e_K$ .)

If assumption (4.45) holds, then  $x_K$  and  $e_K$  must be correlated:

$$Cov(x_K, e_K) = E(x_K e_K) = E(x_K^* e_K) + E(e_K^2) = \sigma_{e_K}^2$$
(4.46)

Thus, under the CEV assumption, the covariance between  $x_K$  and  $e_K$  is equal to the variance of the measurement error.

Looking at equation (4.44), we see that correlation between  $x_K$  and  $e_K$  causes problems for OLS. Because v and  $x_K$  are uncorrelated, the covariance between  $x_K$  and the composite error  $v - \beta_K e_K$  is  $Cov(x_K, v - \beta_K e_K) = -\beta_K Cov(x_K, e_K) = -\beta_K \sigma_{e_K}^2$ . It follows that, in the CEV case, the OLS regression of y on  $x_1, x_2, \ldots, x_K$  generally gives inconsistent estimators of *all* of the  $\beta_i$ .


{91}------------------------------------------------

The plims of the  $\hat{\beta}_j$  for  $j \neq K$  are difficult to characterize except under special assumptions. If  $x_K^*$  is uncorrelated with  $x_j$ , all  $j \neq K$ , then so is  $x_K$ , and it follows that plim  $\hat{\beta}_j = \beta_j$ , all  $j \neq K$ . The plim of  $\hat{\beta}_K$  can be characterized in any case. Problem 4.10 asks you to show that

$$\operatorname{plim}(\hat{\beta}_K) = \beta_K \left( \frac{\sigma_{r_K^*}^2}{\sigma_{r_K^*}^2 + \sigma_{e_K}^2} \right) \tag{4.47}$$

where  $r_K^*$  is the linear projection error in

$$x_K^* = \delta_0 + \delta_1 x_1 + \delta_2 x_2 + \dots + \delta_{K-1} x_{K-1} + r_K^*$$

An important implication of equation (4.47) is that, because the term multiplying  $\beta_K$  is always between zero and one,  $|\text{plim}(\hat{\beta}_K)| < |\beta_K|$ . This is called the **attenuation bias** in OLS due to classical errors-in-variables: on average (or in large samples), the estimated OLS effect will be *attenuated* as a result of the presence of classical errors-in-variables. If  $\beta_K$  is positive,  $\hat{\beta}_K$  will tend to underestimate  $\beta_K$ ; if  $\beta_K$  is negative,  $\hat{\beta}_K$  will tend to overestimate  $\beta_K$ .

In the case of a single explanatory variable (K = 1) measured with error, equation (4.47) becomes

$$\text{plim } \hat{\beta}_1 = \beta_1 \left( \frac{\sigma_{x_1^*}^2}{\sigma_{x_1^*}^2 + \sigma_{e_1}^2} \right)$$
 (4.48)

The term multiplying  $\beta_1$  in equation (4.48) is  $Var(x_1^*)/Var(x_1)$ , which is always less than unity under the CEV assumption (4.45). As  $Var(e_1)$  shrinks relative to  $Var(x_1^*)$ , the attentuation bias disappears.

In the case with multiple explanatory variables, equation (4.47) shows that it is not  $\sigma_{x_K^*}^2$  that affects  $\text{plim}(\hat{\beta}_K)$  but the variance in  $x_K^*$  after netting out the other explanatory variables. Thus, the more collinear  $x_K^*$  is with the other explanatory variables, the worse is the attenuation bias.

Example 4.8 (Measurement Error in Family Income): Consider the problem of estimating the causal effect of family income on college grade point average, after controlling for high school grade point average and SAT score:

$$colGPA = \beta_0 + \beta_1 faminc^* + \beta_2 hsGPA + \beta_3 SAT + v$$

where faminc\* is actual annual family income. Precise data on colGPA, hsGPA, and SAT are relatively easy to obtain from school records. But family income, especially

{92}------------------------------------------------

as reported by students, could be mismeasured. If  $faminc = faminc^* + e_1$ , and the CEV assumptions hold, then using reported family income in place of actual family income will bias the OLS estimator of  $\beta_1$  toward zero. One consequence is that a hypothesis test of  $H_0$ :  $\beta_1 = 0$  will have a higher probability of Type II error.

If measurement error is present in more than one explanatory variable, deriving the inconsistency in the OLS estimators under extensions of the CEV assumptions is complicated and does not lead to very usable results.

In some cases it is clear that the CEV assumption (4.45) cannot be true. For example, suppose that frequency of marijuana usage is to be used as an explanatory variable in a wage equation. Let  $smoked^*$  be the number of days, out of the last 30, that a worker has smoked marijuana. The variable smoked is the self-reported number of days. Suppose we postulate the standard measurement error model,  $smoked = smoked^* + e_1$ , and let us even assume that people try to report the truth. It seems very likely that people who do not smoke marijuana at all—so that  $smoked^* = 0$ —will also report smoked = 0. In other words, the measurement error is zero for people who never smoke marijuana. When  $smoked^* > 0$  it is more likely that someone miscounts how many days he or she smoked marijuana. Such miscounting almost certainly means that  $e_1$  and  $smoked^*$  are correlated, a finding which violates the CEV assumption (4.45).

A general situation where assumption (4.45) is necessarily false occurs when the observed variable  $x_K$  has a smaller population variance than the unobserved variable  $x_K^*$ . Of course, we can rarely know with certainty whether this is the case, but we can sometimes use introspection. For example, consider actual amount of schooling versus reported schooling. In many cases, reported schooling will be a rounded-off version of actual schooling; therefore, reported schooling is less variable than actual schooling.