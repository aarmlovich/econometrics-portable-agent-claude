# Specifying Models of Conditional Expectations with Unobserved Effects

> Pages: 677-678

We now turn to models that explicitly contain an unobserved effect. The issues that arise here are similar to those that arose in linear panel data models. First, we must know whether the explanatory variables are strictly exogenous conditional on an unobserved effect. Second, we must decide how the unobserved effect should appear in the conditional mean.

{678}------------------------------------------------

Given conditioning variables xt, strict exogeneity conditional on the unobserved effect c is defined just as in the linear case:

$$E(y_t | \mathbf{x}_1, \dots, \mathbf{x}_T, c) = E(y_t | \mathbf{x}_t, c)$$

$$(19.53)$$

As always, this definition rules out lagged values of y in xt, and it can rule out feedback from yt to future explanatory variables. In static models, where x<sup>t</sup> ¼ z<sup>t</sup> for variables z<sup>t</sup> dated contemporaneously with yt, assumption (19.53) implies that neither past nor future values of z affect the expected value of yt, once z<sup>t</sup> and c have been controlled for. This can be too restrictive, but it is often the starting point for analyzing static models.

A finite distributed lag relationship assumes that

$$E(y_t | \mathbf{z}_t, \mathbf{z}_{t-1}, \dots, \mathbf{z}_1, c) = E(y_t | \mathbf{z}_t, \mathbf{z}_{t-1}, \dots, \mathbf{z}_{t-Q}, c), \qquad t > Q$$

$$(19.54)$$

where Q is the length of the distributed lag. Under assumption (19.54), the strict exogeneity assumption conditional on c becomes

$$E(y_t | \mathbf{z}_1, \mathbf{z}_2, \dots, \mathbf{z}_T, c) = E(y_t | \mathbf{z}_1, \dots, \mathbf{z}_t, c)$$
(19.55)

which is less restrictive than in the purely static model because lags of z<sup>t</sup> explicitly appear in the model; it still rules out general feedback from yt to ðztþ<sup>1</sup>; ... ; zTÞ.

With count variables, a multiplicative unobserved effect is an attractive functional form:

$$E(y_t | \mathbf{x}_t, c) = c \cdot m(\mathbf{x}_t, \boldsymbol{\beta}_0)$$
(19.56)

where mðxt; *b*Þ is a parametric function known up to the P 1 vector of parameters *b*o. Equation (19.56) implies that the partial effect of xtj on log Eðyt j xt; cÞ does not depend on the unobserved effect c. Thus quantities such as elasticities and semielasticities depend only on x<sup>t</sup> and *b*o. The most popular special case is the exponential model Eðyt j xt; aÞ ¼ expða þ xt*b*Þ, which is obtained by taking c ¼ expðaÞ.