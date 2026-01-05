# Introduction and Motivation

> Pages: 526-530

In this chapter we cover a class of models traditionally called censored regression models. Censored regression models generally apply when the variable to be explained is partly continuous but has positive probability mass at one or more points. In order to apply these methods effectively, we must understand that the statistical model underlying censored regression analysis applies to problems that are conceptually very different.

For the most part, censored regression applications can be put into one of two categories. In the first case there is a variable with quantitative meaning, call it y, and we are interested in the population regression Eðy j xÞ. If y and x were observed for everyone in the population, there would be nothing new: we could use standard regression methods (ordinary or nonlinear least squares). But a data problem arises because y is censored above or below some value; that is, it is not observable for part of the population. An example is top coding in survey data. For example, assume that y is family wealth, and, for a randomly drawn family, the actual value of wealth is recorded up to some threshold, say, \$200,000, but above that level only the fact that wealth was more than \$200,000 is recorded. Top coding is an example of data censoring, and is analogous to the data-coding problem we discussed in Section 15.10.2 in connection with interval regression.

Example 16.1 (Top Coding of Wealth): In the population of all families in the United States, let wealth denote actual family wealth, measured in thousands of dollars. Suppose that wealth follows the linear regression model Eðwealth j xÞ ¼ x*b*, where x is a 1 - K vector of conditioning variables. However, we observe wealth only when wealth a200. When wealth is greater than 200 we know that it is, but we do not know the actual value of wealth. Define observed wealth as

```
wealth ¼ minðwealth; 200Þ
```

The definition wealth ¼ 200 when wealth > 200 is arbitrary, but it is useful for defining the statistical model that follows. To estimate *b* we might assume that wealth given x has a homoskedastic normal distribution. In error form,

wealth\* = 
$$\mathbf{x}\boldsymbol{\beta} + u$$
,  $u \mid \mathbf{x} \sim \text{Normal}(0, \sigma^2)$ 

This is a strong assumption about the conditional distribution of wealth, something we could avoid entirely if wealth were not censored above 200. Under these assumptions we can write recorded wealth as

$$wealth = \min(200, \mathbf{x}\boldsymbol{\beta} + u) \tag{16.1}$$

{527}------------------------------------------------

Data censoring also arises in the analysis of duration models, a topic we treat in Chapter 20.

A second kind of application of censored regression models appears more often in econometrics and, unfortunately, is where the label ''censored regression'' is least appropriate. To describe the situation, let y be an observable choice or outcome describing some economic agent, such as an individual or a firm, with the following characteristics: y takes on the value zero with positive probability but is a continuous random variable over strictly positive values. There are many examples of variables that, at least approximately, have these features. Just a few examples include amount of life insurance coverage chosen by an individual, family contributions to an individual retirement account, and firm expenditures on research and development. In each of these examples we can imagine economic agents solving an optimization problem, and for some agents the optimal choice will be the corner solution, y ¼ 0. We will call this kind of response variable a corner solution outcome. For corner solution outcomes, it makes more sense to call the resulting model a corner solution model. Unfortunately, the name ''censored regression model'' appears to be firmly entrenched.

For corner solution applications, we must understand that the issue is not data observability: we are interested in features of the distribution of y given x, such as Eðy j xÞ and Pðy ¼ 0 j xÞ. If we are interested only in the effect of the xj on the mean response, Eðy j xÞ, it is natural to ask, Why not just assume Eðy j xÞ ¼ x*b* and apply OLS on a random sample? Theoretically, the problem is that, when yb0, Eðy j xÞ cannot be linear in x unless the range of x is fairly limited. A related weakness is that the model implies constant partial effects. Further, for the sample at hand, predicted values for y can be negative for many combinations of x and *b*. These are very similar to the shortcomings of the linear probability model for binary responses.

We have already seen functional forms that ensure that Eðy j xÞ is positive for all values of x and parameters, the leading case being the exponential function, Eðy j xÞ ¼ expðx*b*Þ. [We cannot use logðyÞ as the dependent variable in a linear regression because logð0Þ is undefined.] We could then estimate *b* using nonlinear least squares (NLS), as in Chapter 12. Using an exponential conditional mean function is a reasonable strategy to follow, as it ensures that predicted values are positive and that the parameters are easy to interpret. However, it also has limitations. First, if y is a corner solution outcome, Varðy j xÞ is probably heteroskedastic, and so NLS could be inefficient. While we may be able to partly solve this problem using weighted NLS, any model for the conditional variance would be arbitrary. Probably a more important criticism is that we would not be able to measure the effect of each xj on other features of the distribution of y given x. Two that are commonly of 

{528}------------------------------------------------

interest are Pðy ¼ 0 j xÞ and Eðy j x; y > 0Þ. By definition, a model for Eðy j xÞ does not allow us to estimate other features of the distribution. If we make a full distributional assumption for y given x, we can estimate any feature of the conditional distribution. In addition, we will obtain efficient estimates of quantities such as Eðy j xÞ.

The following example shows how a simple economic model leads to an econometric model where y can be zero with positive probability and where the conditional expectation Eðy j xÞ is not a linear function of parameters.

Example 16.2 (Charitable Contributions): Problem 15.1 shows how to derive a probit model from a utility maximization problem for charitable giving, using utility function utiliðc; qÞ ¼ c þ ai logð1 þ qÞ, where c is annual consumption, in dollars, and q is annual charitable giving. The variable ai determines the marginal utility of giving for family i. Maximizing subject to the budget constraint ci þ piqi ¼ mi (where mi is family income and pi is the price of a dollar of charitable contributions) and the inequality constraint c, qb 0, the solution qi is easily shown to be qi ¼ 0 if ai=pi a1 and qi ¼ ai=pi 1 if ai=pi > 1. We can write this relation as 1 þ qi ¼ maxð1; ai=piÞ. If ai ¼ expðzi*g* þ uiÞ, where ui is an unobservable independent of ðzi; pi; miÞ and normally distributed, then charitable contributions are determined by the equation

$$\log(1+q_i) = \max[0, \mathbf{z}_i \gamma - \log(p_i) + u_i]$$
(16.2)

Comparing equations (16.2) and (16.1) shows that they have similar statistical structures. In equation (16.2) we are taking a maximum, and the lower threshold is zero, whereas in equation (16.1) we are taking a minimum with an upper threshold of 200. Each problem can be transformed into the same statistical model: for a randomly drawn observation i from the population,

$$y_i^* = \mathbf{x}_i \boldsymbol{\beta} + u_i, \qquad u_i \mid \mathbf{x}_i \sim \text{Normal}(0, \sigma^2)$$
 (16.3)

$$y_i = \max(0, y_i^*) {(16.4)}$$

These equations constitute what is known as the standard censored Tobit model (after Tobin, 1956) or type I Tobit model (which is from Amemiya's 1985 taxonomy). This is the canonical form of the model in the sense that it is the form usually studied in methodological papers, and it is the default model estimated by many software packages.

The charitable contributions example immediately fits into the standard censored Tobit framework by defining x<sup>i</sup> ¼ ½zi; logðpiÞ and yi ¼ logð1 þ qiÞ. This particular transformation of qi and the restriction that the coefficient on logðpiÞ is 1 depend critically on the utility function used in the example. In practice, we would probably take yi ¼ qi and allow all parameters to be unrestricted.

{529}------------------------------------------------

The wealth example can be cast as equations (16.3) and (16.4) after a simple transformation:

$$-(wealth_i - 200) = \max(0, -200 - \mathbf{x}_i \beta - u_i)$$

and so the intercept changes, and all slope coefficients have the opposite sign from equation (16.1). For data-censoring problems, it is easier to study the censoring scheme directly, and many econometrics packages support various kinds of data censoring. Problem 16.3 asks you to consider general forms of data censoring, including the case when the censoring point can change with observation, in which case the model is often called the censored normal regression model. (This label properly emphasizes the data-censoring aspect.)

For the population, we write the standard censored Tobit model as

$$y^* = \mathbf{x}\boldsymbol{\beta} + u, \qquad u \mid \mathbf{x} \sim \text{Normal}(0, \sigma^2)$$
 (16.5)

$$y = \max(0, y^*) \tag{16.6}$$

where, except in rare cases, x contains unity. As we saw from the two previous examples, different features of this model are of interest depending on the type of application. In examples with true data censoring, such as Example 16.1, the vector *b* tells us everything we want to know because Eðy j xÞ ¼ x*b* is of interest. For corner solution outcomes, such as Example 16.2, *b* does not give the entire story. Usually, we are interested in Eðy j xÞ or Eðy j x; y > 0Þ. These certainly depend on *b*, but in a nonlinear fashion.

For the statistical model (16.5) and (16.6) to make sense, the variable y should have characteristics of a normal random variable. In data censoring cases this requirement means that the variable of interest y should have a homoskedastic normal distribution. In some cases the logarithmic transformation can be used to make this assumption more plausible. Example 16.1 might be one such case if wealth is positive for all families. See also Problems 16.1 and 16.2.

In corner solution examples, the variable y should be (roughly) continuous when y > 0. Thus the Tobit model is not appropriate for ordered responses, as in Section 15.10. Similarly, Tobit should not be applied to count variables, especially when the count variable takes on only a small number of values (such as number of patents awarded annually to a firm or the number of times someone is arrested during a year). Poisson regression models, a topic we cover in Chapter 19, are better suited for analyzing count data.

For corner solution outcomes, we must avoid placing too much emphasis on the latent variable y. Most of the time y is an artificial construct, and we are not interested in Eðy j xÞ. In Example 16.2 we derived the model for charitable con

{530}------------------------------------------------

tributions using utility maximization, and a latent variable never appeared. Viewing y as something like ''desired charitable contributions'' can only sow confusion: the variable of interest, y, is observed charitable contributions.