# Estimation under Weaker Assumptions

> Pages: 489-491

Probit, logit, and the extensions of these mentioned in the previous subsection are all parametric models: P(y = 1 | x) depends on a finite number of parameters. There have been many recent advances in estimation of binary response models that relax parametric assumptions on P(y = 1 | x). We briefly discuss some of those here.

If we are interested in estimating the directions and relative sizes of the partial effects, and not the response probabilities, several approaches are possible. Ruud (1983) obtains conditions under which we can estimate the slope parameters, call these  $\beta$ , up to scale—that is, we can consistently estimate  $\tau \beta$  for some unknown constant  $\tau$ —even though we misspecify the function  $G(\cdot)$ . Ruud (1986) shows how to exploit these results to consistently estimate the slope parameters up to scale fairly generally.

An alternative approach is to recognize that we do not know the function  $G(\cdot)$ , but the response probability has the index form in equation (15.8). This arises from the latent variable formulation (15.9) when e is independent of  $\mathbf{x}$  but the distribution of e is not known. There are several **semiparametric estimators** of the slope parameters, up to scale, that do not require knowledge of G. Under certain restrictions on the function G and the distribution of  $\mathbf{x}$ , the semiparametric estimators are consistent and  $\sqrt{N}$ -asymptotically normal. See, for example, Stoker (1986); Powell, Stock, and Stoker (1989); Ichimura (1993); Klein and Spady (1993); and Ai (1997). Powell (1994) contains a recent survey of these methods.

Once  $\beta$  is obtained, the function G can be consistently estimated (in a sense we cannot make precise here, as G is part of an infinite dimensional space). Thus, the response probabilities, as well as the partial effects on these probabilities, can be consistently estimated for unknown G. Obtaining  $\hat{G}$  requires **nonparametric regression** 

{490}------------------------------------------------

of  $y_i$  on  $\mathbf{x}_i\hat{\boldsymbol{\beta}}$ , where  $\hat{\boldsymbol{\beta}}$  are the scaled slope estimators. Accessible treatments of the methods used are contained in Stoker (1992), Powell (1994), and Härdle and Linton (1994).

Remarkably, it is possible to estimate  $\beta$  up to scale without assuming that e and  $\mathbf{x}$  are independent in the model (15.9). In the specification  $y = 1[\mathbf{x}\boldsymbol{\beta} + e > 0]$ , Manski (1975, 1988) shows how to consistently estimate  $\beta$ , subject to a scaling, under the assumption that the median of e given  $\mathbf{x}$  is zero. Some mild restrictions are needed on the distribution of  $\mathbf{x}$ ; the most important of these is that at least one element of  $\mathbf{x}$  with nonzero coefficient is essentially continuous. This allows e to have any distribution, and e and  $\mathbf{x}$  can be dependent; for example,  $\mathrm{Var}(e \mid \mathbf{x})$  is unrestricted. Manski's estimator, called the **maximum score estimator**, is a least absolute deviations estimator. Since the median of y given  $\mathbf{x}$  is  $1[\mathbf{x}\boldsymbol{\beta}>0]$ , the maximum score estimator solves

$$\min_{\boldsymbol{\beta}} \sum_{i=1}^{N} |y_i - 1[\mathbf{x}_i \boldsymbol{\beta} > 0]|$$

over all  $\beta$  with, say,  $\beta'\beta = 1$ , or with some element of  $\beta$  fixed at unity if the corresponding  $x_j$  is known to appear in  $Med(y | \mathbf{x})$ . {A normalization is needed because if  $Med(y | \mathbf{x}) = 1[\mathbf{x}\beta > 0]$  then  $Med(y | \mathbf{x}) = 1[\mathbf{x}(\tau\beta) > 0]$  for any  $\tau > 0$ .} The resulting estimator is consistent—for a recent proof see Newey and McFadden (1994)—but its limiting distribution is nonnormal. In fact, it converges to its limiting distribution at rate  $N^{1/3}$ . Horowitz (1992) proposes a smoothed version of the maximum score estimator that converges at a rate close to  $\sqrt{N}$ .

The maximum score estimator's strength is that it consistently estimates  $\beta$  up to scale in cases where the index model (15.8) does not hold. In a sense, this is also the estimator's weakness, because it is not intended to deliver estimates of the response probabilities  $P(y=1|\mathbf{x})$ . In some cases we might only want to know the relative effects of each  $x_j$  on an underlying utility difference or unobserved willingness to pay  $(y^*)$ , and the maximum score estimator is well suited for that purpose. However, for most policy purposes we want to know the magnitude of the change in  $P(y=1|\mathbf{x})$  for a given change in  $x_j$ . As illustrated by the heteroskedasticity example in the previous subsection, where  $Var(e|x_1) = x_1^2$ , it is possible for  $\beta_j$  and  $\partial P(y=1|\mathbf{x})/\partial x_j$  to have opposite signs. More generally, for any variable y, it is possible that  $x_j$  has a positive effect on  $Med(y|\mathbf{x})$  but a negative effect on  $E(y|\mathbf{x})$ , or vice versa. This possibility raises the issue of what should be the focus, the median or the mean. For binary response, the conditional mean is the response probability.

It is also possible to estimate the parameters in a binary response model with endogenous explanatory variables without knowledge of  $G(\cdot)$ . Lewbel (1998) con-


{491}------------------------------------------------

tains some recent results. Apparently, methods for estimating average partial effects with endogenous explanatory variables and unknown  $G(\cdot)$  are not yet available.