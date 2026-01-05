# The Bias of 2SLSF

> Pages: 168-189

It is a fortunate fact that the OLS estimator is not only consistent, it is also unbiased. This means that in a sample of any size, the estimated OLS coe¢ cient vector has a distribution that is centered on the population coe¢ cient vector.[41](#page-168-0) The 2SLS estimator, in contrast, is consistent, but biased. This means that the 2SLS estimator only promises to be close the causal e§ect of interest in large samples. In small samples, the 2SLS estimator can di§er systematically from the population estimand.

For many years, applied researchers have lived with the knowledge that 2SLS is biased without losing too much sleep. Neither of us heard much about the bias of 2SLS in our graduate econometrics classes. A series of papers in the early 1990s changed this, however. These papers show that 2SLS estimates can be highly misleading in cases relevant for empirical practice.[42](#page-168-1)

The 2SLS estimator is most biased when the instruments are ìweak,î meaning the correlation with endogenous regressors is low, and when there are many over-identifying restrictions. When the instruments are both many and weak, the 2SLS estimator is biased towards the probability limit of the corresponding OLS estimate. In the worst-case scenario for many weak instruments, when the instruments are so weak that there really is no Örst-stage in the population, the 2SLS sampling distribution is centered on the probability limit of OLS. The theory behind this result is a little technical but the basic idea is easy to see. The source of the bias in 2SLS estimates is the randomness in estimates of the Örst-stage Ötted values. In practice, the Örst-stage estimates reáect some of the randomness in the endogenous variable since the Örst-stage coe¢ cients come from a regression of the endogenous variable on the instruments. If the population Örst-stage is zero, then all of the randomness in the Örst stage is due to the endogenous variable. This randomness turns into Önite-sample correlation between Örst-stage Ötted values and the second-stage errors, since the endogenous variable is correlated with the second-stage errors (or else you wouldnít be instrumenting in the Örst place).

A more formal derivation of 2SLS bias goes like this. To streamline the discussion we use matrices and vectors and a simple constant-e§ects model (itís di¢ cult to discuss bias in a heterogeneous e§ects world, since the target parameter may be variable across estimators). Suppose you are interested in estimating the e§ect of a single endogenous regressor, stored in a vector x, on a dependent variable, stored in the vector y, with no other covariates. The causal model of interest can then be written

<span id="page-168-2"></span>
$$y = \beta x + \eta. \tag{4.6.17}$$

Abadie, and nonlinear structural estimates of models for hours worked. Angrist (1991) compares 2SLS and bivariate Probit estimates in sampling experiments.

<span id="page-168-0"></span><sup>4 1</sup>A more precise statement is that OLS is unbiased when, either (a) the CEF is linear or, (b) the regressors are non-stochastic, i.e., Öxed in repeated samples. In practice, these qualiÖcations do not seem to matter much. As a rule, the sampling distribution of ^ = P <sup>i</sup> XiX<sup>0</sup> i <sup>1</sup> P <sup>i</sup>Xiyi; tends to be centered on the population analog,  = E[XiX<sup>0</sup> i ]1E[Xiyi] in samples of any size; whether or not the CEF is linear or the regressors are stochastic.

<span id="page-168-1"></span><sup>4 2</sup>Key references are Nelson and Startz, (1990a,b); Buse (1992), Bekker (1994); and especially Bound, Jaeger, and Baker (1995).

{169}------------------------------------------------

The Nq matrix of instrumental variables is Z, with the associated Örst-stage equation

$$x = Z\pi + \xi. \tag{4.6.18}$$

OLS estimates of [\(4.6.17\)](#page-168-2) are biased because <sup>i</sup> is correlated with <sup>i</sup> . The instruments, Z<sup>i</sup> are uncorrelated with <sup>i</sup> by construction and uncorrelated with <sup>i</sup> by assumption.

The 2SLS estimator is

$$\widehat{\beta}_{2SLS} = (x'P_Zx)^{-1} x'P_Zy = \beta + (x'P_Zx)^{-1} x'P_Z\eta.$$

where P<sup>Z</sup> = Z(Z <sup>0</sup>Z) <sup>1</sup>Z 0 is the projection matrix that produces Ötted values from a regression of x on Z. Substituting for x in x <sup>0</sup>PZ, we get

<span id="page-169-0"></span>
$$\widehat{\beta}_{2SLS} - \beta = (x'P_Z x)^{-1} (\pi'Z' + \xi') P_Z \eta = (x'P_Z x)^{-1} \pi'Z' \eta + (x'P_Z x)^{-1} \xi' P_Z \eta$$
(4.6.19)

The bias in 2SLS comes from the nonzero expectation of terms on the right hand side.

The expectation of [\(4.6.19\)](#page-169-0) is hard to evaluate because the expectation operator does not pass through the inverse (x <sup>0</sup>PZx) 1 , a nonlinear function. Itís possible to show, however, that the expectation of the ratios on the right hand side of [\(4.6.19\)](#page-169-0) can be closely approximated by the ratio of expectations. In other words,

$$E[\widehat{\beta}_{2SLS} - \beta] \approx (E[x'P_Zx])^{-1} E[\pi'Z'\eta] + (E[x'P_Zx])^{-1} E[\xi'P_Z\eta].$$

This approximation is much better than the usual Örst-order asymptotic approximation invoked in largesample theory, so we think of it as giving us a good measure of the Önite-sample behavior of the 2SLS estimator.[43](#page-169-1) Furthermore, because E[ 0Z 0 ] = 0 and E[ 0Z <sup>0</sup>] = 0, we have

<span id="page-169-2"></span>
$$E[\widehat{\beta}_{2SLS} - \beta] \approx \left[ E\left(\pi'Z'Z\pi\right) + E(\xi'P_Z\xi) \right]^{-1} E\left(\xi'P_Z\eta\right). \tag{4.6.20}$$

The approximate bias of 2SLS therefore comes from the fact that E <sup>0</sup>PZ is not zero unless <sup>i</sup> and <sup>i</sup> are uncorrelated. But correlation between <sup>i</sup> and <sup>i</sup> is what led us to use IV in the Örst place.

Further manipulation of [\(4.6.20\)](#page-169-2) generates an expression that is especially useful:

$$E[\widehat{\boldsymbol{\beta}}_{2SLS} - \boldsymbol{\beta}] \approx \frac{\sigma_{\eta\xi}}{\sigma_{\xi}^{2}} \left[ \frac{E\left(\pi'Z'Z\pi\right)/\mathbf{Q}}{\sigma_{\xi}^{2}} + 1 \right]^{-1}$$

<span id="page-169-1"></span><sup>4 3</sup> See Bekker (1994) and Angrist and Krueger (1995). This is also called a group-asymptotic approximation because it can be derived from an an asymptotic sequence that lets the number instruments go to inÖnity at the same time as the number of observations goes to inÖnity, thereby keeping the number of observations per instrument constant.

{170}------------------------------------------------

(see the appendix for a derivation). The term  $(1/\sigma_{\xi}^2)E(\pi'Z'Z\pi)/Q$  is the F-statistic for the joint significance of all regressors in the first stage regression.<sup>44</sup> Call this statistic F, so that we can write

<span id="page-170-1"></span>
$$E[\hat{\beta}_{2SLS} - \beta] \approx \frac{\sigma_{\eta\xi}}{\sigma_{\xi}^2} \frac{1}{F+1}.$$
 (4.6.21)

From this we see that as the first stage F-statistic gets small, the bias of 2SLS approaches  $\frac{\sigma_{\eta\xi}}{\sigma_{\xi}^2}$ . The bias of the OLS estimator is  $\frac{\sigma_{\eta\xi}}{\sigma_{x}^2}$ , which also equals  $\frac{\sigma_{\eta\xi}}{\sigma_{\xi}^2}$  if  $\pi=0$ . Thus, we have shown that 2SLS is centered on the same point as OLS when the first stage is zero. More generally, we can say 2SLS estimates are "biased towards" OLS estimates when there isn't much of a first stage. On the other hand, the bias of 2SLS vanishes when F gets large, as it should happen in large samples when  $\pi \neq 0$ .

When the instruments are weak, the F-statistic itself varies inversely with the number of instruments. To see why, consider adding useless instruments to your 2SLS model, that is, instruments with no effect on the first-stage R-squared. The model sum of squares,  $E\left(\pi'Z'Z\pi\right)$ , and the residual variance,  $\sigma_{\xi}^2$ , will both stay the same while Q goes up. The F-statistic becomes smaller as a result. From this we learn that the addition of many weak instruments increases bias.

Intuitively, the bias in 2SLS is a consequence of the fact that the first stage is estimated. If the first stage coefficients were known, we could use  $\hat{x}_{pop} = Z\pi$  for the first-stage fitted values. These fitted values are uncorrelated with the second stage error. In practice, however, we use  $\hat{x} = P_Z x = Z\pi + P_Z \xi$ , which differs from  $\hat{x}_{pop}$  by the term  $P_Z \xi$ . The bias in 2SLS arises from the fact that  $P_Z \xi$  is correlated with  $\eta$ , so some of the correlation between errors in the first and second stages seeps in to our 2SLS estimates through the sampling variability in  $\hat{\pi}$ . Asymptotically, this correlation is negligible, but real life does not play out in "asymptopia".

The bias formula, (4.6.21), shows that the bias in 2SLS is an increasing function of the number of instruments, so clearly bias is least in the just-identified case when the number of instruments is as low as it can get. It turns out, however, that just-identified 2SLS (say, the simple Wald estimator) is approximately unbiased. This is hard to show formally because just-identified 2SLS has no moments (i.e., the sampling distribution has fat tails). Nevertheless, even with weak instruments, just-identified 2SLS is approximately centered where it should be (we therefore say that just-identified 2SLS is median-unbiased). This is not to say that you can happily use weak instruments in just-identified models. With a weak instrument, just-identified IV estimates tend to be highly unstable and imprecise.

The LIML estimator is approximately median-unbiased for over-identified constant-effects models, and therefore provides an attractive alternative to just-identified estimation using one instrument at a time (see, e.g., Davidson and MacKinnon, 1993, and Mariano, 2001). LIML has the advantage of having the same

<span id="page-170-0"></span><sup>&</sup>lt;sup>44</sup>Sort of; the actual F-statistic is  $(1/\hat{\sigma}_{\xi}^2)\hat{\pi}'Z'Z\hat{\pi}/Q$ , where hats denote estimates.  $(1/\sigma_{\xi}^2)E(\pi'Z'Z\pi)/Q$  is therefore sometimes called the population F-statistic since it's the F-statistic we'd get in an infinitely large sample. In practice, the distinction between population and sample F matters little in this context.

{171}------------------------------------------------

large-sample distribution as 2SLS (under constant effects) while providing finite-sample bias reduction. A number of estimators reduce the bias in overidentified 2SLS models. But an extensive Monte Carlo study by Flores-Lagunes (2007) suggests that LIML does at least as well as the alternatives in a wide range of circumstances (in terms of bias, mean absolute error, and the empirical rejection rates for t-tests). Another advantage of LIML is that many statistical packages compute it while other estimators typically require some programming.<sup>45</sup>

We use a small Monte Carlo experiment to illustrate some of the theoretical results from the discussion above. The simulated data are drawn from the following model,

$$y_i = \beta x_i + \eta_i$$

$$x_i = \sum_{j=1}^{Q} \pi_j z_{ij} + \xi_i$$

with  $\beta = 1$ ,  $\pi_1 = 0.1$ ,  $\pi_j = 0 \ \forall j > 1$ ,

$$\left(\begin{array}{c} \eta_i \\ \xi_i \end{array}\right) \left| \, Z \sim N \left( \left(\begin{array}{c} 0 \\ 0 \end{array}\right), \left(\begin{array}{cc} 1 & 0.8 \\ 0.8 & 1 \end{array}\right) \right),$$

where the  $z_{ij}$  are independent, normally distributed random variables with mean zero and unit variance. The sample size is 1000.

Figure 4.6.1 shows the Monte Carlo distributions of four estimators: OLS, just identified IV (i.e. 2SLS with Q = 1, labeled IV), 2SLS with two instruments (for Q = 2, labeled 2SLS), and LIML with Q = 2. The OLS estimator is biased and centered around a value of about 1.79. IV is centered around 1, the value of  $\beta$ . 2SLS with one weak and one uninformative instrument is moderately biased towards OLS (the median is 1.07). The distribution function for LIML with Q = 2 is basically indistinguishable from that for just-identified IV, even though the LIML estimator uses a completely uninformative instrument.

Figure 4.6.2 reports simulation results where we set Q = 20. Thus, in addition to the one informative but weak instrument, we added 19 worthless instruments. The figure again shows OLS, 2SLS, and LIML distributions. The bias in 2SLS is now much worse (the median is 1.53, close to the OLS median). The sampling distribution of the 2SLS estimator is also much tighter than in the Q = 2 case. LIML continues to

<span id="page-171-0"></span><sup>&</sup>lt;sup>45</sup>LIML is available in SAS and in STATA 10. With weak instruments, LIML standard errors are not quite right, but Bekker (1994) gives a simple fix for this. Why is LIML unbiased? Expression (4.6.21) shows that the approximate bias of 2SLS is proportional to the bias of OLS. From this we conclude that there is a linear combination of OLS and 2SLS that is approximately unbiased. LIML turns out to be just such a "combination estimator". Like the bias of 2SLS, the approximate unbiasedness of LIML can be shown using a Bekker-style group-asymptotic sequence that fixes the ratio of instruments to sample size. Its worth mentioning, however, that LIML is biased in models with a certain type of heteroskedasticity; See Hausman, Newey, and Wouterson (2006) for details.

{172}------------------------------------------------

perform well and is centered around  = 1, with a bit more dispersion than in the q= 2 case.

Finally, Figure [4.6.3](#page-176-0) reports simulation results from a model that is truly unidentiÖed. In this case, we set <sup>j</sup> = 0; j = 1; :::; 20. Not surprisingly, all the sampling distributions are centered around the same value as OLS. On the other hand, the 2SLS sampling distribution is much tighter than the LIML distribution. We would say advantage-LIML in this case because the widely dispersed LIML sampling distribution correctly reáects the fact that the sample is uninformative about the parameter of interest.

What does this mean in practice? Besides retaining a vague sense of worry about your Örst stage, we recommend the following:

- 1. Report the Örst stage and think about whether it makes sense. Are the magnitude and sign as you would expect, or are the estimates too big or large but wrong-signed? If so, perhaps your hypothesized Örst-stage mechanism isnít really there, rather, you simply got lucky.
- 2. Report the F-statistic on the excluded instruments. The bigger this is, the better. Stock, Wright, and Yogo (2002) suggest that F-statistics above about 10 put you in the safe zone though obviously this cannot be a theorem.
- 3. Pick your best single instrument and report just-identiÖed estimates using this one only. Just-identiÖed IV is median-unbiased and therefore unlikely to be subject to a weak-instruments critique.
- 4. Check over-identiÖed 2SLS estimates with LIML. LIML is less precise than 2SLS but also less biased. If the results come out similar, be happy. If not, worry, and try to Önd stronger instruments.
- 5. Look at the coe¢ cients, t-statistics, and F-statistics for excluded instruments in the reduced-form regression of dependent variables on instruments. Remember that the reduced form is proportional to the causal e§ect of interest. Most importantly, the reduced-form estimates, since they are OLS, are unbiased. As Angrist and Krueger (2001) note, if you canít see the causal relation of interest in the reduced form, itís probably not there.[46](#page-172-0)

We illustrate some of this reasoning in a re-analysis of the Angrist and Krueger (1991) quarter-of-birth study. Bound, Jaeger, and Baker (1995) argued that bias is a major concern when using quarter birth as an instrument for schooling, in spite of the fact that sample size exceeds 300,000. ìSmall sampleî is clearly relative. Earlier in the chapter, we saw that the QOB pattern in schooling is clearly reáected in the reduced form, so there would seem to be little cause for concern. On the other hand, Bound, Jaeger, and Baker (1995) argue that the most relevant models have additional controls not included in these reduced forms. Table [4.6.2](#page-111-0) reproduces some of the speciÖcations from Angrist and Krueger (1991) as well as other speciÖcations in the spirit of Bound, Jaeger, and Baker (1995).

<span id="page-172-0"></span><sup>4 6</sup>A recent paper by Chernozhukov and Hansen (2007) formalizes this maxim.

{173}------------------------------------------------

<table><tbody><tr><th></th></tr><tr><td>to schooling</td></tr><tr><td>returns</td></tr><tr><td>economic</td></tr><tr><td>of the</td></tr><tr><td>estimates</td></tr><tr><td><math>\geq</math></td></tr><tr><td>ernative <math>\Gamma</math></td></tr><tr><td>41te</td></tr><tr><td>le <math>4.6.2</math>: <math>\neq</math></td></tr><tr><td>Tab</td></tr></tbody></table>

<table><tbody><tr><th>IV<br/>Alternative<br/>4.6.2:<br/>Table</th><th>estimates</th><th>the<br/>of</th><th>economic</th><th>to<br/>returns</th><th>schooling</th><th></th></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>2SLS</td><td>0.105</td><td>0.435</td><td>0.089</td><td>0.076</td><td>0.093</td><td>0.091</td></tr><tr><td></td><td>(0.020)</td><td>(0.450)</td><td>(0.016)</td><td>(0.029)</td><td>(0.009)</td><td>(0.011)</td></tr><tr><td>ML<br/>LI</td><td>0.106</td><td>0.539</td><td>0.093</td><td>0.081</td><td>0.106</td><td>0.110</td></tr><tr><td></td><td>(0.020)</td><td>(0.627)</td><td>(0.018)</td><td>(0.041)</td><td>(0.012)</td><td>(0.015)</td></tr><tr><td>instruments)<br/>(excluded<br/>F-statistic</td><td>32.27</td><td>0.42</td><td>4.91</td><td>1.61</td><td>2.58</td><td>1.97</td></tr><tr><td></td><td></td><td>Controls</td><td></td><td></td><td></td><td></td></tr><tr><td>birth<br/>of<br/>Year</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>birth<br/>of<br/>State</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>squared<br/>Age<br/>Age,</td><td></td><td>X</td><td></td><td>X</td><td></td><td>X</td></tr><tr><td></td><td>Excluded</td><td>Instruments</td><td></td><td></td><td></td><td></td></tr><tr><td>birth<br/>of<br/>Quarter</td><td>X</td><td>X</td><td></td><td></td><td></td><td></td></tr><tr><td>birth<br/>of<br/>birth*year<br/>of<br/>Quarter</td><td></td><td></td><td>X</td><td>X</td><td>X</td><td>X</td></tr><tr><td>birth<br/>of<br/>birth*state<br/>of<br/>Quarter</td><td></td><td></td><td></td><td></td><td>X</td><td>X</td></tr><tr><td>instruments<br/>excluded<br/>of<br/>Number</td><td>3</td><td>2</td><td>30</td><td>28</td><td>180</td><td>178</td></tr><tr><td>2SLS<br/>compares<br/>table<br/>The<br/>Notes:</td><td>ML<br/>LI<br/>and</td><td>estimates</td><td>using</td><td>alternative</td><td>of<br/>sets</td><td></td></tr><tr><td>OLS<br/>The<br/>controls.<br/>and<br/>instruments</td><td>estimate</td><td>corresponding</td><td>the<br/>to</td><td>models</td><td>reported</td><td></td></tr><tr><td>OLS<br/>the<br/>.071;<br/>is<br/>1-4<br/>columns<br/>in</td><td>estimate</td><td>corresponding</td><td>the<br/>to</td><td>models</td><td>in<br/>reported</td><td></td></tr><tr><td>from<br/>are<br/>Data<br/>.067.<br/>is<br/>5-6<br/>columns</td><td>Angrist<br/>the</td><td>and</td><td>Krueger</td><td>1980<br/>(1991)</td><td>Census</td><td></td></tr><tr><td>329,509.<br/>is<br/>size<br/>sample<br/>The<br/>sample.</td><td>Standard</td><td>are<br/>errors</td><td>reported</td><td>in</td><td>parentheses.</td><td></td></tr></tbody></table>

{174}------------------------------------------------

The Örst column in the table reports 2SLS and LIML estimates of a model using three quarter of birth dummies as instruments with year of birth dummies as covariates. The OLS estimate for this speciÖcation is 0.071, while the 2SLS estimate is a bit higher at 0.105. The Örst-stage F-statistic is over 32, well above the danger zone. Not surprisingly, the LIML estimate is almost identical to 2SLS in this case.

Angrist and Krueger (1991) experimented with models that include age and age squared measured in quarters as additional controls. These controls are meant to pick up omitted age e§ects that might confound the quarter-of-birth instruments. The addition of age and age squared reduces the number of instruments to two, since age in quarters, year of birth, and quarter of birth are linearly dependent. As shown in column 2, the Örst stage F-statistic drops to 0.4 when age and age squared are included as controls, a sure sign of trouble. But the 2SLS standard error is high enough that we would not draw any substantive conclusions from this estimate. The LIML estimate is even less precise. This model is e§ectively unidentiÖed.

Columns 3 and 4 report the results of adding interactions between quarter of birth dummies and year of birth dummies to the instrument list, so that there are 30 instruments, or 28 when the age and age squared variables are included. The Örst stage F-statistics are 4.9 and 1.6 in these two speciÖcations. The 2SLS estimates are a bit lower than in column 1 and hence closer to OLS. But LIML is not too far away from 2SLS. Although the LIML standard error is pretty big in column 4, it is not so large that the estimate is uninformative. On balance, there seems to be little cause for worry about weak instruments, even with the age quadratic included.

The most worrisome speciÖcations are those reported in columns 5 and 6. These estimates were produced by adding 150 interactions between quarter of birth and state of birth to the 30 interactions between quarter of birth and year of birth. The rationale for the inclusion of state-of-birth interactions in the instrument list is to exploit di§erences in compulsory schooling laws across states. But this leads to highly over-identiÖed models with 180 (or 178) instruments, many of which are weak. The Örst stage F-statistics for these models are 2.6 and 2.0, well into the discomfort zone. On the plus side, the LIML estimates again look fairly similar to 2SLS. Moreover, the LIML standard errors di§er little from the 2SLS standard errors in this case. This suggests that you canít always determine instrument relevance using a mechanical rule such as "F>10". In some cases, a low F may not be fatal.[47](#page-174-0)

Finally, itís worth noting that in applications with multiple endogenous variables, the conventional Örststage F is no longer appropriate. To see why, suppose there are two instruments for two endogenous variables and that the Örst instrument is strong and predicts both endogenous variables well while the second instrument is weak. The Örst-stage F-statistics in each of the two Örst stage equations are likely to be high but the model is weakly identiÖed because one instrument is not enough to capture two causal e§ects. A simple modiÖcation of the Örst-stage F for this case is given in the appendix.

<span id="page-174-0"></span><sup>4 7</sup> Cruz and Moreira (2005) similarly conclude that, low F-statistics notwithstanding, there is little bias in the Angrist and Krueger (1991) 180-instrument speciÖcations.

{175}------------------------------------------------

![](_page_175_Figure_2.jpeg)

Figure 4.6.1: Distribution of the OLS, IV, 2SLS, and LIML estimators. IV uses one instrument, while 2SLS and LIML use two instruments.

# 4.7 Appendix

#### Derivation of Equation [\(4.6.8\)](#page-160-0)

Rewrite equation [\(4.6.7\)](#page-160-1) as follows

$$Y_{ij} = \mu^* + \pi_0 \tau_i + (\pi_0 + \pi_1) \overline{S}_j + \nu_i;$$

where <sup>i</sup> s<sup>i</sup> S<sup>j</sup> : Since <sup>i</sup> and S<sup>j</sup> are uncorrelated by construction, we have:

$$\rho_1 = \pi_0 + \pi_1.$$

$$\pi_0 = \frac{C(\tau_i, Y_{ij})}{V(\tau_i)}.$$

Simplifying the second line,

$$\pi_0 = \frac{C[(s_i - \overline{S}_j), Y_{ij}]}{[V(s_i) - V(\overline{S}_j)]}$$

$$= \left[\frac{C(s_i, Y_{ij})}{V(s_i)}\right] \left[\frac{V(s_i)}{V(s_i) - V(\overline{S}_j)}\right] - \left[\frac{C(\overline{S}_j, Y_{ij})}{V(\overline{S}_j)}\right] \left[\frac{V(\overline{S}_j)}{V(s_i) - V(\overline{S}_j)}\right]$$

$$= \rho_0 \phi + \rho_1 (1 - \phi) = \rho_1 + \phi(\rho_0 - \rho_1)$$

where V (si) V (si)V (S<sup>j</sup> ) : Solving for 1, we have

$$\pi_1 = \rho_1 - \pi_0 = \phi(\rho_1 - \rho_0).$$

{176}------------------------------------------------

4.7. APPENDIX 161

![](_page_176_Figure_1.jpeg)

Figure 4.6.2: Distribution of the OLS, 2SLS, and LIML estimators with 20 instruments

![](_page_176_Figure_3.jpeg)

<span id="page-176-0"></span>Figure 4.6.3: Distribution of the OLS, 2SLS, and LIML estimators with 20 worthless instruments

{177}------------------------------------------------

#### Derivation of the approximate bias of 2SLS

Start from the last equality in [\(4.6.20\)](#page-169-2):

$$E[\widehat{\beta}_{2SLS} - \beta] \approx \left[ E\left(\pi'Z'Z\pi\right) + E\left(\xi'P_Z\xi\right) \right]^{-1} E\left(\xi'P_Z\eta\right).$$

The magic of linear algebra helps us simplify this expression: The term <sup>0</sup>PZ is a scalar and therefore equal to its trace; the trace is a linear operator which passes through expectations and is invariant to cyclic permutations; Önally, the trace of PZ, an idempotent matrix, is equal to itís rank, q. Using these facts, we have

$$E(\xi' P_Z \xi) = E[\operatorname{tr}(\xi' P_Z \xi)]$$

$$= E[\operatorname{tr}(P_Z \xi \xi')]$$

$$= \operatorname{tr}(P_Z E[\xi \xi'])$$

$$= \operatorname{tr}(P_Z \sigma_{\xi}^2 I)$$

$$= \sigma_{\xi}^2 \operatorname{tr}(P_Z)$$

$$= \sigma_{\xi}^2 Q,$$

where we have assumed that <sup>i</sup> is homoskedastic. Similarly, applying the trace trick to <sup>0</sup>PZ shows that this term is equal to q. Therefore,

$$E[\widehat{\beta}_{2SLS} - \beta] \approx \left[ E \left( \pi' Z' Z \pi \right) + \sigma_{\xi}^{2} Q \right]^{-1} E \left[ \text{tr} \left( \xi' P_{Z} \eta \right) \right]$$

$$= \sigma_{\eta \xi} Q \left[ E \left( \pi' Z' Z \pi \right) + \sigma_{\xi}^{2} Q \right]^{-1}$$

$$= \frac{\sigma_{\eta \xi}}{\sigma_{\xi}^{2}} \left[ \frac{E \left( \pi' Z' Z \pi \right) / Q}{\sigma_{\xi}^{2}} + 1 \right]^{-1}.$$

#### Multivariate Örst-stage F-statistics

Assume any exogenous covariates have been partialled out of the instrument list and that there are two endogenous variables, x<sup>1</sup> and x<sup>2</sup> with coe¢ cients <sup>1</sup> and 2. We are interested in the bias of the 2SLS estimator of <sup>2</sup> when x<sup>1</sup> is also treated as endogenous. The second stage equation is

<span id="page-177-0"></span>
$$y = P_Z x_1 \delta_1 + P_Z x_2 \delta_2 + [\eta + (x_1 - P_Z x_1) \delta_1 + (x_2 - P_Z x_2) \delta_2]. \tag{4.7.1}$$

where PZx<sup>1</sup> and PZx<sup>2</sup> are the Örst-stage Ötted values from regressions of x<sup>1</sup> and x<sup>2</sup> on Z. By the usual anatomy formula for multivariate regression, <sup>2</sup> in [\(4.7.1\)](#page-177-0) is the bivariate regression of y on the residual from

{178}------------------------------------------------

4.7. APPENDIX 163

a regression of PZx<sup>2</sup> on PZx1. This residual is

$$[I - P_Z x_1 (x_1' P_Z x_1)^{-1} x_1' P_Z] P_Z x_2 = M_{1z} P_Z x_2,$$

where M1<sup>z</sup> = [I PZx1(x 0 <sup>1</sup>PZx1) <sup>1</sup>x 0 <sup>1</sup>PZ] is the relevant residual-maker matrix. In addition, note that M1<sup>z</sup>PZx<sup>2</sup> = PZ[M1<sup>z</sup>x2]:

From here we conclude that the 2SLS estimator of <sup>2</sup> is the OLS regression on PZ[M1<sup>z</sup>x2]; in other words, OLS on the Ötted values from a regression of M1<sup>z</sup>x<sup>2</sup> on Z. This is the same as 2SLS using P<sup>Z</sup> to instrument M1<sup>z</sup>x2. So the 2SLS estimator of <sup>2</sup> can be written

$$[x_2'M_{1z}P_ZM_{1z}x_2]^{-1}x_2'M_{1z}P_Zy = \delta_2 + [x_2'M_{1z}P_ZM_{1z}x_2]^{-1}x_2'M_{1z}P_Z\eta.$$

The explained sum of squares (numerator of the F-statistic) that determines the bias of the 2SLS estimator of <sup>2</sup> is therefore the expectation of [x <sup>2</sup>M1<sup>z</sup>PZM1<sup>z</sup>x2], while the bias comes from the fact that the expectation E[ <sup>0</sup>M1<sup>z</sup>PZ] is non-zero when and are correlated.

Hereís how to compute this F-statistic in practice: (a) Regress the Örst stage Ötted values for the regressor of interest, PZx2, on the other Örst-stage Ötted values and any exogenous covariates. Save the residuals from this step; (b) Construct the F-statistic for excluded instruments in a Örst-stage regression of the residuals from (a) on the excluded instruments. Note that you should get the 2SLS coe¢ cient of interest in a 2SLS procedure where the residuals from (a) are instrumented using Z, with no other covariates or endogenous variables. Use this fact to check your calculation.

{179}------------------------------------------------

{180}------------------------------------------------

# Chapter 5

Parallel Worlds: Fixed E§ects,

Di§erences-in-di§erences, and Panel

# Data

The Örst thing to realize about parallel universes . . . is that they are not parallel.

Douglas Adams, Mostly Harmless (1995)

The key to causal inference in chapter [3](#page-36-0) is control for observed confounding factors. If important confounders are unobserved, we might try to get at causal e§ects using IV as discussed in Chapter [4.](#page-98-0) Good instruments are hard to Önd, however, so weíd like to have other tools to deal with unobserved confounders. This chapter considers a variation on the control theme: strategies that use data with a time or cohort dimension to control for unobserved-but-Öxed omitted variables. These strategies punt on comparisons in levels, while requiring the counterfactual trend behavior of treatment and control groups to be the same. We also discuss the idea of controlling for lagged dependent variables, another strategy that exploits timing.

# 5.1 Individual Fixed E§ects

One of the oldest questions in Labor Economics is the connection between union membership and wages. Do workers whose wages are set by collective bargaining earn more because of this, or would they earn more anyway? (Perhaps because they are more experienced or skilled). To set this question up, let yit equal the (log) earnings of worker i at time t and let dit denote his union status. The observed yit is either y0it or y1it, depending on union status. Suppose further that

$$E(\mathbf{Y}_{0it}|A_i, \mathbf{X}_{it}, t, \mathbf{D}_{it}) = E(\mathbf{Y}_{0it}|A_i, \mathbf{X}_{it}, t),$$


{181}------------------------------------------------

i.e. union status is as good as randomly assigned conditional on unobserved worker ability, A<sup>i</sup> , and other observed covariates Xit, like age and schooling.

The key to Öxed-e§ects estimation is the assumption that the unobserved A<sup>i</sup> appears without a time subscript in a linear model for E(y0itjA<sup>i</sup> ;Xit; t) :

$$E(\mathbf{Y}_{0it}|A_i, \mathbf{X}_{it}, t) = \alpha + \lambda_t + A_i'\gamma + \mathbf{X}_{it}\delta, \tag{5.1.1}$$

Finally, we assume that the causal e§ect of union membership is additive and constant:

$$E(\mathbf{Y}_{1it}|A_i,\mathbf{X}_{it},t) = E(\mathbf{Y}_{0it}|A_i,\mathbf{X}_{it},t) + \rho.$$

This implies

<span id="page-181-0"></span>
$$E(\mathbf{Y}_{it}|A_i, \mathbf{X}_{it}, t, \mathbf{D}_{it}) = \alpha + \lambda_t + \rho \mathbf{D}_{it} + A_i' \gamma + \mathbf{X}_{it} \delta,$$
(5.1.2)

where is the causal e§ect of interest. The set of assumptions leading to [\(5.1.2\)](#page-181-0) is more restrictive those we used to motivate regression in Chapter [3;](#page-36-0) we need the linear, additive functional form to make headway on the problem of unobserved confounders using panel data with no instruments.[1](#page-181-1)

Equation [\(5.1.2\)](#page-181-0) implies

<span id="page-181-3"></span>
$$Y_{it} = \alpha_i + \lambda_t + \rho D_{it} + X_{it} \delta + \varepsilon_{it}. \tag{5.1.3}$$

where

$$\alpha_i \equiv \alpha + A_i' \gamma.$$

This is a Öxed-e§ects model. Given panel data, i.e., repeated observations on individuals, the causal e§ect of union status on wages can be estimated by treating <sup>i</sup> , the Öxed e§ect, as a parameter to be estimated. The year e§ect, t; is also treated as a parameter to be estimated. The unobserved individual e§ects are coe¢ cients on dummies for each individual while the year e§ects are coe¢ cients on time dummies.[2](#page-181-2)

It might seem like there are an awful lot of parameters to be estimated in the Öxed e§ects model. For

$$E(\mathbf{Y}_{1it} - \mathbf{Y}_{0it}|A_i, \mathbf{X}_{it}, t) = \rho_i.$$

See, e.g., Wooldridge (2005), who discusses estimators for the average of <sup>i</sup> :

<span id="page-181-2"></span><sup>2</sup>An alternative to the Öxed-e§ects speciÖcation is "random e§ects" (See, e.g., Wooldridge, 2006). The random-e§ects model assumes that <sup>i</sup> is uncorrelated with the regressors. Because the omitted variable in a random-e§ects model is uncorrelated with included regressors there is no bias from ignoring it - in e§ect, it becomes part of the residual. The most important consequence of random e§ects is that the residuals for a given person are correlated across periods. Chapter [8](#page-236-0) discusses the implications of this for standard errors. An alternative approach is GLS, which promises to be more e¢ cient if the assumptions of the random-e§ects model are satisÖed (linear CEF, homoskedasticity). We prefer OLS/Öx-the-standard-errors to GLS under random-e§ects assumptions. As discussed in Section [3.4.1,](#page-81-0) GLS requires stronger assumptions than those we are comfortable with and the resulting e¢ ciency gain is likely to be modest.

<span id="page-181-1"></span><sup>1</sup> In some cases, we can allow heterogeneous treatment e§ects so that

{182}------------------------------------------------

example, the Panel Survey of Income Dynamics, a widely-used panel data set, includes about 5,000 workingage men observed for about 20 years. So there are roughly 5,000 Öxed e§ects. In practice, however, this doesnít matter. Treating the individual e§ects as parameters to be estimated is algebraically the same as estimation in deviations from means. In other words, Örst we calculate the individual averages

$$\overline{\mathbf{Y}}_i = \alpha_i + \overline{\lambda} + \rho \overline{\mathbf{D}}_i + \overline{\mathbf{X}}_i \delta + \overline{\varepsilon}_i.$$

Subtracting this from [\(5.1.3\)](#page-181-3) gives

<span id="page-182-3"></span>
$$Y_{it} - \overline{Y}_i = \lambda_t - \overline{\lambda} + \rho \left( D_{it} - \overline{D}_i \right) + \left( X_{it} - \overline{X}_i \right) \delta + (\varepsilon_{it} - \overline{\varepsilon}_i), \tag{5.1.4}$$

so deviations from means kills the unobserved individual e§ects.[3](#page-182-0)

An alternative to deviations from means is di§erencing. In other words, we estimate,

<span id="page-182-2"></span>
$$\Delta Y_{it} = \Delta \lambda_t + \rho \Delta D_{it} + \Delta X_{it} \delta + \Delta \varepsilon_{it}, \qquad (5.1.5)$$

where the preÖx denotes the change from one year to the next. For example, yit =yityit<sup>1</sup>: With two periods, di§erencing is algebraically the same as deviations from means, but not otherwise. Both should work, although with homoskedastic and serially uncorrelated "it deviations from means is more e¢ cient. You might Önd di§erencing more convenient if you have to do it by hand, though the di§erenced standard errors should be adjusted for the fact that the di§erenced residuals are serially correlated.

Some regression packages automate the deviations-from-means estimator, with an appropriate standarderror adjustment for the degrees of freedoms lost in estimating N individual means. This is all thatís needed to get the standard errors right with a homoskedastic, serially uncorrelated residual. The deviations-frommeans estimator has many names, including the "within estimator" and "analysis of covariance". Estimation in deviations-from-means form is also called absorbing the Öxed e§ects.[4](#page-182-1)

Freeman (1984) uses four data sets to estimate union wage e§ects under the assumption that selection into union status is based on unobserved-but-Öxed individual characteristics. Table [5.1.1](#page-183-0) displays some of his estimates. For each data set, the table displays results from a Öxed-e§ects estimator and the corresponding cross-section estimates. The cross section estimates are typically higher (ranging from .15-.25) than the

<span id="page-182-0"></span><sup>3</sup>Why is deviations from means the same as estimating each Öxed e§ect in [\(5.1.3\)](#page-181-3)? Because, by the regression anatomy formula, [\(3.1.3\)](#page-42-0), any set of multivariate regression coe¢ cients can be estimated in two steps. To get the multivariate coe¢ cient on one set of variables, Örst regress them on all the other included variables, then regress the original dependent variable on the residuals from this Örst step. The residuals from a regression on a full set of person-dummies in a person-year panel are deviations from person means.

<span id="page-182-1"></span><sup>4</sup> The Öxed e§ects are not estimated consistently in a panel where the number of periods <sup>T</sup> is Öxed while <sup>N</sup> ! 1. This is called the "incidental parameters problem," a name which reáects the fact that the number of parameters grows with the sample size. Nevertheless, other parameters in the Öxed e§ects model - the ones we care about - are consistently estimated.

{183}------------------------------------------------

Öxed e§ects estimates (ranging from .10-.20). This may indicate positive selection bias in the cross-section estimates, though selection bias is not the only explanation for the lower Öxed-e§ects estimates.

<span id="page-183-0"></span>Table 5.1.1: Estimated e§ects of union status on log wages

<table><tbody><tr><th>Survey</th><th>Cross section estimate</th><th>Fixed e§ects estimate</th></tr><tr><td>May CPS, 1974-75</td><td>0.19</td><td>0.09</td></tr><tr><td>National Longitudinal Survey of Young Men, 1970-78</td><td>0.28</td><td>0.19</td></tr><tr><td>Michigan PSID, 1970-79</td><td>0.23</td><td>0.14</td></tr><tr><td>QES, 1973-77</td><td>0.14</td><td>0.16</td></tr></tbody></table>

Notes: Adapted from Freeman (1984). The table reports cross-section and panel estimates of the union relative wage e§ect. The estimates were calculated using the surveys listed at left. The cross-section estimates include controls for demographic and human capital variables.

Although they control for a certain type of omitted variable, Öxed-e§ects estimates are notoriously susceptible to attenuation bias from measurement error. On one hand, economic variables like union status tend to be persistent (a worker who is a union member this year is most likely a union member next year). On the other hand, measurement error often changes from year-to-year (union status may be misreported or miscoded this year but not next year). Therefore, while union status may be misreported or miscoded for only a few workers in any single year, the observed year-to-year changes in union status may be mostly noise. In other words, there is more measurement error in the regressors in an equation like [\(5.1.5\)](#page-182-2) or [\(5.1.4\)](#page-182-3) than in the levels of the regressors. This fact may account for smaller Öxed-e§ects estimates.[5](#page-183-1)

A variant on the measurement-error problem arises from that fact that the di§erencing and deviationsfrom-means estimators used to control for Öxed e§ects typically remove both good and bad variation. In other words, these transformations may kill some of the omitted-variables-bias bathwater, but they also remove much of the useful information in the baby - the variable of interest. An example is the use of twins to estimate the causal e§ect of schooling on wages. Although there is no time dimension to this problem, the basic idea is the same as the union problem discussed above: twins have similar but largely unobserved family and genetic backgrounds. We can therefore control for their common family background by including a family Öxed e§ect in samples of pairs of twins.

Ashenfelter and Krueger (1994) and Ashenfelter and Rouse (1998) estimate the returns to schooling using samples of twins, controlling for family Öxed e§ects. Because there are two twins from each family, this is the same as regressing di§erences in earnings within twin-pairs on di§erences in their schooling. Surprisingly, the with-family estimates come our larger than OLS. But how do di§erences in schooling come about between individuals who are otherwise so much alike? Bound and Solon (1999) point out that there are small di§erences between twins, with Örst-borns typically having higher birth weight and higher IQ scores (here di§erences in birth timing are measured in minutes). While these within-twin di§erences are not large,

<span id="page-183-1"></span><sup>5</sup> See Griliches and Hausman (1986) for a more complete analysis of measurement error in panel data.

{184}------------------------------------------------

neither is the di§erence in their schooling. Hence, a small amount of unobserved ability di§erences among twins could be responsible for substantial bias in the resulting estimates.

What should be done about measurement error and related problems in models with Öxed e§ects? A possible Öx-up for measurement error is instrumental variables. Ashenfelter and Krueger (1994) use crosssibling reports to construct instruments for schooling di§erences across twins. For example, they use each twinís report of his brotherís schooling as an instrument for self-reports. A second approach is to bring in external information on the extent of measurement error and adjust naive estimates accordingly. In a study of union wage e§ects, Card (1996) uses external information from a separate validation survey to adjust panel-data estimates for measurement error in reported union status. But data from multiple reports and repeated measures of the sort used by Ashenfelter and Rouse (1994) and Card (1996) are unusual. At a minimum, therefore, itís important to avoid overly strong claims when interpreting Öxed-e§ects estimates (never bad advice for an applied econometrician in any case).

# 5.2 Di§erences-in-di§erences: Pre and Post, Treatment and Control

The Öxed e§ects strategy requires panel data, that is, repeated observations on the same individuals (or Örms or whatever the unit of observation might be). Often, however, the regressor of interest varies only at a more aggregate level such as state or cohort. For example, state policies regarding health care beneÖts for pregnant workers or minimum wages change across states but not within states. The source of omitted variables bias when evaluating these policies must therefore be unobserved variables at the state and year level.

To make this concrete, suppose we are interested in the e§ect of the minimum wage on employment, a classic question in Labor Economics. In a competitive labor market, increases in the minimum wage move us up a downward-sloping demand curve. Higher minimums therefore reduce employment, perhaps hurting the very workers minimum-wage policies were designed to help. Card and Krueger (1994) use a dramatic change in the New Jersey state minimum wage to see if this is true.

On April 1, 1992, New Jersey raised the state minimum from \$4.25 to \$5.05. Card and Krueger collected data on employment at fast food restaurants in New Jersey in February 1992 and again in November 1992. These restaurants (Burger King, Wendyís, and so on) are big minimum-wage employers. Card and Krueger collected data from the same type of restaurants in eastern Pennsylvania, just across the Delaware river. The minimum wage in Pennsylvania stayed at \$4.25 throughout this period. They used their data set to compute di§erences-in-di§erences (DD) estimates of the e§ects of the New Jersey minimum wage increase. That is, they compared the change in employment in New Jersey to the change in employment in Pennsylvania around the time New Jersey raised its minimum.

{185}------------------------------------------------

DD is a version of Öxed-e§ects estimation using aggregate data.[6](#page-185-0) To see this, let

y1ist = fast food employment at restaurant i and period t if there is a high state minimum wage

y0ist = fast food employment at restaurant i and period t if there is a low state minimum wage

These are potential outcomes - in practice, we only get to see one or the other. Fort example, we see y1ist in New Jersey in November of 1992. The heart of the DD setup is an additive structure for potential outcomes in the no-treatment state. SpeciÖcally, we assume that

$$E(\mathbf{Y}_{0ist}|s,t) = \gamma_s + \lambda_t \tag{5.2.1}$$

where s denotes state (New Jersey or Pennsylvania) and t denotes period (February, before the minimum wage increase or November, after the increase). This equations says that in the absence of a minimum wage change, employment is determined by the sum of a time-invariant state e§ect and a year e§ect that is common across states. The additive state e§ect plays the role of the unobserved individual e§ect in the previous subsection.

Let dst be a dummy for high-minimum-wage states, where states are index by s and observed in period t. Assuming that E(y1ist y0istjs; t) is a constant, denoted , we have:

<span id="page-185-1"></span>
$$Y_{ist} = \gamma_s + \lambda_t + \beta D_{st} + \varepsilon_{ist}$$
 (5.2.2)

where E("istjs; t) = 0. From here, we get

$$E[Y_{ist}|s = PA, t = Nov] - E(Y_{ist}|s = PA, t = Feb) = \lambda_{Nov} - \lambda_{Feb}$$

and

$$E(Y_{ist}|s = NJ, t = Nov) - E(Y_{ist}|s = NJ, t = Feb) = \lambda_{Nov} - \lambda_{Feb} + \beta.$$

The population di§erence-in-di§erences,

$$[E(\mathbf{Y}_{ist}|s=PA,t=Nov) - E(\mathbf{Y}_{ist}|s=PA,t=Feb)]$$

$$-\left[E(\mathbf{Y}_{ist}|s=NJ,t=Nov)-E(\mathbf{Y}_{ist}|s=NJ,t=Feb)\right]=\beta,$$

<span id="page-185-0"></span><sup>6</sup> The DD idea is at least as old as IV. Kennan (1995) references a 1915 BLS report using DD to study the employment e§ects of the minimum wage (Obenauer and von der Nienburg, 1915).

{186}------------------------------------------------

is the causal e§ect of interest. This is easily estimated using the sample analog of the population means.

<table><tbody><tr><th></th><th></th><th></th><th></th></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td>Table 5.2.1: Average employment per store before and after the New Jersey minimum wage increase</td><td></td><td></td><td></td></tr></tbody></table>

<table><tbody><tr><th></th><th></th><th>PA</th><th>NJ</th><th>Di§erence, NJ-PA</th></tr><tr><td></td><td>Variable</td><td>(i)</td><td>(ii)</td><td>(iii)</td></tr><tr><td>1.</td><td>FTE employment before,</td><td>23.33</td><td>20.44</td><td>-2.89</td></tr><tr><td></td><td>all available observations</td><td>(1.35)</td><td>(0.51)</td><td>(1.44)</td></tr><tr><td>2.</td><td>FTE employment after,</td><td>21.17</td><td>21.03</td><td>-0.14</td></tr><tr><td></td><td>all available observations</td><td>(0.94)</td><td>(0.52)</td><td>(1.07)</td></tr><tr><td>3.</td><td>Change in mean FTE</td><td>-2.16</td><td>0.59</td><td>2.76</td></tr><tr><td></td><td>employment</td><td>(1.25)</td><td>(0.54)</td><td>(1.36)</td></tr></tbody></table>

Notes: Adapted from Card and Krueger (1994), Table 3. The table reports average full-time equivalent (FTE) employment at restaurants in Pennsylvania and New Jersey before and after a minimum wage increase in New Jersey. The sample consists of all stores with data on employment. Employment at six closed stores is set to zero. Employment at four temporarily closed stores is treated as missing. Standard errors are reported in parentheses

Table [5.2.1](#page-183-0) (based on Table 3 in Card and Krueger, 1994) shows average employment at fast food restaurants in New Jersey and Pennsylvania before and after the change in the New Jersey minimum wage. There are four cells in the Örst two rows and columns, while the margins show state di§erences in each period, the changes over time in each state, and the di§erence-in-di§erences. Employment in Pennsylvania restaurants is somewhat higher than in New Jersey in February but falls by November. Employment in New Jersey, in contrast, increases slightly. These two changes produce a positive di§erence-in-di§erences, the opposite of what we might expect if a higher minimum wage pushes businesses up the labor demand curve.

How convincing is this evidence against the standard labor-demand story? The key identifying assumption here is that employment trends would be the same in both states in the absence of treatment. Treatment induces a deviation from this common trend, as illustrated in Ögure [5.2.1.](#page-187-0) Although the treatment and control states can di§er, this di§erence in captured by the state Öxed e§ect, which plays the same role as the unobserved individual e§ect in [\(5.1.3\)](#page-181-3).[7](#page-186-0)

The common trends assumption can be investigated using data on multiple periods. In an update of their

$$E(\log Y_{0ist}|s,t) = \gamma_s + \lambda_t.$$

Note, however, that if there is a common trend in logs, there will not be one in levels and vice versa. Athey and Imbens (2006) introduce a semi-parametric DD estimator that allows for common trends after an unknown transformation, which they propose to use the data to estimate. Poterba, Venti and Wise (1995) and Meyer, Viscusi, and Durbin (1995) discuss DD-type models for quantiles.

<span id="page-186-0"></span><sup>7</sup> The common trends assumption can be applied to transformed data, for example,

{187}------------------------------------------------

![](_page_187_Figure_2.jpeg)

<span id="page-187-0"></span>Figure 5.2.1: Causal e§ects in the di§erences-in-di§erences model

original minimum wage study, Card and Krueger (2000) obtained administrative payroll data for restaurants in New Jersey and Pennsylvania for a number of years. These data are shown here in Figure [5.2.2,](#page-188-0) similar to Figure 2 in their follow-up study. The vertical lines indicate the dates when their original surveys were conducted, and the third vertical line denotes the increase in the federal minimum wage to \$4.75 in October 1996, which a§ected Pennsylvania but not New Jersey. These data give us an opportunity to look at a new minimum wage "experiment".

Like the original Card and Krueger survey, the administrative data show a slight decline in employment from February to November 1992 in Pennsylvania, and little change in New Jersey over the same period. However, the data also reveal fairly substantial year-to-year employment variation in other periods. These swings often seem to di§er substantially in the two states. In particular, while employment levels in New Jersey and Pennsylvania were similar at the end of 1991, employment in Pennsylvania fell relative to employment in New Jersey over the next three years (especially in the 14-county group), mostly before the 1996 change in Federal minimum. So Pennsylvania may not provide a very good measure of counterfactual employment rates in New Jersey in the absence of a policy change, and vice versa.

A more encouraging example comes from Pischke (2007), who looks at the e§ect of school term length on student performance using variation generated by a sharp policy change in Germany. Until the 1960s, children in all German states except Bavaria started school in the Spring. Beginning in the 1966-67 school year, the Spring-starters moved to start school in the Fall. The transition to a Fall start required two short school years for a§ected cohorts, 24 weeks long instead of 37. Students in these cohorts e§ectively had their time in school compressed relative to cohorts on either side and relative to students in Bavaria, which

{188}------------------------------------------------

![](_page_188_Figure_2.jpeg)

<span id="page-188-0"></span>Figure 5.2.2: Employment in New Jersey and Pennsylvania fast-food restaurants, October 1991 to September 1997 (from Card and Krueger 2000). Vertical lines indicate dates of the original Card and Krueger (1994) survey and the October 1996 federal minimum-wage increase.

{189}------------------------------------------------

already had a Fall start.

Figure 5.2.3 plots the likelihood of grade repetition for the 1962-73 cohorts of 2nd graders in Bavaria and affected states (there are no repetition data for 1963-65). Repetition rates in Bavaria were reasonably flat from 1966 onwards at around 2.5%. Repetition rates are higher in the short-school-year states, at around 4 - 4.5% in 1962 and 1966, before the change in term length. But repetition rates jump up by about a percentage point for the two affected cohorts in these states, a bit more so for the second cohort than the first, before falling back to the baseline level. This graph provides strong visual evidence of treatment and control states with a common underlying trend, and a treatment effect that induces a sharp but transitory deviation from this trend. A shorter school year seems to have increased repetition rates for affected cohorts.

![](_page_189_Figure_4.jpeg)

<span id="page-189-0"></span>Figure 5.2.3: Average rates of grade repetition in second grade for treatment and control schools in Germany (from Pischke 2007). The data span a period before and after a change in term length for students outside of Bavaria.