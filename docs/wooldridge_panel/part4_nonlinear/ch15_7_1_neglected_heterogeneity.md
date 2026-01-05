# Neglected Heterogeneity

> Pages: 479-481

We begin by studying the consequences of omitting variables when those omitted variables are independent of the included explanatory variables. This is also called the neglected heterogeneity problem. The (structural) model of interest is

$$P(y = 1 \mid \mathbf{x}, c) = \Phi(\mathbf{x}\boldsymbol{\beta} + \gamma c)$$
 (15.34)

where x is 1 K with x<sup>1</sup> 1 1 and c is a scalar. We are interested in the partial effects of the xj on the probability of success, holding c (and the other elements of x) fixed. We can write equation (15.34) in latent variable form as y ¼ x*b* þ gc þ e, where y ¼ 1½y > 0 and e j x; c @Normalð0; 1Þ. Because x<sup>1</sup> ¼ 1, EðcÞ ¼ 0 without loss of generality.

Now suppose that c is independent of x and c@ Normalð0; t<sup>2</sup>Þ. [Remember, this assumption is much stronger than Covðx; cÞ ¼ 0 or even Eðc j xÞ ¼ 0: under independence, the distribution of c given x does not depend on x.] Given these assumptions, the composite term, gc þ e, is independent of x and has a Normalð0; g<sup>2</sup>t<sup>2</sup> þ 1Þ distribution. Therefore,

$$P(y = 1 \mid \mathbf{x}) = P(\gamma c + e > -\mathbf{x}\boldsymbol{\beta} \mid \mathbf{x}) = \Phi(\mathbf{x}\boldsymbol{\beta}/\sigma)$$
(15.35)

where s<sup>2</sup> 1g<sup>2</sup>t<sup>2</sup> þ 1. It follows immediately from equation (15.35) that probit of y on x consistently estimates *b*=s. In other words, if ^*b* is the estimator from a probit of <sup>y</sup> on <sup>x</sup>, then plim ^b<sup>j</sup> <sup>¼</sup> <sup>b</sup>j=s. Because <sup>s</sup> ¼ ðg<sup>2</sup>t<sup>2</sup> <sup>þ</sup> <sup>1</sup><sup>Þ</sup> <sup>1</sup>=<sup>2</sup> > 1 (unless g ¼ 0 or t<sup>2</sup> ¼ 0Þ, jbj=sj < jbjj.

The attenuation bias in estimating b<sup>j</sup> in the presence of neglected heterogeneity has prompted statements of the following kind: ''In probit analysis, neglected heterogeneity is a much more serious problem than in linear models because, even if the omitted heterogeneity is independent of x, the probit coefficients are inconsistent.'' We just derived that probit of y on x consistently estimates *b*=s rather than *b*, so the statement is technically correct. However, we should remember that, in nonlinear models, we usually want to estimate partial effects and not just parameters. For the purposes of obtaining the directions of the effects or the relative effects of the explanatory variables, estimating *b*=s is just as good as estimating *b*.

{480}------------------------------------------------

For continuous xj, we would like to estimate

$$\partial \mathbf{P}(y=1 \mid \mathbf{x}, c) / \partial x_j = \beta_j \phi(\mathbf{x}\boldsymbol{\beta} + \gamma c)$$
(15.36)

for various values of x and c. Because c is not observed, we cannot estimate g. Even if we could estimate g, c almost never has meaningful units of measurement—for example, c might be ''ability,'' ''health,'' or ''taste for saving''—so it is not obvious what values of c we should plug into equation (15.36). Nevertheless, c is normalized so that EðcÞ ¼ 0, so we may be interested in equation (15.36) evaluated at c ¼ 0, which is simply bjfðx*b*Þ. What we consistently estimate from the probit of y on x is

$$(\beta_j/\sigma)\phi(\mathbf{x}\boldsymbol{\beta}/\sigma) \tag{15.37}$$

This expression shows that, if we are interested in the partial effects evaluated at c ¼ 0, then probit of y on x does not do the trick. An interesting fact about expression (15.37) is that, even though bj=s is closer to zero than bj, fðx*b*=sÞ is larger than fðx*b*Þ because fðzÞ increases as jzj ! 0, and s > 1. Therefore, for estimating the partial effects in equation (15.36) at c ¼ 0, it is not clear for what values of x an attenuation bias exists.

With c having a normal distribution in the population, the partial effect evaluated at c ¼ 0 describes only a small fraction of the population. [Technically, Pðc ¼ 0Þ ¼ 0.] Instead, we can estimate the average partial effect (APE), which we introduced in Section 2.2.5. The APE is obtained, for given x, by averaging equation (15.36) across the distribution of c in the population. For emphasis, let x<sup>o</sup> be a given value of the explanatory variables (which could be, but need not be, the mean value). When we plug x<sup>o</sup> into equation (15.36) and take the expected value with respect to the distribution of c, we get

$$E[\beta_j \phi(\mathbf{x}^{\circ} \boldsymbol{\beta} + \gamma c)] = (\beta_j / \sigma) \phi(\mathbf{x}^{\circ} \boldsymbol{\beta} / \sigma)$$
(15.38)

In other words, probit of y on x consistently estimates the average partial effects, which is usually what we want.

The result in equation (15.38) follows from the general treatment of average partial effects in Section 2.2.5. In the current setup, there are no extra conditioning variables, w, and the unobserved heterogeneity is independent of x. It follows from equation (2.35) that the APE with respect to xj, evaluated at xo, is simply qEðy j x<sup>o</sup>Þ=qxj. But from the law of iterated expectations, Eðy j xÞ ¼ Ec½Fðx*b* þ gcÞ- ¼ Fðx*b*=sÞ, where EcðÞ denotes the expectation with respect to the distribution of c. The derivative of Fðx*b*=sÞ with respect to xj is ðbj=sÞfðx*b*=sÞ, which is what we wanted to show.

The bottom line is that, except in cases where the magnitudes of the b<sup>j</sup> in equation (15.34) have some meaning, omitted heterogeneity in probit models is not a problem


{481}------------------------------------------------

when it is independent of x: ignoring it consistently estimates the average partial effects. Of course, the previous arguments hinge on the normality of c and the probit structural equation. If the structural model (15.34) were, say, logit and if c were normally distributed, we would not get a probit or logit for the distribution of y given x; the response probability is more complicated. The lesson from Section 2.2.5 is that we might as well work directly with models for Pðy ¼ 1 j xÞ because partial effects of Pðy ¼ 1 j xÞ are always the average of the partial effects of Pðy ¼ 1 j x; cÞ over the distribution of c.

If c is correlated with x or is otherwise dependent on x [for example, if Varðc j xÞ depends on x], then omission of c is serious. In this case we cannot get consistent estimates of the average partial effects. For example, if c j x @Normalðx*d*; h<sup>2</sup>Þ, then probit of y on x gives consistent estimates of ð*b* þ g*d*Þ=r, where r<sup>2</sup> ¼ g<sup>2</sup>h<sup>2</sup> þ 1. Unless g ¼ 0 or *d* ¼ 0, we do not consistently estimate *b*=s. This result is not surprising given what we know from the linear case with omitted variables correlated with the xj. We now study what can be done to account for endogenous variables in probit models.