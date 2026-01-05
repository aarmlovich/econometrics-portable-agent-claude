# Multinomial Logit

> Pages: 506-513

The logit model for binary outcomes extends to the case where the **unordered response** has more than two outcomes. Examples of unordered multinomial responses include occupational choice, choice of health plan, and transportation mode for commuting to work. In each case, an individual chooses one alternative from the group of choices, and the labeling of the choices is arbitrary. Let y denote a random variable taking on the values  $\{0, 1, \ldots, J\}$  for J a positive integer, and let  $\mathbf{x}$  denote a set of conditioning variables. For example, if y denotes occupational choice,  $\mathbf{x}$  can contain things like education, age, gender, race, and marital status. As usual,  $(\mathbf{x}_i, y_i)$  is a random draw from the population.

As in the binary response case, we are interested in how ceteris paribus changes in the elements of  $\mathbf{x}$  affect the response probabilities,  $P(y=j\,|\,\mathbf{x}),\ j=0,1,2,\ldots,J$ . Since the probabilities must sum to unity,  $P(y=0\,|\,\mathbf{x})$  is determined once we know the probabilities for  $j=1,\ldots,J$ .

Let x be a  $1 \times K$  vector with first-element unity. The multinomial logit (MNL) model has response probabilities

$$\mathbf{P}(y=j\,|\,\mathbf{x}) = \exp(\mathbf{x}\boldsymbol{\beta}_j) / \left[1 + \sum_{h=1}^{J} \exp(\mathbf{x}\boldsymbol{\beta}_h)\right], \qquad j=1,\dots,J$$
 (15.76)

where  $\beta_j$  is  $K \times 1$ , j = 1, ..., J. Because the response probabilities must sum to unity,

$$P(y = 0 \mid \mathbf{x}) = 1 / \left[ 1 + \sum_{h=1}^{J} \exp(\mathbf{x} \boldsymbol{\beta}_h) \right]$$

When J = 1,  $\beta_1$  is the  $K \times 1$  vector of unknown parameters, and we get the binary logit model.

The partial effects for this model are complicated. For continuous  $x_k$ , we can write

$$\frac{\partial \mathbf{P}(y=j|\mathbf{x})}{\partial x_k} = \mathbf{P}(y=j|\mathbf{x}) \left\{ \beta_{jk} - \left[ \sum_{h=1}^{J} \beta_{hk} \exp(\mathbf{x}\boldsymbol{\beta}_h) \right] / g(\mathbf{x},\boldsymbol{\beta}) \right\}$$
(15.77)

where  $\beta_{hk}$  is the kth element of  $\beta_h$  and  $g(\mathbf{x}, \boldsymbol{\beta}) = 1 + \sum_{h=1}^{J} \exp(\mathbf{x}\boldsymbol{\beta}_h)$ . Equation

{507}------------------------------------------------

(15.77) shows that even the direction of the effect is not determined entirely by  $\beta_{jk}$ . A simpler interpretation of  $\beta_i$  is given by

$$p_{j}(\mathbf{x},\boldsymbol{\beta})/p_{0}(\mathbf{x},\boldsymbol{\beta}) = \exp(\mathbf{x}\boldsymbol{\beta}_{j}), \qquad j = 1, 2, \dots, J$$
(15.78)

where  $p_j(\mathbf{x}, \boldsymbol{\beta})$  denotes the response probability in equation (15.76). Thus the change in  $p_j(\mathbf{x}, \boldsymbol{\beta})/p_0(\mathbf{x}, \boldsymbol{\beta})$  is approximately  $\beta_{jk} \exp(\mathbf{x}\boldsymbol{\beta}_j)\Delta x_k$  for roughly continuous  $x_k$ . Equivalently, the log-odds ratio is linear in  $\mathbf{x}$ :  $\log[p_j(\mathbf{x}, \boldsymbol{\beta})/p_0(\mathbf{x}, \boldsymbol{\beta})] = \mathbf{x}\boldsymbol{\beta}_j$ . This result extends to general j and h:  $\log[p_j(\mathbf{x}, \boldsymbol{\beta})/p_h(\mathbf{x}, \boldsymbol{\beta})] = \mathbf{x}(\boldsymbol{\beta}_j - \boldsymbol{\beta}_h)$ .

Here is another useful fact about the multinomial logit model. Since  $P(y = j \text{ or } y = h \mid \mathbf{x}) = p_j(\mathbf{x}, \boldsymbol{\beta}) + p_h(\mathbf{x}, \boldsymbol{\beta}),$ 

$$P(y = j | y = j \text{ or } y = h, \mathbf{x}) = p_j(\mathbf{x}, \boldsymbol{\beta}) / [p_j(\mathbf{x}, \boldsymbol{\beta}) + p_h(\mathbf{x}, \boldsymbol{\beta})] = \Lambda[\mathbf{x}(\boldsymbol{\beta}_j - \boldsymbol{\beta}_h)]$$

where  $\Lambda(\cdot)$  is the logistic function. In other words, conditional on the choice being either j or h, the probability that the outcome is j follows a standard logit model with parameter vector  $\boldsymbol{\beta}_j - \boldsymbol{\beta}_h$ .

Since we have fully specified the density of y given  $\mathbf{x}$ , estimation of the MNL model is best carried out by maximum likelihood. For each i the conditional log likelihood can be written as

$$\ell_i(\boldsymbol{\beta}) = \sum_{j=0}^{J} 1[y_i = j] \log[p_j(\mathbf{x}_i, \boldsymbol{\beta})]$$

where the indicator function selects out the appropriate response probability for each observation *i*. As usual, we estimate  $\beta$  by maximizing  $\sum_{i=1}^{N} \ell_i(\beta)$ . McFadden (1974) has shown that the log-likelihood function is globally concave, and this fact makes the maximization problem straightforward. The conditions needed to apply Theorems 13.1 and 13.2 for consistency and asymptotic normality are broadly applicable; see McFadden (1984).

Example 15.4 (School and Employment Decisions for Young Men): The data KEANE.RAW (a subset from Keane and Wolpin, 1997) contains employment and schooling history for a sample of men for the years 1981 to 1987. We use the data for 1987. The three possible outcomes are enrolled in school (status = 0), not in school and not working (status = 1), and working (status = 2). The explanatory variables are education, a quadratic in past work experience, and a black binary indicator. The base category is enrolled in school. Out of 1,717 observations, 99 are enrolled in school, 332 are at home, and 1,286 are working. The results are given in Table 15.2.

Another year of education reduces the log-odds between at home and enrolled in school by -.674, and the log-odds between at home and enrolled in school is .813

{508}------------------------------------------------

Table 15.2 Multinomial Logit Estimates of School and Labor Market Decisions

<table><tbody><tr><th colspan="4">Dependent Variable: status</th></tr><tr><th>Explanatory Variable</th><th>home<br/>(status ¼ 1)</th><th>work<br/>(status ¼ 2)</th><th></th></tr><tr><td>educ</td><td>.674<br/>(.070)</td><td>.315<br/>(.065)</td><td></td></tr><tr><td>exper</td><td>.106<br/>(.173)</td><td>.849<br/>(.157)</td><td></td></tr><tr><td>exper 2</td><td>.013<br/>(.025)</td><td>.077<br/>(.023)</td><td></td></tr><tr><td>black</td><td>.813<br/>(.303)</td><td>.311<br/>(.282)</td><td></td></tr><tr><td>constant</td><td>10.28<br/>(1.13)</td><td>5.54<br/>(1.09)</td><td></td></tr><tr><td>Number of observations</td><td>1,717</td><td></td><td></td></tr><tr><td>Percent correctly predicted</td><td>79.6</td><td></td><td></td></tr><tr><td>Log-likelihood value</td><td>907.86</td><td></td><td></td></tr><tr><td>Pseudo R-squared</td><td>.243</td><td></td><td></td></tr></tbody></table>

higher for black men. The magnitudes of these coefficients are difficult to interpret. Instead, we can either compute partial effects, as in equation (15.77), or compute differences in probabilities. For example, consider two black men, each with five years of experience. A black man with 16 years of education has an employment probability that is .042 higher than a man with 12 years of education, and the at-home probability is .072 lower. (Necessarily, the in-school probability is .030 higher for the man with 16 years of education.) These results are easily obtained by comparing fitted probabilities after multinomial logit estimation.

The experience terms are each insignificant in the home column, but the Wald test for joint significance of exper and exper<sup>2</sup> gives p-value ¼ .047, and so they are jointly significant at the 5 percent level. We would probably leave their coefficients unrestricted in *b*<sup>1</sup> rather than setting them to zero.

The fitted probabilities can be used for prediction purposes: for each observation i, the outcome with the highest estimated probability is the predicted outcome. This can be used to obtain a percent correctly predicted, by category if desired. For the previous example, the overall percent correctly predicted is almost 80 percent, but the model does a much better job of predicting that a man is employed (95.2 percent correct) than in school (12.1 percent) or at home (39.2 percent).

{509}------------------------------------------------

#### 15.9.2 Probabilistic Choice Models

McFadden (1974) showed that a model closely related to the multinomial logit model can be obtained from an underlying utility comparison. Suppose that, for a random draw i from the underlying population (usually, but not necessarily, individuals), the utility from choosing alternative j is

$$y_{ii}^* = \mathbf{x}_{ij}\boldsymbol{\beta} + a_{ij}, \qquad j = 0, \dots, J \tag{15.79}$$

where  $a_{ij}$ , j = 0, 1, 2, ..., J are unobservables affecting tastes. Here,  $\mathbf{x}_{ij}$  is a  $1 \times K$  vector that differs across alternatives and possibly across individuals as well. For example,  $\mathbf{x}_{ij}$  might contain the commute time for individual i using transportation mode j, or the co-payment required by health insurance plan j (which may or may not differ by individual). For reasons we will see,  $\mathbf{x}_{ij}$  cannot contain elements that vary only across i and not j; in particular,  $\mathbf{x}_{ij}$  does not contain unity. We assume that the (J+1)-vector  $\mathbf{a}_i$  is independent of  $\mathbf{x}_i$ , which contains  $\{\mathbf{x}_{ij}: j=0,\ldots,J\}$ .

Let  $y_i$  denote the choice of individual i that maximizes utility:

$$y_i = \operatorname{argmax}(y_{i0}^*, y_{i2}^*, \dots, y_{iJ}^*)$$

so that  $y_i$  takes on a value in  $\{0, 1, ..., J\}$ . As shown by McFadden (1974), if the  $a_{ij}$ , j = 0, ..., J are independently distributed with cdf  $F(a) = \exp[-\exp(-a)]$ —the **type I extreme value distribution**—then

$$\mathbf{P}(y_i = j \mid \mathbf{x}_i) = \exp(\mathbf{x}_{ij}\boldsymbol{\beta}) / \left[ \sum_{h=0}^{J} \exp(\mathbf{x}_{ih}\boldsymbol{\beta}) \right], \qquad j = 0, \dots, J$$
 (15.80)

The response probabilities in equation (15.80) constitute what is usually called the **conditional logit model**. Dropping the subscript i and differentiating shows that the marginal effects are given by

$$\partial p_j(\mathbf{x})/\partial x_{jk} = p_j(\mathbf{x})[1 - p_j(\mathbf{x})]\beta_k, \qquad j = 0, \dots, J, \ k = 1, \dots, K$$
 (15.81)

and

$$\partial p_j(\mathbf{x})/\partial x_{hk} = -p_j(\mathbf{x})p_h(\mathbf{x})\beta_k, \qquad j \neq h, \ k = 1, \dots, K$$
 (15.82)

where  $p_j(\mathbf{x})$  is the response probability in equation (15.80) and  $\beta_k$  is the kth element of  $\boldsymbol{\beta}$ . As usual, if the  $\mathbf{x}_j$  contain nonlinear functions of underlying explanatory variables, this fact will be reflected in the partial derivatives.

The conditional logit and multinomial logit models have similar response probabilities, but they differ in some important respects. In the MNL model, the condi-

{510}------------------------------------------------

tioning variables do not change across alternative: for each i,  $\mathbf{x}_i$  contains variables specific to the individual but not to the alternatives. This model is appropriate for problems where characteristics of the alternatives are unimportant or are not of interest, or where the data are simply not available. For example, in a model of occupational choice, we do not usually know how much someone could make in every occupation. What we can usually collect data on are things that affect individual productivity and tastes, such as education and past experience. The MNL model allows these characteristics to have different effects on the relative probabilities between any two choices.

The conditional logit model is intended specifically for problems where consumer or firm choices are at least partly made based on observable attributes of each alternative. The utility level of each choice is assumed to be a linear function in choice attributes,  $\mathbf{x}_{ij}$ , with common parameter vector  $\boldsymbol{\beta}$ . This turns out to actually contain the MNL model as a special case by appropriately choosing  $\mathbf{x}_{ij}$ . Suppose that  $\mathbf{w}_i$  is a vector of individual characteristics and that  $P(y_i = j \mid \mathbf{w}_i)$  follows the MNL in equation (15.76) with parameters  $\boldsymbol{\delta}_j$ ,  $j = 1, \ldots, J$ . We can cast this model as the conditional logit model by defining  $\mathbf{x}_{ij} = (d1_j \mathbf{w}_i, d2_j \mathbf{w}_i, \ldots, dJ_j \mathbf{w}_i)$ , where  $dj_h$  is a dummy variable equal to unity when j = h, and  $\boldsymbol{\beta} = (\boldsymbol{\delta}'_1, \ldots, \boldsymbol{\delta}'_J)'$ . Consequently, some authors refer to the conditional logit model as the multinomial logit model, with the understanding that alternative-specific characteristics are allowed in the response probability.

Empirical applications of the conditional logit model often include individualspecific variables by allowing them to have separate effects on the latent utilities. A general model is

$$y_{ij}^* = \mathbf{z}_{ij} \boldsymbol{\gamma} + \mathbf{w}_i \boldsymbol{\delta}_j + a_{ij}, \qquad j = 0, 1, \dots, J$$

with  $\delta_0 = \mathbf{0}$  as a normalization, where  $\mathbf{z}_{ij}$  varies across j and possibly i. If  $\delta_j = \delta$  for all j, then  $\mathbf{w}_i \delta$  drops out of all response probabilities.

The conditional logit model is very convenient for modeling probabilistic choice, but it has some limitations. An important restriction is

$$p_j(\mathbf{x}_j)/p_h(\mathbf{x}_h) = \exp(\mathbf{x}_j\boldsymbol{\beta})/\exp(\mathbf{x}_h\boldsymbol{\beta}) = \exp[(\mathbf{x}_j - \mathbf{x}_h)\boldsymbol{\beta}]$$
(15.83)

so that relative probabilities for any two alternatives depend only on the attributes of those two alternatives. This is called the **independence from irrelevant alternatives** (IIA) assumption because it implies that adding another alternative or changing the characteristics of a third alternative does not affect the relative odds between alternatives j and h. This implication is implausible for applications with similar alterna-


{511}------------------------------------------------

tives. A well-known example is due to McFadden (1974). Consider commuters initially choosing between two modes of transportation, car and red bus. Suppose that a consumer chooses between the buses with equal probability, .5, so that the ratio in equation (15.83) is unity. Now suppose a third mode, blue bus, is added. Assuming bus commuters do not care about the color of the bus, consumers will choose between these with equal probability. But then IIA implies that the probability of each mode is  $\frac{1}{3}$ ; therefore, the fraction of commuters taking a car would fall from  $\frac{1}{2}$  to  $\frac{1}{3}$ , a result that is not very realistic. This example is admittedly extreme—in practice, we would lump the blue bus and red bus into the same category, provided there are no other differences—but it indicates that the IIA property can impose unwanted restrictions in the conditional logit model.

Hausman and McFadden (1984) offer tests of the IIA assumption based on the observation that, if the conditional logit model is true,  $\beta$  can be consistently estimated by conditional logit by focusing on any subset of alternatives. They apply the Hausman principle that compares the estimate of  $\beta$  using all alternatives to the estimate using a subset of alternatives.

Several models that relax the IIA assumption have been suggested. In the context of the random utility model the IIA assumption comes about because the  $\{a_{ij}: j=0, 1, \ldots, J\}$  are assumed to be independent Wiebull random variables. A more flexible assumption is that  $\mathbf{a}_i$  has a multivariate normal distribution with arbitrary correlations between  $a_{ij}$  and  $a_{ih}$ , all  $j \neq h$ . The resulting model is called the **multinomial probit model**. [In keeping with the spirit of the previous names, **conditional probit model** is a better name, which is used by Hausman and Wise (1978) but not by many others.]

Theoretically, the multinomial probit model is attractive, but it has some practical limitations. The response probabilities are very complicated, involving a (J+1)-dimensional integral. This complexity not only makes it difficult to obtain the partial effects on the response probabilities, but also makes maximum likelihood infeasible for more than about five alternatives. For details, see Maddala (1983, Chapter 3) and Amemiya (1985, Chapter 9). Hausman and Wise (1978) contain an application to transportation mode for three alternatives.

Recent advances on estimation through simulation make multinomial probit estimation feasible for many alternatives. See Hajivassilou and Ruud (1994) and Keane (1993) for recent surveys of simulation estimation. Keane and Moffitt (1998) apply simulation methods to structural multinomial response models, where the econometric model is obtained from utility maximization subject to constraints. Keane and Moffitt study the tax effects of labor force participation allowing for participation in multiple welfare programs.

{512}------------------------------------------------

A different approach to relaxing IIA is to specify a **hierarchical model**. The most popular of these is called the **nested logit model**. McFadden (1984) gives a detailed treatment of these and other models; here we illustrate the basic approach where there are only two hierarchies.

Suppose that the total number of alternatives can be put into S groups of similar alternatives, and let  $G_s$  denote the number of alternatives within group s. Thus the first hierarchy corresponds to which of the S groups y falls into, and the second corresponds to the actual alternative within each group. McFadden (1981) studied the model

$$\mathbf{P}(y \in G_s \mid \mathbf{x}) = \left\{ \alpha_s \left[ \sum_{j \in G_s} \exp(\rho_s^{-1} \mathbf{x}_j \boldsymbol{\beta}) \right]^{\rho_s} \right\} / \left\{ \sum_{r=1}^S \alpha_r \left[ \sum_{j \in G_r} \exp(\rho_r^{-1} \mathbf{x}_j \boldsymbol{\beta}) \right]^{\rho_r} \right\}$$
(15.84)

and

$$P(y = j \mid y \in G_s, \mathbf{x}) = \exp(\rho_s^{-1} \mathbf{x}_j \boldsymbol{\beta}) / \left[ \sum_{h \in G_s} \exp(\rho_s^{-1} \mathbf{x}_h \boldsymbol{\beta}) \right]$$
(15.85)

where equation (15.84) is defined for s = 1, 2, ..., S while equation (15.85) is defined for  $j \in G_s$  and s = 1, 2, ..., S; of course, if  $j \notin G_s$ ,  $P(y = j | y \in G_s, \mathbf{x}) = 0$ . This model requires a normalization restriction, usually  $\alpha_1 = 1$ . Equation (15.84) gives the probability that the outcome is in group s (conditional on  $\mathbf{x}$ ); then, conditional on  $y \in G_s$ , equation (15.85) gives the probability of choosing alternative j within  $G_s$ . The response probability  $P(y = j | \mathbf{x})$ , which is ultimately of interest, is obtained by multiplying equations (15.84) and (15.85). This model can be derived by specifying a particular joint distribution for  $\mathbf{a}_i$  in equation (15.79); see Amemiya (1985, p. 303).

Equation (15.85) implies that, conditional on choosing group s, the response probabilities take a conditional logit form with parameter vector  $\rho_s^{-1}\boldsymbol{\beta}$ . This suggests a natural two-step estimation procedure. First, estimate  $\lambda_s \equiv \rho_s^{-1}\boldsymbol{\beta}$ , s = 1, 2, ..., S, by applying conditional logit analysis separately to each of the groups. Then, plug the  $\hat{\lambda}_s$  into equation (15.84) and estimate  $\alpha_s$ , s = 2, ..., S and  $\rho_s$ , s = 1, ..., S by maximizing the log-likelihood function

$$\sum_{i=1}^{N} \sum_{s=1}^{S} 1[y_i \in G_s] \log[q_s(\mathbf{x}_i; \hat{\boldsymbol{\lambda}}, \boldsymbol{\alpha}, \boldsymbol{\rho})]$$

where  $q_s(\mathbf{x}; \boldsymbol{\lambda}, \boldsymbol{a}, \boldsymbol{\rho})$  is the probability in equation (15.84) with  $\boldsymbol{\lambda}_s = \rho_s^{-1} \boldsymbol{\beta}$ . This two-step conditional MLE is consistent and  $\sqrt{N}$ -asymptotically normal under general

{513}------------------------------------------------

conditions, but the asymptotic variance needs to be adjusted for the first-stage estimation of the  $\lambda_s$ ; see Chapters 12 and 13 for more on two-step estimators.

Of course, we can also use full maximum likelihood. The log likelihood for observation *i* can be written as

$$\ell_i(\boldsymbol{\beta}, \boldsymbol{\alpha}, \boldsymbol{\rho}) = \sum_{s=1}^{S} (1[y_i \in G_s] \{ \log[q_s(\mathbf{x}_i; \boldsymbol{\beta}, \boldsymbol{\alpha}, \boldsymbol{\rho})] + 1[y_i = j] \log[p_{sj}(\mathbf{x}_i; \boldsymbol{\beta}, \rho_s)] \}) \quad (15.86)$$

where  $q_s(\mathbf{x}_i; \boldsymbol{\beta}, \boldsymbol{\alpha}, \boldsymbol{\rho})$  is the probability in equation (15.84) and  $p_{sj}(\mathbf{x}_i; \boldsymbol{\beta}, \rho_s)$  is the probability in equation (15.85). The regularity conditions for MLE are satisfied under weak assumptions.

When  $\alpha_s = 1$  and  $\rho_s = 1$  for all s, the nested logit model reduces to the conditional logit model. Thus, a test of IIA (as well as the other assumptions underlying the CL model) is a test of H<sub>0</sub>:  $\alpha_2 = \cdots = \alpha_S = \rho_1 = \cdots = \rho_S = 1$ . McFadden (1987) suggests a score test, which only requires estimation of the conditional logit model.

Often special cases of the model are used, such as setting each  $\alpha_s$  to unity and estimating the  $\rho_s$ . In his study of community choice and type of dwelling within a community, McFadden (1978) imposes this restriction along with  $\rho_s = \rho$  for all s, so that the model has only one more parameter than the conditional logit model. This approach allows for correlation among the  $a_j$  for j belonging to the same community group, but the correlation is assumed to be the same for all communities.

Higher-level nested-logit models are covered in McFadden (1984) and Amemiya (1985, Chapter 9).