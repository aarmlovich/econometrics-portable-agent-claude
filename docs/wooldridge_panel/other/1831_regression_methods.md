# **18.3.1** Regression Methods

> Pages: 615-621

We can use equation (18.3), along with Assumption ATE.1', to obtain estimators of  $ATE(\mathbf{x})$ , which can then be used to estimate ATE and  $ATE_1$ . First,

$$E(y \mid \mathbf{x}, w) = E(y_0 \mid \mathbf{x}, w) + w[E(y_1 \mid \mathbf{x}, w) - E(y_0 \mid \mathbf{x}, w)]$$
$$= E(y_0 \mid \mathbf{x}) + w[E(y_1 \mid \mathbf{x}) - E(y_0 \mid \mathbf{x})]$$

where the first equality follows from equation (18.3) and the second follows from Assumption ATE.1'. Therefore, under Assumption ATE.1',

$$E(y | \mathbf{x}, w = 1) - E(y | \mathbf{x}, w = 0) = E(y_1 | \mathbf{x}) - E(y_0 | \mathbf{x}) = ATE(\mathbf{x})$$
(18.7)

{616}------------------------------------------------

Because we have a random sample on  $(y, w, \mathbf{x})$  from the relevant population,  $r_1(\mathbf{x}) \equiv E(y | \mathbf{x}, w = 1)$  and  $r_0(\mathbf{x}) \equiv E(y | \mathbf{x}, w = 0)$  are **nonparametrically identified**. That is, these are conditional expectations that depend entirely on observables, and so they can be consistently estimated quite generally. (See Härdle and Linton, 1994, for assumptions and methods.) For the purposes of identification, we can just assume  $r_1(\mathbf{x})$  and  $r_0(\mathbf{x})$  are known, and the fact that they are known means that  $ATE(\mathbf{x})$  is identified. If  $\hat{r}_1(\mathbf{x})$  and  $\hat{r}_0(\mathbf{x})$  are consistent estimators (in an appropriate sense), using the random sample of size N, a consistent estimator of ATE under fairly weak assumptions is

$$A\hat{T}E = N^{-1} \sum_{i=1}^{N} [\hat{r}_1(\mathbf{x}_i) - \hat{r}_0(\mathbf{x}_i)]$$

while a consistent estimator of  $ATE_1$  is

$$A\hat{T}E_{1} = \left(\sum_{i=1}^{N} w_{i}\right)^{-1} \left\{\sum_{i=1}^{N} w_{i} [\hat{r}_{1}(\mathbf{x}_{i}) - \hat{r}_{0}(\mathbf{x}_{i})]\right\}$$

The formula for  $A\hat{T}E_1$  simply averages  $[\hat{r}_1(\mathbf{x}_i) - \hat{r}_0(\mathbf{x}_i)]$  over the subsample with  $w_i = 1$ .

There are several implementation issues that arise in computing and using  $A\hat{T}E$  and  $A\hat{T}E_1$ . The most obvious of these is obtaining  $\hat{r}_1(\cdot)$  and  $\hat{r}_0(\cdot)$ . To be as flexible as possible, we could use nonparametric estimators, such as a **kernel estimator** (see Härdle and Linton, 1994). Obtaining reliable standard errors when we use nonparametric estimates can be difficult. An alternative is to use flexible parametric models, such as low-order polynomials that include interaction terms. [Presumably, we would also account for the nature of y in estimating  $E(y | \mathbf{x}, w = 1)$  and  $E(y | \mathbf{x}, w = 0)$ . For example, if y is binary, we would use a flexible logit or probit; if y is a corner solution, we might use a flexible Tobit or a flexible exponential regression function.]

With plenty of data, a third possibility is to list all possible values that  $\mathbf{x}$  can take, say,  $\mathbf{c}_1, \mathbf{c}_2, \dots, \mathbf{c}_M$ , and to estimate  $\mathrm{E}(y \mid \mathbf{x} = \mathbf{c}_m, w = 1)$  by averaging the  $y_i$  over all i with  $\mathbf{x}_i = \mathbf{c}_m$  and  $w_i = 1$ ;  $\mathrm{E}(y \mid \mathbf{x} = \mathbf{c}_m, w = 0)$  is estimated similarly. For each m and w = 0 or 1, this method is just estimation of a mean using a sample average. Typically, M is large because  $\mathbf{x}$  takes on many values, and many of the cells may have only a small number of observations.

Regardless of how  $\hat{r}_1(\cdot)$  and  $\hat{r}_0(\cdot)$  are obtained, to use the estimated treatment effects we need to obtain asymptotically valid standard errors. Generally, this task can be very difficult, especially if nonparametric methods are used in estimation.

{617}------------------------------------------------

Nevertheless, we will show how a linear regression model involving level effects and interactions can be used to obtain good estimates of the treatment effects as well as reliable standard errors.

Before we turn to standard regression models, we need to discuss a problem that can arise in the evaluation of programs, especially when flexible estimation of Eðy j x; w ¼ 1Þ and Eðy j x; w ¼ 0Þ is desirable. To illustrate the problem, suppose there is only one binary covariate, x, and Assumption ATE.1<sup>0</sup> holds; for concreteness, x could be an indicator for whether pretraining earnings are below a certain threshold. Suppose that everyone in the relevant population with x ¼ 1 participates in the program. Then, while we can estimate Eðy j x ¼ 1; w ¼ 1Þ with a random sample from the population, we cannot estimate Eðy j x ¼ 1; w ¼ 0Þ because we have no data on the subpopulation with x ¼ 1 and w ¼ 0. Intuitively, we only observe the counterfactual y<sup>1</sup> when x ¼ 1; we never observe y<sup>0</sup> for any members of the population with x ¼ 1. Therefore, ATEðxÞ is not identified at x ¼ 1.

If some people with x ¼ 0 participate while others do not, we can estimate Eðy j x ¼ 0; w ¼ 1Þ Eðy j x ¼ 0; w ¼ 0Þ using a simple difference in averages over the group with x ¼ 0, and so ATEðxÞ is identified at x ¼ 0. But if we cannot estimate ATEð1Þ, we cannot estimate the unconditional ATE because ATE ¼ Pðx ¼ 0Þ ATEð0Þ þ Pðx ¼ 1Þ ATEð1Þ. In effect, we can only estimate the ATE over the subpopulation with x ¼ 0, which means that we must redefine the population of interest. This limitation is unfortunate: presumably we would be very interested in the program's effects on the group that always participates.

A similar conclusion holds if the group with x ¼ 0 never participates in the program. Then ATEð0Þ is not estimable because Eðy j x ¼ 0; w ¼ 1Þ is not estimable. If some people with x ¼ 1 participated while others did not, ATEð1Þ would be identified, and then we would view the population of interest as the subgroup with x ¼ 1. There is one important difference between this situation and the one where the x ¼ 1 group always receives treatment: it seems perfectly natural to exclude from the population people who have no chance of treatment based on observed covariates. This observation is related to the issue we discussed in Section 18.2 concerning the relevant population for defining ATE. If, for example, people with very high preprogram earnings ðx ¼ 0Þ have no chance of participating in a job training program, then we would not want to average together ATEð0Þ and ATEð1Þ; ATEð1Þ by itself is much more interesting.

Although the previous example is extreme, its consequences can arise in more plausible settings. Suppose that x is a vector of binary indicators for pretraining income intervals. For most of the intervals, the probability of participating is strictly between zero and one. If the participation probability is zero at the highest income 

{618}------------------------------------------------

level, we simply exclude the high-income group from the relevant population. Unfortunately, if participation is certain at low income levels, we must exclude lowincome groups as well.

As a practical matter, we often determine whether the probability of participation is one or zero by looking at the random sample. If we list the possible values of the explanatory variables, c1; ... ; cM, as described earlier, the problem arises when there is a value, say cm, where all units with x<sup>i</sup> ¼ c<sup>m</sup> participate in the program. Because we cannot estimate Eðy j x ¼ cm; w ¼ 0Þ, the subpopulation with x ¼ c<sup>m</sup> must be excluded from the analysis.

We now turn to standard parametric regression methods for estimating ATE, and then briefly discuss estimating ATE1. It is useful to decompose the counterfactual outcomes into their means and a stochastic part with zero mean, as we did at the end of Section 18.2:

$$y_0 = \mu_0 + v_0, \qquad E(v_0) = 0$$
 (18.8)

$$y_1 = \mu_1 + v_1, \qquad E(v_1) = 0$$
 (18.9)

Plugging these into equation (18.3) gives

$$y = \mu_0 + (\mu_1 - \mu_0)w + v_0 + w(v_1 - v_0)$$
(18.10)

This is a simple example of a switching regression model, where the outcome equations depend on the regime (treatment status in this case).

If we assume that v<sup>1</sup> v<sup>0</sup> has zero mean conditional on x, we obtain a standard regression model under Assumption ATE.1<sup>0</sup> .

proposition 18.1: Under Assumption ATE.1<sup>0</sup> , assume, in addition, that

$$\mathbf{E}(v_1 \mid \mathbf{x}) = \mathbf{E}(v_0 \mid \mathbf{x}) \tag{18.11}$$

Then ATE<sup>1</sup> ¼ ATE, and

$$E(y \mid w, \mathbf{x}) = \mu_0 + \alpha w + g_0(\mathbf{x})$$
(18.12)

where a 1ATE and g0ðxÞ ¼ Eðv<sup>0</sup> j xÞ. If, in addition, Eðv<sup>0</sup> j xÞ ¼ h<sup>0</sup> þ h0ðxÞ*b*<sup>0</sup> for some vector function h0ðxÞ, then

$$E(y \mid w, \mathbf{x}) = \gamma_0 + \alpha w + \mathbf{h}_0(\mathbf{x}) \boldsymbol{\beta}_0$$
 (18.13)

where g<sup>0</sup> ¼ m<sup>0</sup> þ h0.

Proof: Under Assumption ATE.1<sup>0</sup> , Eðy<sup>1</sup> j w; xÞ ¼ m<sup>1</sup> þ Eðv<sup>1</sup> j xÞ and Eðy<sup>0</sup> j w; xÞ ¼ m<sup>0</sup> þ Eðv<sup>0</sup> j xÞ. Under assumption (18.11), Eðy<sup>1</sup> j w; xÞ Eðy<sup>0</sup> j w; xÞ ¼ m<sup>1</sup> m0.

{619}------------------------------------------------

Therefore, by iterated expectations, Eðy<sup>1</sup> j wÞ Eðy<sup>0</sup> j wÞ ¼ m<sup>1</sup> m0, which implies that ATE<sup>1</sup> ¼ ATE. The proof of equation (18.12) follows by taking the expectation of equation (18.10) given w, x and using Assumption ATE.1<sup>0</sup> and assumption (18.11).

This proposition shows that when the predicted person-specific gain given x is zero—that is, when Eðv<sup>1</sup> v<sup>0</sup> j xÞ ¼ 0—Eðy jw; xÞ is additive in w and a function of x, and the coefficient on w is the average treatment effect. It follows that standard regression methods can be used to estimate ATE. While nonlinear regression methods can be used if Eðv<sup>0</sup> j xÞ is assumed to be nonlinear in parameters, typically we would use an assumption such as equation (18.13). Then, regressing y on an intercept, w, and h0ðxÞ consistently estimates the ATE. By putting enough controls in x, we have arranged it so that w and unobservables affecting ðy0; y1Þ are appropriately unrelated. In effect, x proxies for the unobservables. Using flexible functional forms for the elements of h0ðxÞ should provide a good approximation to Eðv<sup>0</sup> j xÞ.

The function h0ðxÞ*b*<sup>0</sup> in equation (18.13) is an example of a control function: when added to the regression of y on 1, w, it controls for possible self-selection bias. Of course, this statement is only true under the assumptions in Proposition 18.1.

Given Assumption ATE.1<sup>0</sup> , the additively separable form of equation (18.12) hinges crucially on assumption (18.11). Though assumption (18.11) might be reasonable in some cases, it need not generally hold. [A sufficient, but not necessary, condition for assumption (18.11) is v<sup>1</sup> ¼ v<sup>0</sup> or y<sup>1</sup> ¼ a þ y0, which means the effect of treatment is the same for everyone in the population.] If we relax assumption (18.11), then we no longer have equality of ATE and ATE1. Nevertheless, a regression formulation can be used to estimate ATE:

proposition 18.2: Under Assumption ATE.1<sup>0</sup> ,

$$E(y \mid w, \mathbf{x}) = \mu_0 + \alpha w + g_0(\mathbf{x}) + w[g_1(\mathbf{x}) - g_0(\mathbf{x})]$$
where  $\alpha = ATE$ ,  $g_0(\mathbf{x}) \equiv E(v_0 \mid \mathbf{x})$ , and  $g_1(\mathbf{x}) \equiv E(v_1 \mid \mathbf{x})$ .

The proof of Proposition 18.2 is immediate by taking the expectation of equation (18.10) given ðw; xÞ. Equation (18.14) is interesting because it shows that, under Assumption ATE.1<sup>0</sup> only, Eðy j w; xÞ is additive in w, a function of x, and an interaction between w and another function of x. The coefficient on w is the average treatment effect (but not generally ATE1). To operationalize equation (18.14) in a parametric framework, we would replace g0ðÞ and g1ðÞ with parametric functions of x; typically, these would be linear in parameters, say h<sup>0</sup> þ h0ðxÞ*b*<sup>0</sup> and h<sup>1</sup> þ h1ðxÞ*b*1. For notational simplicity, assume that these are both linear in x. Then we can write

{620}------------------------------------------------

$$E(y \mid w, \mathbf{x}) = \gamma + \alpha w + \mathbf{x} \boldsymbol{\beta}_0 + w \cdot (\mathbf{x} - \boldsymbol{\psi}) \boldsymbol{\delta}$$
(18.15)

where  $\beta_0$  and  $\delta$  are vectors of unknown parameters and  $\psi \equiv E(\mathbf{x})$ . Subtracting the mean from  $\mathbf{x}$  ensures that ATE is the coefficient on w. In practice, either we would subtract off the known population mean from each element of  $\mathbf{x}$ , or, more likely, we would demean each element of  $\mathbf{x}$  using the sample average. Therefore, under equation (18.15), we would estimate  $\alpha$  as the coefficient on w in the regression

$$y_i \text{ on } 1, w_i, \mathbf{x}_i, w_i(\mathbf{x}_i - \overline{\mathbf{x}}), \qquad i = 1, 2, \dots, N$$
 (18.16)

where  $\overline{\mathbf{x}}$  is the vector of sample averages. (Subtracting the sample averages rather than population averages introduces a generated regressor problem. However, as argued in Problem 6.10, the adjustments to the standard errors typically have minor effects.) The control functions in this case involve not just the  $\mathbf{x}_i$ , but also interactions of the covariates with the treatment variable. If desired, we can be selective about which elements of  $(\mathbf{x}_i - \overline{\mathbf{x}})$  we interact with  $w_i$ .

Adding functions of x, such as squares or logarithms, as both level terms and interactions, is simple, provided we demean any functions before constructing the interactions.

Because regression (18.16) consistently estimates  $\delta$ , we can also study how the ATE given  $\mathbf{x}$ , that is,  $ATE(\mathbf{x}) = \mathrm{E}(y_1 - y_0 \mid \mathbf{x})$ , changes with elements of  $\mathbf{x}$ . In particular, for any  $\mathbf{x}$  in the valid range,

$$A\hat{T}E(\mathbf{x}) = \hat{\alpha} + (\mathbf{x} - \overline{\mathbf{x}})\hat{\boldsymbol{\delta}}$$

We can then average this equation over interesting values of  $\mathbf{x}$  to obtain the ATE for a subset of the population. For example, if  $\mathbf{x}$  contains pretraining earnings or indicators for earnings groups, we can estimate how the ATE changes for various levels of pretraining earnings.

If the functions of  $\mathbf{x}$  appearing in the regression are very flexible, problems with estimating  $ATE(\mathbf{x})$  at certain values of  $\mathbf{x}$  can arise. In the extreme case, we define dummy variables for each possible outcome on  $\mathbf{x}$  and use these in place of  $\mathbf{x}$ . This approach results in what is known as a **saturated model**. We will not be able to include dummy variables for groups that are always treated or never treated, with the result that our estimator of ATE is for the population that excludes these groups.

To estimate  $ATE_1$ , write  $ATE_1 = \alpha + [E(\mathbf{x} \mid w = 1) - \psi] \delta$ , and so a consistent estimator is

$$A\hat{T}E_1 = \hat{\alpha} + \left(\sum_{i=1}^N w_i\right)^{-1} \left[\sum_{i=1}^N w_i(\mathbf{x}_i - \overline{\mathbf{x}})\hat{\boldsymbol{\delta}}\right]$$


{621}------------------------------------------------

Obtaining a standard error for this estimator is somewhat complicated, but it can be done using the delta method or bootstrapping.

Example 18.1 (Effects of Enterprise Zones on Economic Development): Consider evaluating the effects of enterprise zone (EZ) designation on employment growth, for block groups in a particular state. Suppose that we have 1980 and 1990 census data, and that the EZ designation originated in the early 1980s. To account for the fact that zone designation is likely to depend on prior economic performance, and perhaps other block characteristics, we can estimate a model such as the following:

$$\begin{split} gemp &= \mu_0 + \alpha ez + \beta_1 \, \log(emp80) + \beta_2 \, \log(pop80) + \beta_3 percmanf80 \\ &+ \beta_4 \, \log(housval80) + \beta_5 ez \cdot \left[\log(emp80) - m_1\right] + \beta_6 ez \cdot \left[\log(pop80) - m_2\right] \\ &+ \beta_7 ez \cdot \left[percmanf80 - m_3\right] + \beta_8 ez \cdot \left[\log(housval80) - m_4\right] + error \end{split}$$

where the right-hand-side variables are a dummy variable for EZ designation, employment, population, percent of employment in manufacturing, and median housing value, all in 1980, and where the mj are the sample averages.

The regression estimator (18.16), especially with flexible functions of the covariates, applies directly to what are called regression discontinuity designs. In this case, treatment is determined as a nonstochastic function of a covariate, say w ¼ fðsÞ, where s is an element of x that has sufficient variation. The key is that f is a discontinuous function of s, typically a step function, w ¼ 1½s as0-, where s<sup>0</sup> is a known threshold. The idea is that once s, which could be income level or class size, reaches a certain threshold, a policy automatically kicks in. (See, for example, Angrist and Lavy, 1999.) Because s is a nonrandom function of x, the conditional independence assumption in Assumption ATE.1 must hold. The key is obtaining flexible functional forms for g0ðÞ and g1ðÞ. Generally, we can identify a only if we are willing to assume that g0ðÞ and g1ðÞ are smooth functions of x (which is almost always the case when we estimate parametric or nonparametric regression functions). If we allow g0ðÞ to be discontinuous in s—that is, with jumps—we could never distinguish between changes in y due to a change in s or a change in treatment status.