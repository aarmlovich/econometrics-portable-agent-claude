# Specification Testing

> Pages: 409-412

Since MLE generally relies on its distributional assumptions, it is useful to have available a general class of specification tests that are simple to compute. One general approach is to nest the model of interest within a more general model (which may be much harder to estimate) and obtain the score test against the more general alternative. RESET in a linear model and its extension to exponential regression models in Section 12.6.2 are examples of this approach, albeit in a non-maximum-likelihood setting.

In the context of MLE, it makes sense to test moment conditions implied by the conditional density specification. Let  $\mathbf{w}_i = (\mathbf{x}_i, \mathbf{y}_i)$  and suppose that, when  $f(\cdot | \mathbf{x}; \boldsymbol{\theta})$  is correctly specified,

$$\mathbf{H}_0: \mathbf{E}[\mathbf{g}(\mathbf{w}_i, \boldsymbol{\theta}_0)] = \mathbf{0} \tag{13.37}$$

{410}------------------------------------------------

where  $\mathbf{g}(\mathbf{w}, \boldsymbol{\theta})$  is a  $Q \times 1$  vector. Any application implies innumerable choices for the function  $\mathbf{g}$ . Since the MLE  $\hat{\boldsymbol{\theta}}$  sets the sum of the score to zero,  $\mathbf{g}(\mathbf{w}, \boldsymbol{\theta})$  cannot contain elements of  $\mathbf{s}(\mathbf{w}, \boldsymbol{\theta})$ . Generally,  $\mathbf{g}$  should be chosen to test features of a model that are of primary interest, such as first and second conditional moments, or various conditional probabilities.

A test of hypothesis (13.37) is based on how far the sample average of  $\mathbf{g}(\mathbf{w}_i, \hat{\boldsymbol{\theta}})$  is from zero. To derive the asymptotic distribution, note that

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{g}_i(\hat{\boldsymbol{\theta}}) = N^{-1/2} \sum_{i=1}^{N} \left[ \mathbf{g}_i(\hat{\boldsymbol{\theta}}) - \mathbf{s}_i(\hat{\boldsymbol{\theta}}) \mathbf{\Pi}_{o} \right]$$

holds trivially because  $\sum_{i=1}^{N} \mathbf{s}_i(\hat{\boldsymbol{\theta}}) = \mathbf{0}$ , where

$$\mathbf{\Pi}_{o} \equiv \{ \mathrm{E}[\mathbf{s}_{i}(\boldsymbol{\theta}_{o})\mathbf{s}_{i}(\boldsymbol{\theta}_{o})'] \}^{-1} \{ \mathrm{E}[\mathbf{s}_{i}(\boldsymbol{\theta}_{o})\mathbf{g}_{i}(\boldsymbol{\theta}_{o})'] \}$$

is the  $P \times Q$  matrix of population regression coefficients from regressing  $\mathbf{g}_i(\boldsymbol{\theta}_0)'$  on  $\mathbf{s}_i(\boldsymbol{\theta}_0)'$ . Using a mean-value expansion about  $\boldsymbol{\theta}_0$  and algebra similar to that in Chapter 12, we can write

$$N^{-1/2} \sum_{i=1}^{N} \left[ \mathbf{g}_{i}(\hat{\boldsymbol{\theta}}) - \mathbf{s}_{i}(\hat{\boldsymbol{\theta}}) \mathbf{\Pi}_{o} \right] = N^{-1/2} \sum_{i=1}^{N} \left[ \mathbf{g}_{i}(\boldsymbol{\theta}_{o}) - \mathbf{s}_{i}(\boldsymbol{\theta}_{o}) \mathbf{\Pi}_{o} \right]$$

$$+ E[\nabla_{\boldsymbol{\theta}} \mathbf{g}_{i}(\boldsymbol{\theta}_{o}) - \nabla_{\boldsymbol{\theta}} \mathbf{s}_{i}(\boldsymbol{\theta}_{o}) \mathbf{\Pi}_{o} \right] \sqrt{N} (\hat{\boldsymbol{\theta}} - \boldsymbol{\theta}_{o}) + o_{p}(1)$$

$$(13.38)$$

The key is that, when the density is correctly specified, the second term on the right-hand side of equation (13.38) is identically zero. Here is the reason: First, equation (13.27) implies that  $[E\nabla_{\theta}\mathbf{s}_{i}(\theta_{o})]\{E[\mathbf{s}_{i}(\theta_{o})\mathbf{s}_{i}(\theta_{o})']\}^{-1} = -\mathbf{I}_{P}$ . Second, an extension of the conditional information matrix equality (Newey, 1985; Tauchen, 1985) implies that

$$-\mathbb{E}[\nabla_{\theta}\mathbf{g}_{i}(\boldsymbol{\theta}_{o}) \mid \mathbf{x}_{i}] = \mathbb{E}[\mathbf{g}_{i}(\boldsymbol{\theta}_{o})\mathbf{s}_{i}(\boldsymbol{\theta}_{o})' \mid \mathbf{x}_{i}]. \tag{13.39}$$

To show equation (13.39), write

$$E_{\theta}[\mathbf{g}_{i}(\boldsymbol{\theta}) \mid \mathbf{x}_{i}] = \int_{\mathcal{Y}} \mathbf{g}(\mathbf{y}, \mathbf{x}_{i}, \boldsymbol{\theta}) f(\mathbf{y} \mid \mathbf{x}_{i}; \boldsymbol{\theta}) v(d\mathbf{y}) = \mathbf{0}$$
(13.40)

for all  $\theta$ . Now, if we take the derivative with respect to  $\theta$  and assume that the integrals and derivative can be interchanged, equation (13.40) implies that

$$\int_{\mathcal{M}} \nabla_{\theta} \mathbf{g}(\mathbf{y}, \mathbf{x}_i, \boldsymbol{\theta}) f(\mathbf{y} \mid \mathbf{x}_i; \boldsymbol{\theta}) \nu(d\mathbf{y}) + \int_{\mathcal{M}} \mathbf{g}(\mathbf{y}, \mathbf{x}_i, \boldsymbol{\theta}) \nabla_{\theta} f(\mathbf{y} \mid \mathbf{x}_i; \boldsymbol{\theta}) \nu(d\mathbf{y}) = \mathbf{0}$$


{411}------------------------------------------------

or  $E_{\theta}[\nabla_{\theta}\mathbf{g}_{i}(\theta) \mid \mathbf{x}_{i}] + E_{\theta}[\mathbf{g}_{i}(\theta)\mathbf{s}_{i}(\theta)' \mid \mathbf{x}_{i}] = \mathbf{0}$ , where we use the fact that  $\nabla_{\theta}f(\mathbf{y} \mid \mathbf{x}; \theta) = \mathbf{s}(\mathbf{y}, \mathbf{x}, \theta)'f(\mathbf{y} \mid \mathbf{x}; \theta)$ . Plugging in  $\theta = \theta_{0}$  and rearranging gives equation (13.39). What we have shown is that

$$N^{-1/2} \sum_{i=1}^{N} [\mathbf{g}_{i}(\hat{\boldsymbol{\theta}}) - \mathbf{s}_{i}(\hat{\boldsymbol{\theta}}) \mathbf{\Pi}_{o}] = N^{-1/2} \sum_{i=1}^{N} [\mathbf{g}_{i}(\boldsymbol{\theta}_{o}) - \mathbf{s}_{i}(\boldsymbol{\theta}_{o}) \mathbf{\Pi}_{o}] + o_{p}(1)$$

which means these standardized partial sums have the same asymptotic distribution. Letting

$$\hat{\mathbf{\Pi}} \equiv \left(\sum_{i=1}^{N} \hat{\mathbf{s}}_{i} \hat{\mathbf{s}}_{i}'\right)^{-1} \left(\sum_{i=1}^{N} \hat{\mathbf{s}}_{i} \hat{\mathbf{g}}_{i}'\right)$$

it is easily seen that plim  $\hat{\mathbf{\Pi}} = \mathbf{\Pi}_0$  under standard regularity conditions. Therefore, the asymptotic variance of  $N^{-1/2} \sum_{i=1}^N [\mathbf{g}_i(\hat{\boldsymbol{\theta}}) - \mathbf{s}_i(\hat{\boldsymbol{\theta}}) \mathbf{\Pi}_0] = N^{-1/2} \sum_{i=1}^N \mathbf{g}_i(\hat{\boldsymbol{\theta}})$  is consistently estimated by  $N^{-1} \sum_{i=1}^N (\hat{\mathbf{g}}_i - \hat{\mathbf{s}}_i \hat{\mathbf{\Pi}}) (\hat{\mathbf{g}}_i - \hat{\mathbf{s}}_i \hat{\mathbf{\Pi}})'$ . When we construct the quadratic form, we get the **Newey-Tauchen-White (NTW) statistic**,

$$NTW = \left[\sum_{i=1}^{N} \mathbf{g}_{i}(\hat{\boldsymbol{\theta}})\right]' \left[\sum_{i=1}^{N} (\hat{\mathbf{g}}_{i} - \hat{\mathbf{s}}_{i}\hat{\boldsymbol{\Pi}})(\hat{\mathbf{g}}_{i} - \hat{\mathbf{s}}_{i}\hat{\boldsymbol{\Pi}})'\right]^{-1} \left[\sum_{i=1}^{N} \mathbf{g}_{i}(\hat{\boldsymbol{\theta}})\right]$$
(13.41)

This statistic was proposed independently by Newey (1985) and Tauchen (1985), and is an extension of White's (1982a) information matrix (IM) test statistic.

For computational purposes it is useful to note that equation (13.41) is identical to  $N - \mathrm{SSR}_0 = NR_0^2$  from the regression

1 on 
$$\hat{\mathbf{s}}'_i, \hat{\mathbf{g}}'_i, \qquad i = 1, 2, \dots, N$$
 (13.42)

where  $SSR_0$  is the usual sum of squared residuals. Under the null that the density is correctly specified, NTW is distributed asymptotically as  $\chi_Q^2$ , assuming that  $\mathbf{g}(\mathbf{w}, \boldsymbol{\theta})$  contains Q nonredundant moment conditions. Unfortunately, the outer product form of regression (13.42) means that the statistic can have poor finite sample properties. In particular applications—such as nonlinear least squares, binary response analysis, and Poisson regression, to name a few—it is best to use forms of test statistics based on the expected Hessian. We gave the regression-based test for NLS in equation (12.72), and we will see other examples in later chapters. For the information matrix test statistic, Davidson and MacKinnon (1992) have suggested an alternative form of the IM statistic that appears to have better finite sample properties.

Example 13.2 (continued): To test the specification of the conditional mean for Poission regression, we might take  $\mathbf{g}(\mathbf{w}, \boldsymbol{\theta}) = \exp(\mathbf{x}\boldsymbol{\theta})\mathbf{x}'[y - \exp(\mathbf{x}\boldsymbol{\theta})] = \exp(\mathbf{x}\boldsymbol{\theta})\mathbf{s}(\mathbf{w}, \boldsymbol{\theta})$ ,

{412}------------------------------------------------

where the score is given by equation (13.19). If Eðy j xÞ ¼ expðx*y*oÞ then E½gðw; *y*oÞ j x ¼ expðx*y*oÞE½sðw; *y*oÞ j x ¼ 0. To test the Poisson variance assumption, Varðy j xÞ ¼ Eðy j xÞ ¼ expðx*y*oÞ, g can be of the form gðw; *y*Þ ¼ aðx; *y*Þf½yexpðx*y*Þ<sup>2</sup> expðx*y*Þg, where aðx; *y*Þ is a Q 1 vector. If the Poisson assumption is true, then u ¼ y expðx*y*oÞ has a zero conditional mean and Eðu<sup>2</sup> j xÞ ¼ Varðy j xÞ ¼ expðx*y*oÞ. It follows that E½gðw; *y*oÞ j x ¼ 0.

Example 13.2 contains examples of what are known as conditional moment tests. As the name suggests, the idea is to form orthogonality conditions based on some key conditional moments, usually the conditional mean or conditional variance, but sometimes conditional probabilities or higher order moments. The tests for nonlinear regression in Chapter 12 can be viewed as conditional moment tests, and we will see several other examples in Part IV. For reasons discussed earlier, we will avoid computing the tests using regression (13.42) whenever possible. See Newey (1985), Tauchen (1985), and Pagan and Vella (1989) for general treatments and applications of conditional moment tests. White's (1982a) information matrix test can often be viewed as a conditional moment test; see Hall (1987) for the linear regression model and White (1994) for a general treatment.