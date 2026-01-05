# Poisson Regression Models with Cross Section Data

> Pages: 653-655

In Chapter 13 we used the basic Poisson regression model to illustrate maximum likelihood estimation. Here, we study Poisson regression in much more detail, emphasizing the properties of the estimator when the Poisson distributional assumption is incorrect.

# 19.2.1 Assumptions Used for Poisson Regression

The basic Poisson regression model assumes that y given x 1ðx1; ... ; xK Þ has a Poisson distribution, as in El Sayyad (1973) and Maddala (1983, Section 2.15). The density of y given x under the Poisson assumption is completely determined by the conditional mean mðxÞ 1Eðy j xÞ:

$$f(y | \mathbf{x}) = \exp[-\mu(\mathbf{x})][\mu(\mathbf{x})]^y / y!, \qquad y = 0, 1, \dots$$
 (19.1)

where y! is y factorial. Given a parametric model for mðxÞ [such as mðxÞ ¼ expðx*b*Þ] and a random sample fðxi; yiÞ: i ¼ 1; 2; ... ; Ng on ðx; yÞ, it is fairly straightforward to obtain the conditional MLEs of the parameters. The statistical properties then follow from our treatment of CMLE in Chapter 13.

It has long been recognized that the Poisson distributional assumption imposes restrictions on the conditional moments of y that are often violated in applications. The most important of these is equality of the conditional variance and mean:

$$Var(y \mid \mathbf{x}) = E(y \mid \mathbf{x}) \tag{19.2}$$

The variance-mean equality has been rejected in numerous applications, and later we show that assumption (19.2) is violated for fairly simple departures from the Poisson 

{654}------------------------------------------------

model. Importantly, whether or not assumption (19.2) holds has implications for how we carry out statistical inference. In fact, as we will see, it is assumption (19.2), not the Poisson assumption per se, that is important for large-sample inference; this point will become clear in Section 19.2.2. In what follows we refer to assumption (19.2) as the Poisson variance assumption.

A weaker assumption allows the variance-mean ratio to be any positive constant:

$$Var(y \mid \mathbf{x}) = \sigma^2 E(y \mid \mathbf{x})$$
(19.3)

where s<sup>2</sup> > 0 is the variance-mean ratio. This assumption is used in the generalized linear models (GLM) literature, and so we will refer to assumption (19.3) as the Poisson GLM variance assumption. The GLM literature is concerned with quasimaximum likelihood estimation of a class of nonlinear models that contains Poisson regression as a special case. We do not need to introduce the full GLM apparatus and terminology to analyze Poisson regression. See McCullagh and Nelder (1989).

The case s<sup>2</sup> > 1 is empirically relevant because it implies that the variance is greater than the mean; this situation is called overdispersion (relative to the Poisson case). One distribution for y given x where assumption (19.3) holds with overdispersion is what Cameron and Trivedi (1986) call NegBin I—a particular parameterization of the negative binomial distribution. When s<sup>2</sup> < 1 we say there is underdispersion. Underdispersion is less common than overdispersion, but underdispersion has been found in some applications.

There are plenty of count distributions for which assumption (19.3) does not hold—for example, the NegBin II model in Cameron and Trivedi (1986). Therefore, we are often interested in estimating the conditional mean parameters without specifying the conditional variance. As we will see, Poisson regression turns out to be well suited for this purpose.

Given a parametric model mðx; *b*Þ for mðxÞ, where *b* is a P 1 vector of parameters, the log likelihood for observation i is

$$\ell_i(\boldsymbol{\beta}) = y_i \log[m(\mathbf{x}_i, \boldsymbol{\beta})] - m(\mathbf{x}_i, \boldsymbol{\beta})$$
(19.4)

where we drop the term logðyi!Þ because it does not depend on the parameters *b* (for computational reasons dropping this term is a good idea in practice, too, as yi! gets very large for even moderate yi). We let B H R<sup>P</sup> denote the parameter space, which is needed for the theoretical development but is practically unimportant in most cases.

The most common mean function in applications is the exponential:

$$m(\mathbf{x}, \boldsymbol{\beta}) = \exp(\mathbf{x}\boldsymbol{\beta}) \tag{19.5}$$

{655}------------------------------------------------

where x is 1 K and contains unity as its first element, and *b* is K 1. Under assumption (19.5) the log likelihood is lið*b*Þ ¼ yixi*b* expðxi*b*Þ. The parameters in model (19.5) are easy to interpret. If xj is continuous, then

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_j} = \exp(\mathbf{x}\boldsymbol{\beta})\beta_j$$

and so

$$\beta_j = \frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_j} \cdot \frac{1}{\mathbf{E}(y \mid \mathbf{x})} = \frac{\partial \log[\mathbf{E}(y \mid \mathbf{x})]}{\partial x_j}$$

Therefore, 100b<sup>j</sup> is the semielasticity of Eðy j xÞ with respect to xj: for small changes Dxj, the percentage change in Eðy j xÞ is roughly ð100bjÞDxj. If we replace xj with logðxjÞ, b<sup>j</sup> is the elasticity of Eðy j xÞ with respect to xj. Using assumption (19.5) as the model for Eðy j xÞ is analogous to using logðyÞ as the dependent variable in linear regression analysis.

Quadratic terms can be added with no additional effort, except in interpreting the parameters. In what follows, we will write the exponential function as in assumption (19.5), leaving transformations of x—such as logs, quadratics, interaction terms, and so on—implicit. See Wooldridge (1997c) for a discussion of other functional forms.