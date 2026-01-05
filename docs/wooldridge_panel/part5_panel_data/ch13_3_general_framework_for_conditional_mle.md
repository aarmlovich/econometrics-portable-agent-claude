# General Framework for Conditional MLE

> Pages: 400-402

Let  $p_o(\mathbf{y} | \mathbf{x})$  denote the conditional density of  $\mathbf{y}_i$  given  $\mathbf{x}_i = \mathbf{x}$ , where  $\mathbf{y}$  and  $\mathbf{x}$  are dummy arguments. We index this density by "o" to emphasize that it is the true density of  $\mathbf{y}_i$  given  $\mathbf{x}_i$ , and not just one of many candidates. It will be useful to let  $\mathcal{X} \subset \mathbb{R}^K$  denote the possible values for  $\mathbf{x}_i$  and  $\mathcal{Y}$  denote the possible values of  $\mathbf{y}_i$ ;  $\mathcal{X}$  and  $\mathcal{Y}$  are called the *supports* of the random vectors  $\mathbf{x}_i$  and  $\mathbf{y}_i$ , respectively.

For a general treatment, we assume that, for all  $\mathbf{x} \in \mathcal{X}$ ,  $p_o(\cdot | \mathbf{x})$  is a density with respect to a  $\sigma$ -finite measure, denoted  $v(d\mathbf{y})$ . Defining a  $\sigma$ -finite measure would take us too far afield. We will say little more about the measure  $v(d\mathbf{y})$  because it does not play a crucial role in applications. It suffices to know that  $v(d\mathbf{y})$  can be chosen to allow  $\mathbf{y}_i$  to be discrete, continuous, or some mixture of the two. When  $\mathbf{y}_i$  is discrete, the measure  $v(d\mathbf{y})$  simply turns all integrals into sums; when  $\mathbf{y}_i$  is purely continuous, we obtain the usual Riemann integrals. Even in more complicated cases—where, say,  $\mathbf{y}_i$  has both discrete and continuous characteristics—we can get by with tools from basic probability without ever explicitly defining  $v(d\mathbf{y})$ . For more on measures and general integrals, you are referred to Billingsley (1979) and Davidson (1994, Chapters 3 and 4).

In Chapter 12 we saw how nonlinear least squares can be motivated by the fact that  $\mu_o(\mathbf{x}) \equiv \mathrm{E}(y \mid \mathbf{x})$  minimizes  $\mathrm{E}\{[y-m(\mathbf{x})]^2\}$  for all other functions  $m(\mathbf{x})$  with  $\mathrm{E}\{[m(\mathbf{x})]^2\} < \infty$ . Conditional maximum likelihood has a similar motivation. The result from probability that is crucial for applying the analogy principle is the **conditional Kullback-Leibler information inequality.** Although there are more general statements of this inequality, the following suffices for our purpose: for any nonnegative function  $f(\cdot \mid \mathbf{x})$  such that

$$\int_{\mathcal{Y}} f(\mathbf{y} \,|\, \mathbf{x}) \nu(d\mathbf{y}) = 1, \qquad \text{all } \mathbf{x} \in \mathcal{X}$$
(13.8)

Property CD.1 in the chapter appendix implies that

$$\mathcal{K}(f; \mathbf{x}) \equiv \int_{\mathcal{U}} \log[p_{o}(\mathbf{y} \mid \mathbf{x}) / f(\mathbf{y} \mid \mathbf{x})] p_{o}(\mathbf{y} \mid \mathbf{x}) \nu(d\mathbf{y}) \ge 0, \quad \text{all } \mathbf{x} \in \mathcal{X}$$
 (13.9)

Because the integral is identically zero for  $f = p_o$ , expression (13.9) says that, for each  $\mathbf{x}$ ,  $\mathcal{K}(f;\mathbf{x})$  is minimized at  $f = p_o$ .


{401}------------------------------------------------

We can apply inequality (13.9) to a parametric model for poð j xÞ,

$$\{f(\cdot \mid \mathbf{x}; \boldsymbol{\theta}), \ \boldsymbol{\theta} \in \boldsymbol{\Theta}, \ \boldsymbol{\Theta} \subset \mathbb{R}^{\mathbf{P}}\}\$$
 (13.10)

which we assume satisfies condition (13.8) for each x A X and each *y* A Y; if it does not, then fð j x; *y*Þ does not integrate to unity (with respect to the measure n), and as a result it is a very poor candidate for poðy j xÞ. Model (13.10) is a correctly specified model of the conditional density, poð j Þ, if, for some *y*<sup>o</sup> A Y,

$$f(\cdot | \mathbf{x}; \boldsymbol{\theta}_{o}) = p_{o}(\cdot | \mathbf{x}), \quad \text{all } \mathbf{x} \in \mathcal{X}$$
 (13.11)

As we discussed in Chapter 12, it is useful to use *y*<sup>o</sup> to distinguish the true value of the parameter from a generic element of Y. In particular examples, we will not bother making this distinction unless it is needed to make a point.

For each x A X, Kðf ; xÞ can be written as Eflog½ poðy<sup>i</sup> j xiÞ j x<sup>i</sup> ¼ xg Eflog½ fðy<sup>i</sup> j xiÞ j x<sup>i</sup> ¼ xg. Therefore, if the parametric model is correctly specified, then Eflog½ fðy<sup>i</sup> j xi; *y*oÞ j xig bEflog½ fðy<sup>i</sup> j xi; *y*Þ j xig, or

$$E[\ell_i(\boldsymbol{\theta}_0) \mid \mathbf{x}_i] \ge E[\ell_i(\boldsymbol{\theta}) \mid \mathbf{x}_i], \qquad \boldsymbol{\theta} \in \boldsymbol{\Theta}$$
(13.12)

where

$$\ell_i(\boldsymbol{\theta}) \equiv \ell(\mathbf{y}_i, \mathbf{x}_i, \boldsymbol{\theta}) \equiv \log f(\mathbf{y}_i | \mathbf{x}_i; \boldsymbol{\theta})$$
(13.13)

is the conditional log likelihood for observation i. Note that lið*y*Þ is a random function of *y*, since it depends on the random vector ðxi; yiÞ. By taking the expected value of expression (13.12) and using iterated expectations, we see that *y*<sup>o</sup> solves

$$\max_{\boldsymbol{\theta} \in \mathbf{\Theta}} E[\ell_i(\boldsymbol{\theta})] \tag{13.14}$$

where the expectation is with respect to the joint distribution of ðxi; yiÞ. The sample analogue of expression (13.14) is

$$\max_{\boldsymbol{\theta} \in \mathbf{\Theta}} N^{-1} \sum_{i=1}^{N} \log f(\mathbf{y}_i \mid \mathbf{x}_i; \boldsymbol{\theta})$$
 (13.15)

A solution to problem (13.15), assuming that one exists, is the conditional maximum likelihood estimator (CMLE) of *y*o, which we denote as ^*y*. We will sometimes drop ''conditional'' when it is not needed for clarity.

The CMLE is clearly an M-estimator, since a maximization problem is easily turned into a minimization problem: in the notation of Chapter 12, take w<sup>i</sup> 1 ðxi; yiÞ and qðwi; *y*Þ 1 log fðy<sup>i</sup> j xi; *y*Þ. As long as we keep track of the minus sign in front of the log likelihood, we can apply the results in Chapter 12 directly.

{402}------------------------------------------------

The motivation for the conditional MLE as a solution to problem (13.15) may appear backward if you learned about maximum likelihood estimation in an introductory statistics course. In a traditional framework, we would treat the  $\mathbf{x}_i$  as constants appearing in the distribution of  $\mathbf{y}_i$ , and we would define  $\hat{\boldsymbol{\theta}}$  as the solution to

$$\max_{\boldsymbol{\theta} \in \mathbf{\Theta}} \prod_{i=1}^{N} f(\mathbf{y}_i \mid \mathbf{x}_i; \boldsymbol{\theta})$$
 (13.16)

Under independence, the product in expression (13.16) is the model for the joint density of  $(\mathbf{y}_1, \dots, \mathbf{y}_N)$ , evaluated at the data. Because maximizing the function in (13.16) is the same as maximizing its natural log, we are led to problem (13.15). However, the arguments explaining why solving (13.16) should lead to a good estimator of  $\theta_0$  are necessarily heuristic. By contrast, the analogy principle applies directly to problem (13.15), and we need not assume that the  $\mathbf{x}_i$  are fixed.

In our two examples, the conditional log likelihoods are fairly simple.

Example 13.1 (continued): In the probit example, the log likelihood for observation i is  $\ell_i(\theta) = y_i \log \Phi(\mathbf{x}_i \theta) + (1 - y_i) \log[1 - \Phi(\mathbf{x}_i \theta)]$ .

Example 13.2 (continued): In the Poisson example,  $\ell_i(\theta) = -\exp(\mathbf{x}_i\theta) + y_i\mathbf{x}_i\theta - \log(y_i!)$ . Normally, we would drop the last term in defining  $\ell_i(\theta)$  because it does not affect the maximization problem.