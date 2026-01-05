

{61}------------------------------------------------

For testing the null hypothesis  $H_0$ :  $\mathbf{R}\theta = \mathbf{r}$ , where  $\mathbf{r}$  is a  $Q \times 1$  nonrandom vector, define the **Wald statistic** for testing  $H_0$  against  $H_1$ :  $\mathbf{R}\theta \neq \mathbf{r}$  as

$$W_N \equiv (\mathbf{R}\hat{\boldsymbol{\theta}}_N - \mathbf{r})' [\mathbf{R}(\hat{\mathbf{V}}_N/N)\mathbf{R}']^{-1} (\mathbf{R}\hat{\boldsymbol{\theta}}_N - \mathbf{r})$$
(3.7)

Under  $H_0$ ,  $W_N \stackrel{a}{\sim} \chi_Q^2$ . If we abuse the asymptotics and treat  $\hat{\theta}_N$  as being distributed as Normal $(\theta, \hat{\mathbf{V}}_N/N)$ , we get equation (3.7) exactly.

LEMMA 3.9: Suppose that statement (3.3) holds, where **V** is positive definite. Let **c**:  $\Theta \to \mathbb{R}^Q$  be a continuously differentiable function on the parameter space  $\Theta \subset \mathbb{R}^P$ , where  $Q \leq P$ , and assume that  $\theta$  is in the interior of the parameter space. Define  $\mathbf{C}(\theta) \equiv \nabla_{\theta} \mathbf{c}(\theta)$  as the  $Q \times P$  Jacobian of **c**. Then

$$\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})] \stackrel{a}{\sim} \text{Normal}[\mathbf{0}, \mathbf{C}(\boldsymbol{\theta})\mathbf{V}\mathbf{C}(\boldsymbol{\theta})']$$
 (3.8)

and

$$\{\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})]\}'[\mathbf{C}(\boldsymbol{\theta})\mathbf{V}\mathbf{C}(\boldsymbol{\theta})']^{-1}\{\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})]\} \stackrel{a}{\sim} \chi_O^2$$

Define  $\hat{\mathbf{C}}_N \equiv \mathbf{C}(\hat{\boldsymbol{\theta}}_N)$ . Then plim  $\hat{\mathbf{C}}_N = \mathbf{C}(\boldsymbol{\theta})$ . If plim  $\hat{\mathbf{V}}_N = \mathbf{V}$ , then

$$\{\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})]\}'[\hat{\mathbf{C}}_N\hat{\mathbf{V}}_N\hat{\mathbf{C}}_N']^{-1}\{\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})]\} \stackrel{a}{\sim} \chi_O^2$$
(3.9)

Equation (3.8) is very useful for obtaining asymptotic standard errors for nonlinear functions of  $\hat{\boldsymbol{\theta}}_N$ . The appropriate estimator of  $\operatorname{Avar}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N)]$  is  $\hat{\mathbf{C}}_N(\hat{\mathbf{V}}_N/N)\hat{\mathbf{C}}_N' = \hat{\mathbf{C}}_N[\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)]\hat{\mathbf{C}}_N'$ . Thus, once  $\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)$  and the estimated Jacobian of  $\mathbf{c}$  are obtained, we can easily obtain

$$\operatorname{Avar}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N)] = \hat{\mathbf{C}}_N[\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)]\hat{\mathbf{C}}_N'$$
(3.10)

The asymptotic standard errors are obtained as the square roots of the diagonal elements of equation (3.10). In the scalar case  $\hat{\gamma}_N = c(\hat{\boldsymbol{\theta}}_N)$ , the asymptotic standard error of  $\hat{\gamma}_N$  is  $[\nabla_{\theta}c(\hat{\boldsymbol{\theta}}_N)[\text{Avar}(\hat{\boldsymbol{\theta}}_N)]\nabla_{\theta}c(\hat{\boldsymbol{\theta}}_N)']^{1/2}$ .

Equation (3.9) is useful for testing nonlinear hypotheses of the form  $H_0$ :  $\mathbf{c}(\theta) = \mathbf{0}$  against  $H_1$ :  $\mathbf{c}(\theta) \neq \mathbf{0}$ . The Wald statistic is

$$W_N = \sqrt{N} \mathbf{c}(\hat{\boldsymbol{\theta}}_N)' [\hat{\mathbf{C}}_N \hat{\mathbf{V}}_N \hat{\mathbf{C}}_N']^{-1} \sqrt{N} \mathbf{c}(\hat{\boldsymbol{\theta}}_N) = \mathbf{c}(\hat{\boldsymbol{\theta}}_N)' [\hat{\mathbf{C}}_N (\hat{\mathbf{V}}_N/N) \hat{\mathbf{C}}_N']^{-1} \mathbf{c}(\hat{\boldsymbol{\theta}}_N)$$
(3.11)

Under  $H_0$ ,  $W_N \stackrel{a}{\sim} \chi_Q^2$ .

The method of establishing equation (3.8), given that statement (3.3) holds, is often called the **delta method**, and it is used very often in econometrics. It gets its name from its use of calculus. The argument is as follows. Because  $\theta$  is in the interior of  $\Theta$ , and because plim  $\hat{\theta}_N = \theta$ ,  $\hat{\theta}_N$  is in an open, convex subset of  $\Theta$  containing  $\theta$  with

{62}------------------------------------------------

probability approaching one, therefore w.p.a.1 we can use a mean value expansion  $\mathbf{c}(\hat{\boldsymbol{\theta}}_N) = \mathbf{c}(\boldsymbol{\theta}) + \ddot{\mathbf{C}}_N \cdot (\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})$ , where  $\ddot{\mathbf{C}}_N$  denotes the matrix  $\mathbf{C}(\boldsymbol{\theta})$  with rows evaluated at mean values between  $\hat{\boldsymbol{\theta}}_N$  and  $\boldsymbol{\theta}$ . Because these mean values are trapped between  $\hat{\boldsymbol{\theta}}_N$  and  $\boldsymbol{\theta}$ , they converge in probability to  $\boldsymbol{\theta}$ . Therefore, by Slutsky's theorem,  $\ddot{\mathbf{C}}_N \stackrel{p}{\to} \mathbf{C}(\boldsymbol{\theta})$ , and we can write

$$\begin{split} \sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})] &= \ddot{\mathbf{C}}_N \cdot \sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) \\ &= \mathbf{C}(\boldsymbol{\theta})\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) + [\ddot{\mathbf{C}}_N - \mathbf{C}(\boldsymbol{\theta})]\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) \\ &= \mathbf{C}(\boldsymbol{\theta})\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) + o_p(1) \cdot O_p(1) = \mathbf{C}(\boldsymbol{\theta})\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) + o_p(1) \end{split}$$

We can now apply the asymptotic equivalence lemma and Lemma 3.8 [with  $\mathbf{R} \equiv \mathbf{C}(\boldsymbol{\theta})$ ] to get equation (3.8).

#### **Problems**

- **3.1.** Prove Lemma 3.1.
- 3.2. Using Lemma 3.2, prove Lemma 3.3.
- **3.3.** Explain why, under the assumptions of Lemma 3.4,  $\mathbf{g}(\mathbf{x}_N) = \mathbf{O}_p(1)$ .
- **3.4.** Prove Corollary 3.2.
- **3.5.** Let  $\{y_i: i=1,2,...\}$  be an independent, identically distributed sequence with  $E(y_i^2) < \infty$ . Let  $\mu = E(y_i)$  and  $\sigma^2 = Var(y_i)$ .
- a. Let  $\bar{y}_N$  denote the sample average based on a sample size of N. Find  $Var[\sqrt{N}(\bar{y}_N \mu)]$ .
- b. What is the asymptotic variance of  $\sqrt{N}(\bar{y}_N \mu)$ ?
- c. What is the asymptotic variance of  $\bar{y}_N$ ? Compare this with  $Var(\bar{y}_N)$ .
- d. What is the asymptotic standard deviation of  $\overline{y}_N$ ?
- e. How would you obtain the asymptotic standard error of  $\bar{y}_N$ ?
- **3.6.** Give a careful (albeit short) proof of the following statement: If  $\sqrt{N}(\hat{\boldsymbol{\theta}}_N \boldsymbol{\theta}) = O_p(1)$ , then  $\hat{\boldsymbol{\theta}}_N \boldsymbol{\theta} = O_p(N^{-c})$  for any  $0 \le c < \frac{1}{2}$ .
- **3.7.** Let  $\hat{\theta}$  be a  $\sqrt{N}$ -asymptotically normal estimator for the scalar  $\theta > 0$ . Let  $\hat{\gamma} = \log(\hat{\theta})$  be an estimator of  $\gamma = \log(\theta)$ .
- a. Why is  $\hat{\gamma}$  a consistent estimator of  $\gamma$ ?

{63}------------------------------------------------

b. Find the asymptotic variance of  $\sqrt{N}(\hat{\gamma} - \gamma)$  in terms of the asymptotic variance of  $\sqrt{N}(\hat{\theta} - \theta)$ .

- c. Suppose that, for a sample of data,  $\hat{\theta} = 4$  and  $se(\hat{\theta}) = 2$ . What is  $\hat{\gamma}$  and its (asymptotic) standard error?
- d. Consider the null hypothesis  $H_0$ :  $\theta = 1$ . What is the asymptotic t statistic for testing  $H_0$ , given the numbers from part c?
- e. Now state  $H_0$  from part d equivalently in terms of  $\gamma$ , and use  $\hat{\gamma}$  and  $se(\hat{\gamma})$  to test  $H_0$ . What do you conclude?
- **3.8.** Let  $\hat{\boldsymbol{\theta}} = (\hat{\theta}_1, \hat{\theta}_2)'$  be a  $\sqrt{N}$ -asymptotically normal estimator for  $\boldsymbol{\theta} = (\theta_1, \theta_2)'$ , with  $\theta_2 \neq 0$ . Let  $\hat{\gamma} = \hat{\theta}_1/\hat{\theta}_2$  be an estimator of  $\gamma = \theta_1/\theta_2$ .
- a. Show that plim  $\hat{\gamma} = \gamma$ .
- b. Find  $\operatorname{Avar}(\hat{\gamma})$  in terms of  $\boldsymbol{\theta}$  and  $\operatorname{Avar}(\hat{\boldsymbol{\theta}})$  using the delta method.
- c. If, for a sample of data,  $\hat{\boldsymbol{\theta}} = (-1.5, .5)'$  and  $\operatorname{Avar}(\hat{\boldsymbol{\theta}})$  is estimated as  $\begin{pmatrix} 1 & -.4 \\ -.4 & 2 \end{pmatrix}$ , find the asymptotic standard error of  $\hat{\gamma}$ .
- **3.9.** Let  $\hat{\boldsymbol{\theta}}$  and  $\tilde{\boldsymbol{\theta}}$  be two consistent,  $\sqrt{N}$ -asymptotically normal estimators of the  $P \times 1$  parameter vector  $\boldsymbol{\theta}$ , with Avar  $\sqrt{N}(\hat{\boldsymbol{\theta}} \boldsymbol{\theta}) = \mathbf{V}_1$  and Avar  $\sqrt{N}(\tilde{\boldsymbol{\theta}} \boldsymbol{\theta}) = \mathbf{V}_2$ . Define a  $Q \times 1$  parameter vector by  $\gamma = \mathbf{g}(\boldsymbol{\theta})$ , where  $\mathbf{g}(\cdot)$  is a continuously differentiable function. Show that, if  $\hat{\boldsymbol{\theta}}$  is asymptotically more efficient than  $\tilde{\boldsymbol{\theta}}$ , then  $\hat{\boldsymbol{\gamma}} \equiv \mathbf{g}(\hat{\boldsymbol{\theta}})$  is asymptotically efficient relative to  $\tilde{\boldsymbol{\gamma}} \equiv \mathbf{g}(\tilde{\boldsymbol{\theta}})$ .

{64}------------------------------------------------

# II LINEAR MODELS

In this part we begin our econometric analysis of linear models for cross section and panel data. In Chapter 4 we review the single-equation linear model and discuss ordinary least squares estimation. Although this material is, in principle, review, the approach is likely to be different from an introductory linear models course. In addition, we cover several topics that are not traditionally covered in texts but that have proven useful in empirical work. Chapter 5 discusses instrumental variables estimation of the linear model, and Chapter 6 covers some remaining topics to round out our treatment of the single-equation model.

Chapter 7 begins our analysis of systems of equations. The general setup is that the number of population equations is small relative to the (cross section) sample size. This allows us to cover seemingly unrelated regression models for cross section data as well as begin our analysis of panel data. Chapter 8 builds on the framework from Chapter 7 but considers the case where some explanatory variables may be uncorrelated with the error terms. Generalized method of moments estimation is the unifying theme. Chapter 9 applies the methods of Chapter 8 to the estimation of simultaneous equations models, with an emphasis on the conceptual issues that arise in applying such models.

Chapter 10 explicitly introduces unobserved-effects linear panel data models. Under the assumption that the explanatory variables are strictly exogenous conditional on the unobserved effect, we study several estimation methods, including fixed effects, first differencing, and random effects. The last method assumes, at a minimum, that the unobserved effect is uncorrelated with the explanatory variables in all time periods. Chapter 11 considers extensions of the basic panel data model, including failure of the strict exogeneity assumption.

{65}------------------------------------------------

## 4.1 Overview of the Single-Equation Linear Model

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

### 4.2.1 Consistency

As discussed in Section 4.1, the key assumption for OLS to consistently estimate *b* is the population orthogonality condition:

ASSUMPTION OLS.1: 
$$E(\mathbf{x}'u) = \mathbf{0}$$
.

Because x contains a constant, Assumption OLS.1 is equivalent to saying that u has mean zero and is uncorrelated with each regressor, which is how we will refer to Assumption OLS.1. Sufficient for Assumption OLS.1 is the zero conditional mean assumption (4.3).

The other assumption needed for consistency of OLS is that the expected outer product matrix of x has full rank, so that there are no exact linear relationships among the regressors in the population. This is stated succinctly as follows:

ASSUMPTION OLS.2: rank 
$$E(\mathbf{x}'\mathbf{x}) = K$$
.

As with Assumption OLS.1, Assumption OLS.2 is an assumption about the population. Since Eðx<sup>0</sup> xÞ is a symmetric K K matrix, Assumption OLS.2 is equivalent to assuming that Eðx<sup>0</sup> xÞ is positive definite. Since x<sup>1</sup> ¼ 1, Assumption OLS.2 is also equivalent to saying that the (population) variance matrix of the K 1 nonconstant elements in x is nonsingular. This is a standard assumption, which fails if and only if at least one of the regressors can be written as a linear function of the other regressors (in the population). Usually Assumption OLS.2 holds, but it can fail if the population model is improperly specified [for example, if we include too many dummy variables in x or mistakenly use something like logðageÞ and logðage<sup>2</sup>Þ in the same equation].

Under Assumptions OLS.1 and OLS.2, the parameter vector *b* is identified. In the context of models that are linear in the parameters under random sampling, identi

{69}------------------------------------------------

fication of  $\beta$  simply means that  $\beta$  can be written in terms of population moments in observable variables. (Later, when we consider nonlinear models, the notion of identification will have to be more general. Also, special issues arise if we cannot obtain a random sample from the population, something we treat in Chapter 17.) To see that  $\beta$  is identified under Assumptions OLS.1 and OLS.2, premultiply equation (4.5) by  $\mathbf{x}'$ , take expectations, and solve to get

$$\boldsymbol{\beta} = [\mathbf{E}(\mathbf{x}'\mathbf{x})]^{-1}\mathbf{E}(\mathbf{x}'y)$$

Because  $(\mathbf{x}, y)$  is observed,  $\boldsymbol{\beta}$  is identified. The **analogy principle** for choosing an estimator says to turn the population problem into its sample counterpart (see Goldberger, 1968; Manski, 1988). In the current application this step leads to the **method of moments**: replace the population moments  $E(\mathbf{x}'\mathbf{x})$  and  $E(\mathbf{x}'y)$  with the corresponding sample averages. Doing so leads to the OLS estimator:

$$\hat{\beta} = \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{x}_{i} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' y_{i} \right) = \beta + \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{x}_{i} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' u_{i} \right)$$

which can be written in full matrix form as  $(\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}$ , where  $\mathbf{X}$  is the  $N \times K$  data matrix of regressors with ith row  $\mathbf{x}_i$  and  $\mathbf{Y}$  is the  $N \times 1$  data vector with ith element  $y_i$ . Under Assumption OLS.2,  $\mathbf{X}'\mathbf{X}$  is nonsingular with probability approaching one and  $\text{plim}[(N^{-1}\sum_{i=1}^{N}\mathbf{x}_i'\mathbf{x}_i)^{-1}] = \mathbf{A}^{-1}$ , where  $\mathbf{A} \equiv \mathbf{E}(\mathbf{x}'\mathbf{x})$  (see Corollary 3.1). Further, under Assumption OLS.1,  $\text{plim}(N^{-1}\sum_{i=1}^{N}\mathbf{x}_i'u_i) = \mathbf{E}(\mathbf{x}'u) = \mathbf{0}$ . Therefore, by Slutsky's theorem (Lemma 3.4),  $\text{plim } \hat{\boldsymbol{\beta}} = \boldsymbol{\beta} + \mathbf{A}^{-1} \cdot \mathbf{0} = \boldsymbol{\beta}$ . We summarize with a theorem:

THEOREM 4.1 (Consistency of OLS): Under Assumptions OLS.1 and OLS.2, the OLS estimator  $\hat{\beta}$  obtained from a random sample following the population model (4.5) is consistent for  $\beta$ .

The simplicity of the proof of Theorem 4.1 should not undermine its usefulness. Whenever an equation can be put into the form (4.5) and Assumptions OLS.1 and OLS.2 hold, OLS using a random sample consistently estimates  $\beta$ . It does not matter where this equation comes from, or what the  $\beta_j$  actually represent. As we will see in Sections 4.3 and 4.4, often an estimable equation is obtained only after manipulating an underlying structural equation. An important point to remember is that, once the linear (in parameters) equation has been specified with an additive error and Assumptions OLS.1 and OLS.2 are verified, there is no need to reprove Theorem 4.1.

Under the assumptions of Theorem 4.1,  $x\beta$  is the linear projection of y on x. Thus, Theorem 4.1 shows that OLS consistently estimates the parameters in a linear projection, subject to the rank condition in Assumption OLS.2. This is very general, as it places no restrictions on the nature of y—for example, y could be a binary variable

{70}------------------------------------------------

or some other variable with discrete characteristics. Since a conditional expectation that is linear in parameters is also the linear projection, Theorem 4.1 also shows that OLS consistently estimates conditional expectations that are linear in parameters. We will use this fact often in later sections.

There are a few final points worth emphasizing. First, if either Assumption OLS.1 or OLS.2 fails, then  $\beta$  is not identified (unless we make other assumptions, as in Chapter 5). Usually it is correlation between u and one or more elements of x that causes lack of identification. Second, the OLS estimator is *not* necessarily unbiased even under Assumptions OLS.1 and OLS.2. However, if we impose the zero conditional mean assumption (4.3), then it can be shown that  $E(\hat{\beta} | X) = \beta$  if X'X is non-singular; see Problem 4.2. By iterated expectations,  $\hat{\beta}$  is then also unconditionally unbiased, provided the expected value  $E(\hat{\beta})$  exists.

Finally, we have not made the much more restrictive assumption that u and  $\mathbf{x}$  are *independent*. If E(u) = 0 and u is independent of  $\mathbf{x}$ , then assumption (4.3) holds, but not vice versa. For example,  $Var(u \mid \mathbf{x})$  is entirely unrestricted under assumption (4.3), but  $Var(u \mid \mathbf{x})$  is necessarily constant if u and  $\mathbf{x}$  are independent.

#### 4.2.2 Asymptotic Inference Using OLS

The asymptotic distribution of the OLS estimator is derived by writing

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \left(N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{x}_{i}\right)^{-1} \left(N^{-1/2} \sum_{i=1}^{N} \mathbf{x}_{i}' u_{i}\right)$$

As we saw in Theorem 4.1,  $(N^{-1}\sum_{i=1}^{N}\mathbf{x}_{i}'\mathbf{x}_{i})^{-1} - \mathbf{A}^{-1} = o_{p}(1)$ . Also,  $\{(\mathbf{x}_{i}'u_{i}): i=1,2,\ldots\}$  is an i.i.d. sequence with zero mean, and we assume that each element has finite variance. Then the central limit theorem (Theorem 3.2) implies that  $N^{-1/2}\sum_{i=1}^{N}\mathbf{x}_{i}'u_{i} \stackrel{d}{\to} \text{Normal}(\mathbf{0},\mathbf{B})$ , where  $\mathbf{B}$  is the  $K \times K$  matrix

$$\mathbf{B} \equiv \mathbf{E}(u^2 \mathbf{x}' \mathbf{x}) \tag{4.7}$$

This implies  $N^{-1/2} \sum_{i=1}^{N} \mathbf{x}'_{i} u_{i} = \mathbf{O}_{p}(1)$ , and so we can write

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \mathbf{A}^{-1} \left( N^{-1/2} \sum_{i=1}^{N} \mathbf{x}_{i}' u_{i} \right) + o_{p}(1)$$

$$(4.8)$$

since  $o_p(1) \cdot O_p(1) = o_p(1)$ . We can use equation (4.8) to immediately obtain the asymptotic distribution of  $\sqrt{N}(\hat{\pmb{\beta}} - \pmb{\beta})$ . A **homoskedasticity** assumption simplifies the form of OLS asymptotic variance:

ASSUMPTION OLS.3:  $E(u^2x'x) = \sigma^2E(x'x)$ , where  $\sigma^2 \equiv E(u^2)$ .