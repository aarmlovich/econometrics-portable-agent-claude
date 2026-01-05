# Saturated Models, Main E§ects, and Other Regression Talk

> Pages: 51-53

We often discuss regression models using terms like saturated and main e§ects. These terms originate in an experimentalist tradition that uses regression to model discrete treatment-type variables. This language is now used more widely in many Öelds, however, including applied econometrics. For readers unfamiliar with these terms, this section provides a brief review.

Saturated regression models are regression models with discrete explanatory variables, where the model includes a separate parameter for all possible values taken on by the explanatory variables. For example, when working with a single explanatory variable indicating whether a worker is a college graduate, the model is saturated by including a single dummy for college graduates and a constant. We can also saturate when the regressor takes on many values. Suppose, for example, that s<sup>i</sup> = 0; 1; 2; :::; . A saturated regression model for s<sup>i</sup> is

$$Y_i = \beta_0 + \beta_1 d_{1i} + \beta_2 d_{2i} + \dots + \beta_{\tau} d_{\tau i} + \varepsilon_i,$$

where dji = 1[s<sup>i</sup> = j] is a dummy variable indicating schooling level-j, and <sup>j</sup> is said to be the jth-level schooling e§ect. Note that

$$\beta_j = E[Y_i | S_i = j] - E[Y_i | S_i = 0],$$

while <sup>0</sup> = E[y<sup>i</sup> js<sup>i</sup> = 0]: In practice, you can pick any value of s<sup>i</sup> for the reference group; a regression model is saturated as long as it has one parameter for every possible j in E[y<sup>i</sup> js<sup>i</sup> = j]: Saturated models Öt the

{52}------------------------------------------------

CEF perfectly because the CEF is linear in the dummy regressors used to saturate. This is an important special case of the regression-CEF theorem.

If there are two explanatory variables, say one dummy indicating college graduates and one dummy indicating sex, the model is saturated by including these two dummies, their product, and a constant. The coe¢ cients on the dummies are known as main e§ects, while the product is called an interaction term. This is not the only saturated parameterization; any set of indicators (dummies) that can be used to identify each value taken on by the covariates produces a saturated model. For example, an alternative saturated model includes dummies for male college graduates, male dropouts, female college graduates, and female dropouts, but no intercept.

Hereís some notation to make this more concrete. Let x1<sup>i</sup> indicate college graduates and x2<sup>i</sup> indicate women. The CEF given x1<sup>i</sup> and x2<sup>i</sup> takes on four values:

$$\begin{split} &E\left[\mathbf{Y}_{i} \middle| x_{1i} = 0, x_{2i} = 0\right], \\ &E\left[\mathbf{Y}_{i} \middle| x_{1i} = 1, x_{2i} = 0\right], \\ &E\left[\mathbf{Y}_{i} \middle| x_{1i} = 0, x_{2i} = 1\right], \\ &E\left[\mathbf{Y}_{i} \middle| x_{1i} = 1, x_{2i} = 1\right]. \end{split}$$

We can label these using the following scheme:

$$E[Y_{i}|x_{1i} = 0, x_{2i} = 0] = \alpha$$

$$E[Y_{i}|x_{1i} = 1, x_{2i} = 0] = \alpha + \beta$$

$$E[Y_{i}|x_{1i} = 0, x_{2i} = 1] = \alpha + \gamma$$

$$E[Y_{i}|x_{1i} = 1, x_{2i} = 1] = \alpha + \beta + \gamma + \delta.$$

Since there are four Greek letters and the CEF takes on four values, this parameterization does not restrict the CEF. It can be written in terms of Greek letters as

$$E[Y_i|x_{1i}, x_{2i}] = \alpha + \beta x_{1i} + \gamma x_{2i} + \delta(x_{1i}x_{2i}),$$

a parameterization with two main e§ects and one interaction term.[8](#page-52-0) The saturated regression equation becomes

$$Y_i = \alpha + \beta x_{1i} + \gamma x_{2i} + \delta(x_{1i}x_{2i}) + \varepsilon_i.$$

Finally, we can combine the multi-valued schooling variable with sex to produce a saturated model that

<span id="page-52-0"></span><sup>8</sup>With a third dummy variable in the model, say x3i, a saturated model includes 3 main e§ects, 3 second-order interaction terms fx1ix2i, x2ix3i; x1ix2ig and one third-order term, x1ix2ix3i.

{53}------------------------------------------------

has main e§ects for schooling, one main e§ect for sex, and sex-schooling interactions:

<span id="page-53-1"></span>
$$Y_{i} = \beta_{0} + \sum_{j=1}^{\tau} \beta_{j} d_{ji} + \gamma x_{2i} + \sum_{j=1}^{\tau} \delta_{j} (d_{ji} x_{2i}) + \varepsilon_{i}.$$
(3.1.10)

The interaction terms, <sup>j</sup> , tell us how each of the schooling e§ects di§er by sex. The CEF in this case takes on 2( + 1) values while the regression has this many parameters.

Note that there is a natural hierarchy of modeling strategies with saturated models at the top. Itís natural to start with a saturated model because this Öts the CEF. On the other hand, saturated models generate a lot of interaction terms, many of which may be uninteresting or imprecise. You might therefore sensibly choose to omit some or all of these. Equation [\(3.1.10\)](#page-53-1) without interaction terms approximates the CEF with a purely additive model for schooling and sex. This is a good approximation if the returns to college are similar for men and women. And, in any case, schooling coe¢ cients in the additive speciÖcation give a (weighted) average return across both sexes, as discussed in Section [3.3.1,](#page-66-0) below. On the other hand, it would be strange to estimate a model which included interaction terms but omitted the corresponding main e§ects. In the case of schooling, this would be something like

<span id="page-53-2"></span>
$$Y_i = \beta_0 + \gamma x_{2i} + \sum_{j=1}^{\tau} \delta_j(d_{ji}x_{2i}) + \varepsilon_i.$$
 (3.1.11)

This model allows schooling to shift wages only for women, something very far from the truth. Consequently, the results of estimating [\(3.1.11\)](#page-53-2) are likely to be hard to interpret.

Finally, itís important to recognize that a saturated model Öts the CEF perfectly regardless of the distribution of y<sup>i</sup> . For example, this is true for linear probability models and other limited dependent variable models (e.g., non-negative yi), a point we return to at the end of this chapter.

# <span id="page-53-0"></span>3.2 Regression and Causality

Section [3.1.2](#page-41-0) shows how regression gives the best (MMSE) linear approximation to the CEF. This understanding, however, does not help us with the deeper question of when regression has a causal interpretation. When can we think of a regression coe¢ cient as approximating the causal e§ect that might be revealed in an experiment?