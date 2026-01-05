# An Example

> Pages: 242-246

For further insight into the di§erences between robust covariance estimators, we analyze a simple but important example that has featured in the earlier chapters in this book. Suppose you are interested in an estimate of <sup>1</sup> in the model

<span id="page-242-0"></span>
$$Y_i = \beta_0 + \beta_1 D_i + \varepsilon_i, \tag{8.1.9}$$

{243}------------------------------------------------

where  $D_i$  is a dummy variable. The OLS estimate of  $\beta_1$  is the difference in the means between those with  $D_i$  switched on and off. Denoting these subsamples by the subscripts 1 and 0, we have

$$\widehat{\beta}_1 = \overline{Y}_1 - \overline{Y}_0.$$

For the purposes of this derivation we think of  $D_i$  as non-random, so that  $\sum D_i = N_1$  and  $\sum (1-D_i) = N_0$  are fixed. Let  $r = N_1/N$ .

We know something about the finite-sample behavior of  $\widehat{\beta}_1$  from statistical theory. If  $Y_i$  is Normal with equal but unknown variance in both the  $D_i = 1$  and  $D_i = 0$  populations, then the conventional t-statistic for  $\widehat{\beta}_1$  has a t-distribution. This is the classic two sample t-test. Heteroskedasticity in this context means that the variances in the  $D_i = 1$  and  $D_i = 0$  populations are different. In this case, the testing problem in small samples becomes surprisingly intractable: the exact small sample distribution for even this simple problem is unknown.<sup>5</sup> The robust covariance estimators  $HC_0 - HC_3$  give asymptotic approximations to the unknown finite-sample distribution for the case of unequal variances.

The differences between  $HC_0$  -  $HC_3$  are differences in how the sample variances in the two groups defined by  $D_i$  are processed. Define  $S_j^2 = \sum_{D_i = j} (Y_i - \overline{Y}_j)^2$  for j = 0, 1. The leverage in this example is

$$h_{ii} = egin{array}{ll} 1/N_0 & ext{if } \mathrm{D}_i = 0 \ 1/N_1 & ext{if } \mathrm{D}_i = 1 \end{array}.$$

Using this, it's straightforward to show that the five variance estimators we've been discussing are

$$\begin{split} Conventional &: \frac{N}{N_0N_1} \left( \frac{S_0^2 + S_1^2}{N-2} \right) = \frac{1}{Nr(1-r)} \left( \frac{S_0^2 + S_1^2}{N-2} \right) \\ HC_0 \text{ (White, 1980)} &: \frac{S_0^2}{N_0^2} + \frac{S_1^2}{N_1^2} \\ HC_1 &: \frac{N}{N-2} \left( \frac{S_0^2}{N_0^2} + \frac{S_1^2}{N_1^2} \right) \\ HC_2 &: \frac{S_0^2}{N_0 \left( N_0 - 1 \right)} + \frac{S_1^2}{N_1 \left( N_1 - 1 \right)} \\ HC_3 &: \frac{S_0^2}{\left( N_0 - 1 \right)^2} + \frac{S_1^2}{\left( N_1 - 1 \right)^2}. \end{split}$$

The conventional estimator pools subsamples: this is efficient when the two variances are the same. The White (1980a) estimator,  $HC_0$ , adds separate estimates of the sampling variances of the means, using the consistent (but biased) variance estimators,  $\frac{S_j^2}{N_j}$ . The  $HC_2$  estimator uses unbiased estimators of the sample sample variance for each group, since it makes the correct degrees of freedom correction.  $HC_1$  makes a degrees of freedom correction outside the sum, which will help but is generally not quite correct. Since we know  $HC_2$  to be the unbiased estimate of the sampling variance under homoskedasticity,  $HC_3$  must be too

<span id="page-243-0"></span><sup>&</sup>lt;sup>5</sup>This is known as the Behrens-Fisher problem (see e.g. DeGroot and Schervish, 2001, ch. 8).

{244}------------------------------------------------

big. Note that with r = 0:5, a case where the regression design is said to be balanced, the conventional estimator equals HC<sup>1</sup> and all Öve estimators di§er little.

A small Monte Carlo study based on [\(8.1.9\)](#page-242-0) illustrates the pluses and minuses of the estimators and the extent to which a simple rule of thumb goes a long way towards ameliorating the bias of the HC class. We choose N = 30 to highlight small sample issues, and r = 0:9, which implies hii = 10=N = 1=3 if d<sup>i</sup> = 1. This is a highly unbalanced design. We draw

$$\varepsilon_i \sim \left\{ \begin{array}{ll} N(0,\sigma^2) & \text{if } \mathbf{D}_i = 0 \\ \\ N(0,1) & \text{if } \mathbf{D}_i = 1 \end{array} \right.$$

and report results for three cases. The Örst has lots of heteroskedasticity with = 0:5, while the second has relatively little heteroskedasticity, with = 0:85. No heteroskedasticity is the benchmark case.

Table [8.1.1](#page-258-0) displays the results. Columns (1) and (2) report means and standard deviations of the various standard error estimators across 25,000 replications of the sampling experiment. The standard deviation of c1 is the sampling variance we are trying to measure. With lots of heteroskedasticity, as in the upper panel of the table, Conventional standard errors are badly biased and, on average, only about half the size of the Monte Carlo sampling variance that constitutes our target. On the other hand, while the robust standard errors perform better, except for HC3, they are still too small.[6](#page-244-0)

The standard errors are themselves estimates and have considerable sampling variability. Especially noteworthy is the fact that the robust standard errors have much higher sampling variability than the OLS standard errors, as can be seen in column 2.[7](#page-244-1) The sampling variability further increases when we attempt to reduce bias by dividing the residuals by 1 hii or (1 hii) 2 . The worst case is HC3; with a standard deviation about 50% above that of the White (1980a) standard error, HC0.

The last two columns in the table show empirical rejection rates in a nominal 5% test for the hypothesis b <sup>1</sup> =  , where  is the population parameter (equal to zero, in this case). The test statistics are compared with a Normal distribution and to a t-distribution with N 2 degrees of freedom. Rejection rates are far too high for all tests, even HC3. Using a t-distribution rather than a Normal distribution helps only marginally.

The results with little heteroskedasticity, reported in the second panel, show that conventional standard errors are still too low; this bias is now in the order of 15%. HC<sup>0</sup> and HC<sup>1</sup> are also too small, about like before in absolute terms, though they now look worse relative to the conventional standard errors. The HC<sup>2</sup> and HC<sup>3</sup> standard errors are still larger than the conventional standard errors, on average, but

<span id="page-244-0"></span><sup>6</sup>Notice that HC<sup>2</sup> is an unbiased estimator of the sampling variance, while the mean of the HC<sup>2</sup> standard errors across sampling experiments (0.52) is still below the standard deviation of b (0.59). This comes from the fact that the standard error is the square root of the sampling variance, the sampling variance is itself estimated and hence has sampling variability, and the square root is a concave function.

<span id="page-244-1"></span><sup>7</sup> The large sampling variance of robust standard error estimators is noted by Chesher and Austin (1991). Kauermann and Carroll (2001) propose an adjustment to conÖdence intervals to correct for this.

{245}------------------------------------------------

empirical rejection rates are higher for these two than for conventional standard errors. This means the robust standard errors are sometimes too small ìby accident," an event that happens often enough to ináate rejection rates so that they exceed the conventional rejection rates.

The lesson we can take a away from this is that robust standard errors are no panacea. They can be smaller than conventional standard errors for two reasons: the small sample bias we have discussed and the higher sampling variance of these standard errors. We therefore take empirical results where the robust standard errors fall below the conventional standard errors as a red áag. This is very likely due to bias or a chance occurrence that is better discounted. In this spirit, we like the idea of taking the maximum of the conventional standard error and a robust standard error as your best measure of precision. This rule of thumb helps on two counts: it truncates low values of the robust estimators, reducing bias, and it reduces variability. Table [8.1.1](#page-258-0) shows the empirical rejection rates obtained using M ax(HC<sup>j</sup> ; Conventional): The empirical rejection rates using this rule of thumb look pretty good in the Örst two panels and greatly improve on the robust estimators alone.[8](#page-245-0)

Since there is no gain without pain, there must be some cost to using M ax(HC<sup>j</sup> ; Conventional). The cost is that the best standard error when there is no heteroskedasticity is the conventional OLS estimate. This is documented in the bottom panel of the table. Using the maximum ináates standard errors unnecessarily under homoskedasticity, depressing rejection rates. Nevertheless, the table shows that even in this case rejection rates donít go down all that much. We also view an underestimate of precision as being less costly than an over-estimate. Underestimating precision, we come away thinking the data are not very informative and that we should try to collect more data, while in the latter case, we may mistakenly draw important substantive conclusions.

A Önal comment on this Monte Carlo investigation concerns the sample size. Labor economists like us are used to working with tens of thousands of observations or more. But sometimes we donít. In a study of the e§ects of busing on public school students, Angrist and Lang (2004) work with samples of about 3000 students grouped in 56 schools. The regressor of interest in this study varies within grade only at the school level, so some of the analysis in this paper uses 56 school means. Not surprisingly, therefore, Angrist and Lang (2004) obtained HC<sup>1</sup> standard errors below conventional OLS standard errors when working with school-level data. As a rule, even if you start with the micro data on individuals, when the regressor of interest varies at a higher level of aggregation - a school, state, or some other group or cluster - e§ective sample sizes are much closer to the number of clusters than to the number of individuals. Inference procedures for clustered data are discussed in detail in the next section.

<span id="page-245-0"></span><sup>8</sup>Yang, Hsu, and Zhao (2005) formalize the notion of test procedures based on the maximum of a a set of test statistics with di§ering e¢ ciency and robustness properties.

{246}------------------------------------------------

# 8.2 Clustering and Serial Correlation in Panels