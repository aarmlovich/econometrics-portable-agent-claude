# The Quantile Regression Approximation PropertyF

> Pages: 225-229

The CQF of log wages given schooling is unlikely to be exactly linear, so the assumptions of the original quantile regression model fail to hold in this example. Luckily, quantile regression can also be understood as giving a MMSE linear approximation to the CQF, though in this case the MMSE problem is a little more complicated and harder to derive than for the regression-CEF theorem. For any quantile index 2 (0; 1), deÖne the quantile regression speciÖcation error as:

$$\Delta_{\tau}(\mathbf{X}_{i}, \beta_{\tau}) \equiv \mathbf{X}_{i}' \beta_{\tau} - Q_{\tau}(\mathbf{Y}_{i} | \mathbf{X}_{i}).$$

The population quantile regression vector can be shown to minimize an expected weighted average of the squared speciÖcation error, <sup>2</sup> (X<sup>i</sup> ; ), as shown in the following theorem from Angrist, Chernozhukov, and Fernandez-Val (2006):

Theorem 7.1.1 (Quantile Regression Approximation) Suppose that (i) the conditional density f<sup>Y</sup> (yjXi) exists almost surely, (ii) E[y<sup>i</sup> ], E[Q (y<sup>i</sup> jXi)], and EkXik are Önite, and (iii)  uniquely solves [\(7.1.2\)](#page-220-0). Then

<span id="page-225-0"></span>
$$\beta_{\tau} = \arg \min_{b \in \mathbb{R}^d} E\left[w_{\tau}(\mathbf{X}_i, b) \cdot \Delta_{\tau}^2(\mathbf{X}_i, b)\right], \tag{7.1.7}$$

where

$$w_{\tau}(\mathbf{X}_{i}, b) = \int_{0}^{1} (1 - u) \cdot f_{\epsilon(\tau)} \left( u \Delta_{\tau}(\mathbf{X}_{i}, b) | \mathbf{X}_{i} \right) du$$
$$= \int_{0}^{1} (1 - u) \cdot f_{Y} \left( u \cdot \mathbf{X}_{i}' b + (1 - u) \cdot Q_{\tau}(\mathbf{Y}_{i} | \mathbf{X}_{i}) | \mathbf{X}_{i} \right) du \geq 0$$

and i( ) is a quantile-speciÖc residual,

$$\epsilon_i(\tau) \equiv \mathbf{Y}_i - Q_{\tau}(\mathbf{Y}_i|\mathbf{X}_i),$$

with conditional density f() (ejXi) at i( ) = e. Moreover, when y<sup>i</sup> has a smooth conditional density, we have for  in the neighborhood of  :

$$w_{\tau}(\mathbf{X}_{i}, \beta) \approx 1/2 \cdot f_{Y}\left(Q_{\tau}(\mathbf{Y}_{i}|\mathbf{X}_{i})|\mathbf{X}_{i}\right). \tag{7.1.8}$$

{226}------------------------------------------------

The quantile regression approximation theorem looks complicated but the big picture is simple. We can think of quantile regression as approximating  $Q_{\tau}(Y_i|X_i)$ , just as OLS approximates  $E[Y_i|X_i]$ . The OLS weighting function is the histogram of  $X_i$ , which we denote  $\pi(X_i)$ . The quantile regression weighting function, implicitly given by  $w_{\tau}(X_i, \beta_{\tau}) \cdot \pi(X_i)$ , is more elaborate than  $\pi(X_i)$  alone (the histogram is implicitly part of the quantile regression weighting function because the expectation in (7.1.7) is over the distribution of  $X_i$ . The term  $w_{\tau}(X_i, \beta_{\tau})$  involves the quantile regression vector,  $\beta_{\tau}$ , but can be rewritten with  $\beta_{\tau}$  partialled out so that it is a function of  $X_i$  only (see Angrist, Chernozhukov, and Fernandez-Val, 2006, for details). In any case, the quantile regression weights are approximately proportional to the density of  $Y_i$  in the neighborhood of the CQF.

The quantile regression approximation property is illustrated in Figure 7.1.1, which plots the conditional quantile function of log wages given highest grade completed using 1980 Census data. Here we take advantage of the discreteness of schooling and large census samples to estimate the CQF non-parametrically by computing the quantile of wages for each schooling level. Panels A-C plot a nonparametric estimate of  $Q_{\tau}(Y_i|X_i)$  along with the linear quantile regression fit for the 0.10, 0.50, and 0.90 quantiles, where  $X_i$  includes only the schooling variable and a constant. The nonparametric cell-by-cell estimate of the CQF is plotted with circles in the figure, while the quantile regression line is solid. The figure shows how linear quantile regression approximates the CQF.

It's also interesting to compare quantile regression to a histogram-weighted fit to the CQF, similar to that provided by OLS for the CEF. The histogram-weighted approach to quantile regression was proposed by Chamberlain (1994). The Chamberlain minimum distance (MD) estimator is the sample analog of the vector  $\tilde{\beta}_{\tau}$  obtained by solving

$$\tilde{\beta}_{\tau} = \arg\min_{b \in \mathbb{R}^d} \ E\left[ \left( Q_{\tau}(\mathbf{Y}_i | \mathbf{X}_i) - \mathbf{X}_i' b \right)^2 \right] = \arg\min_{b \in \mathbb{R}^d} \ E\left[ \Delta_{\tau}^2(\mathbf{X}_i, b) \right].$$

In other words,  $\hat{\beta}_{\tau}$  is the slope of the linear regression of  $Q_{\tau}(Y_i|X_i)$  on  $X_i$ , weighted by the histogram of  $X_i$ . In contrast with quantile regression, which requires only one pass through the data, MD relies on the ability to estimate  $Q_{\tau}(Y_i|X_i)$  consistently in a nonparametric first step.

Figure 1 plots MD fitted values with a dashed line. The quantile regression and MD lines are close, but they are not identical because of the weighting by  $w_{\tau}(X_i, \beta_{\tau})$  in the quantile regression fit. This weighting accentuates the quality of the fit at values of  $X_i$  where  $Y_i$  is more densely distributed near the CQF. Panels D-F in Figure 7.1.1 plot the overall quantile weights,  $w_{\tau}(X_i, \beta_{\tau}) \cdot \pi(X_i)$  against  $X_i$ . The panels also show estimates of the  $w_{\tau}(X_i, \beta_{\tau})$ , labeled "importance weights," and their density approximations,  $1/2 \cdot f_Y(Q_{\tau}(Y_i|X_i)|X_i)$ . The importance weights and the density weights are similar and fairly flat. The overall weighting function looks a lot like the schooling histogram, and therefore places the highest weight on 12 and 16 years of schooling.

{227}------------------------------------------------

![](_page_227_Figure_2.jpeg)

<span id="page-227-0"></span>Figure 7.1.1: The quantile regression approximation property (adapted from Angrist, Chernozhukov, and Fernandez-Val, 2006). The Ögure shows alternative estimates of the conditional quantile function of log wages given highest grade completed using 1980 Census data, along with the implied weighting function. Panels A-C report nonparametric (CQ), quantile regression (QR) and minimum distance estimates (MD) for = :1; :5; :9. Panels D-F show the corresponding weighting functions for QR and MD, as explained in the text.

{228}------------------------------------------------

#### 7.1.3 Tricky Points

The language of conditional quantiles is tricky. Sometimes we talk about "quantile regression coe¢ cients at the median," or "e§ects on those at the lower decile." But itís important to remember that quantile coe¢ cients tell us about e§ects on distributions and not on individuals. If we discover, for example, that a training program raises the lower decile of the wage distribution, this does not necessarily mean that someone who would have been poor (i.e. at the lower decile without training) is now less poor. It only means that those who are poor in the regime with training are less poor than the poor would be in a regime without training.

The distinction between making a given set of poor people richer and changing what it means to be poor is subtle. This distinction has to do with whether we think an intervention preserves an individualís rank in the wage (or other dependent variable) distribution. If an intervention is rank-preserving, then an increase in the lower decile indeed makes those who would have been poor richer since rank preservations means relative status is unchanged. Otherwise, we can only say that the poor - deÖned as the group in the bottom 10 percent of the wage distribution, whoever they may be - are better o§. We elaborate on this point brieáy in Section [7.2,](#page-229-0) below.

A second tricky point is the transition from conditional quantiles to marginal quantiles. A link from conditional to marginal quantiles allows us to investigate the impact of changes in quantile regression coe¢ cients on overall inequality. Suppose, for example, that quantile coe¢ cients fan out even further with schooling, beyond whatís observed in the 2000 Census. What does this imply for the ratio of upper-decile to lower-decile wages? Alternately, we can ask: how much of the overall increase in inequality (say, as measured by the ratio of upper- to lower-deciles) is explained by the fanning out of quantile regression coe¢ cients? These sorts of questions turn out to be surprisingly di¢ cult to answer. The di¢ culty has to do with the fact that all conditional quantiles are needed to pin down a particular marginal quantile (Machado and Mata, 2005). In particular, Q (y<sup>i</sup> jXi) =X<sup>0</sup> <sup>i</sup> does not imply Q (yi) = Q (Xi) <sup>0</sup> . This contrast this with the much more tractable expectations operator, where if E(y<sup>i</sup> jXi) =X<sup>0</sup> <sup>i</sup>, then by iterating expectations, we have E(yi) = E(Xi) <sup>0</sup>.

#### Extracting marginal quantiles

<span id="page-228-1"></span>To show the link between conditional quantiles and marginal distributions more formally, suppose the CQF is indeed linear, so that Q (y<sup>i</sup> jXi) =X<sup>0</sup> <sup>i</sup> . Let F<sup>Y</sup> (yjXi) P[y<sup>i</sup> < yjX<sup>i</sup> ] with marginal distribution F<sup>Y</sup> (y) = P[y<sup>i</sup> < y]: By deÖnition of a conditional quantile,

<span id="page-228-0"></span>
$$\int_{0}^{1} 1[F_{Y}^{-1}(\tau|X_{i}) < y]d\tau = F_{Y}(y|X_{i}).$$
(7.1.9)

{229}------------------------------------------------

In other words, the proportion of the population below y conditional on X<sup>i</sup> is the same as the proportion of conditional quantiles that are below y. [4](#page-229-1) Substituting for the CQF inside the integral,

$$F_Y(y|\mathbf{X}_i) = \int_0^1 1[\mathbf{X}_i' \boldsymbol{\beta}_{\tau} < y] d\tau.$$

Next, we use the CDF of X<sup>i</sup> , FX(x), to integrate and get the marginal distribution function, F<sup>Y</sup> (y):

<span id="page-229-2"></span>
$$F_Y(y) = \int \int_0^1 1[X_i'\beta_\tau < y] d\tau dF_X(x).$$
 (7.1.10)

Finally, marginal quantiles, say, Q (yi) for 2 (0; 1), come from inverting F<sup>Y</sup> (y):

$$Q_{\tau}(Y_i) = \inf \{ y : F_Y(y) \ge \tau \}.$$

An estimator of the marginal distribution replaces integrals with sums in [\(7.1.10\)](#page-229-2), where the integral over quantiles comes from quantile regression estimates at, say, every .01 quantile. In a sample of size n, this is:

$$\hat{F}_Y(y) = n^{-1} \sum_i (1/100) \sum_{\tau=0}^{\tau=1} 1[X_i' \hat{\beta}_{\tau} < y].$$

The corresponding marginal quantile estimator inverts F^ <sup>Y</sup> (y):

There are a number of di¢ culties with this approach in practice. For one thing, you have to estimate lots of quantile regressions. Another is that the distribution theory is messy (though not insurmountable; see, e.g., Melly, 2005). Simplifying the conditional-to-marginal quantile transition is an area of active research. Gosling, Machin, and Meghir (2000) and Machado and Mata (2005) are among the Örst empirical studies to go from conditional to marginal quantiles. When the variable of primary interest in a quantile regression model is a dummy variable and the other regressors are seen as controls, a propensity-score type weighting scheme can be used to produce the di§erence in quantiles conditional on the dummy. See Firpo (2007) for the exogenous case and Frolich and Melly (2007) for a marginalization scheme that works for quantile treatment e§ects of the sort discussed in the next section.