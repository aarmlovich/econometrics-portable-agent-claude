# Consistency

> Pages: 68-74

As discussed in Section 4.1, the key assumption for OLS to consistently estimate *b* is the population orthogonality condition:

ASSUMPTION OLS.1: 
$$E(\mathbf{x}'u) = \mathbf{0}$$
.

Because x contains a constant, Assumption OLS.1 is equivalent to saying that u has mean zero and is uncorrelated with each regressor, which is how we will refer to Assumption OLS.1. Sufficient for Assumption OLS.1 is the zero conditional mean assumption (4.3).

The other assumption needed for consistency of OLS is that the expected outer product matrix of x has full rank, so that there are no exact linear relationships among the regressors in the population. This is stated succinctly as follows:

ASSUMPTION OLS.2: rank 
$$E(\mathbf{x}'\mathbf{x}) = K$$
.

As with Assumption OLS.1, Assumption OLS.2 is an assumption about the population. Since Eðx<sup>0</sup> xÞ is a symmetric K K matrix, Assumption OLS.2 is equivalent to assuming that Eðx<sup>0</sup> xÞ is positive definite. Since x<sup>1</sup> ¼ 1, Assumption OLS.2 is also equivalent to saying that the (population) variance matrix of the K 1 nonconstant elements in x is nonsingular. This is a standard assumption, which fails if and only if at least one of the regressors can be written as a linear function of the other regressors (in the population). Usually Assumption OLS.2 holds, but it can fail if the population model is improperly specified [for example, if we include too many dummy variables in x or mistakenly use something like logðageÞ and logðage<sup>2</sup>Þ in the same equation].

Under Assumptions OLS.1 and OLS.2, the parameter vector *b* is identified. In the context of models that are linear in the parameters under random sampling, identi

{69}------------------------------------------------

fication of  $\beta$  simply means that  $\beta$  can be written in terms of population moments in observable variables. (Later, when we consider nonlinear models, the notion of identification will have to be more general. Also, special issues arise if we cannot obtain a random sample from the population, something we treat in Chapter 17.) To see that  $\beta$  is identified under Assumptions OLS.1 and OLS.2, premultiply equation (4.5) by  $\mathbf{x}'$ , take expectations, and solve to get

$$\boldsymbol{\beta} = [\mathbf{E}(\mathbf{x}'\mathbf{x})]^{-1}\mathbf{E}(\mathbf{x}'y)$$

Because  $(\mathbf{x}, y)$  is observed,  $\boldsymbol{\beta}$  is identified. The **analogy principle** for choosing an estimator says to turn the population problem into its sample counterpart (see Goldberger, 1968; Manski, 1988). In the current application this step leads to the **method of moments**: replace the population moments  $E(\mathbf{x}'\mathbf{x})$  and  $E(\mathbf{x}'y)$  with the corresponding sample averages. Doing so leads to the OLS estimator:

$$\hat{\beta} = \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{x}_{i} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' y_{i} \right) = \beta + \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{x}_{i} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' u_{i} \right)$$

which can be written in full matrix form as  $(\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}$ , where  $\mathbf{X}$  is the  $N \times K$  data matrix of regressors with ith row  $\mathbf{x}_i$  and  $\mathbf{Y}$  is the  $N \times 1$  data vector with ith element  $y_i$ . Under Assumption OLS.2,  $\mathbf{X}'\mathbf{X}$  is nonsingular with probability approaching one and  $\text{plim}[(N^{-1}\sum_{i=1}^{N}\mathbf{x}_i'\mathbf{x}_i)^{-1}] = \mathbf{A}^{-1}$ , where  $\mathbf{A} \equiv \mathbf{E}(\mathbf{x}'\mathbf{x})$  (see Corollary 3.1). Further, under Assumption OLS.1,  $\text{plim}(N^{-1}\sum_{i=1}^{N}\mathbf{x}_i'u_i) = \mathbf{E}(\mathbf{x}'u) = \mathbf{0}$ . Therefore, by Slutsky's theorem (Lemma 3.4),  $\text{plim } \hat{\boldsymbol{\beta}} = \boldsymbol{\beta} + \mathbf{A}^{-1} \cdot \mathbf{0} = \boldsymbol{\beta}$ . We summarize with a theorem:

THEOREM 4.1 (Consistency of OLS): Under Assumptions OLS.1 and OLS.2, the OLS estimator  $\hat{\beta}$  obtained from a random sample following the population model (4.5) is consistent for  $\beta$ .

The simplicity of the proof of Theorem 4.1 should not undermine its usefulness. Whenever an equation can be put into the form (4.5) and Assumptions OLS.1 and OLS.2 hold, OLS using a random sample consistently estimates  $\beta$ . It does not matter where this equation comes from, or what the  $\beta_j$  actually represent. As we will see in Sections 4.3 and 4.4, often an estimable equation is obtained only after manipulating an underlying structural equation. An important point to remember is that, once the linear (in parameters) equation has been specified with an additive error and Assumptions OLS.1 and OLS.2 are verified, there is no need to reprove Theorem 4.1.

Under the assumptions of Theorem 4.1,  $x\beta$  is the linear projection of y on x. Thus, Theorem 4.1 shows that OLS consistently estimates the parameters in a linear projection, subject to the rank condition in Assumption OLS.2. This is very general, as it places no restrictions on the nature of y—for example, y could be a binary variable

{70}------------------------------------------------

or some other variable with discrete characteristics. Since a conditional expectation that is linear in parameters is also the linear projection, Theorem 4.1 also shows that OLS consistently estimates conditional expectations that are linear in parameters. We will use this fact often in later sections.

There are a few final points worth emphasizing. First, if either Assumption OLS.1 or OLS.2 fails, then  $\beta$  is not identified (unless we make other assumptions, as in Chapter 5). Usually it is correlation between u and one or more elements of x that causes lack of identification. Second, the OLS estimator is *not* necessarily unbiased even under Assumptions OLS.1 and OLS.2. However, if we impose the zero conditional mean assumption (4.3), then it can be shown that  $E(\hat{\beta} | X) = \beta$  if X'X is non-singular; see Problem 4.2. By iterated expectations,  $\hat{\beta}$  is then also unconditionally unbiased, provided the expected value  $E(\hat{\beta})$  exists.

Finally, we have not made the much more restrictive assumption that u and  $\mathbf{x}$  are *independent*. If E(u) = 0 and u is independent of  $\mathbf{x}$ , then assumption (4.3) holds, but not vice versa. For example,  $Var(u \mid \mathbf{x})$  is entirely unrestricted under assumption (4.3), but  $Var(u \mid \mathbf{x})$  is necessarily constant if u and  $\mathbf{x}$  are independent.

#### 4.2.2 Asymptotic Inference Using OLS

The asymptotic distribution of the OLS estimator is derived by writing

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \left(N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{x}_{i}\right)^{-1} \left(N^{-1/2} \sum_{i=1}^{N} \mathbf{x}_{i}' u_{i}\right)$$

As we saw in Theorem 4.1,  $(N^{-1}\sum_{i=1}^{N}\mathbf{x}_{i}'\mathbf{x}_{i})^{-1} - \mathbf{A}^{-1} = o_{p}(1)$ . Also,  $\{(\mathbf{x}_{i}'u_{i}): i=1,2,\ldots\}$  is an i.i.d. sequence with zero mean, and we assume that each element has finite variance. Then the central limit theorem (Theorem 3.2) implies that  $N^{-1/2}\sum_{i=1}^{N}\mathbf{x}_{i}'u_{i} \stackrel{d}{\to} \text{Normal}(\mathbf{0},\mathbf{B})$ , where  $\mathbf{B}$  is the  $K \times K$  matrix

$$\mathbf{B} \equiv \mathbf{E}(u^2 \mathbf{x}' \mathbf{x}) \tag{4.7}$$

This implies  $N^{-1/2} \sum_{i=1}^{N} \mathbf{x}'_{i} u_{i} = \mathbf{O}_{p}(1)$ , and so we can write

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \mathbf{A}^{-1} \left( N^{-1/2} \sum_{i=1}^{N} \mathbf{x}_{i}' u_{i} \right) + o_{p}(1)$$

$$(4.8)$$

since  $o_p(1) \cdot O_p(1) = o_p(1)$ . We can use equation (4.8) to immediately obtain the asymptotic distribution of  $\sqrt{N}(\hat{\pmb{\beta}} - \pmb{\beta})$ . A **homoskedasticity** assumption simplifies the form of OLS asymptotic variance:

ASSUMPTION OLS.3:  $E(u^2x'x) = \sigma^2E(x'x)$ , where  $\sigma^2 \equiv E(u^2)$ .


{71}------------------------------------------------

Because E(u)=0,  $\sigma^2$  is also equal to Var(u). Assumption OLS.3 is the weakest form of the homoskedasticity assumption. If we write out the  $K\times K$  matrices in Assumption OLS.3 element by element, we see that Assumption OLS.3 is equivalent to assuming that the squared error,  $u^2$ , is uncorrelated with each  $x_j$ ,  $x_j^2$ , and all cross products of the form  $x_jx_k$ . By the law of iterated expectations, sufficient for Assumption OLS.3 is  $E(u^2\,|\,\mathbf{x})=\sigma^2$ , which is the same as  $Var(u\,|\,\mathbf{x})=\sigma^2$  when  $E(u\,|\,\mathbf{x})=0$ . The constant conditional variance assumption for u given  $\mathbf{x}$  is the easiest to interpret, but it is stronger than needed.

THEOREM 4.2 (Asymptotic Normality of OLS): Under Assumptions OLS.1–OLS.3,

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \stackrel{a}{\sim} \text{Normal}(0, \sigma^2 \mathbf{A}^{-1})$$
 (4.9)

*Proof:* From equation (4.8) and definition of **B**, it follows from Lemma 3.7 and Corollary 3.2 that

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \stackrel{a}{\sim} \text{Normal}(0, \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-1})$$

Under Assumption OLS.3,  $\mathbf{B} = \sigma^2 \mathbf{A}$ , which proves the result.

Practically speaking, equation (4.9) allows us to treat  $\hat{\boldsymbol{\beta}}$  as approximately normal with mean  $\boldsymbol{\beta}$  and variance  $\sigma^2[\mathrm{E}(\mathbf{x}'\mathbf{x})]^{-1}/N$ . The usual estimator of  $\sigma^2$ ,  $\hat{\sigma}^2 \equiv \mathrm{SSR}/(N-K)$ , where  $\mathrm{SSR} = \sum_{i=1}^N \hat{u}_i^2$  is the OLS sum of squared residuals, is easily shown to be consistent. (Using N or N-K in the denominator does not affect consistency.) When we also replace  $\mathrm{E}(\mathbf{x}'\mathbf{x})$  with the sample average  $N^{-1}\sum_{i=1}^N \mathbf{x}_i'\mathbf{x}_i = (\mathbf{X}'\mathbf{X}/N)$ , we get

$$\operatorname{Avar}(\hat{\boldsymbol{\beta}}) = \hat{\sigma}^2 (\mathbf{X}'\mathbf{X})^{-1} \tag{4.10}$$

The right-hand side of equation (4.10) should be familiar: it is the usual OLS variance matrix estimator under the classical linear model assumptions. The bottom line of Theorem 4.2 is that, under Assumptions OLS.1–OLS.3, the usual OLS standard errors, t statistics, and F statistics are asymptotically valid. Showing that the F statistic is approximately valid is done by deriving the Wald test for linear restrictions of the form  $\mathbf{R}\boldsymbol{\beta} = \mathbf{r}$  (see Chapter 3). Then the F statistic is simply a degrees-of-freedom-adjusted Wald statistic, which is where the F distribution (as opposed to the chisquare distribution) arises.

# 4.2.3 Heteroskedasticity-Robust Inference

If Assumption OLS.1 fails, we are in potentially serious trouble, as OLS is not even consistent. In the next chapter we discuss the important method of instrumental variables that can be used to obtain consistent estimators of  $\beta$  when Assumption

{72}------------------------------------------------

OLS.1 fails. Assumption OLS.2 is also needed for consistency, but there is rarely any reason to examine its failure.

Failure of Assumption OLS.3 has less serious consequences than failure of Assumption OLS.1. As we have already seen, Assumption OLS.3 has nothing to do with consistency of  $\hat{\beta}$ . Further, the proof of asymptotic normality based on equation (4.8) is still valid without Assumption OLS.3, but the final asymptotic variance is different. We have assumed OLS.3 for deriving the limiting distribution because it implies the asymptotic validity of the usual OLS standard errors and test statistics. All regression packages assume OLS.3 as the default in reporting statistics.

Often there are reasons to believe that Assumption OLS.3 might fail, in which case equation (4.10) is no longer a valid estimate of even the asymptotic variance matrix. If we make the zero conditional mean assumption (4.3), one solution to violation of Assumption OLS.3 is to specify a model for Var(y|x), estimate this model, and apply weighted least squares (WLS): for observation i,  $y_i$  and every element of  $x_i$ (including unity) are divided by an estimate of the conditional standard deviation  $[Var(y_i | \mathbf{x}_i)]^{1/2}$ , and OLS is applied to the weighted data (see Wooldridge, 2000a, Chapter 8, for details). This procedure leads to a different estimator of  $\beta$ . We discuss WLS in the more general context of nonlinear regression in Chapter 12. Lately, it has become more popular to estimate  $\beta$  by OLS even when heteroskedasticity is suspected but to adjust the standard errors and test statistics so that they are valid in the presence of arbitrary heteroskedasticity. Since these standard errors are valid whether or not Assumption OLS.3 holds, this method is much easier than a weighted least squares procedure. What we sacrifice is potential efficiency gains from weighted least squares (WLS) (see Chapter 14). But, efficiency gains from WLS are guaranteed only if the model for  $Var(y|\mathbf{x})$  is correct. Further, WLS is generally inconsistent if  $E(u | \mathbf{x}) \neq 0$  but Assumption OLS.1 holds, so WLS is inappropriate for estimating linear projections. Especially with large sample sizes, the presence of heteroskedasticity need not affect one's ability to perform accurate inference using OLS. But we need to compute standard errors and test statistics appropriately.

The adjustment needed to the asymptotic variance follows from the proof of Theorem 4.2: without OLS.3, the asymptotic variance of  $\hat{\boldsymbol{\beta}}$  is  $\operatorname{Avar}(\hat{\boldsymbol{\beta}}) = \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-1}/N$ , where the  $K \times K$  matrices  $\mathbf{A}$  and  $\mathbf{B}$  were defined earlier. We already know how to consistently estimate  $\mathbf{A}$ . Estimation of  $\mathbf{B}$  is also straightforward. First, by the law of large numbers,  $N^{-1}\sum_{i=1}^N u_i^2 \mathbf{x}_i' \mathbf{x}_i \stackrel{p}{\to} \mathrm{E}(u^2 \mathbf{x}' \mathbf{x}) = \mathbf{B}$ . Now, since the  $u_i$  are not observed, we replace  $u_i$  with the OLS residual  $\hat{u}_i = y_i - \mathbf{x}_i \hat{\boldsymbol{\beta}}$ . This leads to the consistent estimator  $\hat{\mathbf{B}} \equiv N^{-1}\sum_{i=1}^N \hat{u}_i^2 \mathbf{x}_i' \mathbf{x}_i$ . See White (1984) and Problem 4.5.

The heteroskedasticity-robust variance matrix estimator of  $\hat{\beta}$  is  $\hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1}/N$  or, after cancellations,

{73}------------------------------------------------

$$\operatorname{Avar}(\hat{\boldsymbol{\beta}}) = (\mathbf{X}'\mathbf{X})^{-1} \left( \sum_{i=1}^{N} \hat{u}_{i}^{2} \mathbf{x}_{i}' \mathbf{x}_{i} \right) (\mathbf{X}'\mathbf{X})^{-1}$$
(4.11)

This matrix was introduced in econometrics by White (1980b), although some attribute it to either Eicker (1967) or Huber (1967), statisticians who discovered robust variance matrices. The square roots of the diagonal elements of equation (4.11) are often called the **White standard errors** or **Huber standard errors**, or some hyphenated combination of the names Eicker, Huber, and White. It is probably best to just call them **heteroskedasticity-robust standard errors**, since this term describes their purpose. Remember, these standard errors are asymptotically valid in the presence of any kind of heteroskedasticity, including homoskedasticity.

Robust standard errors are often reported in applied cross-sectional work, especially when the sample size is large. Sometimes they are reported along with the usual OLS standard errors; sometimes they are presented in place of them. Several regression packages now report these standard errors as an option, so it is easy to obtain heteroskedasticity-robust standard errors.

Sometimes, as a degrees-of-freedom correction, the matrix in equation (4.11) is multiplied by N/(N-K). This procedure guarantees that, if the  $\hat{u}_i^2$  were constant across i (an unlikely event in practice, but the strongest evidence of homoskedasticity possible), then the usual OLS standard errors would be obtained. There is some evidence that the degrees-of-freedom adjustment improves finite sample performance. There are other ways to adjust equation (4.11) to improve its small-sample properties—see, for example, MacKinnon and White (1985)—but if N is large relative to K, these adjustments typically make little difference.

Once standard errors are obtained, *t* statistics are computed in the usual way. These are robust to heteroskedasticity of unknown form, and can be used to test single restrictions. The *t* statistics computed from heteroskedasticity robust standard errors are **heteroskedasticity-robust** *t* **statistics**. Confidence intervals are also obtained in the usual way.

When Assumption OLS.3 fails, the usual F statistic is not valid for testing multiple linear restrictions, even asymptotically. Some packages allow robust testing with a simple command, while others do not. If the hypotheses are written as

$$\mathbf{H_0: R\beta = r} \tag{4.12}$$

where **R** is  $Q \times K$  and has rank  $Q \leq K$ , and **r** is  $Q \times 1$ , then the heteroskedasticity-robust Wald statistic for testing equation (4.12) is

$$W = (\mathbf{R}\hat{\boldsymbol{\beta}} - \mathbf{r})'(\mathbf{R}\hat{\mathbf{V}}\mathbf{R}')^{-1}(\mathbf{R}\hat{\boldsymbol{\beta}} - \mathbf{r})$$
(4.13)

{74}------------------------------------------------

where  $\hat{\mathbf{V}}$  is given in equation (4.11). Under  $\mathbf{H}_0$ ,  $W \stackrel{a}{\sim} \chi_Q^2$ . The Wald statistic can be turned into an approximate  $\mathscr{F}_{Q,N-K}$  random variable by dividing it by Q (and usually making the degrees-of-freedom adjustment to  $\hat{\mathbf{V}}$ ). But there is nothing wrong with using equation (4.13) directly.