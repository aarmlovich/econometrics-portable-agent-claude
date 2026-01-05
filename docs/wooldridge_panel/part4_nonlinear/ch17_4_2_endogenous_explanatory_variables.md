# Endogenous Explanatory Variables

> Pages: 575-578

We now study the sample selection model when one of the elements of x<sup>1</sup> is thought to be correlated with u1. Or, all the elements of x<sup>1</sup> are exogenous in the population model but data are missing on an element of x1, and the reason data are missing might be systematically related to u1. For simplicity, we focus on the case of a single endogenous explanatory variable.

The model in the population is

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1 \tag{17.25}$$

$$y_2 = \mathbf{z}\boldsymbol{\delta}_2 + v_2 \tag{17.26}$$

$$y_3 = 1(\mathbf{z}\delta_3 + v_3 > 0) \tag{17.27}$$

The first equation is the structural equation of interest, the second equation is a linear projection for the potentially endogenous or missing variable y2, and the third equation is the selection equation. We allow arbitrary correlation among u1, v2, and v3.

The setup in equations (17.25)–(17.27) encompasses at least three cases of interest. The first occurs when y<sup>2</sup> is always observed but is endogenous in equation (17.25). An example is seen when y<sup>1</sup> is logðwageoÞ and y<sup>2</sup> is years of schooling: years of schooling is generally available whether or not someone is in the workforce. The model also applies when y<sup>2</sup> is observed only along with y1, as would happen if y<sup>1</sup> ¼ logðwageoÞ and y<sup>2</sup> is the ratio of the benefits offer to wage offer. As a second example, let y<sup>1</sup> be the percentage of voters supporting the incumbent in a congressional district, and let y<sup>2</sup> be intended campaign expenditures. Then y<sup>3</sup> ¼ 1 if the incumbent runs for reelection, and we only observe ðy1; y2Þ when y<sup>3</sup> ¼ 1. A third application is to missing data only on y2, as in Example 17.4 where y<sup>2</sup> is IQ score. In the last two cases, y<sup>2</sup> might in fact be exogenous in equation (17.25), but endogenous sample selection effectively makes y<sup>2</sup> endogenous in the selected sample.

If y<sup>1</sup> and y<sup>2</sup> were always observed along with z, we would just estimate equation (17.25) by 2SLS if y<sup>2</sup> is endogenous. We can use the results from Section 17.2.1 to show that 2SLS with the inverse Mills ratio added to the regressors is consistent. Regardless of the data availability on y<sup>1</sup> and y2, in the second step we use only observations for which both y<sup>1</sup> and y<sup>2</sup> are observed.

assumption 17.2: (a) ðz; y3Þ is always observed, ðy1; y2Þ is observed when y<sup>3</sup> ¼ 1; (b) ðu1; v3Þ is independent of z; (c) v<sup>3</sup> @Normalð0; 1Þ; (d) Eðu<sup>1</sup> j v3Þ ¼ g1v3; and (e) Eðz<sup>0</sup> v2Þ ¼ 0 and, writing z*d*<sup>2</sup> ¼ z1*d*<sup>21</sup> þ z2*d*22, *d*<sup>22</sup> 0 0.

{576}------------------------------------------------

Parts b, c, and d are identical to the corresponding assumptions when all explanatory variables are observed and exogenous. Assumption e is new, resulting from the endogeneity of  $y_2$  in equation (17.25). It is important to see that Assumption 17.2e is identical to the rank condition needed for identifying equation (17.25) in the absence of sample selection. As we will see, stating identification in the population is not always sufficient, but, from a practical point of view, the focus should be on Assumption 17.2e.

To derive an estimating equation, write (in the population)

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + g(\mathbf{z}, y_3) + e_1 \tag{17.28}$$

where  $g(\mathbf{z}, y_3) \equiv \mathrm{E}(u_1 | \mathbf{z}, y_3)$  and  $e_1 \equiv u_1 - \mathrm{E}(u_1 | \mathbf{z}, y_3)$ . By definition,  $\mathrm{E}(e_1 | \mathbf{z}, y_3) = 0$ . If we knew  $g(\mathbf{z}, y_3)$  then, from Theorem 17.1, we could just estimate equation (17.28) by 2SLS on the selected sample  $(y_3 = 1)$  using instruments  $[\mathbf{z}, g(\mathbf{z}, 1)]$ . It turns out that we do know  $g(\mathbf{z}, 1)$  up to some estimable parameters:  $\mathrm{E}(u_1 | \mathbf{z}, y_3 = 1) = y_1 \lambda(\mathbf{z}\delta_3)$ . Since  $\delta_3$  can be consistently estimated by probit of  $y_3$  on  $\mathbf{z}$  (using the entire sample), we have the following:

*Procedure 17.2:* (a) Obtain  $\hat{\boldsymbol{\delta}}_3$  from probit of  $y_3$  on **z** using all observations. Obtain the estimated inverse Mills ratios,  $\hat{\lambda}_{i3} = \lambda(\mathbf{z}_i\hat{\boldsymbol{\delta}}_3)$ .

(b) Using the selected subsample (for which we observe both  $y_1$  and  $y_2$ ), estimate the equation

$$y_{i1} = \mathbf{z}_{i1}\boldsymbol{\delta}_1 + \alpha_1 y_{i2} + \gamma_1 \hat{\lambda}_{i3} + error_i$$
 (17.29)

by 2SLS, using instruments  $(\mathbf{z}_i, \hat{\lambda}_{i3})$ .

The steps in this procedure show that identification actually requires that  $\mathbf{z}_2$  appear in the linear projection of  $y_2$  onto  $\mathbf{z}_1, \mathbf{z}_2$ , and  $\lambda(\mathbf{z}\boldsymbol{\delta}_3)$  in the selected subpopulation. It would be unusual if this statement were not true when the rank condition 17.2e holds in the population.

The hypothesis-of-no-selection problem (allowing  $y_2$  to be endogenous or not),  $H_0$ :  $\gamma_1 = 0$ , is tested using the usual 2SLS t statistic for  $\hat{\gamma}_1$ . When  $\gamma_1 \neq 0$ , standard errors and test statistics should be corrected for the generated regressors problem, as in Chapter 6.

Example 17.7 (Education Endogenous and Sample Selection): In Example 17.6 we now allow educ to be endogenous in the wage offer equation, and we test for sample selection bias. Just as if we did not have a sample selection problem, we need IVs for educ that do not appear in the wage offer equation. As in Example 5.3, we use parents' education (motheduc, fatheduc) and husband's education as IVs. In addition,

{577}------------------------------------------------

we need some variables that affect labor force participation but not the wage offer; we use the same four variables as in Example 17.6. Therefore, all variables except educ (and, of course, the wage offer) are treated as exogenous.

Unless we have very reliable prior information, all exogenous variables should appear in the selection equation, and all should be listed as instruments in estimating equation (17.29) by 2SLS. Dropping some exogenous variables in either the selection equation or in estimating equation (17.29) imposes exclusion restrictions on a reducedform equation, something that can be dangerous and is unnecessary. Therefore, in the labor force participation equation we include exper, exper2, nwifeinc, kidslt6, kidsge6, motheduc, fatheduc, and huseduc (not educ). In estimating equation (17.29), the same set of variables, along with ^l3, are used as IVs. The 2SLS coefficient on ^l<sup>3</sup> is .040 (se ¼ :133), and so, again, there is little evidence of sample selection bias. The coefficient on educ is .088 (se ¼ :021), which is similar to the 2SLS estimate obtained without the sample selection correction (see Example 5.3). Because there is little evidence of sample selection bias, the standard errors are not corrected for first-stage estimation of *d*3.

Importantly, Procedure 17.2 applies to any kind of endogenous variable y2, including binary and other discrete variables, without any additional assumptions. This statement is true because the reduced form for y<sup>2</sup> is just a linear projection; we do not have to assume, for example, that v<sup>2</sup> is normally distributed or even independent of z. As an example, we might wish to look at the effects of participation in a job training program on the subsequent wage offer, accounting for the fact that not all who participated in the program will be employed in the following period (y<sup>2</sup> is always observed in this case). If participation is voluntary, an instrument for it might be whether the person was randomly chosen as a potential participant.

Even if y<sup>2</sup> is exogenous in the population equation (17.25), when y<sup>2</sup> is sometimes missing we generally need an instrument for y<sup>2</sup> when selection is not ignorable [that is, Eðu<sup>1</sup> j z1; y2; y3Þ 0Eðu1Þ]. In Example 17.4 we could use family background variables and another test score, such as KWW, as IVs for IQ, assuming these are always observed. We would generally include all such variables in the reduced-form selection equation. Procedure 17.2 works whether we assume IQ is a proxy variable for ability or an indicator of ability (see Chapters 4 and 5).

As a practical matter, we should have at least two elements of z that are not also in z1; that is, we need at least two exclusion restrictions in the structural equation. Intuitively, for the procedure to be convincing, we should have at least one instrument for y<sup>2</sup> and another exogenous variable that determines selection. Suppose that the scalar z<sup>2</sup> is our only exogenous variable excluded from equation (17.25). Then,

{578}------------------------------------------------

under random sampling, the equation would be just identified. When we account for sample selection bias, the Mills ratio term in equation (17.29) is a function of z<sup>1</sup> and z2. While the nonlinearity of the Mills ratio technically allows us to identify *d*<sup>1</sup> and a1, it is unlikely to work very well in practice because of severe multicollinearity among the IVs. This situation is analogous to using the standard Heckit method when there are no exclusion restrictions in the structural equation (see Section 17.4.1).

If we make stronger assumptions, it is possible to estimate model (17.25)–(17.27) by partial maximum likelihood of the kind discussed in Problem 13.7. One possibility is to assume that ðu1; v2; v3Þ is trivariate normal and independent of z. In addition to ruling out discrete y2, such a procedure would be computationally difficult. If y<sup>2</sup> is binary, we can model it as y<sup>2</sup> ¼ 1½z*d*<sup>2</sup> þ v<sup>2</sup> > 0, where v<sup>2</sup> j z@ Normalð0; 1Þ. But maximum likelihood estimation that allows any correlation matrix for ðu1; v2; v3Þ is complicated and less robust than Procedure 17.2.