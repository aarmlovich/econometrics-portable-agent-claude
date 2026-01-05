# Models with Contemporaneous Correlation between Some Explanatory Variables and the Idiosyncratic Error

> Pages: 318-325

Consider again model (11.18), where zit is strictly exogenous in the sense that

$$E(\mathbf{z}_{is}^{\prime}u_{it}) = \mathbf{0}, \quad \text{all } s, t$$
 (11.23)

{319}------------------------------------------------

but where we allow wit to be contemporaneously correlated with uit. This correlation can be due to any of the three problems that we studied earlier: omission of an important time-varying explanatory variable, measurement error in some elements of wit, or simultaneity between yit and one or more elements of wit. We assume that equation (11.18) is the equation of interest. In a simultaneous equations model with panel data, equation (11.18) represents a single equation. A system approach is also possible. See, for example, Baltagi (1981); Cornwell, Schmidt, and Wyhowski (1992); and Kinal and Lahiri (1993).

Example 11.5 (Effects of Smoking on Earnings): A panel data model to examine the effects of cigarette smoking on earnings is

$$\log(wage_{it}) = \mathbf{z}_{it}\mathbf{y} + \delta_1 cigs_{it} + c_i + u_{it}$$
(11.24)

(For an empirical analysis, see Levine, Gustafson, and Velenchik, 1997.) As always, we would like to know the causal effect of smoking on hourly wage. For concreteness, assume cigsit is measured as average packs per day. This equation has a causal interpretation: holding fixed the factors in zit and ci, what is the effect of an exogenous change in cigarette smoking on wages? Thus equation (11.24) is a structural equation.

The presence of the individual heterogeneity, ci, in equation (11.24) recognizes that cigarette smoking might be correlated with individual characteristics that also affect wage. An additional problem is that cigsit might also be correlated with uit, something we have not allowed so far. In this example the correlation could be from a variety of sources, but simultaneity is one possibility: if cigarettes are a normal good, then, as income increases—holding everything else fixed—cigarette consumption increases. Therefore, we might add another equation to equation (11.24) that reflects that cigsit may depend on income, which clearly depends on wage. If equation (11.24) is of interest, we do not need to add equations explicitly, but we must find some instrumental variables.

To get an estimable model, we must first deal with the presence of ci, since it might be correlated with zit as well as cigsit. In the general model (11.18), either the FE or FD transformations can be used to eliminate ci before addressing the correlation between wit and uit. If we first difference, as in equation (11.19), we can use the entire vector z<sup>i</sup> as valid instruments in equation (11.19) because zit is strictly exogenous. Neither wit nor w<sup>i</sup>;t<sup>1</sup> is valid as instruments at time t, but it could be that w<sup>i</sup>;t<sup>2</sup> is valid, provided we assume that uit is uncorrelated with wis for s < t. This assumption means that wit has only a contemporaneous effect on yit, something that is likely to be false in example 11.5. [If smoking affects wages, the effects are likely to be deter

{320}------------------------------------------------

mined by prior smoking behavior as well as current smoking behavior. If we include a measure of past smoking behavior in equation (11.24), then this must act as its own instrument in a differenced equation, and so using cigsis for s < t as IVs becomes untenable.]

Another thought is to use lagged values of yit as instruments, but this approach effectively rules out serial correlation in uit. In the wage equation (11.24), it would mean that lagged wage does not predict current wage, once ci and the other variables are controlled for. If this assumption is false, using lags of yit is not a valid way of identifying the parameters.

If z<sup>i</sup> is the only valid set of instruments for equation (11.18), the analysis probably will not be convincing: it relies on Dwit being correlated with some linear combination of z<sup>i</sup> other than Dzit. Such partial correlation is likely to be small, resulting in poor IV estimators; see Problem 11.2.

Perhaps the most convincing possibility for obtaining additional instruments is to follow the standard SEM approach from Chapter 9: use exclusion restrictions in the structural equations. For example, we can hope to find exogenous variables that do not appear in equation (11.24) but that do affect cigarette smoking. The local price of cigarettes (or level of cigarette taxes) is one possibility. Such variables can usually be considered strictly exogenous, unless we think people change their residence based on the price of cigarettes.

If we difference equation (11.24) we get

$$\Delta \log(wage_{it}) = \Delta \mathbf{z}_{it} \mathbf{\gamma} + \delta_1 \Delta cigs_{it} + \Delta u_{it}$$
(11.25)

Now, for each t, we can study identification of this equation just as in the cross sectional case: we must first make sure the order condition holds, and then argue (or test) that the rank condition holds. Equation (11.25) can be estimated using a pooled 2SLS analysis, where corrections to standard errors and test statistics for heteroskedasticity or serial correlation might be warranted. With a large cross section, a GMM system procedure that exploits general heteroskedasticity and serial correlation in Duit can be used instead.

Example 11.6 (Effects of Prison Population on Crime Rates): In order to estimate the causal effect of prison population increases on crime rates at the state level, Levitt (1996) uses instances of prison overcrowding litigation as instruments for the growth in prison population. The equation Levitt estimates is in first differences. We can write an underlying unobserved effects model as

$$\log(crime_{it}) = \theta_t + \beta_1 \log(prison_{it}) + \mathbf{x}_{it}\gamma + c_i + u_{it}$$
(11.26)


{321}------------------------------------------------

where y<sup>t</sup> denotes different time intercepts and crime and prison are measured per 100,000 people. (The prison population variable is measured on the last day of the previous year.) The vector xit contains other controls listed in Levitt, including measures of police per capita, income per capita, unemployment rate, and race, metropolitan, and age distribution proportions.

Differencing equation (11.26) gives the equation estimated by Levitt:

$$\Delta \log(crime_{it}) = \xi_t + \beta_1 \Delta \log(prison_{it}) + \Delta \mathbf{x}_{it} \mathbf{y} + \Delta u_{it}$$
(11.27)

Simultaneity between crime rates and prison population, or, more precisely, in the growth rates, makes OLS estimation of equation (11.27) generally inconsistent. Using the violent crime rate and a subset of the data from Levitt (in PRISON.RAW, for the years 1980 to 1993, for 51 14 ¼ 714 total observations), the OLS estimate of b<sup>1</sup> is :181 (se ¼ :048). We also estimate the equation by 2SLS, where the instruments for Dlogð prisonÞ are two binary variables, one for whether a final decision was reached on overcrowding litigation in the current year and one for whether a final decision was reached in the previous two years. The 2SLS estimate of b<sup>1</sup> is 1:032 (se ¼ :370). Therefore, the 2SLS estimated effect is much larger; not surprisingly, it is much less precise, too. Levitt (1996) found similar results when using a longer time period and more instruments.

A different approach to estimating SEMs with panel data is to use the fixed effects transformation and then to apply an IV technique such as pooled 2SLS. A simple procedure is to estimate the time-demeaned equation (10.46) by pooled 2SLS, where the instruments are also time demeaned. This is equivalent to using 2SLS in the dummy variable formulation, where the unit-specific dummy variables act as their own instruments. See Problem 11.9 for a careful analysis of this approach. Foster and Rosenzweig (1995) use the within transformation along with IV to estimate householdlevel profit functions for adoption of high-yielding seed varieties in rural India. Ayres and Levitt (1998) apply 2SLS to a time-demeaned equation to estimate the effect of Lojack electronic theft prevention devices on city car-theft rates.

The FE transformation precludes the use of lagged values of wit among the instruments, for essentially the same reasons discussed for models with sequentially exogenous explanatory variables: uit will be correlated with the time-demeaned instruments. Therefore, if we make assumptions on the dynamics in the model that ensure that uit is uncorrelated with wis, s < t, differencing is preferred in order to use the extra instruments.

Differencing or time demeaning followed by some sort of IV procedure is useful when uit contains an important, time-varying omitted variable that is correlated with 

{322}------------------------------------------------

 $u_{it}$ . The same considerations for choosing instruments in the simultaneity context are relevant in the omitted variables case as well. In some cases,  $\mathbf{w}_{is}$ , s < t - 1, can be used as instruments at time t in a first-differenced equation (11.18); in other cases, we might not want identification to hinge on using lagged exploratory variables as IVs. For example, suppose that we wish to study the effects of per student spending on test scores, using three years of data, say 1980, 1985, and 1990. A structural model at the school level is

$$avgscore_{it} = \theta_t + \mathbf{z}_{it}\gamma + \delta_1 spending_{it} + c_i + u_{it}$$
(11.28)

where  $\mathbf{z}_{it}$  contains other school and student characteristics. In addition to worrying about the school fixed effect  $c_i$ ,  $u_{it}$  contains average family income for school i at time t (unless we are able to collect data on income); average family income is likely to be correlated with *spending<sub>it</sub>*. After differencing away  $c_i$ , we need an instrument for  $\Delta$ spending<sub>it</sub>. One possibility is to use exogenous changes in property taxes that arose because of an unexpected change in the tax laws. [Such changes occurred in California in 1978 (Proposition 13) and in Michigan in 1994 (Proposal A).] Using lagged spending changes as IVs is probably not a good idea, as spending might affect test scores with a lag.

The third form of endogeneity, measurement error, can also be solved by eliminating  $c_i$  and finding appropriate IVs. Measurement error in panel data was studied by Solon (1985) and Griliches and Hausman (1986). It is widely believed in econometrics that the differencing and FE transformations exacerbate measurement error bias (even though they eliminate heterogeneity bias). However, it is important to know that this conclusion rests on the classical errors-in-variables model under strict exogeneity, as well as on other assumptions.

To illustrate, consider a model with a single explanatory variable,

$$y_{it} = \beta x_{it}^* + c_i + u_{it} \tag{11.29}$$

under the strict exogeneity assumption

$$E(u_{it} | \mathbf{x}_i^*, \mathbf{x}_i, c_i) = 0, \qquad t = 1, 2, \dots, T$$
 (11.30)

where  $x_{it}$  denotes the observed measure of the unobservable  $x_{it}^*$ . Condition (11.30) embodies the standard redundancy condition—that  $x_{it}$  does not matter once  $x_{it}^*$  is controlled for—in addition to strict exogeneity of the unmeasured and measured regressors. Denote the measurement error as  $r_{it} = x_{it} - x_{it}^*$ . Assuming that  $r_{it}$  is uncorrelated with  $x_{it}^*$ —the key CEV assumption—and that variances and covariances are all constant across t, it is easily shown that, as  $N \to \infty$ , the plim of the pooled OLS estimator is

{323}------------------------------------------------

$$\lim_{N \to \infty} \hat{\beta}_{POLS} = \beta + \frac{\text{Cov}(x_{it}, c_i + u_{it} - \beta r_{it})}{\text{Var}(x_{it})}$$

$$= \beta + \frac{\text{Cov}(x_{it}, c_i) - \beta \sigma_r^2}{\text{Var}(x_{it})} \tag{11.31}$$

where  $\sigma_r^2 = \text{Var}(r_{it}) = \text{Cov}(x_{it}, r_{it})$ ; this is essentially the formula derived by Solon (1985).

From equation (11.31), we see that there are two sources of asymptotic bias in the POLS estimator: correlation between  $x_{it}$  and the unobserved effect,  $c_i$ , and a measurement error bias term,  $-\beta \sigma_r^2$ . If  $x_{it}$  and  $c_i$  are positively correlated and  $\beta > 0$ , the two sources of bias tend to cancel each other out.

Now assume that  $r_{is}$  is uncorrelated with  $x_{it}^*$  for all t and s, and for simplicity suppose that T = 2. If we first difference to remove  $c_i$  before performing OLS we obtain

$$\begin{aligned}
& \underset{N \to \infty}{\text{plim}} \hat{\beta}_{FD} = \beta + \frac{\text{Cov}(\Delta x_{it}, \Delta u_{it} - \beta \Delta r_{it})}{\text{Var}(\Delta x_{it})} = \beta - \beta \frac{\text{Cov}(\Delta x_{it}, \Delta r_{it})}{\text{Var}(\Delta x_{it})} \\
&= \beta - 2\beta \frac{[\sigma_r^2 - \text{Cov}(r_{it}, r_{i,t-1})]}{\text{Var}(\Delta x_{it})} \\
&= \beta \left(1 - \frac{\sigma_r^2 (1 - \rho_r)}{\sigma_{x^*}^2 (1 - \rho_{x^*}) + \sigma_r^2 (1 - \rho_r)}\right)
\end{aligned} \tag{11.32}$$

where  $\rho_{x^*} = \operatorname{Corr}(x_{it}^*, x_{i,t-1}^*)$  and  $\rho_r = \operatorname{Corr}(r_{it}, r_{i,t-1})$ , where we have used the fact that  $\operatorname{Cov}(r_{it}, r_{i,t-1}) = \sigma_r^2 \rho_r$  and  $\operatorname{Var}(\Delta x_{it}) = 2[\sigma_{x^*}^2(1 - \rho_{x^*}) + \sigma_r^2(1 - \rho_r)]$ ; see also Solon (1985) and Hsiao (1986, p. 64). Equation (11.32) shows that, in addition to the ratio  $\sigma_r^2/\sigma_{x^*}^2$  being important in determining the size of the measurement error bias, the ratio  $(1 - \rho_r)/(1 - \rho_{x^*})$  is also important. As the autocorrelation in  $x_{it}^*$  increases relative to that in  $r_{it}$ , the measurement error bias in  $\hat{\beta}_{FD}$  increases. In fact, as  $\rho_{x^*} \to 1$ , the measurement error bias approaches  $-\beta$ .

Of course, we can never know whether the bias in equation (11.31) is larger than that in equation (11.32), or vice versa. Also, both expressions are based on the CEV assumptions, and then some. If there is little correlation between  $\Delta x_{it}$  and  $\Delta r_{it}$ , the measurement error bias from first differencing may be small, but the small correlation is offset by the fact that differencing can considerably reduce the variation in the explanatory variables.

Consistent estimation in the presence of measurement error is possible under certain assumptions. Consider the more general model

$$y_{it} = \mathbf{z}_{it}\gamma + \delta w_{it}^* + c_i + u_{it}, \qquad t = 1, 2, \dots, T$$
 (11.33)

{324}------------------------------------------------

where  $w_{it}^*$  is measured with error. Write  $r_{it} = w_{it} - w_{it}^*$ , and assume strict exogeneity along with redundancy of  $w_{it}$ :

$$E(u_{it} | \mathbf{z}_i, \mathbf{w}_i^*, \mathbf{w}_i, c_i) = 0, \qquad t = 1, 2, \dots, T$$
 (11.34)

Replacing  $w_{it}^*$  with  $w_{it}$  and first differencing gives

$$\Delta y_{it} = \Delta \mathbf{z}_{it} \gamma + \delta \Delta w_{it} + \Delta u_{it} - \delta \Delta r_{it} \tag{11.35}$$

The standard CEV assumption in the current context can be stated as

$$E(r_{it} | \mathbf{z}_i, \mathbf{w}_i^*, c_i) = 0, \qquad t = 1, 2, \dots, T$$
 (11.36)

which implies that  $r_{it}$  is uncorrelated with  $\mathbf{z}_{is}$ ,  $w_{is}^*$  for all t and s. (As always in the context of linear models, assuming zero correlation is sufficient for consistency, but not for usual standard errors and test statistics to be valid.) Under assumption (11.36) (and other measurement error assumptions),  $\Delta r_{it}$  is correlated with  $\Delta w_{it}$ . To apply an IV method to equation (11.35), we need at least one instrument for  $\Delta w_{it}$ . As in the omitted variables and simultaneity contexts, we may have additional variables outside the model that can be used as instruments. Analogous to the cross section case (as in Chapter 5), one possibility is to use another measure on  $w_{it}^*$ , say  $h_{it}$ . If the measurement error in  $h_{it}$  is orthogonal to the measurement error in  $w_{is}$ , all t and s, then  $\Delta h_{it}$  is a natural instrument for  $\Delta w_{it}$  in equation (11.35). Of course, we can use many more instruments in equation (11.35), as any linear combination of  $\mathbf{z}_i$  and  $\mathbf{h}_i$  is uncorrelated with the composite error under the given assumptions.

Alternatively, a vector of variables  $\mathbf{h}_{it}$  may exist that are known to be redundant in equation (11.33), strictly exogenous, and uncorrelated with  $r_{is}$  for all s. If  $\Delta \mathbf{h}_{it}$  is correlated with  $\Delta w_{it}$ , then an IV procedure, such as pooled 2SLS, is easy to apply. It may be that in applying something like pooled 2SLS to equation (11.35) results in asymptotically valid statistics; this imposes serial independence and homoskedasticity assumptions on  $\Delta u_{it}$ . Generally, however, it is a good idea to use standard errors and test statistics robust to arbitrary serial correlation and heteroskedasticity, or to use a full GMM approach that efficiently accounts for these. An alternative is to use the FE transformation, as explained in Problem 11.9. Ziliak, Wilson, and Stone (1999) find that, for a model explaining cyclicality of real wages, the FD and FE estimates are different in important ways. The differences largely disappear when IV methods are used to account for measurement error in the local unemployment rate.

So far, the solutions to measurement error in the context of panel data have assumed nothing about the serial correlation in  $r_{it}$ . Suppose that, in addition to assumption (11.34), we assume that the measurement error is serially uncorrelated:

$$E(r_{it}r_{is}) = 0, \qquad s \neq t \tag{11.37}$$

{325}------------------------------------------------

Assumption (11.37) opens up a solution to the measurement error problem with panel data that is not available with a single cross section or independently pooled cross sections. Under assumption (11.36), rit is uncorrelated with w is for all t and s. Thus, if we assume that the measurement error rit is serially uncorrelated, then rit is uncorrelated with wis for all t 0s. Since, by the strict exogeneity assumption, Duit is uncorrelated with all leads and lags of zit and wit, we have instruments readily available. For example, wi;t<sup>2</sup> and wi;t<sup>3</sup> are valid as instruments for Dwit in equation (11.35); so is wi;tþ1. Again, pooled 2SLS or some other IV procedure can be used once the list of instruments is specified for each time period. However, it is important to remember that this approach requires the rit to be serially uncorrelated, in addition to the other CEV assumptions.

The methods just covered for solving measurement error problems all assume strict exogeneity of all explanatory variables. Naturally, things get harder when measurement error is combined with models with only sequentially exogenous explanatory variables. Nevertheless, differencing away the unobserved effect and then selecting instruments—based on the maintained assumptions—generally works in models with a variety of problems.