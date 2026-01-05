# Fixed Effects versus First Differencing

> Pages: 296-300

When we have only two time periods, fixed effects estimation and first differencing produce identical estimates and inference, as you are asked to show in Problem 10.3. First differencing is easier to implement, and all procedures that can be applied to a single cross section—such as heteroskedasticity-robust inference—can be applied directly.

When T > 2, the choice between FD and FE hinges on the assumptions about the idiosyncratic errors, uit. In particular, the FE estimator is more efficient under Assumption FE.3—the uit are serially uncorrelated—while the FD estimator is more efficient when uit follows a random walk. In many cases, the truth is likely to lie somewhere in between.

If FE and FD estimates differ in ways that cannot be attributed to sampling error, we should worry about the strict exogeneity assumption. If uit is correlated with xis for any t and s, FE and FD generally have different probability limits. Any of the standard endogeneity problems, including measurement error, time-varying omitted variables, and simultaneity, generally cause correlation between xit and uit—that is, contemporaneous correlation—which then causes both FD and FE to be inconsistent and to have different probability limits. (We explicitly consider these problems in 

{297}------------------------------------------------

Chapter 11.) In addition, correlation between  $u_{it}$  and  $\mathbf{x}_{is}$  for  $s \neq t$  causes FD and FE to be inconsistent. When lagged  $\mathbf{x}_{it}$  is correlated with  $u_{it}$ , we can solve lack of strict exogeneity by including lags and interpreting the equation as a distributed lag model. More problematical is when  $u_{it}$  is correlated with *future*  $\mathbf{x}_{it}$ : only rarely does putting future values of explanatory variables in an equation lead to an interesting economic model. In Chapter 11 we show how to estimate the parameters consistently when there is feedback from  $u_{it}$  to  $\mathbf{x}_{is}$ , s > t.

We can formally test the assumptions underlying the consistency of the FE and FD estimators by using a Hausman test. It might be important to use a robust form of the Hausman test that maintains neither Assumption FE.3 nor Assumption FD.3 under the null hypothesis. This approach is not difficult—see Problem 10.6—but we focus here on regression-based tests, which are easier to compute.

If T=2, it is easy to test for strict exogeneity. In the equation  $\Delta y_i = \Delta \mathbf{x}_i \boldsymbol{\beta} + \Delta u_i$ , neither  $\mathbf{x}_{i1}$  nor  $\mathbf{x}_{i2}$  should be significant as additional explanatory variables in the first-differenced equation. We simply add, say,  $\mathbf{x}_{i2}$  to the FD equation and carry out an F test for significance of  $\mathbf{x}_{i2}$ . With more than two time periods, a test of strict exogeneity is a test of  $H_0$ :  $\gamma = 0$  in the expanded equation

$$\Delta y_t = \Delta \mathbf{x}_t \boldsymbol{\beta} + \mathbf{w}_t \boldsymbol{\gamma} + \Delta u_t, \qquad t = 2, \dots, T$$

where  $\mathbf{w}_t$  is a subset of  $\mathbf{x}_t$  (that would exclude time dummies). Using the Wald approach, this test can be made robust to arbitrary serial correlation or heteroskedasticity; under Assumptions FD.1–FD.3 the usual F statistic is asymptotically valid.

A test of strict exogeneity using fixed effects, when T > 2, is obtained by specifying the equation

$$y_{it} = \mathbf{x}_{it} \boldsymbol{\beta} + \mathbf{w}_{i,t+1} \boldsymbol{\delta} + c_i + u_{it}, \qquad t = 1, 2, \dots, T - 1$$

where  $\mathbf{w}_{i,t+1}$  is again a subset of  $\mathbf{x}_{i,t+1}$ . Under strict exogeneity,  $\boldsymbol{\delta} = \mathbf{0}$ , and we can carry out the test using fixed effects estimation. (We lose the last time period by leading  $\mathbf{w}_{it}$ .) An example is given in Problem 10.12.

Under strict exogeneity, we can use a GLS procedure on either the time-demeaned equation or the first-differenced equation. If the variance matrix of  $\mathbf{u}_i$  is unrestricted, it does not matter which transformation we use. Intuitively, this point is pretty clear, since allowing  $E(\mathbf{u}_i\mathbf{u}_i')$  to be unrestricted places no restrictions on  $E(\ddot{\mathbf{u}}_i\ddot{\mathbf{u}}_i')$  or  $E(\Delta\mathbf{u}_i\Delta\mathbf{u}_i')$ . Im, Ahn, Schmidt, and Wooldridge (1999) show formally that the FEGLS and FDGLS estimators are asymptotically equivalent under Assumptions FE.1 and FEGLS.3 and the appropriate rank conditions.

{298}------------------------------------------------

#### 10.7.2 The Relationship between the Random Effects and Fixed Effects Estimators

In cases where the key variables in  $\mathbf{x}_t$  do not vary much over time, fixed effects and first-differencing methods can lead to imprecise estimates. We may be forced to use random effects estimation in order to learn anything about the population parameters. If a random effects analysis is appropriate—that is, if  $c_i$  is orthogonal to  $\mathbf{x}_{it}$ —then the random effects estimators can have much smaller variances than the FE or FD estimators. We now obtain an expression for the RE estimator that allows us to compare it with the FE estimator.

Using the fact that  $\mathbf{j}_T'\mathbf{j}_T = T$ , we can write  $\Omega$  under the random effects structure as

$$\begin{aligned} \mathbf{\Omega} &= \sigma_u^2 \mathbf{I}_T + \sigma_c^2 \mathbf{j}_T \mathbf{j}_T' = \sigma_u^2 \mathbf{I}_T + T \sigma_c^2 \mathbf{j}_T (\mathbf{j}_T' \mathbf{j}_T)^{-1} \mathbf{j}_T' \\ &= \sigma_u^2 \mathbf{I}_T + T \sigma_c^2 \mathbf{P}_T = (\sigma_u^2 + T \sigma_c^2) (\mathbf{P}_T + \eta \mathbf{Q}_T) \end{aligned}$$

where  $\mathbf{P}_T \equiv \mathbf{I}_T - \mathbf{Q}_T = \mathbf{j}_T (\mathbf{j}_T' \mathbf{j}_T)^{-1} \mathbf{j}_T'$  and  $\eta \equiv \sigma_u^2/(\sigma_u^2 + T\sigma_c^2)$ . Next, define  $\mathbf{S}_T \equiv \mathbf{P}_T + \eta \mathbf{Q}_T$ . Then  $\mathbf{S}_T^{-1} = \mathbf{P}_T + (1/\eta)\mathbf{Q}_T$ , as can be seen by direct matrix multiplication. Further,  $\mathbf{S}_T^{-1/2} = \mathbf{P}_T + (1/\sqrt{\eta})\mathbf{Q}_T$ , because multiplying this matrix by itself gives  $\mathbf{S}_T^{-1}$  (the matrix is clearly symmetric, since  $\mathbf{P}_T$  and  $\mathbf{Q}_T$  are symmetric). After simple algebra, it can be shown that  $\mathbf{S}_T^{-1/2} = (1-\lambda)^{-1}[\mathbf{I}_T - \lambda \mathbf{P}_T]$ , where  $\lambda = 1 - \sqrt{\eta}$ . Therefore,

$$\mathbf{\Omega}^{-1/2} = (\sigma_u^2 + T\sigma_c^2)^{-1/2} (1 - \lambda)^{-1} [\mathbf{I}_T - \lambda \mathbf{P}_T] = (1/\sigma_u) [\mathbf{I}_T - \lambda \mathbf{P}_T]$$

where  $\lambda = 1 - [\sigma_u^2/(\sigma_u^2 + T\sigma_c^2)]^{1/2}$ . Assume for the moment that we know  $\lambda$ . Then the RE estimator is obtained by estimating the transformed equation  $\mathbf{C}_T \mathbf{y}_i = \mathbf{C}_T \mathbf{X}_i \boldsymbol{\beta} + \mathbf{C}_T \mathbf{v}_i$  by system OLS, where  $\mathbf{C}_T \equiv [\mathbf{I}_T - \lambda \mathbf{P}_T]$ . Write the transformed equation as

$$\dot{\mathbf{y}}_i = \dot{\mathbf{X}}_i \boldsymbol{\beta} + \dot{\mathbf{v}}_i \tag{10.74}$$

The variance matrix of  $\check{\mathbf{v}}_i$  is  $\mathrm{E}(\check{\mathbf{v}}_i\check{\mathbf{v}}_i') = \mathbf{C}_T\mathbf{\Omega}\mathbf{C}_T = \sigma_u^2\mathbf{I}_T$ , which verifies that  $\check{\mathbf{v}}_i$  has variance matrix ideal for system OLS estimation.

The th element of  $\check{\mathbf{y}}_i$  is easily seen to be  $y_{it} - \lambda \bar{y}_i$ , and similarly for  $\check{\mathbf{X}}_i$ . Therefore, system OLS estimation of equation (10.74) is just pooled OLS estimation of

$$y_{it} - \lambda \overline{y}_i = (\mathbf{x}_{it} - \lambda \overline{\mathbf{x}}_i) \boldsymbol{\beta} + (v_{it} - \lambda \overline{v}_i)$$

over all t and i. The errors in this equation are serially uncorrelated and homoskedastic under Assumption RE.3; therefore, they satisfy the key conditions for pooled OLS analysis. The feasible RE estimator replaces the unknown  $\lambda$  with its estimator,  $\hat{\lambda}$ , so that  $\hat{\beta}_{RE}$  can be computed from the pooled OLS regression

$$\check{y}_{it} \text{ on } \check{\mathbf{x}}_{it}, \qquad t = 1, \dots, T; i = 1, \dots, N$$
(10.75)

{299}------------------------------------------------

where now  $\mathbf{\check{x}}_{it} = \mathbf{x}_{it} - \hat{\lambda}\mathbf{\bar{x}}_i$  and  $\mathbf{\check{y}}_{it} = y_{it} - \hat{\lambda}\mathbf{\bar{y}}_i$ , all t and i. Therefore, we can write

$$\hat{\boldsymbol{\beta}}_{RE} = \left(\sum_{i=1}^{N} \sum_{t=1}^{T} \check{\mathbf{x}}_{it}' \check{\mathbf{x}}_{it}\right)^{-1} \left(\sum_{i=1}^{N} \sum_{t=1}^{T} \check{\mathbf{x}}_{it}' \check{y}_{it}\right)$$
(10.76)

The usual variance estimate from the pooled OLS regression (10.75), SSR/(NT - K), is a consistent estimator of  $\sigma_u^2$ . The usual t statistics and F statistics from the pooled regression are asymptotically valid under Assumptions RE.1–RE.3. For F tests, we obtain  $\hat{\lambda}$  from the unrestricted model.

Equation (10.76) shows that the random effects estimator is obtained by a **quasitime demeaning**: rather than removing the time average from the explanatory and dependent variables at each t, random effects removes a fraction of the time average. If  $\hat{\lambda}$  is close to unity, the random effects and fixed effects estimates tend to be close. To see when this result occurs, write  $\hat{\lambda}$  as

$$\hat{\lambda} = 1 - \{1/[1 + T(\hat{\sigma}_c^2/\hat{\sigma}_u^2)]\}^{1/2} \tag{10.77}$$

where  $\hat{\sigma}_u^2$  and  $\hat{\sigma}_c^2$  are consistent estimators of  $\sigma_u^2$  and  $\sigma_c^2$  (see Section 10.4). When  $T(\hat{\sigma}_c^2/\hat{\sigma}_u^2)$  is large, the second term in  $\hat{\lambda}$  is small, in which case  $\hat{\lambda}$  is close to unity. In fact,  $\hat{\lambda} \to 1$  as  $T \to \infty$  or as  $\hat{\sigma}_c^2/\hat{\sigma}_u^2 \to \infty$ . For large T, it is not surprising to find similar estimates from fixed effects and random effects. Even with small T, random effects can be close to fixed effects if the estimated variance of  $c_i$  is large relative to the estimated variance of  $u_{it}$ , a case often relevant for applications. (As  $\lambda$  approaches unity, the precision of the random effects estimator approaches that of the fixed effects estimator, and the effects of time-constant explanatory variables become harder to estimate.)

Example 10.7 (Job Training Grants): In Example 10.4, T = 3,  $\hat{\sigma}_u^2 \approx .248$ , and  $\hat{\sigma}_c^2 \approx 1.932$ , which gives  $\hat{\lambda} \approx .797$ . This helps explain why the RE and FE estimates are reasonably close.

Equations (10.76) and (10.77) also show how random effects and pooled OLS are related. Pooled OLS is obtained by setting  $\hat{\lambda} = 0$ , which is never exactly true but could be close. In practice,  $\hat{\lambda}$  is not usually close to zero because this outcome would require  $\hat{\sigma}_u^2$  to be large relative to  $\hat{\sigma}_c^2$ .

In Section 10.4 we emphasized that consistency of random effects hinges on the orthogonality between  $c_i$  and  $\mathbf{x}_{it}$ . In fact, Assumption POLS.1 is weaker than Assumption RE.1. We now see, because of the particular transformation used by the RE estimator, that its inconsistency when Assumption RE.1b is violated can be small relative to pooled OLS if  $\sigma_c^2$  is large relative to  $\sigma_u^2$  or if T is large.

{300}------------------------------------------------

If we are primarily interested in the effect of a time-constant variable in a panel data study, the robustness of the FE estimator to correlation between the unobserved effect and the xit is practically useless. Without using an instrumental variables approach—something we take up in Chapter 11—random effects is probably our only choice. Sometimes, applications of the RE estimator attempt to control for the part of ci correlated with xit by including dummy variables for various groups, assuming that we have many observations within each group. For example, if we have panel data on a group of working people, we might include city dummy variables in a wage equation. Or, if we have panel data at the student level, we might include school dummy variables. Including dummy variables for groups controls for a certain amount of heterogeneity that might be correlated with the (time-constant) elements of xit. By using RE, we can efficiently account for any remaining serial correlation due to unobserved time-constant factors. (Unfortunately, the language used in empirical work can be confusing. It is not uncommon to see school dummy variables referred to as ''school fixed effects'' even though they appear in a random effects analysis at the individual level.)

Regression (10.75) using the quasi-time-demeaned data has several other practical uses. Since it is just a pooled OLS regression that is asymptotically the same as using l in place of ^l, we can easily obtain standard errors that are robust to arbitrary heteroskedasticity in ci and uit as well as arbitrary serial correlation in the fuitg. All that is required is an econometrics package that computes robust standard errors, t, and F statistics for pooled OLS regression, such as Stata*9*. Further, we can use the residuals from regression (10.75), say ^rit, to test for serial correlation in rit 1vit lvi, which are serially uncorrelated under Assumption RE.3a. If we detect serial correlation in fritg, we conclude that Assumption RE.3a is false, and this result means that the uit are serially correlated. Although the arguments are tedious, it can be shown that estimation of l and *b* has no effect on the null limiting distribution of the usual (or heteroskedasticity-robust) t statistic from the pooled OLS regression ^rit on ^ri;t1, t ¼ 2; ... ; T; i ¼ 1; ... ; N.