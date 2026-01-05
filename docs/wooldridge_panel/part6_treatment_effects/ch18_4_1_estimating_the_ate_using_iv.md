# Estimating the ATE Using IV

> Pages: 628-640

In studying IV procedures, it is useful to write the observed outcome y as in equation (18.10):

$$y = \mu_0 + (\mu_1 - \mu_0)w + v_0 + w(v_1 - v_0)$$
(18.25)

However, unlike in Section 18.3, we do not assume that v<sup>0</sup> and v<sup>1</sup> are mean independent of w, given x. Instead, we assume the availability of instruments, which we collect in the vector z. (Here we separate the extra instruments from the covariates, so that x and z do not overlap. In many cases z is a scalar, but the analysis is no easier in that case.)

If we assume that the stochastic parts of y<sup>1</sup> and y<sup>0</sup> are the same, that is, v<sup>1</sup> ¼ v0, then the interaction term disappears (and ATE ¼ ATE1). Without the interaction term we can use standard IV methods under weak assumptions.

ASSUMPTION ATE.2: (a) In equation (18.25), 
$$v_1 = v_0$$
; (b)  $L(v_0 | \mathbf{x}, \mathbf{z}) = L(v_0 | \mathbf{x})$ ; and (c)  $L(w | \mathbf{x}, \mathbf{z}) \neq L(w | \mathbf{x})$ .

All linear projections in this chapter contain unity, which we suppress for notational simplicity.

{629}------------------------------------------------

Under parts a and b of Assumption ATE.2, we can write

$$y = \delta_0 + \alpha w + \mathbf{x} \boldsymbol{\beta}_0 + u_0 \tag{18.26}$$

where a ¼ ATE and u<sup>0</sup> 1 v<sup>0</sup> Lðv<sup>0</sup> j x; zÞ. By definition, u<sup>0</sup> has zero mean and is uncorrelated with ðx; zÞ, but w and u<sup>0</sup> are generally correlated, which makes OLS estimation of equation (18.26) inconsistent. The redundancy of z in the linear projection Lðv<sup>0</sup> j x; zÞ means that z is appropriately excluded from equation (18.26); this is the part of identification that we cannot test (except indirectly using the overidentification test from Chapter 6). Part c means that z has predictive power in the linear projection of treatment on ðx; zÞ; this is the standard rank condition for identification from Chapter 5, and we can test it using a first-stage regression and heteroskedasticity-robust tests of exclusion restrictions. Under Assumption ATE.2, a [and the other parameters in equation (18.26)] are identified, and they can be consistently estimated by 2SLS. Because the only endogenous explanatory variable in equation (18.26) is binary, equation (18.25) is called a dummy endogenous variable model (Heckman, 1978). As we discussed in Chapter 5, there are no special considerations in estimating equation (18.26) by 2SLS when the endogenous explanatory variable is binary.

Assumption ATE.2b holds if the instruments z are independent of ðy0; xÞ. For example, suppose z is a scalar determining eligibility in a job training program or some other social program. Actual participation, w, might be correlated with v0, which could contain unobserved ability. If eligibility is randomly assigned, it is often reasonable to assume that z is independent of ðy0; xÞ. Eligibility would positively influence participation, and so Assumption ATE.2c should hold.

Random assignment of eligibility is no guarantee that eligibility is a valid instrument for participation. The outcome of z could affect other behavior, which could feed back into u<sup>0</sup> in equation (18.26). For example, consider Angrist's (1990) draft lottery application, where draft lottery number is used as an instrument for enlisting. Lottery number clearly affected enlistment, so Assumption ATE.2c is satisfied. Assumption ATE.2b is also satisfied if men did not change behavior in unobserved ways that affect wage, based on their lottery number. One concern is that men with low lottery numbers may get more education as a way of avoiding service through a deferment. Including years of education in x effectively solves this problem. But what if men with high draft lottery numbers received more job training because employers did not fear losing them? If a measure of job training status cannot be included in x, lottery number would generally be correlated with u0. See AIR and Heckman (1997) for additional discussion.

{630}------------------------------------------------

As the previous discussion implies, the redundancy condition in Assumption ATE.2b allows the instruments z to be correlated with elements of x. For example, in the population of high school graduates, if w is a college degree indicator and the instrument z is distance to the nearest college while attending high school, then z is allowed to be correlated with other controls in the wage equation, such as geographic indicators.

Under v<sup>1</sup> ¼ v<sup>0</sup> and the key assumptions on the instruments, 2SLS on equation (18.26) is consistent and asymptotically normal. But if we make stronger assumptions, we can find a more efficient IV estimator.

assumption ATE.2<sup>0</sup> : (a) In equation (18.25), v<sup>1</sup> ¼ v0; (b) Eðv<sup>0</sup> j x; zÞ ¼ Lðv<sup>0</sup> j xÞ; (c) Pðw ¼ 1 j x; zÞ 0Pðw ¼ 1 j xÞ and Pðw ¼ 1 j x; zÞ ¼ Gðx; z; *g*Þ is a known parametric form (usually probit or logit); and (d) Varðv<sup>0</sup> j x; zÞ ¼ s<sup>2</sup> 0 .

Part b assumes that Eðv<sup>0</sup> j xÞ is linear in x, and so it is more restrictive than Assumption ATE.2b. It does not usually hold for discrete response variables y, although it may be a reasonable approximation in some cases. Under parts a and b, the error u<sup>0</sup> in equation (18.26) has a zero conditional mean:

$$\mathbf{E}(u_0 \mid \mathbf{x}, \mathbf{z}) = 0 \tag{18.27}$$

Part d implies that Varðu<sup>0</sup> j x; zÞ is constant. From the results on efficient choice of instruments in Section 14.5.3, the optimal IV for w is Eðw j x; zÞ ¼ Gðx; z; *g*Þ. Therefore, we can use a two-step IV method:

Procedure 18.1 (Under Assumption ATE.2<sup>0</sup> ): (a) Estimate the binary response model Pðw ¼ 1 j x; zÞ ¼ Gðx; z; *g*Þ by maximum likelihood. Obtain the fitted probabilities, G^i. The leading case occurs when Pðw ¼ 1 j x; zÞ follows a probit model.

(b) Estimate equation (18.26) by IV using instruments 1, G^i, and xi.

There are several nice features of this IV estimator. First, it can be shown that the conditions sufficient to ignore the estimation of *g* in the first stage hold; see Section 6.1.2. Therefore, the usual 2SLS standard errors and test statistics are asymptotically valid. Second, under Assumption ATE.2<sup>0</sup> , the IV estimator from step b is asymptotically efficient in the class of estimators where the IVs are functions of ðxi; ziÞ; see Problem 8.11. If Assumption ATE.2d does not hold, all statistics should be made robust to heteroskedasticity, and we no longer have the efficient IV estimator.

Procedure 18.1 has an important robustness property. Because we are using G^<sup>i</sup> as an instrument for wi, the model for Pðw ¼ 1 j x; zÞ does not have to be correctly specified. For example, if we specify a probit model for Pðw ¼ 1 j x; zÞ, we do not need the probit


{631}------------------------------------------------

model to be correct. Generally, what we need is that the linear projection of w onto ½x; Gðx; z; *g*Þ actually depends on Gðx; z; *g*Þ, where we use *g* to denote the plim of the maximum likelihood estimator when the model is misspecified (see White, 1982a). These requirements are fairly weak when z is partially correlated with w.

Technically, a and *b* are identified even if we do not have extra exogenous variables excluded from x. But we can rarely justify the estimator in this case. For concreteness, suppose that w given x follows a probit model [and we have no z, or z does not appear in Pðw ¼ 1 j x; zÞ]. Because Gðx; *g*Þ 1Fðg<sup>0</sup> þ x*g*1Þ is a nonlinear function of x, it is not perfectly correlated with x, so it can be used as an IV for w. This situation is very similar to the one discussed in Section 17.4.1: while identification holds for all values of a and *b* if *g*<sup>1</sup> 0 0, we are achieving identification off of the nonlinearity of Pðw ¼ 1 j xÞ. Further, Fðg<sup>0</sup> þ x*g*1Þ and x are typically highly correlated. As we discussed in Section 5.2.6, severe multicollinearity among the IVs can result in very imprecise IV estimators. In fact, if Pðw ¼ 1 j xÞ followed a linear probability model, a would not be identified. See Problem 18.5 for an illustration.

Example 18.3 (Estimating the Effects of Education on Fertility): We use the data in FERTIL2.RAW to estimate the effect of attaining at least seven years of education on fertility. The data are for women of childbearing age in Botswana. Seven years of education is, by far, the modal amount of positive education. (About 21 percent of women report zero years of education. For the subsample with positive education, about 33 percent report seven years of education.) Let y ¼ children, the number of living children, and let w ¼ educ7 be a binary indicator for at least seven years of education. The elements of x are age, age2, evermarr (ever married), urban (lives in an urban area), electric (has electricity), and tv (has a television).

The OLS estimate of ATE is :394 (se ¼ :050). We also use the variable frsthalf, a binary variable equal to one if the woman was born in the first half of the year, as an IV for educ7. It is easily shown that educ7 and frsthalf are significantly negatively related. The usual IV estimate is much larger in magnitude than the OLS estimate, but only marginally significant: 1:131 (se ¼ :619). The estimate from Procedure 18.1 is even bigger in magnitude, and very significant: 1:975 (se ¼ :332). The standard error that is robust to arbitrary heteroskedasticity is even smaller. Therefore, using the probit fitted values as an IV, rather than the usual linear projection, produces a more precise estimate (and one notably larger in magnitude).

The IV estimate of education effect seems very large. One possible problem is that, because children is a nonnegative integer that piles up at zero, the assumptions underlying Procedure 18.1—namely, Assumptions ATE.2<sup>0</sup> a and ATE.2<sup>0</sup> b—might not be met. In Chapter 19 we will discuss other methods for handling integer responses.

{632}------------------------------------------------

In principle, it is important to recognize that Procedure 18.1 is not the same as using G^ as a regressor in place of w. That is, IV estimation of equation (18.26) is not the same as the OLS estimator from

$$y_i \text{ on } 1, \hat{G}_i, \mathbf{x}_i \tag{18.28}$$

Consistency of the OLS estimators from regression (18.28) relies on having the model for Pðw ¼ 1 j x; zÞ correctly specified. If the first three parts of Assumption ATE.2<sup>0</sup> hold, then

$$E(y \mid \mathbf{x}, \mathbf{z}) = \delta_0 + \alpha G(\mathbf{x}, \mathbf{z}; \boldsymbol{\gamma}) + \mathbf{x}\boldsymbol{\beta}$$

and, from the results on generated regressors in Chapter 6, the estimators from regression (18.28) are generally consistent. Procedure 18.1 is more robust because it does not require Assumption ATE.2<sup>0</sup> c for consistency.

Another problem with regression (18.28) is that the usual OLS standard errors and test statistics are not valid, for two reasons. First, if Varðu<sup>0</sup> j x; zÞ is constant, Varðy j x; zÞ cannot be constant because Varðw j x; zÞ is not constant. By itself this is a minor nuisance because heteroskedasticity-robust standard errors and test statistics are easy to obtain. [However, it does call into question the efficiency of the estimator from regression (18.28).] A more serious problem is that the asymptotic variance of the estimator from regression (18.28) depends on the asymptotic variance of *g*^ unless a ¼ 0, and the heteroskedasticity-robust standard errors do not correct for this.

In summary, using fitted probabilities from a first-stage binary response model, such as probit or logit, as an instrument for w is a nice way to exploit the binary nature of the endogenous explanatory variable. In addition, the asymptotic inference is always standard. Using G^<sup>i</sup> as an instrument does require the assumption that Eðv<sup>0</sup> j x; zÞ depends only on x and is linear in x, which can be more restrictive than Assumption ATE.2b.

Allowing for the interaction wðv<sup>1</sup> v0Þ in equation (18.25) is notably harder. In general, when v<sup>1</sup> 0v0, the IV estimator (using z or G^ as IVs for w) does not consistently estimate ATE (or ATE1). Nevertheless, it is useful to find assumptions under which IV estimation does consistently estimate ATE. This problem has been studied by Angrist (1991), Heckman (1997), and Wooldridge (1997b), and we synthesize results from these papers.

Under the conditional mean redundancy assumptions

$$E(v_0 \mid \mathbf{x}, \mathbf{z}) = E(v_0 \mid \mathbf{x}) \quad \text{and} \quad E(v_1 \mid \mathbf{x}, \mathbf{z}) = E(v_1 \mid \mathbf{x})$$
(18.29)

we can always write equation (18.25) as

$$y = \mu_0 + \alpha w + g_0(\mathbf{x}) + w[g_1(\mathbf{x}) - g_0(\mathbf{x})] + e_0 + w(e_1 - e_0)$$
(18.30)

{633}------------------------------------------------

where a is the ATE and

$$v_0 = g_0(\mathbf{x}) + e_0, \qquad \mathbf{E}(e_0 \mid \mathbf{x}, \mathbf{z}) = 0$$
 (18.31)

$$v_1 = g_1(\mathbf{x}) + e_1, \qquad \mathbf{E}(e_1 \mid \mathbf{x}, \mathbf{z}) = 0$$
 (18.32)

Given functional form assumptions for g<sup>0</sup> and g1—which would typically be linear in parameters—we can estimate equation (18.30) by IV, where the error term is e<sup>0</sup> þ wðe<sup>1</sup> e0Þ. For concreteness, suppose that

$$g_0(\mathbf{x}) = \eta_0 + \mathbf{x}\boldsymbol{\beta}_0, \qquad g_1(\mathbf{x}) - g_0(\mathbf{x}) = (\mathbf{x} - \boldsymbol{\psi})\boldsymbol{\delta}$$
(18.33)

where *c* ¼ EðxÞ. If we plug these equations into equation (18.30), we need instruments for w and wðx *c*Þ (note that x does not contain a constant here). If q1qðx; zÞ is the instrument for w (such as the response probability in Procedure 18.1), the natural instrument for w x is q x. (And, if q is the efficient IV for w, q x is the efficient instrument for w x.) When will applying IV to

$$y = \gamma + \alpha w + \mathbf{x}\boldsymbol{\beta}_0 + w(\mathbf{x} - \boldsymbol{\psi})\boldsymbol{\delta} + e_0 + w(e_1 - e_0)$$
(18.34)

be consistent? If the last term disappears, and, in particular, if

$$e_1 = e_0 (18.35)$$

then the error e<sup>0</sup> has zero mean given ðx; zÞ; this result means that IV estimation of equation (18.34) produces consistent, asymptotically normal estimators.

assumption ATE.3: With y expressed as in equation (18.25), conditions (18.29), (18.33), and (18.35) hold. In addition, Assumption ATE.2<sup>0</sup> c holds.

We have the following extension of Procedure 18.1:

Procedure 18.2 (Under Assumption ATE.3): (a) Same as Procedure 18.1.

(b) Estimate the equation

$$y_i = \gamma + \alpha w_i + \mathbf{x}_i \boldsymbol{\beta}_0 + [w_i(\mathbf{x}_i - \overline{\mathbf{x}})] \boldsymbol{\delta} + error_i$$
 (18.36)

by IV, using instruments 1, G^i, xi, and G^iðx<sup>i</sup> xÞ.

If we add Assumption ATE.2<sup>0</sup> d, Procedure 18.2 produces the efficient IV estimator [when we ignore estimation of EðxÞ]. As with Procedure 18.1, we do not actually need the binary response model to be correctly specified for identification. As an alternative, we can use z<sup>i</sup> and interactions between z<sup>i</sup> and x<sup>i</sup> as instruments, which generally results in testable overidentifying restrictions.

Technically, the fact that x is an estimator of EðxÞ should be accounted for in computing the standard errors of the IV estimators. But, as shown in Problem 6.10, 

{634}------------------------------------------------

the adjustments for estimating EðxÞ can be expected to have a trivial effect on the standard errors; in practice, we can just use the usual or heteroskedasticity-robust standard errors.

Example 18.4 (An IV Approach to Evaluating Job Training): To evaluate the effects of a job training program on subsequent wages, suppose that x includes education, experience, and the square of experience. If z indicates eligibility in the program, we would estimate the equation

$$\begin{split} \log(wage) &= \mu_0 + \alpha \ jobtrain + \beta_{01}educ + \beta_{02}exper + \beta_{03}exper^2 \\ &+ \delta_1 \ jobtrain \cdot (educ - \overline{educ}) + \delta_2 \ jobtrain \cdot (exper - \overline{exper}) \\ &+ \delta_3 \ jobtrain \cdot (exper^2 - \overline{exper}^2) + error \end{split}$$

by IV, using instruments 1, z, educ, exper, exper2, and interactions of z with all demeaned covariates. Notice that for the last interaction, we subtract off the average of exper2. Alternatively, we could use in place of z the fitted values from a probit of jobtrain on ðx; zÞ.

Procedure 18.2 is easy to carry out, but its consistency generally hinges on condition (18.35), not to mention the functional form assumptions in equation (18.33). We can relax condition (18.35) to

$$E[w(e_1 - e_0) | \mathbf{x}, \mathbf{z}] = E[w(e_1 - e_0)]$$
(18.37)

We do not need wðe<sup>1</sup> e0Þ to have zero mean, as a nonzero mean only affects the intercept. It is important to see that correlation between w and ðe<sup>1</sup> e0Þ does not invalidate the IV estimator of a from Procedure 18.2. However, we must assume that the covariance conditional on ðx; zÞ is constant. Even if this assumption is not exactly true, it might be approximately true.

It is easy to see why, along with conditions (18.29) and (18.33), condition (18.37) implies consistency of the IV estimator. We can write equation (18.34) as

$$y = \xi + \alpha w + \mathbf{x} \boldsymbol{\beta}_0 + w(\mathbf{x} - \boldsymbol{\psi}) \boldsymbol{\delta} + e_0 + r$$
(18.38)

where r ¼ wðe<sup>1</sup> e0Þ E½wðe<sup>1</sup> e0Þ and x ¼ g þ E½wðe<sup>1</sup> e0Þ-. Under condition (18.37), Eðrj x; zÞ ¼ 0, and so the composite error e<sup>0</sup> þ r has zero mean conditional on ðx; zÞ. Therefore, any function of ðx; zÞ can be used as instruments in equation (18.38). Under the following modification of Assumption ATE.3, Procedure 18.2 is still consistent:

assumption ATE.3<sup>0</sup> : With y expressed as in equation (18.25), conditions (18.29), (18.33), and (18.37) hold. In addition, Assumption ATE.2<sup>0</sup> c holds.

{635}------------------------------------------------

Even if Assumption ATE.2<sup>0</sup> d holds in addition to Assumption ATE.2<sup>0</sup> c, the IV estimator is generally not efficient because Varðrj x; zÞ would typically be heteroskedastic.

Angrist (1991) provided primitive conditions for assumption (18.37) in the case where z is independent of ðy0; y1; xÞ. Then, the covariates can be dropped entirely from the analysis (leading to IV estimation of the simple regression equation y ¼ x þ aw þ error). We can extend those conditions here to allow z and x to be correlated. Assume that

$$E(w \mid \mathbf{x}, \mathbf{z}, e_1 - e_0) = h(\mathbf{x}, \mathbf{z}) + k(e_1 - e_0)$$
(18.39)

for some functions hðÞ and kðÞ and that

$$e_1 - e_0$$
 is independent of  $(\mathbf{x}, \mathbf{z})$  (18.40)

Under these two assumptions,

$$E[w(e_1 - e_0) | \mathbf{x}, \mathbf{z}] = h(\mathbf{x}, \mathbf{z}) E(e_1 - e_0 | \mathbf{x}, \mathbf{z}) + E[(e_1 - e_0)k(e_1 - e_0) | \mathbf{x}, \mathbf{z}]$$

$$= h(\mathbf{x}, \mathbf{z}) \cdot 0 + E[(e_1 - e_0)k(e_1 - e_0)]$$

$$= E[(e_1 - e_0)k(e_1 - e_0)]$$
(18.41)

which is just an unconditional moment in the distribution of e<sup>1</sup> e0. We have used the fact that Eðe<sup>1</sup> e<sup>0</sup> j x; zÞ ¼ 0 and that any function of e<sup>1</sup> e<sup>0</sup> is independent of ðx; zÞ under assumption (18.40). If we assume that kðÞ is the identity function (as in Wooldridge, 1997b), then equation (18.41) is Varðe<sup>1</sup> e0Þ.

Assumption (18.40) is reasonable for continuously distributed responses, but it would not generally be reasonable when y is a discrete response or corner solution outcome. Further, even if assumption (18.40) holds, assumption (18.39) is violated when w given x, z, and ðe<sup>1</sup> e0Þ follows a standard binary response model. For example, a probit model would have

$$P(w = 1 \mid \mathbf{x}, \mathbf{z}, e_1 - e_0) = \Phi[\pi_0 + \mathbf{x}\pi_1 + \mathbf{z}\pi_2 + \rho(e_1 - e_0)]$$
(18.42)

which is not separable in ðx; zÞ and ðe<sup>1</sup> e0Þ. Nevertheless, assumption (18.39) might be a reasonable approximation in some cases. Without covariates, Angrist (1991) presents simulation evidence that suggests the simple IV estimator does quite well for estimating the ATE even when assumption (18.39) is violated.

Rather than assuming (18.39), different approaches are available, but they require different assumptions. We first consider a solution that involves adding a nonlinear function of ðx; zÞ to equation (18.38) and estimating the resulting equation by 2SLS. We add to assumptions (18.40) and (18.42) a normality assumption,

{636}------------------------------------------------

$$e_1 - e_0 \sim \text{Normal}(0, \tau^2) \tag{18.43}$$

Under assumptions (18.40), (18.42), and (18.43) we can derive an estimating equation to show that ATE is usually identified.

To derive an estimating equation, note that conditions (18.40), (18.42), and (18.43) imply that

$$P(w = 1 \mid \mathbf{x}, \mathbf{z}) = \Phi(\theta_0 + \mathbf{x}\boldsymbol{\theta}_1 + \mathbf{z}\boldsymbol{\theta}_2)$$
(18.44)

where each theta is the corresponding pi multiplied by  $[1 + \rho^2 \tau^2]^{-1/2}$ . If we let a denote the latent error underlying equation (18.44) (with a standard normal distribution), and define  $c \equiv e_1 - e_0$ , then conditions (18.40), (18.42), and (18.43) imply that (a, c) has a zero-mean bivariate normal distribution that is independent of  $(\mathbf{x}, \mathbf{z})$ . Therefore,  $\mathbf{E}(c \mid a, \mathbf{x}, \mathbf{z}) = \mathbf{E}(c \mid a) = \xi a$  for some parameter  $\xi$ , and

$$E(wc \mid \mathbf{x}, \mathbf{z}) = E[wE(c \mid a, \mathbf{x}, \mathbf{z}) \mid \mathbf{x}, \mathbf{z}] = \xi E(wa \mid \mathbf{x}, \mathbf{z}).$$

Using the fact that  $a \sim \text{Normal}(0, 1)$  and is independent of  $(\mathbf{x}, \mathbf{z})$ , we have

$$E(wa \mid \mathbf{x}, \mathbf{z}) = \int_{-\infty}^{\infty} 1[\theta_0 + \mathbf{x}\boldsymbol{\theta}_1 + \mathbf{z}\boldsymbol{\theta}_2 + a \ge 0]a\phi(a) da$$
$$= \phi(-\{\theta_0 + \mathbf{x}\boldsymbol{\theta}_1 + \mathbf{z}\boldsymbol{\theta}_2\}) = \phi(\theta_0 + \mathbf{x}\boldsymbol{\theta}_1 + \mathbf{z}\boldsymbol{\theta}_2)$$
(18.45)

where  $\phi(\cdot)$  is the standard normal density. Therefore, we can now write

$$y = \gamma + \alpha w + \mathbf{x}\boldsymbol{\beta} + w(\mathbf{x} - \boldsymbol{\psi})\boldsymbol{\delta} + \xi \phi(\theta_0 + \mathbf{x}\boldsymbol{\theta}_1 + \mathbf{z}\boldsymbol{\theta}_2) + e_0 + r$$
(18.46)

where  $r = wc - \mathrm{E}(wc \mid \mathbf{x}, \mathbf{z})$ . The composite error in (18.46) has zero mean conditional on  $(\mathbf{x}, \mathbf{z})$ , and so we can estimate the parameters using IV methods. One catch is the nonlinear function  $\phi(\theta_0 + \mathbf{x}\theta_1 + \mathbf{z}\theta_2)$ . We could use nonlinear two stage least squares, as described in Chapter 14. But a two-step approach is easier. First, we gather together the assumptions:

ASSUMPTION ATE.4: With y written as in equation (18.25), maintain assumptions (18.29), (18.33), (18.40), (18.42) (with  $\pi_2 \neq \mathbf{0}$ ), and (18.43).

Procedure 18.3 (Under Assumption ATE.4): (a) Estimate  $\theta_0$ ,  $\theta_1$ , and  $\theta_2$  from a probit of w on  $(1, \mathbf{x}, \mathbf{z})$ . Form the predicted probabilities,  $\hat{\mathbf{\Phi}}_i$ , along with  $\hat{\boldsymbol{\phi}}_i = \phi(\hat{\theta}_0 + \mathbf{x}_i\hat{\boldsymbol{\theta}}_1 + \mathbf{z}_i\hat{\boldsymbol{\theta}}_2)$ , i = 1, 2, ..., N.

(b) Estimate the equation

$$y_i = \gamma + \alpha w_i + \mathbf{x}_i \boldsymbol{\beta}_0 + w_i (\mathbf{x}_i - \overline{\mathbf{x}}) \boldsymbol{\delta} + \xi \hat{\boldsymbol{\phi}}_i + error_i$$
 (18.47)

by IV, using instruments  $[1, \hat{\Phi}_i, \mathbf{x}_i, \hat{\Phi}_i(\mathbf{x}_i - \overline{\mathbf{x}}), \hat{\phi}_i]$ .

{637}------------------------------------------------

The term  $\hat{\phi}_i \equiv \phi(\hat{\theta}_0 + \mathbf{x}_i\hat{\boldsymbol{\theta}}_1 + \mathbf{z}_i\hat{\boldsymbol{\theta}}_2)$  in equation (18.47) is another example of a control function, although, unlike in Section 18.3, it is obtained from instrumental variables assumptions, rather than ignorability of treatment assumptions.

Even if  $\xi \neq 0$ , the effect of adding  $\hat{\phi}_i$  to the estimate of  $\alpha$  can be small. Consider the version of (18.46) without covariates  $\mathbf{x}$  and with a scalar instrument, z:

$$y = \gamma + \alpha w + \xi \phi(\theta_0 + \theta_1 z) + u, \qquad E(u \mid z) = 0$$
 (18.48)

This equation holds, for example, if the instrument z is independent of  $(\mathbf{x}, v_0, v_1)$ . The simple IV estimator of  $\alpha$  is obtained by omitting  $\phi(\theta_0 + \theta_1 z)$ . If we use z as an IV for w, the simple IV estimator is consistent provided z and  $\phi(\theta_0 + \theta_1 z)$  are uncorrelated. (Remember, having an omitted variable that is uncorrelated with the IV does not cause inconsistency of the IV estimator.) Even though  $\phi(\theta_0 + \theta_1 z)$  is a function of z, these two variables might have small correlation because z is monotic while  $\phi(\theta_0 + \theta_1 z)$  is symmetric about  $-(\theta_0/\theta_1)$ . This discussion shows that condition (18.37) is not necessary for IV to consistently estimate the ATE: It could be that while  $E[w(e_1 - e_0) \mid \mathbf{x}, \mathbf{z}]$  is not constant, it is roughly uncorrelated with  $\mathbf{x}$  (or the functions of  $\mathbf{x}$ ) that appear in (18.38), as well as with the functions of  $\mathbf{z}$  used as instruments.

Equation (18.48) illustrates another important point: If  $\xi \neq 0$  and the single instrument z is binary,  $\alpha$  is not identified. Lack of identification occurs because  $\phi(\theta_0 + \theta_1 z)$  takes on only two values, which means it is perfectly linearly related to z. So long as z takes on more than two values,  $\alpha$  is generally identified, although the identification is due to the fact that  $\phi(\cdot)$  is a different nonlinear function than  $\Phi(\cdot)$ . With  $\mathbf{x}$  in the model  $\hat{\phi}_i$  and  $\hat{\Phi}_i$  might be collinear, resulting in imprecise IV estimates.

Because r in (18.46) is heteroskedastic, the instruments below (18.47) are not optimal, and so we might simply use  $\mathbf{z}_i$  along with interactions of  $\mathbf{z}_i$  with  $(\mathbf{x}_i - \overline{\mathbf{x}})$  and  $\hat{\phi}_i$  as IVs. If  $\mathbf{z}_i$  has dimension greater than one, then we can test the overidentifying restrictions as a partial test of instrument selection and the normality assumptions. Of course, we could use the results of Chapter 14 to characterize and estimate the optimal instruments, but this is fairly involved [see, for example, Newey and McFadden (1994)].

A different approach to estimating the ATE when assumption (18.39) fails is to compute the expected value of y given the endogenous treatment and all exogenous variables: E(y | w, x, z). Finding this expectation requires somewhat more by way of assumptions, but it also has some advantages, which we discuss later. For completeness, we list a set of assumptions:

ASSUMPTION ATE.4': With y written as in equation (18.25), maintain assumptions (18.29) and (18.33). Furthermore, the treatment can be written as  $w = 1[\theta_0 + \mathbf{x}\boldsymbol{\theta}_1 +$ 

{638}------------------------------------------------

 $\mathbf{z}\theta_2 + a \ge 0$ ], where  $(a, e_0, e_1)$  is independent of  $(\mathbf{x}, \mathbf{z})$  with a trivariate normal distribution; in particular,  $a \sim \text{Normal}(0, 1)$ .

Under Assumption ATE.4', we can use calculations very similar to those used in Section 17.4.1 to obtain  $E(y|w, \mathbf{x}, \mathbf{z})$ . In particular,

$$E(y|w, \mathbf{x}, \mathbf{z}) = \gamma + \alpha w + \mathbf{x}\boldsymbol{\beta}_0 + w(\mathbf{x} - \boldsymbol{\psi})\boldsymbol{\delta} + \rho_1 w[\phi(\mathbf{q}\boldsymbol{\theta})/\Phi(\mathbf{q}\boldsymbol{\theta})]$$
$$+ \rho_2 (1 - w)\{\phi(\mathbf{q}\boldsymbol{\theta})/[1 - \Phi(\mathbf{q}\boldsymbol{\theta})]\}$$
(18.49)

where  $\mathbf{q}\boldsymbol{\theta} \equiv \theta_0 + \mathbf{x}\boldsymbol{\theta}_1 + \mathbf{z}\boldsymbol{\theta}_2$  and  $\rho_1$  and  $\rho_2$  are additional parameters. Heckman (1978) used this expectation to obtain two-step estimators of the switching regression model. [See Vella and Verbeek (1999) for a recent discussion of the switching regression model in the context of treatment effects.] Not surprisingly, (18.49) suggests a simple two-step procedure, where the first step is identical to that in Procedure 18.3:

Procedure 18.4 (Under Assumption ATE.4'): (a) Estimate  $\theta_0$ ,  $\theta_1$ , and  $\theta_2$  from a probit of w on  $(1, \mathbf{x}, \mathbf{z})$ . Form the predicted probabilities,  $\hat{\mathbf{\Phi}}_i$ , along with  $\hat{\boldsymbol{\phi}}_i = \phi(\hat{\theta}_0 + \mathbf{x}_i\hat{\boldsymbol{\theta}}_1 + \mathbf{z}_i\hat{\boldsymbol{\theta}}_2)$ , i = 1, 2, ..., N.

(b) Run the OLS regression

$$y_i \text{ on } 1, w_i, \mathbf{x}_i, w_i(\mathbf{x}_i - \overline{\mathbf{x}}), w_i(\hat{\phi}_i/\hat{\mathbf{\Phi}}_i), (1 - w_i)[\hat{\phi}_i/(1 - \hat{\mathbf{\Phi}}_i)]$$
 (18.50)

using all of the observations. The coefficient on  $w_i$  is a consistent estimator of  $\alpha$ , the ATE.

When we restrict attention to the  $w_i = 1$  subsample, thereby dropping  $w_i$  and  $w_i(\mathbf{x}_i - \overline{\mathbf{x}})$ , we obtain the sample selection correction from Section 17.4.1; see equation (17.24). (The treatment  $w_i$  becomes the sample selection indicator.) But the goal of sample selection corrections is very different from estimating an average treatment effect. For the sample selection problem, the goal is to estimate  $\boldsymbol{\beta}_0$ , which indexes  $E(y | \mathbf{x})$  in the population. By contrast, in estimating an ATE we are interested in the causal effect that w has on y.

It makes sense to check for joint significance of the last two regressors in regression (18.50) as a test of endogeneity of w. Because the coefficients  $\rho_1$  and  $\rho_2$  are zero under  $H_0$ , we can use the results from Chapter 6 to justify the usual Wald test (perhaps made robust to heteroskedasticity). If these terms are jointly insignificant at a sufficiently high level, we can justify the usual OLS regression without unobserved heterogeneity. If we reject  $H_0$ , we must deal with the generated regressors problem in obtaining a valid standard error for  $\hat{\alpha}$ .

Technically, Procedure 18.3 is more robust than Procedure 18.4 because the former does not require a trivariate normality assumption. Linear conditional expectations,

{639}------------------------------------------------

along with the assumption that w given ðx; zÞ follows a probit, suffice. In addition, Procedure 18.3 allows us to separate the issues of endogeneity of w and nonconstant treatment effect: if we ignore the estimation error involved with demeaning x<sup>i</sup> in the interaction term—which generally seems reasonable—then a standard t-test (perhaps made robut to heteroskedasticity) for H0: x ¼ 0 is valid for testing the presence of wðe<sup>1</sup> e0Þ, even when w is endogenous.

Practically, the extra assumption in Procedure 18.4 is that e<sup>0</sup> is independent of ðx; zÞ with a normal distribution. We may be willing to make this assumption, especially if the estimates from Procedure 18.3 are too imprecise to be useful. The efficiency issue is a difficult one because of the two-step estimation involved, but, intuitively, Procedure 18.4 is likely to be more efficient because it is based on Eðy j w; x; zÞ. Procedure 18.3 involves replacing the unobserved composite error with its expectation conditional only on ðx; zÞ. In at least one case, Procedure 18.4 gives results when Procedure 18.3 cannot: when x is not in the equation and there is a single binary instrument.

Under a variant of Assumption ATE.3<sup>0</sup> , we can consistently estimate ATE<sup>1</sup> by IV. As before, we express y as in equation (18.25). First, we show how to consistently estimate ATE1ðxÞ, which can be written as

$$ATE_1(\mathbf{x}) = E(y_1 - y_0 | \mathbf{x}, w = 1) = (\mu_1 - \mu_0) + E(v_1 - v_0 | \mathbf{x}, w = 1)$$

The following assumption identifies ATE1ðxÞ:

assumption ATE.3<sup>00</sup>: (a) With y expressed as in equation (18.25), the first part of assumption (18.29) holds, that is, Eðv<sup>0</sup> j x; zÞ ¼ Eðv<sup>0</sup> j xÞ; (b) Eðv<sup>1</sup> v<sup>0</sup> j x; z; w ¼ 1Þ ¼ Eðv<sup>1</sup> v<sup>0</sup> j x; w ¼ 1Þ; and (c) Assumption ATE.2<sup>0</sup> c holds.

We discussed part a of this assumption earlier, as it also appears in Assumption ATE.3<sup>0</sup> . It can be violated if agents change their behavior based on z. Part b deserves some discussion. Recall that v<sup>1</sup> v<sup>0</sup> is the person-specific gain from participation or treatment. Assumption ATE.3<sup>00</sup> requires that for those in the treatment group, the gain is not predictable given z, once x is controlled for. Heckman (1997) discusses Angrist's (1990) draft lottery example, where z (a scalar) is draft lottery number. Men who had a large z were virtually certain to escape the draft. But some men with large draft numbers chose to serve anyway. Even with good controls in x, it seems plausible that, for those who chose to serve, a higher z is associated with a higher gain to military service. In other words, for those who chose to serve, v<sup>1</sup> v<sup>0</sup> and z are positively correlated, even after controlling for x. This argument directly applies to estimation of ATE1; the effect on estimation of ATE is less clear.

{640}------------------------------------------------

Assumption ATE.3<sup>00</sup>b is plausible when z is a binary indicator for eligibility in a program, which is randomly determined and does not induce changes in behavior other than whether or not to participate.

To see how Assumption ATE.3<sup>00</sup> identifies ATE1ðxÞ, rewrite equation (18.25) as

$$y = \mu_0 + g_0(\mathbf{x}) + w[(\mu_1 - \mu_0) + \mathbf{E}(v_1 - v_0 \mid \mathbf{x}, w = 1)]$$

$$+ w[(v_1 - v_0) - \mathbf{E}(v_1 - v_0 \mid \mathbf{x}, w = 1)] + e_0$$

$$= \mu_0 + g_0(\mathbf{x}) + w \cdot ATE_1(\mathbf{x}) + a + e_0$$
(18.51)

where a1w½ðv<sup>1</sup> v0Þ Eðv<sup>1</sup> v<sup>0</sup> j x; w ¼ 1Þ and e<sup>0</sup> is defined in equation (18.31). Under Assumption ATE.3<sup>00</sup>a, Eðe<sup>0</sup> j x; zÞ ¼ 0. The hard part is dealing with the term a. When w ¼ 0, a ¼ 0. Therefore, to show that Eða j x; zÞ ¼ 0, it suffices to show that Eða j x; z; w ¼ 1Þ ¼ 0. [Remember, Eða j x; zÞ ¼ Pðw ¼ 0Þ Eða j x; z; w ¼ 0Þ þ Pðw ¼ 1Þ Eða j x; z; w ¼ 1Þ.] But this result follows under Assumption ATE.3<sup>00</sup>b:

$$E(a | \mathbf{x}, \mathbf{z}, w = 1) = E(v_1 - v_0 | \mathbf{x}, \mathbf{z}, w = 1) - E(v_1 - v_0 | \mathbf{x}, w = 1) = 0$$

Now, letting r1a þ e<sup>0</sup> and assuming that g0ðxÞ ¼ h<sup>0</sup> þ hðxÞ*b*<sup>0</sup> and ATE1ðxÞ ¼ t þ fðxÞ*d* for some row vector of functions hðxÞ and fðxÞ, we can write

$$y = \gamma_0 + \mathbf{h}_0(\mathbf{x})\boldsymbol{\beta}_0 + \tau w + [w \cdot \mathbf{f}(\mathbf{x})]\boldsymbol{\delta} + r, \qquad \mathbf{E}(r \mid \mathbf{x}, \mathbf{z}) = 0$$

All the parameters of this equation can be consistently estimated by IV, using any functions of ðx; zÞ as IVs. [These would include include 1, h0ðxÞ, Gðx; z; *g*^Þ—the fitted treatment probabilities—and Gðx; z; *g*^Þ fðxÞ.] The average treatment effect on the treated for any x is estimated as t^þ fðxÞ ^*d*. Averaging over the observations with wi ¼ 1 gives a consistent estimator of ATE1.