# Weighted Estimators to Account for Stratification

> Pages: 600-604

With variable probability sampling, it is easy to construct weighted objective functions that produce consistent and asymptotically normal estimators of the population parameters. It is useful to define a set of binary variables that indicate whether a random draw w<sup>i</sup> is kept in the sample and, if so, which stratum it falls into:

$$r_{ij} = h_{ij}s_{ij} \tag{17.69}$$

By definition, rij ¼ 1 for at most one j. If hij ¼ 1 then rij ¼ sij. If rij ¼ 0 for all j ¼ 1; 2; ... ; J, then the random draw w<sup>i</sup> does not appear in the sample (and we do not know which stratum it belonged to).

With these definitions, we can define the weighted M-estimator, ^*y*w, as the solution to

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \sum_{i=1}^{N} \sum_{j=1}^{J} p_j^{-1} r_{ij} q(\mathbf{w}_i, \boldsymbol{\theta})$$
(17.70)


{601}------------------------------------------------

where  $q(\mathbf{w}, \boldsymbol{\theta})$  is the objective function that is chosen to identify the population parameters  $\boldsymbol{\theta}_0$ . Note how the outer summation is over all *potential* observations, that is, the observations that *would* appear in a random sample. The indicators  $r_{ij}$  simply pick out the observations that actually appear in the available sample, and these indicators also attach each observed data point to its stratum. The objective function (17.70) weights each observed data point in the sample by the inverse of the sampling probability. For implementation it is useful to write the objective function as

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \sum_{i=1}^{N_0} p_{j_i}^{-1} q(\mathbf{w}_i, \boldsymbol{\theta})$$
 (17.71)

where, without loss of generality, the data points actually observed are ordered  $i = 1, ..., N_0$ . Since  $j_i$  is the stratum for observation i,  $p_{j_i}^{-1}$  is the weight attached to observation i in the estimation. In practice, the  $p_{j_i}^{-1}$  are the **sampling weights** reported with other variables in stratified samples.

The objective function  $q(\mathbf{w}, \boldsymbol{\theta})$  contains all of the M-estimator examples we have covered so far in the book, including least squares (linear and nonlinear), conditional maximum likelihood, and partial maximum likelihood. In panel data applications, the probability weights are from sampling in an initial year. Weights for later years are intended to reflect both stratification (if any) and possible attrition, as discussed in Section 17.7.3 and in Wooldridge (2000d).

Wooldridge (1999b) shows that, under the same assumptions as Theorem 12.2 and the assumption that each sampling probability is strictly positive, the weighted Mestimator consistently estimates  $\theta_0$ , which is assumed to uniquely minimize  $E[q(\mathbf{w}, \theta)]$ . To see that the weighted objective function identifies  $\theta_0$ , we use the fact that  $h_j$  is independent of  $\mathbf{w}$  [and therefore of  $(\mathbf{w}, s_j)$  for each j], and so

$$E\left[\sum_{j=1}^{J} p_j^{-1} h_j s_j q(\mathbf{w}, \boldsymbol{\theta})\right] = \sum_{j=1}^{J} p_j^{-1} E(h_j) E[s_j q(\mathbf{w}, \boldsymbol{\theta})]$$

$$= \sum_{j=1}^{J} p_j^{-1} p_j E[s_j q(\mathbf{w}, \boldsymbol{\theta})] = E\left[\left(\sum_{j=1}^{J} s_j\right) q(\mathbf{w}, \boldsymbol{\theta})\right] = E[q(\mathbf{w}, \boldsymbol{\theta})]$$
(17.72)

where the final equality follows because the  $s_j$  sum to unity. Therefore, the expected value of the weighted objective function [over the distribution of  $(\mathbf{w}, \mathbf{h})$ ] equals the expected value of  $q(\mathbf{w}, \boldsymbol{\theta})$  (over the distribution of  $\mathbf{w}$ ). Consistency of the weighted Mestimator follows under the regularity conditions in Theorem 12.2.

Asymptotic normality also follows under the same regularity conditions as in Chapter 12. Wooldridge (1999b) shows that a valid estimator of the asymptotic

{602}------------------------------------------------

variance of  $\hat{\boldsymbol{\theta}}_{w}$  is

$$\left[\sum_{i=1}^{N_0} p_{j_i}^{-1} \nabla_{\theta}^2 q_i(\hat{\boldsymbol{\theta}}_w)\right]^{-1} \left[\sum_{i=1}^{N_0} p_{j_i}^{-2} \nabla_{\theta} q_i(\hat{\boldsymbol{\theta}}_w)' \nabla_{\theta} q_i(\hat{\boldsymbol{\theta}}_w)\right] \left[\sum_{i=1}^{N_0} p_{j_i}^{-1} \nabla_{\theta}^2 q_i(\hat{\boldsymbol{\theta}}_w)\right]^{-1}$$
(17.73)

which looks like the standard formula for a robust variance matrix estimator except for the presence of the sampling probabilities  $p_i$ .

When **w** partitions as  $(\mathbf{x}, \mathbf{y})$ , an alternative estimator replaces the Hessian  $\nabla_{\theta}^2 q_i(\hat{\boldsymbol{\theta}}_w)$  in expression (17.73) with  $\mathbf{A}(\mathbf{x}_i, \hat{\boldsymbol{\theta}}_w)$ , where  $\mathbf{A}(\mathbf{x}_i, \boldsymbol{\theta}_o) \equiv \mathrm{E}[\nabla_{\theta}^2 q(\mathbf{w}_i, \boldsymbol{\theta}_o) \mid \mathbf{x}_i]$ , as in Chapter 12. Asymptotic standard errors and Wald statistics can be obtained using either estimate of the asymptotic variance.

Example 17.10 (Linear Model under Stratified Sampling): In estimating the linear model

$$y = \mathbf{x}\boldsymbol{\beta}_0 + u, \qquad \mathbf{E}(\mathbf{x}'u) = \mathbf{0} \tag{17.74}$$

by weighted least squares, the asymptotic variance matrix estimator is

$$\left(\sum_{i=1}^{N_0} p_{j_i}^{-1} \mathbf{x}_i' \mathbf{x}_i\right)^{-1} \left(\sum_{i=1}^{N_0} p_{j_i}^{-2} \hat{\mathbf{u}}_i^2 \mathbf{x}_i' \mathbf{x}_i\right) \left(\sum_{i=1}^{N_0} p_{j_i}^{-1} \mathbf{x}_i' \mathbf{x}_i\right)^{-1}$$
(17.75)

where  $\hat{u}_i = y_i - \mathbf{x}_i \hat{\boldsymbol{\beta}}_w$  is the residual after WLS estimation. Interestingly, this is simply the White (1980b) heteroskedasticity-consistent covariance matrix estimator applied to the stratified sample, where all variables for observation i are weighted by  $p_{j_i}^{-1/2}$  before performing the regression. This estimator has been suggested by, among others, Hausman and Wise (1981). Hausman and Wise use maximum likelihood to obtain more efficient estimators in the context of the normal linear regression model, that is,  $u \mid \mathbf{x} \sim \text{Normal}(\mathbf{x}\boldsymbol{\beta}_0, \sigma_0^2)$ . Because of stratification, MLE is not generally robust to failure of the homoskedastic normality assumption.

It is important to remember that the form of expression (17.75) in this example is not due to potential heteroskedasticity in the underlying population model. Even if  $E(u^2 \mid \mathbf{x}) = \sigma_o^2$ , the estimator (17.75) is generally needed because of the stratified sampling. This estimator also works in the presence of heteroskedasticity of arbitrary and unknown form in the population, and it is routinely computed by many regression packages.

Example 17.11 (Conditional MLE under Stratified Sampling): When  $f(\mathbf{y} | \mathbf{x}; \boldsymbol{\theta})$  is a correctly specified model for the density of  $\mathbf{y}_i$  given  $\mathbf{x}_i$  in the population, the inverse-probability-weighted MLE is obtained with  $q_i(\boldsymbol{\theta}) \equiv -\log[f(\mathbf{y}_i | \mathbf{x}_i; \boldsymbol{\theta})]$ . This estimator

{603}------------------------------------------------

is consistent and asymptotically normal, with asymptotic variance estimator given by expression (17.73) [or, preferably, the form that uses  $\mathbf{A}(\mathbf{x}_i, \hat{\boldsymbol{\theta}}_w)$ ].

A weighting scheme is also available in the standard stratified sampling case, but the weights are different from the VP sampling case. To derive them, let  $Q_j = P(\mathbf{w} \in \mathcal{W}_j)$  denote the population frequency for stratum j; we assume that the  $Q_j$  are *known*. By the law of iterated expectations,

$$E[q(\mathbf{w}, \boldsymbol{\theta})] = Q_1 E[q(\mathbf{w}, \boldsymbol{\theta}) \mid \mathbf{w} \in \mathcal{W}_1] + \dots + Q_J E[q(\mathbf{w}, \boldsymbol{\theta}) \mid \mathbf{w} \in \mathcal{W}_J]$$
(17.76)

for any  $\theta$ . For each j,  $\mathrm{E}[q(\mathbf{w}, \theta) \,|\, \mathbf{w} \in \mathcal{W}_j]$  can be consistently estimated using a random sample obtained from stratum j. This scheme leads to the sample objective function

$$Q_1 \left[ N_1^{-1} \sum_{i=1}^{N_1} q(\mathbf{w}_{i1}, \boldsymbol{\theta}) \right] + \dots + Q_J \left[ N_J^{-1} \sum_{i=1}^{N_J} q(\mathbf{w}_{iJ}, \boldsymbol{\theta}) \right]$$

where  $\mathbf{w}_{ij}$  denotes a random draw *i* from stratum *j* and  $N_j$  is the nonrandom sample size for stratum *j*. We can apply the uniform law of large numbers to each term, so that the sum converges uniformly to equation (17.76) under the regularity conditions in Chapter 12. By multiplying and dividing each term by the total number of observations  $N = N_1 + \cdots + N_J$ , we can write the sample objective function more simply as

$$N^{-1} \sum_{i=1}^{N} (Q_{j_i}/H_{j_i}) q(\mathbf{w}_i, \boldsymbol{\theta})$$
 (17.77)

where  $j_i$  denotes the stratum for observation i and  $H_j \equiv N_j/N$  denotes the fraction of observations in stratum j. Because we have the stratum indicator  $j_i$ , we can drop the j subscript on  $\mathbf{w}_i$ . When we omit the division by N, equation (17.77) has the same form as equation (17.71), but the weights are  $(Q_{j_i}/H_{j_i})$  rather than  $p_{j_i}^{-1}$  (and the arguments for why each weighting works are very different). Also, in general, the formula for the asymptotic variance is different in the SS sampling case. In addition to the minor notational change of replacing  $N_0$  with N, the middle matrix in equation (17.73) becomes

$$\sum_{j=1}^J (Q_j^2/H_j^2) \left[ \sum_{i=1}^{N_j} (\nabla_{\!\theta} \hat{q}_{ij} - \overline{\nabla_{\!\theta} q_j})' (\nabla_{\!\theta} \hat{q}_{ij} - \overline{\nabla_{\!\theta} q_j}) \right]$$

where  $\nabla_{\theta}\hat{q}_{ij} \equiv \nabla_{\theta}q(\mathbf{w}_{ij},\hat{\boldsymbol{\theta}}_w)$  and  $\overline{\nabla_{\theta}q_j} \equiv N_j^{-1}\sum_{i=1}^{N_j}\nabla_{\theta}\hat{q}_{ij}$  (the within-stratum sample average). This approach requires us to explicitly partition observations into their respective strata. See Wooldridge (2001) for a detailed derivation. [If in the VP

{604}------------------------------------------------

sampling case the population frequencies Qj are known, it is better to use as weights Qj=ðNj=N0Þ rather than p<sup>1</sup> <sup>j</sup> , which makes the analysis look just like the SS sampling case. See Wooldridge (1999b) for details.]

If in Example 17.11 we have standard stratified sampling rather than VP sampling, the weighted MLE is typically called the weighted exogenous sample MLE (WESMLE); this estimator was suggested by Manski and Lerman (1977) in the context of choice-based sampling in discrete response models. [Actually, Manski and Lerman (1977) use multinomial sampling where Hj is the probability of picking stratum j. But Cosslett (1981) showed that a more efficient estimator is obtained by using Nj=N, as one always does in the case of SS sampling; see Wooldridge (1999b) for an extension of Cosslett's result to the M-estimator case.]

Provided that the sampling weights Qji =Hji or p<sup>1</sup> ji are given (along with the stratum), analysis with the weighted M-estimator under SS or VP sampling is fairly straightforward, but it is not likely to be efficient. In the conditional maximum likelihood case it is certainly possible to do better. See Imbens and Lancaster (1996) for a careful treatment.