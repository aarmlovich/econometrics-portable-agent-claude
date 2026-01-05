# Appendix 13A

> Pages: 429-432

In this appendix we cover some important properties of conditional distributions and conditional densities. Billingsley (1979) is a good reference for this material. For random vectors  $\mathbf{y} \in \mathscr{Y} \subset \mathbb{R}^G$  and  $\mathbf{x} \in \mathscr{X} \subset \mathbb{R}^K$ , the **conditional distribution** of  $\mathbf{y}$  given  $\mathbf{x}$  always exists and is denoted  $\mathbf{D}(\mathbf{y} | \mathbf{x})$ . For each  $\mathbf{x}$  this distribution is a probability measure and completely describes the behavior of the random vector  $\mathbf{y}$  once  $\mathbf{x}$  takes on a particular value. In econometrics, we almost always assume that this distribution is described by a **conditional density**, which we denote by  $p(\cdot | \mathbf{x})$ . The density is with respect to a **measure** defined on the support  $\mathscr{Y}$  of  $\mathbf{y}$ . A conditional density makes sense only when this measure does not change with the value of  $\mathbf{x}$ . In practice, this assumption is not very restrictive, as it means that the nature of  $\mathbf{y}$  is not dramatically different for different values of  $\mathbf{x}$ . Let  $\mathbf{v}$  be this measure on  $\mathbb{R}^J$ . If  $\mathbf{D}(\mathbf{y} | \mathbf{x})$  is discrete,  $\mathbf{v}$  can be the counting measure and all integrals are sums. If  $\mathbf{D}(\mathbf{y} | \mathbf{x})$  is absolutely **continuous**, then  $\mathbf{v}$  is the familiar Lebesgue measure appearing in elementary integration theory. In some cases,  $\mathbf{D}(\mathbf{y} | \mathbf{x})$  has both discrete and continuous characteristics.

The important point is that all conditional probabilities can be obtained by integration:

$$P(\mathbf{y} \in \mathcal{A} \mid \mathbf{x} = x) = \int_{A} p(y \mid x) v(dy)$$

where y is the dummy argument of integration. When  $\mathbf{y}$  is discrete, taking on the values  $y_1, y_2, \ldots$ , then  $p(\cdot | x)$  is a probability mass function and  $P(\mathbf{y} = y_j | \mathbf{x} = x) = p(y_j | x), j = 1, 2, \ldots$ 

Suppose that f and g are nonnegative functions on  $\mathbb{R}^M$ , and define  $\mathcal{G}_f \equiv \{z \in \mathbb{R}^M \colon f(z) > 0\}$ . Assume that

$$1 = \int_{\mathscr{S}_f} f(z) \nu(dz) \ge \int_{\mathscr{S}_f} g(z) \nu(dz)$$
 (13.63)

{430}------------------------------------------------

where n is a measure on R<sup>M</sup>. The equality in expression (13.63) implies that f is a density on R<sup>M</sup>, while the inequality holds if g is also a density on R<sup>M</sup>. An important result is that

$$\mathscr{I}(f;g) \equiv \int_{\mathscr{S}_f} \log[f(z)/g(z)] f(z) \nu(\mathrm{d}z) \ge 0$$
 (13.64)

[Note that Iðf ; gÞ ¼ y is allowed; one case where this result can occur is fðzÞ > 0 but gðzÞ ¼ 0 for some z. Also, the integrand is not defined when fðzÞ ¼ gðzÞ ¼ 0, but such values of z have no effect because the integrand receives zero weight in the integration.] The quantity Iðf ; gÞ is called the Kullback-Leibler information criterion (KLIC). Another way to state expression (13.64) is

$$\mathbb{E}\{\log[f(\mathbf{z})]\} \ge \mathbb{E}\{\log[g(\mathbf{z})]\}\tag{13.65}$$

where z A Z HR<sup>M</sup> is a random vector with density f.

Conditional MLE relies on a conditional version of inequality (13.63):

property CD.1: Let y A Y HR<sup>G</sup> and x A X HR<sup>K</sup> be random vectors. Let pð j Þ denote the conditional density of y given x. For each x, let YðxÞ 1 fy: pðy j xÞ > 0g be the conditional support of y, and let n be a measure that does not depend on x. Then for any other function gð j xÞ b 0 such that

$$1 = \int_{\mathscr{Y}(\mathbf{x})} p(y \mid \mathbf{x}) \nu(dy) \ge \int_{\mathscr{Y}(\mathbf{x})} g(y \mid \mathbf{x}) \nu(dy)$$

the conditional KLIC is nonnegative:

$$\mathcal{I}_{\mathbf{x}}(p;g) \equiv \int_{\mathcal{Y}(\mathbf{x})} \log[p(y \mid \mathbf{x})/g(y \mid \mathbf{x})]p(y \mid \mathbf{x})\nu(\mathrm{d}y) \ge 0$$

That is,

$$\mathbb{E}\{\log[p(\mathbf{y} \mid \mathbf{x})] \mid \mathbf{x}\} \ge \mathbb{E}\{\log[g(\mathbf{y} \mid \mathbf{x})] \mid \mathbf{x}\}$$

for any x A X. The proof uses the conditional Jensen's inequality (Property CE.7 in Chapter 2). See Manski (1988, Section 5.1).

property CD.2: For random vectors y, x, and z, let pðyj x; zÞ be the conditional density of y given ðx; zÞ and let pðx j zÞ denote the conditional density of x given z. Then the density of ðy; xÞ given z is

$$p(y, x | \mathbf{z}) = p(y | x, \mathbf{z})p(x | \mathbf{z})$$

where the script variables are placeholders.


{431}------------------------------------------------

property CD.3: For random vectors y, x, and z, let pðyj x; zÞ be the conditional density of y given ðx; zÞ, let pðyj xÞ be the conditional density of y given x, and let pðz j xÞ denote the conditional density of z given x with respect to the measure nðdzÞ. Then

$$p(y \mid \mathbf{x}) = \int_{\mathscr{Z}} p(y \mid \mathbf{x}, z) p(z \mid \mathbf{x}) v(dz)$$

In other words, we can obtain the density of y given x by integrating the density of y given the larger conditioning set, ðx; zÞ, against the density of z given x.

property CD.4: Suppose that the random variable, u, with cdf, F, is independent of the random vector x. Then, for any function aðxÞ of x,

$$P[u \le a(\mathbf{x}) \,|\, \mathbf{x}] = F[a(\mathbf{x})].$$

{432}------------------------------------------------

In Chapter 8 we saw how the generalized method of moments (GMM) approach to estimation can be applied to multiple-equation linear models, including systems of equations, with exogenous or endogenous explanatory variables, and to panel data models. In this chapter we extend GMM to nonlinear estimation problems. This setup allows us to treat various efficiency issues that we have glossed over until now. We also cover the related method of minimum distance estimation. Because the asymptotic analysis has many features in common with Chapters 8 and 12, the analysis is not quite as detailed here as in previous chapters. A good reference for this material, which fills in most of the gaps left here, is Newey and McFadden (1994).