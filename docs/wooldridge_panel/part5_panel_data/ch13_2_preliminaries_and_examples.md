# Preliminaries and Examples

> Pages: 397-400

Traditional maximum likelihood theory for independent, identically distributed observations fy<sup>i</sup> A RG: i ¼ 1; 2; ...g starts by specifying a family of densities for yi. This is the framework used in introductory statistics courses, where y<sup>i</sup> is a scalar with a normal or Poisson distribution. But in almost all economic applications, we are interested in estimating parameters in conditional distributions. Therefore, we assume that each random draw is partitioned as ðxi; yiÞ, where x<sup>i</sup> A R<sup>K</sup> and y<sup>i</sup> A RG, and we are interested in estimating a model for the conditional distribution of y<sup>i</sup> given xi. We are not interested in the distribution of xi, so we will not specify a model for it. Consequently, the method of this chapter is properly called conditional maximum likelihood estimation (CMLE). By taking x<sup>i</sup> to be null we cover unconditional MLE as a special case.

An alternative to viewing ðxi; yiÞ as a random draw from the population is to treat the conditioning variables x<sup>i</sup> as nonrandom vectors that are set ahead of time and that appear in the unconditional distribution of yi. (This is analogous to the fixed regressor assumption in classical regression analysis.) Then, the y<sup>i</sup> cannot be identically distributed, and this fact complicates the asymptotic analysis. More importantly, 

{398}------------------------------------------------

treating the  $\mathbf{x}_i$  as nonrandom is much too restrictive for all uses of maximum likelihood. In fact, later on we will cover methods where  $\mathbf{x}_i$  contains what are endogenous variables in a structural model, but where it is convenient to obtain the distribution of one set of endogenous variables conditional on another set. Once we know how to analyze the general CMLE case, applications follow fairly directly.

It is important to understand that the subsequent results apply any time we have random sampling in the cross section dimension. Thus, the general theory applies to system estimation, as in Chapters 7 and 9, provided we are willing to assume a distribution for  $\mathbf{y}_i$  given  $\mathbf{x}_i$ . In addition, panel data settings with large cross sections and relatively small time periods are encompassed, since the appropriate asymptotic analysis is with the time dimension fixed and the cross section dimension tending to infinity.

In order to perform maximum likelihood analysis we need to specify, or derive from an underlying (structural) model, the density of  $\mathbf{y}_i$  given  $\mathbf{x}_i$ . We assume this density is known up to a finite number of unknown parameters, with the result that we have a **parametric model** of a conditional density. The vector  $\mathbf{y}_i$  can be continuous or discrete, or it can have both discrete and continuous characteristics. In many of our applications,  $\mathbf{y}_i$  is a scalar, but this fact does not simplify the general treatment.

We will carry along two examples in this chapter to illustrate the general theory of conditional maximum likelihood. The first example is a **binary response model**, specifically the **probit model**. We postpone the uses and interepretation of binary response models until Chapter 15.

Example 13.1 (Probit): Suppose that the latent variable  $y_i^*$  follows

$$y_i^* = \mathbf{x}_i \boldsymbol{\theta} + e_i \tag{13.1}$$

where  $e_i$  is *independent* of  $\mathbf{x}_i$  (which is a  $1 \times K$  vector with first element equal to unity for all i),  $\boldsymbol{\theta}$  is a  $K \times 1$  vector of parameters, and  $e_i \sim \text{Normal}(0,1)$ . Instead of observing  $y_i^*$  we observe only a binary variable indicating the sign of  $y_i^*$ :

$$y_i = \begin{cases} 1 & \text{if } y_i^* > 0 \\ 0 & \text{if } y_i^* \le 0 \end{cases}$$
 (13.2)  
(13.3)

To be succinct, it is useful to write equations (13.2) and (13.3) in terms of the **indicator function**, denoted  $1[\cdot]$ . This function is unity whenever the statement in brackets is true, and zero otherwise. Thus, equations (13.2) and (13.3) are equivalently written as  $y_i = 1[y_i^* > 0]$ . Because  $e_i$  is normally distributed, it is irrelevant whether the strict inequality is in equation (13.2) or (13.3).

{399}------------------------------------------------

We can easily obtain the distribution of  $y_i$  given  $\mathbf{x}_i$ :

$$P(y_i = 1 \mid \mathbf{x}_i) = P(y_i^* > 0 \mid \mathbf{x}_i) = P(\mathbf{x}_i \boldsymbol{\theta} + e_i > 0 \mid \mathbf{x}_i)$$

$$= P(e_i > -\mathbf{x}_i \boldsymbol{\theta} \mid \mathbf{x}_i) = 1 - \Phi(-\mathbf{x}_i \boldsymbol{\theta}) = \Phi(\mathbf{x}_i \boldsymbol{\theta})$$
(13.4)

where  $\Phi(\cdot)$  denotes the standard normal cumulative distribution function (cdf). We have used Property CD.4 in the chapter appendix along with the symmetry of the normal distribution. Therefore,

$$\mathbf{P}(y_i = 0 \mid \mathbf{x}_i) = 1 - \Phi(\mathbf{x}_i \boldsymbol{\theta}) \tag{13.5}$$

We can combine equations (13.4) and (13.5) into the density of  $y_i$  given  $\mathbf{x}_i$ :

$$f(y \mid \mathbf{x}_i) = [\Phi(\mathbf{x}_i \boldsymbol{\theta})]^y [1 - \Phi(\mathbf{x}_i \boldsymbol{\theta})]^{1-y}, \qquad y = 0, 1$$
(13.6)

The fact that  $f(y | \mathbf{x}_i)$  is zero when  $y \notin \{0, 1\}$  is obvious, so we will not be explicit about this in the future.

Our second example is useful when the variable to be explained takes on non-negative integer values. Such a variable is called a **count variable**. We will discuss the use and interpretation of count data models in Chapter 19. For now, it suffices to note that a linear model for  $E(y | \mathbf{x})$  when y takes on nonnegative integer values is not ideal because it can lead to negative predicted values. Further, since y can take on the value zero with positive probability, the transformation  $\log(y)$  cannot be used to obtain a model with constant elasticities or constant semielasticities. A functional form well suited for  $E(y | \mathbf{x})$  is  $\exp(\mathbf{x}\boldsymbol{\theta})$ . We could estimate  $\boldsymbol{\theta}$  by using nonlinear least squares, but all of the standard distributions for count variables imply heteroskedasticity (see Chapter 19). Thus, we can hope to do better. A traditional approach to regression models with count data is to assume that  $y_i$  given  $\mathbf{x}_i$  has a Poisson distribution.

Example 13.2 (Poisson Regression): Let  $y_i$  be a nonnegative count variable; that is,  $y_i$  can take on integer values  $0, 1, 2, \ldots$  Denote the conditional mean of  $y_i$  given the vector  $\mathbf{x}_i$  as  $\mathrm{E}(y_i | \mathbf{x}_i) = \mu(\mathbf{x}_i)$ . A natural distribution for  $y_i$  given  $\mathbf{x}_i$  is the Poisson distribution:

$$f(y | \mathbf{x}_i) = \exp[-\mu(\mathbf{x}_i)] \{\mu(\mathbf{x}_i)\}^y / y!, \qquad y = 0, 1, 2, \dots$$
 (13.7)

(We use y as the dummy argument in the density, not to be confused with the random variable  $y_i$ .) Once we choose a form for the conditional mean function, we have completely determined the distribution of  $y_i$  given  $\mathbf{x}_i$ . For example, from equation (13.7),  $P(y_i = 0 | \mathbf{x}_i) = \exp[-\mu(\mathbf{x}_i)]$ . An important feature of the Poisson distribu-

{400}------------------------------------------------

tion is that the variance equals the mean:  $\operatorname{Var}(y_i | \mathbf{x}_i) = \operatorname{E}(y_i | \mathbf{x}_i) = \mu(\mathbf{x}_i)$ . The usual choice for  $\mu(\cdot)$  is  $\mu(\mathbf{x}) = \exp(\mathbf{x}\boldsymbol{\theta})$ , where  $\boldsymbol{\theta}$  is  $K \times 1$  and  $\mathbf{x}$  is  $1 \times K$  with first element unity.