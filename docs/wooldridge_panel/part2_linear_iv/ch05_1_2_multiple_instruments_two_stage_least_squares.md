# Multiple Instruments: Two-Stage Least Squares

> Pages: 105-107

Consider again the model (5.1) and (5.2), where xK can be correlated with u. Now, however, assume that we have more than one instrumental variable for xK . Let z1, z2; ... ; zM be variables such that

$$Cov(z_h, u) = 0, h = 1, 2, ..., M$$
 (5.13)

so that each zh is exogenous in equation (5.1). If each of these has some partial correlation with xK , we could have M different IV estimators. Actually, there are many more than this—more than we can count—since any linear combination of x1, x2; ... ; xK-1, z1, z2; ... ; zM is uncorrelated with u. So which IV estimator should we use?

In Section 5.2.3 we show that, under certain assumptions, the two-stage least squares (2SLS) estimator is the most efficient IV estimator. For now, we rely on intuition.

To illustrate the method of 2SLS, define the vector of exogenous variables again by z1ð1; x1; x2; ... ; xK-<sup>1</sup>; z1; ... ; zMÞ,a1 L vector ðL ¼ K þ MÞ. Out of all possible linear combinations of z that can be used as an instrument for xK , the method of 2SLS chooses that which is most highly correlated with xK . If xK were exogenous, then this choice would imply that the best instrument for xK is simply itself. Ruling this case out, the linear combination of z most highly correlated with xK is given by the linear projection of xK on z. Write the reduced form for xK as

$$x_K = \delta_0 + \delta_1 x_1 + \dots + \delta_{K-1} x_{K-1} + \theta_1 z_1 + \dots + \theta_M z_M + r_K$$
(5.14)

where, by definition, rK has zero mean and is uncorrelated with each right-hand-side variable. As any linear combination of z is uncorrelated with u,

$$x_K^* \equiv \delta_0 + \delta_1 x_1 + \dots + \delta_{K-1} x_{K-1} + \theta_1 z_1 + \dots + \theta_M z_M$$
 (5.15)

is uncorrelated with u. In fact, x <sup>K</sup> is often interpreted as the part of xK that is uncorrelated with u. If xK is endogenous, it is because rK is correlated with u.

If we could observe x <sup>K</sup> , we would use it as an instrument for xK in equation (5.1) and use the IV estimator from the previous subsection. Since the d<sup>j</sup> and y<sup>j</sup> are population parameters, x <sup>K</sup> is not a usable instrument. However, as long as we make the standard assumption that there are no exact linear dependencies among the exogenous variables, we can consistently estimate the parameters in equation (5.14) by OLS. The sample analogues of the x iK for each observation i are simply the OLS fitted values:

$$\hat{x}_{iK} = \hat{\delta}_0 + \hat{\delta}_1 x_{i1} + \dots + \hat{\delta}_{K-1} x_{i,K-1} + \hat{\theta}_1 z_{i1} + \dots + \hat{\theta}_M z_{iM}$$
(5.16)

{106}------------------------------------------------

Now, for each observation i, define the vector  $\hat{\mathbf{x}}_i \equiv (1, x_{i1}, \dots, x_{i,K-1}, \hat{\mathbf{x}}_{iK}), i = 1, 2, \dots, N$ . Using  $\hat{\mathbf{x}}_i$  as the instruments for  $\mathbf{x}_i$  gives the IV estimator

$$\hat{\boldsymbol{\beta}} = \left(\sum_{i=1}^{N} \hat{\mathbf{x}}_{i}' \mathbf{x}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \hat{\mathbf{x}}_{i}' y_{i}\right) = (\hat{\mathbf{X}}' \mathbf{X})^{-1} \hat{\mathbf{X}}' \mathbf{Y}$$
(5.17)

where unity is also the first element of  $\mathbf{x}_i$ .

The IV estimator in equation (5.17) turns out to be an OLS estimator. To see this fact, note that the  $N \times (K+1)$  matrix  $\hat{\mathbf{X}}$  can be expressed as  $\hat{\mathbf{X}} = \mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{X} = \mathbf{P}_Z\mathbf{X}$ , where the projection matrix  $\mathbf{P}_Z = \mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'$  is idempotent and symmetric. Therefore,  $\hat{\mathbf{X}}'\mathbf{X} = \mathbf{X}'\mathbf{P}_Z\mathbf{X} = (\mathbf{P}_Z\mathbf{X})'\mathbf{P}_Z\mathbf{X} = \hat{\mathbf{X}}'\hat{\mathbf{X}}$ . Plugging this expression into equation (5.17) shows that the IV estimator that uses instruments  $\hat{\mathbf{x}}_i$  can be written as  $\hat{\boldsymbol{\beta}} = (\hat{\mathbf{X}}'\hat{\mathbf{X}})^{-1}\hat{\mathbf{X}}'\mathbf{Y}$ . The name "two-stage least squares" comes from this procedure.

To summarize,  $\hat{\beta}$  can be obtained from the following steps:

1. Obtain the fitted values  $\hat{x}_K$  from the regression

$$x_K \text{ on } 1, x_1, \dots, x_{K-1}, z_1, \dots, z_M$$
 (5.18)

where the *i* subscript is omitted for simplicity. This is called the **first-stage regression.** 

2. Run the OLS regression

$$y \text{ on } 1, x_1, \dots, x_{K-1}, \hat{x}_K$$
 (5.19)

This is called the **second-stage regression**, and it produces the  $\hat{\beta}_i$ .

In practice, it is best to use a software package with a 2SLS command rather than explicitly carry out the two-step procedure. Carrying out the two-step procedure explicitly makes one susceptible to harmful mistakes. For example, the following, seemingly sensible, two-step procedure is generally inconsistent: (1) regress  $x_K$  on  $1, z_1, \ldots, z_M$  and obtain the fitted values, say  $\tilde{x}_K$ ; (2) run the regression in (5.19) with  $\tilde{x}_K$  in place of  $\hat{x}_K$ . Problem 5.11 asks you to show that omitting  $x_1, \ldots, x_{K-1}$  in the first-stage regression and then explicitly doing the second-stage regression produces inconsistent estimators of the  $\beta_i$ .

Another reason to avoid the two-step procedure is that the OLS standard errors reported with regression (5.19) will be incorrect, something that will become clear later. Sometimes for hypothesis testing we need to carry out the second-stage regression explicitly—see Section 5.2.4.

The 2SLS estimator and the IV estimator from Section 5.1.1 are identical when there is only one instrument for  $x_K$ . Unless stated otherwise, we mean 2SLS whenever we talk about IV estimation of a single equation.

{107}------------------------------------------------

What is the analogue of the condition (5.5) when more than one instrument is available with one endogenous explanatory variable? Problem 5.12 asks you to show that Eðz<sup>0</sup> xÞ has full column rank if and only if at least one of the y<sup>j</sup> in equation (5.14) is nonzero. The intuition behind this requirement is pretty clear: we need at least one exogenous variable that does not appear in equation (5.1) to induce variation in xK that cannot be explained by x1; ... ; xK-1. Identification of *b* does not depend on the values of the d<sup>h</sup> in equation (5.14).

Testing the rank condition with a single endogenous explanatory variable and multiple instruments is straightforward. In equation (5.14) we simply test the null hypothesis

$$H_0: \theta_1 = 0, \ \theta_2 = 0, \dots, \theta_M = 0$$
 (5.20)

against the alternative that at least one of the y<sup>j</sup> is different from zero. This test gives a compelling reason for explicitly running the first-stage regression. If rK in equation (5.14) satisfies the OLS homoskedasticity assumption OLS.3, a standard F statistic or Lagrange multiplier statistic can be used to test hypothesis (5.20). Often a heteroskedasticity-robust statistic is more appropriate, especially if xK has discrete characteristics. If we cannot reject hypothesis (5.20) against the alternative that at least one y<sup>h</sup> is different from zero, at a reasonably small significance level, then we should have serious reservations about the proposed 2SLS procedure: the instruments do not pass a minimal requirement.

The model with a single endogenous variable is said to be overidentified when M > 1 and there are M - 1 overidentifying restrictions. This terminology comes from the fact that, if each zh has some partial correlation with xK , then we have M - 1 more exogenous variables than needed to identify the parameters in equation (5.1). For example, if M ¼ 2, we could discard one of the instruments and still achieve identification. In Chapter 6 we will show how to test the validity of any overidentifying restrictions.