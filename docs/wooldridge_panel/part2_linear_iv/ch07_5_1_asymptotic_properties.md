# Asymptotic Properties

> Pages: 170-173

Obtaining the GLS estimator  $\beta^*$  requires knowing  $\Omega$  up to scale. That is, we must be able to write  $\Omega = \sigma^2 \mathbf{C}$  where  $\mathbf{C}$  is a *known*  $G \times G$  positive definite matrix and  $\sigma^2$  is allowed to be an unknown constant. Sometimes  $\mathbf{C}$  is known (one case is  $\mathbf{C} = \mathbf{I}_G$ ), but much more often it is unknown. Therefore, we now turn to the analysis of feasible GLS (FGLS) estimation.

In FGLS estimation we replace the unknown matrix  $\Omega$  with a consistent estimator. Because the estimator of  $\Omega$  appears highly nonlinearly in the expression for the FGLS estimator, deriving finite sample properties of FGLS is generally difficult. [However, under essentially assumption (7.13) and some additional assumptions, including symmetry of the distribution of  $\mathbf{u}_i$ , Kakwani (1967) showed that the distribution of the FGLS is symmetric about  $\boldsymbol{\beta}$ , a property which means that the FGLS is unbiased *if* its expected value exists; see also Schmidt (1976, Section 2.5).] The asymptotic properties of the FGLS estimator are easily established as  $N \to \infty$  because, as we will show, its first-order asymptotic properties are *identical* to those of the GLS estimator under Assumptions SGLS.1 and SGLS.2. It is for this purpose that we spent some time on GLS. After establishing the asymptotic equivalence, we can easily obtain the limiting distribution of the FGLS estimator. Of course, GLS is trivially a special case of FGLS, where there is no first-stage estimation error.

We assume we have a consistent estimator,  $\hat{\Omega}$ , of  $\Omega$ :

$$\underset{N \to \infty}{\text{plim}} \ \hat{\mathbf{\Omega}} = \mathbf{\Omega} \tag{7.36}$$

[Because the dimension of  $\hat{\Omega}$  does not depend on N, equation (7.36) makes sense when defined element by element.] When  $\Omega$  is allowed to be a general positive definite matrix, the following estimation approach can be used. First, obtain the system OLS estimator of  $\beta$ , which we denote  $\hat{\beta}$  in this section to avoid confusion. We already showed that  $\hat{\beta}$  is consistent for  $\beta$  under Assumptions SOLS.1 and SOLS.2, and therefore under Assumptions SGLS.1 and SOLS.2 (In what follows, we assume that Assumptions SOLS.2 and SGLS.2 both hold.) By the WLLN,  $\min(N^{-1}\sum_{i=1}^{N}\mathbf{u}_i\mathbf{u}_i') = \Omega$ , and so a natural estimator of  $\Omega$  is

$$\hat{\mathbf{\Omega}} \equiv N^{-1} \sum_{i=1}^{N} \hat{\mathbf{u}}_{i} \hat{\mathbf{u}}_{i}^{\prime} \tag{7.37}$$


{171}------------------------------------------------

where  $\hat{\mathbf{u}}_i \equiv \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}}$  are the SOLS residuals. We can show that this estimator is consistent for  $\Omega$  under Assumptions SGLS.1 and SOLS.2 and standard moment conditions. First, write

$$\hat{\hat{\mathbf{u}}}_i = \mathbf{u}_i - \mathbf{X}_i (\hat{\hat{\boldsymbol{\beta}}} - \boldsymbol{\beta}) \tag{7.38}$$

so that

$$\hat{\mathbf{u}}_{i}\hat{\mathbf{u}}_{i}' = \mathbf{u}_{i}\mathbf{u}_{i}' - \mathbf{u}_{i}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})'\mathbf{X}_{i}' - \mathbf{X}_{i}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})\mathbf{u}_{i}' + \mathbf{X}_{i}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})'\mathbf{X}_{i}'$$

$$(7.39)$$

Therefore, it suffices to show that the averages of the last three terms converge in probability to zero. Write the average of the vec of the first term as  $N^{-1} \sum_{i=1}^{N} (\mathbf{X}_{i} \otimes \mathbf{u}_{i}) \cdot (\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})$ , which is  $o_{p}(1)$  because  $p\lim(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \mathbf{0}$  and  $N^{-1} \sum_{i=1}^{N} (\mathbf{X}_{i} \otimes \mathbf{u}_{i}) \stackrel{p}{\to} \mathbf{0}$ . The third term is the transpose of the second. For the last term in equation (7.39), note that the average of its vec can be written as

$$N^{-1} \sum_{i=1}^{N} (\mathbf{X}_{i} \otimes \mathbf{X}_{i}) \cdot \text{vec}\{(\hat{\hat{\boldsymbol{\beta}}} - \boldsymbol{\beta})(\hat{\hat{\boldsymbol{\beta}}} - \boldsymbol{\beta})'\}$$

$$(7.40)$$

Now  $\text{vec}\{(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})'\} = o_p(1)$ . Further, assuming that each element of  $\mathbf{X}_i$  has finite second moment,  $N^{-1} \sum_{i=1}^{N} (\mathbf{X}_i \otimes \mathbf{X}_i) = O_p(1)$  by the WLLN. This step takes care of the last term, since  $O_p(1) \cdot o_p(1) = o_p(1)$ . We have shown that

$$\hat{\mathbf{\Omega}} = N^{-1} \sum_{i=1}^{N} \mathbf{u}_i \mathbf{u}_i' + o_p(1)$$
(7.41)

and so equation (7.36) follows immediately. [In fact, a more careful analysis shows that the  $o_p(1)$  in equation (7.41) can be replaced by  $o_p(N^{-1/2})$ ; see Problem 7.4.]

Sometimes the elements of  $\Omega$  are restricted in some way (an important example is the random effects panel data model that we will cover in Chapter 10). In such cases a different estimator of  $\Omega$  is often used that exploits these restrictions. As with  $\hat{\Omega}$  in equation (7.37), such estimators typically use the system OLS residuals in some fashion and lead to consistent estimators assuming the structure of  $\Omega$  is correctly specified. The advantage of equation (7.37) is that it is consistent for  $\Omega$  quite generally. However, if N is not very large relative to G, equation (7.37) can have poor finite sample properties.

Given  $\hat{\Omega}$ , the feasible GLS (FGLS) estimator of  $\beta$  is

$$\hat{\boldsymbol{\beta}} = \left(\sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{X}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{y}_{i}\right)$$
(7.42)

or, in full matrix notation,  $\hat{\beta} = [\mathbf{X}'(\mathbf{I}_N \otimes \hat{\mathbf{\Omega}}^{-1})\mathbf{X}]^{-1}[\mathbf{X}'(\mathbf{I}_N \otimes \hat{\mathbf{\Omega}}^{-1})\mathbf{Y}].$ 

{172}------------------------------------------------

We have already shown that the (infeasible) GLS estimator is consistent under Assumptions SGLS.1 and SGLS.2. Because  $\hat{\Omega}$  converges to  $\Omega$ , it is not surprising that FGLS is also consistent. Rather than show this result separately, we verify the stronger result that FGLS has the same limiting distribution as GLS.

The limiting distribution of FGLS is obtained by writing

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\boldsymbol{\Omega}}^{-1} \mathbf{X}_{i}\right)^{-1} \left(N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\boldsymbol{\Omega}}^{-1} \mathbf{u}_{i}\right)$$
(7.43)

Now

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{u}_{i} - N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{u}_{i} = \left[ N^{-1/2} \sum_{i=1}^{N} (\mathbf{u}_{i} \otimes \mathbf{X}_{i})' \right] \operatorname{vec}(\hat{\mathbf{\Omega}}^{-1} - \mathbf{\Omega}^{-1})$$

Under Assumption SGLS.1, the CLT implies that  $N^{-1/2} \sum_{i=1}^{N} (\mathbf{u}_i \otimes \mathbf{X}_i) = O_p(1)$ . Because  $O_p(1) \cdot o_p(1) = o_p(1)$ , it follows that

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{u}_{i} = N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{u}_{i} + o_{p}(1)$$

A similar argument shows that  $N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{X}_{i} = N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{X}_{i} + o_{p}(1)$ . Therefore, we have shown that

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{X}_{i}\right)^{-1} \left(N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{u}_{i}\right) + o_{p}(1)$$
(7.44)

The first term in equation (7.44) is just  $\sqrt{N}(\beta^* - \beta)$ , where  $\beta^*$  is the GLS estimator. We can write equation (7.44) as

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}^*) = o_p(1) \tag{7.45}$$

which shows that  $\hat{\beta}$  and  $\beta^*$  are  $\sqrt{N}$ -equivalent. Recall from Chapter 3 that this statement is much stronger than simply saying that  $\beta^*$  and  $\hat{\beta}$  are both consistent for  $\beta$ . There are many estimators, such as system OLS, that are consistent for  $\beta$  but are not  $\sqrt{N}$ -equivalent to  $\beta^*$ .

The asymptotic equivalence of  $\hat{\beta}$  and  $\hat{\beta}^*$  has practically important consequences. The most important of these is that, for performing asymptotic inference about  $\hat{\beta}$  using  $\hat{\beta}$ , we do not have to worry that  $\hat{\Omega}$  is an estimator of  $\Omega$ . Of course, whether the asymptotic approximation gives a reasonable approximation to the actual distribution of  $\hat{\beta}$  is difficult to tell. With large N, the approximation is usually pretty good.

{173}------------------------------------------------

But if N is small relative to G, ignoring estimation of  $\Omega$  in performing inference about  $\beta$  can be misleading.

We summarize the limiting distribution of FGLS with a theorem.

THEOREM 7.3 (Asymptotic Normality of FGLS): Under Assumptions SGLS.1 and SGLS.2,

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \stackrel{a}{\sim} \text{Normal}(\mathbf{0}, \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-1})$$
 (7.46)

where  $\bf A$  is defined in equation (7.31) and  $\bf B$  is defined in equation (7.33).

In the FGLS context a consistent estimator of A is

$$\hat{\mathbf{A}} \equiv N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{X}_{i}$$
(7.47)

A consistent estimator of  $\bf B$  is also readily available after FGLS estimation. Define the FGLS residuals by

$$\hat{\mathbf{u}}_i \equiv \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}}, \qquad i = 1, 2, \dots, N \tag{7.48}$$

[The only difference between the FGLS and SOLS residuals is that the FGLS estimator is inserted in place of the SOLS estimator; in particular, the FGLS residuals are *not* from the transformed equation (7.28).] Using standard arguments, a consistent estimator of **B** is

$$\hat{\mathbf{B}} \equiv N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{\Omega}}^{-1} \hat{\mathbf{u}}_{i} \hat{\mathbf{u}}_{i}' \hat{\mathbf{\Omega}}^{-1} \mathbf{X}_{i}$$

The estimator of  $Avar(\hat{\beta})$  can be written as

$$\hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1}/N = \left(\sum_{i=1}^{N} \mathbf{X}_{i}'\hat{\mathbf{\Omega}}^{-1}\mathbf{X}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \mathbf{X}_{i}'\hat{\mathbf{\Omega}}^{-1}\hat{\mathbf{u}}_{i}\hat{\mathbf{u}}_{i}'\hat{\mathbf{\Omega}}^{-1}\mathbf{X}_{i}\right) \left(\sum_{i=1}^{N} \mathbf{X}_{i}'\hat{\mathbf{\Omega}}^{-1}\mathbf{X}_{i}\right)^{-1}$$
(7.49)

This is the extension of the White (1980b) heteroskedasticity-robust asymptotic variance estimator to the case of systems of equations; see also White (1984). This estimator is valid under Assumptions SGLS.1 and SGLS.2; that is, it is completely robust.