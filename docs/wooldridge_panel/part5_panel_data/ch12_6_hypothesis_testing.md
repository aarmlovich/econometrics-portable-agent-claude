# Hypothesis Testing

> Pages: 373-374

#### **12.6.1 Wald Tests**

Wald tests are easily obtained once we choose a form of the asymptotic variance. To test the Q restrictions

$$H_0: \mathbf{c}(\boldsymbol{\theta}_0) = \mathbf{0} \tag{12.62}$$

we can form the Wald statistic

$$W \equiv \mathbf{c}(\hat{\boldsymbol{\theta}})'(\hat{\mathbf{C}}\hat{\mathbf{V}}\hat{\mathbf{C}}')^{-1}\mathbf{c}(\hat{\boldsymbol{\theta}})$$
(12.63)

where  $\hat{\mathbf{V}}$  is an asymptotic variance matrix estimator of  $\hat{\boldsymbol{\theta}}$ ,  $\hat{\mathbf{C}} \equiv \mathbf{C}(\hat{\boldsymbol{\theta}})$ , and  $\mathbf{C}(\boldsymbol{\theta})$  is the  $Q \times P$  Jacobian of  $\mathbf{c}(\boldsymbol{\theta})$ . The estimator  $\hat{\mathbf{V}}$  can be chosen to be fully robust, as in expression (12.48) or (12.49); under assumption (12.53), the simpler forms in Lemma 12.2 are available. Also,  $\hat{\mathbf{V}}$  can be chosen to account for two-step estimation, when necessary. Provided  $\hat{\mathbf{V}}$  has been chosen appropriately,  $W \stackrel{a}{\sim} \chi_Q^2$  under  $\mathbf{H}_0$ .

A couple of practical restrictions are needed for W to have a limiting  $\chi_Q^2$  distribution. First,  $\theta_0$  must be in the interior of  $\Theta$ ; that is,  $\theta_0$  cannot be on the boundary. If, for example, the first element of  $\theta$  must be nonnegative—and we impose this restriction in the estimation—then expression (12.63) does not have a limiting chi-square distribution under  $H_0$ :  $\theta_{01} = 0$ . The second condition is that  $\mathbf{C}(\theta_0) = \nabla_{\theta} \mathbf{c}(\theta_0)$  must have rank Q. This rules out cases where  $\theta_0$  is unidentified under the null hypothesis, such as the NLS example where  $m(\mathbf{x}, \theta) = \theta_1 + \theta_2 x_2 + \theta_3 x_3^{\theta_4}$  and  $\theta_{03} = 0$  under  $H_0$ .

One drawback to the Wald statistic is that it is not invariant to how the nonlinear restrictions are imposed. We can change the outcome of a hypothesis test by redefining the constraint function,  $\mathbf{c}(\cdot)$ . We can illustrate the lack of invariance by studying an asymptotic t statistic (since a t statistic is a special case of a Wald statistic). Suppose that for a parameter  $\theta_1 > 0$ , the null hypothesis is  $H_0$ :  $\theta_{01} = 1$ . The asymptotic t statistic is  $(\hat{\theta}_1 - 1)/\sec(\hat{\theta}_1)$ , where  $\sec(\hat{\theta}_1)$  is the asymptotic standard error of  $\hat{\theta}_1$ . Now define  $\phi_1 = \log(\theta_1)$ , so that  $\phi_{01} = \log(\theta_{01})$  and  $\hat{\phi}_1 = \log(\hat{\theta}_1)$ . The null hypothesis can be stated as  $H_0$ :  $\phi_{01} = 0$ . Using the delta method (see Chapter 3),  $\sec(\hat{\phi}_1) = \cos(\hat{\phi}_1)$ 

{374}------------------------------------------------

 $\hat{\theta}_1^{-1} \operatorname{se}(\hat{\theta}_1)$ , and so the t statistic based on  $\hat{\phi}_1$  is  $\hat{\phi}_1/\operatorname{se}(\hat{\phi}_1) = \log(\hat{\theta}_1)\hat{\theta}_1/\operatorname{se}(\hat{\theta}_1) \neq (\hat{\theta}_1 - 1)/\operatorname{se}(\hat{\theta}_1)$ .

The lack of invariance of the Wald statistic is discussed in more detail by Gregory and Veall (1985), Phillips and Park (1988), and Davidson and MacKinnon (1993, Section 13.6). The lack of invariance is a cause for concern because it suggests that the Wald statistic can have poor finite sample properties for testing nonlinear hypotheses. What is much less clear is that the lack of invariance has led empirical researchers to search over different statements of the null hypothesis in order to obtain a desired result.