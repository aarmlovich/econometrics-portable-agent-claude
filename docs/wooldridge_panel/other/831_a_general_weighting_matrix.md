# **8.3.1** A General Weighting Matrix

> Pages: 201-212

The orthogonality conditions in Assumption SIV.1 suggest an estimation strategy. Under Assumptions SIV.1 and SIV.2,  $\beta$  is the *unique*  $K \times 1$  vector solving the linear set population moment conditions

$$\mathbf{E}[\mathbf{Z}_i'(\mathbf{y}_i - \mathbf{X}_i\boldsymbol{\beta})] = \mathbf{0} \tag{8.19}$$

(That  $\beta$  is a solution follows from Assumption SIV.1; that it is unique follows by Assumption SIV.2.) In other words, if **b** is any other  $K \times 1$  vector (so that at least one element of **b** is different from the corresponding element in  $\beta$ ), then

{202}------------------------------------------------

$$\mathbf{E}[\mathbf{Z}_i'(\mathbf{y}_i - \mathbf{X}_i \mathbf{b})] \neq \mathbf{0} \tag{8.20}$$

This formula shows that  $\beta$  is identified. Because sample averages are consistent estimators of population moments, the analogy principle applied to condition (8.19) suggests choosing the estimator  $\hat{\beta}$  to solve

$$N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}'(\mathbf{y}_{i} - \mathbf{X}_{i}\hat{\boldsymbol{\beta}}) = \mathbf{0}$$
 (8.21)

Equation (8.21) is a set of L linear equations in the K unknowns in  $\hat{\beta}$ . First consider the case L = K, so that we have exactly enough IVs for the explanatory variables in the system. Then, if the  $K \times K$  matrix  $\sum_{i=1}^{N} \mathbf{Z}_{i}^{i} \mathbf{X}_{i}$  is nonsingular, we can solve for  $\hat{\beta}$  as

$$\hat{\boldsymbol{\beta}} = \left(N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{X}_{i}\right)^{-1} \left(N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{y}_{i}\right)$$
(8.22)

We can write  $\hat{\beta}$  using full matrix notation as  $\hat{\beta} = (\mathbf{Z}'\mathbf{X})^{-1}\mathbf{Z}'\mathbf{Y}$ , where  $\mathbf{Z}$  is the  $NG \times L$  matrix obtained by stacking  $\mathbf{Z}_i$  from i = 1, 2, ..., N,  $\mathbf{X}$  is the  $NG \times K$  matrix obtained by stacking  $\mathbf{X}_i$  from i = 1, 2, ..., N, and  $\mathbf{Y}$  is the  $NG \times 1$  vector obtained from stacking  $\mathbf{y}_i$ , i = 1, 2, ..., N. We call equation (8.22) the **system IV (SIV) estimator**. Application of the law of large numbers shows that the SIV estimator is consistent under Assumptions SIV.1 and SIV.2.

When L > K—so that we have more columns in the IV matrix  $\mathbf{Z}_i$  than we need for identification—choosing  $\hat{\boldsymbol{\beta}}$  is more complicated. Except in special cases, equation (8.21) will not have a solution. Instead, we choose  $\hat{\boldsymbol{\beta}}$  to make the vector in equation (8.21) as "small" as possible in the sample. One idea is to minimize the squared Euclidean length of the  $L \times 1$  vector in equation (8.21). Dropping the 1/N, this approach suggests choosing  $\hat{\boldsymbol{\beta}}$  to make

$$\left[\sum_{i=1}^{N} \mathbf{Z}_{i}'(\mathbf{y}_{i} - \mathbf{X}_{i}\hat{\boldsymbol{\beta}})\right]' \left[\sum_{i=1}^{N} \mathbf{Z}_{i}'(\mathbf{y}_{i} - \mathbf{X}_{i}\hat{\boldsymbol{\beta}})\right]$$

as small as possible. While this method produces a consistent estimator under Assumptions SIV.1 and SIV.2, it rarely produces the best estimator, for reasons we will see in Section 8.3.3.

A more general class of estimators is obtained by using a **weighting matrix** in the quadratic form. Let  $\hat{\mathbf{W}}$  be an  $L \times L$  symmetric, positive semidefinite matrix, where the " $^{^{^{^{^{^{^{^{^{^{^{^{^{^{^{^{^{^{^{$ 

{203}------------------------------------------------

$$\min_{\mathbf{b}} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}'(\mathbf{y}_{i} - \mathbf{X}_{i}\mathbf{b}) \right]' \hat{\mathbf{W}} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}'(\mathbf{y}_{i} - \mathbf{X}_{i}\mathbf{b}) \right]$$
(8.23)

Because expression (8.23) is a quadratic function of **b**, the solution to it has a closed form. Using multivariable calculus or direct substitution, we can show that the unique solution is

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{Z}\hat{\mathbf{W}}\mathbf{Z}'\mathbf{X})^{-1}(\mathbf{X}'\mathbf{Z}\hat{\mathbf{W}}\mathbf{Z}'\mathbf{Y}) \tag{8.24}$$

assuming that  $\mathbf{X}'\mathbf{Z}\mathbf{\hat{W}}\mathbf{Z}'\mathbf{X}$  is nonsingular. To show that this estimator is consistent, we assume that  $\mathbf{\hat{W}}$  has a nonsingular probability limit.

ASSUMPTION SIV.3:  $\hat{\mathbf{W}} \stackrel{p}{\to} \mathbf{W}$  as  $N \to \infty$ , where  $\mathbf{W}$  is a nonrandom, symmetric,  $L \times L$  positive definite matrix.

In applications, the convergence in Assumption SIV.3 will follow from the law of large numbers because  $\hat{\mathbf{W}}$  will be a function of sample averages. The fact that  $\mathbf{W}$  is assumed to be positive definite means that  $\hat{\mathbf{W}}$  is positive definite with probability approaching one (see Chapter 3). We could relax the assumption of positive definiteness to positive semidefiniteness at the cost of complicating the assumptions. In most applications, we can assume that  $\mathbf{W}$  is positive definite.

THEOREM 8.1 (Consistency of GMM): Under Assumptions SIV.1–SIV.3,  $\hat{\beta} \stackrel{p}{\to} \beta$  as  $N \to \infty$ .

*Proof:* Write

$$\hat{\boldsymbol{\beta}} = \left[ \left( N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{Z}_{i} \right) \hat{\mathbf{W}} \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{X}_{i} \right) \right]^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{Z}_{i} \right) \hat{\mathbf{W}} \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{y}_{i} \right)$$

Plugging in  $\mathbf{y}_i = \mathbf{X}_i \boldsymbol{\beta} + \mathbf{u}_i$  and doing a little algebra gives

$$\hat{\boldsymbol{\beta}} = \boldsymbol{\beta} + \left[ \left( N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{Z}_{i} \right) \hat{\mathbf{W}} \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{X}_{i} \right) \right]^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{Z}_{i} \right) \hat{\mathbf{W}} \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{u}_{i} \right)$$

Under Assumption SIV.2,  $\mathbf{C} \equiv \mathbf{E}(\mathbf{Z}_i'\mathbf{X}_i)$  has rank K, and combining this with Assumption SIV.3,  $\mathbf{C}'\mathbf{W}\mathbf{C}$  has rank K and is therefore nonsingular. It follows by the law of large numbers that plim  $\hat{\boldsymbol{\beta}} = \boldsymbol{\beta} + (\mathbf{C}'\mathbf{W}\mathbf{C})^{-1}\mathbf{C}'\mathbf{W}(\text{plim } N^{-1}\sum_{i=1}^{N}\mathbf{Z}_i'\mathbf{u}_i) = \boldsymbol{\beta} + (\mathbf{C}'\mathbf{W}\mathbf{C})^{-1}\mathbf{C}'\mathbf{W} \cdot \mathbf{0} = \boldsymbol{\beta}$ .

Theorem 8.1 shows that a large class of estimators is consistent for  $\beta$  under Assumptions SIV.1 and SIV.2, provided that we choose  $\hat{\mathbf{W}}$  to satisfy modest restric-

{204}------------------------------------------------

tions. When L = K, the GMM estimator in equation (8.24) becomes equation (8.22), no matter how we choose  $\hat{\mathbf{W}}$ , because  $\mathbf{X}'\mathbf{Z}$  is a  $K \times K$  nonsingular matrix.

We can also show that  $\hat{\beta}$  is asymptotically normally distributed under these first three assumptions.

THEOREM 8.2 (Asymptotic Normality of GMM): Under Assumptions SIV.1–SIV.3,  $\sqrt{N}(\hat{\beta} - \beta)$  is asymptotically normally distributed with mean zero and

Avar 
$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = (\mathbf{C}'\mathbf{W}\mathbf{C})^{-1}\mathbf{C}'\mathbf{W}\boldsymbol{\Lambda}\mathbf{W}\mathbf{C}(\mathbf{C}'\mathbf{W}\mathbf{C})^{-1}$$
 (8.25)

where

$$\mathbf{\Lambda} \equiv \mathrm{E}(\mathbf{Z}_i' \mathbf{u}_i \mathbf{u}_i' \mathbf{Z}_i) = \mathrm{Var}(\mathbf{Z}_i' \mathbf{u}_i) \tag{8.26}$$

We will not prove this theorem in detail as it can be reasoned from

$$\sqrt{N}(\hat{\pmb{\beta}} - \pmb{\beta})$$

$$= \left[ \left( N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{Z}_{i} \right) \hat{\mathbf{W}} \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{X}_{i} \right) \right]^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{Z}_{i} \right) \hat{\mathbf{W}} \left( N^{-1/2} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{u}_{i} \right)$$

where we use the fact that  $N^{-1/2} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{u}_{i} \xrightarrow{d} \text{Normal}(\mathbf{0}, \mathbf{\Lambda})$ . The asymptotic variance matrix in equation (8.25) looks complicated, but it can be consistently estimated. If  $\hat{\mathbf{\Lambda}}$  is a consistent estimator of  $\mathbf{\Lambda}$ —more on this later—then equation (8.25) is consistently estimated by

$$[(\mathbf{X}'\mathbf{Z}/N)\hat{\mathbf{W}}(\mathbf{Z}'\mathbf{X}/N)]^{-1}(\mathbf{X}'\mathbf{Z}/N)\hat{\mathbf{W}}\hat{\mathbf{\Lambda}}\hat{\mathbf{W}}(\mathbf{Z}'\mathbf{X}/N)[(\mathbf{X}'\mathbf{Z}/N)\hat{\mathbf{W}}(\mathbf{Z}'\mathbf{X}/N)]^{-1}$$
(8.27)

As usual, we estimate Avar( $\hat{\beta}$ ) by dividing expression (8.27) by N.

While the general formula (8.27) is occasionally useful, it turns out that it is greatly simplified by choosing  $\hat{\mathbf{W}}$  appropriately. Since this choice also (and not coincidentally) gives the asymptotically efficient estimator, we hold off discussing asymptotic variances further until we cover the optimal choice of  $\hat{\mathbf{W}}$  in Section 8.3.3.

# 8.3.2 The System 2SLS Estimator

A choice of  $\hat{\mathbf{W}}$  that leads to a useful and familiar-looking estimator is

$$\hat{\mathbf{W}} = \left(N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{Z}_{i}\right)^{-1} = (\mathbf{Z}' \mathbf{Z}/N)^{-1}$$

$$(8.28)$$

which is a consistent estimator of  $[E(\mathbf{Z}_i'\mathbf{Z}_i)]^{-1}$ . Assumption SIV.3 simply requires that  $E(\mathbf{Z}_i'\mathbf{Z}_i)$  exist and be nonsingular, and these requirements are not very restrictive.

{205}------------------------------------------------

When we plug equation (8.28) into equation (8.24) and cancel N everywhere, we get

$$\hat{\boldsymbol{\beta}} = [\mathbf{X}'\mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{X}]^{-1}\mathbf{X}'\mathbf{Z}(\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{Y}$$
(8.29)

This looks just like the single-equation 2SLS estimator, and so we call it the **system 2SLS estimator**.

When we apply equation (8.29) to the system of equations (8.12), with definitions (8.14) and (8.15), we get something very familiar. As an exercise, you should show that  $\hat{\beta}$  produces **2SLS equation by equation**. (The proof relies on the block diagonal structures of  $\mathbf{Z}_i'\mathbf{Z}_i$  and  $\mathbf{Z}_i'\mathbf{X}_i$  for each *i*.) In other words, we estimate the first equation by 2SLS using instruments  $\mathbf{z}_{i1}$ , the second equation by 2SLS using instruments  $\mathbf{z}_{i2}$ , and so on. When we stack these into one long vector, we get equation (8.29).

Problem 8.8 asks you to show that, in panel data applications, a natural choice of  $\mathbb{Z}_i$  makes the system 2SLS estimator a **pooled 2SLS estimator**.

In the next subsection we will see that the system 2SLS estimator is not necessarily the asymptotically efficient estimator. Still, it is  $\sqrt{N}$ -consistent and easy to compute given the data matrices X, Y, and Z. This latter feature is important because we need a preliminary estimator of  $\beta$  to obtain the asymptotically efficient estimator.

# **8.3.3** The Optimal Weighting Matrix

Given that a GMM estimator exists for any positive definite weighting matrix, it is important to have a way of choosing among all of the possibilities. It turns out that there is a choice of **W** that produces the GMM estimator with the smallest asymptotic variance.

We can appeal to expression (8.25) for a hint as to the optimal choice of **W**. It is this expression we are trying to make as small as possible, in the matrix sense. (See Definition 3.11 for the definition of relative asymptotic efficiency.) The expression (8.25) simplifies to  $(\mathbf{C}'\mathbf{\Lambda}^{-1}\mathbf{C})^{-1}$  if we set  $\mathbf{W} \equiv \mathbf{\Lambda}^{-1}$ . Using standard arguments from matrix algebra, it can be shown that  $(\mathbf{C}'\mathbf{W}\mathbf{C})^{-1}\mathbf{C}'\mathbf{W}\mathbf{\Lambda}\mathbf{W}\mathbf{C}(\mathbf{C}'\mathbf{W}\mathbf{C})^{-1} - (\mathbf{C}'\mathbf{\Lambda}^{-1}\mathbf{C})^{-1}$  is positive semidefinite for any  $L \times L$  positive definite matrix **W**. The easiest way to prove this point is to show that

$$(\mathbf{C}'\mathbf{\Lambda}^{-1}\mathbf{C}) - (\mathbf{C}'\mathbf{W}\mathbf{C})(\mathbf{C}'\mathbf{W}\mathbf{\Lambda}\mathbf{W}\mathbf{C})^{-1}(\mathbf{C}'\mathbf{W}\mathbf{C})$$
(8.30)

is positive semidefinite, and we leave this proof as an exercise (see Problem 8.5). This discussion motivates the following assumption and theorem.

ASSUMPTION SIV.4:  $\mathbf{W} = \mathbf{\Lambda}^{-1}$ , where  $\mathbf{\Lambda}$  is defined by expression (8.26).

THEOREM 8.3 (Optimal Weighting Matrix): Under Assumptions SIV.1–SIV.4, the resulting GMM estimator is efficient among all GMM estimators of the form (8.24).

{206}------------------------------------------------

Provided that we can consistently estimate  $\Lambda$ , we can obtain the asymptotically efficient GMM estimator. Any consistent estimator of  $\Lambda$  delivers the efficient GMM estimator, but one estimator is commonly used that imposes no structure on  $\Lambda$ .

Procedure 8.1 (GMM with Optimal Weighting Matrix):

- a. Let  $\hat{\beta}$  be an initial consistent estimator of  $\beta$ . In most cases this is the system 2SLS estimator.
- b. Obtain the  $G \times 1$  residual vectors

$$\hat{\mathbf{u}}_i = \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}}, \qquad i = 1, 2, \dots, N \tag{8.31}$$

- c. A generally consistent estimator of  $\Lambda$  is  $\hat{\Lambda} = N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{u}}_{i}' \hat{\mathbf{z}}_{i}' \mathbf{Z}_{i}$ .
- d. Choose

$$\hat{\mathbf{W}} \equiv \hat{\mathbf{\Lambda}}^{-1} = \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\hat{\mathbf{u}}}_{i} \hat{\mathbf{u}}_{i}' \mathbf{Z}_{i} \right)^{-1}$$
(8.32)

and use this matrix to obtain the asymptotically optimal GMM estimator.

The estimator of  $\Lambda$  in part c of Procedure 8.1 is consistent for  $E(\mathbf{Z}_i'\mathbf{u}_i\mathbf{u}_i'\mathbf{Z}_i)$  under general conditions. When each row of  $\mathbf{Z}_i$  and  $\mathbf{u}_i$  represent different time periods—so that we have a single-equation panel data model—the estimator  $\hat{\Lambda}$  allows for arbitrary heteroskedasticity (conditional or unconditional) as well as arbitrary serial dependence (conditional or unconditional). The reason we can allow this generality is that we fix the row dimension of  $\mathbf{Z}_i$  and  $\mathbf{u}_i$  and let  $N \to \infty$ . Therefore, we are assuming that N, the size of the cross section, is large enough relative to T to make fixed T asymptotics sensible. (This is the same approach we took in Chapter 7.) With N very large relative to T, there is no need to downweight correlations between time periods that are far apart, as in the Newey and West (1987) estimator applied to time series problems. Ziliak and Kniesner (1998) do use a Newey-West type procedure in a panel data application with large N. Theoretically, this is not required, and it is not completely general because it assumes that the underlying time series are weakly dependent. (See Wooldridge, 1994, for discussion of weak dependence in time series contexts.) A Newey-West type estimator might improve the finite-sample performance of the GMM estimator.

The asymptotic variance of the optimal GMM estimator is estimated as

$$\left[ (\mathbf{X}'\mathbf{Z}) \left( \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{u}}_{i} \hat{\mathbf{u}}_{i}' \mathbf{Z}_{i} \right)^{-1} (\mathbf{Z}'\mathbf{X}) \right]^{-1}$$
(8.33)

{207}------------------------------------------------

where  $\hat{\mathbf{u}}_i \equiv \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}}$ ; asymptotically, it makes no difference whether the first-stage residuals  $\hat{\mathbf{u}}_i$  are used in place of  $\hat{\mathbf{u}}_i$ . The square roots of diagonal elements of this matrix are the asymptotic standard errors of the optimal GMM estimator. This estimator is called a **minimum chi-square estimator**, for reasons that will become clear in Section 8.5.2.

When  $\mathbf{Z}_i = \mathbf{X}_i$  and the  $\hat{\mathbf{u}}_i$  are the system OLS residuals, expression (8.33) becomes the robust variance matrix estimator for SOLS [see expression (7.26)]. This expression reduces to the robust variance matrix estimator for FGLS when  $\mathbf{Z}_i = \hat{\mathbf{\Omega}}^{-1}\mathbf{X}_i$  and the  $\hat{\mathbf{u}}_i$  are the FGLS residuals [see equation (7.49)].

# 8.3.4 The Three-Stage Least Squares Estimator

The GMM estimator using weighting matrix (8.32) places no restrictions on either the unconditional or conditional (on  $\mathbf{Z}_i$ ) variance matrix of  $\mathbf{u}_i$ : we can obtain the asymptotically efficient estimator without making additional assumptions. Nevertheless, it is still common, especially in traditional simultaneous equations analysis, to assume that the conditional variance matrix of  $\mathbf{u}_i$  given  $\mathbf{Z}_i$  is constant. This assumption leads to a system estimator that is a middle ground between system 2SLS and the always-efficient minimum chi-square estimator.

The three-stage least squares (3SLS) estimator is a GMM estimator that uses a particular weighting matrix. To define the 3SLS estimator, let  $\hat{\mathbf{u}}_i = \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}}$  be the residuals from an initial estimation, usually system 2SLS. Define the  $G \times G$  matrix

$$\hat{\mathbf{\Omega}} \equiv N^{-1} \sum_{i=1}^{N} \hat{\mathbf{u}}_{i} \hat{\mathbf{u}}_{i}^{\prime} \tag{8.34}$$

Using the same arguments as in the FGLS case in Section 7.5.1,  $\hat{\Omega} \xrightarrow{p} \Omega = E(\mathbf{u}_i \mathbf{u}_i')$ . The weighting matrix used by 3SLS is

$$\hat{\mathbf{W}} = \left(N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{\Omega}} \mathbf{Z}_{i}\right)^{-1} = \left[\mathbf{Z}'(\mathbf{I}_{N} \otimes \hat{\mathbf{\Omega}}) \mathbf{Z}/N\right]^{-1}$$
(8.35)

where  $I_N$  is the  $N \times N$  identity matrix. Plugging this into equation (8.24) gives the 3SLS estimator

$$\hat{\boldsymbol{\beta}} = [\mathbf{X}'\mathbf{Z}\{\mathbf{Z}'(\mathbf{I}_N \otimes \hat{\boldsymbol{\Omega}})\mathbf{Z}\}^{-1}\mathbf{Z}'\mathbf{X}]^{-1}\mathbf{X}'\mathbf{Z}\{\mathbf{Z}'(\mathbf{I}_N \otimes \hat{\boldsymbol{\Omega}})\mathbf{Z}\}^{-1}\mathbf{Z}'\mathbf{Y}$$
(8.36)

By Theorems 8.1 and 8.2,  $\hat{\beta}$  is consistent and asymptotically normal under Assumptions SIV.1–SIV.3. Assumption SIV.3 requires  $E(\mathbf{Z}_i'\Omega\mathbf{Z}_i)$  to be nonsingular, a standard assumption.

{208}------------------------------------------------

When is 3SLS asymptotically efficient? First, note that equation (8.35) always consistently estimates  $[E(\mathbf{Z}_i'\Omega\mathbf{Z}_i)]^{-1}$ . Therefore, from Theorem 8.3, equation (8.35) is an efficient weighting matrix provided  $E(\mathbf{Z}_i'\Omega\mathbf{Z}_i) = \mathbf{\Lambda} = E(\mathbf{Z}_i'\mathbf{u}_i\mathbf{u}_i'\mathbf{Z}_i)$ .

ASSUMPTION SIV.5: 
$$E(\mathbf{Z}_i'\mathbf{u}_i\mathbf{u}_i'\mathbf{Z}_i) = E(\mathbf{Z}_i'\mathbf{\Omega}\mathbf{Z}_i)$$
, where  $\mathbf{\Omega} \equiv E(\mathbf{u}_i\mathbf{u}_i')$ .

Assumption SIV.5 is the system extension of the homoskedasticity assumption for 2SLS estimation of a single equation. A sufficient condition for Assumption SIV.5, and one that is easier to interpret, is

$$E(\mathbf{u}_i \mathbf{u}_i' | \mathbf{Z}_i) = E(\mathbf{u}_i \mathbf{u}_i') \tag{8.37}$$

We do not take equation (8.37) as the homoskedasticity assumption because there are interesting applications where Assumption SIV.5 holds but equation (8.37) does not (more on this topic in Chapters 9 and 11). When

$$\mathbf{E}(\mathbf{u}_i \mid \mathbf{Z}_i) = \mathbf{0} \tag{8.38}$$

is assumed in place of Assumption SIV.1, then equation (8.37) is equivalent to  $Var(\mathbf{u}_i | \mathbf{Z}_i) = Var(\mathbf{u}_i)$ . Whether we state the assumption as in equation (8.37) or use the weaker form, Assumption SIV.5, it is important to see that the elements of the unconditional variance matrix  $\Omega$  are *not* restricted:  $\sigma_g^2 = Var(u_g)$  can change across g, and  $\sigma_{gh} = Cov(u_g, u_h)$  can differ across g and h.

The system homoskedasticity assumption (8.37) necessarily holds when the instruments  $\mathbf{Z}_i$  are treated as nonrandom and  $\text{Var}(\mathbf{u}_i)$  is constant across *i*. Because we are assuming random sampling, we are forced to properly focus attention on the variance of  $\mathbf{u}_i$  conditional on  $\mathbf{Z}_i$ .

For the system of equations (8.12) with instruments defined in the matrix (8.15), Assumption SIV.5 reduces to (without the i subscript)

$$E(u_g u_h \mathbf{z}_g' \mathbf{z}_h) = E(u_g u_h) E(\mathbf{z}_g' \mathbf{z}_h), \qquad g, h = 1, 2, \dots, G$$
(8.39)

Therefore,  $u_g u_h$  must be uncorrelated with each of the elements of  $\mathbf{z}'_g \mathbf{z}_h$ . When g = h, assumption (8.39) becomes

$$E(u_a^2 \mathbf{z}_a' \mathbf{z}_g) = E(u_a^2) E(\mathbf{z}_a' \mathbf{z}_g)$$
(8.40)

so that  $u_g^2$  is uncorrelated with each element of  $\mathbf{z}_g$  along with the squares and cross products of the  $\mathbf{z}_g$  elements. This is exactly the homoskedasticity assumption for single-equation IV analysis (Assumption 2SLS.3). For  $g \neq h$ , assumption (8.39) is new because it involves covariances across different equations.

Assumption SIV.5 implies that Assumption SIV.4 holds [because the matrix (8.35) consistently estimates  $\Lambda^{-1}$  under Assumption SIV.5]. Therefore, we have the following theorem:

{209}------------------------------------------------

THEOREM 8.4 (Optimality of 3SLS): Under Assumptions SIV.1, SIV.2, SIV.3, and SIV.5, the 3SLS estimator is an optimal GMM estimator. Further, the appropriate estimator of  $\text{Avar}(\hat{\pmb{\beta}})$  is

$$\left[ (\mathbf{X}'\mathbf{Z}) \left( \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{\Omega}} \mathbf{Z}_{i} \right)^{-1} (\mathbf{Z}'\mathbf{X}) \right]^{-1} = \left[ \mathbf{X}' \mathbf{Z} \{ \mathbf{Z}' (\mathbf{I}_{N} \otimes \hat{\mathbf{\Omega}}) \mathbf{Z} \}^{-1} \mathbf{Z}' \mathbf{X} \right]^{-1}$$
(8.41)

It is important to understand the implications of this theorem. First, without Assumption SIV.5, the 3SLS estimator is generally less efficient, asymptotically, than the minimum chi-square estimator, and the asymptotic variance estimator for 3SLS in equation (8.41) is inappropriate. Second, even with Assumption SIV.5, the 3SLS estimator is no more asymptotically efficient than the minimum chi-square estimator: expressions (8.32) and (8.35) are both consistent estimators of  $\Lambda^{-1}$  under Assumption SIV.5. In other words, the estimators based on these two different choices for  $\hat{\mathbf{W}}$  are  $\sqrt{N}$ -equivalent under Assumption SIV.5.

Given the fact that the GMM estimator using expression (8.32) as the weighting matrix is never worse, asymptotically, than 3SLS, and in some important cases is strictly better, why is 3SLS ever used? There are at least two reasons. First, 3SLS has a long history in simultaneous equations models, whereas the GMM approach has been around only since the early 1980s, starting with the work of Hansen (1982) and White (1982b). Second, the 3SLS estimator might have better finite sample properties than the optimal GMM estimator when Assumption SIV.5 holds. However, whether it does or not must be determined on a case-by-case basis.

There is an interesting corollary to Theorem 8.4. Suppose that in the system (8.11) we can assume  $E(\mathbf{X}_i \otimes \mathbf{u}_i) = \mathbf{0}$ , which is Assumption SGLS.1 from Chapter 7. We can use a method of moments approach to estimating  $\boldsymbol{\beta}$ , where the instruments for each equation,  $\mathbf{x}_i^o$ , is the row vector containing every row of  $\mathbf{X}_i$ . As shown by Im, Ahn, Schmidt, and Wooldridge (1999), the 3SLS estimator using instruments  $\mathbf{Z}_i \equiv \mathbf{I}_G \otimes \mathbf{x}_i^o$  is equal to the feasible GLS estimator that uses the same  $\hat{\mathbf{\Omega}}$ . Therefore, if Assumption SIV.5 holds with  $\mathbf{Z}_i \equiv \mathbf{I}_G \otimes \mathbf{x}_i^o$ , FGLS is asymptotically efficient in the class of GMM estimators that use the orthogonality condition in Assumption SGLS.1. Sufficient for Assumption SIV.5 in the GLS context is the homoskedasticity assumption  $E(\mathbf{u}_i \mathbf{u}_i' | \mathbf{X}_i) = \hat{\mathbf{\Omega}}$ .

# 8.3.5 Comparison between GMM 3SLS and Traditional 3SLS

The definition of the GMM 3SLS estimator in equation (8.36) differs from the definition of the 3SLS estimator in most textbooks. Using our notation, the expression for the **traditional 3SLS estimator** is

{210}------------------------------------------------

$$\hat{\boldsymbol{\beta}} = \left(\sum_{i=1}^{N} \hat{\mathbf{X}}_{i}' \hat{\mathbf{\Omega}}^{-1} \hat{\mathbf{X}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \hat{\mathbf{X}}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{y}_{i}\right)$$

$$= \left[\hat{\mathbf{X}}' (\mathbf{I}_{N} \otimes \hat{\mathbf{\Omega}}^{-1}) \hat{\mathbf{X}}\right]^{-1} \hat{\mathbf{X}}' (\mathbf{I}_{N} \otimes \hat{\mathbf{\Omega}}^{-1}) \mathbf{Y}$$
(8.42)

where  $\hat{\Omega}$  is given in expression (8.34),  $\hat{\mathbf{X}}_i \equiv \mathbf{Z}_i \hat{\mathbf{\Pi}}$ , and  $\hat{\mathbf{\Pi}} = (\mathbf{Z}'\mathbf{Z})^{-1}\mathbf{Z}'\mathbf{X}$ . Comparing equations (8.36) and (8.42) shows that, in general, these are different estimators. To study equation (8.42) more closely, write it as

$$\hat{\boldsymbol{\beta}} = \boldsymbol{\beta} + \left( N^{-1} \sum_{i=1}^{N} \hat{\mathbf{X}}_{i}' \hat{\mathbf{\Omega}}^{-1} \hat{\mathbf{X}}_{i} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \hat{\mathbf{X}}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{u}_{i} \right)$$

Because  $\hat{\mathbf{\Pi}} \xrightarrow{p} \mathbf{\Pi} \equiv [\mathbf{E}(\mathbf{Z}_i'\mathbf{Z}_i)]^{-1}\mathbf{E}(\mathbf{Z}_i'\mathbf{X}_i)$  and  $\hat{\mathbf{\Omega}} \xrightarrow{p} \mathbf{\Omega}$ , the probability limit of the second term is the same as

$$\operatorname{plim}\left[N^{-1}\sum_{i=1}^{N}(\mathbf{Z}_{i}\mathbf{\Pi})'\mathbf{\Omega}^{-1}(\mathbf{Z}_{i}\mathbf{\Pi})\right]^{-1}\left[N^{-1}\sum_{i=1}^{N}(\mathbf{Z}_{i}\mathbf{\Pi})'\mathbf{\Omega}^{-1}\mathbf{u}_{i}\right]$$
(8.43)

The first factor in expression (8.43) generally converges to a positive definite matrix. Therefore, if equation (8.42) is to be consistent for  $\beta$ , we need

$$E[(\mathbf{Z}_i\mathbf{\Pi})'\mathbf{\Omega}^{-1}\mathbf{u}_i] = \mathbf{\Pi}'E[(\mathbf{\Omega}^{-1}\mathbf{Z}_i)'\mathbf{u}_i] = \mathbf{0}$$

Without assuming a special structure for  $\Pi$ , we should have that  $\Omega^{-1}\mathbf{Z}_i$  is uncorrelated with  $\mathbf{u}_i$ , an assumption that is *not* generally implied by Assumption SIV.1. In other words, the traditional 3SLS estimator generally uses a different set of orthogonality conditions than the GMM 3SLS estimator. The GMM 3SLS estimator is guaranteed to be consistent under Assumptions SIV.1–SIV.3, while the traditional 3SLS estimator is not.

The best way to illustrate this point is with model (8.12) where  $\mathbf{Z}_i$  is given in matrix (8.15) and we assume  $E(\mathbf{z}'_{ig}u_{ig}) = \mathbf{0}$ , g = 1, 2, ..., G. Now, unless  $\mathbf{\Omega}$  is diagonal,  $E[(\mathbf{\Omega}^{-1}\mathbf{Z}_i)'\mathbf{u}_i] \neq \mathbf{0}$  unless  $\mathbf{z}_{ig}$  is uncorrelated with each  $u_{ih}$  for all g, h = 1, 2, ..., G. If  $\mathbf{z}_{ig}$  is correlated with  $u_{ih}$  for some  $g \neq h$ , the transformation of the instruments in equation (8.42) results in inconsistency. The GMM 3SLS estimator is based on the original orthogonality conditions, while the traditional 3SLS estimator is not. See Problem 8.6 for the G = 2 case.

Why, then, does equation (8.42) usually appear as the definition of the 3SLS estimator? The reason is that the 3SLS estimator is typically introduced in simultaneous equations models where any variable exogenous in one equation is assumed to be


{211}------------------------------------------------

exogenous in all equations. Consider the model (8.12) again, but assume that the instrument matrix is  $\mathbf{Z}_i = \mathbf{I}_G \otimes \mathbf{z}_i$ , where  $\mathbf{z}_i$  contains the exogenous variables appearing anywhere in the system. With this choice of  $\mathbf{Z}_i$ , Assumption SIV.1 is equivalent to  $\mathbf{E}(\mathbf{z}_i'u_{ig}) = \mathbf{0}$ ,  $g = 1, 2, \ldots, G$ . It follows that *any* linear combination of  $\mathbf{Z}_i$  is orthogonal to  $\mathbf{u}_i$ , including  $\mathbf{\Omega}^{-1}\mathbf{Z}_i$ . In this important special case, traditional 3SLS is a consistent estimator. In fact, as shown by Schmidt (1990), the GMM 3SLS estimator and the traditional 3SLS estimator are algebraically identical.

Because we will encounter cases where we need different instruments for different equations, the GMM definition of 3SLS in equation (8.36) is preferred: it is more generally valid, and it reduces to the standard definition in the traditional simultaneous equations setting.

# 8.4 Some Considerations When Choosing an Estimator

We have already discussed the assumptions under which the 3SLS estimator is an efficient GMM estimator. It follows that, under the assumptions of Theorem 8.4, 3SLS is as efficient asymptotically as the system 2SLS estimator. Nevertheless, it is useful to know that there are some situations where the system 2SLS and 3SLS estimators are equivalent. First, when the general system (8.11) is just identified, that is, L = K, all GMM estimators reduce to the instrumental variables estimator in equation (8.22). In the special (but still fairly general) case of the SUR system (8.12), the system is just identified if and only if each equation is just identified:  $L_g = K_g$ , g = 1, 2, ..., G and the rank condition holds for each equation. When each equation is just identified, the system IV estimator is IV equation by equation.

For the remaining discussion, we consider model (8.12) when at least one equation is overidentified. When  $\hat{\Omega}$  is a diagonal matrix, that is,  $\hat{\Omega} = \text{diag}(\hat{\sigma}_1^2, \dots, \hat{\sigma}_G^2)$ , 2SLS equation by equation is algebraically equivalent to 3SLS, regardless of the degree of overidentification (see Problem 8.7). Therefore, if we force our estimator  $\hat{\Omega}$  to be diagonal, we obtain 2SLS equation by equation.

The algebraic equivalance between system 2SLS and 3SLS when  $\hat{\Omega}$  is diagonal allows us to conclude that 2SLS and 3SLS are *asymptotically* equivalent if  $\hat{\Omega}$  is diagonal. The reason is simple. If we could use  $\hat{\Omega}$  in the 3SLS estimator, 3SLS would be identical to 2SLS. The actual 3SLS estimator, which uses  $\hat{\Omega}$ , is  $\sqrt{N}$ -equivalent to the hypothetical 3SLS estimator that uses  $\hat{\Omega}$ . Therefore, 3SLS and 2SLS are  $\sqrt{N}$ -equivalent.

Even in cases where the 2SLS estimator is not algebraically or asymptoically equivalent to 3SLS, it is not necessarily true that we should prefer 3SLS (or the minimum chi-square estimator more generally). Why? Suppose that primary interest

{212}------------------------------------------------

lies in estimating the parameters in the first equation,  $\beta_1$ . On the one hand, we know that 2SLS estimation of this equation produces consistent estimators under the orthogonality condition  $E(\mathbf{z}_1'u_1) = \mathbf{0}$  and the condition rank  $E(\mathbf{z}_1'\mathbf{x}_1) = K_1$ . We do not care what is happening elsewhere in the system as long as these two assumptions hold. On the other hand, the system-based 3SLS and minimum chi-square estimators of  $\beta_1$  are generally inconsistent unless  $E(\mathbf{z}_g'u_g) = \mathbf{0}$  for all g. Therefore, in using a system method to consistently estimate  $\beta_1$ , all equations in the system must be properly specified, which means their instruments must be exogenous. Such is the nature of system estimation procedures. As with system OLS and FGLS, there is a trade-off between robustness and efficiency.