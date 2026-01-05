# Two-Step MLE

> Pages: 424-429

Consistency and asymptotic normality results are also available for **two-step maximum likelihood estimators** and **two-step partial maximum likelihood estimators**; we

{425}------------------------------------------------

focus on the former for concreteness. Let the conditional density be  $f(\cdot | \mathbf{x}_i; \boldsymbol{\theta}_o, \gamma_o)$ , where  $\gamma_o$  is an  $R \times 1$  vector of additional parameters. A preliminary estimator of  $\gamma_o$ , say  $\hat{\boldsymbol{\gamma}}$ , is plugged into the log-likelihood function, and  $\hat{\boldsymbol{\theta}}$  solves

$$\max_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \sum_{i=1}^{N} \log f(\mathbf{y}_i | \mathbf{x}_i; \boldsymbol{\theta}, \hat{\boldsymbol{\gamma}})$$

Consistency follow from results for two-step M-estimators. The practical limitation is that  $\log f(\mathbf{y}_i | \mathbf{x}_i; \boldsymbol{\theta}, \boldsymbol{\gamma})$  is continuous on  $\boldsymbol{\Theta} \times \boldsymbol{\Gamma}$  and that  $\boldsymbol{\theta}_0$  and  $\boldsymbol{\gamma}_0$  are identified.

Asymptotic normality of the two-step MLE follows directly from the results on two-step M-estimation in Chapter 12. As we saw there, in general the asymptotic variance of  $\sqrt{N}(\hat{\theta}-\theta_o)$  depends on the asymptotic variance of  $\sqrt{N}(\hat{\gamma}-\gamma_o)$  [see equation (12.41)], so we need to know the estimation problem solved by  $\hat{\gamma}$ . In some cases estimation of  $\gamma_o$  can be ignored. An important case is where the expected Hessian, defined with respect to  $\theta$  and  $\gamma$ , is block diagonal [the matrix  $F_o$  in equation (12.36) is zero in this case]. It can also hold for some values of  $\theta_o$ , which is important for testing certain hypotheses. We will encounter several examples in Part IV.

#### **Problems**

- **13.1.** If  $f(\mathbf{y} | \mathbf{x}; \boldsymbol{\theta})$  is a correctly specified model for the density of  $\mathbf{y}_i$  given  $\mathbf{x}_i$ , does  $\boldsymbol{\theta}_0$  solve  $\max_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} E[f(\mathbf{y}_i | \mathbf{x}_i; \boldsymbol{\theta})]$ ?
- **13.2.** Suppose that for a random sample,  $y_i | \mathbf{x}_i \sim \text{Normal}[m(\mathbf{x}_i, \boldsymbol{\beta}_0), \sigma_0^2]$ , where  $m(\mathbf{x}, \boldsymbol{\beta})$  is a function of the *K*-vector of explanatory variables  $\mathbf{x}$  and the  $P \times 1$  parameter vector  $\boldsymbol{\beta}$ . Recall that  $E(y_i | \mathbf{x}_i) = m(\mathbf{x}_i, \boldsymbol{\beta}_0)$  and  $Var(y_i | \mathbf{x}_i) = \sigma_0^2$ .
- a. Write down the conditional log-likelihood function for observation *i*. Show that the CMLE of  $\boldsymbol{\beta}_{\text{o}}$ ,  $\hat{\boldsymbol{\beta}}$ , solves the problem  $\min_{\boldsymbol{\beta}} \sum_{i=1}^{N} [y_i m(\mathbf{x}_i, \boldsymbol{\beta})]^2$ . In other words, the CMLE for  $\boldsymbol{\beta}_{\text{o}}$  is the nonlinear least squares estimator.
- b. Let  $\theta \equiv (\beta'\sigma^2)'$  denote the  $(P+1) \times 1$  vector of parameters. Find the score of the log likelihood for a generic *i*. Show directly that  $E[\mathbf{s}_i(\theta_0) \mid \mathbf{x}_i] = \mathbf{0}$ . What features of the normal distribution do you need in order to show that the conditional expectation of the score is zero?
- c. Use the first-order condition to find  $\hat{\sigma}^2$  in terms of  $\hat{\beta}$ .
- d. Find the Hessian of the log-likelihood function with respect to  $\theta$ .
- e. Show directly that  $-\mathbb{E}[\mathbf{H}_i(\boldsymbol{\theta}_o) | \mathbf{x}_i] = \mathbb{E}[\mathbf{s}_i(\boldsymbol{\theta}_o)\mathbf{s}_i(\boldsymbol{\theta}_o)' | \mathbf{x}_i].$

{426}------------------------------------------------

- f. Write down the estimated asymptotic variance of  $\hat{\beta}$ , and explain how to obtain the asymptotic standard errors.
- **13.3.** Consider a general binary response model  $P(y_i = 1 | \mathbf{x}_i) = G(\mathbf{x}_i, \theta_0)$ , where  $G(\mathbf{x}, \theta)$  is strictly between zero and one for all  $\mathbf{x}$  and  $\theta$ . Here,  $\mathbf{x}$  and  $\theta$  need not have the same dimension; let  $\mathbf{x}$  be a K-vector and  $\theta$  a P-vector.
- a. Write down the log likelihood for observation i.
- b. Find the score for each *i*. Show directly that  $E[\mathbf{s}_i(\theta_0) \mid \mathbf{x}_i] = \mathbf{0}$ .
- c. When  $G(\mathbf{x}, \boldsymbol{\theta}) = \Phi[\mathbf{x}\boldsymbol{\beta} + \delta_1(\mathbf{x}\boldsymbol{\beta})^2 + \delta_2(\mathbf{x}\boldsymbol{\beta})^3]$ , find the LM statistic for testing  $H_0$ :  $\delta_{o1} = 0, \delta_{o2} = 0$ .
- **13.4.** In the Newey-Tauchen-White specification-testing context, explain why we can take  $\mathbf{g}(\mathbf{w}, \boldsymbol{\theta}) = a(\mathbf{x}, \boldsymbol{\theta})\mathbf{s}(\mathbf{w}, \boldsymbol{\theta})$ , where  $a(\mathbf{x}, \boldsymbol{\theta})$  is essentially any scalar function of  $\mathbf{x}$  and  $\boldsymbol{\theta}$ .
- **13.5.** In the context of CMLE, consider a reparameterization of the kind in Section 12.6.2:  $\phi = \mathbf{g}(\theta)$ , where the Jacobian of  $\mathbf{g}$ ,  $\mathbf{G}(\theta)$ , is continuous and nonsingular for all  $\theta \in \mathbf{\Theta}$ . Let  $\mathbf{s}_i^g(\phi) = \mathbf{s}_i^g[\mathbf{g}(\theta)]$  denote the score of the log likelihood in the reparameterized model; thus, from Section 12.6.2,  $\mathbf{s}_i^g(\phi) = [\mathbf{G}(\theta)']^{-1}\mathbf{s}_i(\theta)$ .
- a. Using the conditional information matrix equality, find  $\mathbf{A}_{i}^{g}(\phi_{o}) \equiv \mathrm{E}[\mathbf{s}_{i}^{g}(\phi_{o})\mathbf{s}_{i}^{g}(\phi_{o})' \mid \mathbf{x}_{i}]$  in terms of  $\mathbf{G}(\theta_{o})$  and  $\mathbf{A}_{i}(\theta_{o}) \equiv \mathrm{E}[\mathbf{s}_{i}(\theta_{o})\mathbf{s}_{i}(\theta_{o})' \mid \mathbf{x}_{i}]$ .
- b. Show that  $\tilde{\mathbf{A}}_{i}^{g} = \tilde{\mathbf{G}}'^{-1}\tilde{\mathbf{A}}_{i}\tilde{\mathbf{G}}^{-1}$ , where these are all evaluated at the restricted estimate,  $\tilde{\boldsymbol{\theta}}$ .
- c. Use part b to show that the expected Hessian form of the LM statistic is invariant to reparameterization.
- **13.6.** Suppose that for a panel data set with T time periods,  $y_{it}$  given  $\mathbf{x}_{it}$  has a Poisson distribution with mean  $\exp(\mathbf{x}_{it}\boldsymbol{\theta}_0)$ , t = 1, ..., T.
- a. Do you have enough information to construct the joint distribution of  $\mathbf{y}_i$  given  $\mathbf{x}_i$ ? Explain.
- b. Write down the partial log likelihood for each *i* and find the score,  $s_i(\theta)$ .
- c. Show how to estimate Avar( $\hat{\boldsymbol{\theta}}$ ); it should be of the form (13.53).
- d. How does the estimator of  $Avar(\hat{\theta})$  simplify if the conditional mean is dynamically complete?
- **13.7.** Suppose that you have two parametric models for conditional densities:  $g(y_1 | y_2, \mathbf{x}; \boldsymbol{\theta})$  and  $h(y_2 | \mathbf{x}; \boldsymbol{\theta})$ ; not all elements of  $\boldsymbol{\theta}$  need to appear in both densities. Denote the true value of  $\boldsymbol{\theta}$  by  $\boldsymbol{\theta}_0$ .

{427}------------------------------------------------

a. What is the joint density of  $(y_1, y_2)$  given  $\mathbf{x}$ ? How would you estimate  $\theta_0$  given a random sample on  $(\mathbf{x}, y_1, y_2)$ ?

b. Suppose now that a random sample is not available on all variables. In particular,  $y_1$  is observed only when  $(\mathbf{x}, y_2)$  satisfies a known rule. For example, when  $y_2$  is binary,  $y_1$  is observed only when  $y_2 = 1$ . We assume  $(\mathbf{x}, y_2)$  is always observed. Let  $r_2$  be a binary variable equal to one if  $y_1$  is observed and zero otherwise. A partial MLE is obtained by defining

$$\ell_i(\boldsymbol{\theta}) = r_{i2} \log g(y_{i1} | y_{i2}, \mathbf{x}_i; \boldsymbol{\theta}) + \log h(y_{i2} | \mathbf{x}_i; \boldsymbol{\theta}) \equiv r_{i2} \ell_{i1}(\boldsymbol{\theta}) + \ell_{i2}(\boldsymbol{\theta})$$

for each *i*. This formulation ensures that first part of  $\ell_i$  only enters the estimation when  $y_{i1}$  is observed. Verify that  $\theta_0$  maximizes  $E[\ell_i(\theta)]$  over  $\Theta$ .

- c. Show that  $-E[\mathbf{H}_i(\boldsymbol{\theta}_o)] = E[\mathbf{s}_i(\boldsymbol{\theta}_o)\mathbf{s}_i(\boldsymbol{\theta}_o)']$ , even though the problem is not a true conditional MLE problem (and therefore a conditional information matrix equality does not hold).
- d. Argue that a consistent estimator of Avar  $\sqrt{N}(\hat{\theta} \theta_0)$  is

$$\left[N^{-1}\sum_{i=1}^{N}(r_{i2}\hat{\mathbf{A}}_{i1}+\hat{\mathbf{A}}_{i2})\right]^{-1}$$

where  $\mathbf{A}_{i1}(\boldsymbol{\theta}_{o}) = -\mathrm{E}[\nabla_{\theta}^{2}\ell_{i1}(\boldsymbol{\theta}_{o}) \mid y_{i2}, \mathbf{x}_{i}], \ \mathbf{A}_{i2}(\boldsymbol{\theta}_{o}) = -\mathrm{E}[\nabla_{\theta}^{2}\ell_{i2}(\boldsymbol{\theta}_{o}) \mid \mathbf{x}_{i}], \ \text{and} \ \hat{\boldsymbol{\theta}} \ \text{replaces}$   $\boldsymbol{\theta}_{o}$  in obtaining the estimates.

13.8. Consider a probit model with an unobserved explanatory variable v,

$$\mathbf{P}(y = 1 \mid \mathbf{x}, \mathbf{z}, v) = \Phi(\mathbf{x}\boldsymbol{\delta}_{o} + \rho_{o}v)$$

but where v depends on observable variables w and  $\mathbf{z}$  and a vector of parameters  $\gamma_0$ :  $v = w - \mathbf{z}\gamma_0$ . Assume that  $E(v | \mathbf{x}, \mathbf{z}) = \mathbf{0}$ ; this assumption implies, among other things, that  $\gamma_0$  can be consistently estimated by the OLS regression of  $w_i$  on  $\mathbf{z}_i$ , using a random sample. Define  $\hat{v}_i \equiv w_i - \mathbf{z}_i \hat{\boldsymbol{\gamma}}$ . Let  $\hat{\boldsymbol{\theta}} = (\hat{\boldsymbol{\delta}}', \hat{\boldsymbol{\rho}})'$  be the **two-step probit estimator** from probit of  $y_i$  on  $\mathbf{x}_i$ ,  $\hat{v}_i$ .

- a. Using the results from Section 12.5.2, show how to consistently estimate Avar  $\sqrt{N}(\hat{\theta} \theta_0)$ .
- b. Show that, when  $\rho_0 = 0$ , the usual probit asymptotic variance estimator is valid. That is, valid inference is obtained for  $(\delta'_0, \rho_0)'$  by ignoring the first-stage estimation.
- c. How would you test  $H_0$ :  $\rho_0 = 0$ ?
- **13.9.** Let  $\{y_t: t = 0, 1, ..., T\}$  be an observable time series representing a population, where we use the convention that t = 0 is the first time period for which y is

{428}------------------------------------------------

- observed. Assume that the sequence follows a *Markov process*:  $D(y_t | y_{t-1}, y_{t-2}, \dots y_0) = D(y_t | y_{t-1})$  for all  $t \ge 1$ . Let  $f_t(y_t | y_{t-1}; \theta)$  denote a correctly specified model for the density of  $y_t$  given  $y_{t-1}$ ,  $t \ge 1$ , where  $\theta_0$  is the true value of  $\theta$ .
- a. Show that, to obtain the joint distribution of  $(y_0, y_2, \dots, y_T)$ , you need to correctly model the density of  $y_0$ .
- b. Given a random sample of size N from the population, that is,  $(y_{i0}, y_{i1}, \dots, y_{iT})$  for each i, explain how to consistently etimate  $\theta_0$  without modeling  $D(y_0)$ .
- c. How would you estimate the asymptotic variance of the estimator from part b? Be specific.
- **13.10.** Let  $\mathbf{y}$  be a  $G \times 1$  random vector with elements  $y_g$ , g = 1, 2, ..., G. These could be different response variables for the same cross section unit or responses at different points in time. Let  $\mathbf{x}$  be a K-vector of observed conditioning variables, and let c be an unobserved conditioning variable. Let  $f_g(\cdot | \mathbf{x}, c)$  denote the density of  $y_g$  given  $(\mathbf{x}, c)$ . Further, assume that the  $y_1, y_2, ..., y_G$  are independent conditional on  $(\mathbf{x}, c)$ .
- a. Write down the joint density of y given  $(\mathbf{x}, c)$ .
- b. Let  $h(\cdot | \mathbf{x})$  be the density of c given  $\mathbf{x}$ . Find the joint density of  $\mathbf{y}$  given  $\mathbf{x}$ .
- c. If each  $f_g(\cdot | \mathbf{x}, c)$  is known up to a  $P_g$ -vector of parameters  $\mathbf{y}_o^g$  and  $h(\cdot | \mathbf{x})$  is known up to an M-vector  $\boldsymbol{\delta}_o$ , find the log likelihood for any random draw  $(\mathbf{x}_i, y_i)$  from the population.
- d. Is there a relationship between this setup and a linear SUR model?
- 13.11. Consider the dynamic, linear unobserved effects model

$$y_{it} = \rho y_{i,t-1} + c_i + e_{it}, \qquad t = 1, 2, \dots, T$$

$$E(e_{it} | y_{i,t-1}, y_{i,t-2}, \dots, y_{i0}, c_i) = 0$$

- In Section 11.1.1 we discussed estimation of  $\rho$  by instrumental variables methods after differencing. The deficiencies of the IV approach for large  $\rho$  may be overcome by applying the conditional MLE methods in Section 13.9.2.
- a. Make the stronger assumption that  $y_{it} | (y_{i,t-1}, y_{i,t-2}, \dots, y_{i0}, c_i)$  is normally distributed with mean  $\rho y_{i,t-1} + c_i$  and variance  $\sigma_e^2$ . Find the density of  $(y_{i1}, \dots, y_{iT})$  given  $(y_{i0}, c_i)$ . Is it a good idea to use the log of this density, summed across i, to estimate  $\rho$  and  $\sigma_e^2$  along with the "fixed effects"  $c_i$ ?
- b. If  $c_i | y_{i0} \sim \text{Normal}(\alpha_0 + \alpha_1 y_{i0}, \sigma_a^2)$ , where  $\sigma_a^2 \equiv \text{Var}(a_i)$  and  $a_i \equiv c_i \alpha_0 \alpha_1 y_{i0}$ , write down the density of  $(y_{i1}, \dots, y_{iT})$  given  $y_{i0}$ . How would you estimate  $\rho$ ,  $\alpha_0$ ,  $\alpha_1$ ,  $\sigma_e^2$ , and  $\sigma_a^2$ ?

{429}------------------------------------------------

c. Under the same assumptions in parts a and b, extend the model to  $y_{it} = \rho y_{i,t-1} + c_i + \delta c_i y_{i,t-1} + e_{it}$ . Explain how to estimate the parameters of this model, and propose a consistent estimator of the average partial effect of the lag,  $\rho + \delta E(c_i)$ .

d. Now extend part b to the case where  $\mathbf{z}_{it}\boldsymbol{\beta}$  is added to the conditional mean function, where the  $\mathbf{z}_{it}$  are strictly exogenous conditional on  $c_i$ . Assume that  $c_i \mid y_{i0}, \mathbf{z}_i \sim \text{Normal}(\alpha_0 + \alpha_1 y_{i0} + \overline{\mathbf{z}}_i \boldsymbol{\delta}, \sigma_a^2)$ , where  $\overline{\mathbf{z}}_i$  is the vector of time averages.