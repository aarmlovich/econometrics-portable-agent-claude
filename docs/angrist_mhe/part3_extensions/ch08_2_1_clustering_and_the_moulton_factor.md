# Clustering and the Moulton Factor

> Pages: 246-251

Bias problems aside, heteroskedasticity rarely leads to dramatic changes in inference. In large samples where bias is not likely to be a problem, we might see standard errors increase by about 25 percent when moving from the conventional to the HC<sup>1</sup> estimator. In contrast, clustering can make all the di§erence.

The clustering problem can be illustrated using a simple bivariate regression estimated in data with a group structure. Suppose weíre interested in the bivariate regression,

<span id="page-246-2"></span>
$$Y_{ig} = \beta_0 + \beta_1 x_g + e_{ig}, (8.2.1)$$

where yig is the dependent variable for individual i in cluster or group g, with G groups. Importantly, the regressor of interest, xg, varies only at the group level. For example, data from the STAR experiment analyzed by Krueger (1999) come in the form of yig, the test score of student i in class g, and class size, xg.

Although students were randomly assigned to classes in the STAR experiment, the data are unlikely to be independent across observations. The test scores of students in the same class tend to be correlated because students in the same class share background characteristics and are exposed to the same teacher and classroom environment. Itís therefore prudent to assume that, for students i and j in the same class, g;

$$E[e_{ig}e_{jg}] = \rho\sigma_e^2 > 0, \tag{8.2.2}$$

where is the intra-class correlation coe¢ cient and 2 e is the residual variance.[9](#page-246-0)

Correlation within groups is often modeled using an additive random e§ects model. SpeciÖcally, we assume that the residual, eig, has a group structure:

<span id="page-246-1"></span>
$$e_{ig} = v_g + \eta_{ig}. \tag{8.2.3}$$

where v<sup>g</sup> is a random component speciÖc to class g and ig is a mean-zero student-level component thatís left over. We focus here on the correlation problem, so both of these error components are assumed to be homoskedastic.

When the regressor of interest varies only at the group level, an error structure like [\(8.2.3\)](#page-246-1) can increase standard errors sharply. This unfortunate fact is not news - Kloek (1981) and Moulton (1986) both made the point - but it seems fair to say that clustering didnít really become part of the applied econometrics

<span id="page-246-0"></span><sup>9</sup> This sort of residual correlation structure is also a consequence of stratiÖed sampling (see, e.g., Wooldridge, 2003). Most of the samples that we work with are close enough to random that we typically worry more about the dependence due to a group structure than clustering due to stratiÖcation.

{247}------------------------------------------------

zeitgeist until about 15 years ago.

Given the error structure, [\(8.2.3\)](#page-246-1), the intra-class correlation coe¢ cient becomes

$$\rho = \frac{\sigma_v^2}{\sigma_v^2 + \sigma_\eta^2}.$$

where 2 v is the variance of v<sup>g</sup> and 2 is the variance of ig. A word on terminology: is called the intra-class correlation coe¢ cient even when the groups of interest are not classrooms.

Let Vc(b 1 ) be the conventional OLS variance formula for the regression slope (generated using <sup>c</sup> in the previous section), while V (b 1 ) denotes the correct sampling variance given the error structure, [\(8.2.3\)](#page-246-1). With regressors Öxed at the group level and groups of equal size, n, we have

<span id="page-247-0"></span>
$$\frac{V(\widehat{\beta}_1)}{V_c(\widehat{\beta}_1)} = 1 + (n-1)\rho, \tag{8.2.4}$$

a formula derived in the appendix to this chapter. We call the square root of this ratio the Moulton factor, after Moultonís (1986) ináuential study. Equation [\(8.2.4\)](#page-247-0) tells us how much we over-estimate precision by ignoring intra-class correlation. Conventional standard errors become increasingly misleading as n and increase. Suppose, for example, that = 1. In this case, all the errors within a group are the same, so the yigís are the same as well. Making a data set larger by copying a smaller one n times generates no new information. The variance Vc(b 1 ) should therefore be scaled up by a factor of n. The Moulton factor increases with group size because with a Öxed overall sample size, larger groups means fewer clusters, in which case there is less independent information in the sample (because the data are independent across clusters but not within).[10](#page-247-1)

Even small intra-class correlation coe¢ cients can generate a big Moulton factor. In Angrist and Lavy (2007), for example, 4000 students are grouped in 40 schools, so the average n is 100. The regressor of interest is school-level treatment status - all students in treated schools were eligible to receive cash rewards for passing their matriculation exams. The intra-class correlation in this study áuctuates around .1. Applying formula [\(8.2.4\)](#page-247-0), the Moulton factor is over 3: the standard errors reported by default are only one-third of what they should be.

Equation [\(8.2.4\)](#page-247-0) covers an important special case where the regressors are Öxed within groups and group size is constant. The general formula allows the regressor, xig, to vary at the individual level and for di§erent group sizes, ng. In this case, the Moulton factor is the square root of

<span id="page-247-2"></span>
$$\frac{V(\widehat{\beta}_1)}{V_c(\widehat{\beta}_1)} = 1 + \left[\frac{V(n_g)}{\overline{n}} + \overline{n} - 1\right] \rho_x \rho, \tag{8.2.5}$$

<span id="page-247-1"></span><sup>1 0</sup>With non-stochastic regressors and homoscedastic residuals, the Moulton factor is a Önite-sample result. Survey statisticians call the Moulton factor the design e§ ect because it tells us how much to adjust standard errors in stratiÖed samples for deviations from simple random sampling (Kish, 1965).

{248}------------------------------------------------

where  $\overline{n}$  is the average group size, and  $\rho_x$  is the intra-class correlation of  $x_{iq}$ :

$$\rho_x = \frac{\sum_g \sum_{i \neq k} (x_{ig} - \overline{x}) (x_{kg} - \overline{x})}{V(x_{ig}) \sum_g n_g (n_g - 1)}.$$

Note that  $\rho_x$  does not impose a variance-components structure like (8.2.3) - here,  $\rho_x$  is a generic measure of the correlation of regressors within groups. The general Moulton formula tells us that clustering has a bigger impact on standard errors with variable group sizes and when  $\rho_x$  is large. The impact vanishes when  $\rho_x = 0$ . In other words, if the  $x_{ig}$ 's are uncorrelated within groups, the grouped error structure does not matter for the estimation of standard errors. That's why we worry most about clustering when the regressor of interest is fixed within groups.

We illustrate formula (8.2.1) using the Tennessee STAR example. A regression of Kindergartners' percentile score on class size yields an estimate of -0.62 with a robust ( $HC_1$ ) standard error of 0.09. In this case,  $\rho_x = 1$  because class size is fixed within classes while  $V(n_g)$  is positive because classes vary in size (in this case,  $V(n_g) = 17.1$ ). The intra-class correlation coefficient for residuals is .31 and the average class size is 19.4. Plugging these numbers into (8.2.1) gives a value of about 7 for  $\frac{V(\hat{\beta}_1)}{V_c(\hat{\beta}_1)}$ , so that conventional standard errors should be multiplied by a factor of  $2.65 = \sqrt{7}$ . The corrected standard error is therefore about 0.24.

The Moulton factor works similarly with 2SLS except that  $\rho_x$  should be computed for the instrumental variable and not the regressor. In particular, use (8.2.5) replacing  $\rho_x$  with  $\rho_z$ , where  $\rho_z$  is the intra-class correlation coefficient of the instrumental variable (Shore-Sheppard, 1996) and  $\rho$  is the intra-class correlation of the second-stage residuals. To understand why this works, recall that conventional standard errors for 2SLS are derived from the residual variance of the second-stage equation divided by the variance of the first-stage fitted values. This is the same asymptotic variance formula as for OLS, with first-stage fitted values playing the role of regressor.<sup>11</sup>

Here are some solutions to the Moulton problem:

- 1. Parametric: Fix conventional standard errors using (8.2.5). The intra-class correlations  $\rho$  and  $\rho_x$  are easy to compute and supplied as descriptive statistics in some software packages.<sup>12</sup>
- 2. Cluster standard errors: Liang and Zeger (1986) generalize the White (1980a) robust covariance matrix

<span id="page-248-0"></span><sup>11</sup> Clustering can also be a problem in regression-discontinuity designs if the variable that determines treatment assignment varies only at a group level (see Card and Lee, 2008, for details).

<span id="page-248-1"></span><sup>&</sup>lt;sup>12</sup>Use Stata's loneway command, for example.

{249}------------------------------------------------

to allow for clustering as well as heteroskedasticity:

<span id="page-249-1"></span>
$$\hat{V}_{c}(\hat{\beta}) = (X'X)^{-1} \left( \sum_{g} X_{g} \hat{\Psi}_{g} X_{g} \right) (X'X)^{-1}, \text{ where}$$

$$\hat{\Psi}_{g} = a \hat{e}_{g} \hat{e}'_{g} = a \begin{bmatrix}
\hat{e}_{1g}^{2} & \hat{e}_{1g} \hat{e}_{2g} & \cdots & \hat{e}_{1g} \hat{e}_{ngg} \\
\hat{e}_{1g} \hat{e}_{2g} & \hat{e}_{2g}^{2} & \vdots \\
\vdots & \ddots & \hat{e}_{(n_{g}-1)g} \hat{e}_{n_{g}g}
\end{bmatrix}.$$

$$\hat{e}_{1g} \hat{e}_{n_{g}g} & \cdots & \hat{e}_{(n_{g}-1)g} \hat{e}_{n_{g}g} & \hat{e}_{n_{g}g}^{2}$$

Here,  $X_g$  is the matrix of regressors for group g and a is a degrees of freedom adjustment factor similar to that which appears in  $HC_1$ . The clustered variance estimator  $\hat{V}_c(\hat{\beta})$  is consistent as the number of groups gets large under any within-group correlation structure and not just the parametric model in (8.2.3).  $\hat{V}_c(\hat{\beta})$  is not consistent with a fixed number of groups, however, even when the group size tends to infinity. To see why, note that the sums in  $\hat{V}_c(\hat{\beta})$  are over g and not i. Consistency is determined by the law of large numbers, which says that we can rely on sample moments to converge to population moments (Section 3.1.3). But here the sums are at the group level and not over individuals. Clustered standard errors are therefore unlikely to be reliable with few clusters, a point we return to below.

3. Use group averages instead of micro data: let  $\overline{Y}_g$  be the mean of  $Y_{ig}$  in group g. Estimate

$$\overline{Y}_q = \beta_0 + \beta_1 x_q + \overline{e}_q$$

by weighted least squares using the group size as weights. This is equivalent to OLS using micro data but the standard errors are asymptotically correct given the group structure, (8.2.3). Again, the asymptotics here are based on the number of groups and not the group size. Importantly, however, because the group means are close to Normally distributed with modest group sizes, we can expect the good finite-sample properties of regression with Normal errors to kick in. The standard errors that come out of grouped estimation are therefore likely to be more reliable than clustered standard errors in samples with few clusters.

Grouped-data estimation can be generalized to models with micro covariates using a two-step procedure. Suppose the equation of interest is

<span id="page-249-0"></span>
$$Y_{iq} = \beta_0 + \beta_1 x_q + W'_{iq} \delta + e_{iq}, \tag{8.2.7}$$

where  $W'_{ig}$  is a vector of covariates that varies within groups. In step 1, construct the covariate-adjusted group effects,  $\mu_g$ , by estimating

$$Y_{iq} = \mu_q + W'_{iq}\delta + \eta_{iq}$$

{250}------------------------------------------------

The <sup>g</sup> , called group e§ects, are coe¢ cients on a full set of group dummies. The estimated ^<sup>g</sup> are group means adjusted for the e§ect of the individual level variables w<sup>0</sup> ig. Note that by virtue of [\(8.2.7\)](#page-249-0) and [\(8.2.3\)](#page-246-1), <sup>g</sup> = <sup>0</sup> + <sup>1</sup>x<sup>g</sup> + g: In step 2, therefore, we regress the estimated group e§ects on group-level variables:

<span id="page-250-0"></span>
$$\hat{\mu}_g = \beta_0 + \beta_1 x_g + \{ \nu_g + (\hat{\mu}_g - \mu_g) \}.$$
 (8.2.8)

The e¢ cient GLS estimator for [\(8.2.8\)](#page-250-0) is weighted least squares, using the reciprocal of the estimated variance of the group-level residual, f<sup>g</sup> + ^<sup>g</sup> <sup>g</sup> g, as weights. This can be a problem since the variance of <sup>g</sup> is not estimated very well with few groups. We might therefore weight by the reciprocal of the variance of the estimated group e§ects, the group size, or use no weights at all.[13](#page-250-1) In an e§ort to better approximate the relevant Önite-sample distribution, Donald and Lang (2007) suggest that inferences in grouped procedures be based on a t-distribution with Gk degrees of freedom.

Note that the grouping approach does not work when xig varies within groups. Averaging xig to x<sup>g</sup> is a version of IV, as we saw in Section [4.](#page-98-0) So with micro-variation in the regressor of interest, grouping estimates parameters that di§er from the target parameters in a model like [\(8.2.7\)](#page-249-0).

- 4. Block bootstrap: In general, bootstrap inference uses the empirical distribution of the data by resampling. But simple random resampling wonít do in this case. The trick with clustered data is to preserve the dependence structure in the target population. We do this by block bootstrapping - that is, drawing blocks of data deÖned by the groups g. In the Tennessee STAR data, for example, weíd block bootstrap by re-sampling entire classes instead of individual students.
- 5. Estimate a parametric GLS or maximum likelihood model based on a version of [\(8.2.1\)](#page-246-2). This Öxes the clustering problem but also changes the estimand unless the CEF is linear, as detailed in section [3.4.1.](#page-81-0) We therefore prefer other approaches.

Table [8.2.1](#page-258-0) compare standard-error Öx-ups in the STAR example. The table reports six estimates of the standard errors: conventional robust standard errors (using HC1); two versions of parametrically corrected standard errors using the Moulton formula [\(8.2.5\)](#page-247-2), the Örst using the formula for the intra-class correlation given by Moulton and the second using Stataís estimator from the loneway command; clustered standard errors; block-bootstrapped standard errors; and standard errors from weighted estimation at the group level. The coe¢ cient estimate is -0.62. In this case, all adjustments deliver similar results, a standard error of about .23. This happy outcome is due in large part to the fact that with 318 classrooms, we have enough clusters for group-level asymptotics to work well. With few clusters, however, things are much dicier, a point we return to at the end of the chapter.

<span id="page-250-1"></span><sup>1 3</sup> See, e.g., Angrist and Lavy (2007) for an example of the latter two weighting schemes.

{251}------------------------------------------------