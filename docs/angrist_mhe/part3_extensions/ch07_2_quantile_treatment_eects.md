# Quantile Treatment E§ects

> Pages: 229-242

The \$42,000 question regarding any set of regression estimates is whether they have a causal interpretation. This is no less true for quantile regression than Ordinary Least Squares. Suppose we are interested in estimating the e§ect of a training program on earnings. OLS regression estimates measure the impact of the

<span id="page-229-1"></span><sup>4</sup>For example, if <sup>y</sup> is the conditional median, then <sup>F</sup><sup>Y</sup> (yjXi) = :<sup>5</sup> and half of all conditional quantiles are below <sup>y</sup>. The relation [\(7.1.9\)](#page-228-0) can be proved formally using the change of variables formula.

{230}------------------------------------------------

program on average earnings while quantile regression estimates can be used to measure the impact of the program on median earnings. In both cases, we must worry about whether the estimated program e§ects are contaminated by omitted variables bias.

Here too, omitted variables problems can be solved using instrumental variables, though IV methods for quantile models are a relatively new development, and are not yet as áexible as conventional 2SLS. We discuss an approach that captures the causal e§ect of a binary variable on quantiles (i.e., a treatment e§ect) using a binary instrument. The Quantile Treatment E§ects (QTE) estimator, introduced in Abadie, Angrist, and Imbens (2002), relies on essentially the same assumptions as the LATE framework for average causal e§ects. The result is an Abadie-type weighting estimator of the causal e§ect of treatment on quantiles for compliers.[5](#page-230-0)

Our discussion of the QTE estimator is based on an additive model for conditional quantiles, so that a single treatment e§ect is estimated. The resulting estimator simpliÖes to Koenker and Bassett (1978) linear quantile regression when there is no instrumenting. The relationship between QTE and quantile regression is therefore analogous to that between conventional 2SLS and OLS when the regressor of interest is a dummy.

The parameters of interest are deÖned as follows. For 2 (0; 1), we assume there exist 2 R and  2 R r such that

$$Q_{\tau}(\mathbf{Y}_{i}|\mathbf{X}_{i},\mathbf{D}_{i},\mathbf{D}_{1i}>\mathbf{D}_{0i}) = \alpha_{\tau}\mathbf{D}_{i} + \mathbf{X}_{i}'\boldsymbol{\beta}_{\tau}, \tag{7.2.1}$$

where Q (y<sup>i</sup> jX<sup>i</sup> ;d<sup>i</sup> ;d1<sup>i</sup>>d0<sup>i</sup>) denotes the -quantile of y<sup>i</sup> given X<sup>i</sup> and d<sup>i</sup> for compliers. Thus, and  are quantile regression coe¢ cients for compliers.

Recall that d<sup>i</sup> is independent of potential outcomes conditional on X<sup>i</sup> and d1<sup>i</sup>>d0<sup>i</sup> , as we discussed in [\(4.5.2\)](#page-146-0). The parameter in this model therefore gives the di§erence in the conditional-on-X<sup>i</sup> quantiles of y1<sup>i</sup> and y0<sup>i</sup> for compliers. In other words,

<span id="page-230-2"></span>
$$Q_{\tau}(\mathbf{Y}_{1i}|\mathbf{X}_{i}, \mathbf{D}_{1i} > \mathbf{D}_{0i}) - Q_{\tau}(\mathbf{Y}_{0i}|\mathbf{X}_{i}, \mathbf{D}_{1i} > \mathbf{D}_{0i}) = \alpha_{\tau}$$
(7.2.2)

This tells us, for example, whether a training program changed the conditional median or lower decile of earnings for compliers. Note that the parameter does not tell us whether treatment changed the quantiles of the unconditional distributions of y1<sup>i</sup> and y0<sup>i</sup> . For that, we have to integrate families of quantile regression results using procedures like the one described in Section [7.1.3.](#page-228-1)

It also bears emphasizing that is not the conditional quantile of the individual treatment e§ects, (y1<sup>i</sup> y0<sup>i</sup>). You might want to know, for example, whether the median treatment e§ect is positive. Unfortunately, questions like this are very hard to answer without making the assumptions usually invoked for causal inference.[6](#page-230-1) Even a randomized trial with perfect compliance fails to reveal the distribution of

<span id="page-230-0"></span><sup>5</sup>For an alternative approach, see Chernozhukov and Hansen (2005), which allows for regressors of any type (i.e., not just dummies), but invokes a rank-invariance assumption that is unnecessary in the QTE framework.

<span id="page-230-1"></span><sup>6</sup> See, for example, Heckman, Smith, and Clements (1997).

{231}------------------------------------------------

(y1<sup>i</sup>y0<sup>i</sup>). This does not matter for average treatment e§ects since the mean of a di§erence is the di§erence in means. But all other features of the distribution of y1<sup>i</sup>y0<sup>i</sup> are hidden because we never get to see both y1<sup>i</sup> and y0<sup>i</sup> for any one person. The good news for applied econometricians is that the di§erence in marginal distributions, [\(7.2.2\)](#page-230-2), is usually more important than the distribution of treatment e§ects because comparisons of aggregate economic welfare typically require only the marginal distributions of y1<sup>i</sup> and y0<sup>i</sup> and not the distribution of their di§erence (see, e.g., Atkinson (1970), for the traditional view). This point can be made by example without reference to quantiles. When evaluating an employment program, we are inclined to view the program favorably if it increases overall employment rates. In other words, we are happy if the average y1<sup>i</sup> is higher than the average y0<sup>i</sup> . The number of individuals who gain jobs (y1<sup>i</sup>y0<sup>i</sup> = 1) or lose jobs (y1<sup>i</sup>y0<sup>i</sup> = 0) seems like it should be of secondary interest since a good program will necessarily have more gainers than losers.

#### 7.2.1 The QTE Estimator

The QTE estimator is motivated by the observation that, since the parameters of interest are quantile regression coe¢ cients for compliers, they can (theoretically) be estimated consistently by running quantile regressions in the population of compliers. As always, however, the compliers population is not identiÖable; we cannot list the compliers in a given data set. Nevertheless, as in Section [4.5.2,](#page-146-0) the relevant econometric minimand can be constructed using the Abadie Kappa theorem. SpeciÖcally,

<span id="page-231-0"></span>
$$(\alpha_{\tau}, \beta_{\tau}) = \arg\min_{a,b} E\{\rho_{\tau}(Y_i - aD_i - X_i'b)|D_{1i} > D_{0i}\} = \arg\min_{a,b} E\{\kappa_i \rho_{\tau}(Y_i - aD_i - X_i'b)\},$$
(7.2.3)

where

$$\kappa_i = 1 - \frac{D_i(1 - Z_i)}{1 - P(Z_i = 1 | X_i)} - \frac{(1 - D_i)Z_i}{P(Z_i = 1 | X_i)},$$

as before. The QTE estimator is the sample analog of [\(7.2.3\)](#page-231-0).

There are a number of practical issues that arise when implementing QTE. First, <sup>i</sup> must be estimated and the sampling variance induced by this Örst-step estimation should be reáected in the relevant asymptotic distribution theory. Abadie, Angrist, and Imbens (2002) derive the limiting distribution of the sample analog of [\(7.2.3\)](#page-231-0) when <sup>i</sup> is estimated nonparametrically. In practice, however, it is easier to bootstrap the whole procedure (i.e., beginning with the construction of estimated kappas) than to use the asymptotic formulas.

Second, <sup>i</sup> is negative when d<sup>i</sup> 6=z<sup>i</sup> : The kappa-weighted quantile regression minimand is therefore nonconvex and no longer has a linear programming representation. This problem can be solved by working with the following minimization problem instead:

<span id="page-231-1"></span>
$$\min_{a,b} E\{E[\kappa_i|Y_i,D_i,X_i]\rho_{\tau}(Y_i - aD_i - X_i'b)\}$$
(7.2.4)

{232}------------------------------------------------

This minimand is derived by iterating expectations in [\(7.2.3\)](#page-231-0). The practical di§erence between [\(7.2.3\)](#page-231-0) and [\(7.2.4\)](#page-231-1) is that the term

$$E[\kappa_i|\mathbf{Y}_i,\mathbf{D}_i,\mathbf{X}_i] = P[\mathbf{D}_{1i} > \mathbf{D}_{0i}|\mathbf{Y}_i,\mathbf{D}_i,\mathbf{X}_i]$$

is a probability and therefore between zero and one.[7](#page-232-0) A further simpliÖcation comes from the fact that

<span id="page-232-1"></span>
$$E[\kappa_i|Y_i, D_i, X_i] = 1 - \frac{D_i(1 - E[z_i|Y_i, D_i = 1, X_i))}{1 - P(z_i = 1|X_i)} - \frac{(1 - D_i)E[z_i|Y_i, D_i = 0, X_i)}{P(z_i = 1|X_i)}.$$
 (7.2.5)

Angrist (2001) uses this to implement QTE via a Probit Örst step to estimate E[z<sup>i</sup> jyi ;d<sup>i</sup> ;X<sup>i</sup> ] separately in the d<sup>i</sup> = 0 and d<sup>i</sup> = 1 subsamples, constructing E[<sup>i</sup> jyi ;d<sup>i</sup> ;X<sup>i</sup> ] using [\(7.2.5\)](#page-232-1), and then trimming any of the resulting estimates of E[<sup>i</sup> jyi ;d<sup>i</sup> ;X<sup>i</sup> ] that are outside the unit interval. The resulting Örst-step estimates of E[<sup>i</sup> jyi ;d<sup>i</sup> ;X<sup>i</sup> ] can simply be plugged in as weights when constructing quantile regression estimates in a second step using Stataís qreg command.[8](#page-232-2)

#### Estimates of the E§ect of Training on the Quantiles of Trainee Earnings

The Job Training Partnership Act was a large federal program that provided subsidized training to disadvantaged American workers in the 1980s. JTPA services were delivered at 649 sites, also called Service Delivery Areas (SDAs), located throughout the country. The original study of the labor-market impact of JTPA services was based on 15,981 people for whom continuous data on earnings (from either State unemployment insurance (UI) records or two follow-up surveys) were available for at least 30 months after random assignment.[9](#page-232-3) There are 6,102 adult women with 30-month earnings data and 5,102 adult men with 30-month earnings data.

In our notation, y<sup>i</sup> is 30-month earnings, d<sup>i</sup> indicates enrollment for JTPA services, and z<sup>i</sup> indicates the randomly assigned o§er of JTPA services. A key feature of most social experiments, as with many randomized trials of new drugs and therapies, is that some participants decline the intervention being o§ered. In the JTPA, those o§ered services were not compelled to participate in training. Consequently, although the o§er of subsidized training was randomly assigned, only about 60 percent of those o§ered training actually received JTPA services. Treatment received is therefore partly self-selected and likely to be correlated with potential outcomes. On the other hand, the randomized o§er of training provides a good instrument for training received since the two are obviously correlated and the o§er of treatment is independent of potential

<span id="page-232-0"></span>Intuitively, this is because <sup>i</sup> "Önds compliers". A formal statement of this result appears in Abadie, Angrist, and Imbens (2002; Lemma 3.2).

<span id="page-232-2"></span><sup>8</sup> Step-by-step, it goes like this:

<sup>1.</sup> Probit z<sup>i</sup> on y<sup>i</sup> and X<sup>i</sup> separately in the d<sup>i</sup> = 0 and d<sup>i</sup> = 1 subsamples. Save these Ötted values. 2. Probit z<sup>i</sup> on X<sup>i</sup> in the whole sample. Save these Ötted values. 3. Construct E[ijyi;di;Xi] by plugging the two sets of Ötted values into [\(7.2.5\)](#page-232-1). Set anything less than zero to zero and anything greater than one to one. 4. Use these kappas to weight quantile regressions.

<sup>5.</sup> Bootstrap this whole procedure to construct standard errors.

<span id="page-232-3"></span><sup>9</sup> See Bloom et al (1997).

{233}------------------------------------------------

outcomes. Moreover, because of the very low percentage of individuals receiving JTPA services in the control group (less than 2 percent), e§ects for compliers in this case can be interpreted as e§ects on those who were treated (there are few always-takers).

Since training o§ers were randomized in the National JTPA Study, covariates (Xi) are not required to consistently estimate e§ects on compliers. Even in experiments like this, however, itís customary to control for covariates to correct for chance associations between treatment status and applicant characteristics and to increase precision (see Chapter [2\)](#page-24-0). The covariates used here are baseline measures from the JTPA intake process. They include dummies for black and Hispanic applicants, a dummy for high-school graduates (including GED holders), dummies for married applicants, 5 age-group dummies, and a dummy for whether the applicant worked at least 12 weeks in the year preceding random assignment. Also included are dummies for the original recommended service strategy (classroom, on-the-job training (OJT), job search assistance (JSA), other) and a dummy for whether earnings data are from the second follow-up survey. Since these covariates mostly summarize coarse demographics, we can think of the quantile analysis as telling us how the JTPA experiment a§ected the earnings distribution within demographic groups.

As a benchmark, OLS and conventional instrumental variables (2SLS) estimates of the impact of training are reported in the Örst column of Table [7.2.1.](#page-221-0) The OLS training coe¢ cient is a precisely estimated \$3,754. This is the coe¢ cient on d<sup>i</sup> in a regression of y<sup>i</sup> on d<sup>i</sup> and X<sup>i</sup> . These estimates ignore the fact that trainees are self-selected. The 2SLS estimates in Table [7.2.1](#page-221-0) use the randomized o§er of treatment z<sup>i</sup> as an instrument for d<sup>i</sup> . The 2SLS estimate for men is \$1,593 with a standard error of \$895, less than half the size of the corresponding OLS estimate.

Quantile regression estimates show that the gap in quantiles by trainee status is much larger (in proportionate terms) below the median than above it. This can be seen in the right-hand columns of Table [7.2.1,](#page-221-0) which reports quantile regression estimates for the .15, .25, .5, .75, and .85 quantiles. SpeciÖcally, the .85 quantile of trainee earnings is about 13 percent higher than the corresponding quantile for non-trainees, while the .15 quantile is 136 percent higher. Like the OLS estimates in the table, these quantile regression coe¢ cients do not necessarily have a causal interpretation. Rather they provide a descriptive comparison of the earnings distributions of trainees and non-trainees.

QTE estimates of the e§ect of training on median earnings are similar in magnitude though less precise than the benchmark 2SLS estimates. On the other hand, the QTE estimates show a pattern very di§erent from the quantile regression estimates, with no evidence of an impact on the .15 or .25 quantile. The estimates at low quantiles are substantially smaller than the corresponding quantile regression estimates, and they are small in absolute terms. For example, the QTE estimate (standard error) of the e§ect on the .15 quantile is \$121 (475), while the corresponding quantile regression estimate is \$1,187 (205). Similarly, the QTE estimate (standard error) of the e§ect on the .25 quantile for men is \$702 (670), while the corresponding quantile regression estimate is \$2,510 (356). Unlike the results at low quantiles, however, the QTE estimates 

{234}------------------------------------------------

of e§ects on male earnings above the median are large and statistically signiÖcant (though still smaller than the corresponding quantile regression estimates).

The result that JTPA training for adult men did not raise the lower quantiles of their earnings is the most interesting Önding arising from this analysis. This suggests that the quantile regression estimates in the top half of Table [7.2.1](#page-221-0) are contaminated by positive selection bias. One response to this Önding might be that few JTPA applicants were very well o§, so that distributional e§ects within applicants are of less concern than the fact that the program helped many applicants overall. However, the upper quantiles of earnings were reasonably high for adults who participated in the National JTPA Study. Increasing earnings in this upper tail is therefore unlikely to have been a high priority.

{235}------------------------------------------------

Table 7.2.1: Quantile regression estimates and quantile treatment e§ects from the JTPA experiment

<table><tbody><tr><th></th><th></th><th></th><th></th><th>A. OLS and Quantile Regression Estimates</th><th></th><th></th></tr><tr><td></td><td>OLS</td><td></td><td></td><td></td><td>Quantile</td><td></td></tr><tr><td></td><td></td><td>0.15</td><td>0.25</td><td>0.50</td><td>0.75</td><td>0.85</td></tr><tr><td>Training</td><td>3,754</td><td>1,187</td><td>2,510</td><td>4,420</td><td>4,678</td><td>4,806</td></tr><tr><td></td><td>(536)</td><td>(205)</td><td>(356)</td><td>(651)</td><td>(937)</td><td>(1,055)</td></tr><tr><td>% Impact of Training</td><td>21.20</td><td>135.56</td><td>75.20</td><td>34.50</td><td>17.24</td><td>13.43</td></tr><tr><td>High school or GED</td><td>4,015</td><td>339</td><td>1,280</td><td>3,665</td><td>6,045</td><td>6,224</td></tr><tr><td></td><td>(571)</td><td>(186)</td><td>(305)</td><td>(618)</td><td>(1,029)</td><td>(1,170)</td></tr><tr><td>Black</td><td>-2,354</td><td>-134</td><td>-500</td><td>-2,084</td><td>-3,576</td><td>-3,609</td></tr><tr><td></td><td>(626)</td><td>(194)</td><td>(324)</td><td>(684)</td><td>(1087)</td><td>(1,331)</td></tr><tr><td>Hispanic</td><td>251</td><td>91</td><td>278</td><td>925</td><td>-877</td><td>-85</td></tr><tr><td></td><td>(883)</td><td>(315)</td><td>(512)</td><td>(1,066)</td><td>(1,769)</td><td>(2,047)</td></tr><tr><td>Married</td><td>6,546</td><td>587</td><td>1,964</td><td>7,113</td><td>10,073</td><td>11,062</td></tr><tr><td></td><td>(629)</td><td>(222)</td><td>(427)</td><td>(839)</td><td>(1,046)</td><td>(1,093)</td></tr><tr><td>Worked less than 13</td><td>-6,582</td><td>-1,090</td><td>-3,097</td><td>-7,610</td><td>-9,834</td><td>-9,951</td></tr><tr><td>weeks in past year</td><td>(566)</td><td>(190)</td><td>(339)</td><td>(665)</td><td>(1,000)</td><td>(1,099)</td></tr><tr><td>Constant</td><td>9,811</td><td>-216</td><td>365</td><td>6,110</td><td>14,874</td><td>21,527</td></tr><tr><td></td><td>(1,541)</td><td>(468)</td><td>(765)</td><td>(1,403)</td><td>(2,134)</td><td>(3,896)</td></tr></tbody></table>

B. 2SLS and QTE Estimates

<table><tbody><tr><th></th><th>2SLS</th><th></th><th></th><th></th><th>Quantile</th><th></th></tr><tr><td></td><td></td><td>0.15</td><td>0.25</td><td>0.50</td><td>0.75</td><td>0.85</td></tr><tr><td>Training</td><td>1,593</td><td>121</td><td>702</td><td>1,544</td><td>3,131</td><td>3,378</td></tr><tr><td></td><td>(895)</td><td>(475)</td><td>(670)</td><td>(1,073)</td><td>(1,376)</td><td>(1,811)</td></tr><tr><td>% Impact of Training</td><td>8.55</td><td>5.19</td><td>11.99</td><td>9.64</td><td>10.69</td><td>9.02</td></tr><tr><td>High school or GED</td><td>4,075</td><td>714</td><td>1,752</td><td>4,024</td><td>5,392</td><td>5,954</td></tr><tr><td></td><td>(573)</td><td>(429)</td><td>(644)</td><td>(940)</td><td>(1,441)</td><td>(1,783)</td></tr><tr><td>Black</td><td>-2,349</td><td>-171</td><td>-377</td><td>-2,656</td><td>-4,182</td><td>-3,523</td></tr><tr><td></td><td>(625)</td><td>(439)</td><td>(626)</td><td>(1,136)</td><td>(1,587)</td><td>(1,867)</td></tr><tr><td>Hispanic</td><td>335</td><td>328</td><td>1,476</td><td>1,499</td><td>379</td><td>1,023</td></tr><tr><td></td><td>(888)</td><td>(757)</td><td>(1,128)</td><td>(1,390)</td><td>(2,294)</td><td>(2,427)</td></tr><tr><td>Married</td><td>6,647</td><td>1,564</td><td>3,190</td><td>7,683</td><td>9,509</td><td>10,185</td></tr><tr><td></td><td>(627)</td><td>(596)</td><td>(865)</td><td>(1,202)</td><td>(1,430)</td><td>(1,525)</td></tr><tr><td>Worked less than 13</td><td>-6,575</td><td>-1,932</td><td>-4,195</td><td>-7,009</td><td>-9,289</td><td>-9,078</td></tr><tr><td>weeks in past year</td><td>(567)</td><td>(442)</td><td>(664)</td><td>(1,040)</td><td>(1,420)</td><td>(1,596)</td></tr><tr><td>Constant</td><td>10,641</td><td>-134</td><td>1,049</td><td>7,689</td><td>14,901</td><td>22,412</td></tr><tr><td></td><td>(1,569)</td><td>(1,116)</td><td>(1,655)</td><td>(2,361)</td><td>(3,292)</td><td>(7,655)</td></tr></tbody></table>

Notes: The table reports OLS, quantile regression, 2SLS, and QTE estimates of the e§ect of training on earnings (adapted from Abadie, Angrist, and Imbens (2002)). Assignment status is used as an instrument for training status in Panel B. All models include as covariates dummies for service strategy recommended and age group, and a dummy indicating data from a second follow-up survey. Robust standard errors are reported in parenthesis.

{236}------------------------------------------------

# Chapter 8

# Nonstandard Standard Error Issues

We have normality. I repeat, we have normality.

Anything you still canít cope with is therefore your own problem.

Douglas Adams, The Hitchhikerís Guide to the Galaxy (1979)

Today, software packages routinely compute asymptotic standard errors derived under weak assumptions about the sampling process or underlying model. For example, you get regression standard errors based on formula [\(3.1.7\)](#page-49-0) using the Stata option "robust". Robust standard errors improve on old-fashioned standard errors because the resulting inferences are asymptotically valid when the regression residuals are heteroskedastic, as they almost certainly are when regression approximates a nonlinear CEF. In contrast, old-fashioned standard errors are derived assuming homoskedasticity. The hang-up here is that robust standard errors can be misleading when the asymptotic approximation is not very good. The Örst part of this chapter looks at the failure of asymptotic inference with robust standard errors and some simple palliatives.

A pillar of traditional cross-section inference - and the discussion in Section [3.1.3](#page-45-0) - is the assumption that the data are independent. Each observation is treated as a random draw from the same population, uncorrelated with the observation before or after. We understand today that this sampling model is unrealistic and potentially even foolhardy. Much as in the time-series studies common in macroeconomics, cross-section analysts must worry about correlation between observations. The most important form of dependence arises in data with a group structure - for example, the test scores of children observed within classes or schools. Children in the same school or class tend to have test scores that are correlated since they are subject to some of the same environmental and family-background ináuences. We call this correlation the clustering problem, or the Moulton problem, after Moulton (1986), who made it famous. A closely-related problem is correlation over time in the data sets commonly used to implement di§erences-in-di§erences estimation strategies. For example, studies of state-level minimum wages must confront the fact that state average employment rates are correlated over time. We call this the serial correlation problem, closely 

{237}------------------------------------------------

related but distinct from the Moulton problem.

Researchers plagued by clustering and serial correlation also have to confront the fact that the simplest Öxups for these problems, like Stataís "cluster" option, may not be very good. The asymptotic approximation relevant for clustered or serially correlated data relies on a large number of clusters or time series observations. Alas, we are rarely blessed with many clusters or long time series. The resulting inference problems are not always insurmountable, though often the best solution is to get more data. Econometric Öx-ups for clustering and serial correlation are discussed in the second part of this chapter. Some of the material in this chapter is hard to work through without matrix algebra, so we take the plunge and switch to a mostly-matrix motif.

# 8.1 The Bias of Robust Standard Errors<sup>F</sup>

In matrix notation

$$\hat{\beta} = \left[\sum_{i} \mathbf{X}_{i} \mathbf{X}_{i}'\right]^{-1} \sum_{i} \mathbf{X}_{i} \mathbf{Y}_{i} = (X'X)^{-1} X' y,$$

where X is the Nk matrix with rows X<sup>0</sup> i and y is the N - 1 vector of yiís. We saw in Section [3.1.3](#page-45-0) that ^ has an asymptotically Normal distribution. We can write:

$$\sqrt{N}(\hat{\beta} - \beta) \sim N(0, \Omega)$$

where is the asymptotic covariance matrix. Repeating [\(3.1.7\)](#page-49-0), the formula for in this case is

$$\Omega_r = E[X_i X_i']^{-1} E[X_i X_i' e_i^2] E[X_i X_i']^{-1}, \tag{8.1.1}$$

where e<sup>i</sup> = yiX<sup>0</sup> <sup>i</sup>: When residuals are homoskedastic, simpliÖes to <sup>c</sup> = <sup>2</sup>E[XiX<sup>0</sup> i ] <sup>1</sup> where <sup>2</sup> = E[e 2 i ]:

We are concerned here with the bias of robust standard errors in independent samples (i.e., no clustering or serial correlation). To simplify the derivation of bias, we assume that the regressor vector can be treated as Öxed in repeated samples, as it would be if we sampled stratifying on X<sup>i</sup> : Non-stochastic-regressors gives a benchmark sampling model that is often used to look at Önite-sample distributions. It turns out that we miss little by making this assumption, while simplifying the derivations considerably.

With Öxed regressors, we have

$$\Omega_r = \left(\frac{X'X}{N}\right)^{-1} \left(\frac{X'\Psi X}{N}\right) \left(\frac{X'X}{N}\right)^{-1} \tag{8.1.2}$$

where

$$\Psi = E[ee'] = diag(\psi_i)$$

{238}------------------------------------------------

is the variance matrix of residuals. Under homosked asticity,  $\psi_i = \sigma^2$  for all i and we get

$$\Omega_c = \sigma^2 \left(\frac{X'X}{N}\right)^{-1}.$$

Asymptotic standard errors are given by the square root of the diagonal elements of  $\Omega_r$  and  $\Omega_c$ , after removing the asymptotic normalization by dividing by N.

In practice, the asymptotic covariance matrix must be estimated. The old-fashioned or conventional variance matrix estimator is

$$\hat{\Omega}_c = (X'X)^{-1}\hat{\sigma}^2 = (X'X)^{-1} \left(\sum \frac{\hat{e}_i^2}{N}\right),$$

where  $\hat{e}_i = Y_i - X_i'\hat{\beta}$  is the estimated regression residual, and

$$\hat{\sigma}^2 = \sum \frac{\hat{e}_i^2}{N}$$

estimates the residual variance. The corresponding robust variance matrix estimator is

$$\hat{\Omega}_r = (X'X)^{-1} \left( \sum \frac{X_i X_i' \hat{e}_i^2}{N} \right) (X'X)^{-1}.$$
(8.1.3)

We can think of the middle term as an estimator of the form  $\sum \frac{\mathbf{X}_i \mathbf{X}_i' \widehat{\psi}_i}{N}$ , where  $\widehat{\psi}_i = \widehat{e}_i^2$  estimates  $\psi_i$ .

By the law of large numbers and Slutsky theorems,  $N\hat{\Omega}_c$  converges in probability to  $\Omega_c$  while  $N\hat{\Omega}_r$  converges to  $\Omega_r$ . But in finite samples, both variance estimators are biased. The bias in  $\hat{\Omega}_c$  is well-known from classical least-squares theory and easy to correct. Less appreciated is the fact that if the residuals are homoskedastic, the robust estimator is more biased than the conventional, perhaps a lot more. From this we conclude that robust standard errors can be more misleading than conventional standard errors in situations where heteroskedasticity is modest. We also propose a rule-of-thumb that uses the maximum of old-fashioned and robust standard errors to avoid gross misjudgments of precision.

With non-stochastic regressors, we have

$$E[\hat{\Omega}_c] = (X'X)^{-1}\hat{\sigma}^2 = (X'X)^{-1} \left(\sum \frac{E(\hat{e}_i^2)}{N}\right).$$

To analyze  $E[\hat{e}_i^2]$ , start by expanding  $\hat{e} = y - X\hat{\beta}$ :

$$\hat{e} = y - X(X'X)^{-1}X'y = [I - X(X'X)^{-1}X'](X\beta + e) = Me$$

where e is the vector of population residuals,  $M = I_N - X(X'X)^{-1}X'$  is a non-stochastic residual-maker

{239}------------------------------------------------

matrix with  $i^{th}$  row  $m'_i$ , and  $I_N$  is the  $N \times N$  identity matrix. Then  $\hat{e}_i = m'_i e$ , and

<span id="page-239-2"></span>
$$E\left(\hat{e}_{i}^{2}\right) = E\left(m_{i}'ee'm_{i}\right)$$
$$= m_{i}'\Psi m_{i}$$

To simplify further, write  $m_i = \ell_i - h_i$  where  $\ell_i$  is the  $i^{th}$  column of  $I_N$  and  $h_i = X(X'X)^{-1}X_i$ , the  $i^{th}$  column of the projection matrix  $H = X(X'X)^{-1}X'$ . Then

$$E\left(\hat{e}_{i}^{2}\right) = \left(\ell_{i} - h_{i}\right)' \Psi\left(\ell_{i} - h_{i}\right)$$

$$= \psi_{i} - 2\psi_{i}h_{ii} + h'_{i}\Psi h_{i}$$
(8.1.4)

where  $h_{ii}$ , the  $i^{th}$  diagonal element of H, satisfies

$$h_{ii} = h'_i h_i = X'_i (X'X)^{-1} X_i. (8.1.5)$$

Parenthetically,  $h_{ii}$  is called the *leverage* of the  $i^{th}$  observation. Leverage tells us how much pull a particular value of  $X_i$  exerts on the regression line. Note that the  $i^{th}$  fitted value ( $i^{th}$  element of Hy) is

<span id="page-239-0"></span>
$$\hat{Y}_i = h'_i y = h_{ii} Y_i + \sum_{j \neq i} h_{ij} Y_j.$$
(8.1.6)

A large  $h_{ii}$  means that the  $i^{th}$  observation has a large impact on the  $i^{th}$  predicted value. In a bivariate regression with a single regressor,  $x_i$ ,

<span id="page-239-3"></span>
$$h_{ii} = \frac{1}{N} + \frac{(x_i - \overline{x})^2}{\sum (x_j - \overline{x})^2}.$$
 (8.1.7)

This shows that leverage increases when  $x_i$  is far the mean. In addition to (8.1.6), we know that  $h_{ii}$  is a number that lies in the interval [0,1] and that  $\sum_{j=1}^{N} h_{ij} = K$ , the number of regressors (see, e.g., Hoaglin and Welch, 1978).

Suppose residuals are homoskedastic, so that  $\psi_i = \sigma^2$ . Then (8.1.4) simplifies to

$$E\left(\hat{e}_{i}^{2}\right) = \sigma^{2}[1 - 2h_{ii} + h'_{i}h_{i}] = \sigma^{2}(1 - h_{ii}) < \sigma^{2}.$$

<span id="page-239-1"></span><sup>&</sup>lt;sup>1</sup>The property  $\sum_{j=1}^{N} h_{ij}$  =K comes from the fact that H is idempotent. You can also use (8.1.7) to verify that in a bivariate regression,  $\sum_{j=1}^{N} h_{ij} = 2$ .

{240}------------------------------------------------

So  $\hat{\Omega}_c$  tends to be too small. Using the properties of  $h_{ii}$ , we can go one step further:

$$\sum \frac{E(\hat{e}_i^2)}{N} = \sigma^2 \sum \frac{1-h_{ii}}{N} = \sigma^2 \left(\frac{N-\mathbf{K}}{N}\right).$$

Thus, the bias in  $\hat{\Omega}_c$  can be fixed by a simple degrees-of-freedom correction: divide by N-K instead of N in the formula for  $\hat{\sigma}^2$ , the default in most empirical variance computations.

We now want to show that under homoskedasticity the bias in  $\hat{\Omega}_r$  is likely to be worse than the bias in  $\hat{\Omega}_c$ . The bias in the robust covariance matrix estimator is

<span id="page-240-0"></span>
$$E[\hat{\Omega}_r] = N(X'X)^{-1} \left( \sum \frac{X_i X_i' E(\hat{e}_i^2)}{N} \right) (X'X)^{-1}, \tag{8.1.8}$$

where  $E\left(\hat{e}_i^2\right)$  is given by (8.1.4). Under homoskedasticity,  $\psi_i = \sigma^2$  and we have  $E\left(\hat{e}_i^2\right) = \sigma^2\left(1 - h_{ii}\right)$  as in  $\hat{\Omega}_c$ . It's clear, therefore, that the bias in  $\hat{e}_i^2$  tends to pull robust standard errors down. The general expression, (8.1.8), is hard to evaluate, however. Chesher and Jewitt (1987) show that as long as there is not "too much" heteroskedasticity, robust standard errors based on  $\hat{\Omega}_r$  are indeed biased downwards.<sup>2</sup>

How do we know that  $\hat{\Omega}_r$  is likely to be more biased than  $\hat{\Omega}_c$ ? Partly this comes from Monte Carlo evidence (e.g., MacKinnon and White, 1985, and our own small study, discussed below). We also prove this for a bivariate example, where the single regressor,  $\tilde{x}_i$ , is assumed to be in deviations-from-means form, so there is a single coefficient. In this case, the estimator of interest is  $\hat{\beta}_1 = \frac{\sum \tilde{x}_i Y_i}{\sum \tilde{x}_i^2}$  and the leverage is  $h_{ii} = \frac{\tilde{x}_i^2}{\sum \tilde{x}_i^2}$  (we lose the  $\frac{1}{N}$  term in (8.1.7) by partialling out the constant). Let  $s_x^2 = \frac{\sum \tilde{x}_i^2}{N}$ . For the conventional covariance estimator, we have

$$E[\hat{\Omega}_c] = \frac{\sigma^2}{Ns_x^2} \left[ \frac{\sum (1 - h_{ii})}{N} \right] = \frac{\sigma^2}{Ns_x^2} \left[ 1 - \frac{1}{N} \right],$$

so the bias here is small. A simple calculation using (8.1.8) shows that under heteroskedasticity, the robust estimator has expectation:

$$E[\hat{\Omega}_r] = \frac{\sigma^2}{N s_x^2} \sum \frac{(1 - h_{ii})}{N} \left( \frac{\hat{x}_i^2}{s_x^2} \right) = \frac{\sigma^2}{N s_x^2} \sum (1 - h_{ii}) h_{ii} = \frac{\sigma^2}{N s_x^2} \left[ 1 - \sum h_{ii}^2 \right].$$

The bias of  $\hat{\Omega}_r$  is therefore worse than the bias of  $\hat{\Omega}_c$  if  $\sum h_{ii}^2 > \frac{1}{N}$ , as it is by Jensen's inequality unless the regressor has constant leverage, in which case  $h_{ii} = \frac{1}{N}$  for all i.

We can reduce the bias in  $\hat{\Omega}_r$  by trying to get a better estimator of  $\psi_i$ , say  $\hat{\psi}_i$ . The estimator  $\hat{\Omega}_r$  sets  $\hat{\psi}_i = \hat{e}_i^2$ , the estimator proposed by White (1980a) and our starting point in this section. Here is a summary

$$E[h_{ii}] = \frac{\sum h_{ii}}{N} = \frac{1}{N}$$

<span id="page-240-1"></span><sup>&</sup>lt;sup>2</sup>In particular, as long as the ratio of the largest  $\psi_i$  to the smallest  $\psi_i$  is less than 2, robust standard errors are biased downwards.

<span id="page-240-2"></span> $<sup>^{3}</sup>$ Think of  $h_{ii}$  as a random variable with a uniform distribution in the sample. Then


{241}------------------------------------------------

of the proposals explored in MacKinnon and White (1985):

$$\begin{split} HC_0 &: & \widehat{\psi}_i = \widehat{e}_i^2 \\ HC_1 &: & \widehat{\psi}_i = \frac{N}{N-K} \widehat{e}_i^2 \\ HC_2 &: & \widehat{\psi}_i = \frac{1}{1-h_{ii}} \widehat{e}_i^2 \\ HC_3 &: & \widehat{\psi}_i = \frac{1}{(1-h_{ii})^2} \widehat{e}_i^2. \end{split}$$

 $HC_1$  is a simple degrees of freedom correction as is used for  $\hat{\Omega}_c$ .  $HC_2$  uses the leverage to give an unbiased estimate of the variance estimate of the  $i^{th}$  residual when the residuals are homoskedastic, while  $HC_3$  approximates a jackknife estimator.<sup>4</sup> In the applications we've seen, the estimated standard errors tend to get larger as we go down the list, but this is not a theorem.

#### Time out for the Bootstrap

Bootstrapping is a resampling scheme that offers an alternative to inference based on asymptotic formulas. A bootstrap sample is a sample drawn from our own data. In other words, if we have a sample of size N, we treat this sample as if it were the population and draw repeatedly from it (with replacement). The bootstrap standard error is the standard deviation of an estimator across many draws of this sort. Intuitively, we expect the sampling distribution constructed by sampling from our own data to provide a good approximation to the sampling distribution we are after.

There are many ways to bootstrap regression estimates. The simplest is to draw pairs of  $\{Y_i, X_i\}$ -values, sometimes called the "pairs bootstrap" or a "nonparametric bootstrap". Alternatively, we can keep the  $X_i$ -values fixed, draw from the distribution of residuals  $(\hat{e}_i)$ , and create a new estimate of the dependent variable based on the predicted value and the residual draw for the particular observation. This procedure, which is a type of "parametric bootstrap", mimics a sample drawn with non-stochastic regressors and ensures that  $X_i$  and the regression residuals are independent. On the other hand, we don't want independence if we're interested in standard errors under heteroskedasticity. An alternative residual bootstrap, called the "wild bootstrap", draws  $X_i'\hat{\beta} + \hat{e}_i$  (which, of course, is just the original  $Y_i$ ) with probability 0.5, and  $X_i'\hat{\beta} - \hat{e}_i$  otherwise (see, e.g., Mammen 1993 and Horowitz, 1997). This preserves the relationship between residual variances and  $X_i$  observed in the original sample.

and

$$E[h_{ii}^2] = \frac{\sum h_{ii}^2}{N} > (E[h_{ii}])^2 = \left(\frac{1}{N}\right)^2$$

by Jensen's inequality unless  $h_{ii}$  is constant. Therefore  $\sum h_{ii}^2 > \frac{1}{N}$ . The constant-leverage case occurs when  $\tilde{x}_i = +/-\kappa$ , for some constant,  $\kappa$ .

<span id="page-241-0"></span><sup>&</sup>lt;sup>4</sup>A jackknife variance estimator estimates sampling variance from the empirical distribution generated by omitting one observation at a time. Stata computes  $HC_1$ ,  $HC_2$ , and  $HC_3$ . You can also use a trick suggested by Messer and White (1984): divide  $Y_i$  and  $X_i$  by  $\sqrt{\widehat{\phi}_i}$  and instrument the transformed model by  $X_i/\sqrt{\widehat{\phi}_i}$  for your preferred choice of  $\widehat{\phi}_i$ .

{242}------------------------------------------------

Bootstrapping is useful for two reasons. First, in some cases the asymptotic distribution of an estimator can be hard to compute (e.g., the asymptotic distributions of quantile regression estimates involve unknown densities). Bootstrapping provides a computer-intensive but otherwise straightforward computational strategy. Not all asymptotic distributions are approximated by the bootstrap, but it seems to work well for the simple estimators we care about. Second, under some circumstances, the sampling distribution obtained via bootstrap may be closer to the Önite-sample distribution of interest than the asymptotic approximation - statisticians call this property asymptotic reÖnement.

Here, we are mostly interested in the bootstrap because of asymptotic reÖnement. The asymptotic distribution of regression estimates is easy enough to compute, but we worry that the estimators HC<sup>0</sup> - HC<sup>3</sup> are biased. As a rule, bootstrapping provides an asymptotic reÖnement when applied to test statistics that have asymptotic distributions which do not depend on any unknown parameters (see, e.g., Horowitz, 2001). Such test statistics are said to be asymptotically pivotal. An example is a t-statistic: this is asymptotically standard normal. Regression coe¢ cients are not asymptotically pivotal; they have an asymptotic distribution which depends on the unknown residual variance.

The upshot is that if you want better Önite-sample inference for regression coe¢ cients, you should bootstrap t-statistics. That is, you calculate the t-statistic in each bootstrap sample and compare the analogous t-statistic from your original sample to this bootstrap ìtî-distribution. A hypothesis is rejected if the absolute value of the original t-statistic is above, say, the 95th percentile of the absolute values from the bootstrap distribution.

Theoretical appeal notwithstanding, as applied researchers, we donít like the idea of bootstrapping pivotal statics very much. This is partly because weíre not only (or even primarily) interested in formal hypothesis testing: we like to see the standard errors in parentheses under our regression coe¢ cients. These provide a summary measure of precision that can be used to construct conÖdence intervals, compare estimators, and test any hypothesis that strikes us, now or later. We can certainly calculate standard errors from bootstrap samples but this promises no asymptotic reÖnement. In our view, therefore, practitioners worried about the Önite-sample behavior of robust standard errors should focus on bias corrections like HC1-HC3: We especially like the idea of taking the larger of the conventional standard error (with degrees of freedom correction) and one of these three.