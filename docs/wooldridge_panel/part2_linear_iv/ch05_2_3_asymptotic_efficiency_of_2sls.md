# Asymptotic Efficiency of 2SLS

> Pages: 111-115

The appeal of 2SLS comes from its efficiency in a class of IV estimators:

THEOREM 5.3 (Relative Efficiency of 2SLS): Under Assumptions 2SLS.1–2SLS.3, the 2SLS estimator is efficient in the class of all instrumental variables estimators using instruments linear in z.

*Proof:* Let  $\hat{\beta}$  be the 2SLS estimator, and let  $\tilde{\beta}$  be any other IV estimator using instruments linear in  $\mathbf{z}$ . Let the instruments for  $\tilde{\beta}$  be  $\tilde{\mathbf{x}} \equiv \mathbf{z}\Gamma$ , where  $\Gamma$  is an  $L \times K$  nonstochastic matrix. (Note that  $\mathbf{z}$  is the  $1 \times L$  random vector in the population.) We assume that the rank condition holds for  $\tilde{\mathbf{x}}$ . For 2SLS, the choice of IVs is effectively  $\mathbf{x}^* = \mathbf{z}\Pi$ , where  $\Pi = [\mathbf{E}(\mathbf{z}'\mathbf{z})]^{-1}\mathbf{E}(\mathbf{z}'\mathbf{x}) \equiv \mathbf{D}^{-1}\mathbf{C}$ . (In both cases, we can replace  $\Gamma$  and  $\Pi$  with  $\sqrt{N}$ -consistent estimators without changing the asymptotic variances.) Now, under Assumptions 2SLS.1–2SLS.3, we know the asymptotic variance

{112}------------------------------------------------

of  $\sqrt{N}(\hat{\boldsymbol{\beta}}-\boldsymbol{\beta})$  is  $\sigma^2[\mathrm{E}(\mathbf{x}^{*'}\mathbf{x}^*)]^{-1}$ , where  $\mathbf{x}^*=\mathbf{z}\boldsymbol{\Pi}$ . It is straightforward to show that  $\mathrm{Avar}[\sqrt{N}(\tilde{\boldsymbol{\beta}}-\boldsymbol{\beta})]=\sigma^2[\mathrm{E}(\tilde{\mathbf{x}}'\mathbf{x})]^{-1}[\mathrm{E}(\tilde{\mathbf{x}}'\tilde{\mathbf{x}})][\mathrm{E}(\mathbf{x}'\tilde{\mathbf{x}})]^{-1}$ . To show that  $\mathrm{Avar}[\sqrt{N}(\tilde{\boldsymbol{\beta}}-\boldsymbol{\beta})]-\mathrm{Avar}[\sqrt{N}(\hat{\boldsymbol{\beta}}-\boldsymbol{\beta})]$  is positive semidefinite (p.s.d.), it suffices to show that  $\mathrm{E}(\mathbf{x}^{*'}\mathbf{x}^*)-\mathrm{E}(\mathbf{x}'\tilde{\mathbf{x}})[\mathrm{E}(\tilde{\mathbf{x}}'\tilde{\mathbf{x}})]^{-1}\mathrm{E}(\tilde{\mathbf{x}}'\mathbf{x})$  is p.s.d. But  $\mathbf{x}=\mathbf{x}^*+\mathbf{r}$ , where  $\mathrm{E}(\mathbf{z}'\mathbf{r})=\mathbf{0}$ , and so  $\mathrm{E}(\tilde{\mathbf{x}}'\mathbf{r})=\mathbf{0}$ . It follows that  $\mathrm{E}(\tilde{\mathbf{x}}'\mathbf{x})=\mathrm{E}(\tilde{\mathbf{x}}'\mathbf{x}^*)$ , and so

$$\begin{split} E(\mathbf{x}^{*\prime}\mathbf{x}^{*}) - E(\mathbf{x}^{\prime}\tilde{\mathbf{x}})[E(\tilde{\mathbf{x}}^{\prime}\tilde{\mathbf{x}})]^{-1}E(\tilde{\mathbf{x}}^{\prime}\mathbf{x}) \\ = E(\mathbf{x}^{*\prime}\mathbf{x}^{*}) - E(\mathbf{x}^{*\prime}\tilde{\mathbf{x}})[E(\tilde{\mathbf{x}}^{\prime}\tilde{\mathbf{x}})]^{-1}E(\tilde{\mathbf{x}}^{\prime}\mathbf{x}^{*}) = E(\mathbf{s}^{*\prime}\mathbf{s}^{*}) \end{split}$$

where  $\mathbf{s}^* = \mathbf{x}^* - \mathbf{L}(\mathbf{x}^* | \tilde{\mathbf{x}})$  is the population residual from the linear projection of  $\mathbf{x}^*$  on  $\tilde{\mathbf{x}}$ . Because  $\mathbf{E}(\mathbf{s}^{*\prime}\mathbf{s}^*)$  is p.s.d, the proof is complete.

Theorem 5.3 is vacuous when L = K because any (nonsingular) choice of  $\Gamma$  leads to the same estimator: the IV estimator derived in Section 5.1.1.

When  $\mathbf{x}$  is exogenous, Theorem 5.3 implies that, under Assumptions 2SLS.1–2SLS.3, the OLS estimator is efficient in the class of all estimators using instruments linear in exogenous variables  $\mathbf{z}$ . This statement is true because  $\mathbf{x}$  is a subset of  $\mathbf{z}$  and so  $L(\mathbf{x} \mid \mathbf{z}) = \mathbf{x}$ .

Another important implication of Theorem 5.3 is that, asymptotically, we always do better by using as many instruments as are available, at least under homoskedasticity. This conclusion follows because using a subset of  $\mathbf{z}$  as instruments corresponds to using a particular linear combination of  $\mathbf{z}$ . For certain subsets we might achieve the same efficiency as 2SLS using all of  $\mathbf{z}$ , but we can do no better. This observation makes it tempting to add many instruments so that L is much larger than K. Unfortunately, 2SLS estimators based on many overidentifying restrictions can cause finite sample problems; see Section 5.2.6.

Since Assumption 2SLS.3 is assumed for Theorem 5.3, it is not surprising that more efficient estimators are available if Assumption 2SLS.3 fails. If L > K, a more efficient estimator than 2SLS exists, as shown by Hansen (1982) and White (1982b, 1984). In fact, even if  $\mathbf{x}$  is exogenous and Assumption OLS.3 holds, OLS is not generally asymptotically efficient if, for  $\mathbf{x} \subset \mathbf{z}$ , Assumptions 2SLS.1 and 2SLS.2 hold but Assumption 2SLS.3 does not. Obtaining the efficient estimator falls under the rubric of generalized method of moments estimation, something we cover in Chapter 8.

# 5.2.4 Hypothesis Testing with 2SLS

We have already seen that testing hypotheses about a single  $\beta_j$  is straightforward using an asymptotic t statistic, which has an asymptotic normal distribution under the null; some prefer to use the t distribution when N is small. Generally, one should be

{113}------------------------------------------------

aware that the normal and t approximations can be poor if N is small. Hypotheses about single linear combinations involving the  $\beta_j$  are also easily carried out using a t statistic. The easiest procedure is to define the linear combination of interest, say  $\theta \equiv a_1\beta_1 + a_2\beta_2 + \cdots + a_K\beta_K$ , and then to write one of the  $\beta_j$  in terms of  $\theta$  and the other elements of  $\beta$ . Then, substitute into the equation of interest so that  $\theta$  appears directly, and estimate the resulting equation by 2SLS to get the standard error of  $\hat{\theta}$ . See Problem 5.9 for an example.

To test multiple linear restrictions of the form  $H_0$ :  $\mathbf{R}\boldsymbol{\beta} = \mathbf{r}$ , the Wald statistic is just as in equation (4.13), but with  $\hat{\mathbf{V}}$  given by equation (5.27). The Wald statistic, as usual, is a limiting null  $\chi_Q^2$  distribution. Some econometrics packages, such as Stata®, compute the Wald statistic (actually, its F statistic counterpart, obtained by dividing the Wald statistic by Q) after 2SLS estimation using a simple test command.

A valid test of multiple restrictions can be computed using a residual-based method, analogous to the usual F statistic from OLS analysis. Any kind of linear restriction can be recast as exclusion restrictions, and so we explicitly cover exclusion restrictions. Write the model as

$$y = \mathbf{x}_1 \boldsymbol{\beta}_1 + \mathbf{x}_2 \boldsymbol{\beta}_2 + u \tag{5.28}$$

where  $\mathbf{x}_1$  is  $1 \times K_1$  and  $\mathbf{x}_2$  is  $1 \times K_2$ , and interest lies in testing the  $K_2$  restrictions

$$H_0: \beta_2 = 0$$
 against  $H_1: \beta_2 \neq 0$  (5.29)

Both  $\mathbf{x}_1$  and  $\mathbf{x}_2$  can contain endogenous and exogenous variables.

Let **z** denote the  $L \ge K_1 + K_2$  vector of instruments, and we assume that the rank condition for identification holds. Justification for the following statistic can be found in Wooldridge (1995b).

Let  $\hat{u}_i$  be the 2SLS residuals from estimating the unrestricted model using  $\mathbf{z}_i$  as instruments. Using these residuals, define the 2SLS unrestricted sum of squared residuals by

$$SSR_{ur} \equiv \sum_{i=1}^{N} \hat{u}_i^2 \tag{5.30}$$

In order to define the F statistic for 2SLS, we need the sum of squared residuals from the *second*-stage regressions. Thus, let  $\hat{\mathbf{x}}_{i1}$  be the  $1 \times K_1$  fitted values from the first-stage regression  $\mathbf{x}_{i1}$  on  $\mathbf{z}_i$ . Similarly,  $\hat{\mathbf{x}}_{i2}$  are the fitted values from the first-stage regression  $\mathbf{x}_{i2}$  on  $\mathbf{z}_i$ . Define  $\hat{SSR}_{ur}$  as the usual sum of squared residuals from the unrestricted second-stage regression y on  $\hat{\mathbf{x}}_1$ ,  $\hat{\mathbf{x}}_2$ . Similarly,  $\hat{SSR}_r$  is the sum of squared residuals from the restricted second-stage regression, y on  $\hat{\mathbf{x}}_1$ . It can be shown that,

{114}------------------------------------------------

under H<sub>0</sub>:  $\beta_2 = 0$  (and Assumptions 2SLS.1–2SLS.3),  $N \cdot (\hat{SSR}_r - \hat{SSR}_{ur})/\hat{SSR}_{ur} \approx \chi_{K_2}^2$ . It is just as legitimate to use an *F*-type statistic:

$$F \equiv \frac{(\hat{SSR}_r - \hat{SSR}_{ur})}{\hat{SSR}_{ur}} \cdot \frac{(N - K)}{K_2}$$
(5.31)

is distributed approximately as  $\mathcal{F}_{K_2,N-K}$ .

Note carefully that  $SSR_r$  and  $SSR_{ur}$  appear in the numerator of (5.31). These quantities typically need to be computed directly from the second-stage regression. In the denominator of F is  $SSR_{ur}$ , which is the 2SLS sum of squared residuals. This is what is reported by the 2SLS commands available in popular regression packages.

For 2SLS it is important not to use a form of the statistic that would work for OLS, namely,

$$\frac{(SSR_r - SSR_{ur})}{SSR_{ur}} \cdot \frac{(N - K)}{K_2} \tag{5.32}$$

where  $SSR_r$  is the 2SLS restricted sum of squared residuals. Not only does expression (5.32) not have a known limiting distribution, but it can also be negative with positive probability even as the sample size tends to infinity; clearly such a statistic cannot have an approximate F distribution, or any other distribution typically associated with multiple hypothesis testing.

Example 5.4 (Parents' and Husband's Education as IVs, continued): We add the number of young children (kidslt6) and older children (kidsge6) to equation (5.12) and test for their joint significance using the Mroz (1987) data. The statistic in equation (5.31) is F = .31; with two and 422 degrees of freedom, the asymptotic p-value is about .737. There is no evidence that number of children affects the wage for working women.

Rather than equation (5.31), we can compute an LM-type statistic for testing hypothesis (5.29). Let  $\tilde{u}_i$  be the 2SLS residuals from the restricted model. That is, obtain  $\tilde{\beta}_1$  from the model  $y = \mathbf{x}_1 \beta_1 + u$  using instruments  $\mathbf{z}$ , and let  $\tilde{u}_i \equiv y_i - \mathbf{x}_{i1} \tilde{\boldsymbol{\beta}}_1$ . Letting  $\hat{\mathbf{x}}_{i1}$  and  $\hat{\mathbf{x}}_{i2}$  be defined as before, the LM statistic is obtained as  $NR_u^2$  from the regression

$$\tilde{u}_i \text{ on } \hat{\mathbf{x}}_{i1}, \hat{\mathbf{x}}_{i2}, \qquad i = 1, 2, \dots, N$$
 (5.33)

where  $R_u^2$  is generally the uncentered *R*-squared. (That is, the total sum of squares in the denominator of *R*-squared is not demeaned.) When  $\{\tilde{u}_i\}$  has a zero sample average, the uncentered *R*-squared and the usual *R*-squared are the same. This is the case when the null explanatory variables  $\mathbf{x}_1$  and the instruments  $\mathbf{z}$  both contain unity, the

{115}------------------------------------------------

typical case. Under H<sub>0</sub> and Assumptions 2SLS.1–2SLS.3,  $LM \stackrel{a}{\sim} \chi_{K_2}^2$ . Whether one uses this statistic or the *F* statistic in equation (5.31) is primarily a matter of taste; asymptotically, there is nothing that distinguishes the two.