# A Random Trend Model

> Pages: 326-328

Consider the following extension of the standard unobserved effects model:

$$y_{it} = c_i + g_i t + \mathbf{x}_{it} \boldsymbol{\beta} + u_{it}, \qquad t = 1, 2, \dots, T$$
 (11.38)

This is sometimes called a random trend model, as each individual, firm, city, and so on is allowed to have its own time trend. The individual-specific trend is an additional source of heterogeneity. If yit is the natural log of a variable, as is often the case in economic studies, then gi is (roughly) the average growth rate over a period (holding the explanatory variables fixed). Then equation (11.38) is referred to a random growth model; see, for example, Heckman and Hotz (1989).

In many applications of equation (11.38) we want to allow ðci; giÞ to be arbitrarily correlated with xit. (Unfortunately, allowing this correlation makes the name ''random trend model'' conflict with our previous usage of random versus fixed effects.) For example, if one element of xit is an indicator of program participation, equation (11.38) allows program participation to depend on individual-specific trends (or growth rates) in addition to the level effect, ci. We proceed without imposing restrictions on correlations among ðci; gi; xitÞ, so that our analysis is of the fixed effects variety. A random effects approach is also possible, but it is more cumbersome; see Problem 11.5.

For the random trend model, the strict exogeneity assumption on the explanatory variables is

$$E(u_{it} | \mathbf{x}_{i1}, \dots, \mathbf{x}_{iT}, c_i, g_i) = 0$$
(11.39)

which follows definitionally from the conditional mean specification

$$E(y_{it} | \mathbf{x}_{i1}, \dots, \mathbf{x}_{iT}, c_i, g_i) = E(y_{it} | \mathbf{x}_{it}, c_i, g_i) = c_i + g_i t + \mathbf{x}_{it} \boldsymbol{\beta}$$

$$(11.40)$$

We are still primarily interested in consistently estimating *b*.

{327}------------------------------------------------

One approach to estimating *b* is to difference away ci:

$$\Delta y_{it} = g_i + \Delta \mathbf{x}_{it} \boldsymbol{\beta} + \Delta u_{it}, \qquad t = 2, 3, \dots, T$$
(11.41)

where we have used the fact that git giðt 1Þ ¼ gi. Now equation (11.41) is just the standard unobserved effects model we studied in Chapter 10. The key strict exogeneity assumption, EðDuit j gi; Dx<sup>i</sup>2; ... ; DxiT Þ ¼ 0, t ¼ 2; 3; ... ; T, holds under assumption (11.39). Therefore, we can apply fixed effects or first-differencing methods to equation (11.41) in order to estimate *b*.

In differencing the equation to eliminate ci we lose one time period, so that equation (11.41) applies to T 1 time periods. To apply FE or FD methods to equation (11.41) we must have T 1b 2, or T b3. In other words, *b* can be estimated consistently in the random trend model only if T b3.

Whether we prefer FE or FD estimation of equation (11.41) depends on the properties of fDuit: t ¼ 2; 3; ... ; Tg. As we argued in Section 10.6, in some cases it is reasonable to assume that the first difference of fuitg is serially uncorrelated, in which case the FE method applied to equation (11.41) is attractive. If we make the assumption that the uit are serially uncorrelated and homoskedastic (conditional on xi, ci, gi), then FE applied to equation (11.41) is still consistent and asymptotically normal, but not efficient. The next subsection covers that case explicitly.

Example 11.7 (Random Growth Model for Analyzing Enterprise Zones): Papke (1994) estimates a random growth model to examine the effects of enterprise zones on unemployment claims:

$$\log(uclms_{it}) = \theta_t + c_i + g_i t + \delta_1 e z_{it} + u_{it}$$

so that aggregate time effects are allowed in addition to a jurisdiction-specific growth rate, gi. She first differences the equation to eliminate ci and then applies fixed effects to the differences. The estimate of d<sup>1</sup> is ^d<sup>1</sup> ¼ :192 with seð^d1Þ ¼ :085. Thus enterprise zone designation is predicted to lower unemployment claims by about 19.2 percent, and the effect is statistically significant at the 5 percent level.

Friedberg (1998) provides an example, using state-level panel data on divorce rates and divorce laws, that shows how important it can be to allow for state-specific trends. Without state-specific trends, she finds no effect of unilateral divorce laws on divorce rates; with state-specific trends, the estimated effect is large and statistically significant. The estimation method Friedberg uses is the one we discuss in the next subsection.

In using the random trend or random growth model for program evaluation, it may make sense to allow the trend or growth rate to depend on program participa

{328}------------------------------------------------

tion: in addition to shifting the level of y, program participation may also affect the rate of change. In addition to progit, we would include progit t in the model:

$$y_{it} = \theta_t + c_i + g_i t + \mathbf{z}_{it} \gamma + \delta_1 prog_{it} + \delta_2 prog_{it} \cdot t + u_{it}$$

Differencing once, as before, removes ci,

$$\Delta y_{it} = \xi_t + g_i + \Delta \mathbf{z}_{it} \boldsymbol{\gamma} + \delta_1 \Delta prog_{it} + \delta_2 \Delta (prog_{it} \cdot t) + \Delta u_{it}$$

We can estimate this differenced equation by fixed effects. An even more flexible specification is to replace progit and progit t with a series of program indicators, prog1it; ... ; progMit, where progjit is one if unit i in time t has been in the program exactly j years, and M is the maximum number of years the program has been around.

If fuitg contains substantial serial correlation—more than a random walk—then differencing equation (11.41) might be more attractive. Denote the second difference of yit by

$$\Delta^2 y_{it} \equiv \Delta y_{it} - \Delta y_{i,t-1} = y_{it} - 2y_{i,t-1} + y_{i,t-2}$$

with similar expressions for D<sup>2</sup> xit and D<sup>2</sup> uit. Then

$$\Delta^2 y_{it} = \Delta^2 \mathbf{x}_{it} \boldsymbol{\beta} + \Delta^2 u_{it}, \qquad t = 3, \dots, T$$
(11.42)

As with the FE transformation applied to equation (11.41), second differencing also eliminates gi. Because D<sup>2</sup> uit is uncorrelated with D<sup>2</sup> xis, for all t and s, we can estimate equation (11.42) by pooled OLS or a GLS procedure.

When T ¼ 3, second differencing is the same as first differencing and then applying fixed effects. Second differencing results in a single cross section on the seconddifferenced data, so that if the second-difference error is homoskedastic conditional on xi, the standard OLS analysis on the cross section of second differences is appropriate. Hoxby (1996) uses this method to estimate the effect of teachers' unions on education production using three years of census data.

If xit contains a time trend, then Dxit contains the same constant for t ¼ 2; 3; ... ; T, which then gets swept away in the FE or FD transformation applied to equation (11.41). Therefore, xit cannot have time-constant variables or variables that have exact linear time trends for all cross section units.