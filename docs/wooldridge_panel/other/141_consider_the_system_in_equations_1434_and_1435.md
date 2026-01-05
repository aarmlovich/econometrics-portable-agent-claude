# **14.1.** Consider the system in equations (14.34) and (14.35).

> Pages: 457-459

a. How would you estimate equation (14.35) using single-equation methods? Give a few possibilities, ranging from simple to more complicated. State any additional assumptions relevant for estimating asymptotic variances or for efficiency of the various estimators.

{458}------------------------------------------------

- b. Is equation (14.34) identified if  $\gamma_1 = 0$ ?
- c. Now suppose that  $y_3 = 0$ , so that the parameters in equation (14.35) can be consistently estimated by OLS. Let  $\hat{y}_2$  be the OLS fitted values. Explain why nonlinear least squares estimation of

$$y_1 = \mathbf{x}_1 \boldsymbol{\delta}_1 + \gamma_1 \hat{y}_2^{\gamma_2} + error$$

does not consistently estimate  $\delta_1$ ,  $\gamma_1$ , and  $\gamma_2$  when  $\gamma_1 \neq 0$  and  $\gamma_2 \neq 1$ .

**14.2.** Consider the following labor supply function nonlinear in parameters:

hours = 
$$\mathbf{z}_1 \boldsymbol{\delta}_1 + \gamma_1 (wage^{\rho_1} - 1)/\rho_1 + u_1$$
,  $E(u_1 | \mathbf{z}) = 0$ 

where  $\mathbf{z}_1$  contains unity and  $\mathbf{z}$  is the full set of exogenous variables.

- a. Show that this model contains the level-level and level-log models as special cases. [Hint: For w > 0,  $(w^{\rho} 1)/\rho \to \log(w)$  as  $\rho \to 0$ .]
- b. How would you test  $H_0$ :  $\gamma_1 = 0$ ? (Be careful here;  $\rho_1$  cannot be consistently estimated under  $H_0$ .)
- c. Assuming that  $\gamma_1 \neq 0$ , how would you estimate this equation if  $Var(u_1 \mid \mathbf{z}) = \sigma_1^2$ ? What if  $Var(u_1 \mid \mathbf{z})$  is not constant?
- d. Find the gradient of the residual function with respect to  $\delta_1$ ,  $\gamma_1$ , and  $\rho_1$ . [Hint: Recall that the derivative of  $w^{\rho}$  with respect to  $\rho$  is  $w^{\rho} \log(w)$ .]
- e. Explain how to obtain the score test of  $H_0$ :  $\rho_1 = 1$ .
- **14.3.** Use Theorem 14.3 to show that the optimal instrumental variables based on the conditional moment restrictions (14.60) are given by equation (14.63).
- **14.4.** a. Show that, under Assumptions WNLS.1–WNLS.3 in Chapter 12, the weighted NLS estimator has asymptotic variance equal to that of the efficient IV estimator based on the orthogonality condition  $E[(y_i m(\mathbf{x}_i, \boldsymbol{\beta}_0)) | \mathbf{x}_i] = 0$ .
- b. When does the nonlinear least squares estimator of  $\beta_0$  achieve the efficiency bound derived in part a?
- c. Suppose that, in addition to  $E(y | \mathbf{x}) = m(\mathbf{x}, \boldsymbol{\beta}_0)$ , you use the restriction  $Var(y | \mathbf{x}) = \sigma_0^2$  for some  $\sigma_0^2 > 0$ . Write down the two conditional moment restrictions for estimating  $\boldsymbol{\beta}_0$  and  $\sigma_0^2$ . What are the efficient instrumental variables?
- **14.5.** Write down  $\theta$ ,  $\pi$ , and the matrix **H** such that  $\pi = \mathbf{H}\theta$  in Chamberlain's approach to unobserved effects panel data models when T = 3.
- **14.6.** Let  $\hat{\pi}$  and  $\tilde{\pi}$  be two consistent estimators of  $\pi_0$ , with Avar  $\sqrt{N}(\hat{\pi} \pi_0) = \Xi_0$  and Avar  $\sqrt{N}(\tilde{\pi} \pi_0) = \Lambda_0$ . Let  $\hat{\theta}$  be the CMD estimator based on  $\hat{\pi}$ , and let  $\tilde{\theta}$  be

{459}------------------------------------------------

the CMD estimator based on  $\tilde{\pi}$ , where  $\pi_o = \mathbf{h}(\theta_o)$ . Show that, if  $\Lambda_o - \Xi_o$  is positive semidefinite, then so is Avar  $\sqrt{N}(\tilde{\theta} - \theta_o) - \text{Avar } \sqrt{N}(\hat{\theta} - \theta_o)$ . (Hint: Twice use the fact that, for two positive definite matrices  $\mathbf{A}$  and  $\mathbf{B}$ ,  $\mathbf{A} - \mathbf{B}$  is p.s.d. if and only if  $\mathbf{B}^{-1} - \mathbf{A}^{-1}$  is p.s.d.)

**14.7.** Show that when the mapping from  $\theta_0$  to  $\pi_0$  is linear,  $\pi_0 = \mathbf{H}\theta_0$  for a known  $S \times P$  matrix  $\mathbf{H}$  with rank( $\mathbf{H}$ ) = P, the CMD estimator  $\hat{\boldsymbol{\theta}}$  is

$$\hat{\boldsymbol{\theta}} = (\mathbf{H}'\hat{\mathbf{\Xi}}^{-1}\mathbf{H})^{-1}\mathbf{H}'\hat{\mathbf{\Xi}}^{-1}\hat{\boldsymbol{\pi}}$$
 (14.81)

Equation (14.81) looks like a generalized least squares (GLS) estimator of  $\hat{\pi}$  on **H** using variance matrix  $\hat{\Xi}$ , and this apparent similarity has prompted some to call the minimum chi-square estimator a "generalized least squares" (GLS) estimator. Unfortunately, the association between CMD and GLS is misleading because  $\hat{\pi}$  and **H** are not data vectors whose row dimension, S, grows with N. The asymptotic properties of the minimum chi-square estimator do *not* follow from those of GLS.

- **14.8.** In Problem 13.9, suppose you model the unconditional distribution of  $y_0$  as  $f_0(y_0; \theta)$ , which depends on at least some elements of  $\theta$  appearing in  $f_t(y_t | y_{t-1}; \theta)$ . Discuss the pros and cons of using  $f_0(y_0; \theta)$  in a maximum likelihood analysis along with  $f_t(y_t | y_{t-1}; \theta)$ , t = 1, 2, ..., T.
- **14.9.** Verify that, for the linear unobserved effects model under Assumptions RE.1–RE.3, the conditions of Lemma 14.1 hold for the fixed effects  $(\hat{\boldsymbol{\theta}}_2)$  and the random effects  $(\hat{\boldsymbol{\theta}}_1)$  estimators, with  $\rho = \sigma_u^2$ . [Hint: For clarity, it helps to introduce a cross section subscript, *i*. Then  $\mathbf{A}_1 = \mathrm{E}(\check{\mathbf{X}}_i'\check{\mathbf{X}}_i)$ , where  $\check{\mathbf{X}}_i = \mathbf{X}_i \lambda \mathbf{j}_T \overline{\mathbf{x}}_i$ ;  $\mathbf{A}_2 = \mathrm{E}(\ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i)$ , where  $\ddot{\mathbf{X}}_i = \mathbf{X}_i \mathbf{j}_T \overline{\mathbf{x}}_i$ ;  $\mathbf{s}_{i1} = \check{\mathbf{X}}_i'\mathbf{r}_i$ , where  $\mathbf{r}_i = \mathbf{v}_i \lambda \mathbf{j}_T \bar{v}_i$ ; and  $\mathbf{s}_{i2} = \ddot{\mathbf{X}}_i'\mathbf{u}_i$ ; see Chapter 10 for further notation. You should show that  $\ddot{\mathbf{X}}_i'\mathbf{u}_i = \ddot{\mathbf{X}}_i'\mathbf{r}_i$  and then  $\ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i = \ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i$ .]