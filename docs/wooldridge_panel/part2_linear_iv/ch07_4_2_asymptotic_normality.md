# Asymptotic Normality

> Pages: 169-170

We now sketch the asymptotic normality of the GLS estimator under Assumptions SGLS.1 and SGLS.2 and some weak moment conditions. The first step is familiar:

$$\sqrt{N}(\boldsymbol{\beta}^* - \boldsymbol{\beta}) = \left(N^{-1} \sum_{i=1}^N \mathbf{X}_i' \mathbf{\Omega}^{-1} \mathbf{X}_i\right)^{-1} \left(N^{-1/2} \sum_{i=1}^N \mathbf{X}_i' \mathbf{\Omega}^{-1} \mathbf{u}_i\right)$$
(7.32)

By the CLT,  $N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{u}_{i} \xrightarrow{d} \text{Normal}(\mathbf{0}, \mathbf{B})$ , where

$$\mathbf{B} \equiv \mathrm{E}(\mathbf{X}_i' \mathbf{\Omega}^{-1} \mathbf{u}_i \mathbf{u}_i' \mathbf{\Omega}^{-1} \mathbf{X}_i) \tag{7.33}$$

Further, since  $N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_i' \mathbf{\Omega}^{-1} \mathbf{u}_i = O_p(1)$  and  $(N^{-1} \sum_{i=1}^{N} \mathbf{X}_i' \mathbf{\Omega}^{-1} \mathbf{X}_i)^{-1} - \mathbf{A}^{-1} = o_p(1)$ , we can write  $\sqrt{N}(\boldsymbol{\beta}^* - \boldsymbol{\beta}) = \mathbf{A}^{-1}(N^{-1/2} \sum_{i=1}^{N} \mathbf{x}_i' \mathbf{\Omega}^{-1} \mathbf{u}_i) + o_p(1)$ . It follows from the asymptotic equivalence lemma that

$$\sqrt{N}(\boldsymbol{\beta}^* - \boldsymbol{\beta}) \stackrel{a}{\sim} \text{Normal}(\mathbf{0}, \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-1})$$
 (7.34)

Thus,

$$Avar(\hat{\beta}) = \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-1}/N \tag{7.35}$$

The asymptotic variance in equation (7.35) is not the asymptotic variance usually derived for GLS estimation of systems of equations. Usually the formula is reported as  $A^{-1}/N$ . But equation (7.35) is the appropriate expression under the assumptions made so far. The simpler form, which results when B = A, is not generally valid under Assumptions SGLS.1 and SGLS.2, because we have assumed nothing about the variance matrix of  $\mathbf{u}_i$  conditional on  $\mathbf{X}_i$ . In Section 7.5.2 we make an assumption that simplifies equation (7.35).

{170}------------------------------------------------

#### 7.5 Feasible GLS