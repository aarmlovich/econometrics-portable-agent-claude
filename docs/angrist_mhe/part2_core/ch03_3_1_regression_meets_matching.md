# Regression Meets Matching

> Pages: 66-81

The past decade or two has seen increasing interest in matching as an empirical tool. Matching as a strategy to control for covariates is typically motivated by the CIA, as for causal regression in the previous section. For example, Angrist (1998) used matching to estimate the e§ects of volunteering for the military service on the later earnings of soldiers. These matching estimates have a causal interpretation assuming that, conditional on the individual characteristics the military uses to select soldiers (age, schooling, test scores), veteran status is independent of potential earnings.

An attractive feature of matching strategies is that they are typically accompanied by an explicit statement of the conditional independence assumption required to give matching estimates a causal interpretation. At the same time, we have just seen that the causal interpretation of a regression coe¢ cient is based on exactly the same assumption. In other words, matching and regression are both control strategies. Since the core assumption underlying causal inference is the same for the two strategies, itís worth asking whether or to what extent matching really di§ers from regression. Our view is that regression can be motivated as a computational device for a particular sort of weighted matching estimator, and therefore the di§erences between regression and matching are unlikely to be of major empirical importance.

To áesh out this idea, it helps to look more deeply into the mathematical structure of the matching and regressions estimands, i.e., the population quantities that these methods attempt to estimate. For regression, of course, the estimand is a vector of population regression coe¢ cients. The matching estimand is typically

<span id="page-66-0"></span><sup>1 7</sup>Griliches and Mason (1972) is a seminal exploration of the use of early and late ability controls in schooling equations. See also Chamberlain (1977, 1978) for closely related studies. Rosenbaum (1984) o§ers an alternative discussion of the proxy control idea using very di§erent notation, outside of a regression framework.

{67}------------------------------------------------

a particular weighted average of contrasts or comparisons across cells deÖned by covariates. This is easiest to see in the case of discrete covariates, as in the military service example, and for a discrete regressor such as veteran status, which we denote here by the dummy, d<sup>i</sup> . Since treatment takes on only two values, we can use the notation y1<sup>i</sup>=fi(1) and y0<sup>i</sup>=fi(0) to denote potential outcomes. A parameter of primary interest in this context is the average e§ect of treatment on the treated, E[y1<sup>i</sup>y0<sup>i</sup> jd<sup>i</sup> = 1]. This tells us the di§erence between the average earnings of soldiers, E[y1<sup>i</sup> jd<sup>i</sup> = 1], an observable quantity, and the counterfactual average earnings they would have obtained if they had not served, E[y0<sup>i</sup> jd<sup>i</sup> = 1]. Simply comparing the observed earnings di§erential by veteran status is a biased measure of the e§ect of treatment on the treated unless d<sup>i</sup> is independent of y0<sup>i</sup> . SpeciÖcally,

$$\begin{split} E\left[\mathbf{Y}_{i}|\mathbf{D}_{i}=1\right] - E\left[\mathbf{Y}_{i}|\mathbf{D}_{i}=0\right] &= E\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{D}_{i}=1\right] \\ &+ \left\{ E\left[\mathbf{Y}_{0i}|\mathbf{D}_{i}=1\right] - E\left[\mathbf{Y}_{0i}|\mathbf{D}_{i}=0\right] \right\}. \end{split}$$

In other words, the observed earnings di§erence by veteran status equals the average e§ect of treatment on the treated plus selection bias. This parallels the discussion of selection bias in Chapter [2.](#page-24-0)

Given the CIA, selection bias disappears after conditioning on X<sup>i</sup> , so the e§ect of treatment on the treated can be constructed by iterating expectations over X<sup>i</sup> :

$$\begin{split} \delta_{TOT} & \equiv & E[\mathbf{Y}_{1i} - \mathbf{Y}_{0i} | \mathbf{D}_i = 1] \\ & = & E\{E[\mathbf{Y}_{1i} | \mathbf{X}_i, \mathbf{D}_i = 1] - E[\mathbf{Y}_{0i} | \mathbf{X}_i, \mathbf{D}_i = 1] | \mathbf{D}_i = 1\}. \end{split}$$

Of course, E[y0<sup>i</sup> jX<sup>i</sup> ;d<sup>i</sup> = 1] is counterfactual. By virtue of the CIA, however,

$$E[Y_{0i}|X_i, D_i = 0] = E[Y_{0i}|X_i, D_i = 1].$$

Therefore,

<span id="page-67-0"></span>
$$\delta_{TOT} = E\{E[Y_{1i}|X_i, D_i = 1] - E[Y_{0i}|X_i, D_i = 0] | D_i = 1\}$$

$$= E[\delta_X|D_i = 1],$$
(3.3.1)

.

where

$$\delta_X \equiv E[\mathbf{Y}_i | \mathbf{X}_i, \mathbf{D}_i = 1] - E[\mathbf{Y}_i | \mathbf{X}_i, \mathbf{D}_i = 0],$$

is the random X-speciÖc di§erence in mean earnings by veteran status at each value of X<sup>i</sup>

The matching estimator in Angrist (1998) uses the fact that X<sup>i</sup> is discrete to construct the sample analog 

{68}------------------------------------------------

of the right-hand-side of [\(3.3.1\)](#page-67-0). In the discrete case, the matching estimand can be written

<span id="page-68-2"></span>
$$E[Y_{1i} - Y_{0i}|D_i = 1] = \sum_x \delta_x P(X_i = x|D_i = 1),$$
(3.3.2)

where P(X<sup>i</sup> = xjd<sup>i</sup> = 1) is the probability mass function for X<sup>i</sup> given d<sup>i</sup> = 1. [18](#page-68-0) . In this case, X<sup>i</sup> , takes on values determined by all possible combinations of year of birth, test-score group, year of application to the military, and educational attainment at the time of application. The test score in this case is from the AFQT, used by the military to categorize the mental abilities of applicants (we included this as a control in the schooling regression discussed in Section [3.2.2\)](#page-59-0). The Angrist (1998) matching estimator simply replaces <sup>X</sup> by the sample veteran-nonveteran earnings di§erence for each combination of covariates, and then combines these in a weighted average using the empirical distribution of covariates among veterans.[19](#page-68-1)

Note also that we can just as easily construct the unconditional average treatment e§ect,

$$\delta_{ATE} = E\{E[Y_{1i}|X_i, D_i = 1] - E[Y_{0i}|X_i, D_i = 0]\} 
= \sum_{x} \delta_x P(X_i = x) 
= E[Y_{1i} - Y_{0i}],$$
(3.3.3)

which is the expectation of <sup>X</sup> using the marginal distribution of X<sup>i</sup> instead of the distribution among the treated. T OT tells us how much the typical soldier gained or lost as a consequence of military service, while AT E tells us how much the typical applicant to the military gained or lost (since the Angrist, 1998, population consists of applicants.)

The US military tends to be fairly picky about itís soldiers, especially after downsizing at the end of the Cold War. For the most part, the military now takes only high school graduates with test scores in the upper half of the test score distribution. The resulting positive screening generates positive selection bias in naive comparisons of veteran and non-veteran earnings. This can be seen in Table [3.3.1,](#page-61-0) which reports di§erences-in-means, matching, and regression estimates of the e§ect voluntary military service on the 1988-91 Social Security-taxable earnings of men who applied to join the military between 1979 and 1982. The matching estimates were constructed from the sample analog of [\(3.3.2\)](#page-68-2). Although white veterans earn \$1,233 more than nonveterans, this di§erence becomes negative once di§erences in covariates are matched away. Similarly, while non-white veterans earn \$2,449 more than nonveterans, controlling for covariates reduces this to \$840.

<span id="page-68-0"></span><sup>1 8</sup> This matching estimator is discussed by Rubin (1977) and used by Card and Sullivan (1988) to estimate the e§ect of subsidized training on employment.

<span id="page-68-1"></span><sup>1 9</sup>With continuous covariates, exact matching is impossible and some sort of approximation is required, a fact that leads to bias. See Abadie and Imbens (2006), who derive the implications of approximate matching for the limiting distirbution of matching estimators.

{69}------------------------------------------------

<table><tbody><tr><th>Race</th><th>Average<br/>earnings<br/>in 1988-<br/>1991</th><th>Di§erences<br/>in means<br/>by veteran<br/>status</th><th>Matching<br/>estimates</th><th>Regression<br/>estimates</th><th>Regression<br/>minus<br/>matching</th></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Whites</td><td>14537</td><td>1233.4</td><td>-197.2</td><td>-88.8</td><td>108.4</td></tr><tr><td></td><td></td><td>(60.3)</td><td>(70.5)</td><td>(62.5)</td><td>(28.5)</td></tr><tr><td>Non-</td><td>11664</td><td>2449.1</td><td>839.7</td><td>1074.4</td><td>234.7</td></tr><tr><td>whites</td><td></td><td>(47.4)</td><td>(62.7)</td><td>(50.7)</td><td>(32.5)</td></tr></tbody></table>

Table 3.3.1: Uncontrolled, matching, and regression estimates of the e§ects of voluntary military service on earnings

Notes: Adapted from Angrist (1998, Tables II and V). Standard errors are reported in parentheses. The table shows estimates of the e§ect of voluntary military service on the 1988-1991 Social Security- taxable earnings of men who applied to enter the armed forces between 1979 and 1982. The matching and regression estimates control for applicantsíyear of birth, education at the time of application, and AFQT score. There are 128,968 whites and 175,262 nonwhites in the sample.

Table [\(3.3.1\)](#page-61-0) also shows regression estimates of the e§ect of voluntary military service, controlling for the same set of covariates that were used to construct the matching estimates. These are estimates of <sup>R</sup> in the equation

<span id="page-69-0"></span>
$$Y_i = \sum_x d_{ix} \beta_x + \delta_R D_i + \varepsilon_i, \qquad (3.3.4)$$

where dix is a dummy that indicates X<sup>i</sup> = x, <sup>x</sup> is a regression-e§ect for X<sup>i</sup> = x, and <sup>R</sup> is the regression estimand. Note that this regression model allows a separate parameter for every value taken on by the covariates. This model can therefore be said to be saturated-in-X<sup>i</sup> , since it includes a parameter for every value of X<sup>i</sup> (it is not "fully saturated," however, because there is a single additive e§ect for d<sup>i</sup> with no d<sup>i</sup> X<sup>i</sup> interactions).

Despite the fact that the matching and regression estimates control for the same variables, the regression estimates in Table [3.3.1](#page-61-0) are somewhat larger than the matching estimates for both whites and nonwhites. In fact, the di§erences between the matching and regression results are statistically signiÖcant. At the same time, the two estimation strategies present a broadly similar picture of the e§ects of military service. The reason the regression and matching estimates are similar is that regression, too, can be seen as a sort of matching estimator: the regression estimand di§ers from the matching estimands only in the weights used to sum the covariate-speciÖc e§ects, <sup>X</sup> into a single e§ect. In particular, matching uses the distribution of covariates among the treated to weight covariate-speciÖc estimates into an estimate of the e§ect of treatment on the treated, while regression produces a variance-weighted average of these e§ects.

{70}------------------------------------------------

To see this, start by using the regression anatomy formula to write the coefficient on  $D_i$  in the regression of  $Y_i$  on  $X_i$  and  $D_i$  as

<span id="page-70-0"></span>
$$\delta_{R} = \frac{Cov(Y_{i}, \tilde{D}_{i})}{V(\tilde{D}_{i})}$$

$$= \frac{E[(D_{i} - E[D_{i}|X_{i}])Y_{i}]}{E[(D_{i} - E[D_{i}|X_{i}])^{2}]}$$

$$= \frac{E\{(D_{i} - E[D_{i}|X_{i}])E[Y_{i}|D_{i}, X_{i}]\}}{E[(D_{i} - E[D_{i}|X_{i}])^{2}]}.$$
(3.3.5)

The second equality in this set of expressions uses the fact that saturating the model in  $X_i$  means  $E[D_i|X_i]$  is linear. Hence,  $\tilde{D}_i$ , which is defined as the residual from a regression of  $D_i$  on  $X_i$ , is the difference between  $D_i$  and  $E[D_i|X_i]$ . The third equality uses the fact that the regression of  $Y_i$  on  $D_i$  and  $X_i$  is the same as the regression of  $Y_i$  on  $E[Y_i|D_i,X_i]$ .

To simplify further, we expand the CEF,  $E[Y_i|D_i,X_i]$ , to get

$$E[\mathbf{Y}_i|\mathbf{D}_i, \mathbf{X}_i] = E[\mathbf{Y}_i|\mathbf{D}_i = 0, \mathbf{X}_i] + \delta_X \mathbf{D}_i.$$

If covariates are unnecessary - in other words, the CIA holds unconditionally, as if in a randomized trial this CEF becomes

$$E[Y_i|D_i, X_i] = E[Y_i|D_i = 0] + E[Y_{1i} - Y_{0i}]D_i$$

from which we conclude that the regression of  $Y_i$  on  $D_i$  estimates the population average treatment effect in this case (e.g., as in the experiment discussed in Section 2.3). But here we are interested in the more general scenario where conditioning  $X_i$  is necessary to eliminate selection bias.

To evaluate the more general regression estimand, (3.3.5), we begin by substituting for  $E[Y_i|D_i,X_i]$  in the numerator. This gives

$$E\{(\mathbf{D}_{i} - E[\mathbf{D}_{i}|\mathbf{X}_{i}])E[\mathbf{Y}_{i}|\mathbf{D}_{i},\mathbf{X}_{i}]\} = E\{(\mathbf{D}_{i} - E[\mathbf{D}_{i}|\mathbf{X}_{i}])E[\mathbf{Y}_{i}|\mathbf{D}_{i} = 0,\mathbf{X}_{i}]\} + E\{(\mathbf{D}_{i} - E[\mathbf{D}_{i}|\mathbf{X}_{i}])\mathbf{D}_{i}\delta_{X}\}.$$

The first term on the right-hand side is zero because  $E[Y_i|D_i = 0,X_i]$  is a function of  $X_i$  and is therefore uncorrelated with  $(D_i - E[D_i|X_i])$ . For the same reason, the second term simplifies to

$$E\{(\mathbf{D}_i - E[\mathbf{D}_i | \mathbf{X}_i]) \mathbf{D}_i \delta_X\} = E\{(\mathbf{D}_i - E[\mathbf{D}_i | \mathbf{X}_i])^2 \delta_X\}.$$

At this point, we've shown

<span id="page-70-1"></span>
$$\delta_R = \frac{E[(D_i - E[D_i | X_i])^2 \delta_X]}{E[(D_i - E[D_i | X_i])^2]} = \frac{E\{E[(D_i - E[D_i | X_i])^2 | X_i] \delta_X\}}{E\{E[(D_i - E[D_i | X_i])^2 | X_i]\}} = \frac{E[\sigma_D^2(X_i) \delta_X]}{E[\sigma_D^2(X_i)]},$$
(3.3.7)

{71}------------------------------------------------

where

$$\sigma_D^2(\mathbf{X}_i) = E[(\mathbf{D}_i - E[\mathbf{D}_i|\mathbf{X}_i])^2 | \mathbf{X}_i]$$

is the conditional variance of d<sup>i</sup> given X<sup>i</sup> . This establishes that the regression model, [\(3.3.4\)](#page-69-0), produces a treatment-variance weighted average of X:

Because the regressor of interest, d<sup>i</sup> is a dummy variable, one last step can be taken. In this case, <sup>D</sup>(Xi) = P(d<sup>i</sup> = 1jXi)(1 P(d<sup>i</sup> = 1jXi)), so

$$\delta_R = \frac{\sum_{x} \delta_x \left[ P(\mathbf{D}_i = 1 | \mathbf{X}_i = x) (1 - P(\mathbf{D}_i = 1 | \mathbf{X}_i = x)) \right] P\left(\mathbf{X}_i = x\right)}{\sum_{x} \left[ P(\mathbf{D}_i = 1 | \mathbf{X}_i = x) (1 - P(\mathbf{D}_i = 1 | \mathbf{X}_i = x)) \right] P\left(\mathbf{X}_i = x\right)}$$

This shows that the regression estimand weights each covariate-speciÖc treatment e§ect by [P(X<sup>i</sup> = xjd<sup>i</sup> = 1)(1 P(X<sup>i</sup> = xjd<sup>i</sup> = 1))]P (X<sup>i</sup> = x). In contrast, the matching estimand for the e§ect of treatment on the treated can be written

$$E[\mathbf{Y}_{1i} - \mathbf{Y}_{0i} | \mathbf{D}_i = 1] = \sum_{x} \delta_x P(\mathbf{X}_i = x | \mathbf{D}_i = 1) = \frac{\sum_{x} \delta_x P(\mathbf{D}_i = 1 | \mathbf{X}_i = x) P(\mathbf{X}_i = x)}{\sum_{x} P(\mathbf{D}_i = 1 | \mathbf{X}_i = x) P(\mathbf{X}_i = x)}$$

because

$$P(X_i = x | D_i = 1) = \frac{P(D_i = 1 | X_i = x) \cdot P(X_i = x)}{P(D_i = 1)}.$$

So the weights used to construct E[y1<sup>i</sup>y0<sup>i</sup> jd<sup>i</sup> = 1] are proportional to the probability of treatment at each value of the covariates.

The point of this derivation is that the treatment-on-the-treated estimand puts the most weight on covariate cells containing those who are most likely to be treated. In contrast, regression puts the most weight on covariate cells where the conditional variance of treatment status is largest. As a rule, this variance is maximized when <sup>P</sup>(d<sup>i</sup> = 1jX<sup>i</sup> <sup>=</sup> <sup>x</sup>) = <sup>1</sup> 2 , in other words, for cells where there are equal numbers of treated and control observations. Of course, the di§erence in weighting schemes is of little importance if <sup>x</sup> does not vary across cells (though weighting still a§ects the statistical e¢ ciency of estimators). In this example, however, men who were most likely to serve in the military appear to beneÖt least from their service. This is probably because those most likely to serve were most qualiÖed, but therefore also had the highest civilian earnings potential and so beneÖted least from military service. This fact leads matching estimates of the e§ect of military service to be smaller than regression estimates based on the same vector of control variables.[20](#page-71-0)

<span id="page-71-0"></span><sup>2 0</sup> Itís no surprise that regression gives the most weight to cells where <sup>P</sup>(d<sup>i</sup> = 1jX<sup>i</sup> <sup>=</sup> <sup>x</sup>) = 1=<sup>2</sup> since regression is e¢ cient for a homoskedastic constant-e§ects linear model. We should expect an e¢ cient estimator to give the most weight to cells where the common treatment e§ect is estimated most precisely. With homoskedastic residuals, the most precise treatment e§ects

{72}------------------------------------------------

Importantly, neither the regression nor the covariate-matching estimands give any weight to covariate cells that do not contain both treated and control observations. Consider a value of X<sup>i</sup> , say x , where either no one is treated or everyone is treated. Then, <sup>x</sup> is undeÖned, while the regression weights, [P(d<sup>i</sup> = 1jX<sup>i</sup> = x )(1 P(d<sup>i</sup> = 1jX<sup>i</sup> = x ))] ; are zero: In the language of the econometric literature on matching, both the regression and matching estimands impose common support, that is, they are limited to covariate values where both treated and control observations are found.[21](#page-72-0)

The step from estimand to estimator is a little more complicated. In practice, both regression and matching estimators are implemented using modelling assumptions that implicitly involve a certain amount of extrapolation across cells. For example, matching estimators often combine covariates cells with few observations. This violates common support if the cells being combined do not each have both treated and non-treated observations. Regression models that are not saturated in X<sup>i</sup> may also violate common support, since covariate cells without both treated and control observations can end up contributing to the estimates by extrapolation. Here too, however, we see a symmetry between the matching and regression strategies: they are in the same class, in principle, and require the same sort of compromises in practice.[22](#page-72-1)

#### Even More on Regression and Matching: Ordered and Continuous Treatments<sup>F</sup>

Does the pseudo-matching interpretation of regression outlined above for a binary treatment apply to models with ordered and continuous treatments? The long answer is fairly technical and may be more than you want to know. The short answer is, to one degree or another, "yes."

As weíve already discussed, one interpretation of regression is that the population OLS slope vector provides the MMSE linear approximation to the CEF. This, of course, works for ordered and continuous regressors as well as for binary. A related property is the fact that regression coe¢ cients have an ìaverage derivativeîinterpretation. In multivariate regression models, this interpretation is unfortunately complicated by the fact that the OLS slope vector is a matrix-weighted average of the gradient of the CEF. Matrixweighted averages are di¢ cult to interpret except in special cases (see Chamberlain and Leamer, 1976). An important special case when the average derivative property is relatively straightforward is in regression models for an ordered or continuous treatment with a saturated model for covariates. To avoid lengthy derivations, we simply explain the formulas. A derivation is sketched in the appendix to this chapter. For additional details, see the appendix to Angrist and Krueger (1999).

come from cells where the probability of treatment equals 1=2.

<span id="page-72-0"></span><sup>2 1</sup> The support of a random variable is the set of realizations that occur with positive probability. See Heckman, Ichimura, Smith, and Todd (1998) and Smith and Todd (2001) for a discussion of common support in matching.

<span id="page-72-1"></span><sup>2 2</sup>Matching problems involving Önely distributed X-variables are often solved by aggregating values to make coarser groupings or by pairing observations that have similar, though not necessarily identical values. See Cochran (1965), Rubin (1973), or Rosenbaum (1995, Chapter 3) for discussions of this approach. With continuously-distributed covariates, matching estimators are biased because matches are imperfect. Abadie and Imbens (2008) have recently shown that a regression-based bias correction can eliminate the (asymptotic) bias from imperfect matches.

{73}------------------------------------------------

For the purposes of this discussion, the treatment intensity,  $s_i$ , is assumed to be a continuously distributed random variable, not necessarily non-negative. Suppose that the CEF of interest can be written  $h(t) \equiv E[Y_i|s_i = t]$  with derivative h'(t). Then

<span id="page-73-0"></span>
$$\frac{E[Y_i(S_i - E[S_i])]}{E[S_i(S_i - E[S_i])]} = \frac{\int h'(t) \mu_t dt}{\int \mu_t dt}$$
(3.3.8)

where

<span id="page-73-2"></span>
$$\mu_t \equiv \{ E[\mathbf{s}_i | \mathbf{s}_i \ge t] - E[\mathbf{s}_i | \mathbf{s}_i < t] \} \{ P(\mathbf{s}_i \ge t) [1 - P(\mathbf{s}_i \ge t)] \}, \tag{3.3.9}$$

and the integrals in (3.3.8) run over the possible values of  $s_i$ . This formula weights each possible value of  $s_i$  in proportion to the difference in the conditional mean of  $s_i$  above and below that value. More weight is also given to points close to the median of  $s_i$  since  $P(s_i \ge t) \cdot [1 - P(s_i \ge t)]$  is maximized at  $P(s_i \ge t) = 1/2$ .

With covariates,  $X_i$ , the weights in (3.3.8) become X-specific. A covariate-averaged version of the same formula applies to the multivariate regression coefficient of  $Y_i$  on  $S_i$ , after partialling out  $X_i$ . In particular,

<span id="page-73-1"></span>
$$\frac{E[Y_i(S_i - E[S_i|X_i])]}{E[S_i(S_i - E[S_i|X])]} = \frac{E\left[\int h_X'(t)\mu_{tX}dt\right]}{E\left[\int \mu_{tX}dt\right]},$$
(3.3.10)

where  $h_X'(t) \equiv \frac{\partial E[\mathbf{Y}_i|\mathbf{X}_i,\mathbf{s}_i=t]}{\partial t}$  and  $\mu_{tX} \equiv \{E[\mathbf{s}_i|\mathbf{X}_i,\mathbf{s}_i\geq t] - E[\mathbf{s}_i|\mathbf{X}_i,\mathbf{s}_i< t]\}\{P(\mathbf{s}_i\geq t|\mathbf{X}_i)[1-P(\mathbf{s}_i\geq t|\mathbf{X}_i)\}$ . It bears emphasizing that equation (3.3.10) reflects two types of averaging: an integral that averages along the length of a nonlinear CEF at fixed covariate values, and an expectation that averages across covariate cells. An important point in this context is that population regression coefficients contain no information about the effect of  $\mathbf{s}_i$  on the CEF for values of  $\mathbf{X}_i$  where  $P(\mathbf{s}_i\geq t|\mathbf{X}_i)$  equals 0 or 1. This includes values of  $\mathbf{X}_i$  where  $\mathbf{s}_i$  is fixed. In the same spirit, it's worth noting that if  $\mathbf{s}_i$  is a dummy variable, we can extract equation (3.3.7) from the more general formula, (3.3.10).

Angrist and Krueger (1999) construct the average weighting function for a schooling regression with state of birth and year of birth covariates. Although equations (3.3.8) and (3.3.10) may seem arcane or at least non-obvious, in this example the average weights,  $E[\mu_{tX}]$ , turn out to be a reasonably smooth symmetric function of t, centered at the mode of  $s_i$ .

The implications of (3.3.8) or (3.3.10) can be explored further given a model for the distribution of regressors. Suppose, for example, that  $s_i$  is Normally distributed. Let  $z_i = \frac{s_i - E(s_i)}{\sigma_s}$ , where  $\sigma_s$  is the standard deviation of  $s_i$ , so that  $z_i$  is standard Normal. Then

$$E[\mathbf{s}_i|\mathbf{s}_i \ge t] = E(\mathbf{s}_i) + \sigma_s E\left[z_i|z_i \ge \frac{\mathbf{t} - E(\mathbf{s}_i)}{\sigma_s}\right] = E(\mathbf{s}_i) + \sigma_s E\left[z_i|z_i \ge t^*\right].$$

{74}------------------------------------------------

From truncated Normal formulas (see, e.g., Johnson and Kotz, 1970), we know that

$$E[z_i|z_i > t^*] = \frac{\phi(t^*)}{[1 - \Phi(t^*)]}$$
 and  $E[z_i|z_i < t^*] = \frac{-\phi(t^*)}{\Phi(t^*)}$ .

where  $\phi(\cdot)$  and  $\Phi(\cdot)$  are the standard Normal density and distribution function. Substituting in the formula for  $\mu_t$ , (3.3.9), we have

$$\mu_t = \sigma_s \left\{ \frac{\phi(t^*)}{[1 - \Phi(t^*)]} - \frac{-\phi(t^*)}{\Phi(t^*)} \right\} [1 - \Phi(t^*)] \Phi(t^*) = \sigma_s \phi(t^*).$$

We have therefore shown that

$$\frac{Cov(\mathbf{Y}_i, \mathbf{S}_i)}{V(\mathbf{S}_i)} = E[h'(\mathbf{S}_i)].$$

In other words, the regression of  $Y_i$  on  $S_i$  is the (unweighted!) population average derivative,  $E[h'(s_i)]$ , when  $S_i$  is Normally distributed. Of course, this result is a special case of a special case.<sup>23</sup> Still, it seems reasonable to imagine that Normality might not matter very much. And in our empirical experience, the average derivatives (also called "marginal effects") constructed from parametric nonlinear models for limited dependent variables (e.g., Probit or Tobit) are usually indistinguishable from the corresponding regression coefficients, regardless of the distribution of regressors. We expand on this point in Section 3.4.2, below.

#### 3.3.2 Control for Covariates Using the Propensity Score

The most important result in regression theory is the omitted variables bias formula: coefficients on included variables are unaffected by the omission of variables when the variables omitted are uncorrelated with the variables included. The propensity score theorem, due to Rosenbaum and Rubin (1983), extends this idea to estimation strategies that rely on matching instead of regression, where the causal variable of interest is a treatment dummy.<sup>24</sup>

The propensity score theorem states that if potential outcomes are independent of treatment status conditional on a multivariate covariate vector,  $X_i$ , then potential outcomes are independent of treatment status conditional on a scalar function of covariates, the propensity score, defined as  $p(X_i) \equiv E[D_i|X_i]$ . Formally, we have

**Theorem 3.3.1** The Propensity-Score Theorem.

Suppose the CIA holds for  $Y_{ii}$ ; j = 0, 1. Then  $Y_{ii} \coprod D_i | p(X_i)$ .

<span id="page-74-0"></span><sup>&</sup>lt;sup>23</sup>More specialized results in this spirit appear in Ruud (1986), who considers distribution-free estimation of limited-dependent-variable models with Normally distributed regressors.

<span id="page-74-1"></span><sup>&</sup>lt;sup>24</sup>Propensity-score methods can be adapted to multi-valued treatments, though this has yet to catch on. See Imbens (2000) for an effort in this direction.

{75}------------------------------------------------

**Proof.** The claim is true if  $P[D_i = 1|Y_{ji}, p(X_i)]$  does not depend on  $Y_{ji}$ .

$$\begin{split} P[\mathbf{D}_{i} &= 1 | \mathbf{Y}_{ji}, p(\mathbf{X}_{i})] &= E[\mathbf{D}_{i} | \mathbf{Y}_{ji}, p(\mathbf{X}_{i})] \\ &= E\{E[\mathbf{D}_{i} | \mathbf{Y}_{ji}, p(\mathbf{X}_{i}), \mathbf{X}_{i}] | \mathbf{Y}_{ji}, p(\mathbf{X}_{i})\} \\ &= E\{E[\mathbf{D}_{i} | \mathbf{Y}_{ji}, \mathbf{X}_{i}] | \mathbf{Y}_{ji}, p(\mathbf{X}_{i})\} \\ &= E\{E[\mathbf{D}_{i} | \mathbf{X}_{i}] | \mathbf{Y}_{ji}, p(\mathbf{X}_{i})\}, \text{ by the CIA.} \end{split}$$

But 
$$E\{E[D_i|X_i]|Y_{ji}, p(X_i)\} = E\{p(X_i)|Y_{ji}, p(X_i)\}$$
, which is clearly just  $p(X_i)$ .

Like the OVB formula for regression, the propensity score theorem says you need only control for covariates that affect the probability of treatment. But it also says something more: the only covariate you really need to control for is the probability of treatment itself. In practice, the propensity score theorem is usually used for estimation in two steps: first,  $p(X_i)$  is estimated using some kind of parametric model, say, Logit or Probit. Then estimates of the effect of treatment are computed either by matching on the fitted values from this first step, or by a weighting scheme described below (see, Imbens, 2004, for an overview).

In practice there are many ways to use the propensity score theorem for estimation. Direct propensityscore matching works like covariate matching, except that we match on the score instead of the covariates directly. By the propensity score theorem and the CIA,

$$E[Y_{1i} - Y_{0i}|D_i = 1] = E\{E[Y_i|p(X_i), D_i = 1] - E[Y_i|p(X_i), D_i = 0]|D_i = 1\}.$$

Estimates of the effect of treatment on the treated can therefore be obtained by stratifying on an estimate of  $p(X_i)$  and substituting conditional sample averages for expectations or by matching each treated observation to controls with the same or similar values of the propensity score (both of these approaches were used by Dehejia and Wahba, 1999). Alternately, a model-based or non-parametric estimate of  $E[Y_i|p(X_i),D_i]$  can be substituted for these conditional mean functions and the outer expectation replaced with a sum (as in Heckman, Ichimura, and Todd, 1998).

The somewhat niftier weighting approach to propensity-score estimation skips the cumbersome matching step by exploiting the fact that the CIA implies  $E\left[\frac{\mathbf{Y}_i\mathbf{D}_i}{p(\mathbf{X}_i)}\right] = E[\mathbf{Y}_{1i}]$  and  $E\left[\frac{\mathbf{Y}_i(1-\mathbf{D}_i)}{(1-p(\mathbf{X}_i))}\right] = E[\mathbf{Y}_{0i}]$ . Therefore, given a scheme for estimating  $p(\mathbf{X}_i)$ , we can construct estimates of the average treatment effect from the sample analog of

<span id="page-75-0"></span>
$$E[Y_{1i} - Y_{0i}] = E\left[\frac{Y_{i}D_{i}}{p(X_{i})} - \frac{Y_{i}(1 - D_{i})}{1 - p(X_{i})}\right]$$

$$= E\left[\frac{(D_{i} - p(X_{i}))Y_{i}}{p(X_{i})(1 - p(X_{i}))}\right].$$
(3.3.11)

This last expression is an estimand of the form suggested by Newey (1990) and Robins, Mark, and Newey

{76}------------------------------------------------

(1992). We can similarly calculate the effect of treatment on the treated from the sample analog of:

<span id="page-76-0"></span>
$$E[Y_{1i} - Y_{0i}|D_i = 1] = E\left[\frac{(D_i - p(X_i))Y_i}{(1 - p(X_i))P(D_i)}\right].$$
(3.3.12)

The idea that you can correct for non-random sampling by weighting by the reciprocal of the probability of selection dates back to Horvitz and Thompson (1952). Of course, to make this approach feasible, and for the resulting estimates to be consistent, we need a consistent estimator for  $p(X_i)$ 

The Horvitz-Thompson version of the propensity-score approach is appealing since the estimator is essentially automated, with no cumbersome matching required. The Horvitz-Thompson approach also highlights the close link between propensity-score matching and regression, much as discussed for covariate matching in section 3.3.1. Consider again the regression estimand,  $\delta_R$ , for the population regression of  $Y_i$  on  $D_i$ , controlling for a saturated model for covariates. This estimand can be written

$$\delta_R = \frac{E[(D_i - p(X_i))Y_i]}{E[p(X_i)(1 - p(X_i))]}.$$
(3.3.13)

The two Horvitz-Thompson matching estimands and the regression estimand are all members of the class of weighted average estimands considered by Hirano, Imbens, and Ridder (2003):

$$E\left\{g(\mathbf{X}_i)\left[\frac{\mathbf{Y}_i\mathbf{D}_i}{p(\mathbf{X}_i)} - \frac{\mathbf{Y}_i(1-\mathbf{D}_i)}{(1-p(\mathbf{X}_i))}\right]\right\},\tag{3.3.14}$$

where  $g(X_i)$  is a known weighting function (To go from estimator, replace  $p(X_i)$  with a consistent estimator, and expectations with sums). For the average treatment effect, set  $g(X_i) = 1$ ; for the effect on the treated, set  $g(X_i) = \frac{p(X_i)}{P(D_i)}$ ; and for regression set

$$g(X_i) = \frac{p(X_i)(1 - p(X_i))}{E[p(X_i)(1 - p(X_i))]}.$$

This similarity highlights once again the fact that regression and matching—including propensity score matching—are not really different animals, at least not until we specify a model for the propensity score.

A big question here is how best to model and estimate  $p(X_i)$ , or how much smoothing or stratification to use when estimating  $E[Y_i|p(X_i),D_i]$ , especially if the covariates are continuous. The regression analog of this question is how to parametrize the control variables (e.g., polynomials or main effects and interaction terms if the covariates are coded as discrete). The answer to this is inherently application-specific. A growing empirical literature suggests that a Logit model for the propensity score with a few polynomial terms in continuous covariates works well in practice, though this cannot be a theorem (see, e.g., Dehejia and Wahba, 1999).

A developing theoretical literature has produced some thought-provoking theorems on efficient use of the

{77}------------------------------------------------

propensity score. First, from the point of view of asymptotic e¢ ciency, there is usually a cost to matching on the propensity score instead of full covariate matching. We can get lower asymptotic standard errors by matching on any covariate that explains outcomes, whether or not it turns up in the propensity score. This we know from Hahnís (1998) investigation of the maximal precision that it is possible to obtain for estimates of treatment e§ects under the CIA, with and without knowledge of the propensity score. For example, in Angrist (1998), there is an e¢ ciency gain from matching on year of birth, even if the probability of serving in the military is unrelated to birth year, because earnings are related to birth year. A regression analog for this point is the result that even in a scenario with no omitted variables bias, the long regression generates more precise estimates of the coe¢ cients on the variables included in a short regression whenever these variables have some predictive power for outcomes because these covariates lead to a smaller residual variance (see Section [3.1.3\)](#page-45-0).

Hahnís (1998) results raise the question of why we should ever bother with estimators that use the propensity score. A philosophical argument is that the propensity score rightly focuses researcher attention on models for treatment assignment, something about which we may have reasonably good information, instead of the typically more complex and mysterious process determining outcomes. This view seems especially compelling when treatment assignment is the outcome of human institutions or government regulations while the process determining outcomes is more anonymous (e.g., a market). For example, in a time series evaluation of the causal e§ects of monetary policy, Angrist and Kuersteiner (2004) argue that we know more about how the Federal Reserve sets interests rates than about the process determining GDP. In the same spirit, it may also be easier to validate a model for treatment assignment than to validate a model for outcomes (see, e.g., Rosenbaum and Rubin, 1985, for a version of this argument).

A more precise though purely statistical argument for using the propensity score is laid out in Angrist and Hahn (2004). This paper shows that even though there is no asymptotic e¢ ciency gain from the use of estimators based on the propensity score, there will often be a gain in precision in Önite samples. Since all real data sets are Önite, this result is empirically relevant. Intuitively, if the covariates omitted from the propensity score explain little of the variation in outcomes (in a purely statistical sense), it may then be better to ignore them than to bear the statistical burden imposed by the need to estimate their e§ects. This is easy to see in studies using data sets such as the NLSY where there are hundreds of covariates that might predict outcomes. In practice, we focus on a small subset of all possible covariates. This subset is chosen with an eye to what predicts treatment as well as outcomes.

Finally, Hirano, Imbens, and Ridder (2003) provide an alternative asymptotic resolution of the ìpropensity score paradoxî generated by Hahnís (1998) theorems. They show that even though estimates of treatment e§ects based on a known propensity score are ine¢ cient, for models with continuous covariates, a Horvitz-Thompson-type weighting estimator is e¢ cient when weighting uses a non-parametric estimate of the score. The fact that the propensity score is estimated and the fact that it is estimated non-parametrically 

{78}------------------------------------------------

are both key for the Hirano, Imbens, and Ridder conclusions.

Do the Hirano, Imbens, and Ridder (2003) results resolve the propensity-score paradox? For the moment, we prefer the Önite-sample resolution given by Angrist and Hahn (2004). Their results highlight the fact that it is the researchersíwillingness to impose some restrictions on the score which gives propensity-score-based inference its conceptual and statistical power. In Angrist (1998), for example, an application with highdimensional though discrete covariates, the unrestricted non-parametric estimator of the score is just the empirical probability of treatment in each covariate cell. With this nonparametric estimator plugged in for p(Xi), itís straightforward to show that the sample analogs of [\(3.3.11\)](#page-75-0) and [\(3.3.12\)](#page-76-0) are algebraically equivalent to the corresponding full-covariate matching estimators. Hence, itís no surprise that score-based estimation comes out e¢ cient, since full-covariate matching is the asymptotically e¢ cient benchmark. An essential element of propensity score methods is the use of prior knowledge for dimension reduction. The statistical payo§ is an improvement in Önite-sample behavior. If youíre not prepared to smooth, restrict, or otherwise reduce the dimensionality of the matching problem in a manner that has real empirical consequences, then you might as well go for full covariate matching or saturated regression control.

#### 3.3.3 Propensity-Score Methods vs. Regression

Propensity-score methods shift attention from the estimation of E[y<sup>i</sup> jX<sup>i</sup> ;d<sup>i</sup> ] to the estimation of the propensity score, p(Xi) E[d<sup>i</sup> jX<sup>i</sup> ]. This is attractive in applications where the latter is easier to model or motivate. For example, Ashenfelter (1978) showed that participants in government-funded training programs often have su§ered a marked pre-program dip in earnings, a pattern found in many later studies. If this dip is the only thing that makes trainees special, then we can estimate the causal e§ect of training on earnings by controlling for past earnings dynamics. In practice, however, itís hard to match on earnings dynamics since earnings histories are both continuous and multi-dimensional. Dehejia and Wahba (1999) argue in this context that the causal e§ects of training programs are better estimated by conditioning on the propensity score than by conditioning on the earnings histories themselves.

The propensity-score estimates reported by Dehejia and Wahba are remarkably close to the estimates from a randomized trial that constitute their benchmark. Nevertheless, we believe regression should be the starting point for most empirical projects. This is not a theorem; undoubtedly, there are circumstances where propensity score matching provides more reliable estimates of average causal e§ects. The Örst reason we donít Önd ourselves on the propensity-score bandwagon is practical: there are many details to be Ölled in when implementing propensity-score matching - such as how to model the score and how to do inference these details are not yet standardized. Di§erent researchers might therefore reach very di§erent conclusions, even when using the same data and covariates. Moreover, as weíve seen with the Horvitz-Thompson estimands, there isnít very much theoretical daylight between regression and propensity-score weighting. If the regression model for covariates is fairly áexible, say, close to saturated, regression can be seen as a type 

{79}------------------------------------------------

of propensity-score weighting, so the di§erence is mostly in the implementation. In practice you may be far from saturation, but with the right covariates this shouldnít matter.

The face-o§ between regression and propensity-score matching is illustrated here using the same National Supported Work (NSW) sample featured in Dehejia and Wahba (1999).[25](#page-79-0) The NSW is a mid-1970s program that provided work experience to a sample with weak labor-force attachment. Somewhat unusually for itís time, the NSW was evaluated in a randomized trial. Lalondeís (1986) path-breaking analysis compared the results from the NSW randomized study to econometric results using non-experimental control groups drawn from the PSID and the CPS. He came away pessimistic because plausible non-experimental methods generated a wide range of results, many of which were far from the experimental estimates. Moreover, Lalonde argued, an objective investigator, not knowing the results of the randomized trial, would be unlikely to pick the best econometric speciÖcations and observational control groups.

In a striking second take on the Lalonde (1986) Öndings, Dehejia and Wahba (1999) found that they could come close to the NSW experimental results by matching the NSW treatment group to observational control groups selected using the propensity score. They demonstrated this using various comparison groups. Following Dehejia and Wahba (1999), we look again at two of the CPS comparison groups, Örst, a largely unselected sample (CPS-1) and then a narrower comparison group selected from the recently unemployed (CPS-3).

Table [3.3.2](#page-82-0) (a replication of Table 1 in Dehejia and Wahba, 1999) reports descriptive statistics for the NSW treatment group, the randomly selected NSW control group, and our two observational control groups. The NSW treatment group and the randomly selected NSW control groups are younger, less educated, more likely to be nonwhite, and have much lower earnings than the general population represented by the CPS-1 sample. The CPS-3 sample matches the NSW treatment group more closely but still shows some di§erences, particularly in terms of race and pre-program earnings.

Table [3.3.3](#page-83-0) reports estimates of the NSW treatment e§ect. The dependent variable is annual earnings in 1978, a year or two after treatment. Rows of the table show results with alternative sets of controls: none; all the demographic variables in Table [3.3.2;](#page-82-0) lagged (1975) earnings; demographics plus lagged earnings; demographics and two lags of earnings. All estimates are from regressions of 1978 earnings on a treatment dummy plus controls (the raw treatment-control di§erence appears in the Örst row).

Estimates using the experimental control group, reported in column 1, are in the order of \$1,600-1,800. Not surprisingly, these estimates vary little across speciÖcations. In contrast, the raw earnings gap between NSW participants and the CPS-1 sample, reported in column 2, is roughly \$-8,500, suggesting this comparison is heavily contaminated by selection bias. The addition of demographic controls and lagged earnings narrows the gap considerably; the estimated treatment e§ect reaches (positive) \$800 in the last row. The results

<span id="page-79-0"></span><sup>2 5</sup>An similar but more extended propensity-score face-o§ appears in the exchange beween Smith and Todd (2005) and Dehejia (2005).

{80}------------------------------------------------

are even better in column 3, which uses the narrower CPS-3 comparison group. The characteristics of this group are much closer to the those of NSW participants; consistent with this, the raw earnings di§erence is only \$-635. The fully-controlled estimate, reported in the last row, is close to \$1,400, not far from the experimental treatment e§ect.

A drawback of the process taking us from CPS-1 to CPS-3 is the ad hoc nature of the rules used to construct the smaller and more carefully-selected CPS-3 comparison group. The CPS-3 selection criteria can be motivated by the NSW program rules, which favor individuals with low earnings and weak labor-force attachment, but in practice, there are many ways to implement this. Weíd therefore like a more systematic approach to pre-screening. In a recent paper, Crump, Hotz, Imbens and Mitnik (2006) suggest that the propensity score be used for systematic sample-selection as a precursor to regression estimation. This contrasts with our earlier discussion of the propensity score as the basis for an estimator.

We implemented the Crump, et al. (2006) suggestion by Örst estimating the propensity score on a pooled NSW-treatment and observational-comparison sample, and then picking only those observations with 0:1 < p(Xi) < 0:9. In other words, the estimation sample is limited to observations with a predicted probability of treatment equal to at least 10 percent, but no more than 90 percent. This ensures that regressions are estimated with a sample including only covariate cells with there are at least a few treated and control observations. Estimation using screened samples therefore requires no extrapolation to cells without "common support", i.e. to cells where there is no overlap in the covariate distribution between treatment and controls. Descriptive statistics for samples screened on the score (estimated using the full set of covariates listed in the table) appear in the last two columns of Table [3.3.2.](#page-82-0) The covariate means in screened CPS-1 and CPS-3 are much closer to the NSW means in column 1 than are the covariate means from unscreened samples.

We explored the common-support screener further using alternative sets of covariates, but with the same covariates used for both screening and the estimation of treatment e§ects at each iteration. The resulting estimates are displayed in the Önal two columns of Table [3.3.3.](#page-83-0) Controlling for demographic variables or lagged earnings alone, these results di§er little from those in columns 2-3. With both demographic variables and a single lag of earnings as controls, however, the screened CPS-1 estimates are quite a bit closer to the experimental estimates than are the unscreened results. Screened CPS-1 estimates with two lags of earnings remain close to the experimental benchmark. On the other hand, the common-support screener improves the CPS-3 results only slightly with a single lag of earnings and seems to be a step backward with two.

This investigation boosts our (already strong) faith in regression. Regression control for covariates does a good job of eliminating selection bias in the CPS-1 sample in spite of a huge baseline gap. Restricting the sample using our knowledge of program admissions criteria yields even better regression estimates with CPS-3, about as good as Dehejia and Wahbaís (1999) propensity score matching results with two lags of earnings. Systematic pre-screening to enforce common support seems like a useful adjunct to regression


{81}------------------------------------------------

estimation with CPS-1, a large and coarsely-selected initial sample. The estimates in screened CPS-1 are as good as unscreened CPS-3. We note, however, that the standard errors for estimates using propensityscore-screened samples have not been adjusted to reáect sampling variance in our estimates of the score. An advantage of pre-screening using prior information, as in the step from CPS-1 to CPS-3, is that no such adjustment is necessary.