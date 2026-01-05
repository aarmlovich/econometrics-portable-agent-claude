# *B - Means by years of schooling*

> Pages: 47-51

#### **. regress average\_earnings school [aweight=count], robust** (sum of wgt is 4.0944e+05)

<table><tbody><tr><th></th><th></th><th></th><th></th><th></th><th></th></tr><tr><td>Source |</td><td>SS</td><td>df</td><td>MS</td><td>Number of obs =</td><td>21</td></tr><tr><td>+</td><td></td><td></td><td></td><td>F( 1,</td><td>19) = 540.31</td></tr><tr><td></td><td>Model | 1.16077332</td><td></td><td>1 1.16077332</td><td>Prob &gt; F</td><td>= 0.0000</td></tr><tr><td></td><td>Residual | .040818796</td><td></td><td>19 .002148358</td><td>R-squared</td><td>= 0.9660</td></tr><tr><td>+</td><td></td><td></td><td></td><td>Adj R-squared = 0.9642</td><td></td></tr><tr><td></td><td>Total | 1.20159212</td><td></td><td>20 .060079606</td><td>Root MSE</td><td>= .04635</td></tr><tr><td></td><td></td><td></td><td></td><td>+</td><td></td></tr><tr><td>average |</td><td></td><td>Robust</td><td colspan="3">Old Fashioned</td></tr><tr><td>_earnings |</td><td>Coef.</td><td>Std. Err.</td><td>t</td><td>Std. Err.</td><td>t</td></tr><tr><td>school |</td><td>.0674387</td><td>.0040352</td><td>16.71</td><td>+<br/>.0029013</td><td>23.24</td></tr><tr><td>const. |</td><td>5.835761</td><td>.0399452</td><td>146.09</td><td>.0381792</td><td>152.85</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

<span id="page-47-0"></span>Figure 3.1.3: Micro-data and grouped-data estimates of returns to schooling. Source: 1980 Census - IPUMS, 5 percent sample. Sample is limited to white men, age 40-49. Derived from Stata regression output. Oldfashioned standard errors are the default reported. Robust standard errors are heteroscedasticity-consistent. Panel A uses individual-level data. Panel B uses earnings averaged by years of schooling.

{48}------------------------------------------------

The asymptotic sampling distribution of ^ depends solely on the deÖnition of the estimand (i.e., the nature of the thing weíre trying to estimate, ) and the assumption that the data constitute a random sample. Before deriving this distribution, it helps to record the general asymptotic distribution theory that covers our needs. This basic theory can be stated mostly in words. For the purposes of these statements, we assume the reader is familiar with the core terms and concepts of statistical theory (e.g., moments, mathematical expectation, probability limits, and asymptotic distributions). For deÖnitions of these terms and a formal mathematical statement of the theoretical propositions given below, see, e.g., Knight (2000).

THE LAW OF LARGE NUMBERS Sample moments converge in probability to the corresponding population moments. In other words, the probability that the sample mean is close to the population mean can be made as high as you like by taking a large enough sample.

THE CENTRAL LIMIT THEOREM Sample moments are asymptotically Normally distributed (after subtracting the corresponding population moment and multiplying by the square root of the sample size). The covariance matrix is given by the variance of the underlying random variable. In other words, in large enough samples, appropriately normalized sample moments are approximately Normally distributed.

#### SLUTSKYíS THEOREM

- (a) Consider the sum of two random variables, one of which converges in distribution and the other converges in probability to a constant: the asymptotic distribution of this sum is una§ected by replacing the one that converges to a constant by this constant. Formally, let a<sup>N</sup> be a statistic with a limiting distribution and let b<sup>N</sup> be a statistic with probability limit b. Then a<sup>N</sup> +b<sup>N</sup> and a<sup>N</sup> +b have the same limiting distribution.
- (b) Consider the product of two random variables, one of which converges in distribution and the other converges in probability to a constant: the asymptotic distribution of this product is una§ected by replacing the one that converges to a constant by this constant. This allows us to replaces some sample moments by population moments (i.e., by their probability limits) when deriving distributions. Formally, let a<sup>N</sup> be a statistic with a limiting distribution and let b<sup>N</sup> be a statistic with probability limit b. Then a<sup>N</sup> b<sup>N</sup> and a<sup>N</sup> b have the same asymptotic distribution.
- THE CONTINUOUS MAPPING THEOREM Probability limits pass through continuous functions. For example, the probability limit of any continuous function of a sample moment is the function evaluated at the corresponding population moment. Formally, the probability limit of h(b<sup>N</sup> ) is h(b) where plim b<sup>N</sup> = b and h() is continuous at b.

X is the matrix whose rows are given by X0 i and y is the vector with elements yi, for i = 1; :::; N. The sample moment 1 N PXiX<sup>0</sup> i is X0X=N and the sample moment <sup>1</sup> N PXiy<sup>i</sup> is X0y=N. Then we can write ^ = (X0X) <sup>1</sup> X0y, a familiar matrix formula.

{49}------------------------------------------------

THE DELTA METHOD Consider a vector-valued random variable that is asymptotically Normally distributed. Most scalar functions of this random variable are also asymptotically Normally distributed, with covariance matrix given by a quadratic form with the covariance matrix of the random variable on the inside and the gradient of the function evaluated at the probability limit of the random variable on the outside. Formally, the asymptotic distribution of h(b<sup>N</sup> ) is Normal with covariance matrix rh(b) 0 rh(b) where plim b<sup>N</sup> = b, h() is continuously di§erentiable at b with gradient rh(b), and b<sup>N</sup> has asymptotic covariance matrix . [5](#page-49-0)

We can use these results to derive the asymptotic distribution of ^ in two ways. A conceptually straightforward but somewhat inelegant approach is to use the delta method: ^ is a function of sample moments, and is therefore asymptotically Normally distributed. It remains only to Önd the covariance matrix of the asymptotic distribution from the gradient of this function. (Note that consistency of ^ comes immediately from the continuous mapping theorem). An easier and more instructive derivation uses the Slutsky and central limit theorems. Note Örst that we can write

<span id="page-49-2"></span>
$$Y_i = X_i'\beta + [Y_i - X_i'\beta] \equiv X_i'\beta + e_i, \qquad (3.1.6)$$

where the residual e<sup>i</sup> is deÖned as the di§erence between the dependent variable and the population regression function, as before. This is as good a place as any to point out that these residuals are uncorrelated with the regressors by deÖnition of . In other words, E[Xie<sup>i</sup> ] = 0 is a consequence of  = E[XiX<sup>0</sup> i ] <sup>1</sup>E[Xiy<sup>i</sup> ] and e<sup>i</sup> = yiX<sup>0</sup> <sup>i</sup>, and not an assumption about an underlying economic relation. We return to this important point in the discussion of causal regression models in Section [3.2.](#page-53-0)[6](#page-49-1)

Substituting the identity [3.1.6](#page-49-2) for y<sup>i</sup> in the formula for ^, we have

$$\hat{\beta} = \beta + \left[\sum X_i X_i'\right]^{-1} \sum X_i e_i.$$

The asymptotic distribution of ^ is the asymptotic distribution of <sup>p</sup> <sup>N</sup>(^) = <sup>N</sup> -PXiX 0 i <sup>1</sup> p 1 N PXie<sup>i</sup> . By the Slutsky theorem, this has the same asymptotic distribution as E[XiX<sup>0</sup> i 1 p 1 N PXie<sup>i</sup> . Since E[Xie<sup>i</sup> ] = 0, <sup>p</sup> N PXie<sup>i</sup> is a root-N-normalized and centered sample moment. By the central limit theorem, this is asymptotically Normally distributed with mean zero and covariance matrix E[XiX<sup>0</sup> i e 2 i ], since this fourth moment is the covariance matrix of Xie<sup>i</sup> . Therefore, ^ has an asymptotic Normal distribution, with probability limit , and covariance matrix

$$E[X_i X_i']^{-1} E[X_i X_i' e_i^2] E[X_i X_i']^{-1}.$$
(3.1.7)

The standard errors used to construct t-statistics are the square roots of the diagonal elements of this

<span id="page-49-0"></span><sup>5</sup>For a derivation of the the delta method formula using the Slutsky and continuous mapping theorems, see, e.g., Knight, 2000, pp. 120-121.

<span id="page-49-1"></span><sup>6</sup>Residuals deÖned in this way are not necessarily mean-independent of Xi; for mean-independence, we need a linear CEF.

{50}------------------------------------------------

matrix. In practice these standard errors are estimated by substituting sums for expectations, and using the estimated residuals,  $\hat{e}_i = Y_i - X_i' \hat{\beta}$  to form the empirical fourth moment,  $\sum [X_i X_i \hat{e}_i^2]/N$ .

Asymptotic standard errors computed in this way are known as heteroskedasticity-consistent standard errors, White (1980a) standard errors, or Eicker-White standard errors in recognition of Eicker's (1967) derivation. They are also known as "robust" standard errors (e.g., in Stata). These standard errors are said to be robust because, in large enough samples, they provide accurate hypothesis tests and confidence intervals given minimal assumptions about the data and model. In particular, our derivation of the limiting distribution makes no assumptions other than those needed to ensure that basic statistical results like the central limit theorem go through. These are not, however, the standard errors that you get by default from packaged software. Default standard errors are derived under a homoskedasticity assumption, specifically, that  $E[e_i^2|X_i] = \sigma^2$ , a constant. Given this assumption, we have

$$E[X_i X_i' e_i^2] = E(X_i X_i' E[e_i^2 | X_i]) = \sigma^2 E[X_i X_i'],$$

by iterating expectations. The asymptotic covariance matrix of  $\hat{\beta}$  then simplifies to

<span id="page-50-0"></span>
$$E[X_{i}X_{i}']^{-1}E[X_{i}X_{i}'e_{i}^{2}]E[X_{i}X_{i}']^{-1} = E[X_{i}X_{i}']^{-1}\sigma^{2}E[X_{i}X_{i}']E[X_{i}X_{i}]^{-1}$$

$$= E[X_{i}X_{i}']^{-1}\sigma^{2}.$$
(3.1.8)

The diagonal elements of (3.1.8) are what SAS or Stata report unless you request otherwise.

Our view of regression as an approximation to the CEF makes heteroskedasticity seem natural. If the CEF is nonlinear and you use a linear model to approximate it, then the quality of fit between the regression line and the CEF will vary with  $X_i$ . Hence, the residuals will be larger, on average, at values of  $X_i$  where the fit is poorer. Even if you are prepared to assumed that the conditional variance of  $Y_i$  given  $X_i$  is constant, the fact that the CEF is nonlinear means that  $E[(Y_i - X_i'\beta)^2 | X_i]$  will vary with  $X_i$ . To see this, note that, as a rule,

<span id="page-50-2"></span>
$$E[(\mathbf{Y}_{i} - \mathbf{X}'_{i}\beta)^{2}|\mathbf{X}_{i}] = E\{[(\mathbf{Y}_{i} - E[\mathbf{Y}_{i}|\mathbf{X}_{i}]) + (E[\mathbf{Y}_{i}|\mathbf{X}_{i}] - \mathbf{X}'_{i}\beta)]^{2}|\mathbf{X}_{i}\}$$

$$= V[\mathbf{Y}_{i}|\mathbf{X}_{i}] + (E[\mathbf{Y}_{i}|\mathbf{X}_{i}] - \mathbf{X}'_{i}\beta)^{2}.$$
(3.1.9)

Therefore, even if  $V[Y_i|X_i]$  is constant, the residual variance increases with the square of the gap between the regression line and the CEF, a fact noted in White (1980b).

In the same spirit, it's also worth noting that while a linear CEF makes homoskedasticity possible, this is

<span id="page-50-1"></span><sup>&</sup>lt;sup>7</sup>The cross-product term resulting from an expansion of the quadratic in the middle of 3.1.9 is zero because  $Y_i - E[Y_i|X_i]$  is mean-independent of  $X_i$ .

{51}------------------------------------------------

not a su¢ cient condition for homoskedasticity. Our favorite example in this context is the linear probability model (LPM). A linear probability model is any regression where the dependent variable is zero-one, i.e., a dummy variable such as an indicator for labor force participation. Suppose the regression model is saturated, so the CEF is linear. Because the CEF is linear, the residual variance is also the conditional variance, V [y<sup>i</sup> jX<sup>i</sup> ]: But the dependent variable is a Bernoulli trial and the variance of a Bernoulli trial is P[y<sup>i</sup> jX<sup>i</sup> ](1 P[y<sup>i</sup> jX<sup>i</sup> ]). We conclude that LPM residuals are necessarily heteroskedastic unless the only regressor is a constant.

These points of principle notwithstanding, as an empirical matter, heteroskedasticity may matter little. In the micro-data schooling regression depicted in Figure [3.1.3,](#page-47-0) the robust standard error is .0003447, while the old-fashioned standard error is .0003043, only slightly smaller. The standard errors from the groupeddata regression, which are necessarily heteroskedastic if group sizes di§er, change somewhat more; compare the .004 robust standard to the .0029 conventional standard error. Based on our experience, these di§erences are typical. If heteroskedasticity matters too much, say, more than a 30% increase or any marked decrease in standard errors, you should worry about possible programming errors or other problems (for example, robust standard errors below conventional may be a sign of Önite-sample bias in the robust calculation; see Chapter [8,](#page-236-0) below.)