# 9.11. Consider a two-equation SEM:

> Pages: 257-259

$$y_1 = \gamma_{12}y_2 + \delta_{11}z_1 + u_1$$
  

$$y_2 = \gamma_{21}y_1 + \delta_{22}z_2 + \delta_{23}z_3 + u_2$$
  

$$E(u_1|z_1, z_2, z_3) = E(u_2|z_1, z_2, z_3) = 0$$

where, for simplicity, we omit intercepts. The exogenous variable z<sup>1</sup> is a policy variable, such as a tax rate. Assume that g12g<sup>21</sup> 01. The structural errors, u<sup>1</sup> and u2, may be correlated.

- a. Under what assumptions is each equation identified?
- b. The reduced form for y<sup>1</sup> can be written in conditional expectation form as Eðy<sup>1</sup> j zÞ ¼ p11z<sup>1</sup> þ p12z<sup>2</sup> þ p13z3, where z ¼ ðz1; z2; z3Þ. Find the p<sup>11</sup> in terms of the ggj and dgj.
- c. How would you estimate the structural parameters? How would you obtain p^<sup>11</sup> in terms of the structural parameter estimates?
- d. Suppose that z<sup>2</sup> should be in the first equation, but it is left out in the estimation from part c. What effect does this omission have on estimating qEðy<sup>1</sup> j zÞ=qz1? Does it matter whether you use single-equation or system estimators of the structural parameters?
- e. If you are only interested in qEðy<sup>1</sup> j zÞ=qz1, what could you do instead of estimating an SEM?
- f. Would you say estimating a simultaneous equations model is a robust method for estimating qEðy<sup>1</sup> j zÞ=qz1? Explain.
- 9.12. The following is a two-equation, nonlinear SEM:

$$y_1 = \delta_{10} + \gamma_{12}y_2 + \gamma_{13}y_2^2 + \mathbf{z}_1\boldsymbol{\delta}_1 + u_1$$
  
$$y_2 = \delta_{20} + \gamma_{12}y_1 + \mathbf{z}_2\boldsymbol{\delta}_2 + u_2$$

where u<sup>1</sup> and u<sup>2</sup> have zero means conditional on all exogenous variables, z. (For emphasis, we have included separate intercepts.) Assume that both equations are identified when g<sup>13</sup> ¼ 0.

- a. When g<sup>13</sup> ¼ 0, Eðy<sup>2</sup> j zÞ ¼ p<sup>20</sup> þ z*p*2. What is Eðy<sup>2</sup> <sup>2</sup> j zÞ under homoskedasticity assumptions for u<sup>1</sup> and u2?
- b. Use part a to find Eðy<sup>1</sup> j zÞ when g<sup>13</sup> ¼ 0.
- c. Use part b to argue that, when g<sup>13</sup> ¼ 0, the forbidden regression consistently estimates the parameters in the first equation, including g<sup>13</sup> ¼ 0.

{258}------------------------------------------------

- d. If u<sup>1</sup> and u<sup>2</sup> have constant variances conditional on z, and g<sup>13</sup> happens to be zero, show that the optimal instrumental variables for estimating the first equation are f1; z; ½Eðy<sup>2</sup> j zÞ<sup>2</sup> g. (Hint: Use Theorem 8.5; for a similar problem, see Problem 8.11.)
- e. Reestimate equation (9.61) using IVs ½1; z;ðy^2Þ 2 , where z is all exogenous variables appearing in equations (9.61) and (9.62) and y^<sup>2</sup> denotes the fitted values from regressing logðwageÞ on 1, z. Discuss the results.
- 9.13. For this question use the data in OPENNESS.RAW, taken from Romer (1993).
- a. A simple simultaneous equations model to test whether ''openness'' (open) leads to lower inflation rates (inf ) is

$$inf = \delta_{10} + \gamma_{12}open + \delta_{11} \log(pcinc) + u_1$$
$$open = \delta_{20} + \gamma_{21}inf + \delta_{21} \log(pcinc) + \delta_{22} \log(land) + u_2$$

Assuming that pcinc (per capita income) and land (land area) are exogenous, under what assumption is the first equation identified?

- b. Estimate the reduced form for open to verify that logðlandÞis statistically significant.
- c. Estimate the first equation from part a by 2SLS. Compare the estimate of g<sup>12</sup> with the OLS estimate.
- d. Add the term g13open<sup>2</sup> to the first equation, and propose a way to test whether it is statistically significant. (Use only one more IV than you used in part c.)
- e. With g13open<sup>2</sup> in the first equation, use the following method to estimate d10, g12, g13, and d11: (1) Regress open on 1, logð pcincÞ and logðlandÞ, and obtain the fitted values, open ^ . (2) Regress inf on 1, open ^ , ðopen ^ Þ 2 , and logð pcincÞ. Compare the results with those from part d. Which estimates do you prefer?

{259}------------------------------------------------

In Chapter 7 we covered a class of linear panel data models where, at a minimum, the error in each time period was assumed to be uncorrelated with the explanatory variables in the same time period. For certain panel data applications this assumption is too strong. In fact, a primary motivation for using panel data is to solve the omitted variables problem.

In this chapter we study population models that explicitly contain a time-constant, unobserved effect. The treatment in this chapter is ''modern'' in the sense that unobserved effects are treated as random variables, drawn from the population along with the observed explained and explanatory variables, as opposed to parameters to be estimated. In this framework, the key issue is whether the unobserved effect is uncorrelated with the explanatory variables.