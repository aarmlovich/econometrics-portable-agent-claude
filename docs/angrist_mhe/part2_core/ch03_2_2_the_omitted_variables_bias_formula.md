# The Omitted Variables Bias Formula

> Pages: 59-62

The omitted variables bias (OVB) formula describes the relationship between regression estimates in models with di§erent sets of control variables. This important formula is often motivated by the notion that a longer regression, i.e., one with more controls such as equation [\(3.2.9\)](#page-59-0), has a causal interpretation, while a shorter regression does not. The coe¢ cients on the variables included in the shorter regression are therefore said to be "biased". In fact, the OVB formula is a mechanical link between coe¢ cient vectors that applies to short and long regressions whether or not the longer regression is causal. Nevertheless, we follow convention and refer to the di§erence between the included coe¢ cients in a long regression and a short regression as being determined by the OVB formula.

To make this discussion concrete, suppose the set of relevant control variables in the schooling regression can be boiled down to a combination of family background, intelligence and motivation. Let these speciÖc factors be denoted by a vector, A<sup>i</sup> , which weíll refer to by the shorthand term ìability.î The regression of

{60}------------------------------------------------

very lucky college dropouts).

wages on schooling,  $S_i$ , controlling for ability can written as

<span id="page-60-0"></span>
$$Y_i = \alpha + \rho S_i + A_i' \gamma + \varepsilon_i, \qquad (3.2.10)$$

where  $\alpha$ ,  $\rho$ , and  $\gamma$  are population regression coefficients, and  $\varepsilon_i$  is a regression residual that is uncorrelated with all regressors by definition. If the CIA applies given  $A_i$ , then  $\rho$  can be equated with the coefficient in the linear causal model, 3.2.7, while the residual  $\varepsilon_i$  is the random part of potential earnings that is left over after controlling for  $A_i$ .

In practice, ability is hard to measure. For example, the American Current Population Survey (CPS), a large data set widely used in applied microeconomics (and the source of U.S. government data on unemployment rates), tells us nothing about adult respondents' family background, intelligence, or motivation. What are the consequences of leaving ability out of regression (3.2.10)? The resulting "short regression" coefficient is related to the "long regression" coefficient in equation (3.2.10) as follows:

$$\frac{Cov(\mathbf{Y}_i, \mathbf{S}_i)}{V(\mathbf{S}_i)} = \rho + \gamma' \delta_{As}, \tag{3.2.11}$$

where  $\delta_{As}$  is the vector of coefficients from regressions of the elements of  $A_i$  on  $s_i$ . To paraphrase, the OVB formula says

Short equals long plus the effect of omitted times the regression of omitted on included.

This formula is easy to derive: plug the long regression into the short regression formula,  $\frac{Cov(\gamma_i, s_i)}{V(s_i)}$ . Not surprisingly, the OVB formula is closely related to the regression anatomy formula, 3.1.3, from Section 3.1.2. Both the OVB and regression anatomy formulas tell us that short and long regression coefficients are the same whenever the omitted and included variables are uncorrelated.<sup>10</sup>

We can use the OVB formula to get a sense of the likely consequences of omitting ability for schooling coefficients. Ability variables have positive effects on wages, and these variables are also likely to be positively correlated with schooling. The short regression coefficient may therefore be "too big" relative to what we want. On the other hand, as a matter of economic theory, the direction of the correlation between schooling and ability is not entirely clear. Some omitted variables may be negatively correlated with schooling, in which case the short regression coefficient will be too small.<sup>11</sup>

<span id="page-60-2"></span><span id="page-60-1"></span>There is the multivariate generalization of OVB: Let  $\beta_1^s$  denote the coefficient vector on a  $K_1 \times 1$  vector of variables,  $X_{1i}$  in a (short) regression that has no other variables and let  $\beta_1^l$  denote the coefficient vector on these variables in a (long) regression that includes a  $K_2 \times 1$  vector of control variables,  $X_{2i}$ , with coefficient vector  $\beta_2^l$ . Then  $\beta_1^s = \beta_1^l + E[X_{1i}X'_{1i}]^{-1}E[X_{1i}X'_{2i}]\beta_2^l$ .

The highly educated people, we like to assume that ability and schooling are positively correlated. This is not a foregone conclusion, however: Mick Jagger dropped out of the London School of Economics and Bill Gates dropped out of Harvard, perhaps because the opportunity cost of schooling for these high-ability guys was high (of course, they may also be a couple of


{61}------------------------------------------------

Table [3.2.1](#page-61-0) illustrates these points using data from the NLSY. The Örst three entries in the table show that the schooling coe¢ cient decreases from .132 to .114 when family background variablesó in this case, parentsíeducationó as well as a few basic demographic characteristics (age, race, census region of residence) are included as controls. Further control for individual ability, as proxied by the Armed Forces QualiÖcation Test (AFQT) test score, reduces the schooling coe¢ cient to .087 (AFQT is used by the military to select soldiers). The omitted variables bias formula tells us that these reductions are a result of the fact that the additional controls are positively correlated with both wages and schooling.[12](#page-61-1)

<span id="page-61-0"></span>

<table><tbody><tr><th colspan="9">Table 3.2.1: Estimates of the returns to education for men in the NLSY</th></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>Controls:</td><td>None</td><td>Age</td><td>Col. (2) and</td><td>Col. (3) and</td><td>Col. (4), with</td></tr><tr><td></td><td></td><td>dummies</td><td>additional</td><td>AFQT score</td><td>occupation</td></tr><tr><td></td><td></td><td></td><td>controls*</td><td></td><td>dummies</td></tr><tr><td></td><td>0.132</td><td>0.131</td><td>0.114</td><td>0.087</td><td>0.066</td></tr><tr><td></td><td>(0.007)</td><td>(0.007)</td><td>(0.007)</td><td>(0.009)</td><td>(0.010)</td></tr></tbody></table>

Notes: Data are from the National Longitudinal Survey of Youth (1979 cohort, 2002 survey). The table reports the coe¢ cient on years of schooling in a regression of log wages on years of schooling and the indicated controls. Standard errors are shown in parentheses. The sample is restricted to men and weighted by NLSY sampling weights. The sample size is 2434.

Although simple, the OVB formula is one of the most important things to know about regression. The importance of the OVB formula stems from the fact that if you claim an absence of omitted variables bias, then typically youíre also saying that the regression youíve got is the one you want. And the regression you want usually has a causal interpretation. In other words, youíre prepared to lean on the CIA for a causal interpretation of the long-regression estimates.

At this point, itís worth considering when the CIA is most likely to give a plausible basis for empirical work. The best-case scenario is random assignment of s<sup>i</sup> , conditional on X<sup>i</sup> , in some sort of (possibly natural) experiment. An example is the study of a mandatory re-training program for unemployed workers by Black, et al. (2003). The authors of this study were interested in whether the re-training program succeeded in raising earnings later on. They exploit the fact that eligibility for the training program they study was determined on the basis of personal characteristics and past unemployment and job histories. Workers were divided up into groups on the basis of these characteristics. While some of these groups of workers were ineligible for training, those in other groups were required to take training if they did not take

<sup>\*</sup>Additional controls are motherís and fatherís years of schooling and dummy variables for race and Census region.

<span id="page-61-1"></span><sup>1 2</sup>A large empirical literature investigates the consequences of omitting ability variables from schooling equations. Key early references include Griliches and Mason (1972), Taubman (1976), Griliches (1977), and Chamberlain (1978).

{62}------------------------------------------------

a job. When some of the mandatory training groups contained more workers than training slots, training opportunities were distributed by lottery. Hence, training requirements were randomly assigned conditional on the covariates used to assign workers to groups. A regression on a dummy for training plus the personal characteristics, past unemployment variables, and job history variables used to classify workers seems very likely to provide reliable estimates of the causal e§ect of training.[13](#page-62-0)

In the schooling context, there is usually no lottery that directly determines whether someone will go to college or Önish high school.[14](#page-62-1) Still, we might imagine subjecting individuals of similar ability and from similar family backgrounds to an experiment that encourages school attendance. The Education Maintenance Allowance, which pays British high school students in certain areas to attend school, is one such policy experiment (Dearden, et al, 2004).

A second type of study that favors the CIA exploits detailed institutional knowledge regarding the process that determines s<sup>i</sup> . An example is the Angrist (1998) study of the e§ect of voluntary military service on the later earnings of soldiers. This research asks whether men who volunteered for service in the US Armed Forces were economically better o§ in the long run. Since voluntary military service is not randomly assigned, we can never know for sure. Angrist therefore used matching and regression techniques to control for observed di§erences between veterans and nonveterans who applied to get into the all-volunteer forces between 1979 and 1982. The motivation for a control strategy in this case is the fact that the military screens soldier-applicants primarily on the basis of observable covariates like age, schooling, and test scores.

The CIA in Angrist (1998) amounts to the claim that after conditioning on all these observed characteristics veterans and nonveterans are comparable. This assumption seems worth entertaining since, conditional on X<sup>i</sup> , variation in veteran status in the Angrist (1998) study comes solely from the fact that some qualiÖed applicants fail to enlist at the last minute. Of course, the considerations that lead a qualiÖed applicant to ìdrop outî of the enlistment process could be related to earnings potential, so the CIA is clearly not guaranteed even in this case.