# Cluster Samples

> Pages: 505-506

In Section 13.8 we noted how partial MLE methods can be applied to cluster samples, and binary choice models are no exception. For cluster i and unit g, we might specify  $P(y_{ig} = 1 | \mathbf{x}_{ig}) = \Phi(\mathbf{x}_{ig}\boldsymbol{\beta})$ , and then estimate  $\boldsymbol{\beta}$  using a pooled probit analysis. (Replacing  $\Phi$  with  $\Lambda$  gives pooled logit.) A robust variance matrix is needed to account for any within-cluster correlation due, say, to unobserved cluster effects. The formula is given in equation (13.53), except that g replaces f, and f, the size of cluster f, replaces f everywhere. This estimator is valid as f and f fixed.

We can also test for peer group effects by including among  $\mathbf{x}_{ig}$  the average (or other summary statistics) of variables within the same cluster. In this scenario there are almost certainly unobserved cluster effects, so statistics robust to intercluster correlation should be computed.

An alternative to pooled probit or logit is to use an unobserved effect framework explicitly. For example, we might have  $P(y_{ig} = 1 \mid \mathbf{x}_i, c_i) = \Phi(\mathbf{x}_{ig}\boldsymbol{\beta} + c_i)$ , where  $c_i$  is an unobserved cluster effect. If observations are assumed independent within cluster conditional on  $(\mathbf{x}_i, c_i)$ , and if  $c_i$  is independent of  $\mathbf{x}_i$ , then the random effects probit MLE is easily modified: just use equation (15.64) with t = g and  $T = G_i$ . The fact that the observations are no longer identically distributed across i has no practical implications. Allowing  $c_i$  and  $\mathbf{x}_i$  to be correlated in the context of cluster sampling is easy if we maintain assumption (15.67) regardless of the cluster size. The details are essentially the same as the panel data case.

When  $G_i = 2$  for all i, the fixed effects logit approach is straightforward. Geronimus and Korenman (1992) use sister pairs to determine the effects of teenage motherhood on subsequent economic outcomes. When the outcome is binary (such as an employ-

{506}------------------------------------------------

ment indicator), Geronimus and Korenman allow for an unobserved family effect by applying fixed effects logit.