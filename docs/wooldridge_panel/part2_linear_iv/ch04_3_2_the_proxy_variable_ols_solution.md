# The Proxy Variable-OLS Solution

> Pages: 79-83

Omitted variables bias can be eliminated, or at least mitigated, if a **proxy variable** is available for the unobserved variable q. There are two formal requirements for a proxy variable for q. The first is that the proxy variable should be **redundant** (sometimes called **ignorable**) in the structural equation. If z is a proxy variable for q, then the most natural statement of redundancy of z in equation (4.18) is

$$E(y \mid \mathbf{x}, q, z) = E(y \mid \mathbf{x}, q) \tag{4.25}$$

Condition (4.25) is easy to interpret: z is irrelevant for explaining y, in a conditional mean sense, once  $\mathbf{x}$  and q have been controlled for. This assumption on a proxy variable is virtually always made (sometimes only implicitly), and it is rarely controversial: the only reason we bother with z in the first place is that we cannot get data on q. Anyway, we cannot get very far without condition (4.25). In the wage-education example, let q be ability and z be IQ score. By definition it is ability that affects wage: IQ would not matter if true ability were known.

Condition (4.25) is somewhat stronger than needed when unobservables appear additively as in equation (4.18); it suffices to assume that v in equation (4.19) is simply uncorrelated with z. But we will focus on condition (4.25) because it is natural, and because we need it to cover models where q interacts with some observed covariates.

The second requirement of a good proxy variable is more complicated. We require that the correlation between the omitted variable q and each  $x_j$  be zero once we partial out z. This is easily stated in terms of a linear projection:

$$L(q | 1, x_1, \dots, x_K, z) = L(q | 1, z)$$
(4.26)

It is also helpful to see this relationship in terms of an equation with an unobserved error. Write q as a linear function of z and an error term as

{80}------------------------------------------------

$$q = \theta_0 + \theta_1 z + r \tag{4.27}$$

where, by definition, EðrÞ ¼ 0 and Covðz;rÞ ¼ 0 because y<sup>0</sup> þ y1z is the linear projection of q on 1, z. If z is a reasonable proxy for q, y<sup>1</sup> 0 0 (and we usually think in terms of y<sup>1</sup> > 0). But condition (4.26) assumes much more: it is equivalent to

$$Cov(x_j, r) = 0, j = 1, 2, ..., K$$

This condition requires z to be closely enough related to q so that once it is included in equation (4.27), the xj are not partially correlated with q.

Before showing why these two proxy variable requirements do the trick, we should head off some possible confusion. The definition of proxy variable here is not universal. While a proxy variable is always assumed to satisfy the redundancy condition (4.25), it is not always assumed to have the second property. In Chapter 5 we will use the notion of an indicator of q, which satisfies condition (4.25) but not the second proxy variable assumption.

To obtain an estimable equation, replace q in equation (4.19) with equation (4.27) to get

$$y = (\beta_0 + \gamma \theta_0) + \beta_1 x_1 + \dots + \beta_K x_K + \gamma \theta_1 z + (\gamma r + v)$$

$$\tag{4.28}$$

Under the assumptions made, the composite error term u 1gr þ v is uncorrelated with xj for all j; redundancy of z in equation (4.18) means that z is uncorrelated with v and, by definition, z is uncorrelated with r. It follows immediately from Theorem 4.1 that the OLS regression y on 1; x1; x2; ... ; xK , z produces consistent estimators of ðb<sup>0</sup> þ gy0Þ; b1; b2; ... ; b<sup>K</sup> , and gy1. Thus, we can estimate the partial effect of each of the xj in equation (4.18) under the proxy variable assumptions.

When z is an imperfect proxy, then r in equation (4.27) is correlated with one or more of the xj. Generally, when we do not impose condition (4.26) and write the linear projection as

$$q = \theta_0 + \rho_1 x_1 + \dots + \rho_K x_K + \theta_1 z + r$$

the proxy variable regression gives plim ^b<sup>j</sup> <sup>¼</sup> <sup>b</sup><sup>j</sup> <sup>þ</sup> grj. Thus, OLS with an imperfect proxy is inconsistent. The hope is that the r<sup>j</sup> are smaller in magnitude than if z were omitted from the linear projection, and this can usually be argued if z is a reasonable proxy for q.

If including z induces substantial collinearity, it might be better to use OLS without the proxy variable. However, in making these decisions we must recognize that including z reduces the error variance if y<sup>1</sup> 0 0: Varðgr þ vÞ < Varðgq þ vÞ because VarðrÞ < VarðqÞ, and v is uncorrelated with both r and q. Including a proxy variable can actually reduce asymptotic variances as well as mitigate bias.


{81}------------------------------------------------

Example 4.3 (Using IQ as a Proxy for Ability): We apply the proxy variable method to the data on working men in NLS80.RAW, which was used by Blackburn and Neumark (1992), to estimate the structural model

$$\log(wage) = \beta_0 + \beta_1 exper + \beta_2 tenure + \beta_3 married$$
$$+ \beta_4 south + \beta_5 urban + \beta_6 black + \beta_7 educ + \gamma abil + v$$
 (4.29)

where exper is labor market experience, married is a dummy variable equal to unity if married, south is a dummy variable for the southern region, urban is a dummy variable for living in an SMSA, black is a race indicator, and educ is years of schooling. We assume that IQ satisfies the proxy variable assumptions: in the linear projection abil ¼ y<sup>0</sup> þ y1IQ þ r, where r has zero mean and is uncorrelated with IQ, we also assume that r is uncorrelated with experience, tenure, education, and other factors appearing in equation (4.29). The estimated equations without and with IQ are

$$\log(\hat{w}age) = 5.40 + .014 \ exper + .012 \ tenure + .199 \ married \ (0.11) \ (.003) \ (.002) \ (.039)$$

$$- .091 \ south + .184 \ urban - .188 \ black + .065 \ educ \ (.026) \ (.027) \ (.038) \ (.006)$$
 $N = 935, \quad R^2 = .253$ 
 $\log(\hat{w}age) = 5.18 + .014 \ exper + .011 \ tenure + .200 \ married \ (0.13) \ (.003) \ (.002) \ (.039)$ 

$$- .080 \ south + .182 \ urban - .143 \ black + .054 \ educ \ (.026) \ (.027) \ (.039) \ (.007)$$

$$+ .0036 \ IQ \ (.0010)$$
 $N = 935, \quad R^2 = .263$ 

Notice how the return to schooling has fallen from about 6.5 percent to about 5.4 percent when IQ is added to the regression. This is what we expect to happen if ability and schooling are (partially) positively correlated. Of course, these are just the findings from one sample. Adding IQ explains only one percentage point more of the variation in logðwageÞ, and the equation predicts that 15 more IQ points (one standard deviation) increases wage by about 5.4 percent. The standard error on the return to education has increased, but the 95 percent confidence interval is still fairly tight.

{82}------------------------------------------------

Often the outcome of the dependent variable from an earlier time period can be a useful proxy variable.

Example 4.4 (Effects of Job Training Grants on Worker Productivity): The data in JTRAIN1.RAW are for 157 Michigan manufacturing firms for the years 1987, 1988, and 1989. These data are from Holzer, Block, Cheatham, and Knott (1993). The goal is to determine the effectiveness of job training grants on firm productivity. For this exercise, we use only the 54 firms in 1988 which reported nonmissing values of the scrap rate (number of items out of 100 that must be scrapped). No firms were awarded grants in 1987; in 1988, 19 of the 54 firms were awarded grants. If the training grant has the intended effect, the average scrap rate should be lower among firms receiving a grant. The problem is that the grants were not randomly assigned: whether or not a firm received a grant could be related to other factors unobservable to the econometrician that affect productivity. In the simplest case, we can write (for the 1988 cross section)

$$\log(scrap) = \beta_0 + \beta_1 grant + \gamma q + v$$

where v is orthogonal to grant but q contains unobserved productivity factors that might be correlated with grant, a binary variable equal to unity if the firm received a job training grant. Since we have the scrap rate in the previous year, we can use logðscrap1Þ as a proxy variable for q:

$$q = \theta_0 + \theta_1 \log(scrap_{-1}) + r$$

where r has zero mean and, by definition, is uncorrelated with logðscrap1Þ. We hope that r has no or little correlation with grant. Plugging in for q gives the estimable model

$$\log(scrap) = \delta_0 + \beta_1 grant + \gamma \theta_1 \log(scrap_{-1}) + r + v$$

From this equation, we see that b<sup>1</sup> measures the proportionate difference in scrap rates for two firms having the same scrap rates in the previous year, but where one firm received a grant and the other did not. This is intuitively appealing. The estimated equations are

$$\log(s\hat{c}rap) = .409 + .057 \ grant$$

$$(.240) \quad (.406)$$

$$N = 54, \qquad R^2 = .0004$$

$$\log(s\hat{c}rap) = .021 - .254 \ grant + .831 \ \log(scrap_{-1})$$

$$(.089) \quad (.147) \qquad (.044)$$

$$N = 54, \qquad R^2 = .873$$

{83}------------------------------------------------

Without the lagged scrap rate, we see that the grant appears, if anything, to reduce productivity (by increasing the scrap rate), although the coefficient is statistically insignificant. When the lagged dependent variable is included, the coefficient on grant changes signs, becomes economically large—firms awarded grants have scrap rates about 25.4 percent less than those not given grants—and the effect is significant at the 5 percent level against a one-sided alternative. [The more accurate estimate of the percentage effect is 100 ½expð:254Þ 1¼22:4%; see Problem 4.1(a).]

We can always use more than one proxy for xK . For example, it might be that Eðq j x; z1; z2Þ ¼ Eðq j z1; z2Þ ¼ y<sup>0</sup> þ y1z<sup>1</sup> þ y2z2, in which case including both z<sup>1</sup> and z<sup>2</sup> as regressors along with x1; ... ; xK solves the omitted variable problem. The weaker condition that the error r in the equation q ¼ y<sup>0</sup> þ y1z<sup>1</sup> þ y2z<sup>2</sup> þ r is uncorrelated with x1; ... ; xK also suffices.

The data set NLS80.RAW also contains each man's score on the knowledge of the world of work (KWW ) test. Problem 4.11 asks you to reestimate equation (4.29) when KWW and IQ are both used as proxies for ability.