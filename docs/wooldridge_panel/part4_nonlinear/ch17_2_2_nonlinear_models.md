# Nonlinear Models

> Pages: 564-566

Results similar to those in the previous section hold for nonlinear models as well. We will cover explicitly the case of nonlinear regression and maximum likelihood. See Problem 17.8 for the GMM case.

{565}------------------------------------------------

In the nonlinear regression case, if Eðy j x;sÞ ¼ Eðy j xÞ—so that selection is ignorable in the conditional mean sense—then NLS on the selected sample is consistent. Sufficient is that s is a deterministic function of x. The consistency argument is simple: NLS on the selected sample solves

$$\min_{\boldsymbol{\beta}} N^{-1} \sum_{i=1}^{N} s_i [y_i - m(\mathbf{x}_i, \boldsymbol{\beta})]^2$$

so it suffices to show that *b*<sup>o</sup> in Eðy j xÞ ¼ mðx; *b*oÞ minimizes Efs½y mðx; *b*Þ<sup>2</sup> g over *b*. By iterated expectations,

$$E\{s[y - m(\mathbf{x}, \boldsymbol{\beta})]^2\} = E(sE\{[y - m(\mathbf{x}, \boldsymbol{\beta})]^2 \mid \mathbf{x}, s\})$$

Next, write ½ymðx; *b*Þ<sup>2</sup> ¼ u<sup>2</sup> þ2½mðx; *b*oÞmðx; *b*Þuþ½mðx; *b*oÞmðx; *b*Þ<sup>2</sup> , where u ¼ y mðx; *b*oÞ. By assumption, Eðu j x;sÞ ¼ 0. Therefore,

$$E\{[y - m(\mathbf{x}, \boldsymbol{\beta})]^2 \mid \mathbf{x}, s\} = E(u^2 \mid \mathbf{x}, s) + [m(\mathbf{x}, \boldsymbol{\beta}_0) - m(\mathbf{x}, \boldsymbol{\beta})]^2$$

and the second term is clearly minimized at *b* ¼ *b*o. We do have to assume that *b*<sup>o</sup> is the unique value of *b* that makes Efs½mðx; *b*Þ mðx; *b*oÞ<sup>2</sup> g zero. This is the identification condition on the subpopulation.

It can also be shown that, if Varðy j x;sÞ ¼ Varðy j xÞ and Varðy j xÞ ¼ s<sup>2</sup> o, then the usual, nonrobust NLS statistics are valid. If heteroskedasticity exists either in the population or the subpopulation, standard heteroskedasticity-robust inference can be used. The arguments are very similar to those for 2SLS in the previous subsection.

Another important case is the general conditional maximum likelihood setup. Assume that the distribution of y given x and s is the same as the distribution of y given x: Dðy j x;sÞ ¼ Dðy j xÞ. This is a stronger form of ignorability of selection, but it always holds if s is a nonrandom function of x, or if s is independent of ðx; yÞ. In any case, Dðy j x;sÞ ¼ Dðy j xÞ ensures that the MLE on the selected sample is consistent and that the usual MLE statistics are valid. The analogy argument should be familiar by now. Conditional MLE on the selected sample solves

$$\max_{\theta} N^{-1} \sum_{i=1}^{N} s_i \ell(\mathbf{y}_i, \mathbf{x}_i; \boldsymbol{\theta})$$
 (17.13)

where lðyi; xi; *y*Þ is the log likelihood for observation i. Now for each x, *y*<sup>o</sup> maximizes E½lðy; x; *y*Þjx over *y*. But E½slðy; x; *y*Þ ¼ EfsE½lðy; x; *y*Þjx;sg ¼ EfsE½lðy; x; *y*Þjxg, since, by assumption, the conditional distribution of y given ðx;sÞ does not depend on s. Since E½lðy; x; *y*Þ j x is maximized at *y*o, so is EfsE½lðy; x; *y*Þ j xg. We must make

{566}------------------------------------------------

the stronger assumption that *y*<sup>o</sup> is the unique maximum, just as in the previous cases: if the selected subset of the population is too small, we may not be able to identify *y*o. Inference can be carried out using the usual MLE statistics obtained from the selected subsample because the information equality now holds conditional on x and s under the assumption that Dðy j x;sÞ ¼ Dðy j xÞ. We omit the details.

Problem 17.8 asks you to work through the case of GMM estimation of general nonlinear models based on conditional moment restrictions.