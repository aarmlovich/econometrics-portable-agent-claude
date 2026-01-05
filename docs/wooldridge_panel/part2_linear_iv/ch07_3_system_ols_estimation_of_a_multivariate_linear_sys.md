# System OLS Estimation of a Multivariate Linear System

> Pages: 160-169

#### 7.3.1 Preliminaries

We now analyze a general multivariate model that contains the examples in Section 7.2, and many others, as special cases. Assume that we have independent, identically distributed cross section observations  $\{(\mathbf{X}_i, \mathbf{y}_i): i = 1, 2, \dots, N\}$ , where  $\mathbf{X}_i$  is a  $G \times K$  matrix and  $\mathbf{y}_i$  is a  $G \times 1$  vector. Thus,  $\mathbf{y}_i$  contains the dependent variables for all G equations (or time periods, in the panel data case). The matrix  $\mathbf{X}_i$  contains the explanatory variables appearing anywhere in the system. For notational clarity we include the i subscript for stating the general model and the assumptions.

The multivariate linear model for a random draw from the population can be expressed as

$$\mathbf{y}_i = \mathbf{X}_i \boldsymbol{\beta} + \mathbf{u}_i \tag{7.9}$$

where  $\beta$  is the  $K \times 1$  parameter vector of interest and  $\mathbf{u}_i$  is a  $G \times 1$  vector of unobservables. Equation (7.9) explains the G variables  $y_{i1}, \ldots, y_{iG}$  in terms of  $\mathbf{X}_i$  and the unobservables  $\mathbf{u}_i$ . Because of the random sampling assumption, we can state all assumptions in terms of a generic observation; in examples, we will often omit the i subscript.

Before stating any assumptions, we show how the two examples introduced in Section 7.2 fit into this framework.

Example 7.1 (SUR, continued): The SUR model (7.1) can be expressed as in equation (7.9) by defining  $\mathbf{y}_i = (y_{i1}, y_{i2}, \dots, y_{iG})', \mathbf{u}_i = (u_{i1}, u_{i2}, \dots, u_{iG})',$  and

$$\mathbf{X}_{i} = \begin{pmatrix} \mathbf{x}_{i1} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\ \mathbf{0} & \mathbf{x}_{i2} & & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & & \vdots \\ \vdots & & & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{x}_{iG} \end{pmatrix}, \qquad \boldsymbol{\beta} = \begin{pmatrix} \boldsymbol{\beta}_{1} \\ \boldsymbol{\beta}_{2} \\ \vdots \\ \boldsymbol{\beta}_{G} \end{pmatrix}$$
(7.10)


{161}------------------------------------------------

Note that the dimension of  $X_i$  is  $G \times (K_1 + K_2 + \cdots + K_G)$ , so we define  $K \equiv K_1 + \cdots + K_G$ .

Example 7.2 (Panel Data, continued): The panel data model (7.6) can be expressed as in equation (7.9) by choosing  $\mathbf{X}_i$  to be the  $T \times K$  matrix  $\mathbf{X}_i = (\mathbf{x}'_{i1}, \mathbf{x}'_{i2}, \dots, \mathbf{x}'_{iT})'$ .

# 7.3.2 Asymptotic Properties of System OLS

Given the model in equation (7.9), we can state the key orthogonality condition for consistent estimation of  $\beta$  by system ordinary least squares (SOLS).

ASSUMPTION SOLS.1: 
$$E(\mathbf{X}_{i}'\mathbf{u}_{i}) = \mathbf{0}$$
.

Assumption SOLS.1 appears similar to the orthogonality condition for OLS analysis of single equations. What it implies differs across examples because of the multiple-equation nature of equation (7.9). For most applications,  $\mathbf{X}_i$  has a sufficient number of elements equal to unity so that Assumption SOLS.1 implies that  $E(\mathbf{u}_i) = \mathbf{0}$ , and we assume zero mean for the sake of discussion.

It is informative to see what Assumption SOLS.1 entails in the previous examples.

Example 7.1 (SUR, continued): In the SUR case,  $\mathbf{X}_{i}'\mathbf{u}_{i} = (\mathbf{x}_{i1}u_{i1}, \dots, \mathbf{x}_{iG}u_{iG})'$ , and so Assumption SOLS.1 holds if and only if

$$E(\mathbf{x}'_{ig}u_{ig}) = \mathbf{0}, \qquad g = 1, 2, \dots, G$$
 (7.11)

Thus, Assumption SOLS.1 does not require  $\mathbf{x}_{ih}$  and  $u_{ig}$  to be uncorrelated when  $h \neq g$ .

Example 7.2 (Panel Data, continued): For the panel data setup,  $\mathbf{X}_i'\mathbf{u}_i = \sum_{t=1}^T \mathbf{x}_{it}'u_{it}$ ; therefore, a sufficient, and very natural, condition for Assumption SOLS.1 is

$$\mathbf{E}(\mathbf{x}_{it}'u_{it}) = \mathbf{0}, \qquad t = 1, 2, \dots, T \tag{7.12}$$

Like assumption (7.5), assumption (7.12) allows  $\mathbf{x}_{is}$  and  $u_{it}$  to be correlated when  $s \neq t$ ; in fact, assumption (7.12) is weaker than assumption (7.5). Therefore, Assumption SOLS.1 does *not* impose strict exogeneity in panel data contexts.

Assumption SOLS.1 is the weakest assumption we can impose in a regression framework to get consistent estimators of  $\beta$ . As the previous examples show, Assumption SOLS.1 allows some elements of  $\mathbf{X}_i$  to be correlated with elements of  $\mathbf{u}_i$ . Much stronger is the zero conditional mean assumption

$$\mathbf{E}(\mathbf{u}_i \mid \mathbf{X}_i) = \mathbf{0} \tag{7.13}$$

{162}------------------------------------------------

which implies, among other things, that every element of  $\mathbf{X}_i$  and every element of  $\mathbf{u}_i$  are uncorrelated. [Of course, assumption (7.13) is not as strong as assuming that  $\mathbf{u}_i$  and  $\mathbf{X}_i$  are actually *independent*.] Even though assumption (7.13) is stronger than Assumption SOLS.1, it is, nevertheless, reasonable in some applications.

Under Assumption SOLS.1 the vector  $\beta$  satisfies

$$E[\mathbf{X}_i'(\mathbf{y}_i - \mathbf{X}_i\boldsymbol{\beta})] = \mathbf{0} \tag{7.14}$$

or  $E(\mathbf{X}_i'\mathbf{X}_i)\boldsymbol{\beta} = E(\mathbf{X}_i'\mathbf{y}_i)$ . For each i,  $\mathbf{X}_i'\mathbf{y}_i$  is a  $K \times 1$  random vector and  $\mathbf{X}_i'\mathbf{X}_i$  is a  $K \times K$  symmetric, positive semidefinite random matrix. Therefore,  $E(\mathbf{X}_i'\mathbf{X}_i)$  is always a  $K \times K$  symmetric, positive semidefinite nonrandom matrix (the expectation here is defined over the population distribution of  $\mathbf{X}_i$ ). To be able to estimate  $\boldsymbol{\beta}$  we need to assume that it is the only  $K \times 1$  vector that satisfies assumption (7.14).

ASSUMPTION SOLS.2:  $\mathbf{A} \equiv \mathbf{E}(\mathbf{X}_i'\mathbf{X}_i)$  is nonsingular (has rank K).

Under Assumptions SOLS.1 and SOLS.2 we can write  $\beta$  as

$$\boldsymbol{\beta} = [\mathbf{E}(\mathbf{X}_i'\mathbf{X}_i)]^{-1}\mathbf{E}(\mathbf{X}_i'\mathbf{y}_i) \tag{7.15}$$

which shows that Assumptions SOLS.1 and SOLS.2 identify the vector  $\beta$ . The analogy principle suggests that we estimate  $\beta$  by the sample analogue of assumption (7.15). Define the system ordinary least squares (SOLS) estimator of  $\beta$  as

$$\hat{\boldsymbol{\beta}} = \left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{X}_{i}\right)^{-1} \left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{y}_{i}\right)$$

$$(7.16)$$

For computing  $\hat{\beta}$  using matrix language programming, it is sometimes useful to write  $\hat{\beta} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{Y}$ , where  $\mathbf{X} \equiv (\mathbf{X}_1', \mathbf{X}_2', \dots, \mathbf{X}_N')'$  is the  $NG \times K$  matrix of stacked  $\mathbf{X}$  and  $\mathbf{Y} \equiv (\mathbf{y}_1', \mathbf{y}_2', \dots, \mathbf{y}_N')'$  is the  $NG \times 1$  vector of stacked observations on the  $\mathbf{y}_i$ . For asymptotic derivations, equation (7.16) is much more convenient. In fact, the consistency of  $\hat{\beta}$  can be read off of equation (7.16) by taking probability limits. We summarize with a theorem:

THEOREM 7.1 (Consistency of System OLS): Under Assumptions SOLS.1 and SOLS.2,  $\hat{\beta} \stackrel{p}{\to} \beta$ .

It is useful to see what the system OLS estimator looks like for the SUR and panel data examples.

Example 7.1 (SUR, continued): For the SUR model,

{163}------------------------------------------------

$$\sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{X}_{i} = \sum_{i=1}^{N} \begin{pmatrix} \mathbf{x}_{i1}' \mathbf{x}_{i1} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\ \mathbf{0} & \mathbf{x}_{i2}' \mathbf{x}_{i2} & & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & & \vdots \\ \vdots & & & \mathbf{0} \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{x}_{iG}' \mathbf{x}_{iG}' \end{pmatrix}; \qquad \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{y}_{i} = \sum_{i=1}^{N} \begin{pmatrix} \mathbf{x}_{i1}' \mathbf{y}_{i1} \\ \mathbf{x}_{i2}' \mathbf{y}_{i2} \\ \vdots \\ \mathbf{x}_{iG}' \mathbf{y}_{iG} \end{pmatrix}$$

Straightforward inversion of a block diagonal matrix shows that the OLS estimator from equation (7.16) can be written as  $\hat{\boldsymbol{\beta}} = (\hat{\boldsymbol{\beta}}_1', \hat{\boldsymbol{\beta}}_2', \dots, \hat{\boldsymbol{\beta}}_G')'$ , where each  $\hat{\boldsymbol{\beta}}_g$  is just the single-equation OLS estimator from the gth equation. In other words, system OLS estimation of a SUR model (without restrictions on the parameter vectors  $\boldsymbol{\beta}_g$ ) is equivalent to OLS equation by equation. Assumption SOLS.2 is easily seen to hold if  $E(\mathbf{x}_{iq}'\mathbf{x}_{ig})$  is nonsingular for all g.

Example 7.2 (Panel Data, continued): In the panel data case,

$$\sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{X}_{i} = \sum_{i=1}^{N} \sum_{t=1}^{T} \mathbf{x}_{it}' \mathbf{x}_{it}; \qquad \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{y}_{i} = \sum_{i=1}^{N} \sum_{t=1}^{T} \mathbf{x}_{it}' \mathbf{y}_{it}$$

Therefore, we can write  $\hat{\beta}$  as

$$\hat{\beta} = \left(\sum_{i=1}^{N} \sum_{t=1}^{T} \mathbf{x}'_{it} \mathbf{x}_{it}\right)^{-1} \left(\sum_{i=1}^{N} \sum_{t=1}^{T} \mathbf{x}'_{it} y_{it}\right)$$
(7.17)

This estimator is called the **pooled ordinary least squares (POLS) estimator** because it corresponds to running OLS on the observations pooled across i and t. We mentioned this estimator in the context of *independent* cross sections in Section 6.3. The estimator in equation (7.17) is for the same cross section units sampled at different points in time. Theorem 7.1 shows that the POLS estimator is consistent under the orthogonality conditions in assumption (7.12) and the mild condition rank  $E(\sum_{t=1}^{T} \mathbf{x}_{it}' \mathbf{x}_{it}) = K$ .

In the general system (7.9), the system OLS estimator does not necessarily have an interpretation as OLS equation by equation or as pooled OLS. As we will see in Section 7.7 for the SUR setup, sometimes we want to impose cross equation restrictions on the  $\beta_q$ , in which case the system OLS estimator has no simple interpretation.

While OLS is consistent under Assumptions SOLS.1 and SOLS.2, it is not necessarily unbiased. Assumption (7.13), and the finite sample assumption rank( $\mathbf{X}'\mathbf{X}$ ) = K, do ensure unbiasedness of OLS conditional on  $\mathbf{X}$ . [This conclusion follows because, under independent sampling,  $\mathrm{E}(\mathbf{u}_i \mid \mathbf{X}_1, \mathbf{X}_2, \ldots, \mathbf{X}_N) = \mathrm{E}(\mathbf{u}_i \mid \mathbf{X}_i) = \mathbf{0}$  under as-

{164}------------------------------------------------

sumption (7.13).] We focus on the weaker Assumption SOLS.1 because assumption (7.13) is often violated in economic applications, something we will see especially in our panel data analysis.

For inference, we need to find the asymptotic variance of the OLS estimator under essentially the same two assumptions; technically, the following derivation requires the elements of  $\mathbf{X}_i'\mathbf{u}_i\mathbf{u}_i'\mathbf{X}_i$  to have finite expected absolute value. From (7.16) and (7.9) write

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{X}_{i}\right)^{-1} \left(N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{u}_{i}\right)$$

Because  $E(\mathbf{X}_i'\mathbf{u}_i) = \mathbf{0}$  under Assumption SOLS.1, the CLT implies that

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{u}_{i} \xrightarrow{d} \text{Normal}(\mathbf{0}, \mathbf{B})$$
(7.18)

where

$$\mathbf{B} \equiv \mathrm{E}(\mathbf{X}_i' \mathbf{u}_i \mathbf{u}_i' \mathbf{X}_i) \equiv \mathrm{Var}(\mathbf{X}_i' \mathbf{u}_i) \tag{7.19}$$

In particular,  $N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{u}_{i} = O_{p}(1)$ . But  $(\mathbf{X}'\mathbf{X}/N)^{-1} = \mathbf{A}^{-1} + o_{p}(1)$ , so

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = \mathbf{A}^{-1} \left( N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{u}_{i} \right) + \left[ (\mathbf{X}' \mathbf{X} / N)^{-1} - \mathbf{A}^{-1} \right] \left( N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{u}_{i} \right) 
= \mathbf{A}^{-1} \left( N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{u}_{i} \right) + o_{p}(1) \cdot O_{p}(1) 
= \mathbf{A}^{-1} \left( N^{-1/2} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{u}_{i} \right) + o_{p}(1)$$
(7.20)

Therefore, just as with single-equation OLS and 2SLS, we have obtained an asymptotic representation for  $\sqrt{N}(\hat{\beta} - \beta)$  that is a *nonrandom* linear combination of a partial sum that satisfies the CLT. Equations (7.18) and (7.20) and the asymptotic equivalence lemma imply

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \stackrel{d}{\to} \text{Normal}(\mathbf{0}, \mathbf{A}^{-1}\mathbf{B}\mathbf{A}^{-1})$$
 (7.21)

We summarize with a theorem.

THEOREM 7.2 (Asymptotic Normality of SOLS): Under Assumptions SOLS.1 and SOLS.2, equation (7.21) holds.

{165}------------------------------------------------

The asymptotic variance of  $\hat{\beta}$  is

$$Avar(\hat{\beta}) = A^{-1}BA^{-1}/N \tag{7.22}$$

so that  $Avar(\hat{\beta})$  shrinks to zero at the rate 1/N, as expected. Consistent estimation of **A** is simple:

$$\hat{\mathbf{A}} \equiv \mathbf{X}'\mathbf{X}/N = N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}'\mathbf{X}_{i}$$
(7.23)

A consistent estimator of **B** can be found using the analogy principle. First, because  $\mathbf{B} = \mathrm{E}(\mathbf{X}_i'\mathbf{u}_i\mathbf{u}_i'\mathbf{X}_i), \ N^{-1}\sum_{i=1}^N \mathbf{X}_i'\mathbf{u}_i\mathbf{u}_i'\mathbf{X}_i \overset{p}{\to} \mathbf{B}$ . Since the  $\mathbf{u}_i$  are not observed, we replace them with the SOLS residuals:

$$\hat{\mathbf{u}}_i \equiv \mathbf{y}_i - \mathbf{X}_i \hat{\boldsymbol{\beta}} = \mathbf{u}_i - \mathbf{X}_i (\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \tag{7.24}$$

Using matrix algebra and the law of large numbers, it can be shown that

$$\hat{\mathbf{B}} \equiv N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{u}}_{i} \hat{\mathbf{u}}_{i}' \mathbf{X}_{i} \stackrel{p}{\to} \mathbf{B}$$
(7.25)

[To establish equation (7.25), we need to assume that certain moments involving  $\mathbf{X}_i$  and  $\mathbf{u}_i$  are finite.] Therefore, Avar  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta})$  is consistently estimated by  $\hat{\mathbf{A}}^{-1}\hat{\mathbf{B}}\hat{\mathbf{A}}^{-1}$ , and Avar $(\hat{\boldsymbol{\beta}})$  is estimated as

$$\hat{\mathbf{V}} \equiv \left(\sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{X}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \mathbf{X}_{i}' \hat{\mathbf{u}}_{i} \hat{\mathbf{u}}_{i}' \mathbf{X}_{i}\right) \left(\sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{X}_{i}\right)^{-1}$$
(7.26)

Under Assumptions SOLS.1 and SOLS.2, we perform inference on  $\beta$  as if  $\hat{\beta}$  is normally distributed with mean  $\beta$  and variance matrix (7.26). The square roots of the diagonal elements of the matrix (7.26) are reported as the asymptotic standard errors. The t ratio,  $\hat{\beta}_j/\text{se}(\hat{\beta}_j)$ , has a limiting normal distribution under the null hypothesis  $H_0$ :  $\beta_j = 0$ . Sometimes the t statistics are treated as being distributed as  $t_{NG-K}$ , which is asymptotically valid because NG - K should be large.

The estimator in matrix (7.26) is another example of a **robust variance matrix estimator** because it is valid without *any* second-moment assumptions on the errors  $\mathbf{u}_i$  (except, as usual, that the second moments are well defined). In a multivariate setting it is important to know what this robustness allows. First, the  $G \times G$  unconditional **variance matrix**,  $\mathbf{\Omega} \equiv \mathrm{E}(\mathbf{u}_i \mathbf{u}_i')$ , is entirely unrestricted. This fact allows **cross equation correlation** in an SUR system as well as different error variances in each equation. In panel data models, an unrestricted  $\mathbf{\Omega}$  allows for arbitrary **serial correlation** and 

{166}------------------------------------------------

**time-varying variances** in the disturbances. A second kind of robustness is that the **conditional variance matrix**,  $Var(\mathbf{u}_i | \mathbf{X}_i)$ , can depend on  $\mathbf{X}_i$  in an arbitrary, unknown fashion. The generality afforded by formula (7.26) is possible because of the  $N \to \infty$  asymptotics.

In special cases it is useful to impose more structure on the conditional and unconditional variance matrix of  $\mathbf{u}_i$  in order to simplify estimation of the asymptotic variance. We will cover an important case in Section 7.5.2. Essentially, the key restriction will be that the conditional and unconditional variances of  $\mathbf{u}_i$  are the same.

There are also some special assumptions that greatly simplify the analysis of the pooled OLS estimator for panel data; see Section 7.8.

# 7.3.3 Testing Multiple Hypotheses

Testing multiple hypotheses in a very robust manner is easy once  $\hat{\mathbf{V}}$  in matrix (7.26) has been obtained. The robust Wald statistic for testing  $\mathbf{H}_0$ :  $\mathbf{R}\boldsymbol{\beta} = \mathbf{r}$ , where  $\mathbf{R}$  is  $Q \times K$  with rank Q and  $\mathbf{r}$  is  $Q \times 1$ , has its usual form,  $W = (\mathbf{R}\hat{\boldsymbol{\beta}} - \mathbf{r})'(\mathbf{R}\hat{\mathbf{V}}\mathbf{R}')^{-1}(\mathbf{R}\hat{\boldsymbol{\beta}} - \mathbf{r})$ . Under  $\mathbf{H}_0$ ,  $W \stackrel{a}{\sim} \chi_Q^2$ . In the SUR case this is the easiest and most robust way of testing cross equation restrictions on the parameters in different equations using system OLS. In the panel data setting, the robust Wald test provides a way of testing multiple hypotheses about  $\boldsymbol{\beta}$  without assuming homoskedasticity or serial independence of the errors.

# 7.4 Consistency and Asymptotic Normality of Generalized Least Squares

# 7.4.1 Consistency

System OLS is consistent under fairly weak assumptions, and we have seen how to perform robust inference using OLS. If we strengthen Assumption SOLS.1 and add assumptions on the conditional variance matrix of  $\mathbf{u}_i$ , we can do better using a generalized least squares procedure. As we will see, GLS is not usually feasible because it requires knowing the variance matrix of the errors up to a multiplicative constant. Nevertheless, deriving the consistency and asymptotic distribution of the GLS estimator is worthwhile because it turns out that the feasible GLS estimator is asymptotically equivalent to GLS.

We start with the model (7.9), but consistency of GLS generally requires a stronger assumption than Assumption SOLS.1. We replace Assumption SOLS.1 with the assumption that each element of  $\mathbf{u}_i$  is uncorrelated with each element of  $\mathbf{X}_i$ . We can state this succinctly using the Kronecker product:

{167}------------------------------------------------

assumption SGLS.1: EðX<sup>i</sup> nuiÞ ¼ 0.

Typically, at least one element of X<sup>i</sup> is unity, so in practice Assumption SGLS.1 implies that EðuiÞ ¼ 0. We will assume u<sup>i</sup> has a zero mean for our discussion but not in proving any results.

Assumption SGLS.1 plays a crucial role in establishing consistency of the GLS estimator, so it is important to recognize that it puts more restrictions on the explanatory variables than does Assumption SOLS.1. In other words, when we allow the explanatory variables to be random, GLS requires a stronger assumption than system OLS in order to be consistent. Sufficient for Assumption SGLS.1, but not necessary, is the zero conditional mean assumption (7.13). This conclusion follows from a standard iterated expectations argument.

For GLS estimation of multivariate equations with i.i.d. observations, the secondmoment matrix of u<sup>i</sup> plays a key role. Define the G G symmetric, positive semidefinite matrix

$$\mathbf{\Omega} \equiv \mathbf{E}(\mathbf{u}_i \mathbf{u}_i') \tag{7.27}$$

As mentioned in Section 7.3.2, we call W the unconditional variance matrix of ui. [In the rare case that EðuiÞ 00, W is not the variance matrix of ui, but it is always the appropriate matrix for GLS estimation.] It is important to remember that expression (7.27) is definitional: because we are using random sampling, the unconditional variance matrix is necessarily the same for all i.

In place of Assumption SOLS.2, we assume that a weighted version of the expected outer product of X<sup>i</sup> is nonsingular.

assumption SGLS.2: W is positive definite and EðX<sup>0</sup> iW-1 XiÞ is nonsingular.

For the general treatment we assume that W is positive definite, rather than just positive semidefinite. In applications where the dependent variables across equations satisfy an adding up constraint—such as expenditure shares summing to unity—an equation must be dropped to ensure that W is nonsingular, a topic we return to in Section 7.7.3. As a practical matter, Assumption SGLS.2 is not very restrictive. The assumption that the K K matrix EðX<sup>0</sup> iW-1 XiÞ has rank K is the analogue of Assumption SOLS.2.

The usual motivation for the GLS estimator is to transform a system of equations where the error has nonscalar variance-covariance matrix into a system where the error vector has a scalar variance-covariance matrix. We obtain this by multiplying equation (7.9) by W-1=2 :

{168}------------------------------------------------

$$\mathbf{\Omega}^{-1/2}\mathbf{y}_i = (\mathbf{\Omega}^{-1/2}\mathbf{X}_i)\boldsymbol{\beta} + \mathbf{\Omega}^{-1/2}\mathbf{u}_i, \quad \text{or} \quad \mathbf{y}_i^* = \mathbf{X}_i^*\boldsymbol{\beta} + \mathbf{u}_i^*$$
 (7.28)

Simple algebra shows that  $E(\mathbf{u}_i^*\mathbf{u}_i^{*\prime}) = \mathbf{I}_G$ .

Now we estimate equation (7.28) by system OLS. (As yet, we have no real justification for this step, but we know SOLS is consistent under some assumptions.) Call this estimator  $\beta^*$ . Then

$$\boldsymbol{\beta}^* \equiv \left(\sum_{i=1}^N \mathbf{X}_i^{*\prime} \mathbf{X}_i^*\right)^{-1} \left(\sum_{i=1}^N \mathbf{X}_i^{*\prime} \mathbf{y}_i^*\right) = \left(\sum_{i=1}^N \mathbf{X}_i^{\prime} \mathbf{\Omega}^{-1} \mathbf{X}_i\right)^{-1} \left(\sum_{i=1}^N \mathbf{X}_i^{\prime} \mathbf{\Omega}^{-1} \mathbf{y}_i\right)$$
(7.29)

This is the generalized least squares (GLS) estimator of  $\beta$ . Under Assumption SGLS.2,  $\beta^*$  exists with probability approaching one as  $N \to \infty$ .

We can write  $\beta^*$  using full matrix notation as  $\beta^* = [\mathbf{X}'(\mathbf{I}_N \otimes \mathbf{\Omega}^{-1})\mathbf{X}]^{-1} \cdot [\mathbf{X}'(\mathbf{I}_N \otimes \mathbf{\Omega}^{-1})\mathbf{Y}]$ , where  $\mathbf{X}$  and  $\mathbf{Y}$  are the data matrices defined in Section 7.3.2 and  $\mathbf{I}_N$  is the  $N \times N$  identity matrix. But for establishing the asymptotic properties of  $\beta^*$ , it is most convenient to work with equation (7.29).

We can establish consistency of  $\beta^*$  under Assumptions SGLS.1 and SGLS.2 by writing

$$\boldsymbol{\beta}^* = \boldsymbol{\beta} + \left( N^{-1} \sum_{i=1}^N \mathbf{X}_i' \mathbf{\Omega}^{-1} \mathbf{X}_i \right)^{-1} \left( N^{-1} \sum_{i=1}^N \mathbf{X}_i' \mathbf{\Omega}^{-1} \mathbf{u}_i \right)$$
(7.30)

By the weak law of large numbers (WLLN),  $N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{X}_{i} \xrightarrow{p} \mathrm{E}(\mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{X}_{i})$ . By Assumption SGLS.2 and Slutsky's theorem (Lemma 3.4),  $\left(N^{-1} \sum_{i=1}^{N} \mathbf{X}_{i}' \mathbf{\Omega}^{-1} \mathbf{X}_{i}\right)^{-1} \xrightarrow{p} \mathbf{A}^{-1}$ , where **A** is now defined as

$$\mathbf{A} \equiv \mathbf{E}(\mathbf{X}_i' \mathbf{\Omega}^{-1} \mathbf{X}_i) \tag{7.31}$$

Now we must show that plim  $N^{-1}\sum_{i=1}^{N}\mathbf{X}_{i}'\mathbf{\Omega}^{-1}\mathbf{u}_{i}=\mathbf{0}$ . By the WLLN, it is sufficient that  $\mathbf{E}(\mathbf{X}_{i}'\mathbf{\Omega}^{-1}\mathbf{u}_{i})=\mathbf{0}$ . This is where Assumption SGLS.1 comes in. We can argue this point informally because  $\mathbf{\Omega}^{-1}\mathbf{X}_{i}$  is a linear combination of  $\mathbf{X}_{i}$ , and since each element of  $\mathbf{X}_{i}$  is uncorrelated with each element of  $\mathbf{u}_{i}$ , any linear combination of  $\mathbf{X}_{i}$  is uncorrelated with  $\mathbf{u}_{i}$ . We can also show this directly using the algebra of Kronecker products and vectorization. For conformable matrices  $\mathbf{D}$ ,  $\mathbf{E}$ , and  $\mathbf{F}$ , recall that  $\text{vec}(\mathbf{DEF})=(\mathbf{F}'\otimes\mathbf{D})\text{ vec}(\mathbf{E})$ , where  $\text{vec}(\mathbf{C})$  is the vectorization of the matrix  $\mathbf{C}$ . [That is,  $\text{vec}(\mathbf{C})$  is the column vector obtained by stacking the columns of  $\mathbf{C}$  from first to last; see Theil (1983).] Therefore, under Assumption SGLS.1,

$$\operatorname{vec} E(\mathbf{X}_{i}'\mathbf{\Omega}^{-1}\mathbf{u}_{i}) = E[(\mathbf{u}_{i}' \otimes \mathbf{X}_{i}')] \operatorname{vec}(\mathbf{\Omega}^{-1}) = E[(\mathbf{u}_{i} \otimes \mathbf{X}_{i})'] \operatorname{vec}(\mathbf{\Omega}^{-1}) = \mathbf{0}$$

{169}------------------------------------------------

where we have also used the fact that the expectation and vec operators can be interchanged. We can now read the consistency of the GLS estimator off of equation (7.30). We do not state this conclusion as a theorem because the GLS estimator itself is rarely available.

The proof of consistency that we have sketched fails if we only make Assumption SOLS.1:  $E(\mathbf{X}_i'\mathbf{u}_i) = \mathbf{0}$  does not imply  $E(\mathbf{X}_i'\Omega^{-1}\mathbf{u}_i) = \mathbf{0}$ , except when  $\Omega$  and  $\mathbf{X}_i$  have special structures. If Assumption SOLS.1 holds but Assumption SGLS.1 fails, the transformation in equation (7.28) generally induces correlation between  $\mathbf{X}_i^*$  and  $\mathbf{u}_i^*$ . This can be an important point, especially for certain panel data applications. If we are willing to make the zero conditional mean assumption (7.13),  $\boldsymbol{\beta}^*$  can be shown to be unbiased conditional on  $\mathbf{X}$ .