# Regression DD

> Pages: 189-197

As with the fixed effects model, we can use regression to estimate equations like (5.2.2). Let  $NJ_s$  be a dummy for restaurants in New Jersey and  $d_t$  be a time-dummy that switches on for observations obtained

{190}------------------------------------------------

in November (i.e., after the minimum wage change). Then

<span id="page-190-0"></span>
$$Y_{ist} = \alpha + \gamma N J_s + \lambda d_t + \beta (N J_s \cdot d_t) + \varepsilon_{ist}$$
(5.2.3)

is the same as [\(5.2.2\)](#page-185-1) where NJ<sup>s</sup> dt=dst. In the language of Section [3.1.4,](#page-51-0) this model includes two main e§ects for state and year and an interaction term that marks observations from New Jersey in November. This is a saturated model since the conditional mean function E(yistjs; t) takes on four possible values and there are four parameters. The link between the parameters in the regression equation, [\(5.2.3\)](#page-190-0), and those in the DD model for the conditional mean function, [\(5.2.2\)](#page-185-1), is

$$\alpha = E(Y_{ist}|s = PA, t = Feb) = \gamma_{PA} + \lambda_{Feb}$$

$$\gamma = E(Y_{ist}|s = NJ, t = Feb) - E(Y_{ist}|s = PA, t = Feb) = \gamma_{NJ} - \gamma_{PA}$$

$$\lambda = E(Y_{ist}|s = PA, t = Nov) - E(Y_{ist}|s = PA, t = Feb) = \lambda_{Nov} - \lambda_{Feb}$$

$$\beta = \{E(Y_{ist}|s = NJ, t = Nov) - E(Y_{ist}|s = NJ, t = Feb)\}$$

$$-\{E(Y_{ist}|s = PA, t = Nov) - E(Y_{ist}|s = PA, t = Feb)\}.$$

The regression formulation of the di§erence-in-di§erence model o§ers a convenient way to construct DD estimates and standard errors. Itís also easy to add additional states or periods to the regression set-up. We might for example, add additional control states and pre-treatment periods to the New Jersey/Pennsylvania sample. The resulting generalization of [\(5.2.3\)](#page-190-0) includes a dummy for each state and period but is otherwise unchanged.

A second advantage of regression-DD is that it facilitates empirical work with regressors other than switched-on/switched-o§ dummy variables. Instead of New Jersey and Pennsylvania in 1992, for example, we might look at all state minimum wages in the United States. Some of these are a little higher than the federal minimum (which covers everyone regardless of where they live), some are a lot higher, and some are the same. The minimum wage is therefore a variable with di§ering "treatment intensity" across states and over time. Moreover, in addition to statutory variation in state minima, the local importance of a minimum wage varies with average state wage levels. For example, the early-1990s Federal minimum of \$4.25 was probably irrelevant in Connecticut - with high average wages - but a big deal in Mississippi.

Card (1992) exploits regional variation in the impact of the federal minimum wage. His approach is motivated by an equation like

<span id="page-190-1"></span>
$$Y_{ist} = \gamma_s + \lambda_t + \beta(FA_s \cdot d_t) + \varepsilon_{ist}$$
(5.2.4)

where the variable fa<sup>s</sup> is a measure of the fraction of teenagers likely to be a§ected by a minimum wage increase in each state and d<sup>t</sup> is a dummy for observations after 1990, when the federal minimum increased from \$3.35 to \$3.80. The fa<sup>s</sup> variable measures the baseline (pre-increase) proportion of each stateís teen 

{191}------------------------------------------------

labor force earning less than \$3.80.

As in the New Jersey/Pennsylvania study, Card (1992) works with data from two periods, before and after, in this case 1989 and 1992. But this study uses 51 states (including the District of Columbia), for a total of 102 state-year observations. Since there are no individual-level covariates in [\(5.2.4\)](#page-190-1), this is the same as estimation with micro data (provided the group-level estimates are weighted by cell size). Note that fa<sup>s</sup> d<sup>t</sup> is an interaction term, like NJ<sup>s</sup> d<sup>t</sup> in [\(5.2.3\)](#page-190-0), though here the interaction term takes on a distinct value for each observation in the data set. Finally, because Card (1992) analyzes data for only two periods, the reported estimates are from an equation in Örst-di§erences:

$$\Delta \bar{\mathbf{Y}}_s = \lambda^* + \beta \mathbf{F} \mathbf{A}_s + \Delta \bar{\varepsilon}_s,$$

where yØ<sup>s</sup> is the change in average teen employment in state s and "<sup>s</sup> is the error term in the di§erenced equation.[8](#page-191-0)

Table [5.2.2,](#page-191-1) based on Table 3 in Card (1992), shows that wages increased more in states where the minimum wage increase is likely to have had more bite (see the estimate of .15 in column 1). This is an important step in Cardís analysis - it veriÖes the notion that the fraction a§ected variable is a good predictor of the wage changes induced by an increase in the federal minimum. Employment, on the other hand, seems largely unrelated to fraction a§ected, as can be seen in column 3. Thus, the results in Card (1992) are in line with the results from the New Jersey/Pennsylvania study.

<span id="page-191-1"></span>Table 5.2.2: Regression-DD estimates of minimum wage e§ects on teens, 1989 to 1992

<table><tbody><tr><th></th><th></th><th colspan="2">Equations for Change</th><th colspan="3">Equations for change in Teen</th></tr><tr><td></td><td></td><td colspan="2">in Mean Log Wage:</td><td colspan="3">Employment-Population Ratio:</td></tr><tr><td></td><td>Explanatory Variable</td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td></tr><tr><td>1.</td><td>Fraction of</td><td>0.15</td><td>.14</td><td>0.02</td><td>01</td></tr><tr><td></td><td>A§ected Teens</td><td>(0.03)</td><td>(0.04)</td><td>(0.03)</td><td>(0.03)</td></tr><tr><td>2.</td><td>Change in Overall</td><td>ñ</td><td>0.46</td><td>ñ</td><td>1.24</td></tr><tr><td></td><td>Emp./Pop. Ratio</td><td></td><td>(0.60)</td><td></td><td>(0.60)</td></tr><tr><td>3.</td><td>R-squared</td><td>0.30</td><td>0.31</td><td>0.01</td><td>0.09</td></tr></tbody></table>

Notes: Adapted from Card (1992). The table reports estimates from a regression of the change in average teen employment by state on the fraction of teens a§ected by a change in the federal minimum wage in each state. Data are from the 1989 and 1992 CPS. Regressions are weighted by the CPS sample size by state and year.

Cardís (1992) analysis illustrates a further advantage of regression-DD: itís easy to add additional covariates in this framework. For example, we might like to control for adult employment as a source of omitted

<span id="page-191-0"></span><sup>8</sup> Card weights estimates of [\(5.2.4\)](#page-190-1) by the sample size used to construct averages for each state. Other speciÖcations in the spirit of [\(5.2.4\)](#page-190-1) put a normalized function of state and federal minimum wages on the right hand side instead of fa<sup>s</sup> dt. See, for example, Neumark and Wascher (1992), who work with the di§erence between state and federal minima, adjusted for minimum-wage coverage provisions, and normalized by state average hourly wages.

{192}------------------------------------------------

state-speciÖc trends. In other words, we can model counterfactual employment in the absence of a change in the minimum wage as

$$E[Y_{0ist}|s, t, X_{st}] = \gamma_s + \lambda_t + X'_{st}\delta.$$

where Xst is a vector of state-and-time-varying covariates, including adult employment (though this may not be kosher if adult employment also responds to the minimum wage change, in which case itís bad control; see Section [3.2.3\)](#page-62-0). As it turns out, the addition of an adult employment control has little e§ect on Cardís estimates, as can be seen in columns 2 and 4 in Table [5.2.2.](#page-191-1)

Itís worth emphasizing the fact that Card (1992) analyzes state averages instead of individual data. He might have used a pooled multi-year sample of micro data from the CPS to estimate an equation like

$$Y_{ist} = \gamma_s + \lambda_t + \beta(FA_s \cdot d_t) + X'_{ist}\delta + \varepsilon_{ist}, \qquad (5.2.5)$$

where Xist can include individual level characteristics such as race. The covariate vector might also include time-varying variables measured at the state level. Only the latter are likely to be a source of omitted variables bias, but individual-level controls can increase precision, a point we noted in Section [2.3.](#page-31-0) Inference is a little more complicated in a framework that combines of micro data on dependent variables with grouplevel regressors, however. The key issue is how best to adjust for possible group-level random e§ects, as we discuss in Chapter [8,](#page-236-0) below.

When the sample includes many years, the regression-DD model lends itself to a test for causality in the spirit of Granger (1969). The Granger idea is to see whether causes happen before consequences and not vice versa (though as we know from the epigram at the beginning of Chapter [4,](#page-98-0) this alone is not su¢ cient for causal inference). Suppose the policy variable of interest, dst, changes at di§erent times in di§erent states. In this context, Granger causality testing means a check on whether, conditional on state and year e§ects, past dst predicts yist while future dst does not. If dst causes yist but not vice versa, then leads should not matter in an equation like:

<span id="page-192-0"></span>
$$Y_{ist} = \gamma_s + \lambda_t + \sum_{\tau=0}^m \beta_{-\tau} D_{s,t-\tau} + \sum_{\tau=1}^q \beta_{+\tau} D_{s,t+\tau} X_{ist} \delta + \varepsilon_{ist}, \qquad (5.2.6)$$

where the sums on the right-hand side allow for m lags (<sup>1</sup> ; <sup>2</sup> ; :::; <sup>m</sup>) or post-treatment e§ects and q leads (+1; +1; :::; +<sup>q</sup> ) or anticipatory e§ects. The pattern of lagged e§ects is usually of substantive interest as well. We might, for example, believe that causal e§ects should grow or fade as time passes.

Autor (2003) implements the Granger test in an investigation of the e§ect of employment protection on Örmsí use of temporary help. Employment protection is a type of labor law - promulgated by state legislatures or, more typically, through common law as made by state courts - that makes it harder to Öre workers. As a rule, U.S. labor law allows "employment at will," which means that workers can be Öred for 

{193}------------------------------------------------

just cause or no cause, at the employerís whim. But some state courts have allowed a number of exceptions to the employment-at-will doctrine, leading to lawsuits for "unjust dismissal". Autor is interested in whether fear of employee lawsuits makes Örms more likely to use temporary workers for tasks for which they would otherwise have increased their workforce. Temporary workers work for someone else besides the Örm for which they are executing tasks. As a result, the Örm using them cannot be sued for unjust dismissal when they let temporary workers go.

Autorís empirical strategy relates the employment of temporary workers in a state to dummy variables indicating state court rulings that allow exceptions to the employment-at-will doctrine. His regression-DD model includes both leads and lags, as in equation [\(5.2.6\)](#page-192-0). The estimated leads and lags, running from two years ahead to 4 years behind, are plotted in Figure [5.2.4,](#page-194-0) a reproduction of Figure 3 from Autor (2003). The estimates show no e§ects in the two years before the courts adopted an exception, with sharply increasing e§ects on temporary employment in the Örst few years after the adoption, which then appear to áatten out with a permanently higher rate of temporary employment in a§ected states. This pattern seems consistent with a causal interpretation of Autorís results.

An alternative check on the DD identiÖcation strategy adds state-speciÖc time trends to the regressors in Xist. In other words, we estimate

$$Y_{ist} = \gamma_{0s} + \gamma_{1st} + \lambda_t + \beta D_{st} + X'_{ist} \delta + \varepsilon_{ist}, \qquad (5.2.7)$$

where <sup>0</sup><sup>s</sup> is a state-speciÖc intercept as before and <sup>1</sup><sup>s</sup> is a state-speciÖc trend coe¢ cient multiplying the time-trend variable, t. This allows treatment and control states to follow di§erent trends in a limited but potentially revealing way. Itís heartening to Önd that the estimated e§ects of interest are unchanged by the inclusion of these trends, and discouraging otherwise. Note, however, that we need at least 3 periods to estimate a model with state-speciÖc trends. Moreover, in practice, 3 periods is typically inadequate to pin down both the trends and the treatment e§ect. As a rule, DD estimation with state-speciÖc trends is likely to be more robust and convincing when the pre-treatment data establish a clear trend that can be extrapolated into the post-treatment period.

In a study of the e§ect of labor regulation on businesses in Indian states, Besley and Burgess (2004)use state trends as a robustness check. Di§erent states change regulatory regimes at di§erent times, giving rise to a DD research design. As in Card (1992), the unit of observation in Besley and Burgess (2004) is a state-year average. Table [5.2.3](#page-195-0) (based on Table IV in their paper) reproduces the key results.

The estimates in column 1, from a regression-DD model without state-speciÖc trends, suggest that labor regulation leads to lower output per capita. The models used to construct the estimates in columns 2 and 3 add time-varying state-speciÖc covariates like government expenditure per capita and state population. This is in the spirit of Cardís (1992) addition of state-level adult employment rates as a control in the minimum

{194}------------------------------------------------

and after adoption.

![](_page_194_Figure_2.jpeg)

<span id="page-194-0"></span>Figure 5.2.4: Estimated impact of state courtsíadoption of an implied-contract exception to the employmentat-will doctrine on use of temporary workers (from Autor 2003). The dependent variable is the log of state temporary help employment in 1979 - 1995. Estimates are from a model that allows for e§ects before, during,

{195}------------------------------------------------

<span id="page-195-0"></span>Table 5.2.3: E§ect of labor regulation on the performance of Örms in Indian states

<table><tbody><tr><th></th><th>(1)</th><th>(2)</th><th>(3)</th><th>(4)</th></tr><tr><td>Labor regulation (lagged)</td><td>-0.186</td><td>-0.185</td><td>-0.104</td><td>0.0002</td></tr><tr><td></td><td>(.0641)</td><td>(.0507)</td><td>(.039)</td><td>(.02)</td></tr><tr><td>Log development</td><td></td><td>0.240</td><td>0.184</td><td>0.241</td></tr><tr><td>expenditure per capita</td><td></td><td>(.1277)</td><td>(.1187)</td><td>(.1057)</td></tr><tr><td>Log installed electricity</td><td></td><td>0.089</td><td>0.082</td><td>0.023</td></tr><tr><td>capacity per capita</td><td></td><td>(.0605)</td><td>(.0543)</td><td>(.0333)</td></tr><tr><td>Log state population</td><td></td><td>0.720</td><td>0.310</td><td>-1.419</td></tr><tr><td></td><td></td><td>(.96)</td><td>(1.1923)</td><td>(2.3262)</td></tr><tr><td>Congress majority</td><td></td><td></td><td>-0.0009</td><td>0.020</td></tr><tr><td></td><td></td><td></td><td>(.01)</td><td>(.0096)</td></tr><tr><td>Hard left majority</td><td></td><td></td><td>-0.050</td><td>-0.007</td></tr><tr><td></td><td></td><td></td><td>(.0168)</td><td>(.0091)</td></tr><tr><td>Janata majority</td><td></td><td></td><td>0.008</td><td>-0.020</td></tr><tr><td></td><td></td><td></td><td>(.0235)</td><td>(.0333)</td></tr><tr><td>Regional majority</td><td></td><td></td><td>0.006</td><td>0.026</td></tr><tr><td></td><td></td><td></td><td>(.0086)</td><td>(.0234)</td></tr><tr><td>State-speciÖc trends</td><td>NO</td><td>NO</td><td>NO</td><td>YES</td></tr><tr><td>Adjusted R-squared</td><td>0.93</td><td>0.93</td><td>0.94</td><td>0.95</td></tr></tbody></table>

Notes: Adapted from Besley and Burgess (2004), Table IV. The table reports regression-DD estimates of the e§ects of labor regulation on productivity. The dependent variable is log manufacturing output per capita. All models include state and year e§ects. Robust standard errors clustered at the state level are reported in parentheses. State amendments to the Industrial Disputes Act are coded 1=pro-worker, 0 = neutral, -1 = pro-employer and then cumulated over the period to generate the labor regulation measure. Log of installed electrical capacity is measured in kilowatts, and log development expenditure is real per capita state spending on social and economic services. Congress, hard left, Janata, and regional majority are counts of the number of years for which these political groupings held a majority of the seats in the state legislatures. The data are for the sixteen main states for the period 1958-1992. There are 552 observations.

wage study. The addition of controls a§ects the Besley and Burgess estimates little. But the addition of state-speciÖc trends kills the labor-regulation e§ect, as can be seen in column 4. Apparently, labor regulation in India increases in states where output is declining anyway. Control for this trend therefore drives the estimated regulation e§ect to zero.

#### Picking Controls

Weíve labeled the two dimensions in the DD set-up ìstatesî and ìtimeî because this is the archetypical DD example in applied econometrics. But the DD idea is much more general. Instead of states, the subscript s might denote demographic groups, some of which are a§ected by a policy and others are not. For example, Kugler, Jimeno, and Hernanz (2005) look at the e§ects of age-speciÖc employment protection

{196}------------------------------------------------

policies in Spain. Likewise, instead of time, we might group data by cohort or other types of characteristics. An example is Angrist and Evans (1999), who study the e§ect of changes in state abortion laws on teen pregnancy using variation by state and year of birth. Implicitly, however, DD designs always set up an implicit treatment-control comparison. The question of whether this comparison is a good one deserves careful consideration.

One potential pitfall in this context arises when the composition of the implicit treatment and control groups changes as a result of treatment. Going back to a design based on state/time comparisons, suppose weíre interested in the e§ects of the generosity of public assistance on labor supply. Historically, U.S. states have o§ered widely-varying welfare payments to poor unmarried mothers. Labor economists have long been interested in the e§ects of such income maintenance policies - how much of an increase in living standards they facilitate, and whether they make work less attractive (see, e.g., Meyer and Rosenbaum, 2001, for a recent study). A concern here, emphasized in a review of research on welfare by Mo¢ tt (1992), is that poor people who would in any case have weak labor force attachment might move to states with more generous welfare beneÖts. In a DD research design, this sort of program-induced migration tends to make generous welfare programs look worse for labor supply than they really are.

Migration problems can usually be Öxed if we know where an individual starts out. Say we know state of residence in the period before treatment, or state of birth. State of birth or previous state of residence are unchanged by the treatment but still highly correlated with current state of residence. The problem of migration is therefore eliminated in comparisons using these dimensions instead of state of residence. This introduces a new problem, however, which is that individuals who do move are incorrectly located. In practice, however, this problem is easily addressed with the IV methods discussed in chapter [4](#page-98-0) (state of birth or previous residence is used to construct instruments for current location).

A modiÖcation of the two-by-two DD set-up uses higher-order contrasts to draw causal inferences. An example is the extension of Medicaid coverage in the U.S. studied by Yelowitz (1995). Eligibility for Medicaid, the massive U.S. health insurance program for the poor, was once tied to eligibility for AFDC, a large cash welfare program. At various times in the 1980s, however, some states extended Medicaid coverage to children in families ineligible for AFDC. Yelowitz was interested in how this expansion a§ected, among other things, mothersílabor force participation and earnings.

In addition to state and time, childrenís age provides a third dimension in which Medicaid policy varies. Yelowitz exploits this variation by estimating

$$Y_{iast} = \gamma_{st} + \lambda_{at} + \theta_{as} + \beta D_{ast} + X_{iast} \delta + \varepsilon_{iast},$$

where s index states, t indexes time, and a is the age of the youngest child in a family. This model provides full non-parametric control for state-speciÖc time e§ects that are common across age groups ( st), time-varying 

{197}------------------------------------------------

age e§ects (at), and state-speciÖc age e§ects (as). The regressor of interest, dast, indicates children in a§ected age groups in states and periods where coverage is provided. This triple-di§erences model may generate a more convincing set of results than a traditional DD analysis that exploits di§erences by state and time alone.