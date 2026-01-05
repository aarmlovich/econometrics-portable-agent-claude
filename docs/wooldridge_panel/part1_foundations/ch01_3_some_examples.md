# Some Examples

> Pages: 25-27

In this section we provide two examples to emphasize some of the concepts from the previous sections. We begin with a standard example from labor economics.

Example 1.1 (Wage Offer Function): Suppose that the natural log of the wage offer, wage<sup>o</sup>, is determined as

{26}------------------------------------------------

$$\log(wage^o) = \beta_0 + \beta_1 educ + \beta_2 exper + \beta_3 married + u \tag{1.1}$$

where educ is years of schooling, exper is years of labor market experience, and married is a binary variable indicating marital status. The variable u, called the error term or disturbance, contains unobserved factors that affect the wage offer. Interest lies in the unknown parameters, the bj.

We should have a concrete population in mind when specifying equation (1.1). For example, equation (1.1) could be for the population of all working women. In this case, it will not be difficult to obtain a random sample from the population.

All assumptions can be stated in terms of the population model. The crucial assumptions involve the relationship between u and the observable explanatory variables, educ, exper, and married. For example, is the expected value of u given the explanatory variables educ, exper, and married equal to zero? Is the variance of u conditional on the explanatory variables constant? There are reasons to think the answer to both of these questions is no, something we discuss at some length in Chapters 4 and 5. The point of raising them here is to emphasize that all such questions are most easily couched in terms of the population model.

What happens if the relevant population is all women over age 18? A problem arises because a random sample from this population will include women for whom the wage offer cannot be observed because they are not working. Nevertheless, we can think of a random sample being obtained, but then wage<sup>o</sup> is unobserved for women not working.

For deriving the properties of estimators, it is often useful to write the population model for a generic draw from the population. Equation (1.1) becomes

$$\log(wage_i^o) = \beta_0 + \beta_1 educ_i + \beta_2 exper_i + \beta_3 married_i + u_i, \tag{1.2}$$

where i indexes person. Stating assumptions in terms of ui and x<sup>i</sup> 1ðeduci; experi; marriediÞ is the same as stating assumptions in terms of u and x. Throughout this book, the i subscript is reserved for indexing cross section units, such as individual, firm, city, and so on. Letters such as j, g, and h will be used to index variables, parameters, and equations.

Before ending this example, we note that using matrix notation to write equation (1.2) for all N observations adds nothing to our understanding of the model or sampling scheme; in fact, it just gets in the way because it gives the mistaken impression that the matrices tell us something about the assumptions in the underlying population. It is much better to focus on the population model (1.1).

The next example is illustrative of panel data applications.

{27}------------------------------------------------

Example 1.2 (Effect of Spillovers on Firm Output): Suppose that the population is all manufacturing firms in a country operating during a given three-year period. A production function describing output in the population of firms is

$$\log(output_t) = \delta_t + \beta_1 \log(labor_t) + \beta_2 \log(capital_t)$$

$$+ \beta_3 spillover_t + quality + u_t, \qquad t = 1, 2, 3$$
(1.3)

Here, spillovert is a measure of foreign firm concentration in the region containing the firm. The term quality contains unobserved factors—such as unobserved managerial or worker quality—which affect productivity and are constant over time. The error ut represents unobserved shocks in each time period. The presence of the parameters dt, which represent different intercepts in each year, allows for aggregate productivity to change over time. The coefficients on labort, capitalt, and spillovert are assumed constant across years.

As we will see when we study panel data methods, there are several issues in deciding how best to estimate the bj. An important one is whether the unobserved productivity factors (quality) are correlated with the observable inputs. Also, can we assume that spillovert at, say, t ¼ 3 is uncorrelated with the error terms in all time periods?

For panel data it is especially useful to add an i subscript indicating a generic cross section observation—in this case, a randomly sampled firm:

$$\log(output_{it}) = \delta_t + \beta_1 \log(labor_{it}) + \beta_2 \log(capital_{it})$$

$$+ \beta_3 spillover_{it} + quality_i + u_{it}, \qquad t = 1, 2, 3$$
(1.4)

Equation (1.4) makes it clear that qualityi is a firm-specific term that is constant over time and also has the same effect in each time period, while uit changes across time and firm. Nevertheless, the key issues that we must address for estimation can be discussed for a generic i, since the draws are assumed to be randomly made from the population of all manufacturing firms.

Equation (1.4) is an example of another convention we use throughout the book: the subscript t is reserved to index time, just as i is reserved for indexing the cross section.