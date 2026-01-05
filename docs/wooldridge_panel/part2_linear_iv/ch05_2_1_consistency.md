# Consistency

> Pages: 107-109

We now summarize asymptotic results for 2SLS in a single-equation model with perhaps several endogenous variables among the explanatory variables. Write the population model as in equation (5.7), where x is 1 K and generally includes unity. Several elements of x may be correlated with u. As usual, we assume that a random sample is available from the population.

{108}------------------------------------------------

assumption 2SLS.1: For some 1 L vector z, Eðz<sup>0</sup> uÞ ¼ 0.

Here we do not specify where the elements of z come from, but any exogenous elements of x, including a constant, are included in z. Unless every element of x is exogenous, z will have to contain variables obtained from outside the model. The zero conditional mean assumption, Eðu j zÞ ¼ 0, implies Assumption 2SLS.1.

The next assumption contains the general rank condition for single-equation analysis.

ASSUMPTION 2SLS.2: (a) rank 
$$E(\mathbf{z}'\mathbf{z}) = L$$
; (b) rank  $E(\mathbf{z}'\mathbf{x}) = K$ .

Technically, part a of this assumption is needed, but it is not especially important, since the exogenous variables, unless chosen unwisely, will be linearly independent in the population (as well as in a typical sample). Part b is the crucial rank condition for identification. In a precise sense it means that z is sufficiently linearly related to x so that rank Eðz<sup>0</sup> xÞ has full column rank. We discussed this concept in Section 5.1 for the situation in which x contains a single endogenous variable. When x is exogenous, so that z ¼ x, Assumption 2SLS.1 reduces to Assumption OLS.1 and Assumption 2SLS.2 reduces to Assumption OLS.2.

Necessary for the rank condition is the order condition, L bK. In other words, we must have at least as many instruments as we have explanatory variables. If we do not have as many instruments as right-hand-side variables, then *b* is not identified. However, L bK is no guarantee that 2SLS.2b holds: the elements of z might not be appropriately correlated with the elements of x.

We already know how to test Assumption 2SLS.2b with a single endogenous explanatory variable. In the general case, it is possible to test Assumption 2SLS.2b, given a random sample on ðx; zÞ, essentially by performing tests on the sample analogue of Eðz<sup>0</sup> xÞ, Z<sup>0</sup> X=N. The tests are somewhat complicated; see, for example Cragg and Donald (1996). Often we estimate the reduced form for each endogenous explanatory variable to make sure that at least one element of z not in x is significant. This is not sufficient for the rank condition in general, but it can help us determine if the rank condition fails.

Using linear projections, there is a simple way to see how Assumptions 2SLS.1 and 2SLS.2 identify *b*. First, assuming that Eðz<sup>0</sup> zÞ is nonsingular, we can always write the linear projection of x onto z as x ¼ zP, where P is the L K matrix P ¼ ½Eðz<sup>0</sup> zÞ-1 Eðz<sup>0</sup> xÞ. Since each column of P can be consistently estimated by regressing the appropriate element of x onto z, for the purposes of identification of *b*, we can treat P as known. Write x ¼ x þ r, where Eðz<sup>0</sup> rÞ ¼ 0 and so Eðx0rÞ ¼ 0. Now, the 2SLS estimator is effectively the IV estimator using instruments x. Multiplying

{109}------------------------------------------------

equation (5.7) by  $\mathbf{x}^{*\prime}$ , taking expectations, and rearranging gives

$$\mathbf{E}(\mathbf{x}^{*\prime}\mathbf{x})\boldsymbol{\beta} = \mathbf{E}(\mathbf{x}^{*\prime}y) \tag{5.21}$$

since  $E(\mathbf{x}^{*\prime}u) = \mathbf{0}$ . Thus,  $\boldsymbol{\beta}$  is identified by  $\boldsymbol{\beta} = [E(\mathbf{x}^{*\prime}\mathbf{x})]^{-1}E(\mathbf{x}^{*\prime}y)$  provided  $E(\mathbf{x}^{*\prime}\mathbf{x})$  is nonsingular. But

$$E(\mathbf{x}^{*'}\mathbf{x}) = \mathbf{\Pi}' E(\mathbf{z}'\mathbf{x}) = E(\mathbf{x}'\mathbf{z})[E(\mathbf{z}'\mathbf{z})]^{-1}E(\mathbf{z}'\mathbf{x})$$

and this matrix is nonsingular if and only if  $E(\mathbf{z}'\mathbf{x})$  has rank K; that is, if and only if Assumption 2SLS.2b holds. If 2SLS.2b fails, then  $E(\mathbf{x}^{*'}\mathbf{x})$  is singular and  $\boldsymbol{\beta}$  is not identified. [Note that, because  $\mathbf{x} = \mathbf{x}^* + \mathbf{r}$  with  $E(\mathbf{x}^{*'}\mathbf{r}) = \mathbf{0}$ ,  $E(\mathbf{x}^{*'}\mathbf{x}) = E(\mathbf{x}^{*'}\mathbf{x}^*)$ . So  $\boldsymbol{\beta}$  is identified if and only if rank  $E(\mathbf{x}^{*'}\mathbf{x}^*) = K$ .]

The 2SLS estimator can be written as in equation (5.17) or as

$$\hat{\boldsymbol{\beta}} = \left[ \left( \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{z}_{i} \right) \left( \sum_{i=1}^{N} \mathbf{z}_{i}' \mathbf{z}_{i} \right)^{-1} \left( \sum_{i=1}^{N} \mathbf{z}_{i}' \mathbf{x}_{i} \right) \right]^{-1} \left( \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{z}_{i} \right) \left( \sum_{i=1}^{N} \mathbf{z}_{i}' \mathbf{z}_{i} \right)^{-1} \left( \sum_{i=1}^{N} \mathbf{z}_{i}' y_{i} \right)$$
(5.22)

We have the following consistency result.

THEOREM 5.1 (Consistency of 2SLS): Under Assumptions 2SLS.1 and 2SLS.2, the 2SLS estimator obtained from a random sample is consistent for  $\beta$ .

Proof: Write

$$\hat{\boldsymbol{\beta}} = \boldsymbol{\beta} + \left[ \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{z}_{i} \right) \left( N^{-1} \sum_{i=1}^{N} \mathbf{z}_{i}' \mathbf{z}_{i} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{z}_{i}' \mathbf{x}_{i} \right) \right]^{-1} \cdot \left( N^{-1} \sum_{i=1}^{N} \mathbf{x}_{i}' \mathbf{z}_{i} \right) \left( N^{-1} \sum_{i=1}^{N} \mathbf{z}_{i}' \mathbf{z}_{i} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{z}_{i}' u_{i} \right)$$

and, using Assumptions 2SLS.1 and 2SLS.2, apply the law of large numbers to each term along with Slutsky's theorem.