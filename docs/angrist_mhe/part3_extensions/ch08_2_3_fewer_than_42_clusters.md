# Fewer than 42 clusters

> Pages: 253-264

Bias from few clusters is a risk in both the Moulton and the serial correlation contexts because in both cases inference is cluster-based. With few clusters, we tend to underestimate either the serial correlation in a random shock like  $v_{st}$  or the intra-class correlation,  $\rho$ , in the Moulton problem. The relevant dimension for counting clusters in the Moulton problem is the number of groups, G. In a differences-in-differences scenario where you'd like to cluster on state (or some other cross-sectional dimension), the relevant dimension for counting clusters is the number of states or cross-sectional groups. Therefore, following Douglas Adam's dictum that the ultimate answer to life, the universe, and everything is 42, we believe the question is: How many clusters are enough for reliable inference using a standard cluster adjustment derived from (8.2.6)?

If 42 is enough for the standard cluster adjustment to be reliable - and less is too few - then what should you do when the cluster count is low? First-best is to get more clusters by collecting more data. But sometimes we're too lazy for that, so other ideas are detailed below. It's worth noting at the outset that not all of these ideas are equally well-suited for the Moulton and serial correlation problems.

1. Bias correction of clustered standard errors. Clustered standard errors are biased in small samples because  $E\left(\hat{e}_g\hat{e}_g'\right) \neq E\left(e_ge_g'\right) = \Psi_g$  just as in Section 8.1. Usually,  $E\left(\hat{e}_g\hat{e}_g'\right)$  is too small. One solution is to inflate residuals in the hopes of reducing bias. Bell and McCaffrey (2002) suggest a procedure (called bias-reduced linearization or BRL) that adjusts residuals by

$$\hat{\Psi}_g = a\tilde{e}_g\tilde{e}_g'$$

$$\widetilde{e}_g = A \widehat{e}_g$$

where A solves

$$A_g'A_g = (I - H_g)^{-1}$$

and

$$H_g = X_g (X'X)^{-1} X_g'.$$

This is a version of  $HC_2$  for the clustered case. BRL works for the straight-up Moulton problem with few clusters but for technical reasons cannot be used for the typical differences-in-differences serial 

{254}------------------------------------------------

correlation problem.[15](#page-254-0)

- 2. Recognizing that the fundamental unit of observation is a cluster and not an individual unit within clusters, Bell and McCa§rey (2002) and Donald and Lang (2007) suggest that inference be based on a t-distribution with Gk degrees of freedom rather than on the standard Normal distribution. For small G, this makes a big di§erence - conÖdence intervals will be much wider, thereby avoiding some mistakes. Cameron, Gelbach, and Miller (2008) report Monte Carlo examples where the combination of a BRL adjustment and use of t-tables works well.
- 3. Donald and Lang (2007) argue that estimation using group means works well with small G in the Moulton problem, and even better when inference is based on a t-distribution with Gk degrees of freedom. But, as we discussed in the previous section, the regressor must be Öxed within groups. The level of aggregation is the level at which youíd like to cluster, e.g., schools in Angrist and Lavy (2007). For serial correlation, this is the state, but state averages cannot be used to estimate a model with a full set of state e§ects. Also, since treatment status varies within states, averaging up to the state level averages the regressor of interest as well, changing the rules of the game in a way we may not like (the estimator becomes instrumental variables using group dummies as instruments). The group means approach is therefore out of bounds for the serial correlation problem.[16](#page-254-1) Note also that if the grouped residuals are heteroskedastic, and you therefore use robust standard errors, you must worry about bias of the form discussed in Section [8.1.](#page-237-0) If both the random e§ect and the underlying micro residual are homoskedastic, you can Öx heteroskedasticity in the group means by weighting by the group size. But weighting changes the estimand when the CEF is nonlinear - so this is not open-and-shut (Angrist and Lavy, 1999 chose not to weight school-level averages because the variation in their study comes mostly from small schools). Weighted or not, the safest course when working with group-level averages is to use of our rule of thumb from Section [8.1:](#page-237-0) take the maximum of robust and conventional standard errors as your best measure of precision.

$$A_g = P\Lambda^{1/2}$$

where P is the matrix of eigenvectors of (I Hg) 1 , is the diagonal matrix of the correponding eigenvalues, and 1=<sup>2</sup> is the diagonal matrix of the square roots of the eigenvalues. One problem with the Bell and McCa§rey adjustment is that (I Hg) may not be of full rank, and hence the inverse may not exist for all designs. This happens, for example, when one of the regressors is a dummy variable which is one for exactly one of the clusters, and zero otherwise. This includes the panel DD model discussed by Bertrand et al. (2004), where you include a full set of state dummies and cluster by state. Moreover, the eigenvalue decomposition is implemented for matrices which are the size of the groups. In many applications, group sizes are large enough that this becomes computationally intractible.

<span id="page-254-0"></span><sup>1 5</sup> The matrix A<sup>g</sup> is not unique; there are many such decompositions. Bell and McCa§rey (2002) use the symemtric square root of (I Hg) 1 or

<span id="page-254-1"></span><sup>1 6</sup>Donald and Lang (2007) discuss serial correlation examples where the regressor is Öxed within the clustering dimension, but this is not the typical di§erences-in-di§erences setup.

{255}------------------------------------------------

- 4. Cameron, Gelbach, and Miller (2008) report that some forms of a block bootstrap work well with small numbers of groups, and that the block bootstrap typically outperforms Stata-clustered standard errors without the bias correction. This appears to be true both for the Moulton and serial correlation problems. But Cameron, Gelbach, and Miller (2008) focus on rejection rates using (pivotal) test statistics, while we like to see standard errors.
- 5. Parametric corrections: For the Moulton problem, this amounts to use of the Moulton factor. With serial correlation, this means correcting your standard errors for Örst-order serial correlation at the group level. Based on our sampling experiments with the Moulton problem and a reading of the literature, parametric approaches may work well, and better than the nonparametric estimator [\(8.2.6\)](#page-249-1), especially if the parametric model is not too far o§ (see, e.g., Hansen, 2007a, which also proposes a bias correction for estimates of serial correlation parameters). Unfortunately, however, beyond the greenhouse world of controlled Monte Carlo studies, weíre unlikely to know whether parametric assumptions are a good Öt.

Alas, the bottom line here is not entirely clear, as is the more basic question of when few clusters are fatal for inference. The severity of the resulting bias seems to depend on the nature of your problem, in particular whether you confront straight-up Moulton or serial correlation issues. Aggregation to the group level as in Donald and Lang (2007) seems to work well in the Moulton case as long as the regressor of interest is Öxed within groups and there is not too much underlying heteroskedasticity. At a minimum, youíd like to show that your conclusions are consistent with the inferences that arise from an analysis of group averages since this is a conservative and transparent approach. Angrist and Lavy (2007) go with BRL standard errors to adjust for clustering at the school level but validate these by showing that key results come out the same using covariate-adjusted group averages.

As far as serial correlation goes, most of the evidence suggests that when you are lucky enough to do research on US states, giving 51 clusters, you are on reasonably safe ground with a naive application of Stataís cluster command at the state level. But you might have to study Canada, which o§ers only 10 clusters in the form of provinces, well below 42. Hansen (2007b) Önds that Liang and Zeger (1986) [Stata-clustered] standard errors are reasonably good at correcting for serial correlation in panels, even in the Canadian scenario. Hansen also recommends use of a t-distribution with G k degrees of freedom for critical values.

Clustering problems have forced applied microeconometricians to eat a little humble pie. Proud of working with large micro data sets, we like to sneer at macroeconomists toying with small time series samples. But he who laughs last laughs best: if the regressor of interest varies only at a coarse group level - such as over time or across states or countries - then itís the macroeconomists who have had the most realistic mode of inference all along.

{256}------------------------------------------------

# 8.3 Appendix: Derivation of the simple Moulton factor

Write

$$y_g = \left[\begin{array}{c} y_{1g} \\ y_{2g} \\ \vdots \\ y_{n_g g} \end{array}\right] \quad e_g = \left[\begin{array}{c} e_{1g} \\ e_{2g} \\ \vdots \\ e_{n_g g} \end{array}\right]$$

and

$$y = \begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_G \end{bmatrix} \quad x = \begin{bmatrix} \iota_1 x_1 \\ \iota_2 x_2 \\ \vdots \\ \iota_G x_G \end{bmatrix} \quad e = \begin{bmatrix} e_1 \\ e_2 \\ \vdots \\ e_G \end{bmatrix}$$

where  $\iota_q$  is a column vector of  $n_q$  ones and G is the number of groups. Note that

$$E(ee') = \Psi = \begin{bmatrix} \Psi_1 & 0 & \cdots & 0 \\ 0 & \Psi_2 & & \vdots \\ \vdots & & \ddots & 0 \\ 0 & \cdots & 0 & \Psi_G \end{bmatrix}$$

$$\Psi_g = \sigma_e^2 \begin{bmatrix} 1 & \rho & \cdots & \rho \\ \rho & 1 & & \vdots \\ \vdots & & \ddots & \rho \\ \rho & \cdots & \rho & 1 \end{bmatrix} = \sigma_e^2 \left[ (1 - \rho)I + \rho \iota_g \iota_g' \right],$$
where  $\rho = \frac{\sigma_v^2}{\sigma_v^2 + \sigma_\eta^2}$ .

Now

$$X'X = \sum_{g} n_g x_g x'_g$$
$$X'\Psi X = \sum_{g} x_g \iota'_g \Psi_g \iota_g x'_g.$$

But

$$x_{g}\iota'_{g}\Psi_{g}\iota_{g}x'_{g} = \sigma_{e}^{2}x_{g}\iota'_{g}\begin{bmatrix} 1 + (n_{g} - 1)\rho \\ 1 + (n_{g} - 1)\rho \\ & \ddots \\ 1 + (n_{g} - 1)\rho \end{bmatrix}x'_{g}$$
$$= \sigma_{e}^{2}n_{g}\left[1 + (n_{g} - 1)\rho\right]x_{g}x'_{g}.$$

{257}------------------------------------------------

Let <sup>g</sup> = 1 + (n<sup>g</sup> 1), so we get

$$x_g \iota_g' \Psi_g \iota_g x_g' = \sigma_e^2 n_g \tau_g x_g x_g'$$
$$X' \Psi X = \sigma_e^2 \sum_g n_g \tau_g x_g x_g'.$$

With this in hand, we can write

$$\begin{split} V(\widehat{\beta}) &= \left(X'X\right)^{-1} X' \Psi X \left(X'X\right)^{-1} \\ &= \sigma_e^2 \left(\sum_g n_g x_g x_g'\right)^{-1} \sum_g n_g \tau_g x_g x_g' \left(\sum_g n_g x_g x_g'\right)^{-1}. \end{split}$$

We want to compare this with the standard OLS covariance estimator

$$V_c(\widehat{\beta}) = \sigma_e^2 \left( \sum_g n_g x_g x_g' \right)^{-1}.$$

If the group sizes are equal, n<sup>g</sup> = n and <sup>g</sup> = = 1 + (n 1); so that

$$\begin{split} V(\widehat{\beta}) &= \sigma_e^2 \tau \left( \sum_g n x_g x_g' \right)^{-1} \sum_g n x_g x_g' \left( \sum_g n x_g x_g' \right)^{-1} \\ &= \sigma_e^2 \tau \left( \sum_g n x_g x_g' \right)^{-1} \\ &= \tau V_c(\widehat{\beta}), \end{split}$$

which implies [\(8.2.4\)](#page-247-0).

{258}------------------------------------------------

<span id="page-258-0"></span>

<table><tbody><tr><th colspan="5">Table 8.1.1: Monte Carlo results for robust standard errors</th></tr><tr><td></td><td></td><td></td><td colspan="2">Empirical 5%</td></tr><tr><td></td><td></td><td></td><td>Rejection Rates</td><td></td></tr><tr><td></td><td>Mean</td><td>Standard</td><td>Normal</td><td>t</td></tr><tr><td></td><td></td><td>Deviation</td><td></td><td></td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td></td><td></td><td>A. Lots of Heteroskedasticity</td><td></td><td></td></tr><tr><td>^<br/>1</td><td>-0.001</td><td>0.586</td><td></td><td></td></tr><tr><td>Standard Errors:</td><td></td><td></td><td></td><td></td></tr><tr><td>Conventional</td><td>0.331</td><td>0.052</td><td>0.278</td><td>0.257</td></tr><tr><td>HC0</td><td>0.417</td><td>0.203</td><td>0.247</td><td>0.231</td></tr><tr><td>HC1</td><td>0.447</td><td>0.218</td><td>0.223</td><td>0.208</td></tr><tr><td>HC2</td><td>0.523</td><td>0.26</td><td>0.177</td><td>0.164</td></tr><tr><td>HC3</td><td>0.636</td><td>0.321</td><td>0.13</td><td>0.12</td></tr><tr><td>max(Conventional, HC0)</td><td>0.448</td><td>0.172</td><td>0.188</td><td>0.171</td></tr><tr><td>max(Conventional, HC1)</td><td>0.473</td><td>0.19</td><td>0.173</td><td>0.157</td></tr><tr><td>max(Conventional, HC2)</td><td>0.542</td><td>0.238</td><td>0.141</td><td>0.128</td></tr><tr><td>max(Conventional, HC3)</td><td>0.649</td><td>0.305</td><td>0.107</td><td>0.097</td></tr><tr><td></td><td></td><td>B. Little Heteroskedasticity</td><td></td><td></td></tr><tr><td>^<br/>1</td><td>0.004</td><td>0.6</td><td></td><td></td></tr><tr><td>Standard Errors:</td><td></td><td></td><td></td><td></td></tr><tr><td>Conventional</td><td>0.52</td><td>0.07</td><td>0.098</td><td>0.084</td></tr><tr><td>HC0</td><td>0.441</td><td>0.193</td><td>0.217</td><td>0.202</td></tr><tr><td>HC1</td><td>0.473</td><td>0.207</td><td>0.194</td><td>0.179</td></tr><tr><td>HC2</td><td>0.546</td><td>0.25</td><td>0.156</td><td>0.143</td></tr><tr><td>HC3</td><td>0.657</td><td>0.312</td><td>0.114</td><td>0.104</td></tr><tr><td>max(Conventional, HC0)</td><td>0.562</td><td>0.121</td><td>0.083</td><td>0.07</td></tr><tr><td>max(Conventional, HC1)</td><td>0.578</td><td>0.138</td><td>0.078</td><td>0.067</td></tr><tr><td>max(Conventional, HC2)</td><td>0.627</td><td>0.186</td><td>0.067</td><td>0.057</td></tr><tr><td>max(Conventional, HC3)</td><td>0.713</td><td>0.259</td><td>0.053</td><td>0.045</td></tr><tr><td colspan="5">C. No Heteroskedasticity</td></tr><tr><td>^<br/>1</td><td>-0.003</td><td>0.611</td><td></td><td></td></tr><tr><td>Standard Errors:</td><td></td><td></td><td></td><td></td></tr><tr><td>Conventional</td><td>0.604</td><td>0.081</td><td>0.061</td><td>0.05</td></tr><tr><td>HC0</td><td>0.453</td><td>0.19</td><td>0.209</td><td>0.193</td></tr><tr><td>HC1</td><td>0.486</td><td>0.203</td><td>0.185</td><td>0.171</td></tr><tr><td>HC2</td><td>0.557</td><td>0.247</td><td>0.15</td><td>0.136</td></tr><tr><td>HC3</td><td>0.667</td><td>0.309</td><td>0.11</td><td>0.1</td></tr><tr><td>max(Conventional, HC0)</td><td>0.629</td><td>0.109</td><td>0.055</td><td>0.045</td></tr><tr><td>max(Conventional, HC1)</td><td>0.64</td><td>0.122</td><td>0.053</td><td>0.044</td></tr><tr><td>max(Conventional, HC2)</td><td>0.679</td><td>0.166</td><td>0.047</td><td>0.039</td></tr><tr><td>max(Conventional, HC3)</td><td>0.754</td><td>0.237</td><td>0.039</td><td>0.031</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

Note: The table reports results from a sampling experiment with 25,000 replications.

{259}------------------------------------------------

Table 8.2.1: Standard errors for class size e§ects in the STAR data

<table><tbody><tr><th colspan="4"></th></tr><tr><td></td><td colspan="3">Standard</td></tr><tr><td></td><td>Error</td></tr><tr><td>Robust (HC1)</td><td>0.09</td></tr><tr><td>Parametric Moulton Correction</td><td>0.222</td></tr><tr><td>(using Moulton intraclass coe¢ cient)</td><td></td></tr><tr><td>Parametric Moulton Correction</td><td>0.23</td></tr><tr><td>(using ANOVA intraclass coe¢ cient)</td><td></td></tr><tr><td>Clustered</td><td>0.232</td></tr><tr><td>Block Bootstrap</td><td>0.231</td></tr><tr><td>Estimation using group means</td><td>0.226</td></tr><tr><td>(weighted by class size)</td><td></td></tr></tbody></table>

Note: The table reports estimates from a regression of average percentile scores on class size for kindergartners using the public use data set from Project STAR. The coe¢ cient on class size is -.62. The group level for clustering is the classroom. The number of observations is 5,743. The bootstrap estimate uses 1,000 replications.

{260}------------------------------------------------

# Last words

If applied econometrics was easy, theorists would do it. But itís not as hard as the dense pages of Econometrica might lead you to believe. Carefully applied to coherent causal questions, regression and 2SLS almost always make sense. Your standard errors probably wonít be quite right, but they rarely are. Avoid embarrassment by being your own best skeptic - and, especially, Donít Panic!


{261}------------------------------------------------

LAST WORDS

{262}------------------------------------------------

# Acronyms

#### Technical terms

- 2SLS Two Stage Least Squares, an Instrumental Variables(IV) estimator [\(89\)](#page-104-0)
- ACR Average Causal Response, the weighted average causal response to an ordered treatment [\(136\)](#page-151-0)
- ANOVA Analysis of Variance, a decomposition of total variance into the variance of the Conditional Expectation Function (CEF) and the average conditional variance [\(26\)](#page-40-0)
- BRL Biased Reduced Linearization estimator, a bias-corrected covariance matrix estimator for clustered data [\(238\)](#page-253-0)
- CDF Cumulative Distribution Function, the probability that a random variable takes on a value less than or equal to a given number [\(72\)](#page-87-0)
- CEF Conditional Expectation Function, the population average of y<sup>i</sup> with X<sup>i</sup> held Öxed [\(23\)](#page-38-0)
- CIA Conditional Independence Assumption, a core assumption that justiÖes a causal interpretation of regression and matching estimators [\(39\)](#page-53-0)
- COP Conditional on Positive e§ect, the treatment-control di§erence in means for a non-negative random variable looking at positive values only [\(73\)](#page-88-0)
- CQF Conditional Quantile Function, deÖned for each quantile , the quantile of y<sup>i</sup> holding X<sup>i</sup> Öxed [\(204\)](#page-219-0)
- DD Di§erences in Di§erences estimator, in itís simplest form, a comparison of changes over time in treatment and control groups [\(169\)](#page-184-0)
- GLS Generalized Least Squares estimator, a regression estimator for models with heteroskedasticity and/or serial correlation; GLS provides e¢ ciency gains when the Conditional Expectation Function (CEF) is linear [\(69\)](#page-81-0)

{263}------------------------------------------------

248 ACRONYMS

GMM Generalized Method of Moments, an econometric estimation framework in which estimates are chosen to minimize a matrix-weighted average of the squared di§erence between sample and population moments [\(105\)](#page-120-0)

- HC<sup>0</sup> HC<sup>3</sup> Heteroskedasticity Consistent variance estimators proposed by MacKinnon and White (1985) [\(227\)](#page-241-0)
- ILS Indirect Least Squares estimator, the ratio of reduced form to Örst-stage coe¢ cients in an Instrumental Variables (IV) set-up [\(89\)](#page-104-1)
- ITT Intention to Treat e§ect, the e§ect of being o§ered treatment [\(122\)](#page-107-0)
- IV Instrumental Variables estimator [\(83\)](#page-98-0)
- LATE Local Average Treatment E§ect, the causal e§ect of treatment on compliers [\(114\)](#page-129-0)
- LDVs Limited Dependent Variables, e.g., dummies, counts, and non-negative random variables on the left-hand side of regression and related statistical models [\(70\)](#page-84-0)
- LIML Limited Information Maximum Likelihood estimator, an alternative to Two-Stage Least Squares (2SLS) with less bias [\(109\)](#page-124-0)
- LM Lagrange Multiplier test, a statistical test of the restrictions imposed by an estimator [\(108\)](#page-122-0)
- LPM Linear Probability Model [\(36\)](#page-50-0)
- MFX Marginal E§ects, in nonlinear models, the derivative of the Conditional Expectation Function (CEF) implied by the model with respect to the regressors [\(78\)](#page-92-0)
- MMSE Minimum Mean Squared Error, minimum expected squared prediction error, or the minimum of the expected square of the di§erence between an estimator and a target [\(25\)](#page-40-1)
- OLS Ordinary Least Squares estimator, the sample analog of the population regression vector [\(78\)](#page-92-0)
- OVB Omitted Variables Bias formula, the relationship between regression estimates in models with di§erent sets of control variables [\(44\)](#page-59-0)
- QTE Quantile Treatment E§ect, the causal e§ect of treatment on conditional quantiles of the outcome variable for compliers [\(215\)](#page-229-0)
- RD Regression Discontinuity design, an identiÖcation strategy in which treatment, the probability of treatment, or the average treatment intensity is a known, discontinuous function of a covariate [\(189\)](#page-204-0)
- SEM Simultaneous Equations Models, an econometric framework in which causal relationships between variables are described by several equations [\(84\)](#page-98-0)

{264}------------------------------------------------

- SSIV Split-Sample Instrumental Variables estimator, a version of the Two-Sample Instrumental Variables (TSIV) estimator [\(111\)](#page-125-0)
- TSIV Two-Sample Instrumental Variables estimator, an Instrumental Variables (IV) estimator that can sometimes be constructed from two data sets, when either data set alone would be inadequate [\(109\)](#page-124-1)
- VIV Visual Instrumental Variables, a plot of reduced-form against Örst-stage Ötted values in instrumental variables models with dummy instruments [\(103\)](#page-116-0)