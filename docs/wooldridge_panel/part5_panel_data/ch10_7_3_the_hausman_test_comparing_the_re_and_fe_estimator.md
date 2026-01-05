# The Hausman Test Comparing the RE and FE Estimators

> Pages: 300-303

Since the key consideration in choosing between a random effects and fixed effects approach is whether ci and xit are correlated, it is important to have a method for testing this assumption. Hausman (1978) proposed a test based on the difference between the random effects and fixed effects estimates. Since FE is consistent when ci and xit are correlated, but RE is inconsistent, a statistically significant difference is interpreted as evidence against the random effects assumption RE.1b.


{301}------------------------------------------------

Before we obtain the Hausman test, there are two caveats. First, strict exogeneity, Assumption RE.1a, is maintained under the null and the alternative. Correlation between  $\mathbf{x}_{is}$  and  $u_{it}$  for any s and t causes both FE and RE to be inconsistent, and generally their plims will differ.

A second caveat is that the test is usually implemented assuming that Assumption RE.3 holds under the null. As we will see, this setup implies that the random effects estimator is more efficient than the FE estimator, and it simplifies computation of the test statistic. But we must emphasize that Assumption RE.3 is an auxiliary assumption, and it is *not* being tested by the Hausman statistic: the Hausman test has no systematic power against the alternative that Assumption RE.1 is true but Assumption RE.3 is false. Failure of Assumption RE.3 causes the usual Hausman test to have a nonstandard limiting distribution, which means the resulting test could have asymptotic size larger or smaller than the nominal size.

Assuming that Assumptions RE.1–RE.3 hold, consider the case where  $\mathbf{x}_{it}$  contains only time-varying elements, since these are the only coefficients that we can estimate using fixed effects. Then

$$\operatorname{Avar}(\hat{\boldsymbol{\beta}}_{FE}) = \sigma_u^2 [\operatorname{E}(\ddot{\mathbf{X}}_i' \ddot{\mathbf{X}}_i)]^{-1} / N \quad \text{and} \quad \operatorname{Avar}(\hat{\boldsymbol{\beta}}_{RE}) = \sigma_u^2 [\operatorname{E}(\check{\mathbf{X}}_i' \check{\mathbf{X}}_i)]^{-1} / N$$

where the tth row of  $\ddot{\mathbf{X}}_i$  is  $\mathbf{x}_{it} - \overline{\mathbf{x}}_i$  and the tth row of  $\dot{\mathbf{X}}_i$  is  $\mathbf{x}_{it} - \lambda \overline{\mathbf{x}}_i$ . Now

$$E(\check{\mathbf{X}}_{i}'\check{\mathbf{X}}_{i}) - E(\ddot{\mathbf{X}}_{i}'\ddot{\mathbf{X}}_{i}) = E[\mathbf{X}_{i}'(\mathbf{I}_{T} - \lambda \mathbf{P}_{T})\mathbf{X}_{i}] - E[\mathbf{X}_{i}'(\mathbf{I}_{T} - \mathbf{P}_{T})\mathbf{X}_{i}]$$
$$= (1 - \lambda)E(\mathbf{X}_{i}'\mathbf{P}_{T}\mathbf{X}_{i}) = (1 - \lambda)TE(\bar{\mathbf{x}}_{i}'\bar{\mathbf{x}}_{i})$$

from which it follows that  $[\operatorname{Avar}(\hat{\boldsymbol{\beta}}_{RE})]^{-1} - [\operatorname{Avar}(\hat{\boldsymbol{\beta}}_{FE})]^{-1}$  is positive definite, implying that  $\operatorname{Avar}(\hat{\boldsymbol{\beta}}_{FE}) - \operatorname{Avar}(\hat{\boldsymbol{\beta}}_{RE})$  is positive definite. Since  $\lambda \to 1$  as  $T \to \infty$ , these expressions show that the asymptotic variance of the RE estimator tends to that of FE as T gets large.

The original form of the Hausman statistic can be computed as follows. Let  $\hat{\delta}_{RE}$  denote the vector of random effects estimates without the coefficients on time-constant variables or aggregate time variables, and let  $\hat{\delta}_{FE}$  denote the corresponding fixed effects estimates; let these each be  $M \times 1$  vectors. Then

$$H = (\hat{\boldsymbol{\delta}}_{FE} - \hat{\boldsymbol{\delta}}_{RE})'[\operatorname{Avar}(\hat{\boldsymbol{\delta}}_{FE}) - \operatorname{Avar}(\hat{\boldsymbol{\delta}}_{RE})]^{-1}(\hat{\boldsymbol{\delta}}_{FE} - \hat{\boldsymbol{\delta}}_{RE})$$
(10.78)

is distributed asymptotically as  $\chi_M^2$  under Assumptions RE.1–RE.3. A key to establishing the limiting chi-square distribution of H is to show that  $\operatorname{Avar}[\sqrt{N}(\hat{\boldsymbol{\delta}}_{FE}-\hat{\boldsymbol{\delta}}_{RE})]$  =  $\operatorname{Avar}[\sqrt{N}(\hat{\boldsymbol{\delta}}_{FE}-\boldsymbol{\delta})]$  -  $\operatorname{Avar}[\sqrt{N}(\hat{\boldsymbol{\delta}}_{RE}-\boldsymbol{\delta})]$ . Newey and McFadden (1994, Section 5.3) provide general sufficient conditions, which are met by the FE and RE estimators under Assumptions RE.1–RE.3. (We cover these conditions in Chapter 14 in our

{302}------------------------------------------------

discussion of general efficiency issues; see Lemma 14.1 and the surrounding discussion.) The usual estimators of  $\text{Avar}(\hat{\boldsymbol{\delta}}_{FE})$  and  $\text{Avar}(\hat{\boldsymbol{\delta}}_{RE})$  can be used in equation (10.78), but if different estimates of  $\sigma_u^2$  are used, the matrix  $\text{Avar}(\hat{\boldsymbol{\delta}}_{FE}) - \text{Avar}(\hat{\boldsymbol{\delta}}_{RE})$  need not be positive definite. Thus it is best to use either the fixed effects estimate or the random effects estimate of  $\sigma_u^2$  in both places.

Often, we are primarly interested in a single parameter, in which case we can use a t statistic that ignores the other parameters. (For example, if one element of  $\mathbf{x}_{it}$  is a policy variable, and the other elements of  $\mathbf{x}_{it}$  are just controls or aggregate time dummies, we may only care about the coefficient on the policy variable.) Let  $\delta$  be the element of  $\boldsymbol{\beta}$  that we wish to use in the test. The Hausman test can be computed as a t statistic version of (10.78),  $(\hat{\delta}_{FE} - \hat{\delta}_{RE})/\{[\sec(\hat{\delta}_{FE})]^2 - [\sec(\hat{\delta}_{RE})]^2\}^{1/2}$ , where the standard errors are computed under the usual assumptions. Under Assumptions RE.1–RE.3, the t statistic has an asymptotic standard normal distribution.

For testing more than one parameter, it is often easier to use an F statistic version of the Hausman test. Let  $\check{\mathbf{x}}_{it}$  and  $\check{\mathbf{y}}_{it}$  be the quasi-demeaned data defined previously. Let  $\mathbf{w}_{it}$  denote a  $1 \times M$  subset of time-varying elements of  $\mathbf{x}_{it}$  (excluding time dummies); one can include all elements of  $\mathbf{x}_{it}$  that vary across i and t or a subset. Let  $\ddot{\mathbf{w}}_{it}$  denote the time-demeaned version of  $\mathbf{w}_{it}$ , and consider the extended model

$$\check{\mathbf{y}}_{it} = \check{\mathbf{x}}_{it}\boldsymbol{\beta} + \ddot{\mathbf{w}}_{it}\boldsymbol{\xi} + error_{it}, \qquad t = 1, \dots, T; i = 1, \dots, N$$
(10.79)

where  $\xi$  is an  $M \times 1$  vector. The error terms are complicated because  $\hat{\lambda}$  replaces  $\lambda$  in obtaining the quasi-demeaned data, but they can be treated as being homoskedastic and serially uncorrelated because replacing  $\lambda$  with  $\hat{\lambda}$  does not matter asymptotically. (This comment is just the usual observation that, in feasible GLS analysis, replacing  $\Omega$  with  $\hat{\Omega}$  has no effect on the asymptotic distribution of the feasible GLS estimator as  $N \to \infty$  under strict exogeneity.) Now, the Hausman test can be implemented by testing  $H_0$ :  $\xi = 0$  using standard pooled OLS analysis. The simplest approach is to compute the F statistic. The restricted SSR is obtained from the pooled regression that can be used to obtain  $\hat{\beta}_{RE}$ , namely regression (10.75). Call this sum of squared residuals SSR<sub>r</sub>. The unrestricted SSR comes from the pooled estimation of (10.79). Then the F statistic is

$$F = \frac{(SSR_r - SSR_{ur})}{SSR_{ur}} \cdot \frac{(NT - K - M)}{M}$$
(10.80)

Under H<sub>0</sub> (which is Assumptions RE.1–RE.3 in this case), F can be treated as an  $\mathscr{F}_{M,NT-K-M}$  random variable (because  $M \cdot F \stackrel{a}{\sim} \chi_M^2$ ).

This statistic turns out to be identical to a statistic derived by Mundlak (1978), who suggested putting  $\overline{\mathbf{w}}_i$  in place of  $\ddot{\mathbf{w}}_{it}$ . Mundlak's motivation is to test an alternative to

{303}------------------------------------------------

Assumption RE.1b of the form Eðci j xiÞ ¼ Eðci j wiÞ ¼ g<sup>0</sup> þ wi*g*. The equivalence of the two approaches follows because the regressors ðxit; w€itÞ are just a nonsingular linear transformation of the regressors ðxit; wiÞ, and so the SSRs in the unrestricted regression are the same; the restricted SSRs are clearly the same.

If Assumption RE.3 fails, then a robust form of the Hausman statistic is needed. Probably the easiest approach is to test H0: *x* ¼ 0 via a robust Wald statistic in the context of pooled OLS estimation of (10.79), or with w<sup>i</sup> in place of w€i. The robust test should account for serial correlation across time as well as general heteroskedasticity.

As in any other context that uses statistical inference, it is possible to get a statistical rejection of RE.1b (say, at the 5 percent level) with the differences between the RE and FE estimates being practically small. The opposite case is also possible: there can be seemingly large differences between the random effects and fixed effects estimates but, due to large standard errors, the Hausman statistic fails to reject. What should be done in this case? A typical response is to conclude that the random effects assumptions hold and to focus on the RE estimates. Unfortunately, we may be committing a Type II error: failing to reject Assumption RE.1b when it is false.