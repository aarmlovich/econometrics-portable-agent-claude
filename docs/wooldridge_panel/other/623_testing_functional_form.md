# **6.2.3 Testing Functional Form**

> Pages: 138-142

Sometimes we need a test with power for detecting neglected nonlinearities in models estimated by OLS or 2SLS. A useful approach is to add nonlinear functions, such as squares and cross products, to the original model. This approach is easy when all explanatory variables are exogenous: F statistics and LM statistics for exclusion restrictions are easily obtained. It is a little tricky for models with endogenous explanatory variables because we need to choose instruments for the additional nonlinear functions of the endogenous variables. We postpone this topic until Chapter 9 when we discuss simultaneous equation models. See also Wooldridge (1995b).

Putting in squares and cross products of all exogenous variables can consume many degrees of freedom. An alternative is Ramsey's (1969) RESET, which has degrees of freedom that do not depend on *K*. Write the model as

$$y = \mathbf{x}\boldsymbol{\beta} + u \tag{6.23}$$

$$\mathbf{E}(u\,|\,\mathbf{x}) = 0\tag{6.24}$$

[You should convince yourself that it makes no sense to test for functional form if we only assume that  $E(\mathbf{x}'u) = \mathbf{0}$ . If equation (6.23) defines a linear projection, then, by definition, functional form is not an issue.] Under condition (6.24) we know that any function of  $\mathbf{x}$  is uncorrelated with u (hence the previous suggestion of putting squares and cross products of  $\mathbf{x}$  as additional regressors). In particular, if condition (6.24) holds, then  $(\mathbf{x}\boldsymbol{\beta})^p$  is uncorrelated with u for any integer p. Since  $\boldsymbol{\beta}$  is not observed, we replace it with the OLS estimator,  $\hat{\boldsymbol{\beta}}$ . Define  $\hat{y}_i = \mathbf{x}_i \hat{\boldsymbol{\beta}}$  as the OLS fitted values and  $\hat{u}_i$  as the OLS residuals. By definition of OLS, the sample covariance between  $\hat{u}_i$  and  $\hat{y}_i$  is zero. But we can test whether the  $\hat{u}_i$  are sufficiently correlated with low-order poly-

{139}------------------------------------------------

nomials in  $\hat{y}_i$ , say  $\hat{y}_i^2$ ,  $\hat{y}_i^3$ , and  $\hat{y}_i^4$ , as a test for neglected nonlinearity. There are a couple of ways to do so. Ramsey suggests adding these terms to equation (6.23) and doing a standard F test [which would have an approximate  $\mathcal{F}_{3,N-K-3}$  distribution under equation (6.23) and the homoskedasticity assumption  $E(u^2 | \mathbf{x}) = \sigma^2$ ]. Another possibility is to use an LM test: Regress  $\hat{u}_i$  onto  $\mathbf{x}_i$ ,  $\hat{y}_i^2$ ,  $\hat{y}_i^3$ , and  $\hat{y}_i^4$  and use N times the R-squared from this regression as  $\chi_3^2$ . The methods discussed in Chapter 4 for obtaining heteroskedasticity-robust statistics can be applied here as well. Ramsey's test uses generated regressors, but the null is that each generated regressor has zero population coefficient, and so the usual limit theory applies. (See Section 6.1.1.)

There is some misunderstanding in the testing literature about the merits of RESET. It has been claimed that RESET can be used to test for a multitude of specification problems, including omitted variables and heteroskedasticity. In fact, RESET is generally a poor test for either of these problems. It is easy to write down models where an omitted variable, say q, is highly correlated with each  $\mathbf{x}$ , but RESET has the same distribution that it has under  $H_0$ . A leading case is seen when  $E(q \mid \mathbf{x})$  is linear in  $\mathbf{x}$ . Then  $E(y \mid \mathbf{x})$  is linear in  $\mathbf{x}$  [even though  $E(y \mid \mathbf{x}) \neq E(y \mid \mathbf{x}, q)$ ], and the asymptotic power of RESET equals its asymptotic size. See Wooldridge (1995b) and Problem 6.4a. The following is an empirical illustration.

Example 6.4 (Testing for Neglected Nonlinearities in a Wage Equation): We use OLS and the data in NLS80.RAW to estimate the equation from Example 4.3:

$$\begin{split} \log(wage) &= \beta_0 + \beta_1 exper + \beta_2 tenure + \beta_3 married + \beta_4 south \\ &+ \beta_5 urban + \beta_6 black + \beta_7 educ + u \end{split}$$

The null hypothesis is that the expected value of u given the explanatory variables in the equation is zero. The R-squared from the regression  $\hat{u}$  on  $\mathbf{x}$ ,  $\hat{y}^2$ , and  $\hat{y}^3$  yields  $R_u^2 = .0004$ , so the chi-square statistic is .374 with p-value  $\approx$  .83. (Adding  $\hat{y}^4$  only increases the p-value.) Therefore, RESET provides no evidence of functional form misspecification.

Even though we already know IQ shows up very significantly in the equation (t statistic = 3.60—see Example 4.3), RESET does not, and should not be expected to, detect the omitted variable problem. It can only test whether the expected value of y given the variables actually in the regression is linear in those variables.

#### **6.2.4** Testing for Heteroskedasticity

As we have seen for both OLS and 2SLS, heteroskedasticity does not affect the consistency of the estimators, and it is only a minor nuisance for inference. Nevertheless, sometimes we want to test for the presence of heteroskedasticity in order to justify use

{140}------------------------------------------------

of the usual OLS or 2SLS statistics. If heteroskedasticity is present, more efficient estimation is possible.

We begin with the case where the explanatory variables are exogenous in the sense that u has zero mean given x:

$$y = \beta_0 + \mathbf{x}\boldsymbol{\beta} + u, \qquad \mathbf{E}(u \mid \mathbf{x}) = 0$$

The reason we do not assume the weaker assumption  $E(\mathbf{x}'u) = \mathbf{0}$  is that the following class of tests we derive—which encompasses all of the widely used tests for heteroskedasticity—are not valid unless  $E(u | \mathbf{x}) = 0$  is maintained under  $H_0$ . Thus we maintain that the mean  $E(y | \mathbf{x})$  is correctly specified, and then we test the constant conditional variance assumption. If we do not assume correct specification of  $E(y | \mathbf{x})$ , a significant heteroskedasticity test might just be detecting misspecified functional form in  $E(y | \mathbf{x})$ ; see Problem 6.4c.

Because  $E(u \mid \mathbf{x}) = 0$ , the null hypothesis can be stated as  $H_0$ :  $E(u^2 \mid \mathbf{x}) = \sigma^2$ . Under the alternative,  $E(u^2 \mid \mathbf{x})$  depends on  $\mathbf{x}$  in some way. Thus it makes sense to test  $H_0$  by looking at covariances

$$Cov[\mathbf{h}(\mathbf{x}), u^2] \tag{6.25}$$

for some  $1 \times Q$  vector function  $\mathbf{h}(\mathbf{x})$ . Under  $H_0$ , the covariance in expression (6.25) should be zero for any choice of  $\mathbf{h}(\cdot)$ .

Of course a general way to test zero correlation is to use a regression. Putting *i* subscripts on the variables, write the model

$$u_i^2 = \delta_0 + \mathbf{h}_i \boldsymbol{\delta} + v_i \tag{6.26}$$

where  $\mathbf{h}_i \equiv \mathbf{h}(\mathbf{x}_i)$ ; we make the standard rank assumption that  $\operatorname{Var}(\mathbf{h}_i)$  has rank Q, so that there is no perfect collinearity in  $\mathbf{h}_i$ . Under  $H_0$ ,  $\mathrm{E}(v_i \mid \mathbf{h}_i) = \mathrm{E}(v_i \mid \mathbf{x}_i) = 0$ ,  $\boldsymbol{\delta} = \mathbf{0}$ , and  $\delta_0 = \sigma^2$ . Thus we can apply an F test or an LM test for the null  $H_0$ :  $\boldsymbol{\delta} = \mathbf{0}$  in equation (6.26). One thing to notice is that  $v_i$  cannot have a normal distribution under  $H_0$ : because  $v_i = u_i^2 - \sigma^2$ ,  $v_i \geq -\sigma^2$ . This does not matter for asymptotic analysis; the OLS regression from equation (6.26) gives a consistent,  $\sqrt{N}$ -asymptotically normal estimator of  $\boldsymbol{\delta}$  whether or not  $H_0$  is true. But to apply a standard F or LM test, we must assume that, under  $H_0$ ,  $\mathrm{E}(v_i^2 \mid \mathbf{x}_i)$  is constant: that is, the errors in equation (6.26) are homoskedastic. In terms of the original error  $u_i$ , this assumption implies that

$$E(u_i^4 \mid \mathbf{x}_i) = constant \equiv \kappa^2 \tag{6.27}$$

under  $H_0$ . This is called the **homokurtosis** (constant conditional fourth moment) assumption. Homokurtosis always holds when u is independent of  $\mathbf{x}$ , but there are


{141}------------------------------------------------

conditional distributions for which  $E(u \mid \mathbf{x}) = 0$  and  $Var(u \mid \mathbf{x}) = \sigma^2$  but  $E(u^4 \mid \mathbf{x})$  depends on  $\mathbf{x}$ .

As a practical matter, we cannot test  $\delta = 0$  in equation (6.26) directly because  $u_i$  is not observed. Since  $u_i = y_i - \mathbf{x}_i \boldsymbol{\beta}$  and we have a consistent estimator of  $\boldsymbol{\beta}$ , it is natural to replace  $u_i^2$  with  $\hat{u}_i^2$ , where the  $\hat{u}_i$  are the OLS residuals for observation *i*. Doing this step and applying, say, the LM principle, we obtain  $NR_c^2$  from the regression

$$\hat{u}_i^2 \text{ on } 1, \mathbf{h}_i, \qquad i = 1, 2, \dots, N$$
 (6.28)

where  $R_c^2$  is just the usual centered *R*-squared. Now, if the  $u_i^2$  were used in place of the  $\hat{u}_i^2$ , we know that, under H<sub>0</sub> and condition (6.27),  $NR_c^2 \stackrel{i}{\sim} \chi_Q^2$ , where *Q* is the dimension of  $\mathbf{h}_i$ .

What adjustment is needed because we have estimated  $u_i^2$ ? It turns out that, because of the structure of these tests, no adjustment is needed to the asymptotics. (This statement is not generally true for regressions where the dependent variable has been estimated in a first stage; the current setup is special in that regard.) After tedious algebra, it can be shown that

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{h}_{i}'(\hat{\mathbf{u}}_{i}^{2} - \hat{\boldsymbol{\sigma}}^{2}) = N^{-1/2} \sum_{i=1}^{N} (\mathbf{h}_{i} - \boldsymbol{\mu}_{h})'(u_{i}^{2} - \boldsymbol{\sigma}^{2}) + o_{p}(1)$$
(6.29)

see Problem 6.5. Along with condition (6.27), this equation can be shown to justify the  $NR_c^2$  test from regression (6.28).

Two popular tests are special cases. Koenker's (1981) version of the Breusch and Pagan (1979) test is obtained by taking  $\mathbf{h}_i \equiv \mathbf{x}_i$ , so that Q = K. [The original version of the Breusch-Pagan test relies heavily on normality of the  $u_i$ , in particular  $\kappa^2 = 3\sigma^2$ , so that Koenker's version based on  $NR_c^2$  in regression (6.28) is preferred.] White's (1980b) test is obtained by taking  $\mathbf{h}_i$  to be all nonconstant, unique elements of  $\mathbf{x}_i$  and  $\mathbf{x}_i'\mathbf{x}_i$ : the levels, squares, and cross products of the regressors in the conditional mean.

The Breusch-Pagan and White tests have degrees of freedom that depend on the number of regressors in  $E(y | \mathbf{x})$ . Sometimes we want to conserve on degrees of freedom. A test that combines features of the Breusch-Pagan and White tests, but which has only two dfs, takes  $\hat{\mathbf{h}}_i \equiv (\hat{y}_i, \hat{y}_i^2)$ , where the  $\hat{y}_i$  are the OLS fitted values. (Recall that these are linear functions of the  $\mathbf{x}_i$ .) To justify this test, we must be able to replace  $\mathbf{h}(\mathbf{x}_i)$  with  $\mathbf{h}(\mathbf{x}_i, \hat{\boldsymbol{\beta}})$ . We discussed the generated regressors problem for OLS in Section 6.1.1 and concluded that, for *testing* purposes, using estimates from earlier stages causes no complications. This is the case here as well:  $NR_c^2$  from  $\hat{u}_i^2$  on 1,  $\hat{y}_i$ ,  $\hat{y}_i^2$ ,  $i = 1, 2, \ldots, N$  has a limiting  $\chi_2^2$  distribution under the null, along with condition (6.27). This is easily seen to be a special case of the White test because  $(\hat{y}_i, \hat{y}_i^2)$  contains two linear combinations of the squares and cross products of all elements in  $\mathbf{x}_i$ .

{142}------------------------------------------------

A simple modification is available for relaxing the auxiliary homokurtosis assumption (6.27). Following the work of Wooldridge (1990)—or, working directly from the representation in equation (6.29), as in Problem 6.5—it can be shown that  $N - \text{SSR}_0$  from the regression (without a constant)

1 on 
$$(\mathbf{h}_i - \bar{\mathbf{h}})(\hat{\mathbf{u}}_i^2 - \hat{\sigma}^2), \qquad i = 1, 2, \dots, N$$
 (6.30)

is distributed asymptotically as  $\chi_Q^2$  under H<sub>0</sub> [there are Q regressors in regression (6.30)]. This test is very similar to the heteroskedasticity-robust LM statistics derived in Chapter 4. It is sometimes called a **heterokurtosis-robust test** for heteroskedasticity.

If we allow some elements of  $\mathbf{x}_i$  to be endogenous but assume we have instruments  $\mathbf{z}_i$  such that  $\mathrm{E}(u_i \,|\, \mathbf{z}_i) = 0$  and the rank condition holds, then we can test  $\mathrm{H}_0$ :  $\mathrm{E}(u_i^2 \,|\, \mathbf{z}_i) = \sigma^2$  (which implies Assumption 2SLS.3). Let  $\mathbf{h}_i \equiv \mathbf{h}(\mathbf{z}_i)$  be a  $1 \times Q$  function of the exogenous variables. The statistics are computed as in either regression (6.28) or (6.30), depending on whether the homokurtosis is maintained, where the  $\hat{u}_i$  are the 2SLS residuals. There is, however, one caveat. For the validity of the asymptotic variances that these regressions implicitly use, an additional assumption is needed under  $\mathrm{H}_0$ :  $\mathrm{Cov}(\mathbf{x}_i, u_i \,|\, \mathbf{z}_i)$  must be constant. This covariance is zero when  $\mathbf{z}_i = \mathbf{x}_i$ , so there is no additional assumption when the regressors are exogenous. Without the assumption of constant conditional covariance, the tests for heteroskedasticity are more complicated. For details, see Wooldridge (1990).

You should remember that  $\mathbf{h}_i$  (or  $\hat{\mathbf{h}}_i$ ) must only be a function of exogenous variables and estimated parameters; it should not depend on endogenous elements of  $\mathbf{x}_i$ . Therefore, when  $\mathbf{x}_i$  contains endogenous variables, it is *not* valid to use  $\mathbf{x}_i\hat{\boldsymbol{\beta}}$  and  $(\mathbf{x}_i\hat{\boldsymbol{\beta}})^2$  as elements of  $\hat{\mathbf{h}}_i$ . It is valid to use, say,  $\hat{\mathbf{x}}_i\hat{\boldsymbol{\beta}}$  and  $(\hat{\mathbf{x}}_i\hat{\boldsymbol{\beta}})^2$ , where the  $\hat{\mathbf{x}}_i$  are the first-stage fitted values from regressing  $\mathbf{x}_i$  on  $\mathbf{z}_i$ .