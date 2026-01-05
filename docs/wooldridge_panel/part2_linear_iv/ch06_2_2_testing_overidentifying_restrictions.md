# Testing Overidentifying Restrictions

> Pages: 136-138

When we have more instruments than we need to identify an equation, we can test whether the additional instruments are valid in the sense that they are uncorrelated with u1. To explain the various procedures, write the equation in the form

{137}------------------------------------------------

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \mathbf{y}_2 \boldsymbol{a}_1 + u_1 \tag{6.21}$$

where  $\mathbf{z}_1$  is  $1 \times L_1$  and  $\mathbf{y}_2$  is  $1 \times G_1$ . The  $1 \times L$  vector of all exogenous variables is again  $\mathbf{z}$ ; partition this as  $\mathbf{z} = (\mathbf{z}_1, \mathbf{z}_2)$  where  $\mathbf{z}_2$  is  $1 \times L_2$  and  $L = L_1 + L_2$ . Because the model is overidentified,  $L_2 > G_1$ . Under the usual identification conditions we could use any  $1 \times G_1$  subset of  $\mathbf{z}_2$  as instruments for  $\mathbf{y}_2$  in estimating equation (6.21) (remember the elements of  $\mathbf{z}_1$  act as their own instruments). Following his general principle, Hausman (1978) suggested comparing the 2SLS estimator using all instruments to 2SLS using a subset that just identifies equation (6.21). If all instruments are valid, the estimates should differ only as a result of sampling error. As with testing for endogeneity, constructing the original Hausman statistic is computationally cumbersome. Instead, a simple regression-based procedure is available.

It turns out that, under homoskedasticity, a test for validity of the overidentification restrictions is obtained as  $NR_u^2$  from the OLS regression

$$\hat{u}_1$$
 on  $\mathbf{z}$  (6.22)

where  $\hat{u}_1$  are the 2SLS residuals using *all* of the instruments  $\mathbf{z}$  and  $R_u^2$  is the usual R-squared (assuming that  $\mathbf{z}_1$  and  $\mathbf{z}$  contain a constant; otherwise it is the uncentered R-squared). In other words, simply estimate regression (6.21) by 2SLS and obtain the 2SLS residuals,  $\hat{u}_1$ . Then regress these on all exogenous variables (including a constant). Under the null that  $E(\mathbf{z}'u_1) = \mathbf{0}$  and Assumption 2SLS.3,  $NR_u^2 \stackrel{a}{\sim} \chi_{Q_1}^2$ , where  $Q_1 \equiv L_2 - G_1$  is the number of overidentifying restrictions.

The usefulness of the Hausman test is that, if we reject the null hypothesis, then our logic for choosing the IVs must be reexamined. If we fail to reject the null, then we can have some confidence in the overall set of instruments used. Of course, it could also be that the test has low power for detecting endogeneity of some of the instruments.

A heteroskedasticity-robust version is a little more complicated but is still easy to obtain. Let  $\hat{\mathbf{y}}_2$  denote the fitted values from the first-stage regressions (each element of  $\mathbf{y}_2$  onto  $\mathbf{z}$ ). Now, let  $\mathbf{h}_2$  be any  $1 \times Q_1$  subset of  $\mathbf{z}_2$ . (It does not matter which elements of  $\mathbf{z}_2$  we choose, as long as we choose  $Q_1$  of them.) Regress each element of  $\mathbf{h}_2$  onto  $(\mathbf{z}_1, \hat{\mathbf{y}}_2)$  and collect the residuals,  $\hat{\mathbf{r}}_2$   $(1 \times Q_1)$ . Then an asymptotic  $\chi^2_{Q_1}$  test statistic is obtained as  $N - \mathrm{SSR}_0$  from the regression 1 on  $\hat{u}_1\hat{\mathbf{r}}_2$ . The proof that this method works is very similar to that for the heteroskedasticity-robust test for exclusion restrictions. See Wooldridge (1995b) for details.

Example 6.3 (Overidentifying Restrictions in the Wage Equation): In estimating equation (6.16) by 2SLS, we used (motheduc, fatheduc, huseduc) as instruments for educ. Therefore, there are two overidentifying restrictions. Letting  $\hat{u}_1$  be the 2SLS residuals from equation (6.16) using all instruments, the test statistic is N times the R-squared from the OLS regression

{138}------------------------------------------------

 $\hat{u}_1$  on 1, exper, exper<sup>2</sup>, motheduc, fatheduc, huseduc

Under H<sub>0</sub> and homoskedasticity,  $NR_u^2 \stackrel{a}{\sim} \chi_2^2$ . Using the data on working women in MROZ.RAW gives  $R_u^2 = .0026$ , and so the overidentification test statistic is about 1.11. The *p*-value is about .574, so the overidentifying restrictions are not rejected at any reasonable level.

For the heteroskedasticity-robust version, one approach is to obtain the residuals,  $\hat{r}_1$  and  $\hat{r}_2$ , from the OLS regressions motheduc on 1, exper, exper<sup>2</sup>, and educ and fatheduc on 1, exper, exper<sup>2</sup>, and educ, where educ are the first-stage fitted values from the regression educ on 1, exper, exper<sup>2</sup>, motheduc, fatheduc, and huseduc. Then obtain N-SSR from the OLS regression 1 on  $\hat{u}_1 \cdot \hat{r}_1$ ,  $\hat{u}_1 \cdot \hat{r}_2$ . Using only the 428 observations on working women to obtain  $\hat{r}_1$  and  $\hat{r}_2$ , the value of the robust test statistic is about 1.04 with p-value = .595, which is similar to the p-value for the nonrobust test.