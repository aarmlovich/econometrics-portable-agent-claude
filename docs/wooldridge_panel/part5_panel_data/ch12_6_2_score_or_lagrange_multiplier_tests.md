# Score (or Lagrange Multiplier) Tests

> Pages: 374-379

In cases where the unrestricted model is difficult to estimate but the restricted model is relatively simple to estimate, it is convenient to have a statistic that only requires estimation under the null. Such a statistic is Rao's (1948) **score statistic**, also called the **Lagrange multiplier statistic** in econometrics, based on the work of Aitchison and Silvey (1958). We will focus on Rao's original motivation for the statistic because it leads more directly to test statistics that are used in econometrics. An important point is that, even though Rao, Aitchison and Silvey, Engle (1984), and many others focused on the maximum likelihood setup, the score principle is applicable to any problem where the estimators solve a first-order condition, including the general class of Mestimators.

The score approach is ideally suited for **specification testing**. Typically, the first step in specification testing is to begin with a popular model—one that is relatively easy to estimate and interpret—and nest it within a more complicated model. Then the popular model is tested against the more general alternative to determine if the original model is misspecified. We do not want to estimate the more complicated model unless there is significant evidence against the restricted form of the model. In stating the null and alternative hypotheses, there is no difference between specification testing and classical tests of parameter restrictions. However, in practice, specification testing gives primary importance to the restricted model, and we may have no intention of actually estimating the general model even if the null model is rejected.

We will derive the score test only in the case where no correction is needed for preliminary estimation of nuisance parameters: either there are no such parameters present, or assumption (12.37) holds under  $H_0$ . If nuisance parameters are present, we do not explicitly show the score and Hessian depending on  $\hat{\gamma}$ .

We again assume that there are Q continuously differentiable restrictions imposed on  $\theta_0$  under  $H_0$ , as in expression (12.62). However, we must also assume that the

{375}------------------------------------------------

restrictions define a mapping from  $\mathbb{R}^{P-Q}$  to  $\mathbb{R}^P$ , say,  $\mathbf{d}$ :  $\mathbb{R}^{P-Q} \to \mathbb{R}^P$ . In particular, under the null hypothesis, we can write  $\boldsymbol{\theta}_0 = \mathbf{d}(\lambda_0)$ , where  $\lambda_0$  is a  $(P-Q) \times 1$  vector. We must assume that  $\lambda_0$  is in the interior of its parameter space,  $\boldsymbol{\Lambda}$ , under  $H_0$ . We also assume that  $\mathbf{d}$  is twice continuously differentiable on the interior of  $\boldsymbol{\Lambda}$ .

Let  $\tilde{\lambda}$  be the solution to the constrained minimization problem

$$\min_{\lambda \in \Lambda} \sum_{i=1}^{N} q[\mathbf{w}_i, \mathbf{d}(\lambda)] \tag{12.64}$$

The constrained estimator of  $\theta_0$  is simply  $\tilde{\theta} \equiv \mathbf{d}(\tilde{\lambda})$ . In practice, we do not have to explicitly find the function  $\mathbf{d}$ ; solving problem (12.64) is easily done just by directly imposing the restrictions, especially when the restrictions set certain parameters to hypothesized values (such as zero). Then, we just minimize the resulting objective function over the free parameters.

As an example, consider the nonlinear regression model

$$m(\mathbf{x}, \boldsymbol{\theta}) = \exp[\mathbf{x}\boldsymbol{\beta} + \delta_1(\mathbf{x}\boldsymbol{\beta})^2 + \delta_2(\mathbf{x}\boldsymbol{\beta})^3]$$

where  $\mathbf{x}$  is  $1 \times K$  and contains unity as its first element. The null hypthosis is  $H_0$ :  $\delta_1 = \delta_2 = 0$ , so that the model with the restrictions imposed is just an exponential regression function,  $m(\mathbf{x}, \boldsymbol{\beta}) = \exp(\mathbf{x}\boldsymbol{\beta})$ .

The simplest method for deriving the LM test is to use Rao's score principle extended to the M-estimator case. The LM statistic is based on the limiting distribution of

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_i(\tilde{\boldsymbol{\theta}}) \tag{12.65}$$

under  $H_0$ . This is the score with respect to the entire vector  $\boldsymbol{\theta}$ , but we are evaluating it at the restricted estimates. If  $\tilde{\boldsymbol{\theta}}$  were replaced by  $\hat{\boldsymbol{\theta}}$ , then expression (12.65) would be identically zero, which would make it useless as a test statistic. If the restrictions imposed by the null hypothesis are true, then expression (12.65) will not be statistically different from zero.

Assume initially that  $\theta_o$  is in the interior of  $\Theta$  under  $H_0$ ; we will discuss how to relax this assumption later. Now  $\sqrt{N}(\tilde{\boldsymbol{\theta}}-\boldsymbol{\theta}_o)=O_p(1)$  by the delta method because  $\sqrt{N}(\tilde{\boldsymbol{\lambda}}-\boldsymbol{\lambda}_o)=O_p(1)$  under the given assumptions. A standard mean value expansion yields

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\tilde{\boldsymbol{\theta}}) = N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\boldsymbol{\theta}_{o}) + \mathbf{A}_{o} \sqrt{N}(\tilde{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) + o_{p}(1)$$
(12.66)

{376}------------------------------------------------

under  $H_0$ , where  $\mathbf{A}_o$  is given in expression (12.19). But  $\mathbf{0} = \sqrt{N}\mathbf{c}(\tilde{\boldsymbol{\theta}}) = \sqrt{N}\mathbf{c}(\boldsymbol{\theta}_o) + \ddot{\mathbf{C}}\sqrt{N}(\tilde{\boldsymbol{\theta}} - \boldsymbol{\theta}_o)$ , where  $\ddot{\mathbf{C}}$  is the  $Q \times P$  Jacobian matrix  $\mathbf{C}(\boldsymbol{\theta})$  with rows evaluated at mean values between  $\tilde{\boldsymbol{\theta}}$  and  $\boldsymbol{\theta}_o$ . Under  $H_0$ ,  $\mathbf{c}(\boldsymbol{\theta}_o) = \mathbf{0}$ , and plim  $\ddot{\mathbf{C}} = \mathbf{C}(\boldsymbol{\theta}_o) \equiv \mathbf{C}_o$ . Therefore, under  $H_0$ ,  $\mathbf{C}_o\sqrt{N}(\tilde{\boldsymbol{\theta}} - \boldsymbol{\theta}_o) = o_p(1)$ , and so multiplying equation (12.66) through by  $\mathbf{C}_o\mathbf{A}_o^{-1}$  gives

$$\mathbf{C}_{o}\mathbf{A}_{o}^{-1}N^{-1/2}\sum_{i=1}^{N}\mathbf{s}_{i}(\tilde{\boldsymbol{\theta}}) = \mathbf{C}_{o}\mathbf{A}_{o}^{-1}N^{-1/2}\sum_{i=1}^{N}\mathbf{s}_{i}(\boldsymbol{\theta}_{o}) + o_{p}(1)$$
(12.67)

By the CLT,  $\mathbf{C}_{o}\mathbf{A}_{o}^{-1}N^{-1/2}\sum_{i=1}^{N}\mathbf{s}_{i}(\boldsymbol{\theta}_{o}) \xrightarrow{d} \mathrm{Normal}(\mathbf{0},\mathbf{C}_{o}\mathbf{A}_{o}^{-1}\mathbf{B}_{o}\mathbf{A}_{o}^{-1}\mathbf{C}_{o}')$ , where  $\mathbf{B}_{o}$  is defined in expression (12.20). Under our assumptions,  $\mathbf{C}_{o}\mathbf{A}_{o}^{-1}\mathbf{B}_{o}\mathbf{A}_{o}^{-1}\mathbf{C}_{o}'$  has full rank Q, and so

$$\left[N^{-1/2}\sum_{i=1}^{N}\mathbf{s}_{i}(\tilde{\boldsymbol{\theta}})\right]'\mathbf{A}_{o}^{-1}\mathbf{C}_{o}'[\mathbf{C}_{o}\mathbf{A}_{o}^{-1}\mathbf{B}_{o}\mathbf{A}_{o}^{-1}\mathbf{C}_{o}']^{-1}\mathbf{C}_{o}\mathbf{A}_{o}^{-1}\left[N^{-1/2}\sum_{i=1}^{N}\mathbf{s}_{i}(\tilde{\boldsymbol{\theta}})\right]\overset{d}{\rightarrow}\chi_{Q}^{2}$$

The score or LM statistic is given by

$$LM = \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right)' \tilde{\mathbf{A}}^{-1} \tilde{\mathbf{C}}' (\tilde{\mathbf{C}} \tilde{\mathbf{A}}^{-1} \tilde{\mathbf{B}} \tilde{\mathbf{A}}^{-1} \tilde{\mathbf{C}}')^{-1} \tilde{\mathbf{C}} \tilde{\mathbf{A}}^{-1} \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right) / N$$
(12.68)

where all quantities are evaluated at  $\tilde{\boldsymbol{\theta}}$ . For example,  $\tilde{\mathbf{C}} \equiv \mathbf{C}(\tilde{\boldsymbol{\theta}})$ ,  $\tilde{\mathbf{B}}$  is given in expression (12.45) but with  $\tilde{\boldsymbol{\theta}}$  in place of  $\hat{\boldsymbol{\theta}}$ , and  $\tilde{\mathbf{A}}$  is one of the estimators in expression (12.42) or (12.44), again evaluated at  $\tilde{\boldsymbol{\theta}}$ . Under  $H_0$ ,  $LM \stackrel{d}{\to} \chi_O^2$ .

For the Wald statistic we assumed that  $\theta_o \in \text{int}(\Theta)$  under  $H_0$ ; this assumption is crucial for the statistic to have a limiting chi-square distribution. We will not consider the Wald statistic when  $\theta_o$  is on the boundary of  $\Theta$  under  $H_0$ ; see Wolak (1991) for some results. The general derivation of the LM statistic also assumed that  $\theta_o \in \text{int}(\Theta)$  under  $H_0$ . Nevertheless, for certain applications of the LM test we can drop the requirement that  $\theta_o$  is in the interior of  $\Theta$  under  $H_0$ . A leading case occurs when  $\theta$  can be partitioned as  $\theta \equiv (\theta'_1, \theta'_2)'$ , where  $\theta_1$  is  $(P - Q) \times 1$  and  $\theta_2$  is  $Q \times 1$ . The null hypothesis is  $H_0$ :  $\theta_{o2} = 0$ , so that  $\mathbf{c}(\theta) \equiv \theta_2$ . It is easy to see that the mean value expansion used to derive the LM statistic is valid provided  $\lambda_o \equiv \theta_{o1}$  is in the interior of its parameter space under  $H_0$ ;  $\theta_o \equiv (\theta'_{o1}, \mathbf{0})'$  can be on the boundary of  $\Theta$ . This observation is useful especially when testing hypotheses about parameters that must be either nonnegative or nonpositive.

If we assume the generalized information matrix equality (12.53) with  $\sigma_o^2 = 1$ , the LM statistic simplifies. The simplification results from the following reasoning: (1)  $\tilde{\mathbf{C}}\tilde{\mathbf{D}} = \mathbf{0}$  by the chain rule, where  $\tilde{\mathbf{D}} \equiv \nabla_{\lambda} \mathbf{d}(\tilde{\lambda})$ , since  $\mathbf{c}[\mathbf{d}(\lambda)] \equiv \mathbf{0}$  for  $\lambda$  in  $\Lambda$ . (2) If  $\mathbf{E}$  is

{377}------------------------------------------------

a  $P \times Q$  matrix  $\mathbf{E}$  with rank Q,  $\mathbf{F}$  is a  $P \times (P - Q)$  matrix with rank P - Q, and  $\mathbf{E}'\mathbf{F} = \mathbf{0}$ , then  $\mathbf{E}(\mathbf{E}'\mathbf{E})^{-1}\mathbf{E}' = \mathbf{I}_{P} - \mathbf{F}(\mathbf{F}'\mathbf{F})^{-1}\mathbf{F}'$ . (This is simply a statement about projections onto orthogonal subspaces.) Choosing  $\mathbf{E} \equiv \tilde{\mathbf{A}}^{-1/2}\tilde{\mathbf{C}}'$  and  $\mathbf{F} \equiv \tilde{\mathbf{A}}^{1/2}\tilde{\mathbf{D}}$  gives  $\tilde{\mathbf{A}}^{-1/2}\tilde{\mathbf{C}}'(\tilde{\mathbf{C}}\tilde{\mathbf{A}}^{-1}\tilde{\mathbf{C}}')^{-1}\tilde{\mathbf{C}}\tilde{\mathbf{A}}^{-1/2} = \mathbf{I}_{P} - \tilde{\mathbf{A}}^{1/2}\tilde{\mathbf{D}}(\tilde{\mathbf{D}}'\tilde{\mathbf{A}}\tilde{\mathbf{D}})^{-1}\tilde{\mathbf{D}}'\tilde{\mathbf{A}}^{1/2}$ . Now, pre- and post-multiply this equality by  $\tilde{\mathbf{A}}^{-1/2}$  to get  $\tilde{\mathbf{A}}^{-1}\tilde{\mathbf{C}}'(\tilde{\mathbf{C}}\tilde{\mathbf{A}}^{-1}\tilde{\mathbf{C}}')^{-1}\tilde{\mathbf{C}}\tilde{\mathbf{A}}^{-1} = \tilde{\mathbf{A}}^{-1} - \tilde{\mathbf{D}}(\tilde{\mathbf{D}}'\tilde{\mathbf{A}}\tilde{\mathbf{D}})^{-1}\tilde{\mathbf{D}}'$ . (3) Plug  $\tilde{\mathbf{B}} = \tilde{\mathbf{A}}$  into expression (12.68) and use step 2, along with the first-order condition  $\tilde{\mathbf{D}}'(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}) = \mathbf{0}$ , to get

$$LM = \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right)' \tilde{\mathbf{M}}^{-1} \left(\sum_{i=1}^{N} \tilde{\mathbf{s}}_{i}\right)$$
(12.69)

where  $\tilde{\mathbf{M}}$  can be chosen as  $\sum_{i=1}^{N} \tilde{\mathbf{A}}_i$ ,  $\sum_{i=1}^{N} \tilde{\mathbf{H}}_i$ , or  $\sum_{i=1}^{N} \tilde{\mathbf{s}}_i \tilde{\mathbf{s}}_i'$ . (Each of these expressions consistently estimates  $\mathbf{A}_0 = \mathbf{B}_0$  when divided by N.) The last choice of  $\tilde{\mathbf{M}}$  results in a statistic that is N times the uncentered R-squared, say  $R_0^2$ , from the regression

1 on 
$$\tilde{\mathbf{s}}'_i$$
,  $i = 1, 2, \dots, N$  (12.70)

(Recall that  $\tilde{\mathbf{s}}_i'$  is a  $1 \times P$  vector.) Because the dependent variable in regression (12.70) is unity,  $NR_0^2$  is equivalent to  $N-\mathrm{SSR}_0$ , where  $\mathrm{SSR}_0$  is the sum of squared residuals from regression (12.70). This is often called the **outer product of the score LM statistic** because of the estimator it uses for  $\mathbf{A}_0$ . While this statistic is simple to compute, there is ample evidence that it can have severe size distortions (typically, the null hypothesis is rejected much more often than the nominal size of the test). See, for example, Davidson and MacKinnon (1993), Bera and McKenzie (1986), Orme (1990), and Chesher and Spady (1991).

The Hessian form of the LM statistic uses  $\tilde{\mathbf{M}} = \sum_{i=1}^{N} \tilde{\mathbf{H}}_i$ , and it has a few drawbacks: (1) the LM statistic can be negative if the average estimated Hessian is not positive definite; (2) it requires computation of the second derivatives; and (3) it is not invariant to reparameterizations. We will discuss the last problem later.

A statistic that always avoids the first problem, and often the second and third problems, is based on  $E[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_o) \,|\, \mathbf{x}]$ , assuming that  $\mathbf{w}$  partitions into endogenous variables  $\mathbf{y}$  and exogenous variables  $\mathbf{x}$ . We call the LM statistic that uses  $\tilde{\mathbf{M}} = \sum_{i=1}^{N} \tilde{\mathbf{A}}_i$  the **expected Hessian form of the LM statistic**. This name comes from the fact that the statistic is based on the *conditional* expectation of  $\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_o)$  given  $\mathbf{x}$ . When it can be computed, the expected Hessian form is usually preferred because it tends to have the best small sample properties.

The LM statistic in equation (12.69) is valid only when  $\mathbf{B}_o = \mathbf{A}_o$ , and therefore it is not robust to failures of auxiliary assumptions in some important models. If  $\mathbf{B}_o \neq \mathbf{A}_o$ , the limiting distribution of equation (12.69) is not chi-square and is not suitable for testing.

{378}------------------------------------------------

In the context of NLS, the expected Hessian form of the LM statistic needs to be modified for the presence of  $\sigma_o^2$ , assuming that Assumption NLS.3 holds under  $H_0$ . Let  $\tilde{\sigma}^2 \equiv N^{-1} \sum_{i=1}^N \tilde{u}_i^2$  be the estimate of  $\sigma_o^2$  using the restricted estimator of  $\theta_o$ :  $\tilde{u}_i \equiv y_i - m(\mathbf{x}_i, \tilde{\boldsymbol{\theta}})$ , i = 1, 2, ..., N. It is customary not to make a degrees-of-freedom adjustment when estimating the variance using the null estimates, partly because the sum of squared residuals for the restricted model is always larger than for the unrestricted model. The score evaluated at the restricted estimates can be written as  $\tilde{\mathbf{s}}_i = \nabla_{\theta} \tilde{m}_i' \tilde{u}_i$ . Thus the LM statistic that imposes homoskedasticity is

$$LM = \left(\sum_{i=1}^{N} \nabla_{\theta} \tilde{\boldsymbol{m}}_{i}' \tilde{\boldsymbol{u}}_{i}\right)' \left(\sum_{i=1}^{N} \nabla_{\theta} \tilde{\boldsymbol{m}}_{i}' \nabla_{\theta} \tilde{\boldsymbol{m}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \nabla_{\theta} \tilde{\boldsymbol{m}}_{i}' \tilde{\boldsymbol{u}}_{i}\right) / \tilde{\boldsymbol{\sigma}}^{2}$$
(12.71)

A little algebra shows that this expression is identical to N times the uncentered R-squared,  $R_u^2$ , from the auxiliary regression

$$\tilde{u}_i \text{ on } \nabla_{\theta} \tilde{m}_i, \qquad i = 1, 2, \dots, N$$
 (12.72)

In other words, just regress the residuals from the restricted model on the gradient with respect to the *unrestricted* mean function but evaluated at the *restricted* estimates. Under H<sub>0</sub> and Assumption NLS.3,  $LM = NR_u^2 \stackrel{a}{\sim} \chi_O^2$ .

In the nonlinear regression example with  $m(\mathbf{x}, \boldsymbol{\theta}) = \exp[\mathbf{x}\boldsymbol{\beta} + \delta_1(\mathbf{x}\boldsymbol{\beta})^2 + \delta_2(\mathbf{x}\boldsymbol{\beta})^3]$ , let  $\tilde{\boldsymbol{\beta}}$  be the restricted NLS estimator with  $\delta_1 = 0$  and  $\delta_2 = 0$ ; in other words,  $\tilde{\boldsymbol{\beta}}$  is from a nonlinear regression with an exponential regression function. The restricted residuals are  $\tilde{\boldsymbol{u}}_i = y_i - \exp(\mathbf{x}_i\tilde{\boldsymbol{\beta}})$ , and the gradient of  $m(\mathbf{x}, \boldsymbol{\theta})$  with respect to all parameters, evaluated at the null, is

$$\nabla_{\theta} m(\mathbf{x}_i, \boldsymbol{\beta}_{o}, \mathbf{0}) = \{\mathbf{x}_i \exp(\mathbf{x}_i \boldsymbol{\beta}_{o}), (\mathbf{x}_i \boldsymbol{\beta}_{o})^2 \exp(\mathbf{x}_i \boldsymbol{\beta}_{o}), (\mathbf{x}_i \boldsymbol{\beta}_{o})^3 \exp(\mathbf{x}_i \boldsymbol{\beta}_{o})\}$$

Plugging in  $\tilde{\boldsymbol{\beta}}$  gives  $\nabla_{\theta}\tilde{\boldsymbol{m}}_{i} = [\mathbf{x}_{i}\tilde{\boldsymbol{m}}_{i}, (\mathbf{x}_{i}\tilde{\boldsymbol{\beta}})^{2}\tilde{\boldsymbol{m}}_{i}, (\mathbf{x}_{i}\tilde{\boldsymbol{\beta}})^{3}\tilde{\boldsymbol{m}}_{i}]$ , where  $\tilde{\boldsymbol{m}}_{i} \equiv \exp(\mathbf{x}_{i}\tilde{\boldsymbol{\beta}})$ . Regression (12.72) becomes

$$\tilde{\mathbf{u}}_i \text{ on } \mathbf{x}_i \tilde{\mathbf{m}}_i, \ (\mathbf{x}_i \tilde{\mathbf{\beta}})^2 \tilde{\mathbf{m}}_i, \ (\mathbf{x}_i \tilde{\mathbf{\beta}})^3 \tilde{\mathbf{m}}_i, \qquad i = 1, 2, \dots, N$$
 (12.73)

Under H<sub>0</sub> and homoskedasticity,  $NR_u^2 \sim \chi_2^2$ , since there are two restrictions being tested. This is a fairly simple way to test the exponential functional form without ever estimating the more complicated alternative model. Other models that nest the exponential model are discussed in Wooldridge (1992).

This example illustrates an important point: even though  $\sum_{i=1}^{N} (\mathbf{x}_i \tilde{m}_i)' \tilde{u}_i$  is identically zero by the first-order condition for NLS, the term  $\mathbf{x}_i \tilde{m}_i$  must generally be included in regression (12.73). The *R*-squared from the regression without  $\mathbf{x}_i \tilde{m}_i$  will be different because the remaining regressors in regression (12.73) are usually correlated with  $\mathbf{x}_i \tilde{m}_i$  in the sample. [More importantly, for h = 2 and 3,  $(\mathbf{x}_i \boldsymbol{\beta})^h \exp(\mathbf{x}_i \boldsymbol{\beta})$  is

{379}------------------------------------------------

probably correlated with  $\mathbf{x}_i \boldsymbol{\beta}$  in the population.] As a general rule, the entire gradient  $\nabla_{\theta} \tilde{m}_i$  must appear in the auxiliary regression.

In order to be robust against failure of Assumption NLS.3, the more general form of the statistic in expression (12.68) should be used. Fortunately, this statistic also can be easily computed for most hypotheses. Partition  $\theta$  into the  $(P-Q) \times 1$  vector  $\beta$  and the Q vector  $\delta$ . Assume that the null hypothesis is  $H_0$ :  $\delta_0 = \bar{\delta}$ , where  $\bar{\delta}$  is a prespecified vector (often containing all zeros, but not always). Let  $\nabla_{\beta}\tilde{m}_i$   $[1 \times (P-Q)]$  and  $\nabla_{\delta}\tilde{m}_i$   $(1 \times Q)$  denote the gradients with respect to  $\beta$  and  $\delta$ , respectively, evaluated at  $\hat{\beta}$  and  $\bar{\delta}$ . After tedious algebra, and using the special structure  $\mathbf{C}(\theta) = [\mathbf{0} \mid \mathbf{I}_Q]$ , where  $\mathbf{0}$  is a  $Q \times (P-Q)$  matrix of zero, the following procedure can be shown to produce expression (12.68):