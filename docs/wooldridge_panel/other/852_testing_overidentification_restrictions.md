# **8.5.2** Testing Overidentification Restrictions

> Pages: 214-215

Just as in the case of single-equation analysis with more exogenous variables than explanatory variables, we can test whether overidentifying restrictions are valid in a system context. In the model (8.11) with instrument matrix  $\mathbf{Z}_i$ , where  $\mathbf{X}_i$  is  $G \times K$  and  $\mathbf{Z}_i$  is  $G \times L$ , there are overidentifying restrictions if L > K. Assuming that  $\hat{\mathbf{W}}$  is an optimal weighting matrix, it can be shown that

$$\left(N^{-1/2} \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{u}}_{i}\right)' \hat{\mathbf{W}} \left(N^{-1/2} \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{u}}_{i}\right) \stackrel{a}{\sim} \chi_{L-K}^{2}$$

$$(8.49)$$

under the null hypothesis  $H_0$ :  $E(\mathbf{Z}_i'\mathbf{u}_i) = \mathbf{0}$ . The asymptotic  $\chi^2_{L-K}$  distribution is similar to result (8.44), but expression (8.44) contains the unobserved errors,  $\mathbf{u}_i$ , whereas expression (8.49) contains the residuals,  $\hat{\mathbf{u}}_i$ . Replacing  $\mathbf{u}_i$  with  $\hat{\mathbf{u}}_i$  causes the degrees of freedom to fall from L to L - K: in effect, K orthogonality conditions have been used to compute  $\hat{\boldsymbol{\beta}}$ , and L - K are left over for testing.

The **overidentification test statistic** in expression (8.49) is just the objective function (8.23) evaluated at the solution  $\hat{\beta}$  and divided by N. It is because of expression (8.49) that the GMM estimator using the optimal weighting matrix is called the minimum chi-square estimator:  $\hat{\beta}$  is chosen to make the minimum of the objective function have an asymptotic chi-square distribution. If  $\hat{\mathbf{W}}$  is not optimal, expression (8.49) fails to hold, making it much more difficult to test the overidentifying restrictions. When L = K, the left-hand side of expression (8.49) is identically zero; there are no overidentifying restrictions to be tested.

Under Assumption SIV.5, the 3SLS estimator is a minimum chi-square estimator, and the overidentification statistic in equation (8.49) can be written as

$$\left(\sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{u}}_{i}\right)' \left(\sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{\Omega}} \mathbf{Z}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{u}}_{i}\right)$$
(8.50)

Without Assumption SIV.5, the limiting distribution of this statistic is not chi square. In the case where the model has the form (8.12), overidentification test statistics can be used to choose between a systems and a single-equation method. For example, if the test statistic (8.50) rejects the overidentifying restrictions in the entire system, then the 3SLS estimators of the first equation are generally inconsistent. Assuming that the single-equation 2SLS estimation passes the overidentification test discussed in Chapter 6, 2SLS would be preferred. However, in making this judgment it is, as always, important to compare the magnitudes of the two sets of estimates in addition

{215}------------------------------------------------

to the statistical significance of test statistics. Hausman (1983, p. 435) shows how to construct a statistic based directly on the 3SLS and 2SLS estimates of a particular equation (assuming that 3SLS is asymptotically more efficient under the null), and this discussion can be extended to allow for the more general minimum chi-square estimator.