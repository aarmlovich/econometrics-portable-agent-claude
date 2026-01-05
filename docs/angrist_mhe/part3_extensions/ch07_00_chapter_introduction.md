# Chapter Introduction

> Pages: 218-225

# Quantile Regression

Hereís a prayer for you. Got a pencil? . . . ëProtect me from knowing what I donít need to know. Protect me from even knowing that there are things to know that I donít know. Protect me from knowing that I decided not to know about the things I decided not to know about. Amen.í Thereís another prayer that goes with it. ëLord, lord, lord. Protect me from the consequences of the above prayer.í

Douglas Adams, Mostly Harmless (1995)

Rightly or wrongly, 95 percent of applied econometrics is concerned with averages. If, for example, a training program raises average earnings enough to o§set the costs, we are happy. The focus on averages is partly because obtaining a good estimate of the average causal e§ect is hard enough. And if the dependent variable is a dummy for something like employment, the mean describes the entire distribution. But many variables, like earnings and test scores, have continuous distributions. These distributions can change in ways not revealed by an examination of averages, for example, they can spread out or become more compressed. Applied economists increasingly want to know whatís happening to an entire distribution, to the relative winners and losers, as well as to averages.

Policy-makers and labor economists have been especially concerned with changes in the wage distribution. We know, for example, that áat average real wages are only a small part of whatís been going on in the labor market for the past 25 years. Upper earnings quantiles have been increasing, while lower quantiles have been falling. In other words, the rich are getting richer and the poor are getting poorer. But thatís not all - recently, inequality has grown asymmetrically; for example, among college graduates, itís mostly the rich getting richer, with wages at the lower decile unchanging. The complete story of the changing wage distribution is fairly complicated and would seem to be hard to summarize.

Quantile regression is a powerful tool that makes the task of modeling distributions easy, even when the underlying story is complex and multi-dimensional. We can use this tool to see whether participation in a training program or membership in a labor union a§ects earnings inequality as well as average earnings. We 

{219}------------------------------------------------

can also check for interactions, like whether and how the relation between schooling and inequality has been changing over time. Quantile regression works very much like conventional regression: confounding factors can be held Öxed by including covariates; interaction terms work the same as with regular regression, too. And sometimes we can even use instrumental variables methods to estimate causal e§ects on quantiles when a selection-on-observables story seems implausible.

#### 7.1 The Quantile Regression Model

The starting point for quantile regression is the conditional quantile function (CQF). Suppose we are interested in the distribution of a continuously-distributed random variable, y<sup>i</sup> , with a well-behaved density (no gaps or spikes). Then the CQF at quantile given a vector of regressors, x<sup>i</sup> , can be deÖned as:

$$Q_{\tau}(\mathbf{Y}_i|\mathbf{X}_i) = F_Y^{-1}(\tau|\mathbf{X}_i)$$

where F<sup>Y</sup> (yjXi) is the distribution function for y<sup>i</sup> conditional on X<sup>i</sup> . When = :10, for example, Q (y<sup>i</sup> jXi) describes the lower decile of y<sup>i</sup> given X<sup>i</sup> , while = :5 gives us the conditional median.[1](#page-219-0) By looking at changes in the CQF of earnings as a function of education, we can tell whether the dispersion in earnings goes up or down with schooling. By looking at changes in the CQF of earnings as a function of education and time, we can tell whether the relationship between schooling and inequality is changing over time.

The CQF is the conditional-quantile version of the CEF. Recall that the CEF can be derived as the solution to a mean-squared error prediction problem,

$$E\left[\mathbf{Y}_{i} \middle| \mathbf{X}_{i}\right] = \underset{m(\mathbf{X}_{i})}{\operatorname{arg\,min}} E\left[\left(\mathbf{Y}_{i} - m\left(\mathbf{X}_{i}\right)\right)^{2}\right].$$

In the same spirit, the CQF solves the following minimization problem,

<span id="page-219-1"></span>
$$Q_{\tau}(\mathbf{Y}_i|\mathbf{X}_i) = \arg\min_{q(X)} E\left[\rho_{\tau}(\mathbf{Y}_i - q(\mathbf{X}_i))\right], \tag{7.1.1}$$

where (u) = ( 1(u 0))u is called the "check function" because it looks like a check-mark when you plot it. If = :5; this becomes least absolute deviations because :<sup>5</sup> (u) = <sup>1</sup> 2 (sign u)u = 1 2 juj. In this case, Q (y<sup>i</sup> jXi) is the conditional median since the conditional median minimizes absolute deviations. Otherwise,

$$Q_{\tau}(\mathbf{Y}_i|\mathbf{X}_i) = \inf \{ y : F_Y(y|\mathbf{X}_i) \ge \tau \}.$$

<span id="page-219-0"></span><sup>1</sup>More generally, we can deÖne the CQF for discrete random variables and random variables with less-than-well-behaved densities as

{220}------------------------------------------------

the check function weights positive and negative terms asymmetrically:

$$\rho_{\tau}(u) = 1(u > 0) \cdot \tau u + 1(u \le 0) \cdot (1 - \tau)u.$$

This asymmetric weighting generates a minimand that picks out conditional quantiles (a fact thatís not immediately obvious but can be proved with a little work; see Koenker, 2005).

As a practical tool, the CQF shares the disadvantages of the CEF with continuous or high-dimensional X<sup>i</sup> : it may be hard to estimate and summarize. Weíd therefore like to boil this function down to a small set of numbers, one for each element of X<sup>i</sup> . Quantile regression accomplishes this by substituting a linear model for q(Xi) in [\(7.1.1\)](#page-219-1), producing

<span id="page-220-0"></span>
$$\beta_{\tau} \equiv \arg\min_{b \in \mathbb{R}^d} E\left[\rho_{\tau}(\mathbf{Y}_i - \mathbf{X}_i'b)\right]. \tag{7.1.2}$$

The quantile regression estimator, ^ , is the sample analog of [\(7.1.2\)](#page-220-0). It turns out this is a linear programming problem that is fairly easy (for computers) to solve.

Just as OLS Öts a linear model to y<sup>i</sup> by minimizing expected squared error, quantile regression Öts a linear model to y<sup>i</sup> using the asymmetric loss function, (). If Q (y<sup>i</sup> jXi) is in fact linear, the quantile regression minimand will Önd it (just as if the CEF is linear, OLS will Önd it). The original quantile regression model, introduced by Koenker and Bassett (1978), was motivated by the assumption that the CQF is linear. As it turns out, however, the assumption of a linear CQF is unnecessary - quantile regression is useful whether or not we believe this.

Before turning to a more general theoretical discussion of quantile regression, we illustrate the use of this tool to study the wage distribution. The motivation for the use of quantile regression to look at the wage distribution comes from labor economistsíinterest in the question of how inequality varies conditional on covariates like education and experience (see, e.g., Buchinsky, 1994). The overall gap in earnings by schooling group (e.g., the college/high-school di§erential) grew considerably in the 1980s and 1990s. Less clear, however, is how the wage distribution has been changing within education and experience groups. Many labor economists believe that increases in so-called "within-group inequality" provide especially strong evidence of fundamental changes in the labor market, not easily accounted for by changes in institutional features like the percent of workers who belong to labor unions.


{221}------------------------------------------------

<span id="page-221-0"></span>

<table><tbody><tr><th></th><th></th><th>Desc.</th><th>Stats.</th><th></th><th>Quantile</th><th>Regression</th><th>Estimates</th><th></th><th>OLS</th><th>Estimates</th></tr><tr><th>Census</th><th>Obs.</th><th>Mean</th><th>SD</th><th>0.1</th><th>0.25</th><th>0.5</th><th>0.75</th><th>0.9</th><th>Coe§.</th><th>MSE<br/>Root</th></tr><tr><td></td><td></td><td></td><td></td><td>.074</td><td>.074</td><td>.068</td><td>.070</td><td>.079</td><td>.072</td><td></td></tr><tr><td>1980</td><td>65023</td><td>6.4</td><td>0.67</td><td>(.002)</td><td>(.001)</td><td>(.001)</td><td>(.001)</td><td>(.001)</td><td>(.001)</td><td>0.63</td></tr><tr><td></td><td></td><td></td><td></td><td>.112</td><td>.110</td><td>.106</td><td>.111</td><td>.137</td><td>.114</td><td></td></tr><tr><td>1990</td><td>86785</td><td>6.46</td><td>0.06</td><td>(.003)</td><td>(.001)</td><td>(.001)</td><td>(.001)</td><td>(.003)</td><td>(.001)</td><td>0.64</td></tr><tr><td></td><td></td><td></td><td></td><td>.092</td><td>.105</td><td>.111</td><td>.120</td><td>.157</td><td>.114</td><td></td></tr><tr><td>2000</td><td>97397</td><td>6.5</td><td>0.75</td><td>(.002)</td><td>(.001)</td><td>(.001)</td><td>(.001)</td><td>(.004)</td><td>(.001)</td><td>0.69</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Notes:</td><td>Adapted</td><td>from</td><td>Angrist,</td><td>Chernozhukov,</td><td>and</td><td>Fernandez-Val</td><td>(2006).</td><td>tables<br/>The</td><td>reports</td><td>re-<br/>quantile</td></tr><tr><td>gression</td><td>estimates</td><td>the<br/>of</td><td>to<br/>returns</td><td>schooling,</td><td>OLS<br/>with</td><td>estimates</td><td>shown</td><td>right<br/>the<br/>at</td><td>for</td><td>The<br/>comparison.</td></tr><tr><td>sample</td><td>includes</td><td>US-born</td><td>and<br/>white</td><td>men<br/>black</td><td>aged</td><td>Standard<br/>40-49.</td><td>errors</td><td>reported<br/>are</td><td>in</td><td>All<br/>parentheses.</td></tr><tr><td>models</td><td>for<br/>control</td><td>and<br/>race</td><td>potential</td><td>experience.</td><td>Sampling</td><td>weights</td><td>were</td><td>the<br/>for<br/>used</td><td>Census<br/>2000</td><td>estimates.</td></tr></tbody></table>

{222}------------------------------------------------

Table 7.1.1 reports schooling coefficients from quantile regressions estimated using the 1980, 1990, and 2000 Censuses. The models used to construct these estimates control for race and a quadratic function of potential labor market experience (defined to be age - education - 6). The .5 quantile coefficients - for the conditional median - are very much like the OLS coefficients at the far right-hand side of the table. For example, the OLS estimate of .072 in the 1980 census is not very different from the .5 quantile coefficient of about .068 in the same data. If the conditional-on-covariates distribution of log wages is symmetric, so that the conditional median equals the conditional mean, we should expect these two coefficients to be the same. Also noteworthy is that fact that the quantile coefficients are similar across quantiles in 1980. An additional year of schooling raises median wages by 6.8 percent, with slightly higher effects on the lower and upper quartiles of .074 and .070. Although the estimated returns to schooling increased sharply between 1980 and 1990 (up to .106 at the median, with an OLS return of .114 percent), there is a reasonably stable pattern of returns across quantiles in the 1990 Census. The largest effect is on the upper decile, a coefficient of .137, while the other quantile coefficients are around .11.

We should expect to see constant coefficients across quantiles if the effect of schooling on wages amounts to what is sometimes called a "location shift.". Here, that means that as higher schooling levels raise average earnings, other parts of the wage distribution move in tandem (i.e., within-group inequality does not change). Suppose, for example, that log wages can be described by a classical linear regression model:

<span id="page-222-0"></span>
$$Y_i \sim N(X_i'\beta, \sigma_\varepsilon^2),$$
 (7.1.3)

where  $E[Y_i|X_i] = X_i'\beta$  and  $Y_i - X_i'\beta \equiv \varepsilon_i$  is a Normally distributed error with constant variance  $\sigma_{\varepsilon}^2$ . Homoskedasticity means the conditional distribution of log wages is no more spread out for college graduates than for high school graduates. The implications of the linear homoskedastic model for quantiles are apparent from the fact that

$$P[Y_i - X_i'\beta < \sigma_{\varepsilon}\Phi^{-1}(\tau)|X_i] = \tau,$$

where  $\Phi^{-1}(\tau)$  is the inverse of the standard Normal CDF. From this we conclude that  $Q_{\tau}(\mathbf{Y}_i|\mathbf{X}_i) = \mathbf{X}_i'\beta + \Phi^{-1}(\tau)$ . In other words, apart from the changing intercept, all quantile regression coefficients are the same. The results in Table 7.1.1 for 1980 and 1990 are not too far from this stylized representation.

In contrast with the simple pattern in 1980 and 1990 Census data, quantile regression estimates from the 2000 Census differ markedly across quantiles, especially in the right tail. An additional year of schooling raises the lower decile of wages by 9.2 percent and the median by 11.1 percent. In contrast, an additional year of schooling raises the upper decile by 15.7 percent. Thus, in addition to increases in overall inequality in the 1980s and 1990s (a fact we know from simple descriptive statistics), by 2000, inequality began to increase with education as well. This development is the subject of considerable discussion among labor economists, who are particularly concerned with whether it points to fundamental or institutional changes

{223}------------------------------------------------

in the labor market (see, e.g., Autor, Katz, and Kearney (2005) and Lemieux (2008)).

Again, a parametric example helps us see where an increasing pattern of quantile regression coefficients might come from. We can generate increasing quantile regression coefficients by adding heteroskedasticity to the classical Normal regression model, (7.1.3). Suppose that

$$\mathbf{Y}_i \sim N(\mathbf{X}_i'\beta, \sigma^2(\mathbf{X}_i)),$$

where  $\sigma^2(X_i) = (\lambda' X_i)^2$  and  $\lambda$  is a vector of positive coefficients such that  $\lambda' X_i > 0$  (perhaps proportional to  $\beta$ , so that the conditional variance grows with the conditional mean).<sup>2</sup> Then

$$P[Y_i - X_i'\beta < (\lambda'X_i)\Phi^{-1}(\tau)|X_i] = \tau,$$

with the implication that

$$Q_{\tau}(Y_i|X_i) = X_i'\beta + (\lambda'X_i)\Phi^{-1}(\tau) = X_i'[\beta + \lambda\Phi^{-1}(\tau)]. \tag{7.1.4}$$

so that quantile regression coefficients increase across quantiles.

Putting the pieces together, Table 7.1.1 neatly summarizes two stories, both related to variation in within-group inequality. First, results from the 2000 Census show inequality increasing sharply with education. The increase is asymmetric, however, and appears much more clearly in the upper tail of the wage distribution. Second, this increase is a new development. In 1980 and 1990, in contrast, schooling affected the wage distribution in a manner roughly consistent with a simple location shift.<sup>3</sup>

#### 7.1.1 Censored Quantile Regression

Quantile regression allows us to look at features of the conditional distribution of  $Y_i$  when part of the distribution is hidden. Suppose you have have data of the form

$$Y_{i,obs} = Y_i \cdot 1[Y_i < c], \tag{7.1.5}$$

$$\tau(1-\tau)\{E[f_{u_{\tau}}(0|X_i)X_iX_i']^{-1}E[X_iX_i']E[f_{u_{\tau}}(0|X_i)X_iX_i']^{-1},$$

where  $f_{u_{\tau}}(0|\mathbf{X}_i)$  is the conditional density of the quantile-regression residual at zero. If the residuals are homoskedastic this simplifies to  $\frac{\tau(1-\tau)}{f_{u_{\tau}}^2(0)}E[\mathbf{X}_i\mathbf{X}_i']^{-1}$ . The second set are robust to misspecification, computed using formulas in Angrist, Chernozhukov, and Fernandez-Val (2006). In this example, the impact of nonlinearity on standard errors is minor.

<span id="page-223-0"></span><sup>&</sup>lt;sup>2</sup>See Card and Lemieux (1996) for an empirical example of a regression model with this sort of heteroskedasticity. Koenker and Portnoy (1996) call this a linear location-scale model.

<span id="page-223-1"></span><sup>&</sup>lt;sup>3</sup>The results in table 7.1.1 include two sets of standard errors. The first are conventional standard errors, of the sort reported by Stata's qreg command (also specifying "robust"). These presume the CQF is truly linear. The formula for these is

{224}------------------------------------------------

where  $Y_{i,obs}$  is what you get to see and  $Y_i$  is the variable you would like to see. The variable  $Y_{i,obs}$  is censored - information about  $Y_i$  in  $Y_{i,obs}$  is limited for confidentiality reasons or because it was too difficult or time-consuming to collect more information. In the CPS, for example, high earnings are topcoded to protect respondent confidentiality. This means data above the topcode are recoded to have the topcode value. Duration data may also be censored: in a study of the effects of unemployment insurance on the duration of employment, we might follow new UI claimants for up to 40 weeks. Anyone out of work for longer has an unemployment spell length that is censored at 40. Note that limited dependent variables like hours worked or medical expenditure, discussed in Section 3.4.2, are <u>not</u> censored; they commonly take on the value zero by their nature, just as dummy variables like employment status do.

When dealing with censored dependent variables, quantile regression can be used to estimate the effect of covariates on conditional quantiles that are below the censoring point (assuming censoring is from above). This reflects the fact that recoding earnings above the upper decile to be equal to the upper decile has no effect on the median. So if CPS topcoding affects relatively few people (as is often true), censoring has no effect on estimates of the conditional median or even  $\beta_{\tau}$  for  $\tau = .75$ . Likewise, if less than 10 percent of the sample is censored conditional on all values of  $X_i$ , then when estimating  $\beta_{\tau}$  for  $\tau$  up to .9 you can simply ignore it. Alternately, you can limit the sample to values of  $X_i$  where  $Q_{\tau}(Y_i|X_i)$  is below c (or above, if censoring is from the bottom with  $Y_{i,obs} = Y_i \cdot 1[Y_i > c]$ ).

Powell (1986) formalizes this idea with the censored quantile regression estimator. Because we may not know which conditional quantiles are below the censoring point (continuing to think of top codes), Powell proposes we work with

$$Q_{\tau}(\mathbf{Y}_i|\mathbf{X}_i) = \min(c, \mathbf{X}_i'\beta_{\tau}^c).$$

The parameter vector  $\beta_{\tau}^{c}$  solves

<span id="page-224-0"></span>
$$\beta_{\tau}^{c} \equiv \arg\min_{b \in \mathbb{R}^{d}} E\{1\left[X_{i}'\beta_{\tau}^{c} < c\right] \cdot \rho_{\tau}(Y_{i} - X_{i}'b)\right]\}. \tag{7.1.6}$$

In other words, we solve the quantile regression minimization problem for values of  $X_i$  such that  $X_i'\beta_\tau^c < c$ . That is, we minimize the sample analog of (7.1.6). As long is there is enough uncensored data, the resulting estimates give us the quantile regression function we would have gotten had the data not been censored (assuming the conditional quantile function is, in fact, linear). And if it turns out that the conditional quantiles you are estimating are below the censoring point, then you are back to regular quantile regression.

The sample analog of (7.1.6) is no longer a linear programming problem but Buchinsky (1994) proposes a simple iterated linear programming algorithm that appears to work well. The iterations go like this: First you estimate  $\beta_{\tau}^{c}$  ignoring the censoring. Then find the cells with  $X'_{i}\beta_{\tau}^{c} < c$ . Then estimate the quantile regression again using these cells only, and so on. This algorithm is not guaranteed to converge but it appears to do so in practice. Standard errors can be bootstrapped. Buchinsky (1994) and Chamberlain

{225}------------------------------------------------

(1994) use this approach to estimate the returns to schooling for highly-experienced workers that may have earnings above the CPS topcode. The censoring adjustment tends to increase the returns to schooling for this group.