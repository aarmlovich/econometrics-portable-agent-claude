# 5.2. Consider a model for the health of an individual:

> Pages: 123-129

$$health = \beta_0 + \beta_1 age + \beta_2 weight + \beta_3 height + \beta_4 male + \beta_5 work + \beta_6 exercise + u_1$$
 (5.53)

where health is some quantitative measure of the person's health, age, weight, height, and male are self-explanatory, work is weekly hours worked, and exercise is the hours of exercise per week.

- a. Why might you be concerned about exercise being correlated with the error term u1?
- b. Suppose you can collect data on two additional variables, disthome and distwork, the distances from home and from work to the nearest health club or gym. Discuss whether these are likely to be uncorrelated with u1.
- c. Now assume that disthome and distwork are in fact uncorrelated with u1, as are all variables in equation (5.53) with the exception of exercise. Write down the reduced form for exercise, and state the conditions under which the parameters of equation (5.53) are identified.
- d. How can the identification assumption in part c be tested?
- 5.3. Consider the following model to estimate the effects of several variables, including cigarette smoking, on the weight of newborns:

{124}------------------------------------------------

$$\log(bwght) = \beta_0 + \beta_1 male + \beta_2 parity + \beta_3 \log(faminc) + \beta_4 packs + u$$
 (5.54)

where male is a binary indicator equal to one if the child is male; parity is the birth order of this child; faminc is family income; and packs is the average number of packs of cigarettes smoked per day during pregnancy.

- a. Why might you expect packs to be correlated with u?
- b. Suppose that you have data on average cigarette price in each woman's state of residence. Discuss whether this information is likely to satisfy the properties of a good instrumental variable for packs.
- c. Use the data in BWGHT.RAW to estimate equation (5.54). First, use OLS. Then, use 2SLS, where cigprice is an instrument for packs. Discuss any important differences in the OLS and 2SLS estimates.
- d. Estimate the reduced form for packs. What do you conclude about identification of equation (5.54) using cigprice as an instrument for packs? What bearing does this conclusion have on your answer from part c?

# 5.4. Use the data in CARD.RAW for this problem.

- a. Estimate a logðwageÞ equation by OLS with educ, exper, exper2, black, south, smsa, reg661 through reg668, and smsa66 as explanatory variables. Compare your results with Table 2, Column (2) in Card (1995).
- b. Estimate a reduced form equation for educ containing all explanatory variables from part a and the dummy variable nearc4. Do educ and nearc4 have a practically and statistically significant partial correlation? [See also Table 3, Column (1) in Card (1995).]
- c. Estimate the logðwageÞ equation by IV, using nearc4 as an instrument for educ. Compare the 95 percent confidence interval for the return to education with that obtained from part a. [See also Table 3, Column (5) in Card (1995).]
- d. Now use nearc2 along with nearc4 as instruments for educ. First estimate the reduced form for educ, and comment on whether nearc2 or nearc4 is more strongly related to educ. How do the 2SLS estimates compare with the earlier estimates?
- e. For a subset of the men in the sample, IQ score is available. Regress iq on nearc4. Is IQ score uncorrelated with nearc4?
- f. Now regress iq on nearc4 along with smsa66, reg661, reg662, and reg669. Are iq and nearc4 partially correlated? What do you conclude about the importance of controlling for the 1966 location and regional dummies in the logðwageÞ equation when using nearc4 as an IV for educ?

{125}------------------------------------------------

5.5. One occasionally sees the following reasoning used in applied work for choosing instrumental variables in the context of omitted variables. The model is

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + \gamma q + a_1$$

where q is the omitted factor. We assume that a<sup>1</sup> satisfies the structural error assumption Eða<sup>1</sup> j z1; y2; qÞ ¼ 0, that z<sup>1</sup> is exogenous in the sense that Eðq j z1Þ ¼ 0, but that y<sup>2</sup> and q may be correlated. Let z<sup>2</sup> be a vector of instrumental variable candidates for y2. Suppose it is known that z<sup>2</sup> appears in the linear projection of y<sup>2</sup> onto ðz1; z2Þ, and so the requirement that z<sup>2</sup> be partially correlated with y<sup>2</sup> is satisfied. Also, we are willing to assume that z<sup>2</sup> is redundant in the structural equation, so that a<sup>1</sup> is uncorrelated with z2. What we are unsure of is whether z<sup>2</sup> is correlated with the omitted variable q, in which case z<sup>2</sup> would not contain valid IVs.

To ''test'' whether z<sup>2</sup> is in fact uncorrelated with q, it has been suggested to use OLS on the equation

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + \mathbf{z}_2 \boldsymbol{\psi}_1 + u_1 \tag{5.55}$$

where u<sup>1</sup> ¼ gq þ a1, and test H0: *c*<sup>1</sup> ¼ 0. Why does this method not work?

- 5.6. Refer to the multiple indicator model in Section 5.3.2.
- a. Show that if q<sup>2</sup> is uncorrelated with xj, j ¼ 1; 2; ... ; K, then the reduced form of q<sup>1</sup> depends only on q2. [Hint: Use the fact that the reduced form of q<sup>1</sup> is the linear projection of q<sup>1</sup> onto ð1; x1; x2; ... ; xK ; q2Þ and find the coefficient vector on x using Property LP.7 from Chapter 2.]
- b. What happens if q<sup>2</sup> and x are correlated? In this setting, is it realistic to assume that q<sup>2</sup> and x are uncorrelated? Explain.
- 5.7. Consider model (5.45) where v has zero mean and is uncorrelated with x1; ... ; xK and q. The unobservable q is thought to be correlated with at least some of the xj. Assume without loss of generality that EðqÞ ¼ 0.

You have a single indicator of q, written as q<sup>1</sup> ¼ d1q þ a1, d<sup>1</sup> 0 0, where a<sup>1</sup> has zero mean and is uncorrelated with each of xj, q, and v. In addition, z1; z2; ... ; zM is a set of variables that are (1) redundant in the structural equation (5.45) and (2) uncorrelated with a1.

- a. Suggest an IV method for consistently estimating the bj. Be sure to discuss what is needed for identification.
- b. If equation (5.45) is a logðwageÞ equation, q is ability, q<sup>1</sup> is IQ or some other test score, and z1; ... ; zM are family background variables, such as parents' education and

{126}------------------------------------------------

number of siblings, describe the economic assumptions needed for consistency of the the IV procedure in part a.

- c. Carry out this procedure using the data in NLS80.RAW. Include among the explanatory variables *exper*, *tenure*, *educ*, *married*, *south*, *urban*, and *black*. First use IQ as  $q_1$  and then KWW. Include in the  $z_h$  the variables *meduc*, *feduc*, and *sibs*. Discuss the results.
- **5.8.** Consider a model with unobserved heterogeneity (q) and measurement error in an explanatory variable:

$$y = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K^* + q + v$$

where  $e_K = x_K - x_K^*$  is the measurement error and we set the coefficient on q equal to one without loss of generality. The variable q might be correlated with any of the explanatory variables, but an indicator,  $q_1 = \delta_0 + \delta_1 q + a_1$ , is available. The measurement error  $e_K$  might be correlated with the observed measure,  $x_K$ . In addition to  $q_1$ , you also have variables  $z_1, z_2, \ldots, z_M, M \ge 2$ , that are uncorrelated with  $v, a_1$ , and  $e_K$ .

- a. Suggest an IV procedure for consistently estimating the  $\beta_j$ . Why is  $M \ge 2$  required? (Hint: Plug in  $q_1$  for q and  $x_K$  for  $x_K^*$ , and go from there.)
- b. Apply this method to the model estimated in Example 5.5, where actual education, say  $educ^*$ , plays the role of  $x_K^*$ . Use IQ as the indicator of q = ability, and KWW, meduc, feduc, and sibs as the elements of  $\mathbf{z}$ .
- **5.9.** Suppose that the following wage equation is for working high school graduates:

$$\log(wage) = \beta_0 + \beta_1 exper + \beta_2 exper^2 + \beta_3 twoyr + \beta_4 fouryr + u$$

where *twoyr* is years of junior college attended and *fouryr* is years completed at a four-year college. You have distances from each person's home at the time of high school graduation to the nearest two-year and four-year colleges as instruments for *twoyr* and *fouryr*. Show how to rewrite this equation to test  $H_0$ :  $\beta_3 = \beta_4$  against  $H_0$ :  $\beta_4 > \beta_3$ , and explain how to estimate the equation. See Kane and Rouse (1995) and Rouse (1995), who implement a very similar procedure.

**5.10.** Consider IV estimation of the simple linear model with a single, possibly endogenous, explanatory variable, and a single instrument:

$$y=\beta_0+\beta_1x+u$$
 
$$\mathrm{E}(u)=0,\qquad \mathrm{Cov}(z,u)=0,\qquad \mathrm{Cov}(z,x)\neq 0,\qquad \mathrm{E}(u^2\,|\,z)=\sigma^2$$

{127}------------------------------------------------

a. Under the preceding (standard) assumptions, show that Avar  $\sqrt{N}(\hat{\beta}_1 - \beta_1)$  can be expressed as  $\sigma^2/(\rho_{zx}^2\sigma_x^2)$ , where  $\sigma_x^2 = \mathrm{Var}(x)$  and  $\rho_{zx} = \mathrm{Corr}(z,x)$ . Compare this result with the asymptotic variance of the OLS estimator under Assumptions OLS.1–OLS.3.

- b. Comment on how each factor affects the asymptotic variance of the IV estimator. What happens as  $\rho_{zx} \to 0$ ?
- **5.11.** A model with a single endogenous explanatory variable can be written as

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1, \quad \mathbf{E}(\mathbf{z}' u_1) = \mathbf{0}$$

where  $\mathbf{z} = (\mathbf{z}_1, \mathbf{z}_2)$ . Consider the following two-step method, intended to mimic 2SLS:

- a. Regress  $y_2$  on  $\mathbf{z}_2$ , and obtain fitted values,  $\tilde{y}_2$ . (That is,  $\mathbf{z}_1$  is omitted from the first-stage regression.)
- b. Regress  $y_1$  on  $\mathbf{z}_1$ ,  $\tilde{y}_2$  to obtain  $\tilde{\boldsymbol{\delta}}_1$  and  $\tilde{\alpha}_1$ . Show that  $\tilde{\boldsymbol{\delta}}_1$  and  $\tilde{\alpha}_1$  are generally inconsistent. When would  $\tilde{\boldsymbol{\delta}}_1$  and  $\tilde{\alpha}_1$  be consistent? [Hint: Let  $y_2^0$  be the population linear projection of  $y_2$  on  $\mathbf{z}_2$ , and let  $a_2$  be the projection error:  $y_2^0 = \mathbf{z}_2 \lambda_2 + a_2$ ,  $\mathrm{E}(\mathbf{z}_2'a_2) = \mathbf{0}$ . For simplicity, pretend that  $\lambda_2$  is known, rather than estimated; that is, assume that  $\tilde{y}_2$  is actually  $y_2^0$ . Then, write

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2^0 + \alpha_1 a_2 + u_1$$

and check whether the composite error  $\alpha_1 a_2 + u_1$  is uncorrelated with the explanatory variables.]

- **5.12.** In the setup of Section 5.1.2 with  $\mathbf{x} = (x_1, \dots, x_K)$  and  $\mathbf{z} \equiv (x_1, x_2, \dots, x_{K-1}, z_1, \dots, z_M)$  (let  $x_1 = 1$  to allow an intercept), assume that  $E(\mathbf{z}'\mathbf{z})$  is nonsingular. Prove that rank  $E(\mathbf{z}'\mathbf{x}) = K$  if and only if at least one  $\theta_j$  in equation (5.15) is different from zero. [Hint: Write  $\mathbf{x}^* = (x_1, \dots, x_{K-1}, x_K^*)$  as the linear projection of each element of  $\mathbf{x}$  on  $\mathbf{z}$ , where  $x_K^* = \delta_1 x_1 + \dots + \delta_{K-1} x_{K-1} + \theta_1 z_1 + \dots + \theta_M z_M$ . Then  $\mathbf{x} = \mathbf{x}^* + \mathbf{r}$ , where  $E(\mathbf{z}'\mathbf{r}) = \mathbf{0}$ , so that  $E(\mathbf{z}'\mathbf{x}) = E(\mathbf{z}'\mathbf{x}^*)$ . Now  $\mathbf{x}^* = \mathbf{z}\mathbf{\Pi}$ , where  $\mathbf{\Pi}$  is the  $L \times K$  matrix whose first K 1 columns are the first K 1 unit vectors in  $\mathbb{R}^L (1, 0, 0, \dots, 0)'$ ,  $(0, 1, 0, \dots, 0)'$ ,  $(0, 0, \dots, 1, 0, \dots, 0)'$ —and whose last column is  $(\delta_1, \delta_2, \dots, \delta_{K-1}, \theta_1, \dots, \theta_M)$ . Write  $E(\mathbf{z}'\mathbf{x}^*) = E(\mathbf{z}'\mathbf{z})\mathbf{\Pi}$ , so that, because  $E(\mathbf{z}'\mathbf{z})$  is nonsingular,  $E(\mathbf{z}'\mathbf{x}^*)$  has rank K if and only if  $\mathbf{\Pi}$  has rank K.]
- **5.13.** Consider the simple regression model

$$y = \beta_0 + \beta_1 x + u$$

and let z be a *binary* instrumental variable for x.

a. Show that the IV estimator  $\hat{\beta}_1$  can be written as

{128}------------------------------------------------

$$\hat{\beta}_1 = (\bar{y}_1 - \bar{y}_0)/(\bar{x}_1 - \bar{x}_0)$$

where  $\bar{y}_0$  and  $\bar{x}_0$  are the sample averages of  $y_i$  and  $x_i$  over the part of the sample with  $z_i = 0$ , and  $\bar{y}_1$  and  $\bar{x}_1$  are the sample averages of  $y_i$  and  $x_i$  over the part of the sample with  $z_i = 1$ . This estimator, known as a **grouping estimator**, was first suggested by Wald (1940).

- b. What is the interretation of  $\hat{\beta}_1$  if x is also binary, for example, representing participation in a social program?
- **5.14.** Consider the model in (5.1) and (5.2), where we have additional exogenous variables  $z_1, \ldots, z_M$ . Let  $\mathbf{z} = (1, x_1, \ldots, x_{K-1}, z_1, \ldots, z_M)$  be the vector of all exogenous variables. This problem essentially asks you to obtain the 2SLS estimator using linear projections. Assume that  $\mathbf{E}(\mathbf{z}'\mathbf{z})$  is nonsingular.
- a. Find  $L(y | \mathbf{z})$  in terms of the  $\beta_i, x_1, \dots, x_{K-1}$ , and  $x_K^* = L(x_K | \mathbf{z})$ .
- b. Argue that, provided  $x_1, \ldots, x_{K-1}, x_K^*$  are not perfectly collinear, an OLS regression of y on  $1, x_1, \ldots, x_{K-1}, x_K^*$ —using a random sample—consistently estimates all  $\beta_i$ .
- c. State a necessary and sufficient condition for  $x_K^*$  not to be a perfect linear combination of  $x_1, \ldots, x_{K-1}$ . What 2SLS assumption is this identical to?
- **5.15.** Consider the model  $y = \mathbf{x}\boldsymbol{\beta} + u$ , where  $x_1, x_2, \dots, x_{K_1}, K_1 \leq K$ , are the (potentially) endogenous explanatory variables. (We assume a zero intercept just to simplify the notation; the following results carry over to models with an unknown intercept.) Let  $z_1, \dots, z_{L_1}$  be the instrumental variables available from outside the model. Let  $\mathbf{z} = (z_1, \dots, z_{L_1}, x_{K_1+1}, \dots, x_K)$  and assume that  $E(\mathbf{z}'\mathbf{z})$  is nonsingular, so that Assumption 2SLS.2a holds.
- a. Show that a necessary condition for the rank condition, Assumption 2SLS.2b, is that for each  $j = 1, ..., K_1$ , at least one  $z_h$  must appear in the reduced form of  $x_j$ .
- b. With  $K_1 = 2$ , give a simple example showing that the condition from part a is not sufficient for the rank condition.
- c. If  $L_1 = K_1$ , show that a sufficient condition for the rank condition is that only  $z_j$  appears in the reduced form for  $x_j$ ,  $j = 1, ..., K_1$ . [As in Problem 5.12, it suffices to study the rank of the  $L \times K$  matrix  $\Pi$  in  $L(\mathbf{x} | \mathbf{z}) = \mathbf{z}\Pi$ .]

{129}------------------------------------------------

# 6.1 Estimation with Generated Regressors and Instruments