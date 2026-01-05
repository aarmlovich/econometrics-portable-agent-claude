# Some Examples of Unobserved Effects Panel Data Models

> Pages: 266-269

Our discussions in Sections 10.2.1 and 10.2.2 emphasize that in any panel data application we should initially focus on two questions: (1) Is the unobserved effect, ci, uncorrelated with xit for all t? (2) Is the strict exogeneity assumption (conditional on ci) reasonable? The following examples illustrate how we might organize our thinking on these two questions.

Example 10.1 (Program Evaluation): A standard model for estimating the effects of job training or other programs on subsequent wages is

$$\log(wage_{it}) = \theta_t + \mathbf{z}_{it}\gamma + \delta_1 prog_{it} + c_i + u_{it}$$
(10.16)

where i indexes individual and t indexes time period. The parameter y<sup>t</sup> denotes a time-varying intercept, and zit is a set of observable characteristics that affect wage and may also be correlated with program participation.

Evaluation data sets are often collected at two points in time. At t ¼ 1, no one has participated in the program, so that progi<sup>1</sup> ¼ 0 for all i. Then, a subgroup is chosen to participate in the program (or the individuals choose to participate), and subsequent wages are observed for the control and treatment groups in t ¼ 2. Model (10.16) allows for any number of time periods and general patterns of program participation.

The reason for including the individual effect, ci, is the usual omitted ability story: if individuals choose whether or not to participate in the program, that choice could be correlated with ability. This possibility is often called the self-selection problem. Alternatively, administrators might assign people based on characteristics that the econometrician cannot observe.

{267}------------------------------------------------

The other issue is the strict exogeneity assumption of the explanatory variables, particularly progit. Typically, we feel comfortable with assuming that uit is uncorrelated with progit. But what about correlation between uit and, say, progi;tþ1? Future program participation could depend on uit if people choose to participate in the future based on shocks to their wage in the past, or if administrators choose people as participants at time t þ 1 who had a low uit. Such feedback might not be very important, since ci is being allowed for, but it could be. See, for example, Bassi (1984) and Ham and Lalonde (1996). Another issue, which is more easily dealt with, is that the training program could have lasting effects. If so, then we should include lags of progit in model (10.16). Or, the program itself might last more than one period, in which case progit can be replaced by a series of dummy variables for how long unit i at time t has been subject to the program.

Example 10.2 (Distributed Lag Model): Hausman, Hall, and Griliches (1984) estimate nonlinear distributed lag models to study the relationship between patents awarded to a firm and current and past levels of R&D spending. A linear, five-lag version of their model is

$$patents_{it} = \theta_t + \mathbf{z}_{it}\gamma + \delta_0 RD_{it} + \delta_1 RD_{i,t-1} + \dots + \delta_5 RD_{i,t-5} + c_i + u_{it}$$
 (10.17)

where RDit is spending on R&D for firm i at time t and zit contains variables such as firm size (as measured by sales or employees). The variable ci is a firm heterogeneity term that may influence patentsit and that may be correlated with current, past, and future R&D expenditures. Interest lies in the pattern of the d<sup>j</sup> coefficients. As with the other examples, we must decide whether R&D spending is likely to be correlated with ci. In addition, if shocks to patents today (changes in uit) influence R&D spending at future dates, then strict exogeneity can fail, and the methods in this chapter will not apply.

The next example presents a case where the strict exogeneity assumption is necessarily false, and the unobserved effect and the explanatory variable must be correlated.

Example 10.3 (Lagged Dependent Variable): A simple dynamic model of wage determination with unobserved heterogeneity is

$$\log(wage_{it}) = \beta_1 \log(wage_{i,t-1}) + c_i + u_{it}, \qquad t = 1, 2, \dots, T$$
(10.18)

Often, interest lies in how persistent wages are (as measured by the size of b1) after controlling for unobserved heterogeneity (individual productivity), ci. Letting yit ¼ logðwageitÞ, a standard assumption would be

$$E(u_{it} | y_{i,t-1}, \dots, y_{i0}, c_i) = 0$$
(10.19)

{268}------------------------------------------------

which means that all of the dynamics are captured by the first lag. Let  $x_{it} = y_{i,t-1}$ . Then, under assumption (10.19),  $u_{it}$  is uncorrelated with  $(x_{it}, x_{i,t-1}, \dots, x_{i1})$ , but  $u_{it}$  cannot be uncorrelated with  $(x_{i,t+1}, \dots, x_{iT})$ , as  $x_{i,t+1} = y_{it}$ . In fact,

$$E(y_{it}u_{it}) = \beta_1 E(y_{i,t-1}u_{it}) + E(c_i u_{it}) + E(u_{it}^2) = E(u_{it}^2) > 0$$
(10.20)

because  $E(y_{i,t-1}u_{it}) = 0$  and  $E(c_iu_{it}) = 0$  under assumption (10.19). Therefore, the strict exogeneity assumption never holds in unobserved effects models with lagged dependent variables.

In addition,  $y_{i,t-1}$  and  $c_i$  are necessarily correlated (since at time t-1,  $y_{i,t-1}$  is the left-hand-side variable). Not only must strict exogeneity fail in this model, but the exogeneity assumption required for pooled OLS estimation of model (10.18) is also violated. We will study estimation of such models in Chapter 11.

#### 10.3 Estimating Unobserved Effects Models by Pooled OLS

Under certain assumptions, the pooled OLS estimator can be used to obtain a consistent estimator of  $\beta$  in model (10.11). Write the model as

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + v_{it}, \qquad t = 1, 2, \dots, T \tag{10.21}$$

where  $v_{it} \equiv c_i + u_{it}$ , t = 1, ..., T are the **composite errors**. For each t,  $v_{it}$  is the sum of the unobserved effect and an idiosyncratic error. From Section 7.8, we know that pooled OLS estimation of this equation is consistent if  $E(\mathbf{x}'_{it}v_{it}) = \mathbf{0}$ , t = 1, 2, ..., T. Practically speaking, no correlation between  $x_{it}$  and  $v_{it}$  means that we are assuming  $E(\mathbf{x}'_{it}u_{it}) = \mathbf{0}$  and

$$E(\mathbf{x}'_{it}c_i) = \mathbf{0}, \qquad t = 1, 2, \dots, T$$
 (10.22)

Equation (10.22) is the restrictive assumption, since  $E(\mathbf{x}'_{it}u_{it}) = \mathbf{0}$  holds if we have successfully modeled  $E(y_{it} | \mathbf{x}_{it}, c_i)$ .

In static and finite distributed lag models we are sometimes willing to make the assumption (10.22); in fact, we will do so in the next section on random effects estimation. As seen in Example 10.3, models with lagged dependent variables in  $\mathbf{x}_{it}$  must violate assumption (10.22) because  $y_{i,t-1}$  and  $c_i$  must be correlated.

Even if assumption (10.22) holds, the composite errors will be serially correlated due to the presence of  $c_i$  in each time period. Therefore, inference using pooled OLS requires the robust variance matrix estimator and robust test statistics from Chapter 7. Because  $v_{it}$  depends on  $c_i$  for all t, the correlation between  $v_{it}$  and  $v_{is}$  does not generally decrease as the distance |t - s| increases; in time-series parlance, the  $v_{it}$  are

{269}------------------------------------------------

not weakly dependent across time. (We show this fact explicitly in the next section when fuit: t ¼ 1; ... ; Tg is homoskedastic and serially uncorrelated.) Therefore, it is important that we be able to do large-N and fixed-T asymptotics when applying pooled OLS.

As we discussed in Chapter 7, each ðyi; XiÞ has T rows and should be ordered chronologically, and the ðyi; XiÞ should be stacked from i ¼ 1; ... ; N. The order of the cross section observations is, as usual, irrelevant.