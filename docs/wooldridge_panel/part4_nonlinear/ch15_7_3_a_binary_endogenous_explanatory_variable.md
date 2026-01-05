# A Binary Endogenous Explanatory Variable

> Pages: 486-488

We now consider the case where the probit model contains a binary explanatory variable that is endogenous. The model is

$$y_1 = 1[\mathbf{z}_1 \delta_1 + \alpha_1 y_2 + u_1 > 0]$$
 (15.51)

$$y_2 = 1[\mathbf{z}\delta_2 + v_2 > 0] \tag{15.52}$$

where ðu1; v2Þ is independent of z and distributed as bivariate normal with mean zero, each has unit variance, and r<sup>1</sup> ¼ Corrðu1; v2Þ. If r<sup>1</sup> 00, then u<sup>1</sup> and y<sup>2</sup> are correlated, and probit estimation of equation (15.51) is inconsistent for *d*<sup>1</sup> and a1.

As discussed in Section 15.7.2, the normalization Varðu1Þ ¼ 1 is the proper one for computing average partial effects. Often, the effect of y<sup>2</sup> is of primary interest, especially when y<sup>2</sup> indicates participation in some sort of program, such as job training, and the binary outcome y<sup>1</sup> might denote employment status. The average treatment effect (for a given value of z1) is Fðz1*d*<sup>1</sup> þ a1Þ Fðz1*d*1Þ.

To derive the likelihood function, we again need the joint distribution of ðy1; y2Þ given z, which we obtain from equation (15.48). To obtain Pðy<sup>1</sup> ¼ 1 j y2; zÞ, first note that

$$\mathbf{P}(y_1 = 1 \mid v_2, \mathbf{z}) = \Phi[(\mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + \rho_1 v_2) / (1 - \rho_1^2)^{1/2}]$$
(15.53)

Since y<sup>2</sup> ¼ 1 if and only if v<sup>2</sup> > z*d*2, we need a basic fact about truncated normal distributions: If v<sup>2</sup> has a standard normal distribution and is independent of z, then the density of v<sup>2</sup> given v<sup>2</sup> > z*d*<sup>2</sup> is

$$\phi(v_2)/P(v_2 > -\mathbf{z}\boldsymbol{\delta}_2) = \phi(v_2)/\Phi(\mathbf{z}\boldsymbol{\delta}_2)$$
(15.54)

Therefore,

{487}------------------------------------------------

$$P(y_{1} = 1 | y_{2} = 1, \mathbf{z}) = E[P(y_{1} = 1 | v_{2}, \mathbf{z}) | y_{2} = 1, \mathbf{z}]$$

$$= E\{\Phi[(\mathbf{z}_{1}\boldsymbol{\delta}_{1} + \alpha_{1}y_{2} + \rho_{1}v_{2})/(1 - \rho_{1}^{2})^{1/2}] | y_{2} = 1, \mathbf{z}\}$$

$$= \frac{1}{\Phi(\mathbf{z}\boldsymbol{\delta}_{2})} \int_{-\mathbf{z}\boldsymbol{\delta}_{2}}^{\infty} \Phi[(\mathbf{z}_{1}\boldsymbol{\delta}_{1} + \alpha_{1}y_{2} + \rho_{1}v_{2})/(1 - \rho_{1}^{2})^{1/2}]\phi(v_{2}) dv_{2}$$
(15.55)

where  $v_2$  in the integral is a dummy argument of integration. Of course  $P(y_1 = 0 | y_2 = 1, \mathbf{z})$  is just one minus equation (15.55).

Similarly, 
$$P(y_1 = 1 | y_2 = 0, \mathbf{z})$$
 is

$$\frac{1}{1 - \Phi(\mathbf{z}\boldsymbol{\delta}_2)} \int_{-\infty}^{-\mathbf{z}\boldsymbol{\delta}_2} \Phi[(\mathbf{z}_1\boldsymbol{\delta}_1 + \alpha_1y_2 + \rho_1v_2)/(1 - \rho_1^2)^{1/2}]\phi(v_2) dv_2$$
 (15.56)

Combining the four possible outcomes of  $(y_1, y_2)$ , along with the probit model for  $y_2$ , and taking the log gives the log-likelihood function for maximum likelihood analysis. It is messy but certainly doable. Evans and Schwab (1995) use the MLE approach to study the causal effects of attending a Catholic high school on the probability of attending college, allowing the Catholic high school indicator to be correlated with unobserved factors that affect college attendence. As an IV they use a binary variable indicating whether a student is Catholic.

Because the MLE is nontrivial to compute, it is tempting to use some seemingly "obvious" two-step procedures. As an example, we might try to inappropriately mimic 2SLS. Since  $E(y_2 | \mathbf{z}) = \Phi(\mathbf{z}\boldsymbol{\delta}_2)$  and  $\boldsymbol{\delta}_2$  is consistently estimated by probit of  $y_2$  on  $\mathbf{z}$ , it is tempting to estimate  $\boldsymbol{\delta}_1$  and  $\alpha_1$  from the probit of  $y_1$  on  $\mathbf{z}$ ,  $\hat{\boldsymbol{\Phi}}_2$ , where  $\hat{\boldsymbol{\Phi}}_2 \equiv \Phi(\mathbf{z}\hat{\boldsymbol{\delta}}_2)$ . This approach does not produce consistent estimators, for the same reasons the forbidden regression discussed in Section 9.5 for nonlinear simultaneous equations models does not. For this two-step procedure to work, we would have to have  $P(y_1 = 1 | \mathbf{z}) = \Phi[\mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 \Phi(\mathbf{z}\boldsymbol{\delta}_2)]$ . But  $P(y_1 = 1 | \mathbf{z}) = E(y_1 | \mathbf{z}) = E(1[\mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1 > 0] | \mathbf{z})$ , and since the indicator function  $1[\cdot]$  is nonlinear, we cannot pass the expected value through. If we were to compute the correct (complicated) formula for  $P(y_1 = 1 | \mathbf{z})$ , plug in  $\hat{\boldsymbol{\delta}}_2$ , and then maximize the resulting binary response log likelihood, then the two-step approach would produce consistent estimators. But full maximum likelihood is easier and more efficient.

As mentioned in the previous subsection, we can use the Rivers-Vuong approach to *test* for exogeneity of  $y_2$ . This has the virtue of being simple, and, if the test fails to reject, we may not need to compute the MLE. A more efficient test is the score test of  $H_0$ :  $\rho_1 = 0$ , and this does not require estimation of the full MLE.

{488}------------------------------------------------