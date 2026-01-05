# Methods Assuming Ignorability of Treatment

> Pages: 614-615

We adopt the framework of the previous section, and, in addition, we let x denote a vector of observed covariates. Therefore, the population is described by ðy0; y1; w; xÞ, and we observe y, w, and x, where y is given by equation (18.3). When w and ðy0; y1Þ are allowed to be correlated, we need an assumption in order to identify treatment effects. Rosenbaum and Rubin (1983) introduced the following assumption, which they called ignorability of treatment (given observed covariates x):

assumption ATE.1: Conditional on x, w and ðy0; y1Þ are independent.

For many purposes, it suffices to assume ignorability in a conditional mean independence sense:

ASSUMPTION ATE.1': (a) 
$$E(y_0 \mid \mathbf{x}, w) = E(y_0 \mid \mathbf{x})$$
; and (b)  $E(y_1 \mid \mathbf{x}, w) = E(y_1 \mid \mathbf{x})$ .

Naturally, Assumption ATE.1 implies Assumption ATE.1<sup>0</sup> . In practice, Assumption ATE.1<sup>0</sup> might not afford much generality, although it does allow Varðy<sup>0</sup> j x; wÞ and Varðy<sup>1</sup> j x; wÞ to depend on w. The idea underlying Assumption ATE.1<sup>0</sup> is this: if we can observe enough information (contained in x) that determines treatment, then ðy0; y1Þ might be mean independent of w, conditional on x. Loosely, even though ðy0; y1Þ and w might be correlated, they are uncorrelated once we partial out x.

Assumption ATE.1 certainly holds if w is a deterministic function of x, which has prompted some authors in econometrics to call assumptions like ATE.1 selection on observables; see, for example, Barnow, Cain, and Goldberger (1980, 1981), Heckman and Robb (1985), and Moffitt (1996). (We discussed a similar assumption in Section

{615}------------------------------------------------

17.7.3 in the context of attrition in panel data.) The name is fine as a label, but we must realize that Assumption ATE.1 does allow w to depend on unobservables, albeit in a restricted fashion. If  $w = g(\mathbf{x}, a)$ , where a is an unobservable random variable independent of  $(\mathbf{x}, y_0, y_1)$ , then Assumption ATE.1 holds. But a cannot be arbitrarily correlated with  $y_0$  and  $y_1$ .

An important fact is that, under Assumption ATE.1', the average treatment effect conditional on  $\mathbf{x}$  and the average treatment effect of the treated, conditional on  $\mathbf{x}$ , are identical:

$$ATE_1(\mathbf{x}) \equiv E(y_1 - y_0 | \mathbf{x}, w = 1) = E(y_1 - y_0 | \mathbf{x}) = ATE(\mathbf{x})$$

because  $\mathrm{E}(y_g \mid \mathbf{x}, w) = \mathrm{E}(y_g \mid \mathbf{x}), g = 0, 1$ . However, the unconditional versions of the treatment effects are not generally equal. For clarity, define  $r(\mathbf{x}) = \mathrm{E}(y_1 - y_0 \mid \mathbf{x}) = ATE(\mathbf{x})$ . Then ATE is the expected value of  $r(\mathbf{x})$  across the entire population, whereas  $ATE_1$  is the expected value of  $r(\mathbf{x})$  in the treated subpopulation. Mathematically,

$$ATE = E[r(\mathbf{x})]$$
 and  $ATE_1 = E[r(\mathbf{x}) | w = 1]$ 

If we can estimate  $r(\cdot)$ , then ATE can be estimated by averaging across the entire random sample from the population, whereas  $ATE_1$  would be estimated by averaging across the part of the sample with  $w_i = 1$ . We will discuss specific estimation strategies in the next subsection.

An interesting feature of Assumptions ATE.1 and ATE.1′—and one that is perhaps foreign to economists—is that they are stated without imposing any kind of model on joint or conditional distributions. It turns out that no more structure is needed in order to identify either of the treatment effects. We first show how the ignorability assumption relates to standard regression analysis.