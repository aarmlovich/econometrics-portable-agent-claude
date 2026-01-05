# Introduction

> Pages: 156-160

This chapter begins our analysis of linear systems of equations. The first method of estimation we cover is system ordinary least squares, which is a direct extension of OLS for single equations. In some important special cases the system OLS estimator turns out to have a straightforward interpretation in terms of single-equation OLS estimators. But the method is applicable to very general linear systems of equations.

We then turn to a generalized least squares (GLS) analysis. Under certain assumptions, GLS—or its operationalized version, feasible GLS—will turn out to be asymptotically more efficient than system OLS. However, we emphasize in this chapter that the efficiency of GLS comes at a price: it requires stronger assumptions than system OLS in order to be consistent. This is a practically important point that is often overlooked in traditional treatments of linear systems, particularly those which assume that explanatory variables are nonrandom.

As with our single-equation analysis, we assume that a random sample is available from the population. Usually the unit of observation is obvious—such as a worker, a household, a firm, or a city. For example, if we collect consumption data on various commodities for a sample of families, the unit of observation is the family (not a commodity).

The framework of this chapter is general enough to apply to panel data models. Because the asymptotic analysis is done as the cross section dimension tends to infinity, the results are explicitly for the case where the cross section dimension is large relative to the time series dimension. (For example, we may have observations on N firms over the same T time periods for each firm. Then, we assume we have a random sample of firms that have data in each of the T years.) The panel data model covered here, while having many useful applications, does not fully exploit the replicability over time. In Chapters 10 and 11 we explicitly consider panel data models that contain time-invariant, unobserved effects in the error term.

# 7.2 Some Examples

We begin with two examples of systems of equations. These examples are fairly general, and we will see later that variants of them can also be cast as a general linear system of equations.

Example 7.1 (Seemingly Unrelated Regressions): The population model is a set of G linear equations,

{157}------------------------------------------------

$$y_{1} = \mathbf{x}_{1}\boldsymbol{\beta}_{1} + u_{1}$$

$$y_{2} = \mathbf{x}_{2}\boldsymbol{\beta}_{2} + u_{2}$$

$$\vdots$$

$$y_{G} = \mathbf{x}_{G}\boldsymbol{\beta}_{G} + u_{G}$$

$$(7.1)$$

where  $\mathbf{x}_g$  is  $1 \times K_g$  and  $\boldsymbol{\beta}_g$  is  $K_g \times 1$ ,  $g = 1, 2, \ldots, G$ . In many applications  $\mathbf{x}_g$  is the same for all g (in which case the  $\boldsymbol{\beta}_g$  necessarily have the same dimension), but the general model allows the elements and the dimension of  $\mathbf{x}_g$  to vary across equations. Remember, the system (7.1) represents a generic person, firm, city, or whatever from the population. The system (7.1) is often called Zellner's (1962) seemingly unrelated regressions (SUR) model (for cross section data in this case). The name comes from the fact that, since each equation in the system (7.1) has its own vector  $\boldsymbol{\beta}_g$ , it appears that the equations are unrelated. Nevertheless, correlation across the errors in different equations can provide links that can be exploited in estimation; we will see this point later.

As a specific example, the system (7.1) might represent a set of demand functions for the population of families in a country:

$$\begin{aligned} \textit{housing} &= \beta_{10} + \beta_{11} \textit{houseprc} + \beta_{12} \textit{foodprc} + \beta_{13} \textit{clothprc} + \beta_{14} \textit{income} \\ &+ \beta_{15} \textit{size} + \beta_{16} \textit{age} + u_1 \\ \textit{food} &= \beta_{20} + \beta_{21} \textit{houseprc} + \beta_{22} \textit{foodprc} + \beta_{23} \textit{clothprc} + \beta_{24} \textit{income} \\ &+ \beta_{25} \textit{size} + \beta_{26} \textit{age} + u_2 \\ \textit{clothing} &= \beta_{30} + \beta_{31} \textit{houseprc} + \beta_{32} \textit{foodprc} + \beta_{33} \textit{clothprc} + \beta_{34} \textit{income} \\ &+ \beta_{35} \textit{size} + \beta_{36} \textit{age} + u_3 \end{aligned}$$

In this example, G = 3 and  $\mathbf{x}_g$  (a  $1 \times 7$  vector) is the same for g = 1, 2, 3.

When we need to write the equations for a particular random draw from the population,  $y_g$ ,  $\mathbf{x}_g$ , and  $u_g$  will also contain an i subscript: equation g becomes  $y_{ig} = \mathbf{x}_{ig}\boldsymbol{\beta}_g + u_{ig}$ . For the purposes of stating assumptions, it does not matter whether or not we include the i subscript. The system (7.1) has the advantage of being less cluttered while focusing attention on the population, as is appropriate for applications. But for derivations we will often need to indicate the equation for a generic cross section unit i.

When we study the asymptotic properties of various estimators of the  $\beta_g$ , the asymptotics is done with G fixed and N tending to infinity. In the household demand example, we are interested in a set of three demand functions, and the unit of obser-

{158}------------------------------------------------

vation is the family. Therefore, inference is done as the number of families in the sample tends to infinity.

The assumptions that we make about how the unobservables ug are related to the explanatory variables ðx1; x2; ... ; xGÞ are crucial for determining which estimators of the *b*<sup>g</sup> have acceptable properties. Often, when system (7.1) represents a structural model (without omitted variables, errors-in-variables, or simultaneity), we can assume that

$$E(u_g | \mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_G) = 0, \qquad g = 1, \dots, G$$
 (7.2)

One important implication of assumption (7.2) is that ug is uncorrelated with the explanatory variables in all equations, as well as all functions of these explanatory variables. When system (7.1) is a system of equations derived from economic theory, assumption (7.2) is often very natural. For example, in the set of demand functions that we have presented, x<sup>g</sup> 1x is the same for all g, and so assumption (7.2) is the same as Eðug j xgÞ ¼ Eðug j xÞ ¼ 0.

If assumption (7.2) is maintained, and if the x<sup>g</sup> are not the same across g, then any explanatory variables excluded from equation g are assumed to have no effect on expected yg once x<sup>g</sup> has been controlled for. That is,

$$E(y_g \mid \mathbf{x}_1, \mathbf{x}_2, \dots \mathbf{x}_G) = E(y_g \mid \mathbf{x}_g) = \mathbf{x}_g \boldsymbol{\beta}_g, \qquad g = 1, 2, \dots, G$$
(7.3)

There are examples of SUR systems where assumption (7.3) is too strong, but standard SUR analysis either explicitly or implicitly makes this assumption.

Our next example involves panel data.

Example 7.2 (Panel Data Model): Suppose that for each cross section unit we observe data on the same set of variables for T time periods. Let x<sup>t</sup> be a 1 K vector for t ¼ 1; 2; ... ; T, and let *b* be a K 1 vector. The model in the population is

$$y_t = \mathbf{x}_t \boldsymbol{\beta} + u_t, \qquad t = 1, 2, \dots, T \tag{7.4}$$

where yt is a scalar. For example, a simple equation to explain annual family saving over a five-year span is

$$sav_t = \beta_0 + \beta_1 inc_t + \beta_2 age_t + \beta_3 educ_t + u_t, \qquad t = 1, 2, \dots, 5$$

where inct is annual income, educt is years of education of the household head, and aget is age of the household head. This is an example of a linear panel data model. It is a static model because all explanatory variables are dated contemporaneously with savt.

The panel data setup is conceptually very different from the SUR example. In Example 7.1, each equation explains a different dependent variable for the same cross

{159}------------------------------------------------

section unit. Here we only have one dependent variable we are trying to explain—sav—but we observe sav, and the explanatory variables, over a five-year period. (Therefore, the label "system of equations" is really a misnomer for panel data applications. At this point, we are using the phrase to denote more than one equation in any context.) As we will see in the next section, the statistical properties of estimators in SUR and panel data models can be analyzed within the same structure.

When we need to indicate that an equation is for a particular cross section unit i during a particular time period t, we write  $y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + u_{it}$ . We will omit the i subscript whenever its omission does not cause confusion.

What kinds of exogeneity assumptions do we use for panel data analysis? One possibility is to assume that  $u_t$  and  $\mathbf{x}_t$  are orthogonal in the conditional mean sense:

$$\mathbf{E}(u_t | \mathbf{x}_t) = 0, \qquad t = 1, \dots, T \tag{7.5}$$

We call this **contemporaneous exogeneity** of  $\mathbf{x}_t$  because it only restricts the relationship between the disturbance and explanatory variables in the same time period. It is very important to distinguish assumption (7.5) from the stronger assumption

$$E(u_t | \mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_T) = 0, \qquad t = 1, \dots, T$$
 (7.6)

which, combined with model (7.4), is identical to  $E(y_t | \mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_T) = E(y_t | \mathbf{x}_t)$ . Assumption (7.5) places no restrictions on the relationship between  $\mathbf{x}_s$  and  $u_t$  for  $s \neq t$ , while assumption (7.6) implies that each  $u_t$  is uncorrelated with the explanatory variables in *all* time periods. When assumption (7.6) holds, we say that the explanatory variables  $\{\mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_t, \dots, \mathbf{x}_T\}$  are **strictly exogenous**.

To illustrate the difference between assumptions (7.5) and (7.6), let  $\mathbf{x}_t \equiv (1, y_{t-1})$ . Then assumption (7.5) holds if  $\mathrm{E}(y_t \mid y_{t-1}, y_{t-2}, \dots, y_0) = \beta_0 + \beta_1 y_{t-1}$ , which imposes first-order dynamics in the conditional mean. However, assumption (7.6) *must* fail since  $\mathbf{x}_{t+1} = (1, y_t)$ , and therefore  $\mathrm{E}(u_t \mid \mathbf{x}_1, \mathbf{x}_2, \dots, \mathbf{x}_T) = \mathrm{E}(u_t \mid y_0, y_1, \dots, y_{T-1}) = u_t$  for  $t = 1, 2, \dots, T-1$  (because  $u_t = y_t - \beta_0 - \beta_1 y_{t-1}$ ).

Assumption (7.6) can fail even if  $\mathbf{x}_t$  does *not* contain a lagged dependent variable. Consider a model relating poverty rates to welfare spending per capita, at the city level. A **finite distributed lag (FDL) model** is

$$poverty_t = \theta_t + \delta_0 welfare_t + \delta_1 welfare_{t-1} + \delta_2 welfare_{t-2} + u_t$$
(7.7)

where we assume a two-year effect. The parameter  $\theta_t$  simply denotes a different aggregate time effect in each year. It is reasonable to think that welfare spending reacts to lagged poverty rates. An equation that captures this feedback is

$$welfare_t = \eta_t + \rho_1 poverty_{t-1} + r_t \tag{7.8}$$

{160}------------------------------------------------

Even if equation (7.7) contains enough lags of welfare spending, assumption (7.6) would be violated if  $\rho_1 \neq 0$  in equation (7.8) because welfare<sub>t+1</sub> depends on  $u_t$  and  $\mathbf{x}_{t+1}$  includes welfare<sub>t+1</sub>.

How we go about consistently estimating  $\beta$  depends crucially on whether we maintain assumption (7.5) or the stronger assumption (7.6). Assuming that the  $\mathbf{x}_{it}$  are fixed in repeated samples is effectively the same as making assumption (7.6).