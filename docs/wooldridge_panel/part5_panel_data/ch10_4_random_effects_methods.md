# Random Effects Methods

> Pages: 269-275

# 10.4.1 Estimation and Inference under the Basic Random Effects Assumptions

As with pooled OLS, a random effects analysis puts ci into the error term. In fact, random effects analysis imposes more assumptions than those needed for pooled OLS: strict exogeneity in addition to orthogonality between ci and xit. Stating the assumption in terms of conditional means, we have

assumption RE.1:

(a) 
$$E(u_{it} | \mathbf{x}_i, c_i) = 0, t = 1, ..., T.$$

(b) 
$$E(c_i | \mathbf{x}_i) = E(c_i) = 0$$

where 
$$\mathbf{x}_i \equiv (\mathbf{x}_{i1}, \mathbf{x}_{i2}, \dots, \mathbf{x}_{iT}).$$

In Section 10.2 we discussed the meaning of the strict exogeneity Assumption RE.1a. Assumption RE.1b is how we will state the orthogonality between ci and each xit. For obtaining consistent results, we could relax RE.1b to assumption (10.22), but in practice this approach affords little more generality, and we will use Assumption RE.1b later to derive the traditional asymptotic variance for the random effects estimator. Assumption RE.1b is always implied by the assumption that the xit are fixed and EðciÞ ¼ 0, or by the assumption that ci is independent of xi. The important part is Eðci j xiÞ ¼ EðciÞ; the assumption EðciÞ ¼ 0 is without loss of generality, provided an intercept is included in xit, as should almost always be the case.

Why do we maintain Assumption RE.1 when it is more restrictive than needed for a pooled OLS analysis? The random effects approach exploits the serial correlation in the composite error, vit ¼ ci þ uit, in a generalized least squares (GLS) framework. In order to ensure that feasible GLS is consistent, we need some form of strict exogeneity between the explanatory variables and the composite error. Under Assumption RE.1 we can write

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + v_{it} \tag{10.23}$$

{270}------------------------------------------------

$$E(v_{it} | \mathbf{x}_i) = 0, \qquad t = 1, 2, \dots, T$$
 (10.24)

where

$$v_{it} = c_i + u_{it} \tag{10.25}$$

Equation (10.24) shows that  $\{\mathbf{x}_{it}: t=1,\ldots,T\}$  satisfies the strict exogeneity assumption SGLS.1 (see Chapter 7) in the model (10.23). Therefore, we can apply GLS methods that account for the particular error structure in equation (10.25).

Write the model (10.23) for all T time periods as

$$\mathbf{y}_i = \mathbf{X}_i \boldsymbol{\beta} + \mathbf{v}_i \tag{10.26}$$

and  $\mathbf{v}_i$  can be written as  $\mathbf{v}_i = c_i \mathbf{j}_T + \mathbf{u}_i$ , where  $\mathbf{j}_T$  is the  $T \times 1$  vector of ones. Define the (unconditional) variance matrix of  $\mathbf{v}_i$  as

$$\mathbf{\Omega} \equiv \mathbf{E}(\mathbf{v}_i \mathbf{v}_i') \tag{10.27}$$

a  $T \times T$  matrix that we assume to be positive definite. Remember, this matrix is necessarily the same for all i because of the random sampling assumption in the cross section.

For consistency of GLS, we need the usual rank condition for GLS:

Assumption RE.2: rank 
$$E(\mathbf{X}_i'\mathbf{\Omega}^{-1}\mathbf{X}_i) = K$$
.

Applying the results from Chapter 7, we know that GLS and feasible GLS are consistent under Assumptions RE.1 and RE.2. A general FGLS analysis, using an unrestricted variance estimator  $\Omega$ , is consistent and  $\sqrt{N}$ -asymptotically normal as  $N \to \infty$ . But we would not be exploiting the unobserved effects structure of  $v_{it}$ . A standard random effects analysis adds assumptions on the idiosyncratic errors that give  $\Omega$  a special form. The first assumption is that the idiosyncratic errors  $u_{it}$  have a constant unconditional variance across t:

$$E(u_{it}^2) = \sigma_u^2, \qquad t = 1, 2, \dots, T$$
 (10.28)

The second assumption is that the idiosyncratic errors are serially uncorrelated:

$$E(u_{it}u_{is}) = 0, \qquad \text{all } t \neq s \tag{10.29}$$

Under these two assumptions, we can derive the variances and covariances of the elements of  $\mathbf{v}_i$ . Under Assumption RE.1a,  $E(c_i u_{it}) = 0$ , t = 1, 2, ..., T, and so

$$E(v_{it}^{2}) = E(c_{i}^{2}) + 2E(c_{i}u_{it}) + E(u_{it}^{2}) = \sigma_{c}^{2} + \sigma_{u}^{2}$$

where  $\sigma_c^2 = E(c_i^2)$ . Also, for all  $t \neq s$ ,


{271}------------------------------------------------

$$E(v_{it}v_{is}) = E[(c_i + u_{it})(c_i + u_{is})] = E(c_i^2) = \sigma_c^2$$

Therefore, under assumptions RE.1, (10.28), and (10.29),  $\Omega$  takes the special form

$$\mathbf{\Omega} = \mathbf{E}(\mathbf{v}_{i}\mathbf{v}_{i}^{\prime}) = \begin{pmatrix} \sigma_{c}^{2} + \sigma_{u}^{2} & \sigma_{c}^{2} & \cdots & \sigma_{c}^{2} \\ \sigma_{c}^{2} & \sigma_{c}^{2} + \sigma_{u}^{2} & \cdots & \vdots \\ \vdots & & \ddots & \sigma_{c}^{2} \\ \sigma_{c}^{2} & & \sigma_{c}^{2} + \sigma_{u}^{2} \end{pmatrix}$$
(10.30)

Because  $\mathbf{j}_T \mathbf{j}_T'$  is the  $T \times T$  matrix with unity in every element, we can write the matrix (10.30) as

$$\mathbf{\Omega} = \sigma_u^2 \mathbf{I}_T + \sigma_c^2 \mathbf{j}_T \mathbf{j}_T' \tag{10.31}$$

When  $\Omega$  has the form (10.31), we say it has the **random effects structure**. Rather than depending on T(T+1)/2 unrestricted variances and covariances, as would be the case in a general GLS analysis,  $\Omega$  depends only on two parameters,  $\sigma_c^2$  and  $\sigma_u^2$ , regardless of the size of T. The correlation between the composite errors  $v_{it}$  and  $v_{is}$  does not depend on the difference between t and s:  $Corr(v_{is}, v_{it}) = \sigma_c^2/(\sigma_c^2 + \sigma_u^2) \ge 0$ ,  $s \ne t$ . This correlation is also the ratio of the variance of  $c_i$  to the variance of the composite error, and it is useful as a measure of the relative importance of the unobserved effect  $c_i$ .

Assumptions (10.28) and (10.29) are special to random effects. For efficiency of feasible GLS, we assume that the variance matrix of  $\mathbf{v}_i$  conditional on  $\mathbf{x}_i$  is constant:

$$E(\mathbf{v}_i \mathbf{v}_i' \mid \mathbf{x}_i) = E(\mathbf{v}_i \mathbf{v}_i') \tag{10.32}$$

Assumptions (10.28), (10.29), and (10.32) are implied by our third random effects assumption:

ASSUMPTION RE.3: (a) 
$$E(\mathbf{u}_i\mathbf{u}_i' | \mathbf{x}_i, c_i) = \sigma_u^2 \mathbf{I}_T$$
. (b)  $E(c_i^2 | \mathbf{x}_i) = \sigma_c^2$ .

Under Assumption RE.3a,  $E(u_{it}^2 | \mathbf{x}_i, c_i) = \sigma_u^2$ , t = 1, ..., T, which implies assumption (10.28), and  $E(u_{it}u_{is} | \mathbf{x}_i, c_i) = 0$ ,  $t \neq s$ , t, s = 1, ..., T, which implies assumption (10.29) (both by the usual iterated expectations argument). But Assumption RE.3a is stronger because it assumes that the *conditional* variances are constant and the *conditional* covariances are zero. Along with Assumption RE.1b, Assumption RE.3b is the same as  $Var(c_i | \mathbf{x}_i) = Var(c_i)$ , which is a homoskedasticity assumption on the unobserved effect  $c_i$ . Under Assumption RE.3, assumption (10.32) holds and  $\Omega$  has the form (10.30).

{272}------------------------------------------------

To implement an FGLS procedure, define  $\sigma_v^2 = \sigma_c^2 + \sigma_u^2$ . For now, assume that we have consistent estimators of  $\sigma_u^2$  and  $\sigma_c^2$ . Then we can form

$$\hat{\mathbf{\Omega}} \equiv \hat{\sigma}_{v}^{2} \mathbf{I}_{T} + \hat{\sigma}_{c}^{2} \mathbf{j}_{T} \mathbf{j}_{T}^{\prime} \tag{10.33}$$

a  $T \times T$  matrix that we assume to be positive definite. In a panel data context, the FGLS estimator that uses the variance matrix (10.33) is what is known as the **random** effects estimator:

$$\hat{\boldsymbol{\beta}}_{RE} = \left(\sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\boldsymbol{\Omega}}^{-1} \mathbf{X}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\boldsymbol{\Omega}}^{-1} \mathbf{y}_{i}\right)$$
(10.34)

The random effects estimator is clearly motivated by Assumption RE.3. Nevertheless,  $\hat{\boldsymbol{\beta}}_{RE}$  is consistent whether or not Assumption RE.3 holds. As long as Assumption RE.1 and the appropriate rank condition hold,  $\hat{\boldsymbol{\beta}}_{RE} \stackrel{p}{\to} \boldsymbol{\beta}$  as  $N \to \infty$ . The argument is almost the same as showing that consistency of the FGLS estimator does not rely on  $\mathrm{E}(\mathbf{v}_i\mathbf{v}_i'|\mathbf{X}_i) = \mathbf{\Omega}$ . The only difference is that, even if  $\mathbf{\Omega}$  does not have the special form in equation (10.31),  $\hat{\mathbf{\Omega}}$  still has a well-defined probability limit. The fact that it does not necessarily converge to  $\mathrm{E}(\mathbf{v}_i\mathbf{v}_i')$  does not affect the consistency of the random effects procedure. (Technically, we need to replace  $\mathbf{\Omega}$  with  $\mathrm{plim}(\hat{\mathbf{\Omega}})$  in stating Assumption RE.2.)

Under Assumption RE.3 the random effects estimator is efficient in the class of estimators consistent under  $E(\mathbf{v}_i | \mathbf{x}_i) = \mathbf{0}$ , including pooled OLS and a variety of weighted least squares estimators, because RE is asymptotically equivalent to GLS under Assumptions RE.1–RE.3. The usual feasible GLS variance matrix—see equation (7.51)—is valid under Assumptions RE.1–RE.3. The only difference from the general analysis is that  $\hat{\Omega}$  is chosen as in expression (10.33).

In order to implement the RE procedure, we need to obtain  $\hat{\sigma}_c^2$  and  $\hat{\sigma}_u^2$ . Actually, it is easiest to first find  $\hat{\sigma}_v^2 = \hat{\sigma}_c^2 + \hat{\sigma}_u^2$ . Under Assumption RE.3a,  $\sigma_v^2 = T^{-1} \sum_{t=1}^T \mathrm{E}(v_{it}^2)$  for all i; therefore, averaging  $v_{it}^2$  across all i and t would give a consistent estimator of  $\sigma_v^2$ . But we need to estimate  $\beta$  to make this method operational. A convenient initial estimator of  $\beta$  is the pooled OLS estimator, denoted here by  $\hat{\beta}$ . Let  $\hat{v}_{it}$  denote the pooled OLS residuals. A consistent estimator of  $\sigma_v^2$  is

$$\hat{\sigma}_v^2 = \frac{1}{(NT - K)} \sum_{i=1}^{N} \sum_{t=1}^{T} \hat{\hat{\mathbf{v}}}_{it}^2$$
(10.35)

which is the usual variance estimator from the OLS regression on the pooled data. The degrees-of-freedom correction in equation (10.35)—that is, the use of NT - K

{273}------------------------------------------------

rather than NT—has no effect asymptotically. Under Assumptions RE.1–RE.3, equation (10.35) is a consistent estimator of  $\sigma_v^2$ .

To find a consistent estimator of  $\sigma_c^2$ , recall that  $\sigma_c^2 = \mathrm{E}(v_{it}v_{is})$ , all  $t \neq s$ . Therefore, for each i, there are T(T-1)/2 nonredundant error products that can be used to estimate  $\sigma_c^2$ . If we sum all these combinations and take the expectation, we get, for each i,

$$E\left(\sum_{t=1}^{T-1} \sum_{s=t+1}^{T} v_{it} v_{is}\right) = \sum_{t=1}^{T-1} \sum_{s=t+1}^{T} E(v_{it} v_{is}) = \sum_{t=1}^{T-1} \sum_{s=t+1}^{T} \sigma_c^2 = \sigma_c^2 \sum_{t=1}^{T-1} (T-t)$$

$$= \sigma_c^2 ((T-1) + (T-2) + \dots + 2 + 1) = \sigma_c^2 T(T-1)/2 \quad (10.36)$$

where we have used the fact that the sum of the first T-1 positive integers is T(T-1)/2. As usual, a consistent estimator is obtained by replacing the expectation with an average (across i) and replacing  $v_{it}$  with its pooled OLS residual. We also make a degrees-of-freedom adjustment as a small-sample correction:

$$\hat{\sigma}_c^2 = \frac{1}{[NT(T-1)/2 - K]} \sum_{i=1}^{N} \sum_{t=1}^{T-1} \sum_{s=t+1}^{T} \hat{\hat{v}}_{it} \hat{\hat{v}}_{is}$$
(10.37)

is a consistent estimator of  $\sigma_c^2$  under Assumptions RE.1–RE.3. Given  $\hat{\sigma}_v^2$  and  $\hat{\sigma}_c^2$ , we can form  $\hat{\sigma}_u^2 = \hat{\sigma}_v^2 - \hat{\sigma}_c^2$ . [The idiosyncratic error variance,  $\sigma_u^2$ , can also be estimated using the fixed effects method, which we discuss in Section 10.5. Also, there are other methods of estimating  $\sigma_c^2$ . A common estimator of  $\sigma_c^2$  is based on the between estimator of  $\sigma_c^2$ , which we touch on in Section 10.5; see Hsiao (1986, Section 3.3) and Baltagi (1995, Section 2.3). Because the RE estimator is a feasible GLS estimator, all that we need are consistent estimators of  $\sigma_c^2$  and  $\sigma_u^2$  in order to obtain a  $\sqrt{N}$ -efficient estimator of  $\sigma_c^2$ .

As a practical matter, equation (10.37) is not guaranteed to be positive, although it is in the vast majority of applications. A negative value for  $\hat{\sigma}_c^2$  is indicative of negative serial correlation in  $u_{it}$ , probably a substantial amount, which means that Assumption RE.3a is violated. Alternatively, some other assumption in the model can be false. We should make sure that time dummies are included in the model if they are significant; omitting them can induce serial correlation in the implied  $u_{it}$ . If  $\hat{\sigma}_c^2$  is negative, unrestricted FGLS may be called for; see Section 10.4.3.

Example 10.4 (RE Estimation of the Effects of Job Training Grants): We now use the data in JTRAIN1.RAW to estimate the effect of job training grants on firm scrap rates, using a random effects analysis. There are 54 firms that reported scrap rates for each of the years 1987, 1988, and 1989. Grants were not awarded in 1987. Some firms

{274}------------------------------------------------

received grants in 1988, others received grants in 1989, and a firm could not receive a grant twice. Since there are firms in 1989 that received a grant only in 1988, it is important to allow the grant effect to persist one period. The estimated equation is

$$\log(\hat{s}crap) = .415 - .093 \ d88 - .270 \ d89 + .548 \ union$$

$$(.243) \ (.109) \ (.132) \ (.411)$$

$$- .215 \ grant - .377 \ grant_{-1}$$

$$(.148) \ (.205)$$

The lagged value of *grant* has the larger impact and is statistically significant at the 5 percent level against a one-sided alternative. You are invited to estimate the equation without  $grant_{-1}$  to verify that the estimated grant effect is much smaller (on the order of 6.7 percent) and statistically insignificant.

Multiple hypotheses tests are carried out as in any FGLS analysis; see Section 7.6, where G = T. In computing an F-type statistic based on weighted sums of squared residuals,  $\hat{\Omega}$  in expression (10.33) should be based on the pooled OLS residuals from the unrestricted model. Then, obtain the residuals from the unrestricted random effects estimation as  $\hat{\mathbf{v}}_i \equiv \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}}_{RE}$ . Let  $\tilde{\boldsymbol{\beta}}_{RE}$  denote the random effects estimator with the Q linear restrictions imposed, and define the restricted random effects residuals as  $\tilde{\mathbf{v}}_i \equiv \mathbf{y}_i - \mathbf{X}_i \tilde{\boldsymbol{\beta}}_{RE}$ . Insert these into equation (7.52) in place of  $\hat{\mathbf{u}}_i$  and  $\tilde{\mathbf{u}}_i$  for a chi-square statistic or into equation (7.53) for an F-type statistic.

In Example 10.4, the Wald test for joint significance of *grant* and  $grant_{-1}$  (against a two-sided alternative) yields a  $\chi_2^2$  statistic equal to 3.66, with *p*-value = .16. (This test comes from Stata<sup>®</sup>.)

#### 10.4.2 Robust Variance Matrix Estimator

Because failure of Assumption RE.3 does not cause inconsistency in the RE estimator, it is very useful to be able to conduct statistical inference without this assumption. Assumption RE.3 can fail for two reasons. First,  $E(\mathbf{v}_i\mathbf{v}_i'|\mathbf{x}_i)$  may not be constant, so that  $E(\mathbf{v}_i\mathbf{v}_i'|\mathbf{x}_i) \neq E(\mathbf{v}_i\mathbf{v}_i')$ . This outcome is always a possibility with GLS analysis. Second,  $E(\mathbf{v}_i\mathbf{v}_i')$  may not have the random effects structure: the idiosyncratic errors  $u_{it}$  may have variances that change over time, or they could be serially correlated. In either case a robust variance matrix is available from the analysis in Chapter 7. We simply use equation (7.49) with  $\hat{\mathbf{u}}_i$  replaced by  $\hat{\mathbf{v}}_i = \mathbf{y}_i - \mathbf{X}_i\hat{\boldsymbol{\beta}}_{RE}$ ,  $i = 1, 2, \ldots, N$ , the  $T \times 1$  vectors of RE residuals.

Robust standard errors are obtained in the usual way from the robust variance matrix estimator, and robust Wald statistics are obtained by the usual formula W =

{275}------------------------------------------------

 $(\mathbf{R}\hat{\boldsymbol{\beta}} - \mathbf{r})'(\mathbf{R}\hat{\mathbf{V}}\mathbf{R}')^{-1}(\mathbf{R}\hat{\boldsymbol{\beta}} - \mathbf{r})$ , where  $\hat{\mathbf{V}}$  is the robust variance matrix estimator. Remember, if Assumption RE.3 is violated, the sum of squared residuals form of the F statistic is not valid.

The idea behind using a robust variance matrix is the following. Assumptions RE.1–RE.3 lead to a well-known estimation technique whose properties are understood under these assumptions. But it is always a good idea to make the analysis robust whenever feasible. With fixed T and large N asymptotics, we lose nothing in using the robust standard errors and test statistics even if Assumption RE.3 holds. In Section 10.7.2, we show how the RE estimator can be obtained from a particular pooled OLS regression, which makes obtaining robust standard errors and t and t statistics especially easy.