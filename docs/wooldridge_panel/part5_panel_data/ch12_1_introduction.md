# Introduction

> Pages: 352-356

We begin our study of nonlinear estimation with a general class of estimators known as M-estimators, a term introduced by Huber (1967). (You might think of the ''M'' as standing for minimization or maximization.) M-estimation methods include maximum likelihood, nonlinear least squares, least absolute deviations, quasi-maximum likelihood, and many other procedures used by econometricians.

This chapter is somewhat abstract and technical, but it is useful to develop a unified theory early on so that it can be applied in a variety of situations. We will carry along the example of nonlinear least squares for cross section data to motivate the general approach.

In a nonlinear regression model, we have a random variable, y, and we would like to model Eðy j xÞ as a function of the explanatory variables x, a K-vector. We already know how to estimate models of Eðy j xÞ when the model is linear in its parameters: OLS produces consistent, asymptotically normal estimators. What happens if the regression function is nonlinear in its parameters?

Generally, let mðx; *y*Þ be a parametric model for Eðy j xÞ, where m is a known function of x and *y*, and *y* is a P 1 parameter vector. [This is a parametric model because mð- ; *y*Þ is assumed to be known up to a finite number of parameters.] The dimension of the parameters, P, can be less than or greater than K. The parameter space, Y, is a subset of RP. This is the set of values of *y* that we are willing to consider in the regression function. Unlike in linear models, for nonlinear models the asymptotic analysis requires explicit assumptions on the parameter space.

An example of a nonlinear regression function is the exponential regression function, mðx; *y*Þ ¼ expðx*y*Þ, where x is a row vector and contains unity as its first element. This is a useful functional form whenever y b0. A regression model suitable when the response y is restricted to the unit interval is the logistic function, mðx; *y*Þ ¼ expðx*y*Þ=½1 þ expðx*y*Þ. Both the exponential and logistic functions are nonlinear in *y*.

In any application, there is no guarantee that our chosen model is adequate for Eðy j xÞ. We say that we have a correctly specified model for the conditional mean, Eðy j xÞ, if, for some *y*<sup>o</sup> A Y,

$$E(y \mid \mathbf{x}) = m(\mathbf{x}, \boldsymbol{\theta}_{o}) \tag{12.1}$$

We introduce the subscript ''o'' on theta to distinguish the parameter vector appearing in Eðy j xÞ from other candidates for that vector. (Often, the value *y*<sup>o</sup> is called ''the true value of theta,'' a phrase that is somewhat loose but still useful as shorthand.) As an example, for yb 0 and a single explanatory variable x, consider the model mðx; *y*Þ ¼ y1x<sup>y</sup><sup>2</sup> . If the population regression function is Eðy j xÞ ¼ 4x<sup>1</sup>:5, then

{353}------------------------------------------------

yo1 ¼ 4 and yo2 ¼ 1:5. We will never know the actual yo1 and yo2 (unless we somehow control the way the data have been generated), but, if the model is correctly specified, then these values exist, and we would like to estimate them. Generic candidates for yo1 and yo2 are labeled y<sup>1</sup> and y2, and, without further information, y<sup>1</sup> is any positive number and y<sup>2</sup> is any real number: the parameter space is Y 1 fðy1; y2Þ: y<sup>1</sup> > 0; y<sup>2</sup> A Rg. For an exponential regression model, mðx; *y*Þ ¼ expðx*y*Þ is a correctly specified model for Eðy j xÞ if and only if there is some K-vector *y*<sup>o</sup> such that Eðy j xÞ ¼ expðx*y*oÞ.

In our analysis of linear models, there was no need to make the distinction between the parameter vector in the population regression function and other candidates for this vector, because the estimators in linear contexts are obtained in closed form, and so their asymptotic properties can be studied directly. As we will see, in our theoretical development we need to distinguish the vector appearing in Eðy j xÞ from a generic element of Y. We will often drop the subscripting by ''o'' when studying particular applications because the notation can be cumbersome.

Equation (12.1) is the most general way of thinking about what nonlinear least squares is intended to do: estimate models of conditional expectations. But, as a statistical matter, equation (12.1) is equivalent to a model with an additive, unobservable error with a zero conditional mean:

$$y = m(\mathbf{x}, \boldsymbol{\theta}_{o}) + u, \qquad \mathbf{E}(u \mid \mathbf{x}) = 0$$
 (12.2)

Given equation (12.2), equation (12.1) clearly holds. Conversely, given equation (12.1), we obtain equation (12.2) by defining the error to be u1 y mðx; *y*oÞ. In interpreting the model and deciding on appropriate estimation methods, we should not focus on the error form in equation (12.2) because, evidently, the additivity of u has some unintended connotations. In particular, we must remember that, in writing the model in error form, the only thing implied by equation (12.1) is Eðu j xÞ ¼ 0. Depending on the nature of y, the error u may have some unusual properties. For example, if yb 0 then ub mðx; *y*oÞ, in which case u and x cannot be independent. Heteroskedasticity in the error—that is, Varðu j xÞ 0VarðuÞ—is present whenever Varðy j xÞ depends on x, as is very common when y takes on a restricted range of values. Plus, when we introduce randomly sampled observations fðxi; yiÞ: i ¼ 1; 2; ... ; Ng, it is too tempting to write the model and its assumptions as ''yi ¼ mðxi; *y*oÞ þ ui where the ui are i.i.d. errors.'' As we discussed in Section 1.4 for the linear model, under random sampling the fuig are always i.i.d. What is usually meant is that ui and x<sup>i</sup> are independent, but, for the reasons we just gave, this assumption is often much too strong. The error form of the model does turn out to be useful for defining estimators of asymptotic variances and for obtaining test statistics.

{354}------------------------------------------------

For later reference, we formalize the first nonlinear least squares (NLS) assumption as follows:

ASSUMPTION NLS.1: For some 
$$\theta_0 \in \Theta$$
,  $E(y | \mathbf{x}) = m(\mathbf{x}, \theta_0)$ .

This form of presentation represents the level at which we will state assumptions for particular econometric methods. In our general development of M-estimators that follows, we will need to add conditions involving moments of mðx; *y*Þ and y, as well as continuity assumptions on mðx; -Þ.

If we let w1 ðx; yÞ, then *y*<sup>o</sup> indexes a feature of the population distribution of w, namely, the conditional mean of y given x. More generally, let w be an M-vector of random variables with some distribution in the population. We let W denote the subset of R<sup>M</sup> representing the possible values of w. Let *y*<sup>o</sup> denote a parameter vector describing some feature of the distribution of w. This could be a conditional mean, a conditional mean and conditional variance, a conditional median, or a conditional distribution. As shorthand, we call *y*<sup>o</sup> ''the true parameter'' or ''the true value of theta.'' These phrases simply mean that *y*<sup>o</sup> is the parameter vector describing the underlying population, something we will make precise later. We assume that *y*<sup>o</sup> belongs to a known parameter space Y HRP.

We assume that our data come as a random sample of size N from the population; we label this random sample fwi: i ¼ 1; 2; ...g, where each w<sup>i</sup> is an M-vector. This assumption is much more general than it may initially seem. It covers cross section models with many equations, and it also covers panel data settings with small time series dimension. The extension to independently pooled cross sections is almost immediate. In the NLS example, w<sup>i</sup> consists of x<sup>i</sup> and yi, the ith draw from the population on x and y.

What allows us to estimate *y*<sup>o</sup> when it indexes Eðy j xÞ? It is the fact that *y*<sup>o</sup> is the value of *y* that minimizes the expected squared error between y and mðx; *y*Þ. That is, *y*<sup>o</sup> solves the population problem

$$\min_{\boldsymbol{\theta} \in \mathbf{\Theta}} E\{ [y - m(\mathbf{x}, \boldsymbol{\theta})]^2 \}$$
 (12.3)

where the expectation is over the joint distribution of ðx; yÞ. This conclusion follows immediately from basic properties of conditional expectations (in particular, condition CE.8 in Chapter 2). We will give a slightly different argument here. Write

$$[y - m(\mathbf{x}, \boldsymbol{\theta})]^2 = [y - m(\mathbf{x}, \boldsymbol{\theta}_0)]^2 + 2[m(\mathbf{x}, \boldsymbol{\theta}_0) - m(\mathbf{x}, \boldsymbol{\theta})]u$$
$$+ [m(\mathbf{x}, \boldsymbol{\theta}_0) - m(\mathbf{x}, \boldsymbol{\theta})]^2$$
(12.4)

{355}------------------------------------------------

where u is defined in equation (12.2). Now, since Eðu j xÞ ¼ 0, u is uncorrelated with any function of x, including mðx; *y*oÞ mðx; *y*Þ. Thus, taking the expected value of equation (12.4) gives

$$E\{[y - m(\mathbf{x}, \boldsymbol{\theta})]^2\} = E\{[y - m(\mathbf{x}, \boldsymbol{\theta}_0)]^2\} + E\{[m(\mathbf{x}, \boldsymbol{\theta}_0) - m(\mathbf{x}, \boldsymbol{\theta})]^2\}$$
(12.5)

Since the last term in equation (12.5) is nonnegative, it follows that

$$E\{[y - m(\mathbf{x}, \boldsymbol{\theta})]^2\} \ge E\{[y - m(\mathbf{x}, \boldsymbol{\theta}_0)]^2\}, \quad \text{all } \boldsymbol{\theta} \in \boldsymbol{\Theta}$$
 (12.6)

The inequality is strict when *y* 0*y*<sup>o</sup> unless Ef½mðx; *y*oÞ mðx; *y*Þ<sup>2</sup> g ¼ 0; for *y*<sup>o</sup> to be identified, we will have to rule this possibility out.

Because *y*<sup>o</sup> solves the population problem in expression (12.3), the analogy principle—which we introduced in Chapter 4—suggests estimating *y*<sup>o</sup> by solving the sample analogue. In other words, we replace the population moment Ef½ðymðx; *y*Þ<sup>2</sup> g with the sample average. The nonlinear least squares (NLS) estimator of *y*o, ^*y*, solves

$$\min_{\theta \in \Theta} N^{-1} \sum_{i=1}^{N} [y_i - m(\mathbf{x}_i, \theta)]^2$$
 (12.7)

For now, we assume that a solution to this problem exists.

The NLS objective function in expression (12.7) is a special case of a more general class of estimators. Let qðw; *y*Þ be a function of the random vector w and the parameter vector *y*. An M-estimator of *y*<sup>o</sup> solves the problem

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} N^{-1} \sum_{i=1}^{N} q(\mathbf{w}_i, \boldsymbol{\theta})$$
 (12.8)

assuming that a solution, call it ^*y*, exists. The estimator clearly depends on the sample fwi: i ¼ 1; 2; ... ; Ng, but we suppress that fact in the notation.

The objective function for an M-estimator is a sample average of a function of w<sup>i</sup> and *y*. The division by N, while needed for the theoretical development, does not affect the minimization problem. Also, the focus on minimization, rather than maximization, is without loss of generality because maximiziation can be trivially turned into minimization.

The parameter vector *y*<sup>o</sup> is assumed to uniquely solve the population problem

$$\min_{\boldsymbol{\theta} \in \mathbf{\Theta}} \ \mathrm{E}[q(\mathbf{w}, \boldsymbol{\theta})] \tag{12.9}$$

Comparing equations (12.8) and (12.9), we see that M-estimators are based on the analogy principle. Once *y*<sup>o</sup> has been defined, finding an appropriate function q that

{356}------------------------------------------------

delivers  $\theta_0$  as the solution to problem (12.9) requires basic results from probability theory. Usually there is more than one choice of q such that  $\theta_0$  solves problem (12.9), in which case the choice depends on efficiency or computational issues. In this chapter we carry along the NLS example; we treat maximum likelihood estimation in Chapter 13.

How do we translate the fact that  $\theta_0$  solves the population problem (12.9) into consistency of the M-estimator  $\hat{\theta}$  that solves problem (12.8)? Heuristically, the argument is as follows. Since for each  $\theta \in \Theta$   $\{q(\mathbf{w}_i, \theta): i = 1, 2, ...\}$  is just an i.i.d. sequence, the law of large numbers implies that

$$N^{-1} \sum_{i=1}^{N} q(\mathbf{w}_i, \boldsymbol{\theta}) \stackrel{p}{\to} E[q(\mathbf{w}, \boldsymbol{\theta})]$$
 (12.10)

under very weak finite moment assumptions. Since  $\hat{\boldsymbol{\theta}}$  minimizes the function on the left side of equation (12.10) and  $\boldsymbol{\theta}_{o}$  minimizes the function on the right, it seems plausible that  $\hat{\boldsymbol{\theta}} \stackrel{p}{\rightarrow} \boldsymbol{\theta}_{o}$ . This informal argument turns out to be correct, except in pathological cases. There are essentially two issues to address. The first is identifiability of  $\boldsymbol{\theta}_{o}$ , which is purely a population issue. The second is the sense in which the convergence in equation (12.10) happens across different values of  $\boldsymbol{\theta}$  in  $\boldsymbol{\Theta}$ .