# Specification Testing

> Pages: 661-664

Various specification tests have been proposed in the context of Poisson regression. The two most important kinds are conditional mean specification tests and condi

{662}------------------------------------------------

tional variance specification tests. For conditional mean tests, we usually begin with a fairly simple model whose parameters are easy to interpret—such as  $m(\mathbf{x}, \boldsymbol{\beta}) = \exp(\mathbf{x}\boldsymbol{\beta})$ —and then test this against other alternatives. Once the set of conditioning variables  $\mathbf{x}$  has been specified, all such tests are functional form tests.

A useful class of functional form tests can be obtained using the score principle, where the null model  $m(\mathbf{x}, \boldsymbol{\beta})$  is nested in a more general model. Fully robust tests and less robust tests are obtained exactly as in the previous section. Wooldridge (1997c, Section 3.5) contains details and some examples, including an extension of RESET to exponential regression models.

Conditional variance tests are more difficult to compute, especially if we want to maintain only that the first two moments are correctly specified under  $H_0$ . For example, it is very natural to test the GLM assumption (19.3) as a way of determining whether the Poisson QMLE is efficient in the class of estimators using only assumption (19.7). Cameron and Trivedi (1986) propose tests of the stronger assumption (19.2) and, in fact, take the null to be that the Poisson distribution is correct in its entirety. These tests are useful if we are interested in whether y given x truly has a Poisson distribution. However, assumption (19.2) is not necessary for consistency or relative efficiency of the Poisson QMLE.

Wooldridge (1991b) proposes fully robust tests of conditional variances in the context of the linear exponential family, which contains Poisson regression as a special case. To test assumption (19.3), write  $u_i = y_i - m(\mathbf{x}_i, \boldsymbol{\beta}_0)$  and note that, under assumptions (19.3) and (19.7),  $u_i^2 - \sigma_0^2 m(\mathbf{x}_i, \boldsymbol{\beta}_0)$  is uncorrelated with any function of  $\mathbf{x}_i$ . Let  $\mathbf{h}(\mathbf{x}_i, \boldsymbol{\beta})$  be a  $1 \times Q$  vector of functions of  $\mathbf{x}_i$  and  $\boldsymbol{\beta}$ , and consider the alternative model

$$E(u_i^2 \mid \mathbf{x}_i) = \sigma_o^2 m(\mathbf{x}_i, \boldsymbol{\beta}_o) + \mathbf{h}(\mathbf{x}_i, \boldsymbol{\beta}_o) \boldsymbol{\delta}_o$$
 (19.23)

For example, the elements of  $\mathbf{h}(\mathbf{x}_i, \boldsymbol{\beta})$  can be powers of  $m(\mathbf{x}_i, \boldsymbol{\beta})$ . Popular choices are unity and  $\{m(\mathbf{x}_i, \boldsymbol{\beta})\}^2$ . A test of  $H_0$ :  $\boldsymbol{\delta}_0 = \mathbf{0}$  is then a test of the GLM assumption. While there are several moment conditions that can be used, a fruitful one is to use the weighted residuals, as we did with the conditional mean tests. We base the test on

$$N^{-1} \sum_{i=1}^{N} (\hat{\mathbf{h}}_i / \hat{m}_i)' \{ (\hat{u}_i^2 - \hat{\sigma}^2 \hat{m}_i) / \hat{m}_i \} = N^{-1} \sum_{i=1}^{N} \tilde{\mathbf{h}}_i' (\tilde{u}_i^2 - \hat{\sigma}^2)$$
 (19.24)

where  $\tilde{\mathbf{h}}_i = \hat{\mathbf{h}}_i/\hat{m}_i$  and  $\tilde{u}_i = \hat{u}_i/\sqrt{\hat{m}_i}$ . (Note that  $\hat{\mathbf{h}}_i$  is weighted by  $1/\hat{m}_i$ , not  $1/\sqrt{\hat{m}_i}$ .) To turn this equation into a test statistic, we must confront the fact that its standardized limiting distribution depends on the limiting distributions of  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}_o)$  and  $\sqrt{N}(\hat{\sigma}^2 - \sigma_o^2)$ . To handle this problem, we use a trick suggested by Wooldridge

{663}------------------------------------------------

(1991b) that removes the dependence of the limiting distribution of the test statistic on that of  $\sqrt{N}(\hat{\sigma}^2 - \sigma_o^2)$ : replace  $\tilde{\mathbf{h}}_i$  in equation (19.24) with its demeaned counterpart,  $\tilde{\mathbf{r}}_i \equiv \tilde{\mathbf{h}}_i - \bar{\mathbf{h}}$ , where  $\bar{\mathbf{h}}$  is just the  $1 \times Q$  vector of sample averages of each element of  $\tilde{\mathbf{h}}_i$ . There is an additional purging that then leads to a simple regression-based statistic. Let  $\nabla_{\beta}\hat{m}_i$  be the unweighted gradient of the conditional mean function, evaluated at the Poisson QMLE  $\hat{\boldsymbol{\beta}}$ , and define  $\nabla_{\beta}\hat{m}_i \equiv \nabla_{\beta}\hat{m}_i/\sqrt{\hat{m}_i}$ , as before. The following steps come from Wooldridge (1991b, Procedure 4.1):

- 1. Obtain  $\hat{\sigma}^2$  as in equation (19.15) and  $\hat{\mathbf{A}}$  as in equation (19.16), and define the  $P \times Q$  matrix  $\hat{\mathbf{J}} = \hat{\sigma}^2 (N^{-1} \sum_{i=1}^N \nabla_{\!\beta} \hat{m}_i' \tilde{\mathbf{r}}_i / \hat{m}_i)$ .
- 2. For each i, define the  $1 \times Q$  vector

$$\hat{\mathbf{z}}_i \equiv (\tilde{\mathbf{u}}_i^2 - \hat{\boldsymbol{\sigma}}^2)\tilde{\mathbf{r}}_i - \hat{\mathbf{s}}_i'\hat{\mathbf{A}}^{-1}\hat{\mathbf{J}}$$
(19.25)

where  $\hat{\mathbf{s}}_i \equiv \nabla_{\beta} \tilde{m}_i' \tilde{u}_i$  is the Poisson score for observation *i*.

3. Run the regression

1 on 
$$\hat{\mathbf{z}}_i$$
,  $i = 1, 2, ..., N$  (19.26)

Under assumptions (19.3) and (19.7), N - SSR from this regression is distributed asymptotically as  $\chi_O^2$ .

The leading case occurs when  $\hat{m}_i = \exp(\mathbf{x}_i\hat{\boldsymbol{\beta}})$  and  $\nabla_{\boldsymbol{\beta}}\hat{m}_i = \exp(\mathbf{x}_i\hat{\boldsymbol{\beta}})\mathbf{x}_i = \hat{m}_i\mathbf{x}_i$ . The subtraction of  $\hat{\mathbf{s}}_i'\hat{\mathbf{A}}^{-1}\hat{\mathbf{J}}$  in equation (19.25) is a simple way of handling the fact that the limiting distribution of  $\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}_o)$  affects the limiting distribution of the unadjusted statistic in equation (19.24). This particular adjustment ensures that the tests are just as efficient as any maximum-likelihood-based statistic if  $\sigma_o^2 = 1$  and the Poisson assumption is correct. But this procedure is fully robust in the sense that only assumptions (19.3) and (19.7) are maintained under  $H_0$ . For further discussion the reader is referred to Wooldridge (1991b).

In practice, it is probably sufficient to choose the number of elements in Q to be small. Setting  $\hat{\mathbf{h}}_i = (1, \hat{m}_i^2)$ , so that  $\tilde{\mathbf{h}}_i = (1/\hat{m}_i, \hat{m}_i)$ , is likely to produce a fairly powerful two-degrees-of-freedom test against a fairly broad class of alternatives.

The procedure is easily modified to test the more restrictive assumption (19.2). First, replace  $\hat{\sigma}^2$  everywhere with unity. Second, there is no need to demean the auxiliary regressors  $\tilde{\mathbf{h}}_i$  (so that now  $\tilde{\mathbf{h}}_i$  can contain a constant); thus, wherever  $\tilde{\mathbf{r}}_i$  appears, simply use  $\tilde{\mathbf{h}}_i$ . Everything else is the same. For the reasons discussed earlier, when the focus is on  $\mathrm{E}(y \mid \mathbf{x})$ , we are more interested in testing assumption (19.3) than assumption (19.2).

{664}------------------------------------------------