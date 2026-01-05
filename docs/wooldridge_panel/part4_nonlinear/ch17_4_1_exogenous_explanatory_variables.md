# Exogenous Explanatory Variables

> Pages: 568-575

The incidental truncation problem is motivated by Gronau's (1974) model of the wage offer and labor force participation.

Example 17.5 (Labor Force Participation and the Wage Offer): Interest lies in estimating  $E(w_i^o | \mathbf{x}_i)$ , where  $w_i^o$  is the hourly wage offer for a randomly drawn individual

{569}------------------------------------------------

i. If  $w_i^0$  were observed for everyone in the (working age) population, we would proceed in a standard regression framework. However, a potential sample selection problem arises because  $w_i^0$  is observed only for people who work.

We can cast this problem as a weekly labor supply model:

$$\max_{h} \operatorname{util}_{i}(w_{i}^{0}h + a_{i}, h) \quad \text{subject to } 0 \le h \le 168$$
 (17.15)

where h is hours worked per week and  $a_i$  is nonwage income of person i. Let  $s_i(h) \equiv \operatorname{util}_i(w_i^\circ h + a_i, h)$ , and assume that we can rule out the solution  $h_i = 168$ . Then the solution can be  $h_i = 0$  or  $0 < h_i < 168$ . If  $ds_i/dh \le 0$  at h = 0, then the optimum is  $h_i = 0$ . Using this condition, straightforward algebra shows that  $h_i = 0$  if and only if

$$w_i^{0} \le -mu_i^{h}(a_i, 0)/mu_i^{q}(a_i, 0) \tag{17.16}$$

where  $mu_i^h(\cdot,\cdot)$  is the marginal disutility of working and  $mu_i^q(\cdot,\cdot)$  is the marginal utility of income. Gronau (1974) called the right-hand side of equation (17.16) the reservation wage,  $w_i^r$ , which is assumed to be strictly positive.

We now make the parametric assumptions

$$w_i^{\text{o}} = \exp(\mathbf{x}_{i1}\boldsymbol{\beta}_1 + u_{i1}), \qquad w_i^{\text{r}} = \exp(\mathbf{x}_{i2}\boldsymbol{\beta}_2 + \gamma_2 a_i + u_{i2})$$
 (17.17)

where  $(u_{i1}, u_{i2})$  is independent of  $(\mathbf{x}_{i1}, \mathbf{x}_{i2}, a_i)$ . Here,  $\mathbf{x}_{i1}$  contains productivity characteristics, and possibly demographic characteristics, of individual i, and  $\mathbf{x}_{i2}$  contains variables that determine the marginal utility of leisure and income; these may overlap with  $\mathbf{x}_{i1}$ . From equation (17.17) we have the log wage equation

$$\log w_i^0 = \mathbf{x}_{i1} \beta_1 + u_{i1} \tag{17.18}$$

But the wage offer  $w_i^0$  is observed only if the person works, that is, only if  $w_i^0 \ge w_i^r$ , or

$$\log w_i^{\text{o}} - \log w_i^{\text{r}} = \mathbf{x}_{i1} \boldsymbol{\beta}_1 - \mathbf{x}_{i2} \boldsymbol{\beta}_2 - \gamma_2 a_i + u_{i1} - u_{i2} \equiv \mathbf{x}_i \boldsymbol{\delta}_2 + v_{i2} > 0$$

This behavior introduces a potential sample selection problem if we use data only on working people to estimate equation (17.18).

This example differs in an important respect from top coding examples. With top coding, the censoring rule is known for each unit in the population. In Gronau's example, we do not know  $w_i^r$ , so we cannot use  $w_i^o$  in a censored regression analysis. If  $w_i^r$  were observed and exogenous and  $\mathbf{x}_{i1}$  were always observed, then we would be in the censored regression framework (see Problem 16.3). If  $w_i^r$  were observed and exogenous but  $\mathbf{x}_{i1}$  were observed only when  $w_i^o$  is, we would be in the truncated Tobit framework. But  $w_i^r$  is allowed to depend on unobservables, and so we need a new framework.

{570}------------------------------------------------

If we drop the i subscript, let y<sup>1</sup> 1log wo, and let y<sup>2</sup> be the binary labor force participation indicator, Gronau's model can be written for a random draw from the population as

$$y_1 = \mathbf{x}_1 \boldsymbol{\beta}_1 + u_1 \tag{17.19}$$

$$y_2 = 1[\mathbf{x}\delta_2 + v_2 > 0] \tag{17.20}$$

We discuss estimation of this model under the following set of assumptions:

assumption 17.1: (a) ðx; y2Þ are always observed, y<sup>1</sup> is observed only when y<sup>2</sup> ¼ 1; (b) ðu1; v2Þ is independent of x with zero mean; (c) v<sup>2</sup> @ Normalð0; 1Þ; and (d) Eðu<sup>1</sup> j v2Þ ¼ g1v2.

Assumption 17.1a emphasizes the sample selection nature of the problem. Part b is a strong, but standard, form of exogeneity of x. We will see that Assumption 17.1c is needed to derive a conditional expectation given the selected sample. It is probably the most restrictive assumption because it is an explicit distributional assumption. Assuming Varðv2Þ ¼ 1 is without loss of generality because y<sup>2</sup> is a binary variable.

Assumption 17.1d requires linearity in the population regression of u<sup>1</sup> on v2. It always holds if ðu1; v2Þ is bivariate normal—a standard assumption in these contexts—but Assumption 17.1d holds under weaker assumptions. In particular, we do not need to assume that u<sup>1</sup> itself is normally distributed.

Amemiya (1985) calls equations (17.19) and (17.20) the type II Tobit model. This name is fine as a label, but we must understand that it is a model of sample selection, and it has nothing to do with y<sup>1</sup> being a corner solution outcome. Unfortunately, in almost all treatments of this model, y<sup>1</sup> is set to zero when y<sup>2</sup> ¼ 0. Setting y<sup>1</sup> to zero (or any value) when y<sup>2</sup> ¼ 0 is misleading and can lead to inappropriate use of the model. For example, it makes no sense to set the wage offer to zero just because we do not observe it. As another example, it makes no sense to set the price per dollar of life insurance ðy1Þ to zero for someone who did not buy life insurance (so y<sup>2</sup> ¼ 1 if and only if a person owns a life insurance policy).

We also have some interest in the parameters of the selection equation (17.20); for example, in Gronau's model it is a reduced-form labor force participation equation. In program evaluation with attrition, the selection equation explains the probability of dropping out of the program.

We can allow a little more generality in the model by replacing x in equation (17.20) with x2; then, as will become clear, x<sup>1</sup> would only need to be observed whenever y<sup>1</sup> is, whereas x<sup>2</sup> must always be observed. This extension is not especially useful for something like Gronau's model because it implies that x<sup>1</sup> contains elements


{571}------------------------------------------------

that cannot also appear in x2. Because the selection equation is not typically a structural equation, it is undesirable to impose exclusion restrictions in equation (17.20). If a variable affecting y<sup>1</sup> is observed only along with y1, the instrumental variables method that we cover in Section 17.4.2 is more attractive.

To derive an estimating equation, let ðy1; y2; x; u1; v2Þ denote a random draw from the population. Since y<sup>1</sup> is observed only when y<sup>2</sup> ¼ 1, what we can hope to estimate is Eðy<sup>1</sup> j x; y<sup>2</sup> ¼ 1Þ [along with Pðy<sup>2</sup> ¼ 1 j xÞ]. How does Eðy<sup>1</sup> j x; y<sup>2</sup> ¼ 1Þ depend on the vector of interest, *b*1? First, under Assumption 17.1 and equation (17.19),

$$E(y_1 | \mathbf{x}, v_2) = \mathbf{x}_1 \boldsymbol{\beta}_1 + E(u_1 | \mathbf{x}, v_2) = \mathbf{x}_1 \boldsymbol{\beta}_1 + E(u_1 | v_2) = \mathbf{x}_1 \boldsymbol{\beta}_1 + \gamma_1 v_2$$
 (17.21)

where the second equality follows because ðu1; v2Þ is independent of x. Equation (17.21) is very useful. The first thing to note is that, if g<sup>1</sup> ¼ 0—which implies that u<sup>1</sup> and v<sup>2</sup> are uncorrelated—then Eðy<sup>1</sup> j x; v2Þ ¼ Eðy<sup>1</sup> j xÞ ¼ Eðy<sup>1</sup> j x1Þ ¼ x1*b*1. Because y<sup>2</sup> is a function of ðx; v2Þ, it follows immediately that Eðy<sup>1</sup> j x; y2Þ ¼ Eðy<sup>1</sup> j x1Þ. In other words, if g<sup>1</sup> ¼ 0, then there is no sample selection problem, and *b*<sup>1</sup> can be consistently estimated by OLS using the selected sample.

What if g<sup>1</sup> 00? Using iterated expectations on equation (17.21),

$$E(y_1 | \mathbf{x}, y_2) = \mathbf{x}_1 \boldsymbol{\beta}_1 + \gamma_1 E(v_2 | \mathbf{x}, y_2) = \mathbf{x}_1 \boldsymbol{\beta}_1 + \gamma_1 h(\mathbf{x}, y_2)$$

where hðx; y2Þ ¼ Eðv<sup>2</sup> j x; y2Þ. If we knew hðx; y2Þ, then, from Theorem 17.1, we could estimate *b*<sup>1</sup> and g<sup>1</sup> from the regression y<sup>1</sup> on x<sup>1</sup> and hðx; y2Þ, using only the selected sample. Because the selected sample has y<sup>2</sup> ¼ 1, we need only find hðx; 1Þ. But hðx; 1Þ ¼ Eðv<sup>2</sup> j v<sup>2</sup> > x*d*2Þ ¼ lðx*d*2Þ, where lð-Þ1 fð-Þ=Fð-Þ is the inverse Mills ratio, and so we can write

$$E(y_1 | \mathbf{x}, y_2 = 1) = \mathbf{x}_1 \boldsymbol{\beta}_1 + \gamma_1 \lambda(\mathbf{x}\boldsymbol{\delta}_2)$$
(17.22)

Equation (17.22), which can be found in numerous places (see, for example, Heckman, 1979, and Amemiya, 1985) makes it clear that an OLS regression of y<sup>1</sup> on x<sup>1</sup> using the selected sample omits the term lðx*d*2Þ and generally leads to inconsistent estimation of *b*1. As pointed out by Heckman (1979), the presence of selection bias can be viewed as an omitted variable problem in the selected sample. An interesting point is that, even though only x<sup>1</sup> appears in the population expectation, Eðy<sup>1</sup> j xÞ, other elements of x appear in the expectation on the subpopulation, Eðy<sup>1</sup> j x; y<sup>2</sup> ¼ 1Þ.

Equation (17.22) also suggests a way to consistently estimate *b*1. Following Heckman (1979), we can consistently estimate *b*<sup>1</sup> and g<sup>1</sup> using the selected sample by regressing yi<sup>1</sup> on xi1, lðxi*d*2Þ. The problem is that *d*<sup>2</sup> is unknown, so we cannot compute the additional regressor lðxi*d*2Þ. Nevertheless, a consistent estimator of *d*<sup>2</sup> is available from the first-stage probit estimation of the selection equation.

{572}------------------------------------------------

*Procedure 17.1:* (a) Obtain the probit estimate  $\hat{\delta}_2$  from the model

$$\mathbf{P}(y_{i2} = 1 \mid \mathbf{x}_i) = \Phi(\mathbf{x}_i \boldsymbol{\delta}_2) \tag{17.23}$$

using all N observations. Then, obtain the estimated inverse Mills ratios  $\hat{\lambda}_{i2} \equiv \lambda(\mathbf{x}_i \hat{\boldsymbol{\delta}}_2)$  (at least for  $i = 1, \dots, N_1$ ).

(b) Obtain  $\hat{\beta}_1$  and  $\hat{\gamma}_1$  from the OLS regression on the selected sample,

$$y_{i1} \text{ on } \mathbf{x}_{i1}, \hat{\lambda}_{i2}, \qquad i = 1, 2, \dots, N_1$$
 (17.24)

These estimators are consistent and  $\sqrt{N}$ -asymptotically normal.

The procedure is sometimes called **Heckit** after Heckman (1976) and the tradition of putting "it" on the end of procedures related to probit (such as Tobit).

A very simple test for selection bias is available from regression (17.24). Under the the null of no selection bias,  $H_0$ :  $\gamma_1 = 0$ , we have  $\text{Var}(y_1 \mid \mathbf{x}, y_2 = 1) = \text{Var}(y_1 \mid \mathbf{x}) = \text{Var}(u_1)$ , and so homoskedasticity holds under  $H_0$ . Further, from the results on generated regressors in Chapter 6, the asymptotic variance of  $\hat{\gamma}_1$  (and  $\hat{\beta}_1$ ) is not affected by  $\hat{\delta}_2$  when  $\gamma_1 = 0$ . Thus, a standard t test on  $\hat{\gamma}_1$  is a valid test of the null hypothsesis of no selection bias.

When  $\gamma_1 \neq 0$ , obtaining a consistent estimate for the asymptotic variance of  $\hat{\beta}_1$  is complicated for two reasons. The first is that, if  $\gamma_1 \neq 0$ , then  $\text{Var}(\gamma_1 \mid \mathbf{x}, \gamma_2 = 1)$  is not constant. As we know, heteroskedasticity itself is easy to correct for using the robust standard errors. However, we should also account for the fact that  $\hat{\delta}_2$  is an estimator of  $\delta_2$ . The adjustment to the variance of  $(\hat{\beta}_1, \hat{\gamma}_1)$  because of the two-step estimation is cumbersome—it is *not* enough to simply make the standard errors heteroskedasticity-robust. Some statistical packages now have this feature built in.

As a technical point, we do not need  $\mathbf{x}_1$  to be a strict subset of  $\mathbf{x}$  for  $\boldsymbol{\beta}_1$  to be indentified, and Procedure 17.1 does carry through when  $\mathbf{x}_1 = \mathbf{x}$ . However, if  $\mathbf{x}_i \hat{\boldsymbol{\delta}}_2$  does not have much variation in the sample, then  $\hat{\lambda}_{i2}$  can be approximated well by a linear function of  $\mathbf{x}$ . If  $\mathbf{x} = \mathbf{x}_1$ , this correlation can introduce severe collinearity among the regressors in regression (17.24), which can lead to large standard errors of the elements of  $\hat{\boldsymbol{\beta}}_1$ . When  $\mathbf{x}_1 = \mathbf{x}$ ,  $\boldsymbol{\beta}_1$  is identified only due to the nonlinearity of the inverse Mills ratio.

The situation is not quite as bad as in Section 9.5.1. There, identification failed for certain values of the structural parameters. Here, we still have identification for any value of  $\beta_1$  in equation (17.19), but it is unlikely we can estimate  $\beta_1$  with much precision. Even if we can, we would have to wonder whether a statistically inverse Mills ratio term is due to sample selection or functional form misspecification in the population model (17.19).

{573}------------------------------------------------

<table><tbody><tr><th>Table 17.1</th><th></th><th></th></tr><tr><td></td><td>Wage Offer Equation for Married Women</td><td></td></tr></tbody></table>

<table><tbody><tr><th colspan="4">Dependent Variable: logðwageÞ</th></tr><tr><th>Independent Variable</th><th>OLS</th><th>Heckit</th><th></th></tr><tr><td>educ</td><td>.108<br/>(.014)</td><td>.109<br/>(.016)</td><td></td></tr><tr><td>exper</td><td>.042<br/>(.012)</td><td>.044<br/>(.016)</td><td></td></tr><tr><td>exper 2</td><td>.00081<br/>(.00039)</td><td>.00086<br/>(.00044)</td><td></td></tr><tr><td>constant</td><td>.522<br/>(.199)</td><td>.578<br/>(.307)</td><td></td></tr><tr><td>^l2</td><td>—</td><td>.032<br/>(.134)</td><td></td></tr><tr><td>Sample size<br/>R-squared</td><td>428<br/>.157</td><td>428<br/>.157</td><td></td></tr></tbody></table>

Example 17.6 (Wage Offer Equation for Married Women): We use the data in MROZ.RAW to estimate a wage offer function for married women, accounting for potential selectivity bias into the workforce. Of the 753 women, we observe the wage offer for 428 working women. The labor force participation equation contains the variables in Table 15.1, including other income, age, number of young children, and number of older children—in addition to educ, exper, and exper2. The results of OLS on the selected sample and the Heckit method are given in Table 17.1.

The differences between the OLS and Heckit estimates are practically small, and the inverse Mills ratio term is statistically insignificant. The fact that the intercept estimates differ somewhat is usually unimportant. [The standard errors reported for Heckit are the unadjusted ones from regression (17.24). If ^l<sup>2</sup> were statistically significant, we should obtain the corrected standard errors.]

The Heckit results in Table 17.1 use four exclusion restrictions in the structural equation, because nwifeinc, age, kidslt6, and kidsge6 are all excluded from the wage offer equation. If we allow all variables in the selection equation to also appear in the wage offer equation, the Heckit estimates become very imprecise. The coefficient on educ becomes .119 (se ¼ :034), compared with the OLS estimate .100 (se ¼ :015). The coefficient on kidslt6—which now appears in the wage offer equation—is :188 (se ¼ :232) in the Heckit estimation, and :056 (se ¼ :009) in the OLS estimation. The imprecision of the Heckit estimates is due to the severe collinearity that comes from adding ^l<sup>2</sup> to the equation, because ^l<sup>2</sup> is now a function only of the explanatory variables in the wage offer equation. In fact, using the selected sample, regressing ^l<sup>2</sup> on

{574}------------------------------------------------

the seven explanatory variables gives R-squared = .962. Unfortunately, comparing the OLS and Heckit results does not allow us to resolve some important issues. For example, the OLS results suggest that another young child reduces the wage offer by about 5.6 percent (t statistic  $\approx -6.2$ ), other things being equal. Is this effect real, or is it simply due to our inability to adequately correct for sample selection bias? Unless we have a variable that affects labor force participation without affecting the wage offer, we cannot answer this question.

If we replace parts c and d in Assumption 17.1 with the stronger assumption that  $(u_1, v_2)$  is bivariate normal with mean zero,  $Var(u_1) = \sigma_1^2$ ,  $Cov(u_1, v_2) = \sigma_{12}$ , and  $Var(v_2) = 1$ , then partial maximum likelihood estimation can be used, as described generally in Problem 13.7. Partial MLE will be more efficient than the two-step procedure under joint normality of  $u_1$  and  $v_2$ , and it will produce standard errors and likelihood ratio statistics that can be used directly (this conclusion follows from Problem 13.7). The drawbacks are that it is less robust than the two-step procedure and that it is sometimes difficult to get the problem to converge.

The reason we cannot perform full conditional MLE is that  $y_1$  is only observed when  $y_2 = 1$ . Thus, while we can use the full density of  $y_2$  given  $\mathbf{x}$ , which is  $f(y_2 | \mathbf{x}) = [\Phi(\mathbf{x}\boldsymbol{\delta}_2)]^{y_2}[1 - \Phi(\mathbf{x}\boldsymbol{\delta}_2)]^{1-y_2}$ ,  $y_2 = 0$ , 1, we can only use the density  $f(y_1 | y_2, \mathbf{x})$  when  $y_2 = 1$ . To find  $f(y_1 | y_2, \mathbf{x})$  at  $y_2 = 1$ , we can use Bayes' rule to write  $f(y_1 | y_2, \mathbf{x}) = f(y_2 | y_1, \mathbf{x}) f(y_1 | \mathbf{x}) / f(y_2 | \mathbf{x})$ . Therefore,  $f(y_1 | y_2 = 1, \mathbf{x}) = P(y_2 = 1 | y_1, \mathbf{x}) f(y_1 | \mathbf{x}) / P(y_2 = 1 | \mathbf{x})$ . But  $y_1 | \mathbf{x} \sim \text{Normal}(\mathbf{x}_1 \boldsymbol{\beta}_1, \sigma_1^2)$ . Further,  $y_2 = 1[\mathbf{x}\boldsymbol{\delta}_2 + \sigma_{12}\sigma_1^{-2}(y_1 - \mathbf{x}_1\boldsymbol{\beta}_1) + e_2 > 0]$ , where  $e_2$  is independent of  $(\mathbf{x}, y_1)$  and  $e_2 \sim \text{Normal}(0, 1 - \sigma_{12}^2\sigma_1^{-2})$  (this conclusion follows from standard conditional distribution results for joint normal random variables). Therefore,

$$P(y_2 = 1 \mid y_1, \mathbf{x}) = \Phi\{ [\mathbf{x}\boldsymbol{\delta}_2 + \sigma_{12}\sigma_1^{-2}(y_1 - \mathbf{x}_1\boldsymbol{\beta}_1)](1 - \sigma_{12}^2\sigma_1^{-2})^{-1/2} \}$$

Combining all of these pieces [and noting the cancellation of  $P(y_2 = 1 | \mathbf{x})$ ] we get

$$\ell_i(\boldsymbol{\theta}) = (1 - y_{i2}) \log[1 - \Phi(\mathbf{x}_i \boldsymbol{\delta}_2)] + y_{i2} (\log \Phi\{[\mathbf{x} \boldsymbol{\delta}_2 + \sigma_{12} \sigma_1^{-2} (y_{i1} - \mathbf{x}_{i1} \boldsymbol{\beta}_1)]$$

$$\times (1 - \sigma_{12}^2 \sigma_1^{-2})^{-1/2}\} + \log \phi[(y_{i1} - \mathbf{x}_{i1} \boldsymbol{\beta}_1) / \sigma_1] - \log(\sigma_1))$$

The partial log likelihood is obtained by summing  $\ell_i(\theta)$  across *all* observations;  $y_{i2} = 1$  picks out when  $y_{i1}$  is observed and therefore contains information for estimating  $\beta_1$ .

Ahn and Powell (1993) show how to consistently estimate  $\beta_1$  without making any distributional assumptions; in particular, the selection equation need not have the probit form. Vella (1998) contains a recent survey.

{575}------------------------------------------------