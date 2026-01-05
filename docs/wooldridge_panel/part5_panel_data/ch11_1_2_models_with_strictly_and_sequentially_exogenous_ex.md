# Models with Strictly and Sequentially Exogenous Explanatory Variables

> Pages: 316-318

Estimating models with both strictly exogenous and sequentially exogenous variables is not difficult. For t = 1, 2, ..., T, suppose that

$$y_{it} = \mathbf{z}_{it} \boldsymbol{\gamma} + \mathbf{w}_{it} \boldsymbol{\delta} + c_i + u_{it}$$
 (11.18)

Assume that  $\mathbf{z}_{is}$  is uncorrelated with  $u_{it}$  for all s and t, but that  $u_{it}$  is uncorrelated with

{317}------------------------------------------------

wis only for sat; sufficient is Eðuit j zi; wit; w<sup>i</sup>;t<sup>1</sup>; ... ; w<sup>i</sup>1Þ ¼ 0. This model covers many cases of interest, including when wit contains a lagged dependent variable.

After first differencing we have

$$\Delta y_{it} = \Delta \mathbf{z}_{it} \boldsymbol{\gamma} + \Delta \mathbf{w}_{it} \boldsymbol{\delta} + \Delta u_{it} \tag{11.19}$$

and the instruments available at time t are ðzi; w<sup>i</sup>;t<sup>1</sup>; ... ; w<sup>i</sup>1Þ. In practice, so that there are not so many overidentifying restrictions, we might replace z<sup>i</sup> with Dzit and choose something like ðDzit; w<sup>i</sup>;t<sup>1</sup>; w<sup>i</sup>;t<sup>2</sup>Þ as the instruments at time t. Or, zit and a couple of lags of zit can be used. In the AR(1) model (11.4), this approach would mean something like ðzit; zi;t<sup>1</sup>; zi;t<sup>2</sup>; yi;t<sup>2</sup>; yi;t3Þ. We can even use leads of zit, such as zi;tþ1, when zit is strictly exogenous. Such choices are amenable to a pooled 2SLS procedure to estimate *g* and *d*. Of course, whether or not the usual 2SLS standard errors are valid depends on serial correlation and variance properties of Duit. Nevertheless, assuming that the changes in the errors are (conditionally) homoskedastic and serially uncorrelated is a reasonable start.

Example 11.4 (Effects of Enterprise Zones): Papke (1994) uses several different panel data models to determine the effect of enterprise zone designation on economic outcomes for 22 communities in Indiana. One model she uses is

$$y_{it} = \theta_t + \rho_1 y_{i,t-1} + \delta_1 e z_{it} + c_i + u_{it}$$
(11.20)

where yit is the log of unemployment claims. The coefficient of interest is on the binary indicator ezit, which is unity if community i in year t was designated as an enterprise zone. The model holds for the years 1981 to 1988, with yi<sup>0</sup> corresponding to 1980, the first year of data. Differencing gives

$$\Delta y_{it} = \xi_t + \rho_1 \Delta y_{i,t-1} + \delta_1 \Delta e z_{it} + \Delta u_{it}$$
(11.21)

The differenced equation has new time intercepts, but as we are not particularly interested in these, we just include year dummies in equation (11.21).

Papke estimates equation (11.21) by 2SLS, using Dyi;t<sup>2</sup> as an instrument for Dyi;t1; because of the lags used, equation (11.21) can be estimated for six years of data. The enterprise zone indicator is assumed to be strictly exogenous in equation (11.20), and so Dezit acts as its own instrument. Strict exogeneity of ezit is valid because, over the years in question, each community was a zone in every year following initial designation: future zone designation did not depend on past performance.

The estimated equation in first differences is

$$\Delta \log(\hat{u}clms) = \hat{\xi}_t + .165 \Delta \log(uclms)_{-1} - .219 \Delta ez$$

$$(.288) \qquad (.106)$$

{318}------------------------------------------------

where the intercept and year dummies are supressed for brevity. Based on the usual pooled 2SLS standard errors, <sup>r</sup>^<sup>1</sup> is not significant (or practially very large), while ^d<sup>1</sup> is economically large and statistically significant at the 5 percent level.

If the uit in equation (11.20) are serially uncorrelated, then, as we saw in Chapter 10, Duit must be serially correlated. Papke found no important differences when the standard error for ^d<sup>1</sup> was adjusted for serial correlation and heteroskedasticity.

In the pure AR(1) model, using lags of yit as an instrument for Dyi;t<sup>1</sup> means that we are assuming the AR(1) model captures all of the dynamics. If further lags of yit are added to the structural model, then we must go back even further to obtain instruments. If strictly exogenous variables appear in the model along with yi;t1 such as in equation (11.4)—then lags of zit are good candidates as instruments for Dyi;t1. Much of the time inclusion of yi;t<sup>1</sup> (or additional lags) in a model with other explanatory variables is intended to simply control for another source of omitted variables bias; Example 11.4 falls into this class.

Things are even trickier in finite distributed lag models. Consider the patents-R&D model of Example 10.2: after first differencing, we have

$$\Delta patents_{it} = \Delta \theta_t + \Delta \mathbf{z}_{it} \gamma + \delta_0 \Delta R D_{it} + \dots + \delta_5 \Delta R D_{i,t-5} + \Delta u_{it}$$
(11.22)

If we are concerned that strict exogeneity fails because of feedback from uit to future R&D expenditures, then DRDit and Duit are potentially correlated (because ui;t<sup>1</sup> and RDit are correlated). Assuming that the distributed lag dynamics are correct—and assuming strict exogeneity of zit—all other explanatory variables in equation (11.22) are uncorrelated with Duit. What can we use as an instrument for DRDit in equation (11.22)? We can include RDi;t<sup>1</sup>; RDi;t<sup>2</sup>; ... in the instrument list at time t (along with all of zi).

This approach identifies the parameters under the assumptions made, but it is problematic. What if we have the distributed lag dynamics wrong, so that six lags, rather than five, belong in the structural model? Then choosing additional lags of RDit as instruments fails. If DRDit is sufficiently correlated with the elements of zis for some s, then using all of z<sup>i</sup> as instruments can help. Generally, some exogenous factors either in zit or from outside the structural equation are needed for a convincing analysis.