# IV Details

> Pages: 156-168

#### 4.6.1 2SLS Mistakes

2SLS estimates are easy to compute, especially since software like SAS and Stata will do it for you. Occasionally, however, you might be tempted to do it yourself just to see if it really works. Or you may be stranded on the planet Krikkit with all of your software licenses expired (Krikkit is encased in a slo-time envelope, so it will take you a long time to get licenses renewed). "Manual 2SLS" is for just such emergencies. In the Manual 2SLS procedure, you estimate the first stage yourself (which in any case, you should be looking at), and plug the fitted values into the second stage equation, which is then estimated by OLS. Returning to the system at the beginning of this chapter, the first and second stages are

$$\mathbf{S}_{i} = \mathbf{X}'_{i}\pi_{10} + \pi'_{11}\mathbf{Z}_{i} + \xi_{1i}$$

$$\mathbf{Y}_{i} = \alpha'\mathbf{X}_{i} + \rho\hat{\mathbf{s}}_{i} + [\eta_{i} + \rho(\mathbf{S}_{i} - \hat{\mathbf{s}}_{i})]$$

where  $X_i$  is a set of covariates,  $Z_i$  is a set of excluded instruments, and the first stage fitted values are  $\hat{s}_i = X_i' \hat{\pi}_{10} + \pi_{11}' Z_i$ .

Manual 2SLS takes some of the mystery out of canned 2SLS, and may be useful in a software crisis, but it opens the door to mistakes. For one thing, as we discussed earlier, the OLS standard errors from the manual second stage will not be correct (the OLS residual variance is the variance of  $\eta_i + \rho(s_i - \hat{s}_i)$ , while for proper 2SLS standard errors you want the variance of  $\eta_i$  only). There are more subtle risks as well.

#### Covariate Ambivalence

Suppose the covariate vector contains two sorts of variables, some (say,  $X_{0i}$ ) that you are comfortable with, and others (say,  $X_{1i}$ ) about which you are ambivalent. Griliches and Mason (1972) faced this scenario when

{157}------------------------------------------------

constructing 2SLS estimates of a wage equation that treats AFQT scores (an ability test used by the armed forces) as an endogenous control variable to be instrumented. The instruments for AFQT are early schooling (completed before military service), race, and family background variables. They estimated a system that can be described like this:

$$\mathbf{S}_{i} = \mathbf{X}'_{0i}\pi_{10} + \pi'_{11}\mathbf{Z}_{i} + \xi_{1i}$$

$$\mathbf{Y}_{i} = \alpha'_{0}\mathbf{X}_{0i} + \alpha'_{0}\mathbf{X}_{1i} + \rho\hat{s}_{i} + [\eta_{i} + \rho(\mathbf{S}_{i} - \hat{s}_{i})].$$

This looks a lot like manual 2SLS.

A closer look, however, reveals an important di§erence between the equations above and the usual 2SLS procedure: the covariates in the Örst and second stages are not the same. For example, Griliches and Mason included age in the second stage but not in the Örst, a fact noted by Cardell and Hopkins (1977) in a comment on their paper. This is a mistake. Grilichesí and Masonís second stage estimates are not the same as 2SLS. Whatís worse, they are inconsistent where 2SLS might have been Öne. To see why, note that the Örst-stage residual, s<sup>i</sup> s^<sup>i</sup> , is uncorrelated with X0<sup>i</sup> by construction since OLS residuals are always uncorrelated with included regressors. But because X1<sup>i</sup> is not included in the Örst-stage it is likely to be correlated with the Örst-stage residuals (e.g., age is probably correlated with the AFQT residual from the Griliches and Mason (1972) Örst stage). The inconsistency from this correlation spills over to all coe¢ cients in the second stage. The moral of the story: put the same exogenous covariates in your Örst and second stage. If a covariate is good enough for the second stage, itís good enough for the Örst.

#### Forbidden Regressions

Forbidden regressions were forbidden by MIT Professor Jerry Hausman in 1975, and while they occasionally resurface in an under-supervised thesis, they are still technically o§-limits. A forbidden regression crops up when researchers apply 2SLS reasoning directly to nonlinear models. A common scenario is a dummy endogenous variable. Suppose, for example, the causal model of interest is

<span id="page-157-1"></span>
$$Y_i = \alpha' X_i + \rho D_i + \eta_i, \tag{4.6.1}$$

where d<sup>i</sup> is a dummy variable for veteran status. The usual 2SLS Örst stage is

<span id="page-157-0"></span>
$$D_i = \pi'_{10} X_i + \pi'_{11} Z_i + \xi_{1i}, \tag{4.6.2}$$

a linear regression of d<sup>i</sup> on covariates and regressors.

Because d<sup>i</sup> is a dummy variable, the CEF associated with this Örst stage, E[d<sup>i</sup> jX<sup>i</sup> ;Z<sup>i</sup> ], is probably nonlinear. So the usual OLS Örst-stage is an approximation to the underlying nonlinear CEF. We might, 

{158}------------------------------------------------

4.6. IV DETAILS 143

therefore, use a nonlinear first stage in an attempt to come closer to the CEF. Suppose that we use Probit to model  $E[D_i|X_i,Z_i]$ . The Probit first stage is  $\Phi[X_i'\pi_{p0} + \pi'_{p1}Z_i]$ , where  $\pi_{p0}$  and  $\pi_{p1}$  are Probit coefficients, and the fitted values are  $\hat{D}_{pi} = \Phi[X_i'\hat{\pi}_{p0} + \hat{\pi}'_{p1}Z_i]$ . The forbidden regression in this case is the second stage equation created by substituting  $\hat{D}_{pi}$  for  $D_i$ :

<span id="page-158-0"></span>
$$Y_{i} = \alpha' X_{i} + \rho \hat{D}_{ni} + [\eta_{i} + \rho (D_{i} - \hat{D}_{ni})]. \tag{4.6.3}$$

The problem with (4.6.3) is that only OLS estimation of (4.6.2) is guaranteed to produce first-stage residuals that are uncorrelated with fitted values and covariates. If  $E[D_i|X_i,Z_i] = \Phi[X_i'\pi_{p0} + \pi_{p1}'Z_i]$ , then residuals from the nonlinear model will be asymptotically uncorrelated with  $X_i$  and  $\hat{D}_{pi}$ , but who is to say that the first stage CEF is really Probit? With garden-variety 2SLS, in contrast, we do not need to worry about whether the first-stage CEF is really linear.<sup>35</sup>

A simple alternative to the forbidden second step, (4.6.3), avoids problems due to an incorrect nonlinear first stage. Instead of plugging in nonlinear fitted values, we can use the nonlinear fitted values as instruments. In other words, use  $\hat{D}_{pi}$  as an instrument for (4.6.1) in a conventional 2SLS procedure (as always, the exogenous covariates,  $X_i$ , should also be in the instrument list). Use of fitted values as instruments is the same as plugging in fitted values when the first-stage is estimated by OLS, but not in general. Nonlinear-fits-as-instruments has the further advantage that, if the nonlinear model gives a better approximation of the first-stage CEF than the linear model, the resulting 2SLS estimates will be more efficient than those using a linear first stage (Newey, 1990).

But here, too, there is a drawback. The nonlinear-fits-as-instruments procedure implicitly uses nonlinearities in the first stage as a source of identifying information. To see this, suppose the causal model of interest includes the instruments,  $Z_i$ :

<span id="page-158-2"></span>
$$Y_i = \alpha' X_i + \gamma' Z_i + \rho D_i + \eta_i. \tag{4.6.4}$$

Now, with the first stage given by (4.6.2), the model is unidentified and conventional 2SLS estimates of (4.6.4) don't exist. But 2SLS estimates using  $X_i$ ,  $Z_i$ ,  $\hat{D}_{pi}$  do exist, because  $\hat{D}_{pi}$  is a nonlinear function of  $X_i$  and  $Z_i$  that is excluded from the second stage. Should you use this nonlinearity as a source of identifying information? We usually prefer to avoid this sort of back-door identification since its not clear what the underlying experiment really is.

As a rule, naively plugging in first-stage fitted values in nonlinear models is a bad idea. This includes models with a nonlinear second stage as well as those where the CEF for the first stage is nonlinear. Suppose,

<span id="page-158-1"></span><sup>&</sup>lt;sup>35</sup>The insight that consistency of 2SLS estimates in a traditional SEM does not depend on correct specification of the first-stage CEF goes back to Kelejian (1971). Use of a nonlinear plug-in first-stage may not do too much damage in practice - a probit first-stage can be pretty close to linear - but why take a chance when you don't have to?

{159}------------------------------------------------

for example, that you believe the causal relation between schooling and earnings is approximately quadratic (as in Card's [1995] structural model). In other words, the model of interest is

<span id="page-159-0"></span>
$$Y_{i} = \alpha' X_{i} + \rho_{1} S_{i} + \rho_{2} S_{i}^{2} + \eta_{i}. \tag{4.6.5}$$

Given two instruments, it's easy enough to estimate (4.6.5) treating both  $S_i$  and  $S_i^2$  as endogenous. In this case, there are two first-stage equations, one for  $S_i$  and one for  $S_i^2$ . You need at least two instruments for this to work, of course. It's natural to use  $Z_i$  and its square (unless  $Z_i$  is a dummy, in which case you'll need a better idea).

You might be tempted, however, to work with a single first stage, say equation (4.6.2), and estimate the following second stage manually:

$$Y_i = \alpha' X_i + \rho_1 \hat{s}_i + \rho_2 \hat{s}_i^2 + [\eta_i + \rho_1 (S_i - \hat{s}_i) + \rho_2 (S_i^2 - \hat{s}_i^2)].$$

This is a mistake since  $\hat{s}_i$  can be correlated with  $S_i^2 - \hat{s}_i^2$  while  $\hat{s}_i^2$  can be correlated with both  $S_i - \hat{s}_i$  and  $S_i^2 - \hat{s}_i^2$ . On the other hand, as long as  $X_i$  and  $Z_i$  are uncorrelated with  $\eta_i$  in (4.6.5), and you have enough instruments in  $Z_i$ , 2SLS estimation of (4.6.5) is straightforward.

#### 4.6.2 Peer Effects

A vast literature in social science is concerned with peer effects. Loosely speaking, this means the causal effect of group characteristics on individual outcomes. Sometimes regression is used in an attempt to uncover these effects. In practice, the use of regression models to estimate peer effects is fraught with peril. Although this is not really an IV issue *per se*, the language and algebra of 2SLS helps us understand why peer effects are hard to identify.

Broadly speaking, there are two types of peer effects. The first concerns the effect of group characteristics such as the average schooling in a state or city on individually-measured outcome variable. This peer effect links the average of one variable to individual outcomes as described by another variable. For example, Acemoglu and Angrist (2000) ask whether a given individual's earnings are affected by the average schooling in his or her state of residence. The theory of human capital externalities suggests that living in a state with a more educated workforce may make everyone in the state more productive, not just those who are more educated. This kind of spillover is said to be a *social return* to schooling: human capital that benefits everyone, whether or not they are more educated.

A causal model which allows for such externalities can be written

<span id="page-159-1"></span>
$$Y_{ijt} = \delta_i + \lambda_t + \gamma \overline{S}_{it} + \rho S_i + u_{it} + \eta_{iit}, \tag{4.6.6}$$

{160}------------------------------------------------

4.6. IV DETAILS 145

where Yijt is the log weekly wage of individual i in state j in year t, ujt is a state-year error component, and i is an individual error term. The controls <sup>j</sup> and <sup>t</sup> are state-of-residence and year e§ects. The coe¢ cient is the returns to schooling for an individual, while the coe¢ cient is meant to capture the e§ect of average schooling, Sjt, in state j and year t.

In addition to the usual concerns about s<sup>i</sup> , the most important identiÖcation problem raised by equation [\(4.6.6\)](#page-159-1) is omitted variables bias from correlation between average schooling and other state-year e§ects embodied in the error component ujt. For example, public university systems may expand during cyclical upturns, generating a common trend in state average schooling levels and state average earnings. Acemoglu and Angrist (2000) attempt to solve this problem using instrumental variables derived from historical compulsory attendance laws that are correlated with Sjt but uncorrelated with contemporary ujt and <sup>i</sup> :

While omitted state-year e§ects are the primary concern motivating Acemoglu and Angristís (2000) instrumental variables estimation, the fact that one regressor, Sjt, is the average of another regressor, s<sup>i</sup> , also complicates the interpretation of OLS estimates of equation [\(4.6.6\)](#page-159-1). To see this, consider a simpler version of [\(4.6.6\)](#page-159-1) with a cross-section dimension only. This can be written

<span id="page-160-0"></span>
$$Y_{ij} = \mu + \pi_0 \mathbf{S}_i + \pi_1 \overline{\mathbf{S}}_j + \nu_i; \text{ where } E[\nu_i \mathbf{S}_i] = E[\nu_i \overline{\mathbf{S}}_j] \equiv 0.$$

$$(4.6.7)$$

where Yij is he log weekly wage of individual i in state j and S<sup>j</sup> is average schooling in the state. Now, let <sup>0</sup> denote the coe¢ cient from a bivariate regression of Yij on s<sup>i</sup> only and let <sup>1</sup> denote the coe¢ cient from a bivariate regression of Yij on S<sup>j</sup> only. From the discussion of grouping and 2SLS earlier in this chapter, itís clear that <sup>1</sup> is the 2SLS estimate of the coe¢ cient on s<sup>i</sup> in a bivariate regression of Yij on s<sup>i</sup> using a full set of state dummies as instruments. The Appendix uses this fact to show that the parameters in equation [\(4.6.7\)](#page-160-0) can be written in terms of <sup>0</sup> and <sup>1</sup> as

<span id="page-160-1"></span>
$$\pi_0 = \rho_1 + \phi(\rho_0 - \rho_1)$$

$$\pi_1 = \phi(\rho_1 - \rho_0)$$
(4.6.8)

where = 1 <sup>1</sup>R<sup>2</sup> <sup>&</sup>gt; <sup>1</sup>; and <sup>R</sup><sup>2</sup> is the Örst-stage R-squared.

The upshot of [\(4.6.8\)](#page-160-1) is that if, for any reason, OLS estimates of the bivariate regression of wages on individual schooling di§er from 2SLS estimates using state-dummy instruments, the coe¢ cient on average schooling in [\(4.6.7\)](#page-160-0) will be nonzero. For example, if instrumenting with state dummies corrects for attenuation bias due to measurement error in s<sup>i</sup> , we have <sup>1</sup> > <sup>0</sup> and the spurious appearance of positive external returns. In contrast, if instrumenting with state dummies eliminates the bias from positive correlation between s<sup>i</sup> and unobserved earnings potential, we have <sup>1</sup> < <sup>0</sup> , and the appearance of negative social returns.[36](#page-160-2) In practice, therefore, it is very di¢ cult to substantiate social e§ects by OLS estimation of an

<span id="page-160-2"></span><sup>3 6</sup> The coe¢ cient on average schooling in an equation with individual schooling can be interpreted as the Hausman (1978)


{161}------------------------------------------------

equation like [4.6.6,](#page-159-0) though more sophisticated strategies where both the individual and group averages are treated as endogenous may work.

A second and even more di¢ cult peer e§ect to uncover is the e§ect of the group average of a variable on the individual level of this same variable. This is not really an IV problem; it takes us back to basic regression issues. To see this point, suppose that S<sup>j</sup> is the high-school graduation rate in school j, and we would like to know whether students are more likely to graduate from high school when everyone around them is more likely to graduate from high school. To uncover the peer e§ect in high school graduation rates, we might work with a regression model like:

<span id="page-161-0"></span>
$$S_{ij} = \mu + \pi_2 \overline{S}_j + \xi_{ij}, \tag{4.6.9}$$

where sij is individual iís high school graduation status and S<sup>j</sup> is the average high school graduation rate in school j, which i attends.

At Örst blush, equation [\(4.6.9\)](#page-161-0) seems like a sensible formulation of a well-deÖned causal question, but in fact it is nonsense. The regression of sij on S<sup>j</sup> always has a coe¢ cient of 1, a conclusion that can be drawn immediately once you recognize S<sup>j</sup> as the Örst-stage Ötted value from a regression of sij on a full set of school dummies.[37](#page-161-1) Thus, an equation like [\(4.6.9\)](#page-161-0) cannot possibly be informative about causal e§ects.

A modestly improved version of the bad peer regression changes [\(4.6.9\)](#page-161-0) to

<span id="page-161-2"></span>
$$S_{ij} = \mu + \pi_4 \overline{S}_{(i)j} + \xi_{ij}, \tag{4.6.10}$$

where S(i)<sup>j</sup> is the mean of sij in school j, excluding student i. This is a step in the right direction by deÖnition, i is not in the group used to construct S(i)<sup>j</sup> - but still problematic because sij and S(i)<sup>j</sup> are both a§ected by school-level random shocks. The presence of random e§ects in the error term raises important issues for statistical inference, issues discussed at length in Chapter [8.](#page-236-0) But in an equation like [\(4.6.10\)](#page-161-2), group-level random shocks are more that a problem for standard errors: any shock common to the group (school) creates spurious peer e§ects. For example, particularly e§ective school principals may raise graduation rates for everyone in the schools at which they work. This looks like a peer e§ect since it induces correlation between sij and S(i)<sup>j</sup> even if there is no causal link between peer means and individual student

test statistic for the equality of OLS estimates and 2SLS estimates of private returns to schooling using state dummies as instruments. Borjas (1992) discusses a similar problem a§ecting the estimation of ethnic-background e§ects.

$$\frac{\sum_{j} \sum_{i} s_{ij} (\overline{S}_{j} - \overline{S})}{\sum_{j} n_{j} (\overline{S}_{j} - \overline{S})^{2}} = \frac{\sum_{j} (\overline{S}_{j} - \overline{S}) \sum_{i} s_{ij}}{\sum_{j} n_{j} (\overline{S}_{j} - \overline{S})^{2}}$$

$$= \frac{\sum_{j} (\overline{S}_{j} - \overline{S}) (n_{j} \overline{S}_{j})}{\sum_{j} n_{j} (\overline{S}_{j} - \overline{S})^{2}} = 1.$$

<span id="page-161-1"></span><sup>3 7</sup>Here is a direct proof that the regression of sij on S<sup>j</sup> is always unity:

{162}------------------------------------------------

achievement. We therefore prefer not see regressions like [\(4.6.10\)](#page-161-2) either.

The best shot at a causal investigation of peer e§ects focuses on variation in ex ante peer characteristics, that is, some measure of peer quality which predates the outcome variable and is therefore una§ected by common shocks. A recent example is Ammermueller and Pischke (2006), who study the link between classmatesífamily background, as measured by the number of books in their homes, and student achievement in European primary schools. The Ammermueller and Pischke regressions are versions of

$$\mathbf{S}_{ij} = \mu^* + \pi_4 \overline{B}_{(i)j} + \xi_{ij},$$

where B(i)<sup>j</sup> is the average number of books in the home of student iís peers. This looks like [\(4.6.10\)](#page-161-2), but with an important di§erence. The variable B(i)<sup>j</sup> is a feature of the home environment that predates test scores and is therefore una§ected by school-level random shocks.

Angrist and Lang (2004) provide another example of an attempt to link student achievement with the ex ante characteristics of peers. The Angrist and Lang study looks at the impact of bused-in low-achieving newcomers on high-achieving residentsítest scores. The regression of interest in this case is a version of

<span id="page-162-0"></span>
$$S_{ij} = \mu + \pi_3 \overline{m}_j + \xi_{ij}, \tag{4.6.11}$$

where m<sup>j</sup> is the number of bused-in low-achievers in school j and sij is resident-student iís test score. Spurious correlation due to common shocks is not a concern in this context for two reasons. First, m<sup>j</sup> is a feature of the school population determined by students outside the sample used to estimate [\(4.6.11\)](#page-162-0). Second, the number of low-achievers is an ex ante variable biased on prior information about where the students come from and not the outcome variable, sij . School-level random e§ects remain an important issue for inference, however, since m<sup>j</sup> is a group-level variable.

#### 4.6.3 Limited Dependent Variables Reprise

In Section [3.4.2,](#page-84-0) we discussed the consequences of limited dependent variables for regression models. When the dependent variable is binary or non-negative, say, employment status or hours worked, the CEF is typically nonlinear. Most nonlinear LDV models are built around a non-linear transformation of a linear latent index. Examples include Probit, Logit, and Tobit. These models capture features of the associated CEFs (e.g., Probit Ötted values are guaranteed to be between zero and one, while Tobit Ötted values are non-negative). Yet we saw that the added complexity and extra work required to interpret the results from latent-index models may not be worth the trouble.

An important consideration in favor of OLS is a conceptual robustness that structural models often lack. OLS is always a MMSE linear approximation to the CEF. In fact, we can think of OLS as a scheme for computing marginal e§ects - a scheme that has the virtue of simplicity, automation, and comparability 

{163}------------------------------------------------

across studies. Nonlinear latent-index models are more like GLS - they provide an efficiency gain when taken literally, but they require a commitment to functional form and distributional assumptions about which we do not usually feel strongly.<sup>38</sup> A second consideration is the difference between the latent-index parameters at heart of nonlinear models and the average causal effects that we believe should be the objects of primary interest in most research projects.

The arguments in favor of conventional OLS with LDVs apply with equal force to 2SLS and models with endogenous variables. IV methods capture local average treatment effects regardless of whether the dependent variable is binary, non-negative, or continuously distributed on the real line. With covariates, we can think of 2SLS as estimating LATE averaged across covariate cells. In models with variable or continuous treatment intensity, 2SLS gives us the average causal response or an average derivative. Although Abadie (2003) has shown that 2SLS does not, in general, provide the MMSE approximation to the complier causal response function, in practice, 2SLS estimates come out remarkably close to estimates using the more rigorously grounded Abadie procedure (and with a saturated model for covariates, 2SLS and Abadie are the same). And, of course, 2SLS estimates LATE directly; there is no intermediate step involving the calculation of marginal effects.

2SLS is not the only way to go. An alternative more elaborate approach tries to build up a causal story by describing the process generating LDVs in detail. A good example is bivariate Probit, which can be applied to the Angrist and Evans (1998) example like this. Suppose that a woman decides to have a third child by comparing costs and benefits using a net benefit function or latent index that is linear in covariates and excluded instruments, with a random component or error term,  $v_i$ . The bivariate Probit first stage can be written

<span id="page-163-1"></span>
$$D_i = 1[X_i'\gamma_0 + \gamma_1 Z_i > v_i], \tag{4.6.12}$$

where  $z_i$  is an instrumental variable that increases the benefit of a third child, conditional on covariates,  $X_i$ . For example, American parents appear to value a third child more when they have had either two boys or two girls, a sort-of portfolio-diversification phenomenon that can be understood as increasing the benefit

$$\sum \frac{(\mathbf{Y}_i - p_i)\mathbf{X}_i}{p_i(1 - p_i)} = 0.$$

Thus, maximum likelihood is the same as GLS estimation of the nonlinear model

$$\mathbf{Y}_i = \Phi\left[\frac{\mathbf{X}_i'\beta}{\sigma}\right] + \boldsymbol{\xi}_i.$$

Consistency of the maximum likelihood estimator turns on the assumption that the conditional variance of  $Y_i$  is  $p_i(1-p_i)$ . It's worth noting that we can dispense with this assumption and simply fit  $Y_i$  to  $\Phi\left[\frac{X_i'\beta}{\sigma}\right]$  by nonlinear least squares (NLLS). This sort of agnostic NLLS shares the robustness properties of OLS; it gives the best MMSE fit in a class of approximating functions.

<span id="page-163-0"></span><sup>&</sup>lt;sup>38</sup>The analogy between nonlinear LDV models and GLS is more than rhetorical. Consider a Probit model with nonlinear CEF  $E[Y_i|X_i] = \Phi\left[\frac{X_i'\beta}{\sigma}\right] \equiv p_i$ . The first-order conditions for maximum likelihood estimation of this model are

{164}------------------------------------------------

of a third child in families with same-sex sibships.

An outcome of primary interest in this context is employment status, a Bernoulli random variable with a conditional mean between zero and one. To complete the model, suppose that employment status, y<sup>i</sup> , is determined by the latent index

<span id="page-164-0"></span>
$$Y_i = 1[X_i'\beta_0 + \beta_1 D_i > \varepsilon_i], \tag{4.6.13}$$

where "<sup>i</sup> is a second random component or error term. This latent index can be seen as arising from a comparison of the costs and beneÖts of working.

The source of omitted variables bias in the bivariate Probit setup is correlation between v<sup>i</sup> and "<sup>i</sup> . In other words, unmeasured random determinants of childbearing are correlated with unmeasured random determinants of employment. The model is identiÖed by assuming z<sup>i</sup> is independent of these components, and that the random components are normally distributed. Given normality, the parameters in [\(4.6.12\)](#page-163-1) and [\(4.6.13\)](#page-164-0) can be estimated by maximum likelihood. The log likelihood function is

$$\sum_{i} Y_{i} \ln \Phi_{b} \left( \frac{X_{i}' \beta_{0} + \beta_{1} D_{i}}{\sigma_{\varepsilon}}, \frac{X_{i}' \gamma_{0} + \gamma_{1} Z_{i}}{\sigma_{\nu}}; \rho_{\varepsilon \nu} \right)$$

$$+ (1 - Y_{i}) \ln \left[ 1 - \Phi_{b} \left( \frac{X_{i}' \beta_{0} + \beta_{1} D_{i}}{\sigma_{\varepsilon}}, \frac{X_{i}' \gamma_{0} + \gamma_{1} Z_{i}}{\sigma_{\nu}}; \rho_{\varepsilon \nu} \right) \right],$$

$$(4.6.14)$$

where b(; ; ") is the bivariate normal distribution function with correlation coe¢ cient ". Note, however, that we can multiply the latent index coe¢ cients by a positive constant without changing the likelihood. The object of estimation is therefore the ratio of the index coe¢ cients to the standard deviation of the error terms (e.g., <sup>1</sup>=").

The potential outcomes deÖned by the bivariate Probit model are

$$\mathbf{Y}_{0i} = \mathbf{1}[\mathbf{X}_i'\boldsymbol{\beta}_0 > \varepsilon_i] \text{ and } \mathbf{Y}_{1i} = \mathbf{1}[\mathbf{X}_i'\boldsymbol{\beta}_0 + \boldsymbol{\beta}_1 > \varepsilon_i],$$

while potential treatment assignments are

$$D_{0i} = 1[X_i'\gamma_0 > v_i] \text{ and } D_{1i} = 1[X_i'\gamma_0 + \gamma_1 > v_i].$$

As usual, only one potential outcome and one potential assignment is observed for any one person. Itís also clear from this representation that correlation between v<sup>i</sup> and "<sup>i</sup> is the same thing as correlation between potential treatment assignments and potential outcomes.

The latent index coe¢ cients do not themselves tell us anything about the size of the causal e§ect of childbearing on employment other than the sign. To see this, note that the average causal e§ect of childbearing is

$$E[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}] = E\{1[\mathbf{X}_i'\beta_0 + \beta_1 > \varepsilon_i] - 1[\mathbf{X}_i'\beta_0 > \varepsilon_i]\}$$

{165}------------------------------------------------

while the average effect on the treated is

$$E[Y_{1i} - Y_{0i}|D_i = 1] = E\{1[X_i'\beta_0 + \beta_1 > \varepsilon_i] - 1[X_i'\beta_0 > \varepsilon_i]|X_i'\gamma_0 + \gamma_1Z_i > v_i\}.$$

Given alterative distributional assumptions for  $v_i$  and  $\varepsilon_i$ , these can be anything (If the error terms are heteroskedastic then even the sign is indeterminate).

Under normality, the average causal effects generated by the bivariate Probit model are easy to evaluate.

The average causal effect is

<span id="page-165-1"></span>
$$E\left\{1\left[X_{i}'\beta_{0} + \beta_{1} > \varepsilon_{i}\right] - 1\left[X_{i}'\beta_{0} > \varepsilon_{i}\right]\right\}$$

$$= E\left\{\Phi\left[\frac{X_{i}'\beta_{0} + \beta_{1}}{\sigma}\right] - \Phi\left[\frac{X_{i}'\beta_{0}}{\sigma}\right]\right\},$$

$$(4.6.15)$$

where  $\Phi[\cdot]$  is the normal CDF. The effect on the treated is a little more complicated since it involves the bivariate normal CDF

<span id="page-165-2"></span>
$$E\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{D}_{i} = 1\right]$$

$$= E\left\{\frac{\Phi_{b}\left(\frac{\mathbf{X}_{i}'\beta_{0} + \beta_{1}}{\sigma_{\varepsilon}}, \frac{\mathbf{X}_{i}'\gamma_{0} + \gamma_{1}\mathbf{Z}_{i}}{\sigma_{\nu}}; \rho_{\varepsilon\nu}\right) - \Phi_{b}\left(\frac{\mathbf{X}_{i}'\beta_{0}}{\sigma_{\varepsilon}}, \frac{\mathbf{X}_{i}'\gamma_{0} + \gamma_{1}\mathbf{Z}_{i}}{\sigma_{\nu}}; \rho_{\varepsilon\nu}\right)}{\Phi\left(\frac{\mathbf{X}_{i}'\gamma_{0} + \gamma_{1}\mathbf{Z}_{i}}{\sigma_{\nu}}\right)}\right\}$$

$$(4.6.16)$$

Since the bivariate normal CDF is a canned function in many software packages, this is easy enough to calculate in practice.

Bivariate Probit probably qualifies as harmless in the sense that it's not very complicated, and easy to get right using packaged software routines. Still, it shares the disadvantages of nonlinear latent-index modeling discussed in the previous chapter. First, some researchers become distracted by an effort to identify index coefficients instead of average causal effects. For example, a large literature in econometrics is concerned with the identification of index coefficients without the need for distributional assumptions. Applied researchers interested in causal effects can safely ignore this work.<sup>39</sup>

A second vice in this context is also a virtue. Bivariate Probit and other models of this sort can be used to identify population average causal effects and/or effects on the treated. 2SLS does not promise you average causal effects, only *local* average causal effects. But it should be clear from (4.6.15) that the assumed normality of the latent index error terms is essential for this. As always, the best you can do without a distributional assumption is LATE, the average causal effect for compliers. For bivariate Probit, we can

$$E\left\{\Lambda\left[X_{i}'\beta_{0}+\beta_{1}\right]-\Lambda\left[X_{i}'\beta_{0}\right]\right\}=\Lambda'\left[X_{i}'\beta_{0}+\tilde{\beta}_{1}\right]\beta_{1},$$

where  $\tilde{\beta}_1$  is in  $[0, \beta_1]$ . This always depends on the shape of  $\Lambda[\cdot]$ .

<span id="page-165-0"></span><sup>&</sup>lt;sup>39</sup>Suppose the latent error term has an unknown distribution, with CDF  $\Lambda[\cdot]$ . The average causal effect in this case is

{166}------------------------------------------------

write LATE as

$$\begin{split} &E\left[\mathbf{Y}_{1i}-\mathbf{Y}_{0i}\middle|\mathbf{D}_{1i}>\mathbf{D}_{0i}\right]\\ =&E\{\mathbf{1}[\mathbf{X}_{i}'\boldsymbol{\beta}_{0}+\boldsymbol{\beta}_{1}>\boldsymbol{\varepsilon}_{i}]-\mathbf{1}[\mathbf{X}_{i}'\boldsymbol{\beta}_{0}>\boldsymbol{\varepsilon}_{i}]\middle|\mathbf{X}_{i}'\boldsymbol{\gamma}_{0}+\boldsymbol{\gamma}_{1}>\boldsymbol{v}_{i}>\mathbf{X}_{i}'\boldsymbol{\gamma}_{0}\}, \end{split}$$

which, like [\(4.6.16\)](#page-165-2), can be evaluated using joint normality of v<sup>i</sup> and "<sup>i</sup> : But you neednít bother using normality to evaluate E[y1<sup>i</sup>y0<sup>i</sup> jd1<sup>i</sup> >d0<sup>i</sup> ], since LATE can be estimated by IV for each X<sup>i</sup> and averaged using the histogram of the covariates. Alternately, do 2SLS and settle for a variance-weighted average of covariate-speciÖc LATEs.

You might be wondering whether LATE is enough. Perhaps you would like to estimate the average treatment e§ect or the e§ect of treatment on the treated and are willing to make a few extra assumptions to do so. Thatís all well and good, but in our experience, you canít get blood from a stone, even with heroic assumptions. Since local information is all thatís in the data, in practice the average causal e§ects produced by bivariate Probit are likely to be similar to 2SLS estimates provided the model for covariates is su¢ ciently áexible. This is illustrated in Table [4.6.1](#page-107-0), which reports 2SLS and bivariate Probit estimates of the e§ects of a third child on female labor supply using the Angrist-Evans (1998) same-sex instruments and the same 1980 census sample of married women with 2 or more children used in their paper. The dependent variable is a dummy for having worked the previous year; the endogenous variable is a dummy for having a third child. The Örst stage e§ect of a same-sex sibship on the probability of a third birth is about 7 percentage points.

Panel A of Table [4.6.1](#page-107-0) reports estimates from a model with no covariates. The 2SLS estimate of -.138 in column 1 is numerically identical to the Abadie causal e§ect estimated using a linear model in column 2, as it should be in this case. Without covariates, the 2SLS slope coe¢ cient provides the best linear approximation to the complier causal response function as does Abadieís kappa-weighting procedure. The marginal e§ect changes little if, instead of a linear approximation, we use nonlinear least squares with a Probit CEF. The marginal e§ect estimated by minimizing

$$E\left\{\kappa_i\left(\mathbf{Y}_i - \Phi\left[\frac{\beta_0 + \beta_1\mathbf{D}_i}{\sigma_\varepsilon}\right]\right)^2\right\}$$

is -.137, reported in column 3. This is not surprising since the model without covariates imposes no functional form assumptions.

Perhaps more surprising is the fact that marginal e§ects and the average treatment e§ects calculated using [\(4.6.15\)](#page-165-1) and [\(4.6.16\)](#page-165-2) are also the same as the 2SLS and Abadie estimates. These results are reported in columns 4-6. The marginal e§ect calculated using a derivative to approximate to the Önite di§erence in [\(4.6.15\)](#page-165-1) is -.138 (in column 4, labelled MFX for marginal e§ects), while both average treatment e§ects are -.139 in columns 5 and 6. Adding a few covariates has little e§ect on the estimates, as can be seen in Panel

{167}------------------------------------------------

Table 4.6.1: 2SLS, Abadie, and bivariate probit estimates of the e§ects of a third child on female labor supply

<table><tbody><tr><th></th><th></th><th></th><th></th><th></th><th></th><th></th></tr><tr><td></td><td>2SLS</td><td></td><td>Abadie Estimates</td><td></td><td></td><td>Bivariate probit</td></tr><tr><td></td><td></td><td>Linear</td><td>Probit</td><td>MFX</td><td>ATE</td><td>TOT</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td></td><td></td><td></td><td>A. No Covariates</td><td></td><td></td><td></td></tr><tr><td>Employment</td><td>-0.138</td><td>-0.138</td><td>-0.137</td><td>-0.138</td><td>-0.139</td><td>-0.139</td></tr><tr><td></td><td>(0.029)</td><td>(0.030)</td><td>(0.030)</td><td>(0.029)</td><td>(0.029)</td><td>(0.029)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>B. Some covariates (no age controls)</td><td></td><td></td></tr><tr><td>Employment</td><td>-0.132</td><td>-0.132</td><td>-0.131</td><td>-0.135</td><td>-0.135</td><td>-0.135</td></tr><tr><td></td><td>(0.029)</td><td>(0.029)</td><td>(0.028)</td><td>(0.028)</td><td>(0.028)</td><td>(0.028)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>C. Some covariates plus age at Örst birth</td><td></td><td></td></tr><tr><td>Employment</td><td>-0.129</td><td>-0.129</td><td>-0.129</td><td>-0.133</td><td>-0.133</td><td>-0.133</td></tr><tr><td></td><td>(0.028)</td><td>(0.028)</td><td>(0.028)</td><td>(0.026)</td><td>(0.026)</td><td>(0.026)</td></tr><tr><td></td><td></td><td></td><td></td><td>D. Some covariates plus age at Örst birth and a dummy for age&gt;30</td><td></td><td></td></tr><tr><td>Employment</td><td>-0.124</td><td>-0.125</td><td>-0.125</td><td>-0.131</td><td>-0.131</td><td>-0.131</td></tr><tr><td></td><td>(0.028)</td><td>(0.029)</td><td>(0.029)</td><td>(0.025)</td><td>(0.025)</td><td>(0.025)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td>E. Some covariates plus age at Örst birth and age</td><td></td><td></td></tr><tr><td>Employment</td><td>-0.120</td><td>-0.121</td><td>-0.121</td><td>-0.171</td><td>-0.171</td><td>-0.171</td></tr><tr><td></td><td>(0.028)</td><td>(0.026)</td><td>(0.026)</td><td>(0.023)</td><td>(0.023)</td><td>(0.023)</td></tr></tbody></table>

Notes: Adapted from Angrist (2001). The table compares 2SLS estimates to alternative IVtype estimates of the e§ect of childbearing on labor supply using nonlinear models. Standard errors for the Abadie estimates were bootstrapped using 100 replications of subsamples of size 20,000. MFX denotes marginal e§ects; ATE is the average treatment e§ect; TOT is the average e§ect of treatment on the treated.

B. In this case, the covariates are all dummy variables, three for race (black, Hispanic, and other), and two indicating Örst and second-born boys (the excluded instrument is the interaction of these two). Panels C and D show that adding a linear term in age at Örst birth and a dummy for maternal age also leaves the estimates unchanged.

The invariance to covariates seems desirable: since the same-sex instrument is essentially independent of the covariates, control for covariates is unnecessary to eliminate bias and should primarily a§ect precision. Yet, as Panel E shows, the marginal e§ects generated by bivariate Probit are sensitive to the list of covariates. Swapping a dummy indicating mothers over 30 with a linear age term increases the bivariate Probit estimates markedly, to -.171, while leaving 2SLS and the Abadie estimators unchanged. This probably reáects the fact that the linear age change induces an extrapolation into cells where there is little data. Although there is no harm in reporting the results in Panel E, itís hard to see why the more robust 2SLS and Abadie estimators should not be featured as most likely more reliable.[40](#page-167-0)

<span id="page-167-0"></span><sup>4 0</sup>Angrist (2001) makes the same point using twins instruments, and reports a similar pattern in a comparison of 2SLS,

{168}------------------------------------------------