# Attrition

> Pages: 593-598

We now turn specifically to testing and correcting for attrition in a linear, unobserved effects panel data model. General attrition, where units may reenter the sample after leaving, is complicated. We analyze a common special case. At t ¼ 1 a random sample is obtained from the relevant population—people, for concreteness. In t ¼ 2 and beyond, some people drop out of the sample for reasons that may not be entirely random. We assume that, once a person drops out, he or she is out forever: attrition is an absorbing state. Any panel data set with attrition can be set up in this way by ignoring any subsequent observations on units after they initially leave the sample. In Section 17.7.2 we discussed one way to test for attrition bias when we assume that attrition is an absorbing state: include si;tþ<sup>1</sup> as an additional explanatory variable in a fixed effects analysis.

One method for correcting for attrition bias is closely related to the corrections for incidental truncation covered in the previous subsection. Write the model for a random draw from the population as in equation (17.49), where we assume that ðxit; yitÞ is observed for all i when t ¼ 1. Let sit denote the selection indicator for each time period, where sit ¼ 1 if ðxit; yitÞ are observed. Because we ignore units once they initially leave the sample, sit ¼ 1 implies sir ¼ 1 for r < t.

The sequential nature of attrition makes first differencing a natural choice to remove the unobserved effect:

$$\Delta y_{it} = \Delta \mathbf{x}_{it} \boldsymbol{\beta} + \Delta u_{it}, \qquad t = 2, \dots, T$$

Conditional on si;t<sup>1</sup> ¼ 1, write a (reduced-form) selection equation for t b 2 as

$$s_{it} = 1[\mathbf{w}_{it}\boldsymbol{\delta}_t + v_{it} > 0], \qquad v_{it} \mid \{\mathbf{w}_{it}, s_{i,t-1} = 1\} \sim \text{Normal}(0, 1)$$
 (17.59)

where wit must contain variables observed at time t for all units with si;t<sup>1</sup> ¼ 1. Good candidates for wit include the variables in x<sup>i</sup>;t<sup>1</sup> and any variables in xit that are observed at time t when si;t<sup>1</sup> ¼ 1 (for example, if xit contains lags of variables or a variable such as age). In general, the dimension of wit can grow with t. For example, if equation (17.49) is dynamically complete, then yi;t<sup>2</sup> is orthogonal to Duit, and so it can be an element of wit. Since yi;t<sup>1</sup> is correlated with ui;t1, it should not be included in wit.

{594}------------------------------------------------

If the  $\mathbf{x}_{it}$  are strictly exogenous *and* selection does not depend on  $\Delta \mathbf{x}_{it}$  once  $\mathbf{w}_{it}$  has been controlled for, a reasonable assumption (say, under joint normality of  $\Delta u_{it}$  and  $v_{it}$ ) is

$$E(\Delta u_{it} \mid \Delta \mathbf{x}_{it}, \mathbf{w}_{it}, v_{it}, s_{i,t-1} = 1) = E(\Delta u_{it} \mid v_{it}) = \rho_t v_{it}$$
(17.60)

Then

$$E(\Delta y_{it} | \Delta \mathbf{x}_{it}, \mathbf{w}_{it}, s_{it} = 1) = \Delta \mathbf{x}_{it} \boldsymbol{\beta} + \rho_t \lambda(\mathbf{w}_{it} \boldsymbol{\delta}_t), \qquad t = 2, \dots, T$$
(17.61)

Notice how, because  $s_{i,t-1} = 1$  when  $s_{it} = 1$ , we do not have to condition on  $s_{i,t-1}$  in equation (17.61). It now follows from equation (17.61) that pooled OLS of  $\Delta y_{it}$  on  $\Delta \mathbf{x}_{it}$ ,  $d2_t\hat{\lambda}_{it}$ , ...,  $dT_t\hat{\lambda}_{it}$ , t = 2, ..., T, where the  $\hat{\lambda}_{it}$  are from the T - 1 cross section probits in equation (17.59), is consistent for  $\boldsymbol{\beta}_1$  and the  $\rho_t$ . A joint test of  $H_0$ :  $\rho_t = 0$ , t = 2, ..., T, is a fairly simple test for attrition bias, although nothing guarantees serial independence of the errors.

There are two potential problems with this approach. For one, the first equality in equation (17.60) is restrictive because it means that  $\mathbf{x}_{it}$  does not affect attrition once the elements in  $\mathbf{w}_{it}$  have been controlled for. Second, we have assumed strict exogeneity of  $\mathbf{x}_{it}$ . Both these restrictions can be relaxed by using an IV procedure.

Let  $\mathbf{z}_{it}$  be a vector of variables such that  $\mathbf{z}_{it}$  is redundant in the selection equation (possibly because  $\mathbf{w}_{it}$  contains  $\mathbf{z}_{it}$ ) and that  $\mathbf{z}_{it}$  is exogenous in the sense that equation (17.58) holds with  $\mathbf{z}_{it}$  in place of  $\Delta \mathbf{x}_{it}$ ; for example,  $\mathbf{z}_{it}$  should contain  $\mathbf{x}_{ir}$  for r < t. Now, using an argument similar to the cross section case in Section 17.4.2, we can estimate the equation

$$\Delta y_{it} = \Delta \mathbf{x}_{it} \boldsymbol{\beta} + \rho_2 d2_t \hat{\lambda}_{it} + \dots + \rho_T dT_t \hat{\lambda}_{it} + error_{it}$$
(17.62)

by instrumental variables with instruments  $(\mathbf{z}_{it}, d2_t \hat{\lambda}_{it}, \dots, dT_t \hat{\lambda}_{it})$ , using the selected sample. For example, the pooled 2SLS estimator on the selected sample is consistent and asymptotically normal, and attrition bias can be tested by a joint test of  $H_0$ :  $\rho_t = 0$ ,  $t = 2, \dots, T$ . Under  $H_0$ , only serial correlation and heteroskedasticity adjustments are possibly needed. If  $H_0$  fails we have the usual generated regressors problem for estimating the asymptotic variance. Other IV procedures, such as GMM, can also be used, but they too must account for the generated regressors problem.

Example 17.9 (Dynamic Model with Attrition): Consider the model

$$y_{it} = \mathbf{g}_{it} \gamma + \eta_1 y_{i,t-1} + c_i + u_{it}, \qquad t = 1, \dots, T$$
 (17.63)

where we assume that  $(y_{i0}, \mathbf{g}_{i1}, y_{i1})$  are all observed for a random sample from the population. Assume that  $E(u_{it} | \mathbf{g}_i, y_{i,t-1}, \dots, y_{i0}, c_i) = 0$ , so that  $\mathbf{g}_{it}$  is strictly exoge-

{595}------------------------------------------------

nous. Then the explanatory variables in the probit at time t, wit, can include g<sup>i</sup>;t1, yi;t2, and further lags of these. After estimating the selection probit for each t, and differencing, we can estimate

$$\Delta y_{it} = \Delta \mathbf{g}_{it} \boldsymbol{\beta} + \eta_1 \Delta y_{i,t-1} + \rho_3 d3_t \hat{\lambda}_{it} + \dots + \rho_T dT_t \hat{\lambda}_{it} + error_{it}$$

by pooled 2SLS on the selected sample starting at t ¼ 3, using instruments ðg<sup>i</sup>;t<sup>1</sup>; g<sup>i</sup>;t<sup>2</sup>; yi;t<sup>2</sup>; yi;t<sup>3</sup>Þ. As usual, there are other possibilities for the instruments.

Although the focus in this section has been on pure attrition, where units disappear entirely from the sample, the methods can also be used in the context of incidental truncation without strictly exogenous explanatory variables. For example, suppose we are interested in the population of men who are employed at t ¼ 0 and t ¼ 1, and we would like to estimate a dynamic wage equation with an unobserved effect. Problems arise if men become unemployed in future periods. Such events can be treated as an attrition problem if all subsequent time periods are dropped once a man first becomes unemployed. This approach loses information but makes the econometrics relatively straightforward, especially because, in the preceding general model, xit will always be observed at time t and so can be included in the labor force participation probit (assuming that men do not leave the sample entirely). Things become much more complicated if we are interested in the wage offer for all working age men at t ¼ 1 because we have to deal with the sample selection problem into employment at t ¼ 0 and t ¼ 1.

The methods for attrition and selection just described apply only to linear models, and it is difficult to extend them to general nonlinear models. An alternative approach is based on inverse probability weighting (IPW ), which can be applied to general M-estimation, at least under certain assumptions.

Moffitt, Fitzgerald, and Gottschalk (1999) (MFG) propose inverse probability weighting to estimate linear panel data models under possibly nonrandom attrition. [MFG propose a different set of weights, analogous to those studied by Horowitz and Manski (1998), to solve missing data problems. The weights we use require estimation of only one attrition model, rather than two as in MFG.] IPW must be used with care to solve the attrition problem. As before, we assume that we have a random sample from the population at t ¼ 1. We are interested in some feature, such as the conditional mean, or maybe the entire conditional distribution, of yit given xit. Ideally, at each t we would observe ðyit; xitÞ for any unit that was in the random sample at t ¼ 1. Instead, we observe ðyit; xitÞ only if sit ¼ 1. We can easily solve the attrition problem if we assume that, conditional on observables in the first time period, say, zi1, ðyit; xitÞ is independent of sit:

{596}------------------------------------------------

$$P(s_{it} = 1 \mid y_{it}, \mathbf{x}_{it}, \mathbf{z}_{i1}) = P(s_{it} = 1 \mid \mathbf{z}_{i1}), \qquad t = 2, \dots, T$$
(17.64)

Assumption (17.64) has been called **selection on observables** because we assume that  $\mathbf{z}_{i1}$  is a strong enough predictor of selection in each time period so that the distribution of  $s_{it}$  given  $[\mathbf{z}_{i1}, (y_{it}, \mathbf{x}_{it})]$  does not depend on  $(y_{it}, \mathbf{x}_{it})$ . In the statistics literature, selection on observables is also called **ignorability of selection** conditional on  $\mathbf{z}_{i1}$ . [The more standard approach, where selection is given by equation (17.59) and  $\Delta u_{it}$  is correlated with  $v_{it}$ , is sometimes called **selection on unobservables**. These categorizations are not strictly correct, as selection in both cases depends on observables and unobservables, but they serve as useful shorthand.]

Inverse probability weighting involves two steps. First, for each t, we estimate a probit or logit of  $s_{it}$  on  $\mathbf{z}_{i1}$ . (A crucial point is that the same cross section units—namely, all units appearing in the first time period—are used in the probit or logit for each time period.) Let  $\hat{p}_{it}$  be the fitted probabilities, t = 2, ..., T, i = 1, ..., N. In the second step, the objective function for (i, t) is weighted by  $1/\hat{p}_{it}$ . For general Mestimation, the objective function is

$$\sum_{i=1}^{N} \sum_{t=1}^{T} (s_{it}/\hat{p}_{it}) q_t(\mathbf{w}_{it}, \boldsymbol{\theta})$$
 (17.65)

where  $\mathbf{w}_{it} \equiv (y_{it}, \mathbf{x}_{it})$  and  $q_t(\mathbf{w}_{it}, \boldsymbol{\theta})$  is the objective function in each time period. As usual, the selection indicator  $s_{it}$  chooses the observations where we actually observe data. (For t = 1,  $s_{it} = \hat{p}_{it} = 1$  for all i.) For least squares,  $q_t(\mathbf{w}_{it}, \boldsymbol{\theta})$  is simply the squared residual function; for partial MLE,  $q_t(\mathbf{w}_{it}, \boldsymbol{\theta})$  is the log-likelihood function.

The argument for why IPW works is rather simple. Let  $\boldsymbol{\theta}_{o}$  denote the value of  $\boldsymbol{\theta}$  that solves the population problem  $\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \sum_{t=1}^{T} \mathrm{E}[q_{t}(\mathbf{w}_{it}, \boldsymbol{\theta})]$ . Let  $\boldsymbol{\delta}_{t}^{o}$  denote the true values of the selection response parameters in each time period, so that  $\mathrm{P}(s_{it} = 1 \mid \mathbf{z}_{i1}) = p_{t}(\mathbf{z}_{i1}, \boldsymbol{\delta}_{t}^{o}) \equiv p_{it}^{o}$ . Now, under standard regularity conditions, we can replace  $p_{it}^{o}$  with  $\hat{p}_{it} \equiv p_{t}(\mathbf{z}_{i1}, \hat{\boldsymbol{\delta}}_{t})$  without affecting the consistency argument. So, apart from regularity conditions, it is sufficient to show that  $\boldsymbol{\theta}_{o}$  minimizes  $\sum_{t=1}^{T} \mathrm{E}[(s_{it}/p_{it}^{o})q_{t}(\mathbf{w}_{it}, \boldsymbol{\theta})]$  over  $\boldsymbol{\theta}$ . But, from iterated expectations,

$$E[(s_{it}/p_{it}^{o})q_{t}(\mathbf{w}_{it},\boldsymbol{\theta})] = E\{E[(s_{it}/p_{it}^{o})q_{t}(\mathbf{w}_{it},\boldsymbol{\theta}) \mid \mathbf{w}_{it}, \mathbf{z}_{i1}]\}$$

$$= E\{[E(s_{it} \mid \mathbf{w}_{it}, \mathbf{z}_{i1})/p_{it}^{o}]q_{t}(\mathbf{w}_{it},\boldsymbol{\theta})\} = E[q_{t}(\mathbf{w}_{it},\boldsymbol{\theta})]$$

because  $E(s_{it} | \mathbf{w}_{it}, \mathbf{z}_{i1}) = P(s_{it} = 1 | \mathbf{z}_{i1})$  by assumption (17.64). Therefore, the probability limit of the weighted objective function is identical to that of the unweighted function *if* we had no attrition problem. Using this simple analogy argument, Wooldridge (2000d) shows that the inverse probability weighting produces a consistent,

{597}------------------------------------------------

 $\sqrt{N}$ -asymptotically normal estimator. The methods for adjusting the asymptotic variance matrix of two step M-estimators—described in Subsection 12.5.2—can be applied to the IPW M-estimator from (17.65). For reasons we will see, a sequential method of estimating attrition probabilities can be more attractive.

MFG propose an IPW scheme where the conditioning variables in the attrition probits change across time. In particular, at time t an attrition probit is estimated restricting attention to those units still in the sample at time t-1. (Out of this group, some are lost to attrition at time t, and some are not.) If we assume that attrition is an absorbing state, we can include in the conditioning variables,  $\mathbf{z}_{it}$ , all values of y and x dated at time t-1 and earlier (as well as other variables observed for all units in the sample at t-1). This approach is appealing because the ignorability assumption is much more plausible if we can condition on both recent responses and covariates. [That is,  $P(s_{it} = 1 | \mathbf{w}_{it}, \mathbf{w}_{i,t-1}, \dots, \mathbf{w}_{i1}, s_{i,t-1} = 1) = P(s_{it} = 1 | \mathbf{w}_{i,t-1}, \dots, \mathbf{w}_{it}, s_{i,t-1} = 1)$  $\mathbf{w}_{i1}, s_{i,t-1} = 1$ ) is more likely than assumption (17.64).] Unfortunately, obtaining the fitted probabilities in this way and using them in an IPW procedure does not generally produce consistent estimators. The problem is that the selection models at each time period are not representative of the population that was originally sampled at t=1. Letting  $p_{it}^{o}=\mathbf{P}(s_{it}=1\,|\,\mathbf{w}_{i,t-1},\ldots,\mathbf{w}_{i1},s_{i,t-1}=1),$  we can no longer use the iterated expectations argument to conclude that  $E[(s_{it}/p_{it}^{o})q_{t}(\mathbf{w}_{it},\boldsymbol{\theta})] = E[q_{t}(\mathbf{w}_{it},\boldsymbol{\theta})].$ Only if  $E[q_t(\mathbf{w}_{it}, \boldsymbol{\theta})] = E[q_t(\mathbf{w}_{it}, \boldsymbol{\theta}) | s_{i,t-1} = 1]$  for all  $\boldsymbol{\theta}$  does the argument work, but this assumption essentially requires that  $\mathbf{w}_{it}$  be independent of  $s_{i,t-1}$ .

It is possible to allow the covariates in the selection probabilities to increase in richness over time, but the MFG procedure must be modified. For the case where attrition is an absorbing state, Wooldridge (2000d), building on work for regression models by Robins, Rotnitzky, and Zhao (1995) (RRZ), shows that the following probabilities can be used in the IPW procedure:

$$p_{it}(\boldsymbol{\delta}_{t}^{o}) \equiv \pi_{i2}(\boldsymbol{\gamma}_{2}^{o})\pi_{i3}(\boldsymbol{\gamma}_{3}^{o})\cdots\pi_{it}(\boldsymbol{\gamma}_{t}^{o}), \qquad t = 2,\dots,T$$

$$(17.66)$$

where

$$\pi_{it}(\gamma_t^0) \equiv \mathbf{P}(s_{it} = 1 \mid \mathbf{z}_{it}, s_{i,t-1} = 1)$$
 (17.67)

In other words, as in the MFG procedure, we estimate probit models at each time t, restricted to units that are in the sample at t-1. The covariates in the probit are essentially everything we can observe for units in the sample at time t-1 that might affect attrition. For  $t=2,\ldots,T$ , let  $\hat{\pi}_{it}$  denote the fitted selection probabilities. Then we construct the probability weights as the product  $\hat{p}_{it} \equiv \hat{\pi}_{i2}\hat{\pi}_{i3}\cdots\hat{\pi}_{it}$  and use the objective function (17.65). Naturally, this method only works under certain assumptions. The key ignorability condition can be stated as

{598}------------------------------------------------

$$P(s_{it} = 1 \mid \mathbf{v}_{i1}, \dots, \mathbf{v}_{iT}, s_{i,t-1} = 1) = P(s_{it} = 1 \mid \mathbf{z}_{it}, s_{i,t-1} = 1)$$
(17.68)

where vit 1 ðwit; zitÞ. Now, we must include future values of wit and zit in the conditioning set on the left-hand side. Assumption (17.68) is fairly strong, but it does allow for attrition to be strongly related to past outcomes on y and x (which can be included in zit).

A convenient feature of the sequential method described above is that ignoring the first-stage estimation of the probabilities actually leads to conservative inference concerning *y*0: the (correct) asymptotic variance that adjusts for the first-stage estimation is actually smaller than the one that does not. See Wooldridge (2000d) for the general case and RRZ (1995) for the nonlinear regression case. See Wooldridge (2000d) for more on the pros and cons of using inverse probability weighting to reduce attrition bias.