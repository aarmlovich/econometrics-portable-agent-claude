# Random or Fixed Effects?

> Pages: 263-266

The basic unobserved effects model (UEM) can be written, for a randomly drawn cross section observation i, as

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + c_i + u_{it}, \qquad t = 1, 2, \dots, T$$
 (10.11)

where xit is 1 K and can contain observable variables that change across t but not i, variables that change across i but not t, and variables that change across i and t. In addition to unobserved effect, there are many other names given to ci in applications: unobserved component, latent variable, and unobserved heterogeneity are common. If i indexes individuals, then ci is sometimes called an individual effect or individual heterogeneity; analogous terms apply to families, firms, cities, and other cross-sectional units. The uit are called the idiosyncratic errors or idiosyncratic disturbances because these change across t as well as across i.

Especially in methodological papers, but also in applications, one often sees a discussion about whether ci will be treated as a random effect or a fixed effect. Originally, such discussions centered on whether ci is properly viewed as a random variable or as a parameter to be estimated. In the traditional approach to panel data models, ci is called a ''random effect'' when it is treated as a random variable and a ''fixed effect'' when it is treated as a parameter to be estimated for each cross section observation i. Our view is that discussions about whether the ci should be treated as

{264}------------------------------------------------

random variables or as parameters to be estimated are wrongheaded for microeconometric panel data applications. With a large number of random draws from the cross section, it almost always makes sense to treat the unobserved effects, ci, as random draws from the population, along with yit and xit. This approach is certainly appropriate from an omitted variables or neglected heterogeneity perspective. As our discussion in Section 10.1 suggests, the key issue involving ci is whether or not it is uncorrelated with the observed explanatory variables xit, t ¼ 1; 2; ... ; T. Mundlak (1978) made this argument many years ago, and it still is persuasive.

In modern econometric parlance, ''random effect'' is synonymous with zero correlation between the observed explanatory variables and the unobserved effect: Covðxit; ciÞ ¼ 0, t ¼ 1; 2; ... ; T. [Actually, a stronger conditional mean independence assumption, Eðci j xi1; ... ; xiT Þ ¼ EðciÞ, will be needed to fully justify statistical inference; more on this subject in Section 10.4.] In applied papers, when ci is referred to as, say, an ''individual random effect,'' then ci is probably being assumed to be uncorrelated with the xit.

In microeconometric applications, the term ''fixed effect'' does not usually mean that ci is being treated as nonrandom; rather, it means that one is allowing for arbitrary correlation between the unobserved effect ci and the observed explanatory variables xit. So, if ci is called an ''individual fixed effect'' or a ''firm fixed effect,'' then, for practical purposes, this terminology means that ci is allowed to be correlated with xit. In this book, we avoid referring to ci as a random effect or a fixed effect. Instead, we will refer to ci as unobserved effect, unobserved heterogeneity, and so on. Nevertheless, later we will label two different estimation methods random effects estimation and fixed effects estimation. This terminology is so ingrained that it is pointless to try to change it now.

# 10.2.2 Strict Exogeneity Assumptions on the Explanatory Variables

Traditional unobserved components panel data models take the xit as fixed. We will never assume the xit are nonrandom because potential feedback from yit to xis for s > t needs to be addressed explicitly.

In Chapter 7 we discussed strict exogeneity assumptions in panel data models that did not explicitly contain unobserved effects. We now provide strict exogeneity assumptions for models with unobserved effects.

In Section 10.1 we stated the strict exogeneity assumption in terms of zero correlation. For inference and efficiency discussions, we need to state the strict exogeneity assumption in terms of conditional expectations, and this statement also gives the assumption a clear meaning. With an unobserved effect, the most revealing form of the strict exogeneity assumption is

{265}------------------------------------------------

$$E(y_{it} | \mathbf{x}_{i1}, \mathbf{x}_{i2}, \dots, \mathbf{x}_{iT}, c_i) = E(y_{it} | \mathbf{x}_{it}, c_i) = \mathbf{x}_{it}\boldsymbol{\beta} + c_i$$

$$(10.12)$$

for t ¼ 1; 2; ... ; T. The second equality is the functional form assumption on Eðyit j xit; ciÞ. It is the first equality that gives the strict exogeneity its interpretation. It means that, once xit and ci are controlled for, xis has no partial effect on yit for s 0t.

When assumption (10.12) holds, we say that the fxit: t ¼ 1; 2; ... ; Tg are strictly exogenous conditional on the unobserved effect ci. Assumption (10.12) and the corresponding terminology were introduced and used by Chamberlain (1982). We will explicitly cover Chamberlain's approach to estimating unobserved effects models in the next chapter, but his manner of stating assumptions is instructive even for traditional panel data analysis.

Assumption (10.12) restricts how the expected value of yit can depend on explanatory variables in other time periods, but it is more reasonable than strict exogeneity without conditioning on the unobserved effect. Without conditioning on an unobserved effect, the strict exogeneity assumption is

$$E(y_{it} | \mathbf{x}_{i1}, \mathbf{x}_{i2}, \dots, \mathbf{x}_{iT}) = E(y_{it} | \mathbf{x}_{it}) = \mathbf{x}_{it}\boldsymbol{\beta}$$

$$(10.13)$$

t ¼ 1; ... ; T. To see that assumption (10.13) is less likely to hold than assumption (10.12), first consider an example. Suppose that yit is output of soybeans for farm i during year t, and xit contains capital, labor, materials (such as fertilizer), rainfall, and other observable inputs. The unobserved effect, ci, can capture average quality of land, managerial ability of the family running the farm, and other unobserved, timeconstant factors. A natural assumption is that, once current inputs have been controlled for along with ci, inputs used in other years have no effect on output during the current year. However, since the optimal choice of inputs in every year generally depends on ci, it is likely that some partial correlation between output in year t and inputs in other years will exist if ci is not controlled for: assumption (10.12) is reasonable while assumption (10.13) is not.

More generally, it is easy to see that assumption (10.13) fails whenever assumption (10.12) holds and the expected value of ci depends on ðx<sup>i</sup>1; ... ; xiT Þ. From the law of iterated expectations, if assumption (10.12) holds, then

$$E(y_{it} | \mathbf{x}_{i1}, \dots, \mathbf{x}_{iT}) = \mathbf{x}_{it} \boldsymbol{\beta} + E(c_i | \mathbf{x}_{i1}, \dots, \mathbf{x}_{iT})$$

and so assumption (10.13) fails if Eðci j x<sup>i</sup>1; ... ; xiT Þ 0EðciÞ. In particular, assumption (10.13) fails if ci is correlated with any of the xit.

Given equation (10.11), the strict exogeneity assumption can be stated in terms of the idiosyncratic errors as

$$E(u_{it} | \mathbf{x}_{i1}, \dots, \mathbf{x}_{iT}, c_i) = 0, \qquad t = 1, 2, \dots, T$$
 (10.14)

{266}------------------------------------------------

This assumption, in turn, implies that explanatory variables in each time period are uncorrelated with the idiosyncratic error in each time period:

$$E(\mathbf{x}'_{is}u_{it}) = \mathbf{0}, \qquad s, t = 1, \dots, T$$
 (10.15)

This assumption is much stronger than assuming zero contemporaneous correlation: Eðx<sup>0</sup> ituitÞ ¼ 0, t ¼ 1; ... ; T. Nevertheless, assumption (10.15) does allow arbitary correlation between ci and xit for all t, something we ruled out in Section 7.8. Later, we will use the fact that assumption (10.14) implies that uit and ci are uncorrelated.

For examining consistency of panel data estimators, the zero correlation assumption (10.15) generally suffices. Further, assumption (10.15) is often the easiest way to think about whether strict exogeneity is likely to hold in a particular application. But standard forms of statistical inference, as well as the efficiency properties of standard estimators, rely on the stronger conditional mean formulation in assumption (10.14). Therefore, we focus on assumption (10.14).