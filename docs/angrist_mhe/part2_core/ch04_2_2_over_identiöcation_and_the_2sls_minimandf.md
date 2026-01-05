# Over-identiÖcation and the 2SLS MinimandF

> Pages: 120-126

Constant-e§ects models with more instruments than endogenous regressors are said to be over-identiÖed. Because there are more instruments than needed to identify the parameters of interest, these models impose a set of restrictions that can be evaluated as part of a process of speciÖcation testing. This process amounts to asking whether the line plotted in a VIV-type picture Öts the relevant conditional means tightly enough given the precision with which the means are estimated. The details behind this useful idea are easiest to spell out using matrix notation and a traditional linear model.

Let Z<sup>i</sup> X 0 <sup>i</sup> z1<sup>i</sup> ::: zq<sup>i</sup> 0 denote the vector formed by concatenating the exogenous covariates and q instrumental variables and let W<sup>i</sup> X 0 i si 0 denote the vector formed by concatenating the covariates and the single endogenous variable of interest. In the quarter-of-birth paper, for example, the covariates are year-of-birth and state-of-birth dummies, the instruments are quarter-of-birth dummies, and the endogenous variable is schooling. The coe¢ cient vector is still [ 0 ; ] 0 , as in the previous subsection. The residuals for the causal model can be deÖned as a function of using

$$\eta_i(\Gamma) \equiv Y_i - \Gamma' W_i = Y_i - [\alpha' X_i + \rho S_i].$$

This residual is assumed to be uncorrelated with the instrument vector, z<sup>i</sup> . In other words, <sup>i</sup> satisÖes the orthogonality condition,

<span id="page-120-1"></span>
$$E[\mathbf{z}_i \eta_i(\Gamma)] = 0. \tag{4.2.2}$$

In any sample, however, this equation will not hold exactly because there are more moment conditions than there are elements of : [12](#page-120-0) The sample analog of [\(4.2.2\)](#page-120-1) is the sum over i,

$$\frac{1}{N} \sum Z_i \eta_i(\Gamma) \equiv m_N(\Gamma). \tag{4.2.3}$$

2SLS can be understood as a generalized method of moments (GMM) estimator that chooses a value for by making the sample analog of [\(4.2.2\)](#page-120-1) as close to zero as possible.

By the central limit theorem, the sample moment vector <sup>p</sup> Nm<sup>N</sup> () has an asymptotic covariance matrix equal to E[ZiZ 0 i i ()<sup>2</sup> ], a matrix weíll call . Although somewhat intimidating at Örst blush, this is just a matrix of 4th moments, as in the sandwich formula used to construct robust standard errors, [\(3.1.7\)](#page-49-0). As shown by Hansen (1982), the optimal GMM estimator based on [\(4.2.2\)](#page-120-1) minimizes a quadratic form in the sample moment vector, m<sup>N</sup> (^g), where g^ is a candidate estimator of . [13](#page-120-2) The optimal weighting matrix in

<span id="page-120-0"></span><sup>1 2</sup>With a single endogenous variable and more than one instrument, is [k+1] - 1, while Z<sup>i</sup> is [k+q] - 1 for q> 1. Hence the resulting linear system cannot be solved unless there is a linear dependency that makes some of the instruments redundant.

<span id="page-120-2"></span><sup>1 3</sup> "Quadratic form" is matrix language for a weighted sum of squares. Suppose <sup>v</sup> is an <sup>N</sup> - 1 vector and M is an N -N


{121}------------------------------------------------

the middle of the GMM quadratic form is 1 . In practice, of course, , is unknown and must be estimated. A feasible version of the GMM procedure uses a consistent estimator of in the weighting matrix. Since the estimator using known and estimated have the same limiting distribution, weíll ignore this distinction for now. The quadratic form to be minimized can therefore be written,

<span id="page-121-0"></span>
$$J_N(\hat{g}) \equiv N m_N(\hat{g})' \Lambda^{-1} m_N(\hat{g}), \tag{4.2.4}$$

where the <sup>N</sup>-term out front comes from <sup>p</sup> N normalization of the sample moments. As shown immediately below, when the residuals are conditionally homoskedastic, the minimizer of J<sup>N</sup> (^g) is the 2SLS estimator. Without homoskedasticity, the GMM estimator that minimizes [\(4.2.4\)](#page-121-0) is Whiteís (1982) Two-Stage IV (a generalization of 2SLS) so that it makes sense to call J<sup>N</sup> (^g) the ì2SLS minimandî.

Here are some of the details behind the GMM interpretation of 2SLS[14](#page-121-1) . Conditional homoskedasticity means that

$$E[Z_i Z_i' \eta_i(\Gamma)^2] = E[Z_i Z_i'] \sigma_{\eta}^2.$$

Substituting for <sup>1</sup> and using Z;y and W to denote sample data vectors and matrices, the quadratic form to be minimized becomes

$$J_N(\hat{g}) = (N\sigma_{\eta}^2)^{-1} \times (Y - W\hat{g})' ZE[Z_i Z_i']^{-1} Z'(Y - W\hat{g}). \tag{4.2.5}$$

Finally, substituting the sample cross-product matrix <sup>h</sup> Z 0Z N i for E[ZiZ 0 i ], we have

$$\hat{J}_N(\hat{g}) = (1/\sigma_{\eta}^2) \times (\mathbf{Y} - W\hat{g})' P_Z(\mathbf{Y} - W\hat{g}),$$

where P<sup>Z</sup> = Z(Z <sup>0</sup>Z) <sup>1</sup>Z. From here, we get the solution

$$\hat{g} = \hat{\Gamma}_{2SLS} = [W'P_ZW]^{-1}W'P_ZY.$$

Since the projection operator, PZ, produces Ötted values, and P<sup>Z</sup> is an idempotent matrix, this can be seen to be the OLS estimator of the second-stage equation, [\(4.1.9\)](#page-105-0), written in matrix notation. More generally, even without homoskedasticity we can obtain a feasible e¢ cient 2SLS-type estimator by minimizing [\(4.2.4\)](#page-121-0) and using a consistent estimator of E[ZiZ 0 i i (^g) 2 ] to form J^<sup>N</sup> (^g). Typically, weíd use the empirical fourth moments, PZiZ 0 i ^ 2 i , where ^<sup>i</sup> is the regular 2SLS residual computed without worrying about heteroskedasticity (see, White, 1982, for distribution theory and other details).

<span id="page-121-1"></span>matrix. A quadratic form in v is v <sup>0</sup>M v. If M is a N - N diagonal matrix with diagonal elements mi, then v 0M v = P i miv 2 i 1 4Much more detailed explanations can be found in Newey (1985), Newey and West (1987), and the original Hansen (1982) GMM paper.

{122}------------------------------------------------

The over-identiÖcation test statistic is given by the minimized 2SLS minimand. Intuitively, this statistic tells us whether the sample moment vector, m<sup>N</sup> (^g), is close enough to zero for the assumption that E[Zi<sup>i</sup> ] = 0 to be plausible. In particular, under the null hypothesis that the residuals and instruments are indeed orthogonal, the minimized J<sup>N</sup> (^g) has a 2 (q 1) distribution. We can therefore compare the empirical value of the 2SLS minimand with chi-square tables in a formal testing procedure for H<sup>0</sup> : E[Zi<sup>i</sup> ] = 0.

For reasons that will soon become apparent, weíre not often interested in over-identiÖcation per se. Our main interest is in the 2SLS minimand when the instruments are a full set of mutually exclusive dummy variables, as for the Wald estimators and grouped-data estimation strategies discussed above. In this important special case, the 2SLS becomes weighted least squares of a grouped equation like [\(4.1.16\)](#page-116-0), while the 2SLS minimand is the relevant weighted sum of squares being minimized. To see this, note that projection on a full set of mutually exclusive dummy variables for an instrument that takes on j values produces an N - 1 vector of Ötted values equal to the j conditional means at each value of the instrument (included covariates are counted as instruments), each one of these n<sup>j</sup> times, where n<sup>j</sup> is the group size and Pn<sup>j</sup> = N. The cross product matrix [Z <sup>0</sup>Z] in this case is a jj diagonal matrix with elements n<sup>j</sup> . Simplifying, we then have

$$\hat{J}_N(\hat{g}) = (1/\sigma_\eta^2) \times \sum_j n_j (\bar{y}_j - \hat{g}' \bar{W}_j)^2, \tag{4.2.6}$$

where W <sup>j</sup> is the sample mean of the rows of matrix W in group j. Thus, J^<sup>N</sup> (^g) is the GLS weighted least squares minimand for estimation of the grouped regression: y<sup>j</sup> on W <sup>j</sup> . With a little bit more work (here we skip the details), we can similarly show that the e¢ cient Two-Step IV procedure without homoskedasticity minimizes

<span id="page-122-0"></span>
$$\hat{J}_N(\hat{g}) = \sum_j \left(\frac{n_j}{\sigma_j^2}\right) (\bar{y}_j - \hat{g}'\bar{W}_j)^2, \tag{4.2.7}$$

where 2 j is the variance of <sup>i</sup> in group j. Estimation using [\(4.2.7\)](#page-122-0) is feasible because we can estimate 2 j in a Örst-step, say, using ine¢ cient-but-still-consistent 2SLS that ignores heteroskedasticity. E¢ cient two-step IV estimators are constructed in Angrist (1990, 1991).

The GLS structure of the 2SLS minimand allows us to see the over-identiÖcation test statistic for dummy instruments as a simple measure of the goodness of Öt of the line connecting y<sup>j</sup> and W <sup>j</sup> . In other words, this is the chi-square goodness of Öt statistic for the line in a VIV plot like Ögure [4.1.2.](#page-118-0) The chi-square degrees of freedom parameter is given by the di§erence between the number of values taken on by the instrument and the number of parameters being estimated[15](#page-122-1) .

Like the various paths leading to the 2SLS estimator, there are many roads to the test-statistic, [\(4.2.7\)](#page-122-0), as well. Here are two further paths that are worth knowing. First, the test-statistic based on the general GMM minimand for IV, whether the instruments are group dummies or not, is the same as the over-

<span id="page-122-1"></span><sup>1 5</sup> If, for example, the instrument takes on three values, one of which is assigned to the constant, and the model includes a constant and a single the endogenous variable only, the test statistic has 1 degree of freedom.

{123}------------------------------------------------

identiÖcation test statistic discussed in many widely-used econometric references on simultaneous equations models. For example, this statistic features in Hausmanís (1983) chapter on simultaneous equations in the Handbook of Econometrics, which also proposes a simple computational procedure: for homoskedastic models, the minimized 2SLS minimand is the sample size times the R<sup>2</sup> from a regression of the 2SLS residuals on the instruments (and the included exogenous covariates). The formula for this is N h ^ <sup>0</sup>P<sup>Z</sup> ^ ^ 0^ i , where ^ <sup>=</sup>yW^ <sup>2</sup>SLS is the vector of 2SLS residuals.

Second, itís worth emphasizing that the essence of over-identiÖcation can be said to be ìmore than one way to skin the same econometric cat.îIn other words, given more than one instrument for the same causal relation, we might consider constructing simple IV estimators one at a time and comparing them. This comparison checks over-identiÖcation directly: If each just-identiÖed estimator is consistent, the distance between them should be small relative to sampling variance, and should shrink as the sample size and hence the precision of these estimates increases. In fact, we might consider formally testing whether all possible just-identiÖed estimators are the same. The resulting test statistic is said to generate a Wald[16](#page-123-0) test of this null, while the test-statistic based on the 2SLS minimand is said to be a Lagrange Multiplier (LM) test because it can be related to the score vector in a maximum likelihood version of the IV setup.

In the grouped-data version of IV, the Wald test amounts to a test of equality for the set of all possible linearly independent Wald estimators. If, for example, lottery numbers are divided into 4 groups based on various cohorts eligibility cuto§s (RSN 1-95, 96-125, 126-195, and the rest), then 3 linearly independent Wald estimators can be constructed. Alternatively, the e¢ cient grouped-data estimator can be constructed by running GLS on these four conditional means. Four groups means there are 3 possible Wald estimators and 2 non-redundant equality restrictions on these three; hence, the relevant Wald statistic has 2 degrees of freedom. On the other hand, 4 groups means three instruments and a constant available to estimate a model with 2 parameters (the constant and the causal e§ect of military service). So the 2SLS minimand generates an over-identiÖcation test statistic with 4 2 = 2 degrees of freedom. And, in fact, provided you use the same method of estimating the weighting matrix in the relevant quadratic forms, these two test statistics not only test the same thing, they are numerically equivalent. This makes sense since we have already seen that 2SLS is the e¢ cient linear combination of Wald estimators.[17](#page-123-1)

Finally, a caveat regarding over-identiÖcation tests in practice: In our experience, the ìover-ID statisticî is often of little value in applied work. Because J<sup>N</sup> (^g) measures variance-normalized goodness of-Öt, the over-ID test-statistic tends to be low when the underlying estimates are imprecise. Since IV estimates are very often imprecise, we cannot take much satisfaction from the fact that one estimate is within sampling variance of another even if the individual estimates appear precise enough to be informative. On the other

<span id="page-123-0"></span><sup>1 6</sup> The Wald estimator and Wald test are named after the same statistician, Abraham Wald, but the latter reference is Wald (1943).

<span id="page-123-1"></span><sup>1 7</sup> The fact that Wald and LM testing procedures for the same null are equivalent in linear models was established by Newey and West (1987). Angrist (1991) gives a formal statement of the argument in this paragraph.

{124}------------------------------------------------

hand, in cases where the underlying IV estimates are quite precise, the fact that the over-ID statistic rejects need not point to an identiÖcation failure. Rather, this may be evidence of treatment e§ect heterogeneity, a possibility we discuss further below. On the conceptual side, however, an understanding of the anatomy of the 2SLS minimand is invaluable, for it once again highlights the important link between grouped data and IV. This link takes the mystery out of estimation and testing with instrumental variables and forces us to confront the raw moments that are the foundation for causal inference.

# 4.3 Two-Sample IV and Split-Sample IV<sup>F</sup>

The GMM interpretation of 2SLS highlights the fact that the IV estimator can be constructed from sample moments alone, with no micro data. Returning to the sample moment condition, [\(4.2.3\)](#page-120-0), and re-arranging slightly produces a regression-like equation involving second moments:

<span id="page-124-0"></span>
$$\frac{Z'Y}{N} = \frac{Z'W}{N}\Gamma + \frac{Z'\eta}{N} \tag{4.3.1}$$

GLS estimates of in [\(4.3.1\)](#page-124-0) are consistent because E h Z 0y N i = E h Z 0W N i .

The 2SLS minimand can be thought of as GLS applied to equation [\(4.3.1\)](#page-124-0), after multiplying by <sup>p</sup> N to keep the residual from disappearing as the sample size gets large. In other words, 2SLS minimizes a quadratic form in the residuals from [\(4.3.1\)](#page-124-0) with a (possibly non-diagonal) weighting matrix.[18](#page-124-1) An important insight that comes from writing the 2SLS problem in this way is that we do not need the individual observations in our sample to estimate [\(4.3.1\)](#page-124-0). Just as with the OLS coe¢ cient vector, which can be constructed from the sample conditional mean function, IV estimators can also be constructed from sample moments. The moments needed for IV are <sup>Z</sup> 0y N and <sup>Z</sup> 0W N . The dependent variable, <sup>Z</sup> 0y N , is a vector of dimension [k+q] - 1. The regressor matrix, <sup>Z</sup> 0W N , is of dimension [k+q] - [k+1]. The second-moment equation cannot be solved exactly unless q= 1 so it makes sense to make the Öt as good as possible by minimizing a quadratic form in the residuals. The most e¢ cient weighting matrix for this purpose is the asymptotic covariance matrix of Z 0 p N . This again produces the 2SLS minimand, J^<sup>N</sup> (^g).

A related insight is the fact that the moment matrices on the left and right hand side of the equals sign in equation [\(4.3.1\)](#page-124-0) need not come from the same data sets provided these data sets are drawn from the same population. This observation leads to the two-sample instrumental variables (TSIV) estimator used by Angrist (1990) and developed formally in Angrist and Krueger (1992)[19](#page-124-2) . Brieáy, let Z<sup>1</sup> and y<sup>1</sup> denote

<span id="page-124-1"></span><sup>1 8</sup>A quadratic form is the matrix-weighted product, x <sup>0</sup>Ax, where x is a random vector of, say, dimension k and A is a kk matrix of constants.

<span id="page-124-2"></span><sup>1 9</sup>Applications of TSIV include Bjorklund and Jantti (1997), Jappelli, Pischke, and Souleles (1998), Currie and Yelowitz (2000), and Dee and Evans (2003). In a recent paper, Inoue and Solon (2005) compare the asymptotic distributions of alternative TSIV estimators, and introduce a maximum likelihood (LIML-type) version of TSIV. They also correct a mistake in the distribution theory in Angrist and Krueger (1995), discussed further, below.

{125}------------------------------------------------

the instrument/covariate matrix and dependent variable vector in data set 1 of size N<sup>1</sup> and let Z<sup>2</sup> and W<sup>2</sup> denote the instrument /covariate matrix and endogenous variable/covariate matrix in data set 2 of size N2. Assuming plim Z <sup>2</sup>W<sup>2</sup> N<sup>2</sup> <sup>=</sup> plim Z <sup>1</sup>W<sup>1</sup> N<sup>1</sup> , GLS estimates of the two-sample moment equation

$$\frac{Z_1'\mathbf{Y}_1}{N_1} = \frac{Z_2'W_2}{N_2}\Gamma + \left\{ \left[ \frac{Z_1'W_1}{N_1} - \frac{Z_2'W_2}{N_2} \right]\Gamma + \frac{Z_1'\eta_1}{N_1} \right\}$$

are also consistent for . The limiting distribution of this estimator is obtained by normalizing by p N<sup>1</sup> and assuming plim N<sup>2</sup> N<sup>1</sup> is a constant.

The utility of TSIV comes from the fact that it widens the scope for IV estimation to situations where observations on dependent variables, instruments, and the endogenous variable of interest are hard to Önd in a single sample. It may be easier to Önd one data set that has information on outcomes and instruments, with which the reduced form can be estimated, and another data set which has information on endogenous variables and instruments, with which the Örst stage can be estimated. For example, in Angrist (1990), administrative records from the Social Security Administration (SSA) provide information on the dependent variable (annual earnings) and the instruments (draft lottery numbers coded from dates of birth, as well as covariates for race and year of birth). The SSA, however, does not track participantsíveteran status. This information was taken from military records, which also contain dates of birth that can used to code lottery numbers. Angrist (1990) used these military records to construct <sup>Z</sup> <sup>2</sup>W<sup>2</sup> N<sup>2</sup> , the Örst-stage correlation between lottery numbers and veteran status conditional on race and year of birth, while the SSA data were used to construct <sup>Z</sup> <sup>1</sup>y<sup>1</sup> N<sup>1</sup> .

Two further simpliÖcations make TSIV especially easy to use. First, as noted previously, when the instruments consist of a full set of mutually exclusive dummy variables, as in Angrist (1990) and Angrist and Krueger (1992), the second moment equation, [\(4.3.1\)](#page-124-0), simpliÖes to a model for conditional means. In particular, the 2SLS minimand for the two-sample problem becomes

$$\hat{J}_N(\hat{g}) = \sum_j \omega_j \left( \bar{y}_{1j} - \hat{g}' \bar{W}_{2j} \right)^2, \tag{4.3.2}$$

where y1<sup>j</sup> is the mean of the dependent variable at instrument/covariate value j in one sample, W <sup>2</sup><sup>j</sup> is the mean of endogenous variables and covariates at instrument/covariate value j in a second sample, and !<sup>j</sup> is an appropriate weight. This amounts to weighted least squares estimation of the VIV equation, except that the dependent and independent variables do not come from the same sample. Again, Angrist (1990) and Angrist and Krueger (1992) provide illustrations. The optimal weights for asymptotically e¢ cient TSIV are given by variance of y1<sup>j</sup> g^ 0W <sup>2</sup><sup>j</sup> . This variance is a§ected by the fact that moments come from di§erent samples, as are the TSIV standard errors, which are easy to compute in the dummy-instrument case since the estimator is equivalent to weighted least squares.

{126}------------------------------------------------

Second, Angrist and Krueger (1995) introduced a computationally attractive TSIV-type estimator that requires no matrix manipulation and can be implemented with ordinary regression software. This estimator, called Split-Sample IV (SSIV), works as follows.<sup>20</sup> The first-stage estimates in data set two are given by  $(Z_2'Z_2)^{-1}Z_2'W_2$ . These fitted values can be carried over to data set 1 by constructing the cross-sample fitted value,  $\hat{W}_{12} \equiv Z_1(Z_2'Z_2)^{-1}Z_2'W_2$ . The SSIV second stage is a regression of  $Y_1$  on  $\hat{W}_{12}$ . The correct limiting distribution for this estimator is derived in Inoue and Solon (2005), who show that the limiting distribution presented in Angrist and Krueger (1992) requires the assumption that  $Z_1'Z_1 = Z_2'Z_2$  (as would be true if the marginal distribution of the instruments and covariates is fixed in repeated samples). It's worth noting, however, that the limiting distributions of SSIV and 2SLS are the same when the coefficient on the endogenous variable is zero. The standard errors for this special case are simple to construct and probably provide a reasonably good approximation to the general case.<sup>21</sup>