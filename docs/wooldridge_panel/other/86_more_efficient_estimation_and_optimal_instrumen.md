# **8.6** More Efficient Estimation and Optimal Instruments

> Pages: 215-222

In Section 8.3.3 we characterized the optimal weighting matrix given the matrix  $\mathbf{Z}_i$  of instruments. But this discussion begs the question of how we can best choose  $\mathbf{Z}_i$ . In this section we briefly discuss two efficiency results. The first has to do with adding valid instruments.

To be precise, let  $\mathbf{Z}_{i1}$  be a  $G \times L_1$  submatrix of the  $G \times L$  matrix  $\mathbf{Z}_i$ , where  $\mathbf{Z}_i$  satisfies Assumptions SIV.1 and SIV.2. We also assume that  $\mathbf{Z}_{i1}$  satisfies Assumption SIV.2; that is,  $\mathrm{E}(\mathbf{Z}'_{i1}\mathbf{X}_i)$  has rank K. This assumption ensures that  $\boldsymbol{\beta}$  is identified using the smaller set of instruments. (Necessary is  $L_1 \geq K$ .) Given  $\mathbf{Z}_{i1}$ , we know that the efficient GMM estimator uses a weighting matrix that is consistent for  $\boldsymbol{\Lambda}_1^{-1}$ , where  $\boldsymbol{\Lambda}_1 = \mathrm{E}(\mathbf{Z}'_{i1}\mathbf{u}_i\mathbf{u}'_i\mathbf{Z}_{i1})$ . When we use the full set of instruments  $\mathbf{Z}_i = (\mathbf{Z}_{i1}, \mathbf{Z}_{i2})$ , the optimal weighting matrix is a consistent estimator of  $\boldsymbol{\Lambda}$  given in expression (8.26). The question is, Can we say that using the full set of instruments (with the optimal weighting matrix) is better than using the reduced set of instruments (with the optimal weighting matrix)? The answer is that, asymptotically, we can do no worse, and often we can do better, using a larger set of valid instruments.

The proof that adding orthogonality conditions generally improves efficiency proceeds by comparing the asymptotic variances of  $\sqrt{N}(\tilde{\pmb{\beta}}-\pmb{\beta})$  and  $\sqrt{N}(\hat{\pmb{\beta}}-\pmb{\beta})$ , where the former estimator uses the restricted set of IVs and the latter uses the full set. Then

Avar 
$$\sqrt{N}(\tilde{\boldsymbol{\beta}} - \boldsymbol{\beta})$$
 - Avar  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = (\mathbf{C}_1' \boldsymbol{\Lambda}_1^{-1} \mathbf{C}_1)^{-1} - (\mathbf{C}' \boldsymbol{\Lambda}^{-1} \mathbf{C})^{-1}$  (8.51)

where  $\mathbf{C}_1 = \mathrm{E}(\mathbf{Z}_{i1}'\mathbf{X}_i)$ . The difference in equation (8.51) is positive semidefinite if and only if  $\mathbf{C}'\mathbf{\Lambda}^{-1}\mathbf{C} - \mathbf{C}_1'\mathbf{\Lambda}_1^{-1}\mathbf{C}_1$  is p.s.d. The latter result is shown by White (1984, Proposition 4.49) using the formula for partitioned inverse; we will not reproduce it here.

The previous argument shows that we can never do worse asymptotically by adding instruments and computing the minimum chi-square estimator. But we need not always do better. The proof in White (1984) shows that the asymptotic variances of  $\tilde{\beta}$  and  $\hat{\beta}$  are identical if and only if

$$\mathbf{C}_2 = \mathrm{E}(\mathbf{Z}'_{i2}\mathbf{u}_i\mathbf{u}'_i\mathbf{Z}_{i1})\mathbf{\Lambda}_1^{-1}\mathbf{C}_1 \tag{8.52}$$

{216}------------------------------------------------

where  $\mathbf{C}_2 = \mathrm{E}(\mathbf{Z}_{i2}'\mathbf{X}_i)$ . Generally, this condition is difficult to check. However, if we assume that  $\mathrm{E}(\mathbf{Z}_i'\mathbf{u}_i\mathbf{u}_i'\mathbf{Z}_i) = \sigma^2\mathrm{E}(\mathbf{Z}_i'\mathbf{Z}_i)$ —the ideal assumption for system 2SLS—then condition (8.52) becomes

$$E(\mathbf{Z}_{i2}'\mathbf{X}_i) = E(\mathbf{Z}_{i2}'\mathbf{Z}_{i1})[E(\mathbf{Z}_{i1}'\mathbf{Z}_{i1})]^{-1}E(\mathbf{Z}_{i1}'\mathbf{X}_i)$$

Straightforward algebra shows that this condition is equivalent to

$$E[(\mathbf{Z}_{i2} - \mathbf{Z}_{i1}\mathbf{D}_1)'\mathbf{X}_i] = \mathbf{0}$$
(8.53)

where  $\mathbf{D}_1 = [\mathrm{E}(\mathbf{Z}'_{i1}\mathbf{Z}_{i1})]^{-1}\mathrm{E}(\mathbf{Z}'_{i1}\mathbf{Z}_{i2})$  is the  $L_1 \times L_2$  matrix of coefficients from the population regression of  $\mathbf{Z}_{i1}$  on  $\mathbf{Z}_{i2}$ . Therefore, condition (8.53) has a simple interpretation:  $\mathbf{X}_i$  is orthogonal to the part of  $\mathbf{Z}_{i2}$  that is left after netting out  $\mathbf{Z}_{i1}$ . This statement means that  $\mathbf{Z}_{i2}$  is not *partially* correlated with  $\mathbf{X}_i$ , and so it is not useful as instruments once  $\mathbf{Z}_{i1}$  has been included.

Condition (8.53) is very intuitive in the context of 2SLS estimation of a single equation. Under  $E(u_i^2 \mathbf{z}_i' \mathbf{z}_i) = \sigma^2 E(\mathbf{z}_i' \mathbf{z}_i)$ , 2SLS is the minimum chi-square estimator. The elements of  $\mathbf{z}_i$  would include all exogenous elements of  $\mathbf{x}_i$ , and then some. If, say,  $x_{iK}$  is the only endogenous element of  $\mathbf{x}_i$ , condition (8.53) becomes

$$L(x_{iK} | \mathbf{z}_{i1}, \mathbf{z}_{i2}) = L(x_{iK} | \mathbf{z}_{i1})$$
(8.54)

so that the linear projection of  $x_{iK}$  onto  $\mathbf{z}_i$  depends only on  $\mathbf{z}_{i1}$ . If you recall how the IVs for 2SLS are obtained—by estimating the linear projection of  $x_{iK}$  on  $\mathbf{z}_i$  in the first stage—it makes perfectly good sense that  $\mathbf{z}_{i2}$  can be omitted under condition (8.54) without affecting efficiency of 2SLS.

In the general case, if the error vector  $\mathbf{u}_i$  contains conditional heteroskedasticity, or correlation across its elements (conditional or otherwise), condition (8.52) is unlikely to be true. As a result, we can keep improving asymptotic efficiency by adding more valid instruments. Whenever the error term satisfies a zero conditional mean assumption, unlimited IVs are available. For example, consider the linear model  $E(y | \mathbf{x}) = \mathbf{x}\boldsymbol{\beta}$ , so that the error  $u = y - \mathbf{x}\boldsymbol{\beta}$  has a zero mean given  $\mathbf{x}$ . The OLS estimator is the IV estimator using IVs  $\mathbf{z}_1 = \mathbf{x}$ . The preceding efficiency result implies that, if  $Var(u | \mathbf{x}) \neq Var(u)$ , there are unlimited minimum chi-square estimators that are asymptotically more efficient than OLS. Because  $E(u | \mathbf{x}) = 0$ ,  $\mathbf{h}(\mathbf{x})$  is a valid set of IVs for any vector function  $\mathbf{h}(\cdot)$ . (Assuming, as always, that the appropriate moments exist.) Then, the minimum chi-square estimate using IVs  $\mathbf{z} = [\mathbf{x}, \mathbf{h}(\mathbf{x})]$  is generally more asymptotically efficient than OLS. (Chamberlain, 1982, and Cragg, 1983, independently obtained this result.) If  $Var(y | \mathbf{x})$  is constant, adding functions of  $\mathbf{x}$  to the IV list results in no asymptotic improvement because the linear projection of  $\mathbf{x}$  onto  $\mathbf{x}$  and  $\mathbf{h}(\mathbf{x})$  obviously does not depend on  $\mathbf{h}(\mathbf{x})$ .

{217}------------------------------------------------

Under homoskedasticity, adding moment conditions does not reduce the asymptotic efficiency of the minimum chi-square estimator. Therefore, it may seem that, when we have a linear model that represents a conditional expectation, we cannot lose by adding IVs and performing minimum chi-square. [Plus, we can then test the functional form  $E(y | \mathbf{x}) = \mathbf{x}\boldsymbol{\beta}$  by testing the overidentifying restrictions.] Unfortunately, as shown by several authors, including Tauchen (1986), Altonji and Segal (1996), and Ziliak (1997), GMM estimators that use many overidentifying restrictions can have very poor finite sample properties.

The previous discussion raises the following possibility: rather than adding more and more orthogonality conditions to improve on inefficient estimators, can we find a small set of optimal IVs? The answer is yes, provided we replace Assumption SIV.1 with a zero conditional mean assumption.

ASSUMPTION SIV.1':  $E(u_{iq} | \mathbf{z}_i) = 0, g = 1, ..., G$  for some vector  $\mathbf{z}_i$ .

Assumption SIV.1' implies that  $\mathbf{z}_i$  is exogenous in *every* equation, and each element of the instrument matrix  $\mathbf{Z}_i$  can be *any* function of  $\mathbf{z}_i$ .

THEOREM 8.5 (Optimal Instruments): Under Assumption SIV.1' (and sufficient regularity conditions), the optimal choice of instruments is  $\mathbf{Z}_i^* = \mathbf{\Omega}(\mathbf{z}_i)^{-1} \mathrm{E}(\mathbf{X}_i \,|\, \mathbf{z}_i)$ , where  $\mathbf{\Omega}(\mathbf{z}_i) \equiv \mathrm{E}(\mathbf{u}_i'\mathbf{u}_i \,|\, \mathbf{z}_i)$ , provided that rank  $\mathrm{E}(\mathbf{Z}_i^{*'}\mathbf{X}_i) = K$ .

We will not prove Theorem 8.5 here. We discuss a more general case in Section 14.5; see also Newey and McFadden (1994, Section 5.4). Theorem 8.5 implies that, if the  $G \times K$  matrix  $\mathbf{Z}_i^*$  were available, we would use it in equation (8.22) in place of  $\mathbf{Z}_i$  to obtain the SIV estimator with the smallest asymptotic variance. This would take the arbitrariness out of choosing additional functions of  $\mathbf{z}_i$  to add to the IV list: once we have  $\mathbf{Z}_i^*$ , all other functions of  $\mathbf{z}_i$  are redundant.

Theorem 8.5 implies that, if the errors in the system satisfy SIV.1', the homoskedasticity assumption (8.37), and  $E(\mathbf{X}_i | \mathbf{z}_i) = \mathbf{Z}_i \mathbf{\Pi}$  for some  $G \times L$  matrix  $\mathbf{Z}_i$  and an  $L \times K$  unknown matrix  $\mathbf{\Pi}$ , then the 3SLS estimator is the efficient estimator based on the orthogonality conditions SIV.1'. Showing this result is easy given the traditional form of the 3SLS estimator in equation (8.41).

If  $E(\mathbf{u}_i | \mathbf{X}_i) = \mathbf{0}$  and  $E(\mathbf{u}_i \mathbf{u}_i' | \mathbf{X}_i) = \mathbf{\Omega}$ , then the optimal instruments are  $\mathbf{\Omega}^{-1} \mathbf{X}_i$ , which gives the GLS estimator. Replacing  $\mathbf{\Omega}$  by  $\hat{\mathbf{\Omega}}$  has no effect asymptotically, and so the FGLS is the SIV estimator with optimal choice of instruments.

Without further assumptions, both  $\Omega(\mathbf{z}_i)$  and  $\mathrm{E}(\mathbf{X}_i | \mathbf{z}_i)$  can be arbitrary functions of  $\mathbf{z}_i$ , in which case the optimal SIV estimator is not easily obtainable. It is possible to find an estimator that is asymptotically efficient using *nonparametric* estimation

{218}------------------------------------------------

methods to estimate  $\Omega(\mathbf{z}_i)$  and  $E(\mathbf{X}_i | \mathbf{z}_i)$ , but there are many practical hurdles to overcome in applying such procedures. See Newey (1990) for an approach that approximates  $E(\mathbf{X}_i | \mathbf{z}_i)$  by parametric functional forms, where the approximation gets better as the sample size grows.

#### **Problems**

**8.1.** Show that the GMM estimator that solves the problem (8.23) satisfies the first-order condition

$$\left(\sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{X}_{i}\right)' \hat{\mathbf{W}} \left(\sum_{i=1}^{N} \mathbf{Z}_{i}' (\mathbf{y}_{i} - \mathbf{X}_{i} \hat{\boldsymbol{\beta}})\right) = \mathbf{0}$$

Use this expression to obtain formula (8.24).

**8.2.** Consider the system of equations

$$\mathbf{y}_i = \mathbf{X}_i \boldsymbol{\beta} + \mathbf{u}_i$$

where *i* indexes the cross section observation,  $\mathbf{y}_i$  and  $\mathbf{u}_i$  are  $G \times 1$ ,  $\mathbf{X}_i$  is  $G \times K$ ,  $\mathbf{Z}_i$  is the  $G \times L$  matrix of instruments, and  $\boldsymbol{\beta}$  is  $K \times 1$ . Let  $\mathbf{\Omega} = \mathrm{E}(\mathbf{u}_i \mathbf{u}_i')$ . Make the following four assumptions: (1)  $\mathrm{E}(\mathbf{Z}_i'\mathbf{u}_i) = \mathbf{0}$ ; (2) rank  $\mathrm{E}(\mathbf{Z}_i'\mathbf{X}_i) = K$ ; (3)  $\mathrm{E}(\mathbf{Z}_i'\mathbf{Z}_i)$  is nonsingular; and (4)  $\mathrm{E}(\mathbf{Z}_i'\mathbf{\Omega}_i)$  is nonsingular.

- a. What are the properties of the 3SLS estimator?
- b. Find the asymptotic variance matrix of  $\sqrt{N}(\hat{\beta}_{3SLS} \beta)$ .
- c. How would you estimate Avar( $\hat{\beta}_{3SLS}$ )?
- **8.3.** Let  $\mathbf{x}$  be a  $1 \times K$  random vector and let  $\mathbf{z}$  be a  $1 \times M$  random vector. Suppose that  $\mathbf{E}(\mathbf{x} \mid \mathbf{z}) = \mathbf{L}(\mathbf{x} \mid \mathbf{z}) = \mathbf{z} \mathbf{\Pi}$ , where  $\mathbf{\Pi}$  is an  $M \times K$  matrix; in other words, the expectation of  $\mathbf{x}$  given  $\mathbf{z}$  is linear in  $\mathbf{z}$ . Let  $\mathbf{h}(\mathbf{z})$  be any  $1 \times Q$  nonlinear function of  $\mathbf{z}$ , and define an expanded instrument list as  $\mathbf{w} = [\mathbf{z}, \mathbf{h}(\mathbf{z})]$ .

Show that rank  $E(\mathbf{z}'\mathbf{x}) = \operatorname{rank} E(\mathbf{w}'\mathbf{x})$ . {Hint: First show that rank  $E(\mathbf{z}'\mathbf{x}) = \operatorname{rank} E(\mathbf{z}'\mathbf{x}^*)$ , where  $\mathbf{x}^*$  is the linear projection of  $\mathbf{x}$  onto  $\mathbf{z}$ ; the same holds with  $\mathbf{z}$  replaced by  $\mathbf{w}$ . Next, show that when  $E(\mathbf{x} \mid \mathbf{z}) = L(\mathbf{x} \mid \mathbf{z})$ ,  $L[\mathbf{x} \mid \mathbf{z}, \mathbf{h}(\mathbf{z})] = L(\mathbf{x} \mid \mathbf{z})$  for any function  $\mathbf{h}(\mathbf{z})$  of  $\mathbf{z}$ .}

**8.4.** Consider the system of equations (8.12), and let  $\mathbf{z}$  be a row vector of variables exogenous in every equation. Assume that the exogeneity assumption takes the stronger form  $\mathrm{E}(u_g \mid \mathbf{z}) = 0, \ g = 1, 2, \ldots, G$ . This assumption means that  $\mathbf{z}$  and nonlinear functions of  $\mathbf{z}$  are valid instruments in every equation.

{219}------------------------------------------------

a. Suppose that  $E(\mathbf{x}_g \mid \mathbf{z})$  is linear in  $\mathbf{z}$  for all g. Show that adding nonlinear functions of  $\mathbf{z}$  to the instrument list cannot help in satisfying the rank condition. (Hint: Apply Problem 8.3.)

- b. What happens if  $E(\mathbf{x}_q | \mathbf{z})$  is a nonlinear function of  $\mathbf{z}$  for some g?
- **8.5.** Verify that the difference  $(\mathbf{C}'\Lambda^{-1}\mathbf{C}) (\mathbf{C}'\mathbf{W}\mathbf{C})(\mathbf{C}'\mathbf{W}\Lambda\mathbf{W}\mathbf{C})^{-1}(\mathbf{C}'\mathbf{W}\mathbf{C})$  in expression (8.30) is positive semidefinite for any symmetric positive definite matrices  $\mathbf{W}$  and  $\mathbf{\Lambda}$ . {Hint: Show that the difference can be expressed as

$$\mathbf{C}' \mathbf{\Lambda}^{-1/2} [\mathbf{I}_L - \mathbf{D} (\mathbf{D}' \mathbf{D})^{-1} \mathbf{D}'] \mathbf{\Lambda}^{-1/2} \mathbf{C}$$

where  $\mathbf{D} \equiv \mathbf{\Lambda}^{1/2}\mathbf{WC}$ . Then, note that for any  $L \times K$  matrix  $\mathbf{D}$ ,  $\mathbf{I}_L - \mathbf{D}(\mathbf{D}'\mathbf{D})^{-1}\mathbf{D}'$  is a symmetric, idempotent matrix, and therefore positive semidefinite.}

**8.6.** Consider the system (8.12) in the G = 2 case, with an i subscript added:

$$y_{i1} = \mathbf{x}_{i1}\boldsymbol{\beta}_1 + u_{i1}$$

$$y_{i2} = \mathbf{x}_{i2}\boldsymbol{\beta}_2 + u_{i2}$$

The instrument matrix is

$$\mathbf{Z}_i = \begin{pmatrix} \mathbf{z}_{i1} & \mathbf{0} \\ \mathbf{0} & \mathbf{z}_{i2} \end{pmatrix}$$

Let  $\Omega$  be the 2 × 2 variance matrix of  $\mathbf{u}_i \equiv (u_{i1}, u_{i2})'$ , and write

$$\mathbf{\Omega}^{-1} = \begin{pmatrix} \sigma^{11} & \sigma^{12} \\ \sigma^{12} & \sigma^{22} \end{pmatrix}$$

- a. Find  $E(\mathbf{Z}_i'\mathbf{\Omega}^{-1}\mathbf{u}_i)$  and show that it is not necessarily zero under the orthogonality conditions  $E(\mathbf{z}_{i1}'u_{i1}) = \mathbf{0}$  and  $E(\mathbf{z}_{i2}'u_{i2}) = \mathbf{0}$ .
- b. What happens if  $\Omega$  is diagonal (so that  $\Omega^{-1}$  is diagonal)?
- c. What if  $\mathbf{z}_{i1} = \mathbf{z}_{i2}$  (without restrictions on  $\mathbf{\Omega}$ )?
- **8.7.** With definitions (8.14) and (8.15), show that system 2SLS and 3SLS are numerically identical whenever  $\hat{\Omega}$  is a diagonal matrix.
- **8.8.** Consider the standard panel data model introduced in Chapter 7:

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + u_{it} \tag{8.55}$$

where the  $1 \times K$  vector  $\mathbf{x}_{it}$  might have some elements correlated with  $u_{it}$ . Let  $\mathbf{z}_{it}$  be a  $1 \times L$  vector of instruments,  $L \ge K$ , such that  $\mathbf{E}(\mathbf{z}'_{it}u_{it}) = \mathbf{0}$ , t = 1, 2, ..., T. (In prac-

{220}------------------------------------------------

tice,  $\mathbf{z}_{it}$  would contain some elements of  $\mathbf{x}_{it}$ , including a constant and possibly time dummies.)

- a. Write down the system 2SLS estimator if the instrument matrix is  $\mathbf{Z}_i = (\mathbf{z}'_{i1}, \mathbf{z}'_{i2}, \dots, \mathbf{z}'_{iT})'$  (a  $T \times L$  matrix). Show that this estimator is a pooled 2SLS estimator. That is, it is the estimator obtained by 2SLS estimation of equation (8.55) using instruments  $\mathbf{z}_{it}$ , pooled across all i and t.
- b. What is the rank condition for the pooled 2SLS estimator?
- c. Without further assumptions, show how to estimate the asymptotic variance of the pooled 2SLS estimator.
- d. Show that the assumptions

$$E(u_{it} | \mathbf{z}_{it}, u_{i,t-1}, \mathbf{z}_{i,t-1}, \dots, u_{i1}, \mathbf{z}_{i1}) = 0, \qquad t = 1, \dots, T$$
(8.56)

$$E(u_{it}^2 | \mathbf{z}_{it}) = \sigma^2, \qquad t = 1, ..., T$$
 (8.57)

imply that the usual standard errors and test statistics reported from the pooled 2SLS estimation are valid. These assumptions make implementing 2SLS for panel data very simple.

- e. What estimator would you use under condition (8.56) but where we relax condition (8.57) to  $E(u_{it}^2 | \mathbf{z}_{it}) = E(u_{it}^2) \equiv \sigma_t^2$ , t = 1, ..., T? This approach will involve an initial pooled 2SLS estimation.
- **8.9.** Consider the single-equation linear model from Chapter 5:  $y = x\beta + u$ . Strengthen Assumption 2SLS.1 to  $E(u \mid z) = 0$  and Assumption 2SLS.3 to  $E(u^2 \mid z) = \sigma^2$ , and keep the rank condition 2SLS.2. Show that if  $E(x \mid z) = z\Pi$  for some  $L \times K$  matrix  $\Pi$ , the 2SLS estimator uses the optimal instruments based on the orthogonality condition  $E(u \mid z) = 0$ . What does this result imply about OLS if  $E(u \mid x) = 0$  and  $Var(u \mid x) = \sigma^2$ ?
- **8.10.** In the model from Problem 8.8, let  $\hat{u}_{it} \equiv y_{it} \mathbf{x}_{it}\hat{\boldsymbol{\beta}}$  be the residuals after pooled 2SLS estimation.
- a. Consider the following test for AR(1) serial correlation in  $\{u_{it}: t = 1, ..., T\}$ : estimate the auxiliary equation

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + \rho \hat{\boldsymbol{u}}_{i,t-1} + error_{it}, \qquad t = 2, \dots, T, \ i = 1, \dots, N$$

by 2SLS using instruments  $(\mathbf{z}_{it}, \hat{u}_{i,t-1})$ , and use the t statistic on  $\hat{\rho}$ . Argue that, if we strengthen (8.56) to  $\mathrm{E}(u_{it} | \mathbf{z}_{it}, \mathbf{x}_{i,t-1}, u_{i,t-1}, \mathbf{z}_{i,t-1}, \mathbf{x}_{i,t-2}, \dots, \mathbf{x}_{i1}, u_{i1}, \mathbf{z}_{i1}) = 0$ , then the heteroskedasticity-robust t statistic for  $\hat{\rho}$  is asymptotically valid as a test for serial correlation. [Hint: Under the dynamic completeness assumption (8.56), which is


{221}------------------------------------------------

effectively the null hypothesis, the fact that u^<sup>i</sup>;t<sup>1</sup> is used in place of ui;t<sup>1</sup> does not affect the limiting distribution of r^; see Section 6.1.3.] What is the homoskedasticity assumption that justifies the usual t statistic?

- b. What should be done to obtain a heteroskedasticity-robust test?
- 8.11. a. Use Theorem 8.5 to show that, in the single-equation model

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1$$

with Eðu<sup>1</sup> j zÞ ¼ 0—where z<sup>1</sup> is a strict subset of z—and Varðu<sup>1</sup> j zÞ ¼ s<sup>2</sup> <sup>1</sup> , the optimal instrumental variables are ½z1; Eðy<sup>2</sup> j zÞ.

b. If y<sup>2</sup> is a binary variable with Pðy<sup>2</sup> ¼ 1 j zÞ ¼ FðzÞ for some known function Fð-Þ, 0aFðzÞ a1, what are the optimal IVs?

{222}------------------------------------------------