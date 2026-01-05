# Fixed Effects Estimation with Unbalanced Panels

> Pages: 586-593

We begin by studying assumptions under which the usual fixed effects estimator on the unbalanced panel is consistent. The model is the usual linear, unobserved effects model under random sampling in the cross section: for any i,

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + c_i + u_{it}, \qquad t = 1, \dots, T$$
(17.49)

where xit is 1 K and *b* is the K 1 vector of interest. As before, we assume that N cross section observations are available and the asymptotic analysis is as N ! y. We explicitly cover the case where ci is allowed to be correlated with xit, so that all elements of xit are time varying. A random effects analysis is also possible under stronger assumptions; see, for example, Verbeek and Nijman (1992, 1996).

We covered the case where all T time periods are available in Chapters 10 and 11. Now we consider the case where some time periods might be missing for some of the cross section draws. Think of t ¼ 1 as the first time period for which data on anyone in the population are available, and t ¼ T as the last possible time period. For a random draw i from the population, let s<sup>i</sup> 1ðsi1; ... ;siT Þ <sup>0</sup> denote the T 1 vector of selection indicators: sit ¼ 1 if ðxit; yitÞ is observed, and zero otherwise. Generally, we 

{587}------------------------------------------------

have an unbalanced panel. We can treat  $\{(\mathbf{x}_i, \mathbf{y}_i, \mathbf{s}_i): i = 1, 2, ..., N\}$  as a random sample from the population; the selection indicators tell us which time periods are missing for each i.

We can easily find assumptions under which the fixed effects estimator on the unbalanced panel is consistent by writing it as

$$\hat{\boldsymbol{\beta}} = \left( N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} s_{it} \ddot{\mathbf{x}}_{it}' \ddot{\mathbf{x}}_{it} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} s_{it} \ddot{\mathbf{x}}_{it}' \ddot{y}_{it} \right)$$

$$= \boldsymbol{\beta} + \left( N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} s_{it} \ddot{\mathbf{x}}_{it}' \ddot{\mathbf{x}}_{it} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \sum_{t=1}^{T} s_{it} \ddot{\mathbf{x}}_{it}' u_{it} \right)$$
(17.50)

where we define

$$\ddot{\mathbf{x}}_{it} \equiv \mathbf{x}_{it} - T_i^{-1} \sum_{r=1}^T s_{ir} \mathbf{x}_{ir}, \qquad \ddot{\mathbf{y}}_{it} \equiv \mathbf{y}_{it} - T_i^{-1} \sum_{r=1}^T s_{ir} \mathbf{y}_{ir}, \qquad \text{and} \qquad T_i \equiv \sum_{t=1}^T s_{it}$$

That is,  $T_i$  is the number of time periods observed for cross section i, and we apply the within transformation on the available time periods.

If fixed effects on the unbalanced panel is to be consistent, we should have  $E(s_{it}\ddot{\mathbf{x}}'_{it}u_{it}) = 0$  for all t. Now, since  $\ddot{\mathbf{x}}_{it}$  depends on all of  $\mathbf{x}_i$  and  $\mathbf{s}_i$ , a form of strict exogeneity is needed.

ASSUMPTION 17.6: (a) 
$$\mathrm{E}(u_{it} \mid \mathbf{x}_i, \mathbf{s}_i, c_i) = 0$$
,  $t = 1, 2, \dots, T$ ; (b)  $\sum_{t=1}^T \mathrm{E}(s_{it}\ddot{\mathbf{x}}_{it}'\ddot{\mathbf{x}}_{it})$  is nonsingular; and (c)  $\mathrm{E}(\mathbf{u}_i\mathbf{u}_i' \mid \mathbf{x}_i, \mathbf{s}_i, c_i) = \sigma_u^2\mathbf{I}_T$ .

Under Assumption 17.6a,  $E(s_{it}\ddot{\mathbf{x}}'_{it}u_{it}) = \mathbf{0}$  from the law of iterated expectations [because  $s_{it}\ddot{\mathbf{x}}_{it}$  is a function of  $(\mathbf{x}_i, \mathbf{s}_i)$ ]. The second assumption is the rank condition on the expected outer product matrix, after accounting for sample selection; naturally, it rules out time-constant elements in  $\mathbf{x}_{it}$ . These first two assumptions ensure consistency of FE on the unbalanced panel.

In the case of a randomly rotating panel, and in other cases where selection is entirely random,  $\mathbf{s}_i$  is independent of  $(\mathbf{u}_i, \mathbf{x}_i, c_i)$ , in which case Assumption 17.6a follows under the standard fixed effects assumption  $\mathrm{E}(u_{it} \mid \mathbf{x}_i, c_i) = 0$  for all t. In this case, the natural assumptions on the population model imply consistency and asymptotic normality on the unbalanced panel. Assumption 17.6a also holds under much weaker conditions. In particular, it does not assume anything about the relationship between  $\mathbf{s}_i$  and  $(\mathbf{x}_i, c_i)$ . Therefore, if we think selection in all time periods is correlated with  $c_i$  or  $\mathbf{x}_i$ , but that  $u_{it}$  is mean independent of  $\mathbf{s}_i$  given  $(\mathbf{x}_i, c_i)$  for all t, then FE on the

{588}------------------------------------------------

unbalanced panel is consistent and asymptotically normal. This conclusion may be a reasonable approximation, especially for short panels. What Assumption 17.6a rules out is selection that is partially correlated with the idiosyncratic errors,  $u_{it}$ .

A random effects analysis on the unbalanced panel requires much stronger assumptions: it effectively requires  $\mathbf{s}_i$  and  $c_i$  to be independent. Random effects will be inconsistent if, say, in a wage offer equation, less able people are more likely to disappear from the sample. This conclusion is true even if  $E(c_i | \mathbf{x}_i) = 0$  (Assumption RE.1 from Chapter 10) holds in the underlying population; see Wooldridge (1995a) for further discussion.

When we add Assumption 17.6c, standard inference procedures based on FE are valid. In particular, under Assumptions 17.6a and 17.6c,

$$\operatorname{Var}\left(\sum_{t=1}^{T} s_{it} \ddot{\mathbf{x}}_{it}' u_{it}\right) = \sigma_{u}^{2} \left[\sum_{t=1}^{T} \operatorname{E}(s_{it} \ddot{\mathbf{x}}_{it}' \ddot{\mathbf{x}}_{it})\right]$$

Therefore, the asymptotic variance of the fixed effects estimator is estimated as

$$\hat{\sigma}_{u}^{2} \left( \sum_{i=1}^{N} \sum_{t=1}^{T} s_{it} \ddot{\mathbf{x}}_{it}' \ddot{\mathbf{x}}_{it} \right)^{-1}$$
(17.51)

The estimator  $\hat{\sigma}_u^2$  can be derived from

$$E\left(\sum_{t=1}^{T} s_{it} \ddot{\boldsymbol{u}}_{it}^{2}\right) = E\left[\sum_{t=1}^{T} s_{it} E(\ddot{\boldsymbol{u}}_{it}^{2} | \mathbf{s}_{i})\right] = E\left\{T_{i}[\sigma_{u}^{2}(1 - 1/T_{i})]\right\} = \sigma_{u}^{2} E[(T_{i} - 1)]$$

Now, define the FE residuals as  $\hat{\mathbf{u}}_{it} = \ddot{\mathbf{y}}_{it} - \ddot{\mathbf{x}}_{it}\hat{\boldsymbol{\beta}}$  when  $s_{it} = 1$ . Then, because  $N^{-1} \sum_{i=1}^{N} (T_i - 1) \stackrel{p}{\to} \mathrm{E}(T_i - 1)$ ,

$$\hat{\sigma}_u^2 = \left[ N^{-1} \sum_{i=1}^N (T_i - 1) \right]^{-1} N^{-1} \sum_{i=1}^N \sum_{t=1}^T s_{it} \hat{u}_{it}^2 = \left[ \sum_{i=1}^N (T_i - 1) \right]^{-1} \sum_{i=1}^N \sum_{t=1}^T s_{it} \hat{u}_{it}^2$$

is consistent for  $\sigma_u^2$  as  $N \to \infty$ . Standard software packages also make a degrees-of-freedom adjustment by subtracting K from  $\sum_{i=1}^{N} (T_i - 1)$ . It follows that all of the usual test statistics based on an unbalanced fixed effects analysis are valid. In particular, the dummy variable regression discussed in Chapter 10 produces asymptotically valid statistics.

Because the FE estimator uses time demeaning, any unit i for which  $T_i = 1$  drops out of the fixed effects estimator. To use these observations we would need to add more assumptions, such as the random effects assumption  $E(c_i | \mathbf{x}_i, \mathbf{s}_i) = 0$ .

{589}------------------------------------------------

Relaxing Assumption 17.6c is easy: just apply the robust variance matrix estimator in equation (10.59) to the unbalanced panel. The only changes are that the rows of  $\ddot{\mathbf{X}}_i$  are  $s_{it}\ddot{\mathbf{x}}_{it}$  and the elements of  $\hat{\mathbf{u}}_i$  are  $s_{it}\hat{\mathbf{u}}_{it}$ ,  $t = 1, \ldots, T$ .

Under Assumption 17.6, it is also valid to used a standard fixed effects analysis on any balanced subset of the unbalanced panel; in fact, we can condition on any outcomes of the  $s_{it}$ . For example, if we use unit i only when observations are available in all time periods, we are conditioning on  $s_{it} = 1$  for all t.

Using similar arguments, it can be shown that any kind of differencing method on any subset of the observed panel is consistent. For example, with T=3, we observe cross section units with data for one, two, or three time periods. Those units with  $T_i=1$  drop out, but any other combinations of differences can be used in a pooled OLS analysis. The analogues of Assumption 17.6 for first differencing—for example, Assumption 17.6c is replaced with  $E(\Delta \mathbf{u}_i \Delta \mathbf{u}_i' | \mathbf{x}_i, \mathbf{s}_i, c_i) = \sigma_e^2 \mathbf{I}_{T-1}$ —ensure that the usual statistics from pooled OLS on the unbalanced first differences are asymptotically valid.

#### 17.7.2 Testing and Correcting for Sample Selection Bias

The results in the previous subsection imply that sample selection in a fixed effects context is only a problem when selection is related to the idiosyncratic errors,  $u_{it}$ . Therefore, any test for selection bias should test only this assumption. A simple test was suggested by Nijman and Verbeek (1992) in the context of random effects estimation, but it works for fixed effects as well: add, say, the lagged selection indicator,  $s_{i,t-1}$ , to the equation, estimate the model by fixed effects (on the unbalanced panel), and do a t test (perhaps making it fully robust) for the significance of  $s_{i,t-1}$ . (This method loses the first time period for *all* observations.) Under the null hypothesis,  $u_{it}$  is uncorrelated with  $s_{ir}$  for all r, and so selection in the previous time period should not be significant in the equation at time t. (Incidentally, it never makes sense to put  $s_{it}$  in the equation at time t because  $s_{it} = 1$  for all i and t in the selected subsample.)

Putting  $s_{i,t-1}$  does not work if  $s_{i,t-1}$  is unity whenever  $s_{it}$  is unity because then there is no variation in  $s_{i,t-1}$  in the selected sample. This is the case in attrition problems if (say) a person can only appear in period t if he or she appeared in t-1. An alternative is to include a lead of the selection indicator,  $s_{i,t+1}$ . For observations t that are in the sample every time period,  $s_{i,t+1}$  is always zero. But for attriters,  $s_{i,t+1}$  switches from zero to one in the period just before attrition. If we use fixed effects or first differencing, we need T > 2 time periods to carry out the test.

For incidental truncation problems it makes sense to extend Heckman's (1976) test to the unobserved effects panel data context. This is done in Wooldridge (1995a). Write the equation of interest as

{590}------------------------------------------------

$$y_{it1} = \mathbf{x}_{it1} \boldsymbol{\beta}_1 + c_{i1} + u_{it1}, \qquad t = 1, \dots, T$$
 (17.52)

Initially, suppose that yit<sup>1</sup> is observed only if the binary selection indicator, sit2, is unity. Let xit denote the set of all exogenous variables at time t; we assume that these are observed in every time period, and xit<sup>1</sup> is a subset of xit. Suppose that, for each t, sit<sup>2</sup> is determined by the probit equation

$$s_{it2} = 1[\mathbf{x}_i \boldsymbol{\psi}_{t2} + v_{it2} > 0], \quad v_{it2} \mid \mathbf{x}_i \sim \text{Normal}(0, 1)$$
 (17.53)

where x<sup>i</sup> contains unity. This is best viewed as a reduced-form selection equation: we let the explanatory variables in all time periods appear in the selection equation at time t to allow for general selection models, including those with unobserved effect and the Chamberlain (1980) device discussed in Section 15.8.2, as well as certain dynamic models of selection. A Mundlak (1978) approach would replace x<sup>i</sup> with ðxit; xiÞ at time t and assume that coefficients are constant across time. [See equation (15.68).] Then the parameters can be estimated by pooled probit, greatly conserving on degrees of freedom. Such conservation may be important for small N. For testing purposes, under the null hypothesis it does not matter whether equation (17.53) is the proper model of sample selection, but we will need to assume equation (17.53), or a Mundlak version of it, when correcting for sample selection.

Under the null hypothesis in Assumption 17.6a (with the obvious notational changes), the inverse Mills ratio obtained from the sample selection probit should not be significant in the equation estimated by fixed effects. Thus, let ^lit<sup>2</sup> be the estimated Mills ratios from estimating equation (17.53) by pooled probit across i and t. Then a valid test of the null hypothesis is a t statistic on ^lit<sup>2</sup> in the FE estimation on the unbalanced panel. Under Assumption 17.6c the usual t statistic is valid, but the approach works whether or not the uit<sup>1</sup> are homoskedastic and serially uncorrelated: just compute the robust standard error. Wooldridge (1995a) shows formally that the firststage estimation of *c*<sup>2</sup> does not affect the limiting distribution of the t statistic under H0. This conclusion also follows from the results in Chapter 12 on M-estimation.

Correcting for sample selection requires much more care. Unfortunately, under any assumptions that actually allow for an unobserved effect in the underlying selection equation, adding ^lit<sup>2</sup> to equation (17.52) and using FE does not produce consistent estimators. To see why, suppose

$$s_{it2} = 1[\mathbf{x}_{it}\boldsymbol{\delta}_2 + c_{i2} + a_{it2} > 0], \quad a_{it2} \mid (\mathbf{x}_i, c_{i1}, c_{i2}) \sim \text{Normal}(0, 1)$$
 (17.54)

Then, to get equation (17.53), vit<sup>2</sup> depends on ait<sup>2</sup> and, at least partially, on ci2. Now, suppose we make the strong assumption Eðuit<sup>1</sup> j xi; ci1; ci2; v<sup>i</sup>2Þ ¼ gi<sup>1</sup> þ r1vit2, which would hold under the assumption that the ðuit1; ait2Þ are independent across t condi-


{591}------------------------------------------------

tional on  $(\mathbf{x}_i, c_{i1}, c_{i2})$ . Then we have

$$y_{ii1} = \mathbf{x}_{ii1} \boldsymbol{\beta}_1 + \rho_1 \mathbf{E}(v_{ii2} \mid \mathbf{x}_i, \mathbf{s}_{i2}) + (c_{i1} + g_{i1}) + e_{ii1} + \rho_1 [v_{ii2} - \mathbf{E}(v_{ii2} \mid \mathbf{x}_i, \mathbf{s}_{i2})]$$

The composite error,  $e_{it1} + \rho_1[v_{it2} - \mathrm{E}(v_{it2} \mid \mathbf{x}_i, \mathbf{s}_{i2})]$ , is uncorrelated with any function of  $(\mathbf{x}_i, \mathbf{s}_{i2})$ . The problem is that  $\mathrm{E}(v_{it2} \mid \mathbf{x}_i, \mathbf{s}_{i2})$  depends on all elements in  $\mathbf{s}_{i2}$ , and this expectation is complicated for even small T.

A method that does work is available using Chamberlain's approach to panel data models, but we need some linearity assumptions on the expected values of  $u_{it1}$  and  $c_{i1}$  given  $\mathbf{x}_i$  and  $v_{it2}$ .

ASSUMPTION 17.7: (a) The selection equation is given by equation (17.53); (b) 
$$E(u_{it1} | \mathbf{x}_i, v_{it2}) = E(u_{it1} | v_{it2}) = \rho_{t1} v_{it2}, t = 1, ..., T$$
; and (c)  $E(c_{i1} | \mathbf{x}_i, v_{it2}) = L(c_{i1} | 1, \mathbf{x}_i, v_{it2})$ 

The second assumption is standard and follows under joint normality of  $(u_{it1}, v_{it2})$  when this vector is independent of  $\mathbf{x}_i$ . Assumption 17.7c implies that

$$\mathbf{E}(c_{i1} \mid \mathbf{x}_i, v_{it2}) = \mathbf{x}_i \boldsymbol{\pi}_1 + \phi_{t1} v_{it2}$$

where, by equation (17.53) and iterated expectations,  $E(c_{i1} | \mathbf{x}_i) = \mathbf{x}_i \boldsymbol{\pi}_1 + E(v_{it2} | \mathbf{x}_{it}) = \mathbf{x}_i \boldsymbol{\pi}_1$ . These assumptions place no restrictions on the serial dependence in  $(u_{it1}, v_{it2})$ . They do imply that

$$E(y_{it1} | \mathbf{x}_i, v_{it2}) = \mathbf{x}_{it1} \boldsymbol{\beta}_1 + \mathbf{x}_i \boldsymbol{\pi}_1 + \gamma_{t1} v_{it2}$$
(17.55)

Conditioning on  $s_{it2} = 1$  gives

$$E(y_{it1} | \mathbf{x}_i, s_{it2} = 1) = \mathbf{x}_{it1} \boldsymbol{\beta}_1 + \mathbf{x}_i \boldsymbol{\pi}_1 + \gamma_{t1} \lambda(\mathbf{x}_i \boldsymbol{\psi}_{t2})$$

Therefore, we can consistently estimate  $\beta_1$  by first estimating a probit of  $s_{it2}$  on  $\mathbf{x}_i$  for each t and then saving the inverse Mills ratio,  $\hat{\lambda}_{it2}$ , all i and t. Next, run the pooled OLS regression using the selected sample:

$$y_{it1}$$
 on  $\mathbf{x}_{it1}, \mathbf{x}_i, \hat{\lambda}_{it2}, d2_t \hat{\lambda}_{it2}, \dots, dT_t \hat{\lambda}_{it2}$  for all  $s_{it} = 1$  (17.56)

where  $d2_t$  through  $dT_t$  are time dummies. If  $\gamma_{t1}$  in equation (17.55) is constant across t, simply include  $\hat{\lambda}_{t2}$  by itself in equation (17.56).

The asymptotic variance of  $\hat{\beta}_1$  needs to be corrected for general heteroskedasticity and serial correlation, as well as first-stage estimation of the  $\psi_{t2}$ . These corrections can be made using the formulas for two-step M-estimation from Chapter 12; Wooldridge (1995a) contains the formulas.

If the selection equation is of the Tobit form, we have somewhat more flexibility. Write the selection equation now as

{592}------------------------------------------------

$$y_{it2} = \max(0, \mathbf{x}_i \psi_{t2} + v_{it2}), \quad v_{it2} \mid \mathbf{x}_i \sim \text{Normal}(0, \sigma_{t2}^2)$$
 (17.57)

where yit<sup>1</sup> is observed if yit<sup>2</sup> > 0. Then, under Assumption 17.6, with the Tobit selection equation in place of equation (17.53), consistent estimation follows from the pooled regression (17.56) where ^lit<sup>2</sup> is replaced by the Tobit residuals, v^it<sup>2</sup> when yit<sup>2</sup> > 0 ðsit<sup>2</sup> ¼ 1Þ. The Tobit residuals are obtained from the T cross section Tobits in equation (17.57); alternatively, especially with small N, we can use a Mundlak-type approach and use pooled Tobit with xi*c*<sup>t</sup><sup>2</sup> replaced with xit*d*<sup>2</sup> þ xi*p*2; see equation (16.52).

It is easy to see that we can add a<sup>1</sup> yit<sup>2</sup> to the structural equation (17.52), provided we make an explicit exclusion restriction in Assumption 17.7. In particular, we must assume that Eðci<sup>1</sup> j xi; vit2Þ ¼ xi1*p*<sup>1</sup> þ f<sup>t</sup>1vit2, and that xit<sup>1</sup> is a strict subset of xit. Then, because yit<sup>2</sup> is a function of ðxi; vit2Þ, we can write Eðyit<sup>1</sup> j xi; vit2Þ ¼ xit1*b*<sup>1</sup> þ a<sup>1</sup> yit<sup>2</sup> þ xi1*p*<sup>1</sup> þ g<sup>t</sup>1vit2. We obtain the Tobit residuals, v^it<sup>2</sup> for each t, and then run the regression yit<sup>1</sup> on xit1; yit2; xi1, and v^it<sup>2</sup> (possibly interacted with time dummies) for the selected sample. If we do not have an exclusion restriction, this regression suffers from perfect multicollinearity. As an example, we can easily include hours worked in a wage offer function for panel data, provided we have a variable affecting labor supply (such as the number of young children) but not the wage offer.

A pure fixed effects approach is more fruitful when the selection equation is of the Tobit form. The following assumption comes from Wooldridge (1995a):

assumption 17.8: (a) The selection equation is equation (17.57). (b) For some unobserved effect gi1, Eðuit<sup>1</sup> j xi; ci1; gi1; vi2Þ ¼ Eðuit<sup>1</sup> j gi1; vit2Þ ¼ gi<sup>1</sup> þ r1vit2.

Under part b of this assumption,

$$E(y_{it1} | \mathbf{x}_i, \mathbf{v}_{i2}, c_{i1}, g_{i1}) = \mathbf{x}_{it1} \boldsymbol{\beta}_1 + \rho_1 v_{it2} + f_{i1}$$
(17.58)

where fi<sup>1</sup> ¼ ci<sup>1</sup> þ gi1. The same expectation holds when we also condition on si<sup>2</sup> (since si<sup>2</sup> is a function of xi, vi2). Therefore, estimating equation (17.58) by fixed effects on the unbalanced panel would consistently estimate *b*<sup>1</sup> and r1. As usual, we replace vit<sup>2</sup> with the Tobit residuals v^it<sup>2</sup> whenever yit<sup>2</sup> > 0. A t test of H0: r<sup>1</sup> ¼ 0 is valid very generally as a test of the null hypothesis of no sample selection. If the fuit1g satisfy the standard homoskedasticity and serial uncorrelatedness assumptions, then the usual t statistic is valid. A fully robust test may be warranted. (Again, with an exclusion restriction, we can add yit<sup>2</sup> as an additional explanatory variable.)

Wooldridge (1995a) discusses an important case where Assumption 17.8b holds: in the Tobit version of equation (17.54) with ðu<sup>i</sup>1; a<sup>i</sup>2Þ independent of ðxi; ci1; ci2Þ and Eðuit<sup>1</sup> j a<sup>i</sup>2Þ ¼ Eðuit<sup>1</sup> j ait2Þ ¼ r1ait2. The second-to-last equality holds under the common assumption that fðuit1; ait2Þ: t ¼ 1; ... ; Tg is serially independent.

{593}------------------------------------------------

The preceding methods assume normality of the errors in the selection equation and, implicitly, the unobserved heterogeneity. Kyriazidou (1997) and Honore´ and Kyriazidou (2000b) have proposed methods that do not require distributional assumptions. Dustmann and Rochina-Barrachina (2000) apply Wooldridge's (1995a) and Kyriazidou's (1997) methods to the problem of estimating a wage offer equation with selection into the work force.