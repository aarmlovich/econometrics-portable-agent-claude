# Average Partial Effects

> Pages: 39-41

When we explicitly allow the expectation of the response variable, y, to depend on unobservables—usually called unobserved heterogeneity—we must be careful in specifying the partial effects of interest. Suppose that we have in mind the (structural) conditional mean Eðy j x; qÞ ¼ m1ðx; qÞ, where x is a vector of observable explanatory variables and q is an unobserved random variable—the unobserved heterogeneity. (We take q to be a scalar for simplicity; the discussion for a vector is essentially the same.) For continuous xj, the partial effect of immediate interest is

$$\theta_j(\mathbf{x}, q) \equiv \partial \mathbf{E}(y \mid \mathbf{x}, q) / \partial x_j = \partial \mu_1(\mathbf{x}, q) / \partial x_j$$
(2.30)

(For discrete xj, we would simply look at differences in the regression function for xj at two different values, when the other elements of x and q are held fixed.) Because yjðx; qÞ generally depends on q, we cannot hope to estimate the partial effects across many different values of q. In fact, even if we could estimate yjðx; qÞ for all x and q, we would generally have little guidance about inserting values of q into the mean function. In many cases we can make a normalization such as EðqÞ ¼ 0, and estimate yjðx; 0Þ, but q ¼ 0 typically corresponds to a very small segment of the population. (Technically, q ¼ 0 corresponds to no one in the population when q is continuously distributed.) Usually of more interest is the partial effect averaged across the population distribution of q; this is called the average partial effect (APE ).

For emphasis, let x<sup>o</sup> denote a fixed value of the covariates. The average partial effect evaluated at x<sup>o</sup> is

$$\delta_j(\mathbf{x}^o) \equiv \mathrm{E}_q[\theta_j(\mathbf{x}^o, q)] \tag{2.31}$$

{40}------------------------------------------------

where Eq½ denotes the expectation with respect to q. In other words, we simply average the partial effect yjðx<sup>o</sup>; qÞ across the population distribution of q. Definition (2.31) holds for any population relationship between q and x; in particular, they need not be independent. But remember, in definition (2.31), x<sup>o</sup> is a nonrandom vector of numbers.

For concreteness, assume that q has a continuous distribution with density function gðÞ, so that

$$\delta_j(\mathbf{x}^o) = \int_{\mathbb{R}} \theta_j(\mathbf{x}^o, \varphi) g(\varphi) \, d\varphi \tag{2.32}$$

where q is simply the dummy argument in the integration. The question we answer here is, Is it possible to estimate djðxoÞ from conditional expectations that depend only on observable conditioning variables? Generally, the answer must be no, as q and x can be arbitrarily related. Nevertheless, if we appropriately restrict the relationship between q and x, we can obtain a very useful equivalance.

One common assumption in nonlinear models with unobserved heterogeneity is that q and x are independent. We will make the weaker assumption that q and x are independent conditional on a vector of observables, w:

$$D(q \mid \mathbf{x}, \mathbf{w}) = D(q \mid \mathbf{w}) \tag{2.33}$$

where Dð j Þ denotes conditional distribution. (If we take w to be empty, we get the special case of independence between q and x.) In many cases, we can interpret equation (2.33) as implying that w is a vector of good proxy variables for q, but equation (2.33) turns out to be fairly widely applicable. We also assume that w is redundant or ignorable in the structural expectation

$$E(y \mid \mathbf{x}, q, \mathbf{w}) = E(y \mid \mathbf{x}, q) \tag{2.34}$$

As we will see in subsequent chapters, many econometric methods hinge on being able to exclude certain variables from the equation of interest, and equation (2.34) makes this assumption precise. Of course, if w is empty, then equation (2.34) is trivially true.

Under equations (2.33) and (2.34), we can show the following important result, provided that we can interchange a certain integral and partial derivative:

$$\delta_j(\mathbf{x}^o) = \mathbf{E}_w[\partial \mathbf{E}(y \mid \mathbf{x}^o, \mathbf{w})/\partial x_j] \tag{2.35}$$

where Ew½ denotes the expectation with respect to the distribution of w. Before we verify equation (2.35) for the special case of continuous, scalar q, we must understand its usefulness. The point is that the unobserved heterogeneity, q, has disappeared entirely, and the conditional expectation Eðy j x; wÞ can be estimated quite generally


{41}------------------------------------------------

because we assume that a random sample can be obtained on ðy; x; wÞ. [Alternatively, when we write down parametric econometric models, we will be able to derive Eðy j x; wÞ.] Then, estimating the average partial effect at any chosen x<sup>o</sup> amounts to averaging qm^2ðx<sup>o</sup>; wiÞ=qxj across the random sample, where m2ðx; wÞ 1Eðy j x; wÞ.

Proving equation (2.35) is fairly simple. First, we have

$$\mu_2(\mathbf{x}, \mathbf{w}) = \mathrm{E}[\mathrm{E}(y \mid \mathbf{x}, q, \mathbf{w}) \mid \mathbf{x}, \mathbf{w}] = \mathrm{E}[\mu_1(\mathbf{x}, q) \mid \mathbf{x}, \mathbf{w}] = \int_{\mathbb{R}} \mu_1(\mathbf{x}, q) g(\mathbf{y} \mid \mathbf{w}) d\mathbf{y}$$

where the first equality follows from the law of iterated expectations, the second equality follows from equation (2.34), and the third equality follows from equation (2.33). If we now take the partial derivative with respect to xj of the equality

$$\mu_2(\mathbf{x}, \mathbf{w}) = \int_{\mathbb{R}} \mu_1(\mathbf{x}, q) g(\mathbf{y} \mid \mathbf{w}) d\mathbf{y}$$
 (2.36)

and interchange the partial derivative and the integral, we have, for any ðx; wÞ,

$$\partial \mu_2(\mathbf{x}, \mathbf{w}) / \partial x_j = \int_{\mathbb{R}} \theta_j(\mathbf{x}, \varphi) g(\varphi \mid \mathbf{w}) \, d\varphi \tag{2.37}$$

For fixed xo, the right-hand side of equation (2.37) is simply E½yjðx<sup>o</sup>; qÞ j w-, and so another application of iterated expectations gives, for any xo,

$$\mathbf{E}_{w}[\partial \mu_{2}(\mathbf{x}^{o}, \mathbf{w})/\partial x_{j}] = \mathbf{E}\{\mathbf{E}[\theta_{j}(\mathbf{x}^{o}, q) \mid \mathbf{w}]\} = \delta_{j}(\mathbf{x}^{o})$$

which is what we wanted to show.

As mentioned previously, equation (2.35) has many applications in models where unobserved heterogeneity enters a conditional mean function in a nonadditive fashion. We will use this result (in simplified form) in Chapter 4, and also extensively in Part III. The special case where q is independent of x—and so we do not need the proxy variables w—is very simple: the APE of xj on Eðy j x; qÞ is simply the partial effect of xj on m2ðxÞ ¼ Eðy j xÞ. In other words, if we focus on average partial effects, there is no need to introduce heterogeneity. If we do specify a model with heterogeneity independent of x, then we simply find Eðy j xÞ by integrating Eðy j x; qÞ over the distribution of q.