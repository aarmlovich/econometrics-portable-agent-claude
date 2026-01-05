# Consistency

> Pages: 364-367

For the general two-step M-estimator, when will  $\hat{\theta}$  be consistent for  $\theta_0$ ? In practice, the important condition is the identification assumption. To state the identification

{365}------------------------------------------------

condition, we need to know about the asymptotic behavior of  $\hat{\gamma}$ . A general assumption is that  $\hat{\gamma} \xrightarrow{p} \gamma^*$ , where  $\gamma^*$  is some element in  $\Gamma$ . We label this value  $\gamma^*$  to allow for the possibility that  $\hat{\gamma}$  does not converge to a parameter indexing some interesting feature of the distribution of  $\mathbf{w}$ . In some cases, the plim of  $\hat{\gamma}$  will be of direct interest. In the weighted regression case, if we assume that  $h(\mathbf{x}, \gamma)$  is a correctly specified model for  $\mathrm{Var}(y \mid \mathbf{x})$ , then it is possible to choose an estimator such that  $\hat{\gamma} \xrightarrow{p} \gamma_0$ , where  $\mathrm{Var}(y \mid \mathbf{x}) = h(\mathbf{x}, \gamma_0)$ . (For an example, see Problem 12.2.) If the variance model is misspecified, plim  $\hat{\gamma}$  is generally well defined, but  $\mathrm{Var}(y \mid \mathbf{x}) \neq h(\mathbf{x}, \gamma^*)$ ; it is for this reason that we use the notation  $\gamma^*$ .

The identification condition for the two-step M-estimator is

$$E[q(\mathbf{w}, \boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*})] < E[q(\mathbf{w}, \boldsymbol{\theta}; \boldsymbol{\gamma}^{*})], \quad \text{all } \boldsymbol{\theta} \in \boldsymbol{\Theta}, \quad \boldsymbol{\theta} \neq \boldsymbol{\theta}_{o}$$

The consistency argument is essentially the same as that underlying Theorem 12.2. If  $q(\mathbf{w}_i, \theta; \gamma)$  satisfies the UWLLN over  $\mathbf{\Theta} \times \mathbf{\Gamma}$  then expression (12.31) can be shown to converge to  $\mathrm{E}[q(\mathbf{w}, \theta; \gamma^*)]$  uniformly over  $\mathbf{\Theta}$ . Along with identification, this result can be shown to imply consistency of  $\hat{\boldsymbol{\theta}}$  for  $\theta_0$ .

In some applications of two-step M-estimation, identification of  $\theta_0$  holds for *any*  $\gamma \in \Gamma$ . This result can be shown for the WNLS estimator (see Problem 12.4). It is for this reason that WNLS is still consistent even if the function  $h(\mathbf{x}, \gamma)$  is not correctly specified for  $\text{Var}(y \mid \mathbf{x})$ . The weakest version of the identification assumption for WNLS is the following:

Assumption WNLS.2: 
$$\mathrm{E}\{[m(\mathbf{x}, \boldsymbol{\theta}_{\mathrm{o}}) - m(\mathbf{x}, \boldsymbol{\theta})]^2 / h(\mathbf{x}, \boldsymbol{\gamma}^*)\} > 0$$
, all  $\boldsymbol{\theta} \in \boldsymbol{\Theta}$ ,  $\boldsymbol{\theta} \neq \boldsymbol{\theta}_{\mathrm{o}}$ , where  $\boldsymbol{\gamma}^* = \mathrm{plim} \ \hat{\boldsymbol{\gamma}}$ .

As with the case of NLS, we know that weak inequality holds in Assumption WNLS.2 under Assumption WNLS.1. The strict inequality in Assumption WNLS.2 puts restrictions on the distribution of  $\mathbf{x}$  and the functional forms of m and h.

In other cases, including several two-step maximum likelihood estimators we encounter in Part IV, the identification condition for  $\theta_o$  holds only for  $\gamma = \gamma^* = \gamma_o$ , where  $\gamma_o$  also indexes some feature of the distribution of **w**.

# 12.4.2 Asymptotic Normality

With the two-step M-estimator, there are two cases worth distinguishing. The first occurs when the asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o})$  does not depend on the asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{y}}-\boldsymbol{\gamma}^{*})$ , and the second occurs when the asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{\theta}}-\boldsymbol{\theta}_{o})$  must be adjusted to account for the first-stage estimation of  $\boldsymbol{\gamma}^{*}$ . We first derive conditions under which we can ignore the first-stage estimation error.

{366}------------------------------------------------

Using arguments similar to those in Section 12.3, it can be shown that, under standard regularity conditions,

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = \mathbf{A}_{o}^{-1} \left( -N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\boldsymbol{\theta}_{o}; \hat{\boldsymbol{\gamma}}) \right) + o_{p}(1)$$
(12.33)

where now  $\mathbf{A}_{o} = \mathrm{E}[\mathbf{H}(\mathbf{w}, \boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*})]$ . In obtaining the score and the Hessian, we take derivatives only with respect to  $\boldsymbol{\theta}$ ;  $\boldsymbol{\gamma}^{*}$  simply appears as an extra argument. Now, if

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\boldsymbol{\theta}_{o}; \hat{\boldsymbol{\gamma}}) = N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*}) + o_{p}(1)$$
(12.34)

then  $\sqrt{N}(\hat{\theta} - \theta_0)$  behaves the same asymptotically whether we used  $\hat{\gamma}$  or its plim in defining the M-estimator.

When does equation (12.34) hold? Assuming that  $\sqrt{N}(\hat{\gamma} - \gamma^*) = O_p(1)$ , which is standard, a mean value expansion similar to the one in Section 12.3 gives

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\boldsymbol{\theta}_{o}; \hat{\boldsymbol{\gamma}}) = N^{-1/2} \sum_{i=1}^{N} \mathbf{s}_{i}(\boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*}) + \mathbf{F}_{o} \sqrt{N} (\hat{\boldsymbol{\gamma}} - \boldsymbol{\gamma}^{*}) + o_{p}(1)$$
(12.35)

where  $\mathbf{F}_0$  is the  $P \times J$  matrix

$$\mathbf{F}_{o} \equiv \mathrm{E}[\nabla_{\gamma} \mathbf{s}(\mathbf{w}, \boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*})] \tag{12.36}$$

(Remember, J is the dimension of  $\gamma$ .) Therefore, if

$$E[\nabla_{\mathbf{y}}\mathbf{s}(\mathbf{w},\boldsymbol{\theta}_{0};\boldsymbol{\gamma}^{*})] = \mathbf{0}$$
 (12.37)

then equation (12.34) holds, and the asymptotic variance of the two-step M-estimator is the same as if  $\gamma^*$  were plugged in. In other words, under assumption (12.37), we conclude that equation (12.18) holds, where  $\mathbf{A}_o$  and  $\mathbf{B}_o$  are given in expressions (12.19) and (12.20), respectively, except that  $\gamma^*$  appears as an argument in the score and Hessian. For deriving the asymptotic distribution of  $\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_o)$ , we can ignore the fact that  $\hat{\boldsymbol{\gamma}}$  was obtained in a first-stage estimation.

One case where assumption (12.37) holds is weighted nonlinear least squares, something you are asked to show in Problem 12.4. Naturally, we must assume that the conditional mean is correctly specified, but, interestingly, assumption (12.37) holds whether or not the conditional variance is correctly specified.

There are many problems for which assumption (12.37) does not hold, including some of the methods for correcting for endogeneity in probit and Tobit models in Part IV. In Chapter 17 we will see that two-step methods for correcting sample selection

{367}------------------------------------------------

bias are two-step M-estimators, but assumption (12.37) fails. In such cases we need to make an adjustment to the asymptotic variance of  $\sqrt{N}(\hat{\theta} - \theta_0)$ . The adjustment is easily obtained from equation (12.35), once we have a first-order representation for  $\sqrt{N}(\hat{\gamma} - \gamma^*)$ . We assume that

$$\sqrt{N}(\hat{\gamma} - \gamma^*) = N^{-1/2} \sum_{i=1}^{N} \mathbf{r}_i(\gamma^*) + o_p(1)$$
(12.38)

where  $\mathbf{r}_i(\gamma^*)$  is a  $J \times 1$  vector with  $\mathrm{E}[\mathbf{r}_i(\gamma^*)] = \mathbf{0}$  (in practice,  $\mathbf{r}_i$  depends on parameters other than  $\gamma^*$ , but we suppress those here for simplicity). Therefore,  $\hat{\gamma}$  could itself be an M-estimator or, as we will see in Chapter 14, a generalized method of moments estimator. In fact, every estimator considered in this book has a representation as in equation (12.38).

Now we can write

$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = \mathbf{A}_{o}^{-1} N^{-1/2} \sum_{i=1}^{N} [-\mathbf{g}_{i}(\boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*})] + o_{p}(1)$$
(12.39)

where  $\mathbf{g}_i(\boldsymbol{\theta}_o; \boldsymbol{\gamma}^*) \equiv \mathbf{s}_i(\boldsymbol{\theta}_o; \boldsymbol{\gamma}^*) + \mathbf{F}_o \mathbf{r}_i(\boldsymbol{\gamma}^*)$ . Since  $\mathbf{g}_i(\boldsymbol{\theta}_o; \boldsymbol{\gamma}^*)$  has zero mean, the standardized partial sum in equation (12.39) can be assumed to satisfy the central limit theorem. Define the  $P \times P$  matrix

$$\mathbf{D}_{o} \equiv \mathrm{E}[\mathbf{g}_{i}(\boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*})\mathbf{g}_{i}(\boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*})'] = \mathrm{Var}[\mathbf{g}_{i}(\boldsymbol{\theta}_{o}; \boldsymbol{\gamma}^{*})]$$
(12.40)

Then

Avar 
$$\sqrt{N}(\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) = \mathbf{A}_{o}^{-1}\mathbf{D}_{o}\mathbf{A}_{o}^{-1}$$
 (12.41)

We will discuss estimation of this matrix in the next section.