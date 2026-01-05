# Covariates in the Heterogeneous-e§ects Model

> Pages: 146-151

You might be wondering where the covariates have gone. After all, covariates played a starring role in our earlier discussion of regression and matching. Yet the LATE theorem does not involve covariates. This stems from the fact that when we see instrumental variables as a type of (natural or man-made) randomized trial, covariates take a back seat. If, after all, the instrument is randomly assigned, it is likely to be independent of covariates. Not all instruments have this property, however. As with covariates in the regression models in the previous chapter, the main reason why covariates are included in causal analyses using instrumental variables is that the conditional independence and exclusion restrictions underlying IV estimation may be more likely to be valid after conditioning on covariates. Even randomly assigned instruments, like drafteligibility status, may be valid only after conditioning on covariates. In the case of draft-eligibility, older cohorts were more likely to be draft-eligible because the cuto§s were higher. Because there are year-of-birth (or age) di§erences in earnings, draft-eligibility status is a valid instrument only after conditioning on year of birth.

<span id="page-146-1"></span><sup>3 0</sup>Using twins instruments alone, the IV estimate of the e§ect of a third child on female labor force participation is -.084 (s.e.=.017). The corresponding samesex estimate is -.138 (s.e.=.029). Using both instruments produces a 2SLS estimate of -.098 (.015). The 2SLS weight in this case is .74 for twins, .26 for samesex, due to the much stronger twins Örst stage.

{147}------------------------------------------------

More formally, IV estimation with covariates may be justiÖed by a conditional independence assumption

<span id="page-147-0"></span>
$$\{Y_{1i}, Y_{0i}, D_{1i}, D_{0i}\} \coprod Z_i | X_i$$
 (4.5.1)

In other words, we think of the instrumental variables as being ìas good as randomly assigned,îconditional on covariates, X<sup>i</sup> (here we are implicitly maintaining the exclusion restriction as well). A second reason for incorporating covariates is that conditioning on covariates may reduce some of the variability in the dependent variable. This leads to more precise 2SLS estimates under constant conditional e§ects.

The simplest causal model with covariates is the constant-e§ects model, with functional form restrictions as follows:

$$E[Y_{0i}|X_i] = X_i'\alpha^*$$
 for a K × 1 vector of coefficients,  $\alpha^*$ ;  
 $Y_{1i} - Y_{0i} = \rho$ .

In combination with [\(4.5.1\)](#page-147-0), this motivates 2SLS estimation of an equation like [\(4.1.6\)](#page-104-0) as discussed in Section [4.1.](#page-99-0)

A straightforward generalization of the constant-e§ects model allows

$$\mathbf{Y}_{1i} - \mathbf{Y}_{0i} = \rho(\mathbf{X}_i),$$

where (Xi) is a deterministic function of X<sup>i</sup> . This model can be estimated by adding interactions between z<sup>i</sup> and X<sup>i</sup> to the Örst stage and (the same) interactions between d<sup>i</sup> and X<sup>i</sup> to the second stage. There are now multiple endogenous variables and hence multiple Örst-stage equations. These can be written

$$\begin{aligned} \mathbf{D}_{i} &= \mathbf{X}_{i}' \pi_{00} + \pi_{01} \mathbf{Z}_{i} + \mathbf{Z}_{i} \mathbf{X}_{i}' \pi_{02} + \xi_{0i} \\ \\ \mathbf{D}_{i} \mathbf{X}_{i} &= \mathbf{X}_{i}' \pi_{10} + \pi_{11} \mathbf{Z}_{i} + \mathbf{Z}_{i} \mathbf{X}_{i}' \pi_{12} + \xi_{1i} \end{aligned}$$

The second stage equation in this case is

$$\mathbf{Y}_i = \alpha' \mathbf{X}_i + \rho_0 \mathbf{D}_i + \mathbf{D}_i \mathbf{X}_i' \rho_1 + \eta_i,$$

so (Xi) = <sup>0</sup> + 0 <sup>1</sup>X<sup>i</sup> : Alternately, a nonparametric version of (Xi) can be estimated by 2SLS in subsamples stratiÖed on X<sup>i</sup> .

The heterogeneous-e§ects model underlying the LATE theorem also allows for identiÖcation based on conditional independence as in [\(4.5.1\)](#page-147-0), though the estimand is a little more complicated. For each value of

{148}------------------------------------------------

 $X_i$ , we define covariate- specific LATE,

$$\lambda(\mathbf{X}_i) \equiv E[\mathbf{Y}_{1i} - \mathbf{Y}_{0i} | \mathbf{D}_{1i} > \mathbf{D}_{0i}, \mathbf{X}_i].$$

The "saturate and weight" approach to estimation with covariates is spelled out in the following theorem (from Angrist and Imbens, 1995).

**Theorem 4.5.1** SATURATE AND WEIGHT. Suppose the assumptions of the LATE theorem hold conditional on  $X_i$ . That is,

(CA1, Independence)  $\{Y_i(D_{1i}, 1), Y_{0i}(D_{0i}, 0), D_{1i}, D_{0i}\}\coprod Z_i | X_i;$ 

(CA2, Exclusion) 
$$P[Y_i(d, 0) = Y_i(d, 1)|X_i] = 1$$
 for  $d = 0, 1$ ;

(CA3, First-stage), 
$$E[D_{1i}-D_{0i}|X_i] \neq 0$$

We also assume monotonicity (A4) holds as before. Consider the 2SLS estimand based on the first stage equation

<span id="page-148-1"></span>
$$D_i = \pi_X + \pi_{1X} Z_i + \xi_{1i} \tag{4.5.3}$$

and the second stage equation

$$Y_i = \alpha_X + \rho_c D_i + \eta_i$$

where  $\pi_X$  and  $\alpha_X$  denote saturated models for covariates (a full set of dummies for all values of  $X_i$ ) and  $\pi'_{1X}$  denotes a separate first-stage effect of  $Z_i$  for every value of  $X_i$ . Then  $\rho_c = E[\omega(X_i)\lambda(X_i)]$  where

<span id="page-148-2"></span>
$$\omega(\mathbf{X}_{i}) = \frac{V\{E[\mathbf{D}_{i}|\mathbf{X}_{i}, \mathbf{z}_{i}]|\mathbf{X}_{i}\}}{E[V\{E[\mathbf{D}_{i}|\mathbf{X}_{i}, \mathbf{z}_{i}]|\mathbf{X}_{i}\}]}$$

$$= \frac{E\{P[\mathbf{D}_{i} = 1|\mathbf{X}_{i}, \mathbf{z}_{i}](1 - P[\mathbf{D}_{i} = 1|\mathbf{X}_{i}, \mathbf{z}_{i}])|\mathbf{X}_{i}\}}{E[E[\mathbf{D}_{i}|\mathbf{X}_{i}, \mathbf{z}_{i}](1 - P[\mathbf{D}_{i} = 1|\mathbf{X}_{i}, \mathbf{z}_{i}])]}.$$
(4.5.4)

.

This theorem says that 2SLS with a fully saturated first stage and a saturated model for covariates in the second stage produces a weighted average of covariate-specific LATEs. The weights are proportional to the average conditional variance of the population first-stage fitted value,  $E[D_i|X_i,Z_i]$ , at each value of  $X_i$ . The theorem comes from he fact that the first stage coincides with  $E[D_i|X_i,Z_i]$  when (4.5.3) is saturated (i.e., the first-stage regression recovers the CEF).

In practice, we may not want to work with a model with a first-stage parameter for each value of the covariates. First, there is the risk of bias, as we discuss at the end of this chapter, and second, a big pile of

<span id="page-148-0"></span><sup>31</sup>Note that the variability in  $E[D_i|X_i,Z_i]$  conditional on  $X_i$  comes from  $Z_i$ . So the weighting formula gives more weight to covariate values where the instrument creates more variation in fitted values. The first line of the weight formula, (4.5.4), holds for any endogenous variable in a 2SLS setup. The second is a consequence of the fact that here the endogenous variable is a dummy.

{149}------------------------------------------------

individually-imprecise Örst-stage estimates is not pretty to look at. It seems reasonable to imagine that models with fewer parameters, say a restricted Örst stage imposing a constant 1<sup>X</sup>, nevertheless approximates some kind of covariate-averaged LATE. This turns out to be true, but the argument is surprisingly indirect. The vision of 2SLS as providing a MMSE error approximation to an underlying causal relation was developed by Abadie (2003).

The Abadie approach begins by deÖning the object of interest to be E[y<sup>i</sup> jdi ;X<sup>i</sup> ;d1<sup>i</sup> >d0<sup>i</sup> ], the CEF for y<sup>i</sup> given treatment status and covariates, for compliers. An important feature of this CEF is that when the conditions of the LATE theorem hold conditional on X<sup>i</sup> , it has a causal interpretation. In other words, for compliers, treatment-control contrasts conditional on X<sup>i</sup> are equal to conditional-on-X<sup>i</sup> LATEs:

$$\begin{split} &E\left[\mathbf{Y}_{i}\middle|\mathbf{D}_{i}=1,\mathbf{X}_{i},\mathbf{D}_{1i}>\mathbf{D}_{0i}\right]-E\left[\mathbf{Y}_{i}\middle|\mathbf{D}_{i}=0,\mathbf{X}_{i},\mathbf{D}_{1i}>\mathbf{D}_{0i}\right]\\ &=&E\left[\mathbf{Y}_{1i}-\mathbf{Y}_{0i}\middle|\mathbf{X}_{i},\mathbf{D}_{1i}>\mathbf{D}_{0i}\right] \end{split}$$

This follows immediately from the fact that, given [\(4.5.1\)](#page-147-0), potential outcomes are independent of d<sup>i</sup> given X<sup>i</sup> and d1<sup>i</sup> >d0<sup>i</sup> . [32](#page-149-0) The upshot is that we can imagine running a regression of y<sup>i</sup> on d<sup>i</sup> and X<sup>i</sup> in the complier population. Although this regression might not give us the CEF of interest (unless it is linear or the model is saturated), it will, as always, provide the MMSE approximation to it. So a regression of y<sup>i</sup> on d<sup>i</sup> and X<sup>i</sup> in the complier population approximates E[y<sup>i</sup> jdi ;X<sup>i</sup> ;d1<sup>i</sup> >d0<sup>i</sup> ] just like OLS approximates E[y<sup>i</sup> jdi ;X<sup>i</sup> ]: Alas, we do not know who the compliers are, so we cannot sample them. Nevertheless, they can be found, in the following sense:

Theorem 4.5.2 ABADIE KAPPA. Suppose the assumptions of the LATE theorem hold conditional on covariates, Xi. Let g(y<sup>i</sup> ;d<sup>i</sup> ;Xi) be any measurable function of (y<sup>i</sup> ;d<sup>i</sup> ;Xi) with Önite expectation. DeÖne

$$\kappa_i = 1 - \frac{D_i(1 - Z_i)}{1 - P(Z_i = 1 | X_i)} - \frac{(1 - D_i)Z_i}{P(Z_i = 1 | X_i)}.$$

Then

$$E[g(\mathbf{Y}_i,\mathbf{D}_i,\mathbf{X}_i)|\mathbf{D}_{1i}>\mathbf{D}_{0i}] = \frac{E[\kappa_i g(\mathbf{Y}_i,\mathbf{D}_i,\mathbf{X}_i)]}{E[\kappa_i]}.$$

$$P[D_i = 1 | \{Y_{1i}, Y_{0i}\}, X_i, D_{1i} > D_{0i}]$$

$$= P[Z_i = 1 | \{Y_{1i}, Y_{0i}\}, X_i, D_{1i} > D_{0i}].$$

And by conditional independence,

$$P[z_i = 1 | \{Y_{1i}, Y_{0i}\}, X_i, D_{1i} > D_{0i}]$$

$$= P[z_i = 1 | X_i, D_{1i} > D_{0i}].$$

<span id="page-149-0"></span><sup>3 2</sup>For compliers,

{150}------------------------------------------------

This can be proved by direct calculation using the fact that, given the assumptions of the LATE theorem, any expectation is a weighted average of means for always-takers, never-takers, and compliers. By monotonicity, those with di(1zi) = 1 are always-takers because they have d0<sup>i</sup> = 1, while those with (1di)z<sup>i</sup> = 1 are never-takers because they have d1<sup>i</sup> = 0. Hence, the compliers are the left-out group.

The Abadie theorem has a number of important implications; for example, it crops up again in the discussion of quantile treatment e§ects. Here, we use it to approximate E[y<sup>i</sup> jdi ;X<sup>i</sup> ;d1<sup>i</sup> >d0<sup>i</sup> ] by linear regression. SpeciÖcally, let <sup>a</sup> and <sup>a</sup> solve

$$(\alpha_a, \beta_a) = \arg\min_{a,b} E\{(E[Y_i|D_i, X_i, D_{1i} > D_{0i}] - aD_i - X_i'b)^2 | D_{1i} > D_{0i}\}.$$

In other words, <sup>a</sup>di+X<sup>0</sup> <sup>i</sup> <sup>a</sup> gives the MMSE approximation to E[y<sup>i</sup> jdi ;X<sup>i</sup> ;d1<sup>i</sup> >d0<sup>i</sup> ], or Öts it exactly if itís linear. A consequence of Abadieís theorem is that this approximating function can be obtained by solving

<span id="page-150-1"></span>
$$(\alpha_a, \beta_a) = \arg\min_{a,b} E\{\kappa_i (\mathbf{Y}_i - a\mathbf{D}_i - \mathbf{X}_i'b)^2\}, \tag{4.5.5}$$

the kappa-weighted least-squares minimand.[33](#page-150-0)

Abadie proposes an estimation strategy (and develops distribution theory) for a procedure which involves Örst-step estimation of <sup>i</sup> using parametric or semiparametric models for the function, p(Xi) = P(z<sup>i</sup> = 1jXi). The estimates from the Örst step are then plugged into the sample analog of [\(4.5.5\)](#page-150-1) in the second step. Not surprisingly, when the only covariate is a constant, Abadieís procedure simpliÖes to the Wald estimator. More surprisingly, minimization of [\(4.5.5\)](#page-150-1) produces the traditional 2SLS estimator as long as a linear model is used for p(Xi) in the construction of <sup>i</sup> . In other words, if P(z<sup>i</sup> = 1jXi) =X<sup>0</sup> <sup>i</sup> is used when constructing an estimate of <sup>i</sup> , the Abadie estimand is 2SLS. Thus, we can conclude that whenever p(Xi) can be Öt or closely approximated by a linear model, it makes sense to view 2SLS as an approximation to the complier causal response function, E[y<sup>i</sup> jdi ;X<sup>i</sup> ;d1<sup>i</sup> >d0<sup>i</sup> ]. On the other hand, <sup>a</sup> is not, in general, the 2SLS estimand and <sup>a</sup> is not, in general, the vector of covariate e§ects produced by 2SLS. Still, the equivalence to 2SLS for linear P(z<sup>i</sup> = 1jXi) leads us to think that Abadieís method and 2SLS are likely to produce similar estimates in most applications, with the further implication that we can think of 2SLS as approximating E[y<sup>i</sup> jdi ;X<sup>i</sup> ;d1<sup>i</sup> >d0<sup>i</sup> ]:

The Angrist (2001) re-analysis of Angrist and Evans (1998) is an example where estimates based on [\(4.5.5\)](#page-150-1) are indistinguishable from 2SLS estimates. Using twins instruments to estimate the e§ect of a third child on female labor supply generates a 2SLS estimate of -.088 (s.e.=.017), while the corresponding Abadie estimate is -.089 (s.e.=.017). Similarly, 2SLS and Abadie estimates of the e§ect on hours worked

<span id="page-150-0"></span><sup>3 3</sup> The class of approximating functions neednít be linear. Instead of adi+X<sup>0</sup> i b, it might make sense to use a nonlinear function like an exponential (if the dependent variable is non-negative) or probit (if the dependent variable is zero-one). We return to this point at the end of this chapter. As noted in Section [\(4.4.4\)](#page-138-0), the kappa-weighting sceme can be used to characterize covariate distributions for compliers as well as to estimate outcome distributions.

{151}------------------------------------------------

are identical at -3.55 (s.e.=.617). This is not a strike against Abadieís procedure. Rather, it supports the notion, which we hold dear, that 2SLS approximates the causal relation of interest.[34](#page-151-0)

# 4.5.3 Average Causal Response with Variable Treatment Intensity<sup>F</sup>

An important di§erence between the causal e§ects of a dummy variable and a variable that takes on the values {0, 1, 2, . . .} is that in the Örst case, there is only one causal e§ect for any one person, while in the latter there are many: the e§ect of going from 0 to 1, the e§ect of going from 1 to 2, and so on. The potential-outcomes notation we used for schooling recognizes this. Here it is again: let

$$Y_{si} \equiv f_i(s),$$

denote the potential (or latent) earnings that person i would receive after obtaining s years of education. Note that the function fi(s) has an ìiî subscript on it while s does not. The function fi(s) tells us what i would earn for any value of schooling, s, and not just for the realized value, s<sup>i</sup> . In other words, fi(s) answers causal ìwhat ifî questions for multinomial s<sup>i</sup> .

Suppose that s<sup>i</sup> takes on values in the set f0; 1; :::; sg. Then there are s unit causal e§ects, Ysi Y<sup>s</sup>1;i: A linear causal model assumes these are the same for all s and for all i, obviously unrealistic assumptions. But we need not take these assumptions literally. Rather, 2SLS provides a computational device that generates a weighted average of unit causal e§ects, with a weighting function we can estimate and study, so as to learn where the action is coming from with a particular instrument. This weighting function tells us how the compliers are distributed over the range of s<sup>i</sup> : It tells us, for example, that the returns to schooling estimated using quarter of birth or compulsory schooling laws come from shifts in the distribution of high school grades. Other instruments, like the distance instruments used by Card (1995), act elsewhere on the schooling distribution and therefore capture a di§erent sort of return.

To áesh this out, assume that a single binary instrument, z<sup>i</sup> ; a dummy for having been born in a state with restrictive compulsory school laws, is to be used to estimate the returns to schooling (as in Acemoglu and Angrist, 2000). Also, let s1<sup>i</sup> denote the schooling i would get if z<sup>i</sup> = 1, and let s0<sup>i</sup> denote the schooling i would get if z<sup>i</sup> = 0: The theorem below, from Angrist and Imbens (1995), o§ers an interpretation of the Wald estimand with variable treatment intensity in this case. Note that here we combine the independence and exclusion restrictions by simply stating that potential outcomes indexed by s are independent of the instruments.