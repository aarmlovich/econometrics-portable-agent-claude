# Selection on the Basis of the Response Variable: Truncated Regression

> Pages: 566-568

Let ðxi; yiÞ denote a random draw from a population. In this section we explicitly treat the case where the sample is selected on the basis of yi.

In applying the following methods it is important to remember that there is an underlying population of interest, often described by a linear conditional expectation: Eðyi j xiÞ ¼ xi*b*. If we could observe a random sample from the population, then we would just use standard regression analysis. The problem comes about because the sample we can observe is chosen at least partly based on the value of yi. Unlike in the case where selection is based only on xi, selection based on yi causes problems for standard OLS analysis on the selected sample.

A classic example of selection based on yi is Hausman and Wise's (1977) study of the determinants of earnings. Hausman and Wise recognized that their sample from a negative income tax experiment was truncated because only families with income below 1.5 times the poverty level were allowed to participate in the program; no data were available on families with incomes above the threshold value. The truncation rule was known, and so the effects of truncation could be accounted for.

A similar example is Example 17.2. We do not observe data on families with wealth above \$200,000. This case is different from the top coding example we discussed in Chapter 16. Here, we observe nothing about families with high wealth: they are entirely excluded from the sample. In the top coding case, we have a random sample of families, and we always observe xi; the information on x<sup>i</sup> is useful even if wealth is top coded.

We assume that yi is a continuous random variable and that the selection rule takes the form

$$s_i = 1[a_1 < y_i < a_2]$$

where a<sup>1</sup> and a<sup>2</sup> are known constants such that a<sup>1</sup> < a2. A good way to think of the sample selection is that we draw ðxi; yiÞ randomly from the population. If yi falls in 

{567}------------------------------------------------

the interval ða1; a2Þ, then we observe both yi and xi. If yi is outside this interval, then we do not observe yi or xi. Thus all we know is that there is some subset of the population that does not enter our data set because of the selection rule. We know how to characterize the part of the population not being sampled because we know the constants a<sup>1</sup> and a2.

In most applications we are still interested in estimating Eðyi j xiÞ ¼ xi*b*. However, because of sample selection based on yi, we must—at least in a parametric context specify a full conditional distribution of yi given xi. Parameterize the conditional density of yi given x<sup>i</sup> by fð j xi; *b*; *g*Þ, where *b* are the conditional mean parameters and *g* is a G 1 vector of additional parameters. The cdf of yi given x<sup>i</sup> is Fðj xi; *b*; *g*Þ.

What we can use in estimation is the density of yi conditional on x<sup>i</sup> and the fact that we observe ðyi; xiÞ. In other words, we must condition on a<sup>1</sup> < yi < a<sup>2</sup> or, equivalently, si ¼ 1. The cdf of yi conditional on ðxi;si ¼ 1Þ is simply

$$P(y_i \le y \mid \mathbf{x}_i, s_i = 1) = \frac{P(y_i \le y, s_i = 1 \mid \mathbf{x}_i)}{P(s_i = 1 \mid \mathbf{x}_i)}$$

Because yi is continuously distributed, Pðsi ¼1jxiÞ¼Pða<sup>1</sup> < yi <a<sup>2</sup> jxiÞ¼Fða<sup>2</sup> jxi; *b*; *g*Þ Fða<sup>1</sup> j xi; *b*; *g*Þ > 0 for all possible values of xi. The case a<sup>2</sup> ¼ y corresponds to truncation only from below, in which case Fða<sup>2</sup> j xi; *b*; *g*Þ 11. If a<sup>1</sup> ¼ y (truncation only from above), then Fða<sup>1</sup> j xi; *b*; *g*Þ ¼ 0. To obtain the numerator when a<sup>1</sup> < y < a2, we have

$$P(y_i \le y, s_i = 1 \mid \mathbf{x}_i) = P(a_1 < y_i \le y \mid \mathbf{x}_i) = F(y \mid \mathbf{x}_i; \boldsymbol{\beta}, \boldsymbol{\gamma}) - F(a_1 \mid \mathbf{x}_i; \boldsymbol{\beta}, \boldsymbol{\gamma})$$

When we put this equation over Pðsi ¼ 1 j xiÞ and take the derivative with respect to the dummy argument y, we obtain the density of yi given ðxi;si ¼ 1Þ:

$$p(y \mid \mathbf{x}_i, s_i = 1) = \frac{f(y \mid \mathbf{x}_i; \boldsymbol{\beta}, \boldsymbol{\gamma})}{F(a_2 \mid \mathbf{x}_i; \boldsymbol{\beta}, \boldsymbol{\gamma}) - F(a_1 \mid \mathbf{x}_i; \boldsymbol{\beta}, \boldsymbol{\gamma})}$$
(17.14)

for a<sup>1</sup> < y < a2.

Given a model for fðy j x; *b*; *g*Þ, the log-likelihood function for any ðxi; yiÞ in the sample can be obtained by plugging yi into equation (17.14) and taking the log. The CMLEs of *b* and *g* using the selected sample are efficient in the class of estimators that do not use information about the distribution of xi. Standard errors and test statistics can be computed using the general theory of conditional MLE.

In most applications of truncated samples, the population conditional distribution is assumed to be Normalðx*b*; s<sup>2</sup>Þ, in which case we have the truncated Tobit model or truncated normal regression model. The truncated Tobit model is related to the censored Tobit model for data-censoring applications (see Chapter 16), but there is a key

{568}------------------------------------------------

difference: in censored regression, we observe the covariates  $\mathbf{x}$  for *all* people, even those for whom the response is not known. If we drop observations entirely when the response is not observed, we obtain the truncated regression model. If in Example 16.1 we use the information in the top coded observations, we are in the censored regression case. If we drop all top coded observations, we are in the truncated regression case. (Given a choice, we should use a censored regression analysis, as it uses all of the information in the sample.)

From our analysis of the censored regression model in Chapter 16, it is not surprising that heteroskedasticity or nonnormality in truncated regression results in inconsistent estimators of  $\beta$ . This outcome is unfortunate because, if not for the sample selection problem, we could consistently estimate  $\beta$  under  $E(y | \mathbf{x}) = \mathbf{x}\beta$ , without specifying  $Var(y | \mathbf{x})$  or the conditional distribution. Distribution-free methods for the truncated regression model have been suggested by Powell (1986) under the assumption of a symmetric error distribution; see Powell (1994) for a recent survey.

Truncating a sample on the basis of y is related to **choice-based sampling**. Traditional choice-based sampling applies when y is a discrete response taking on a finite number of values, where sampling frequencies differ depending on the outcome of y. [In the truncation case, the sampling frequency is one when y falls in the interval  $(a_1, a_2)$  and zero when y falls outside of the interval.] We do not cover choice-based sampling here; see Manksi and McFadden (1981), Imbens (1992), and Cosslett (1993). In Section 17.8 we cover some estimation methods for stratified sampling, which can be applied to some choice-based samples.