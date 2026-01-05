# Pooled Probit and Logit

> Pages: 491-492

In Section 13.8 we used a probit model to illustrate partial likelihood methods with panel data. Naturally, we can use logit or any other binary response function as well. Suppose the model is

$$P(y_{it} = 1 \mid \mathbf{x}_{it}) = G(\mathbf{x}_{it}\boldsymbol{\beta}), \qquad t = 1, 2, ..., T$$
 (15.57)

where  $G(\cdot)$  is a known function taking on values in the open unit interval. As we discussed in Chapter 13,  $\mathbf{x}_{it}$  can contain a variety of factors, including time dummies, interactions of time dummies with time-constant or time-varying variables, and lagged dependent variables.

In specifying the model (15.57) we have not assumed nearly enough to obtain the distribution of  $\mathbf{y}_i \equiv (y_{i1}, \dots, y_{iT})$  given  $\mathbf{x}_i = (\mathbf{x}_{i1}, \dots, \mathbf{x}_{iT})$ . Nevertheless, we can obtain a  $\sqrt{N}$ -consistent estimator of  $\boldsymbol{\beta}$  by maximizing the partial log-likelihood function

$$\sum_{i=1}^{N} \sum_{t=1}^{T} \{ y_{it} \log G(\mathbf{x}_{it} \boldsymbol{\beta}) + (1 - y_{it}) \log[1 - G(\mathbf{x}_{it} \boldsymbol{\beta})] \}$$

which is simply an exercise in pooled estimation. Without further assumptions, a robust variance matrix estimator is needed to account for serial correlation in the scores across t; see equation (13.53) with  $\hat{\beta}$  in place of  $\hat{\theta}$  and G in place of  $\Phi$ . Wald and score statistics can be computed as in Chapter 12.

In the case that the model (15.57) is dynamically complete, that is,

$$P(y_{it} = 1 \mid \mathbf{x}_{it}, y_{i,t-1}, \mathbf{x}_{i,t-1}, \ldots) = P(y_{it} = 1 \mid \mathbf{x}_{it})$$
(15.58)

{492}------------------------------------------------

inference is considerably easier: all the usual statistics from a probit or logit that pools observations and treats the sample as a long independent cross section of size NT are valid, including likelihood ratio statistics. Remember, we are definitely not assuming independence across t (for example, xit can contain lagged dependent variables). Dynamic completeness implies that the scores are serially uncorrelated across t, which is the key condition for the standard inference procedures to be valid. (See the general treatment in Section 13.8.)

To test for dynamic completeness, we can always add a lagged dependent variable and possibly lagged explanatory variables. As an alternative, we can derive a simple one-degree-of-freedom test that works regardless of what is in xit. For concreteness, we focus on the probit case; other index models are handled similarly. Define uit 1 yit Fðxit*b*Þ, so that, under assumption (15.58), Eðuit j xit; yi;t<sup>1</sup>; xi;t<sup>1</sup>; ...Þ ¼ 0, all t. It follows that uit is uncorrelated with any function of the variables ðxit; yi;t<sup>1</sup>; xi;t<sup>1</sup>; ...Þ, including ui;t1. By studying equation (13.53), we can see that it is serial correlation in the uit that makes the usual inference procedures invalid. Let u^it ¼ yit <sup>F</sup>ðxit ^*b*Þ. Then a simple test is available by using pooled probit to estimate the artificial model

$$\mathbf{P}(y_{it} = 1 \mid \mathbf{x}_{it}, \hat{\mathbf{u}}_{i,t-1}) = \Phi(\mathbf{x}_{it}\boldsymbol{\beta} + \gamma_1 \hat{\mathbf{u}}_{i,t-1})$$
(15.59)

using time periods t ¼ 2; ... ; T. The null hypothesis is H0: g<sup>1</sup> ¼ 0. If H0 is rejected, then so is assumption (15.58). This is a case where under the null hypothesis, the estimation of *b* required to obtain u^i;t<sup>1</sup> does not affect the limiting distribution of any of the usual test statistics, Wald, LR, or LM, of H0: g<sup>1</sup> ¼ 0. The Wald statistic, that is, the t statistic on g^1, is the easiest to obtain. For the LM and LR statistics we must be sure to drop the first time period in estimating the restricted model ðg<sup>1</sup> ¼ 0Þ.