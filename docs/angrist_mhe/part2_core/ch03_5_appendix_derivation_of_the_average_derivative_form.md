# Appendix: Derivation of the average derivative formula

> Pages: 96-99

Begin with the regression of  $Y_i$  on  $S_i$ :

$$\frac{Cov(\mathbf{y}_i, \mathbf{s}_i)}{V(\mathbf{s}_i)} = \frac{E[h(\mathbf{s}_i)(\mathbf{s}_i - E[\mathbf{s}_i])]}{E[\mathbf{s}_i(\mathbf{s}_i - E[\mathbf{s}_i])]}.$$

<span id="page-96-0"></span><sup>&</sup>lt;sup>30</sup>Yule's first applied paper on the poor laws was published in 1895 in the *Economic Journal*, where Pischke is proud to serve as co-editor. The theory of multiple regression that goes along with this appears in Yule (1897).

{97}------------------------------------------------

Let 1 = lim <sup>t</sup>!1 h (t). By the fundamental theorem of calculus, we have:

$$h(\mathbf{s}_i) = \kappa_{-\infty} + \int_{-\infty}^{\mathbf{s}_i} h'(t) dt.$$

Substituting for h(si), the numerator becomes

$$E[h(\mathbf{s}_i)(\mathbf{s}_i - E[\mathbf{s}_i])] = \int_{-\infty}^{+\infty} \int_{-\infty}^{s} h'(t) \left(s - E[\mathbf{s}_i]\right) g(s) dt ds$$

where g(s) is the density of s<sup>i</sup> at s. Reversing the order of integration, we have

$$E[h(\mathbf{s}_i)(\mathbf{s}_i - E[\mathbf{s}_i])] = \int_{-\infty}^{+\infty} h'(t) \int_t^{+\infty} (s - E[\mathbf{s}_i])g(s)dsdt.$$

The inner integral is easily seen to be equal to <sup>t</sup> fE[s<sup>i</sup> js<sup>i</sup> t] E[s<sup>i</sup> js<sup>i</sup> < t]gfP(s<sup>i</sup> t)[1 P(s<sup>i</sup> t)g, which is clearly non-negative. Setting s<sup>i</sup> =y<sup>i</sup> , the denominator can similarly be shown to be the integral of these weights. We therefore have a weighted average derivative representation of the bivariate regression coe¢ cient, Cov(yi;si) V (si) ; equation [\(3.3.8\)](#page-73-0) in the text. A similar formula for a regression with covariates, X<sup>i</sup> , is derived in the appendix to Angrist and Krueger (1999).

{98}------------------------------------------------

# Chapter 4

# Instrumental Variables in Action:

# Sometimes You Get What You Need

Anything that happens, happens.

Anything that, in happening, causes something else to happen,

causes something else to happen.

Anything that, in happening,

causes itself to happen again, happens again.

It doesnít necessarily do it in chronological order, though.

Douglas Adams, Mostly Harmless (1995)

Two things distinguish the discipline of Econometrics from our older sister Öeld of Statistics. One is a lack of shyness about causality. Causal inference has always been the name of the game in applied econometrics. Statistician Paul Holland (1986) cautions that there can be ìno causation without manipulation,î a maxim that would seem to rule out causal inference from non-experimental data. Less thoughtful observers fall back on the truism that ìcorrelation is not causality.î Like most people who work with data for a living, we believe that correlation can sometimes provide pretty good evidence of a causal relation, even when the variable of interest has not been manipulated by a researcher or experimenter. [1](#page-98-0)

The second thing that distinguishes us from most statisticiansó and indeed most other social scientistsó is an arsenal of statistical tools that grew out of early econometric research on the problem of how to estimate the parameters in a system of linear simultaneous equations. The most powerful weapon in this arsenal is the method of Instrumental Variables (IV), the subject of this chapter. As it turns out, IV does more than allow us to consistently estimate the parameters in a system of simultaneous equations, though it allows us

<span id="page-98-0"></span><sup>1</sup>Recent years have seen an increased willingness by statisticians to discuss statistical models for observational data in an explicitly causal framework; see, for example, Freedmanís (2005) review.

{99}------------------------------------------------

to do that as well.

Studying agricultural markets in the 1920s, the father and son research team of Phillip and Sewall Wright were interested in a challenging problem of causal inference: how to estimate the slope of supply and demand curves when observed data on prices and quantities are determined by the intersection of these two curves. In other words, equilibrium prices and quantitiesó the only ones we get to observeó solve these two stochastic equations at the same time. Upon which curve, therefore, does the observed scatterplot of prices and quantities lie? The fact that population regression coe¢ cients do not capture the slope of any one equation in a set of simultaneous equations had been understood by Phillip Wright for some time. The IV method, Örst laid out in Wright (1928), solves the statistical simultaneous equations problem by using variables that appear in one equation to shift this equation and trace out the other. The variables that do the shifting came to be known as instrumental variables (Reiersol, 1941).

In a separate line of inquiry, IV methods were pioneered to solve the problem of bias from measurement error in regression models[2](#page-99-0) . One of the most important results in the statistical theory of linear models is that a regression coe¢ cient is biased towards zero when the regressor of interest is measured with random errors (to see why, imagine the regressor contains only random error; then it will be uncorrelated with the dependent variable, and hence the regression of y<sup>i</sup> on this variable will be zero). Instrumental variables methods can be used to eliminate this sort of bias.

Simultaneous equations models (SEMs) have been enormously important in the history of econometric thought. At the same time, few of todayís most ináuential applied papers rely on an orthodox SEM framework, though the technical language used to discuss IV still comes from this framework. Today, we are more likely to Önd IV used to address measurement error problems than to estimate the parameters of an SEM. Undoubtedly, however, the most important contemporary use of IV is to solve the problem of omitted variables bias. IV solves the problem of missing or unknown control variables, much as a randomized trial obviates the need for extensive controls in a regression.[3](#page-99-1)