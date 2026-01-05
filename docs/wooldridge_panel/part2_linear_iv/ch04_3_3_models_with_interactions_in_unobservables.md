# Models with Interactions in Unobservables

> Pages: 83-86

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