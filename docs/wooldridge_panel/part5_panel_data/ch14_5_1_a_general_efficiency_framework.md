# A General Efficiency Framework

> Pages: 447-449

Most estimators in econometrics—and all of the ones we have studied—are  $\sqrt{N}$ -asymptotically normal, with variance matrices of the form

$$\mathbf{V} = \mathbf{A}^{-1} \mathbf{E}[\mathbf{s}(\mathbf{w})\mathbf{s}(\mathbf{w})'] (\mathbf{A}')^{-1}$$
(14.54)

where, in most cases, s(w) is the score of an objective function (evaluated at  $\theta_o$ ) and A is the expected value of the Jacobian of the score, again evaluated at  $\theta_o$ . (We suppress an "o" subscript here, as the value of the true parameter is irrelevant.) All M-estimators with twice continuously differentiable objective functions (and even some without) have variance matrices of this form, as do GMM estimators. The following lemma is a useful sufficient condition for showing that one estimator is more efficient than another.

LEMMA 14.1 (Relative Efficiency): Let  $\hat{\theta}_1$  and  $\hat{\theta}_2$  be two  $\sqrt{N}$ -asymptotically normal estimators of the  $P \times 1$  parameter vector  $\theta_0$ , with asymptotic variances of the form (14.54) (with appropriate subscripts on  $\mathbf{A}$ ,  $\mathbf{s}$ , and  $\mathbf{V}$ ). If for some  $\rho > 0$ ,

$$\mathbf{E}[\mathbf{s}_{1}(\mathbf{w})\mathbf{s}_{1}(\mathbf{w})'] = \rho \mathbf{A}_{1} \tag{14.55}$$

$$\mathbf{E}[\mathbf{s}_2(\mathbf{w})\mathbf{s}_1(\mathbf{w})'] = \rho \mathbf{A}_2 \tag{14.56}$$

then  $V_2 - V_1$  is positive semidefinite.

{448}------------------------------------------------

The proof of Lemma 14.1 is given in the chapter appendix.

Condition (14.55) is essentially the generalized information matrix equality (GIME) we introduced in Section 12.5.1 for the estimator  $\hat{\theta}_1$ . Notice that  $\mathbf{A}_1$  is necessarily symmetric and positive definite under condition (14.55). Condition (14.56) is new. In most cases, it says that the expected outer product of the scores  $\mathbf{s}_2$  and  $\mathbf{s}_1$  equals the expected Jacobian of  $\mathbf{s}_2$  (evaluated at  $\theta_0$ ). In Section 12.5.1 we claimed that the GIME plays a role in efficiency, and Lemma 14.1 shows that it does so.

Verifying the conditions of Lemma 14.1 is also very convenient for constructing simple forms of the Hausman (1978) statistic in a variety of contexts. Provided that the two estimators are jointly asymptotically normally distributed—something that is almost always true when each is  $\sqrt{N}$ -asymptotically normal, and that can be verified by stacking the first-order representations of the estimators—assumptions (14.55) and (14.56) imply that the asymptotic covariance between  $\sqrt{N}(\hat{\theta}_2 - \theta_0)$  and  $\sqrt{N}(\hat{\theta}_1 - \theta_0)$ is  $\mathbf{A}_2^{-1} \mathbf{E}(\mathbf{s}_2 \mathbf{s}_1') \mathbf{A}_1^{-1} = \mathbf{A}_2^{-1} (\rho \mathbf{A}_2) \mathbf{A}_1^{-1} = \rho \mathbf{A}_1^{-1} = \text{Avar}[\sqrt{N}(\hat{\boldsymbol{\theta}}_1 - \boldsymbol{\theta}_0)]$ . In other words, the asymptotic covariance between the  $(\sqrt{N}$ -scaled) estimators is equal to the asymptotic variance of the efficient estimator. This equality implies that  $\operatorname{Avar}[\sqrt{N}(\hat{\boldsymbol{\theta}}_2 - \hat{\boldsymbol{\theta}}_1)] =$  $\mathbf{V}_2 + \mathbf{V}_1 - \mathbf{C} - \mathbf{C}' = \mathbf{V}_2 + \mathbf{V}_1 - 2\mathbf{V}_1 = \mathbf{V}_2 - \mathbf{V}_1$ , where **C** is the asymptotic covariance. If  $V_2 - V_1$  is actually positive definite (rather than just positive semidefinite), then  $[\sqrt{N}(\hat{\boldsymbol{\theta}}_2 - \hat{\boldsymbol{\theta}}_1)]'(\hat{\mathbf{V}}_2 - \hat{\mathbf{V}}_1)^{-1}[\sqrt{N}(\hat{\boldsymbol{\theta}}_2 - \hat{\boldsymbol{\theta}}_1)] \stackrel{a}{\sim} \chi_P^2$  under the assumptions of Lemma 14.1, where  $\hat{\mathbf{V}}_q$  is a consistent estimator of  $\mathbf{V}_q$ , g=1,2. Statistically significant differences between  $\hat{\theta}_2$  and  $\hat{\theta}_1$  signal some sort of model misspecification. (See Section 6.2.1, where we discussed this form of the Hausman test for comparing 2SLS and OLS to test whether the explanatory variables are exogenous.) If assumptions (14.55) and (14.56) do not hold, this standard form of the Hausman statistic is invalid.

Given Lemma 14.1, we can state a condition that implies efficiency of an estimator in an entire *class* of estimators. It is useful to be somewhat formal in defining the relevant class of estimators. We do so by introducing an index,  $\tau$ . For each  $\tau$  in an index set, say,  $\mathcal{T}$ , the estimator  $\hat{\boldsymbol{\theta}}_{\tau}$  has an associated  $\mathbf{s}_{\tau}$  and  $\mathbf{A}_{\tau}$  such that the asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{\theta}}_{\tau}-\boldsymbol{\theta}_{o})$  has the form (14.54). The index can be very abstract; it simply serves to distinguish different  $\sqrt{N}$ -asymptotically normal estimators of  $\boldsymbol{\theta}_{o}$ . For example, in the class of M-estimators, the set  $\mathcal{T}$  consists of objective functions  $q(\cdot,\cdot)$  such that  $\boldsymbol{\theta}_{o}$  uniquely minimizes  $\mathrm{E}[q(\mathbf{w},\boldsymbol{\theta})]$  over  $\boldsymbol{\Theta}$ , and q satisfies the twice continuously differentiable and bounded moment assumptions imposed for asymptotic normality. For GMM with *given* moment conditions,  $\mathcal{T}$  is the set of all  $L \times L$  positive definite matrices. We will see another example in Section 14.5.3.

Lemma 14.1 immediately implies the following theorem.

THEOREM 14.3 (Efficiency in a Class of Estimators): Let  $\{\hat{\theta}_{\tau}: \tau \in \mathcal{T}\}$  be a class of  $\sqrt{N}$ -asymptotically normal estimators with variance matrices of the form (14.54). If

{449}------------------------------------------------

for some  $\tau^* \in \mathcal{T}$  and  $\rho > 0$ 

$$\mathbf{E}[\mathbf{s}_{\tau}(\mathbf{w})\mathbf{s}_{\tau^*}(\mathbf{w})'] = \rho \mathbf{A}_{\tau}, \quad \text{all } \tau \in \mathcal{T}$$
(14.57)

then  $\hat{\boldsymbol{\theta}}_{\tau^*}$  is asymptotically relatively efficient in the class  $\{\hat{\boldsymbol{\theta}}_{\tau}: \tau \in \mathscr{T}\}$ .

This theorem has many applications. If we specify a class of estimators by defining the index set  $\mathscr{T}$ , then the estimator  $\hat{\theta}_{\tau^*}$  is more efficient than all other estimators in the class if we can show condition (14.57). [A partial converse to Theorem 14.3 also holds; see Newey and McFadden (1994, Section 5.3).] This is not to say that  $\hat{\theta}_{\tau^*}$  is necessarily more efficient than *all* possible  $\sqrt{N}$ -asymptotically normal estimators. If there is an estimator that falls outside of the specified class, then Theorem 14.3 does not help us to compare it with  $\hat{\theta}_{\tau^*}$ . In this sense, Theorem 14.3 is a more general (and asymptotic) version of the Gauss-Markov theorem from linear regression analysis: while the Gauss-Markov theorem states that OLS has the smallest variance in the class of linear, unbiased estimators, it does not allow us to compare OLS to unbiased estimators that are not linear in the vector of observations on the dependent variable.