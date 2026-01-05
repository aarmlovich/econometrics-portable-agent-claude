

{81}------------------------------------------------

Example 4.3 (Using IQ as a Proxy for Ability): We apply the proxy variable method to the data on working men in NLS80.RAW, which was used by Blackburn and Neumark (1992), to estimate the structural model

$$\log(wage) = \beta_0 + \beta_1 exper + \beta_2 tenure + \beta_3 married$$
$$+ \beta_4 south + \beta_5 urban + \beta_6 black + \beta_7 educ + \gamma abil + v$$
 (4.29)

where exper is labor market experience, married is a dummy variable equal to unity if married, south is a dummy variable for the southern region, urban is a dummy variable for living in an SMSA, black is a race indicator, and educ is years of schooling. We assume that IQ satisfies the proxy variable assumptions: in the linear projection abil ¼ y<sup>0</sup> þ y1IQ þ r, where r has zero mean and is uncorrelated with IQ, we also assume that r is uncorrelated with experience, tenure, education, and other factors appearing in equation (4.29). The estimated equations without and with IQ are

$$\log(\hat{w}age) = 5.40 + .014 \ exper + .012 \ tenure + .199 \ married \ (0.11) \ (.003) \ (.002) \ (.039)$$

$$- .091 \ south + .184 \ urban - .188 \ black + .065 \ educ \ (.026) \ (.027) \ (.038) \ (.006)$$
 $N = 935, \quad R^2 = .253$ 
 $\log(\hat{w}age) = 5.18 + .014 \ exper + .011 \ tenure + .200 \ married \ (0.13) \ (.003) \ (.002) \ (.039)$ 

$$- .080 \ south + .182 \ urban - .143 \ black + .054 \ educ \ (.026) \ (.027) \ (.039) \ (.007)$$

$$+ .0036 \ IQ \ (.0010)$$
 $N = 935, \quad R^2 = .263$ 

Notice how the return to schooling has fallen from about 6.5 percent to about 5.4 percent when IQ is added to the regression. This is what we expect to happen if ability and schooling are (partially) positively correlated. Of course, these are just the findings from one sample. Adding IQ explains only one percentage point more of the variation in logðwageÞ, and the equation predicts that 15 more IQ points (one standard deviation) increases wage by about 5.4 percent. The standard error on the return to education has increased, but the 95 percent confidence interval is still fairly tight.

{82}------------------------------------------------

Often the outcome of the dependent variable from an earlier time period can be a useful proxy variable.

Example 4.4 (Effects of Job Training Grants on Worker Productivity): The data in JTRAIN1.RAW are for 157 Michigan manufacturing firms for the years 1987, 1988, and 1989. These data are from Holzer, Block, Cheatham, and Knott (1993). The goal is to determine the effectiveness of job training grants on firm productivity. For this exercise, we use only the 54 firms in 1988 which reported nonmissing values of the scrap rate (number of items out of 100 that must be scrapped). No firms were awarded grants in 1987; in 1988, 19 of the 54 firms were awarded grants. If the training grant has the intended effect, the average scrap rate should be lower among firms receiving a grant. The problem is that the grants were not randomly assigned: whether or not a firm received a grant could be related to other factors unobservable to the econometrician that affect productivity. In the simplest case, we can write (for the 1988 cross section)

$$\log(scrap) = \beta_0 + \beta_1 grant + \gamma q + v$$

where v is orthogonal to grant but q contains unobserved productivity factors that might be correlated with grant, a binary variable equal to unity if the firm received a job training grant. Since we have the scrap rate in the previous year, we can use logðscrap1Þ as a proxy variable for q:

$$q = \theta_0 + \theta_1 \log(scrap_{-1}) + r$$

where r has zero mean and, by definition, is uncorrelated with logðscrap1Þ. We hope that r has no or little correlation with grant. Plugging in for q gives the estimable model

$$\log(scrap) = \delta_0 + \beta_1 grant + \gamma \theta_1 \log(scrap_{-1}) + r + v$$

From this equation, we see that b<sup>1</sup> measures the proportionate difference in scrap rates for two firms having the same scrap rates in the previous year, but where one firm received a grant and the other did not. This is intuitively appealing. The estimated equations are

$$\log(s\hat{c}rap) = .409 + .057 \ grant$$

$$(.240) \quad (.406)$$

$$N = 54, \qquad R^2 = .0004$$

$$\log(s\hat{c}rap) = .021 - .254 \ grant + .831 \ \log(scrap_{-1})$$

$$(.089) \quad (.147) \qquad (.044)$$

$$N = 54, \qquad R^2 = .873$$

{83}------------------------------------------------

Without the lagged scrap rate, we see that the grant appears, if anything, to reduce productivity (by increasing the scrap rate), although the coefficient is statistically insignificant. When the lagged dependent variable is included, the coefficient on grant changes signs, becomes economically large—firms awarded grants have scrap rates about 25.4 percent less than those not given grants—and the effect is significant at the 5 percent level against a one-sided alternative. [The more accurate estimate of the percentage effect is 100 ½expð:254Þ 1¼22:4%; see Problem 4.1(a).]

We can always use more than one proxy for xK . For example, it might be that Eðq j x; z1; z2Þ ¼ Eðq j z1; z2Þ ¼ y<sup>0</sup> þ y1z<sup>1</sup> þ y2z2, in which case including both z<sup>1</sup> and z<sup>2</sup> as regressors along with x1; ... ; xK solves the omitted variable problem. The weaker condition that the error r in the equation q ¼ y<sup>0</sup> þ y1z<sup>1</sup> þ y2z<sup>2</sup> þ r is uncorrelated with x1; ... ; xK also suffices.

The data set NLS80.RAW also contains each man's score on the knowledge of the world of work (KWW ) test. Problem 4.11 asks you to reestimate equation (4.29) when KWW and IQ are both used as proxies for ability.

## 4.3.3 Models with Interactions in Unobservables

In some cases we might be concerned about interactions between unobservables and observable explanatory variables. Obtaining consistent estimators is more difficult in this case, but a good proxy variable can again solve the problem.

Write the structural model with unobservable q as

$$y = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + \gamma_1 q + \gamma_2 x_K q + v$$
 (4.30)

where we make a zero conditional mean assumption on the structural error v:

$$E(v \mid \mathbf{x}, q) = 0 \tag{4.31}$$

For simplicity we have interacted q with only one explanatory variable, xK .

Before discussing estimation of equation (4.30), we should have an interpretation for the parameters in this equation, as the interaction xK q is unobservable. (We discussed this topic more generally in Section 2.2.5.) If xK is an essentially continuous variable, the partial effect of xK on Eðy j x; qÞ is

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x}, q)}{\partial x_K} = \beta_K + \gamma_2 q \tag{4.32}$$

Thus, the partial effect of xK actually depends on the level of q. Because q is not observed for anyone in the population, equation (4.32) can never be estimated, even if we could estimate g<sup>2</sup> (which we cannot, in general). But we can average equation

{84}------------------------------------------------

(4.32) across the population distribution of q. Assuming EðqÞ ¼ 0, the average partial effect (APE ) of xK is

$$E(\beta_K + \gamma_2 q) = \beta_K \tag{4.33}$$

A similar interpretation holds for discrete xK . For example, if xK is binary, then Eðy j x1; ... ; xK<sup>1</sup>; 1; qÞ Eðy j x1; ... ; xK<sup>1</sup>; 0; qÞ ¼ b<sup>K</sup> þ g2q, and b<sup>K</sup> is the average of this difference over the distribution of q. In this case, b<sup>K</sup> is called the average treatment effect (ATE). This name derives from the case where xK represents receiving some ''treatment,'' such as participation in a job training program or participation in an income maintenence program. We will consider the binary treatment case further in Chapter 18, where we introduce a counterfactual framework for estimating average treatment effects.

It turns out that the assumption EðqÞ ¼ 0 is without loss of generality. Using simple algebra we can show that, if m<sup>q</sup> 1EðqÞ 00, then we can consistently estimate b<sup>K</sup> þ g2mq, which is the average partial effect.

If the elements of x are exogenous in the sense that Eðq j xÞ ¼ 0, then we can consistently estimate each of the b<sup>j</sup> by an OLS regression, where q and xK q are just part of the error term. This result follows from iterated expectations applied to equation (4.30), which shows that Eðy j xÞ ¼ b<sup>0</sup> þ b1x<sup>1</sup> þþ b<sup>K</sup> xK if Eðq j xÞ ¼ 0. The resulting equation probably has heteroskedasticity, but this is easily dealt with. Incidentally, this is a case where only assuming that q and x are uncorrelated would not be enough to ensure consistency of OLS: xK q and x can be correlated even if q and x are uncorrelated.

If q and x are correlated, we can consistently estimate the b<sup>j</sup> by OLS if we have a suitable proxy variable for q. We still assume that the proxy variable, z, satisfies the redundancy condition (4.25). In the current model we must make a stronger proxy variable assumption than we did in Section 4.3.2:

$$E(q \mid \mathbf{x}, z) = E(q \mid z) = \theta_1 z \tag{4.34}$$

where now we assume z has a zero mean in the population. Under these two proxy variable assumptions, iterated expectations gives

$$E(y | \mathbf{x}, z) = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + \gamma_1 \theta_1 z + \gamma_2 \theta_1 x_K z$$
(4.35)

and the parameters are consistently estimated by OLS.

If we do not define our proxy to have zero mean in the population, then estimating equation (4.35) by OLS does not consistently estimate b<sup>K</sup> . If EðzÞ 00, then we would have to write Eðq j zÞ ¼ y<sup>0</sup> þ y1z, in which case the coefficient on xK in equation (4.35) would be b<sup>K</sup> þ y0g2. In practice, we may not know the population mean of the 

{85}------------------------------------------------

proxy variable, in which case the proxy variable should be demeaned in the sample before interacting it with xK .

If we maintain homoskedasticity in the structural model—that is, Varðy j x; q; zÞ ¼ Varðy j x; qÞ ¼ s2—then there must be heteroskedasticity in Varðy j x; zÞ. Using Property CV.3 in Appendix 2A, it can be shown that

$$\operatorname{Var}(y \mid \mathbf{x}, z) = \sigma^2 + (\gamma_1 + \gamma_2 x_K)^2 \operatorname{Var}(q \mid \mathbf{x}, z)$$

Even if Varðq j x; zÞ is constant, Varðy j x; zÞ depends on xK . This situation is most easily dealt with by computing heteroskedasticity-robust statistics, which allows for heteroskedasticity of arbitrary form.

Example 4.5 (Return to Education Depends on Ability): Consider an extension of the wage equation (4.29):

$$\log(wage) = \beta_0 + \beta_1 exper + \beta_2 tenure + \beta_3 married + \beta_4 south$$
$$+ \beta_5 urban + \beta_6 black + \beta_7 educ + \gamma_1 abil + \gamma_2 educ \cdot abil + v$$
(4.36)

so that educ and abil have separate effects but also have an interactive effect. In this model the return to a year of schooling depends on abil: b<sup>7</sup> þ g2abil. Normalizing abil to have zero population mean, we see that the average of the return to education is simply b7. We estimate this equation under the assumption that IQ is redundant in equation (4.36) and Eðabil j x;IQÞ ¼ Eðabil jIQÞ ¼ y1ðIQ 100Þ 1 y1IQ0, where IQ<sup>0</sup> is the population-demeaned IQ (IQ is constructed to have mean 100 in the population). We can estimate the b<sup>j</sup> in equation (4.36) by replacing abil with IQ<sup>0</sup> and educabil with educIQ<sup>0</sup> and doing OLS.

Using the sample of men in NLS80.RAW gives the following:

$$\log(\hat{w}age) = \dots + .052 \ educ - .00094 \ IQ_0 + .00034 \ educ \cdot IQ_0$$

$$(.007) \qquad (.00516) \qquad (.00038)$$

$$N = 935, \qquad R^2 = .263$$

where the usual OLS standard errors are reported (if g<sup>2</sup> ¼ 0, homoskedasticity may be reasonable). The interaction term educIQ<sup>0</sup> is not statistically significant, and the return to education at the average IQ, 5.2 percent, is similar to the estimate when the return to education is assumed to be constant. Thus there is little evidence for an interaction between education and ability. Incidentally, the F test for joint significance of IQ<sup>0</sup> and educIQ<sup>0</sup> yields a p-value of about .0011, but the interaction term is not needed.

{86}------------------------------------------------

In this case, we happen to know the population mean of IQ, but in most cases we will not know the population mean of a proxy variable. Then, we should use the sample average to demean the proxy before interacting it with xK ; see Problem 4.8. Technically, using the sample average to estimate the population average should be reflected in the OLS standard errors. But, as you are asked to show in Problem 6.10 in Chapter 6, the adjustments generally have very small impacts on the standard errors and can safely be ignored.

In his study on the effects of computer usage on the wage structure in the United States, Krueger (1993) uses computer usage at home as a proxy for unobservables that might be correlated with computer usage at work; he also includes an interaction between the two computer usage dummies. Krueger does not demean the ''uses computer at home'' dummy before constructing the interaction, so his estimate on ''uses a computer at work'' does not have an average treatment effect interpretation. However, just as in Example 4.5, Krueger found that the interaction term is insignificant.

## 4.4 Properties of OLS under Measurement Error

As we saw in Section 4.1, another way that endogenous explanatory variables can arise in economic applications occurs when one or more of the variables in our model contains measurement error. In this section, we derive the consequences of measurement error for ordinary least squares estimation.

The measurement error problem has a statistical structure similar to the omitted variable–proxy variable problem discussed in the previous section. However, they are conceptually very different. In the proxy variable case, we are looking for a variable that is somehow associated with the unobserved variable. In the measurement error case, the variable that we do not observe has a well-defined, quantitative meaning (such as a marginal tax rate or annual income), but our measures of it may contain error. For example, reported annual income is a measure of actual annual income, whereas IQ score is a proxy for ability.

Another important difference between the proxy variable and measurement error problems is that, in the latter case, often the mismeasured explanatory variable is the one whose effect is of primary interest. In the proxy variable case, we cannot estimate the effect of the omitted variable.

Before we turn to the analysis, it is important to remember that measurement error is an issue only when the variables on which we can collect data differ from the variables that influence decisions by individuals, families, firms, and so on. For example, 

{87}------------------------------------------------

suppose we are estimating the effect of peer group behavior on teenage drug usage, where the behavior of one's peer group is self-reported. Self-reporting may be a mismeasure of actual peer group behavior, but so what? We are probably more interested in the effects of how a teenager perceives his or her peer group.

## 4.4.1 Measurement Error in the Dependent Variable

We begin with the case where the dependent variable is the only variable measured with error. Let  $y^*$  denote the variable (in the population, as always) that we would like to explain. For example,  $y^*$  could be annual family saving. The regression model has the usual linear form

$$y^* = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + v \tag{4.37}$$

and we assume that it satisfies at least Assumptions OLS.1 and OLS.2. Typically, we are interested in  $E(y^* | x_1, ..., x_K)$ . We let y represent the observable measure of  $y^*$  where  $y \neq y^*$ .

The population measurement error is defined as the difference between the observed value and the actual value:

$$e_0 = y - y^* (4.38)$$

For a random draw *i* from the population, we can write  $e_{i0} = y_i - y_i^*$ , but what is important is how the measurement error in the population is related to other factors. To obtain an estimable model, we write  $y^* = y - e_0$ , plug this into equation (4.37), and rearrange:

$$y = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + v + e_0 \tag{4.39}$$

Since  $y, x_1, x_2, ..., x_K$  are observed, we can estimate this model by OLS. In effect, we just ignore the fact that y is an imperfect measure of  $y^*$  and proceed as usual.

When does OLS with y in place of  $y^*$  produce consistent estimators of the  $\beta_j$ ? Since the original model (4.37) satisfies Assumption OLS.1, v has zero mean and is uncorrelated with each  $x_j$ . It is only natural to assume that the measurement error has zero mean; if it does not, this fact only affects estimation of the intercept,  $\beta_0$ . Much more important is what we assume about the relationship between the measurement error  $e_0$  and the explanatory variables  $x_j$ . The usual assumption is that the measurement error in y is statistically independent of each explanatory variable, which implies that  $e_0$  is uncorrelated with  $\mathbf{x}$ . Then, the OLS estimators from equation (4.39) are consistent (and possibly unbiased as well). Further, the usual OLS inference procedures (t statistics, t statistics, t statistics) are asymptotically valid under appropriate homoskedasticity assumptions.

{88}------------------------------------------------

If  $e_0$  and v are uncorrelated, as is usually assumed, then  $Var(v+e_0) = \sigma_v^2 + \sigma_0^2 > \sigma_v^2$ . Therefore, measurement error in the dependent variable results in a larger error variance than when the dependent variable is not measured with error. This result is hardly surprising and translates into larger asymptotic variances for the OLS estimators than if we could observe  $y^*$ . But the larger error variance violates none of the assumptions needed for OLS estimation to have its desirable large-sample properties.

Example 4.6 (Saving Function with Measurement Error): Consider a saving function

$$E(sav^* | inc, size, educ, age) = \beta_0 + \beta_1 inc + \beta_2 size + \beta_3 educ + \beta_4 age$$

but where actual saving ( $sav^*$ ) may deviate from reported saving (sav). The question is whether the size of the measurement error in sav is systematically related to the other variables. It may be reasonable to assume that the measurement error is not correlated with inc, size, educ, and age, but we might expect that families with higher incomes, or more education, report their saving more accurately. Unfortunately, without more information, we cannot know whether the measurement error is correlated with inc or educ.

When the dependent variable is in logarithmic form, so that  $log(y^*)$  is the dependent variable, a natural measurement error equation is

$$\log(y) = \log(y^*) + e_0 \tag{4.40}$$

This follows from a **multiplicative measurement error** for y:  $y = y^*a_0$  where  $a_0 > 0$  and  $e_0 = \log(a_0)$ .

Example 4.7 (Measurement Error in Firm Scrap Rates): In Example 4.4, we might think that the firm scrap rate is mismeasured, leading us to postulate the model  $\log(scrap^*) = \beta_0 + \beta_1 grant + v$ , where  $scrap^*$  is the true scrap rate. The measurement error equation is  $\log(scrap) = \log(scrap^*) + e_0$ . Is the measurement error  $e_0$  independent of whether the firm receives a grant? Not if a firm receiving a grant is more likely to underreport its scrap rate in order to make it look as if the grant had the intended effect. If underreporting occurs, then, in the estimable equation  $\log(scrap) = \beta_0 + \beta_1 grant + v + e_0$ , the error  $u = v + e_0$  is negatively correlated with grant. This result would produce a downward bias in  $\beta_1$ , tending to make the training program look more effective than it actually was.

These examples show that measurement error in the dependent variable *can* cause biases in OLS if the measurement error is systematically related to one or more of the explanatory variables. If the measurement error is uncorrelated with the explanatory variables, OLS is perfectly appropriate.

{89}------------------------------------------------

## 4.4.2 Measurement Error in an Explanatory Variable

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