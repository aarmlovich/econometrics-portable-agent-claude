# Overview of the Single-Equation Linear Model

> Pages: 65-68

This and the next couple of chapters cover what is still the workhorse in empirical economics: the single-equation linear model. Though you are assumed to be comfortable with ordinary least squares (OLS) estimation, we begin with OLS for a couple of reasons. First, it provides a bridge between more traditional approaches to econometrics—which treats explanatory variables as fixed—and the current approach, which is based on random sampling with stochastic explanatory variables. Second, we cover some topics that receive at best cursory treatment in first-semester texts. These topics, such as proxy variable solutions to the omitted variable problem, arise often in applied work.

The population model we study is linear in its parameters,

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + u \tag{4.1}$$

where y; x1; x2; x3; ... ; xK are observable random scalars (that is, we can observe them in a random sample of the population), u is the unobservable random disturbance or error, and b0; b1; b2; ... ; b<sup>K</sup> are the parameters (constants) we would like to estimate.

The error form of the model in equation (4.1) is useful for presenting a unified treatment of the statistical properties of various econometric procedures. Nevertheless, the steps one uses for getting to equation (4.1) are just as important. Goldberger (1972) defines a structural model as one representing a causal relationship, as opposed to a relationship that simply captures statistical associations. A structural equation can be obtained from an economic model, or it can be obtained through informal reasoning. Sometimes the structural model is directly estimable. Other times we must combine auxiliary assumptions about other variables with algebraic manipulations to arrive at an estimable model. In addition, we will often have reasons to estimate nonstructural equations, sometimes as a precursor to estimating a structural equation.

The error term u can consist of a variety of things, including omitted variables and measurement error (we will see some examples shortly). The parameters b<sup>j</sup> hopefully correspond to the parameters of interest, that is, the parameters in an underlying structural model. Whether this is the case depends on the application and the assumptions made.

As we will see in Section 4.2, the key condition needed for OLS to consistently estimate the b<sup>j</sup> (assuming we have available a random sample from the population) is that the error (in the population) has mean zero and is uncorrelated with each of the regressors:

$$E(u) = 0,$$
  $Cov(x_j, u) = 0,$   $j = 1, 2, ..., K$  (4.2)

{66}------------------------------------------------

The zero-mean assumption is for free when an intercept is included, and we will restrict attention to that case in what follows. It is the zero covariance of u with each xj that is important. From Chapter 2 we know that equation (4.1) and assumption (4.2) are equivalent to defining the linear projection of y onto ð1; x1; x2; ... ; xK Þ as b<sup>0</sup> þ b1x<sup>1</sup> þ b2x<sup>2</sup> þþ b<sup>K</sup> xK .

Sufficient for assumption (4.2) is the zero conditional mean assumption

$$E(u | x_1, x_2, \dots, x_K) = E(u | \mathbf{x}) = 0$$
(4.3)

Under equation (4.1) and assumption (4.3) we have the population regression function

$$E(y | x_1, x_2, \dots, x_K) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K$$
(4.4)

As we saw in Chapter 2, equation (4.4) includes the case where the xj are nonlinear functions of underlying explanatory variables, such as

$$\begin{split} \text{E}(\textit{savings} \,|\, \textit{income}, \textit{size}, \textit{age}, \textit{college}) &= \beta_0 + \beta_1 \, \log(\textit{income}) + \beta_2 \textit{size} + \beta_3 \textit{age} \\ &+ \beta_4 \textit{college} + \beta_5 \textit{college} \cdot \textit{age} \end{split}$$

We will study the asymptotic properties of OLS primarily under assumption (4.2), since it is weaker than assumption (4.3). As we discussed in Chapter 2, assumption (4.3) is natural when a structural model is directly estimable because it ensures that no additional functions of the explanatory variables help to explain y.

An explanatory variable xj is said to be endogenous in equation (4.1) if it is correlated with u. You should not rely too much on the meaning of ''endogenous'' from other branches of economics. In traditional usage, a variable is endogenous if it is determined within the context of a model. The usage in econometrics, while related to traditional definitions, is used broadly to describe any situation where an explanatory variable is correlated with the disturbance. If xj is uncorrelated with u, then xj is said to be exogenous in equation (4.1). If assumption (4.3) holds, then each explanatory variable is necessarily exogenous.

In applied econometrics, endogeneity usually arises in one of three ways:

Omitted Variables Omitted variables appear when we would like to control for one or more additional variables but, usually because of data unavailability, we cannot include them in a regression model. Specifically, suppose that Eðy j x; qÞ is the conditional expectation of interest, which can be written as a function linear in parameters and additive in q. If q is unobserved, we can always estimate Eðy j xÞ, but this need have no particular relationship to Eðy j x; qÞ when q and x are allowed to be correlated. One way to represent this situation is to write equation (4.1) where q is part of the error term u. If q and xj are correlated, then xj is endogenous. The cor

{67}------------------------------------------------

relation of explanatory variables with unobservables is often due to *self-selection*: if agents choose the value of  $x_j$ , this might depend on factors (q) that are unobservable to the analyst. A good example is omitted ability in a wage equation, where an individual's years of schooling are likely to be correlated with unobserved ability. We discuss the omitted variables problem in detail in Section 4.3.

**Measurement Error** In this case we would like to measure the (partial) effect of a variable, say  $x_K^*$ , but we can observe only an imperfect measure of it, say  $x_K$ . When we plug  $x_K$  in for  $x_K^*$ —thereby arriving at the estimable equation (4.1)—we necessarily put a measurement error into u. Depending on assumptions about how  $x_K^*$  and  $x_K$  are related, u and  $x_K$  may or may not be correlated. For example,  $x_K^*$  might denote a marginal tax rate, but we can only obtain data on the average tax rate. We will study the measurement error problem in Section 4.4.

**Simultaneity** Simultaneity arises when at least one of the explanatory variables is determined simultaneously along with y. If, say,  $x_K$  is determined partly as a function of y, then  $x_K$  and u are generally correlated. For example, if y is city murder rate and  $x_K$  is size of the police force, size of the police force is partly determined by the murder rate. Conceptually, this is a more difficult situation to analyze, because we must be able to think of a situation where we *could* vary  $x_K$  exogenously, even though in the data that we collect y and  $x_K$  are generated simultaneously. Chapter 9 treats simultaneous equations models in detail.

The distinctions among the three possible forms of endogeneity are not always sharp. In fact, an equation can have more than one source of endogeneity. For example, in looking at the effect of alcohol consumption on worker productivity (as typically measured by wages), we would worry that alcohol usage is correlated with unobserved factors, possibly related to family background, that also affect wage; this is an omitted variables problem. In addition, alcohol demand would generally depend on income, which is largely determined by wage; this is a simultaneity problem. And measurement error in alcohol usage is always a possibility. For an illuminating discussion of the three kinds of endogeneity as they arise in a particular field, see Deaton's (1995) survey chapter on econometric issues in development economics.

#### 4.2 Asymptotic Properties of OLS

We now briefly review the asymptotic properties of OLS for random samples from a population, focusing on inference. It is convenient to write the population equation of interest in vector form as

{68}------------------------------------------------

$$y = \mathbf{x}\boldsymbol{\beta} + u \tag{4.5}$$

where x is a 1 K vector of regressors and *b* 1ðb1; b2; ... ; b<sup>K</sup> Þ <sup>0</sup> is a K 1 vector. Since most equations contain an intercept, we will just assume that x<sup>1</sup> 1 1, as this assumption makes interpreting the conditions easier.

We assume that we can obtain a random sample of size N from the population in order to estimate *b*; thus, fðxi; yiÞ: i ¼ 1; 2; ... ; Ng are treated as independent, identically distributed random variables, where x<sup>i</sup> is 1 K and yi is a scalar. For each observation i we have

$$y_i = \mathbf{x}_i \boldsymbol{\beta} + u_i \tag{4.6}$$

which is convenient for deriving statistical properties of estimators. As for stating and interpreting assumptions, it is easiest to focus on the population model (4.5).