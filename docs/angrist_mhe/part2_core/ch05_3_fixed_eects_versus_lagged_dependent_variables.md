# Fixed E§ects versus Lagged Dependent Variables

> Pages: 197-204

Fixed e§ects and di§erences-in-di§erences estimators are based on the presumption of time-invariant (or group-invariant) omitted variables. Suppose, for example, we are interested in the e§ects of participation in a subsidized training program, as in the Dehejia and Wahba (1999) and Lalonde (1986) studies discussed in section [\(3.3.3\)](#page-78-0). The key identifying assumption motivating Öxed e§ects estimation in this case is

<span id="page-197-0"></span>
$$E(\mathbf{Y}_{0it}|\alpha_i, \mathbf{X}_{it}, \mathbf{D}_{it}) = E(\mathbf{Y}_{0it}|\alpha_i, \mathbf{X}_{it}), \tag{5.3.1}$$

where <sup>i</sup> is an unobserved personal characteristic that determines, along with covariates, Xit, whether individual i gets training. To be concrete, <sup>i</sup> might be a measure of vocational skills, though a strike against the Öxed-e§ects setup is the fact that the exact nature of the unobserved variables typically remains somewhat mysterious. In any case, coupled with a linear model for E(y0itj<sup>i</sup> ;Xit), assumption [\(5.3.1\)](#page-197-0) leads to simple estimation strategies involving di§erences or deviations from means.

For many causal questions, the notion that the most important omitted variables are time-invariant doesnít seem plausible. The evaluation of training programs is a case in point. It seems likely that people looking to improve their labor market options by participating in a government-sponsored training program have su§ered some kind of setback. Many training programs explicitly target people who have su§ered a recent setback, e.g., men who recently lost their jobs. Consistent with this, Ashenfelter (1978) and Ashenfelter and Card (1985) Önd that training participants typically have earnings histories that exhibit a pre-program dip. Past earnings is a time-varying confounder that cannot be subsumed in a time-invariant variable like <sup>i</sup> :

The distinctive earnings histories of trainees motivates an estimation strategy that controls for past earnings directly and dispenses with the Öxed e§ects. To be precise, instead of [\(5.3.1\)](#page-197-0), we might base causal inference on the conditional independence assumption,

<span id="page-197-1"></span>
$$E(Y_{0it}|Y_{it-h}, X_{it}, D_{it}) = E(Y_{0it}|Y_{it-h}, X_{it}).$$
(5.3.2)

This is like saying that what makes trainees special is their earnings h periods ago. We can then use panel data to estimate

<span id="page-197-2"></span>
$$Y_{it} = \alpha + \theta Y_{it-h} + \lambda_t + \beta D_{it} + X_{it} \delta + \varepsilon_{it}, \qquad (5.3.3)$$

{198}------------------------------------------------

where the causal e§ect of training is . To make this more general, yit<sup>h</sup> can be a vector including lagged earnings for multiple periods: [9](#page-198-0)

Applied researchers using panel data are often faced with the challenge of choosing between Öxed-e§ects and lagged-dependent variables models, i.e., between causal inferences based on [\(5.3.1\)](#page-197-0) and [\(5.3.2\)](#page-197-1). One solution to this dilemma is to work with a model that includes both lagged dependent variables and unobserved individual e§ects. In other words, identiÖcation might be based on a weaker conditional independence assumption:

$$E(Y_{0it}|a_i, Y_{it-h}, X_{it}, D_{it}) = E(Y_{0it}|\alpha_i, Y_{it-h}, X_{it}),$$
(5.3.4)

which requires conditioning on both <sup>i</sup> and yit<sup>h</sup>: We can then try to estimate causal e§ects using a speciÖcation like

<span id="page-198-1"></span>
$$Y_{it} = \alpha_i + \theta Y_{it-h} + \lambda_t + \beta D_{it} + X_{it} \delta + v_{it}.$$

$$(5.3.5)$$

Unfortunately, the conditions for consistent estimation of  in equation [\(5.3.5\)](#page-198-1) are much more demanding than those required with Öxed e§ects or lagged dependent variables alone. This can be seen in a simple example where the lagged dependent variable is yit<sup>1</sup>. We kill the Öxed e§ect by di§erencing, which produces

<span id="page-198-2"></span>
$$\Delta Y_{it} = \theta \Delta Y_{it-1} + \Delta \lambda_t + \beta \Delta D_{it} + \Delta X_{it} \delta + \Delta v_{it}.$$
(5.3.6)

The problem here is that the di§erenced residual, it, is necessarily correlated with the lagged dependent variable, yit<sup>1</sup>, because both are a function of it<sup>1</sup>: Consequently, OLS estimates of [\(5.3.6\)](#page-198-2) are not consistent for the parameters in [\(5.3.5\)](#page-198-1), a problem Örst noted by Nickell (1981). This problem can be solved, though the solution requires strong assumptions. The easiest solution is to use yit<sup>2</sup> as an instrument for yit<sup>1</sup> in [\(5.3.6\)](#page-198-2).[10](#page-198-3) But this requires that <sup>y</sup>it<sup>2</sup> be uncorrelated with the di§erenced residuals, it. This seems unlikely since residuals are the part of earnings left over after accounting for covariates. Most peopleís earnings are highly correlated from one year to the next, so that past earnings are an excellent predictor of future earnings and earnings growth . If it is serially correlated, there may be no consistent estimator for [\(5.3.6\)](#page-198-2). (Note also that the IV strategy using yit<sup>2</sup> as an instrument requires at least three periods to obtain data for t; t 1; and t 2).

Given the di¢ culties that arise when trying to estimate [\(5.3.6\)](#page-198-2), we might ask whether the distinction between Öxed e§ects and lagged dependent variables matters. The answer, unfortunately, is yes. The Öxed-e§ects and lagged dependent variables models are not nested, which means we cannot hope to estimate

<span id="page-198-0"></span><sup>9</sup>Abadie, Diamond, and Hainmueller (2007) develop a semiparametric version of the lagged-dependent variables model, more áexible than the traditional regression setup. As with our regression setup, the key assumption in this model is conditional independence of potential outcomes conditional on lagged earnings, i.e., assumption [\(5.3.2\)](#page-197-1).

<span id="page-198-3"></span><sup>1 0</sup> See Holtz-Eakin, Newey and Rosen (1988), Arellano and Bond (1991), Blundell and Bond (1998) for details and examples.

{199}------------------------------------------------

one and get the other as a special case if need be. Only the more general and harder-to-identify model, [\(5.3.5\)](#page-198-1), nests both Öxed e§ects and lagged dependent variables.[11](#page-199-0) .

So whatís an applied guy to do? One answer, as always, is to check the robustness of your Öndings using alternative identifying assumptions. That means that you would like to Önd broadly similar results using both models. Fixed e§ects and lagged dependent variables estimates also have a useful bracketing property. The appendix to this chapter shows that if [\(5.3.2\)](#page-197-1) is correct, but you mistakenly use Öxed e§ects, estimates of a positive treatment e§ect will tend to be too big. On the other hand, if [\(5.3.1\)](#page-197-0) is correct and you mistakenly estimate an equation with lagged outcomes like [\(5.3.3\)](#page-197-2), estimates of a positive treatment e§ect will tend to be too small. You can therefore think of Öxed e§ects and lagged dependent variables as bounding the causal e§ect you are after. Guryan (2004) illustrates this sort of reasoning in a study estimating the e§ects of court-ordered busing on Black high school graduation rates.

# 5.4 Appendix: More on Öxed e§ects and lagged dependent variables

To simplify, we ignore covariates and year e§ects and assume there are only two periods, with treatment equal to zero for everyone in the Örst period (the punch line is the same in a more general setup). The causal e§ect of interest, , is positive. Suppose Örst that treatment is correlated with an unobserved individual e§ect, a<sup>i</sup> , and that outcomes can be described by

<span id="page-199-1"></span>
$$Y_{it} = a_i + \beta D_{it} + \varepsilon_{it}. \tag{5.4.1}$$

where "it is serially uncorrelated, and uncorrelated with a<sup>i</sup> and dit. We also have

$$Y_{it-1} = a_i + \varepsilon_{it-1},$$

where a<sup>i</sup> and "it<sup>1</sup> are uncorrelated. You mistakenly estimate the e§ect of dit in a model that controls for <sup>y</sup>it<sup>1</sup> but ignores Öxed e§ects. The resulting estimator has probability limit Cov(yit;dòit) V (dòit) , where dòit =dit yit<sup>1</sup> is the residual from a regression of dit on yit<sup>1</sup>.

$$\Delta \mathbf{Y}_{it} = \alpha + \lambda_t + \beta \mathbf{D}_{it} + \mathbf{X}_{it} \delta + \varepsilon_{it}$$

i.e., a di§erenced dependent variable with regressors in levels. This is not the model with Örst di§erences on both the right and left side needed to kill the Öxed e§ect.

<span id="page-199-0"></span><sup>1 1</sup> In particular, setting = 1 in [\(5.3.3\)](#page-197-2) does not produce the Öxed-e§ects model as a special case of the lagged dependent variables model. Instead we get

{200}------------------------------------------------

Now substitute a<sup>i</sup> = yit<sup>1</sup> "it<sup>1</sup> in [\(5.4.1\)](#page-199-1) to get

$$\mathbf{Y}_{it} = \mathbf{Y}_{it-1} + \beta \mathbf{D}_{it} + \varepsilon_{it} - \varepsilon_{it-1}.$$

From here, we get

$$\frac{Cov(\mathbf{Y}_{it}, \tilde{\mathbf{D}}_{it})}{V(\tilde{\mathbf{D}}_{it})} = \beta - \frac{Cov(\varepsilon_{it-1}, \tilde{\mathbf{D}}_{it})}{V(\tilde{\mathbf{D}}_{it})} = \beta - \frac{Cov(\varepsilon_{it-1}, \mathbf{D}_{it} - \gamma \mathbf{Y}_{it-1})}{V(\tilde{\mathbf{D}}_{it})} = \beta + \frac{\gamma \sigma_{\varepsilon}^{2}}{V(\tilde{\mathbf{D}}_{it})}.$$

where 2 " is the variance of "it<sup>1</sup>. Since trainees have low yit<sup>1</sup>; 
 < 0 and the resulting estimate of  is too small.

Suppose instead that treatment is determined by low yit<sup>1</sup>. The correct speciÖcation is a simpliÖed version of [\(5.3.3\)](#page-197-2), say

<span id="page-200-0"></span>
$$Y_{it} = \alpha + \theta Y_{it-1} + \beta D_{it} + \varepsilon_{it}, \qquad (5.4.2)$$

where "it is serially uncorrelated. You mistakenly estimate a Örst-di§erenced equation in an e§ort to kill Öxed e§ects. This ignores lagged dependent variables. In this simple example, where dit<sup>1</sup> = 0 for everyone, the Örst-di§erenced estimator has probability limit

$$\frac{Cov(Y_{it} - Y_{it-1}, D_{it} - D_{it-1})}{V(D_{it} - D_{it-1})} = \frac{Cov(Y_{it} - Y_{it-1}, D_{it})}{V(D_{it})}.$$
(5.4.3)

Subtracting yit<sup>1</sup> from both sides of [\(5.4.2\)](#page-200-0), we have

$$Y_{it} - Y_{it-1} = \alpha + (\theta - 1)Y_{it-1} + \beta D_{it} + \varepsilon_{it}.$$

Substituting this in [\(4.2.2\)](#page-120-0), the inappropriately di§erenced model yields

$$\frac{Cov(\mathbf{Y}_{it} - \mathbf{Y}_{it-1}, \mathbf{D}_{it})}{V(\mathbf{D}_{it})} = \beta + (\theta - 1) \left[ \frac{Cov(\mathbf{Y}_{it-1}, \mathbf{D}_{it})}{V(\mathbf{D}_{it})} \right].$$

In general, we think is a number between zero and one, otherwise yit is non-stationary (i.e., an explosive time series process). Therefore, since trainees have low yit1; the estimate of  in Örst di§erences is too big.


{201}------------------------------------------------

{202}------------------------------------------------

Part III

Extensions

{203}------------------------------------------------

<table><tbody><tr><th></th><th></th><th></th></tr><tr><th></th><th></th><th></th></tr><tr><th></th><th></th><th></th></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></tbody></table>

{204}------------------------------------------------