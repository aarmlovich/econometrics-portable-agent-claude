# General Models with Individual-Specific Slopes

> Pages: 328-343

We now consider a more general model with interactions between time-varying explanatory variables and some unobservable, time-constant variables:

{329}------------------------------------------------

$$y_{it} = \mathbf{z}_{it}\mathbf{a}_i + \mathbf{x}_{it}\boldsymbol{\beta} + u_{it}, \qquad t = 1, 2, \dots, T$$

$$(11.43)$$

where zit is 1 J, a<sup>i</sup> is J 1, xit is 1 K, and *b* is K 1. The standard unobserved effects model is a special case with zit 1 1; the random trend model is a special case with zit ¼ z<sup>t</sup> ¼ ð1; tÞ.

Equation (11.43) allows some time-constant unobserved heterogeneity, contained in the vector ai, to interact with some of the observable explanatory variables. For example, suppose that progit is a program participation indicator and yit is an outcome variable. The model

$$y_{it} = \mathbf{x}_{it}\boldsymbol{\beta} + a_{i1} + a_{i2} \cdot prog_{it} + u_{it}$$

allows the effect of the program to depend on the unobserved effect ai<sup>2</sup> (which may or may not be tied to ai1). While we are interested in estimating *b*, we are also interested in the average effect of the program, m<sup>2</sup> ¼ Eðai2Þ. We cannot hope to get good estimators of the ai<sup>2</sup> in the usual case of small T. Polachek and Kim (1994) study such models, where the return to experience is allowed to be person-specific. Lemieux (1998) estimates a model where unobserved heterogeneity is rewarded differently in the union and nonunion sectors.

In the general model, we initially focus on estimating *b* and then turn to estimation of *a* ¼ EðaiÞ, which is the vector of average partial effects for the covariates zit. The strict exogeneity assumption is the natural extension of assumption (11.39):

ASSUMPTION FE.1': 
$$E(u_{it} | \mathbf{z}_i, \mathbf{x}_i, \mathbf{a}_i) = 0, t = 1, 2, ..., T.$$

Along with equation (11.43), Assumption FE.1<sup>0</sup> is equivalent to

$$E(y_{it} | \mathbf{z}_{i1}, \dots, \mathbf{z}_{iT}, \mathbf{x}_{i1}, \dots, \mathbf{x}_{iT}, \mathbf{a}_i) = E(y_{it} | \mathbf{z}_{it}, \mathbf{x}_{it}, \mathbf{a}_i) = \mathbf{z}_{it}\mathbf{a}_i + \mathbf{x}_{it}\boldsymbol{\beta}$$

which says that, once zit, xit, and a<sup>i</sup> have been controlled for, ðzis; xisÞ for s0t do not help to explain yit.

Define Z<sup>i</sup> as the T J matrix with tth row zit, and similarly for the T K matrix Xi. Then equation (11.43) can be written as

$$\mathbf{y}_i = \mathbf{Z}_i \mathbf{a}_i + \mathbf{X}_i \boldsymbol{\beta} + \mathbf{u}_i \tag{11.44}$$

Assuming that Z<sup>0</sup> <sup>i</sup>Z<sup>i</sup> is nonsingular (technically, with probability one), define

$$\mathbf{M}_{i} \equiv \mathbf{I}_{T} - \mathbf{Z}_{i} (\mathbf{Z}_{i}^{\prime} \mathbf{Z}_{i})^{-1} \mathbf{Z}_{i}^{\prime}$$
(11.45)

the projection matrix onto the null space of Z<sup>i</sup> [the matrix ZiðZ<sup>0</sup> <sup>i</sup>ZiÞ 1 Z0 <sup>i</sup> is the projection matrix onto the column space of Zi]. In other words, for each cross section observation i, Miy<sup>i</sup> is the T 1 vector of residuals from the time series regression

{330}------------------------------------------------

$$y_{it}$$
 on  $\mathbf{z}_{it}$ ,  $t = 1, 2, \dots, T$  (11.46)

In the basic fixed effects case, regression (11.46) is the regression  $y_{it}$  on 1, t = 1, 2, ..., T, and the residuals are simply the time-demeaned variables. In the random trend case, the regression is  $y_{it}$  on 1, t, t = 1, 2, ..., T, which linearly detrends  $y_{it}$  for each i.

The  $T \times K$  matrix  $\mathbf{M}_i \mathbf{X}_i$  contains as its rows the  $1 \times K$  vectors of residuals from the regression  $\mathbf{x}_{it}$  on  $\mathbf{z}_{it}$ , t = 1, 2, ..., T. The usefulness of premultiplying by  $\mathbf{M}_i$  is that it allows us to eliminate the unobserved effect  $\mathbf{a}_i$  by premultiplying equation (11.44) through by  $\mathbf{M}_i$  and noting that  $\mathbf{M}_i \mathbf{Z}_i = \mathbf{0}$ :

$$\ddot{\mathbf{y}}_{i} = \ddot{\mathbf{X}}_{i}\boldsymbol{\beta} + \ddot{\mathbf{u}}_{i} \tag{11.47}$$

where  $\ddot{\mathbf{y}}_i = \mathbf{M}_i \mathbf{y}_i$ ,  $\ddot{\mathbf{X}}_i = \mathbf{M}_i \mathbf{X}_i$ , and  $\ddot{\mathbf{u}}_i = \mathbf{M}_i \mathbf{u}_i$ . This is an extension of the within transformation used in basic fixed effects estimation.

To consistently estimate  $\beta$  by system OLS on equation (11.47), we make the following assumption:

ASSUMPTION FE.2': rank  $E(\ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i) = K$ , where  $\ddot{\mathbf{X}}_i = \mathbf{M}_i\mathbf{X}_i$ .

The rank of  $\mathbf{M}_i$  is T - J, so a necessary condition for Assumption FE.2' is J < T. In other words, we must have at least one more time period than the number of elements in  $\mathbf{a}_i$ . In the basic unobserved effects model, J = 1, and we know that  $T \ge 2$  is needed. In the random trend model, J = 2, and we need  $T \ge 3$  to estimate  $\beta$ .

The system OLS estimator of equation (11.47) is

$$\hat{\boldsymbol{\beta}}_{FE} = \left(\sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \ddot{\mathbf{X}}_{i}\right)^{-1} \left(\sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \ddot{\mathbf{y}}_{i}\right) = \boldsymbol{\beta} + \left(N^{-1} \sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \ddot{\mathbf{X}}_{i}\right)^{-1} \left(N^{-1} \sum_{i=1}^{N} \ddot{\mathbf{X}}_{i}' \mathbf{u}_{i}\right)$$

Under Assumption FE.1',  $E(\ddot{\mathbf{X}}_i'\mathbf{u}_i) = \mathbf{0}$ , and under Assumption FE.2', rank  $E(\ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i) = K$ , and so the usual consistency argument goes through. Generally, it is possible that for some observations,  $\ddot{\mathbf{X}}_i'\ddot{\mathbf{X}}_i$  has rank less than K. For example, this result occurs in the standard fixed effects case when  $\mathbf{x}_{it}$  does not vary over time for unit i. However, under Assumption FE.2',  $\hat{\boldsymbol{\beta}}_{FE}$  should be well defined unless our cross section sample size is small or we are unlucky in obtaining the sample.

Naturally, the FE estimator is  $\sqrt{N}$ -asymptotically normally distributed. To obtain the simplest expression for its asymptotic variance, we add the assumptions of constant conditional variance and no (conditional) serial correlation on the idiosyncratic errors  $\{u_{it}: t = 1, 2, ..., T\}$ .

ASSUMPTION FE.3':  $E(\mathbf{u}_i \mathbf{u}_i' | \mathbf{z}_i, \mathbf{x}_i, \mathbf{a}_i) = \sigma_u^2 \mathbf{I}_T$ .


{341}------------------------------------------------

One complication that arises in cluster samples, which we have not yet addressed, is that the number of observations within a cluster usually differs across clusters. Nevertheless, for cluster i, we can write

$$\mathbf{y}_i = \mathbf{X}_i \boldsymbol{\beta} + c_i \mathbf{j}_{G_i} + \mathbf{u}_i \tag{11.74}$$

where the row dimension of yi, Xi, jGi , and u<sup>i</sup> is Gi, the number of units in cluster i. The dimension of *b* is K 1.

To apply the panel data methods we have discussed so far, we assume that the number of clusters, N, is large, because we fix the number of units within each cluster in analyzing the asymptotic properties of the estimators. Because the dimension of the vectors and matrix in equation (11.74) changes with i, we cannot assume an identical distribution across i. However, in most cases it is reasonable to assume that the observations are independent across cluster. The fact that they are not also identically distributed makes the theory more complicated but has no practical consequences.

The strict exogeneity assumption in the model (11.73) requires that the error uis be uncorrelated with the explanatory variables for all units within cluster i. This assumption is often reasonable when a cluster effect ci is explicitly included. (In other words, we assume strict exogeneity conditional on ci.) If we also assume that ci is uncorrelated with xis for all s ¼ 1; ... ; Gi, then pooled OLS across all clusters and units is consistent as N ! y. However, the composite error will be correlated within cluster, just as in a random effects analysis. Even with different cluster sizes a valid variance matrix for pooled OLS is easy to obtain: just use formula (7.26) but where ^vi, the Gi 1 vector of pooled OLS residuals for cluster i, replaces ^ui. The resulting variance matrix estimator is robust to any kind of intracluster correlation and arbitrary heteroskedasticity, provided N is large relative to the Gi.

In the hierarchical models literature, ci is often allowed to depend on cluster-level covariates, for example, ci ¼ d<sup>0</sup> þ wi*d* þ ai, where ai is assumed to be independent of (or at least uncorrelated with) w<sup>i</sup> and xis, s ¼ 1; ... ; Gi. But this is equivalent to simply adding cluster-level observables to the original model and relabeling the unobserved cluster effect.

The fixed effects transformation can be used to eliminate ci in equation (11.74) when ci is thought to be correlated with xis. The different cluster sizes cause no problems here: demeaning is done within each cluster. Any explanatory variable that is constant within each cluster for all clusters—for example, the gender of the teacher if the clusters are elementary school classrooms—is eliminated, just as in the panel data case. Pooled OLS can be applied to the demeaned data, just as with panel data. Under the immediate generalizations of Assumptions FE.1–FE.3 to allow for different cluster sizes, the variance matrix of the FE estimator for cluster samples can be 

{342}------------------------------------------------

estimated as in expression (10.54), but  $\sigma_u^2$  must be estimated with care. A consistent estimator is  $\hat{\sigma}_u^2 = \text{SSR}/[\sum_{i=1}^N (G_i - 1) - K]$ , which is exactly the estimator that would be obtained from the pooled regression that includes a dummy variable for each cluster. The robust variance matrix (10.59) is valid very generally, where  $\hat{\mathbf{u}}_i = \ddot{\mathbf{y}}_i - \ddot{\mathbf{x}}_i \hat{\boldsymbol{\beta}}_{FF}$ , as usual.

The 2SLS estimator described in Section 11.1.3 can also be applied to cluster samples, once we adjust for different cluster sizes in doing the within-cluster demeaning.

Rather than include a cluster effect,  $c_i$ , sometimes the goal is to see whether person s within cluster i is affected by the characteristics of other people within the cluster. One way to estimate the importance of **peer effects** is to specify

$$y_{is} = \mathbf{x}_{is}\boldsymbol{\beta} + \overline{\mathbf{w}}_{i(s)}\boldsymbol{\delta} + v_{is} \tag{11.75}$$

where  $\overline{\mathbf{w}}_{i(s)}$  indicates averages of a subset of elements of  $\mathbf{x}_{is}$  across all other people in the cluster. If equation (11.75) represents  $\mathrm{E}(y_{is} \,|\, \mathbf{x}_i) = \mathrm{E}(y_{is} \,|\, \mathbf{x}_{is}, \overline{\mathbf{w}}_{i(s)})$  for each s, then the strict exogeneity assumption  $\mathrm{E}(v_{is} \,|\, \mathbf{x}_i) = 0$ ,  $s = 1, \ldots, G_i$ , necessarily holds. Pooled OLS will consistently estimate  $\boldsymbol{\beta}$  and  $\boldsymbol{\delta}$ , although a robust variance matrix may be needed to account for correlation in  $v_{is}$  across s, and possibly for heteroskedasticity. If  $\mathrm{Cov}(v_{is}, v_{ir} \,|\, \mathbf{x}_i) = 0$ ,  $s \neq r$ , and  $\mathrm{Var}(v_{is} \,|\, \mathbf{x}_i) = \sigma_v^2$  are assumed, then pooled OLS is efficient, and the usual test standard errors and test statistics are valid. It is also easy to allow the unconditional variance to change across cluster using a simple weighting; for a similar example, see Problem 7.7.

We can also apply the more general models from Section 11.2.2, where unobserved cluster effects interact with some of the explanatory variables. If we allow arbitrary dependence between the cluster effects and the explanatory variables, the transformations in Section 11.2.2 should be used. In the hierarchical models literature, the unobserved cluster effects are assumed to be either independent of the covariates  $\mathbf{x}_{is}$  or independent of the covariates after netting out observed cluster covariates. This assumption results in a particular form of heteroskedasticity that can be exploited for efficiency. However, it makes as much sense to include cluster-level covariates, individual-level covariates, and possibly interactions of these in an initial model, and then to make inference in pooled OLS robust to arbitrary heteroskedasticity and cluster correlation. (See Problem 11.5 for a related analysis in the context of panel data.)

We should remember that the methods described in this section are known to have good properties only when the number of clusters is large relative to the number of units within a cluster. Case and Katz (1991) and Evans, Oates, and Schwab (1992) apply cluster-sampling methods to the problem of estimating peer effects.

{343}------------------------------------------------