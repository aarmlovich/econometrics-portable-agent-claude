# Binary Response Model with Sample Selection

> Pages: 578-579

We can estimate binary response models with sample selection if we assume that the latent errors are bivariate normal and independent of the explanatory variables. Write the model as

$$y_1 = 1[\mathbf{x}_1 \boldsymbol{\beta}_1 + u_1 > 0] \tag{17.30}$$

$$y_2 = 1[\mathbf{x}\delta_2 + v_2 > 0] \tag{17.31}$$

where the second equation is the sample selection equation and y<sup>1</sup> is observed only when y<sup>2</sup> ¼ 1; we assume that x is always observed. For example, suppose y<sup>1</sup> is an employment indicator and x<sup>1</sup> contains a job training binary indicator (which we assume is exogenous), as well as other human capital and family background variables. We might lose track of some people who are eligible to participate in the program; this is an example of sample attrition. If attrition is systematically related to u1, estimating equation (17.30) on the sample at hand can result in an inconsistent estimator of *b*1.

If we assume that ðu1; v2Þ is independent of x with a zero-mean normal distribution (and unit variances), we can apply partial maximum likelihood. What we need is the density of y<sup>1</sup> conditional on x and y<sup>2</sup> ¼ 1. We have essentially found this density in Chapter 15: in equation (15.55) set a<sup>1</sup> ¼ 0, replace z with x, and replace *d*<sup>1</sup> with *b*1. The parameter r<sup>1</sup> is still the correlation between u<sup>1</sup> and v2. A two-step procedure can be applied: first, estimate *d*<sup>2</sup> by probit of y<sup>2</sup> on x. Then, estimate *b*<sup>1</sup> and r<sup>1</sup> in the second stage using equation (15.55) along with Pðy<sup>1</sup> ¼ 0 j x; y<sup>2</sup> ¼ 1Þ.

{579}------------------------------------------------

A convincing analysis requires at least one variable in  $\mathbf{x}$ —that is, something that determines selection—that is not also in  $\mathbf{x}_1$ . Otherwise, identification is off of the nonlinearities in the probit models.

Allowing for endogenous explanatory variables in equation (17.30) along with sample selection is difficult, and it could be the focus of future research.