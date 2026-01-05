# Unobserved Effects Logit Models under Strict Exogeneity

> Pages: 499-502

The unobserved effects probit models of the previous subsection have logit counterparts. If we replace the standard normal cdf  $\Phi$  in assumption (15.60) with the logistic function  $\Lambda$ , and also maintain assumptions (15.61) and (15.63), we arrive at what is usually called the **random effects logit model**. This model is not as attractive as the random effects probit model because there are no simple estimators available. The normal distribution, with its property that linear combinations of normals are normally distributed, facilitates the pooled probit, random effects, and minimum distance estimation approaches. By contrast, in the random effects logit model,  $P(y_{it} = 1 \mid \mathbf{x}_i)$  has no simple form: integrating the logit response  $\Lambda(\mathbf{x}_t \boldsymbol{\beta} + c)$  with respect to the normal density  $(1/\sigma_c)\phi(c/\sigma_c)$  yields no simple functional form. This statement is also true of other popular continuous distributions for c.

There is one important advantage of the unobserved effects logit model over the probit model: under assumptions (15.60) (with  $\Phi$  replaced by  $\Lambda$ ) and (15.61), it is possible to obtain a  $\sqrt{N}$ -consistent estimator of  $\beta$  without *any* assumptions about how  $c_i$  is related to  $\mathbf{x}_i$ .

{500}------------------------------------------------

How can we allow  $c_i$  and  $\mathbf{x}_i$  to be arbitrarily related in the unobserved effects logit model? In the linear case we used the FE or FD transformation to eliminate  $c_i$  from the estimating equation. It turns out that a similar strategy works in the logit case, although the argument is more subtle. What we do is find the joint distribution of  $\mathbf{y}_i \equiv (y_{i1}, \ldots, y_{iT})'$  conditional on  $\mathbf{x}_i, c_i$ , and  $n_i \equiv \sum_{t=1}^T y_{it}$ . It turns out that this conditional distribution does not depend on  $c_i$ , so that it is also the distribution of  $\mathbf{y}_i$  given  $\mathbf{x}_i$  and  $n_i$ . Therefore, we can use standard conditional maximum likelihood methods to estimate  $\boldsymbol{\beta}$ . (The fact that we can find a conditional distribution that does not depend on the  $c_i$  is a feature of the logit functional form. Unfortunately, the same argument does not work for the unobserved effects probit model.)

First consider the T=2 case, where  $n_i$  takes a value in  $\{0,1,2\}$ . Intuitively, the conditional distribution of  $(y_{i1}, y_{i2})'$  given  $n_i$  cannot be informative for  $\beta$  when  $n_i = 0$  or  $n_i = 2$  because these values completely determine the outcome on  $\mathbf{y}_i$ . However, for  $n_i = 1$ ,

$$P(y_{i2} = 1 | \mathbf{x}_{i}, c_{i}, n_{i} = 1) = P(y_{i2} = 1, n_{i} = 1 | \mathbf{x}_{i}, c_{i}) / P(n_{i} = 1 | \mathbf{x}_{i}, c_{i})$$

$$= P(y_{i2} = 1 | \mathbf{x}_{i}, c_{i}) P(y_{i1} = 0 | \mathbf{x}_{i}, c_{i}) / \{ P(y_{i1} = 0, y_{i2} = 1 | \mathbf{x}_{i}, c_{i}) + P(y_{i1} = 1, y_{i2} = 0 | \mathbf{x}_{i}, c_{i}) \}$$

$$= \Lambda(\mathbf{x}_{i2}\boldsymbol{\beta} + c_{i}) [1 - \Lambda(\mathbf{x}_{i1}\boldsymbol{\beta} + c_{i})] / \{ [1 - \Lambda(\mathbf{x}_{i1}\boldsymbol{\beta} + c_{i})] \Lambda(\mathbf{x}_{i2}\boldsymbol{\beta} + c_{i}) + \Lambda(\mathbf{x}_{i1}\boldsymbol{\beta} + c_{i}) [1 - \Lambda(\mathbf{x}_{i2}\boldsymbol{\beta} + c_{i})] \} = \Lambda[(\mathbf{x}_{i2} - \mathbf{x}_{i1})\boldsymbol{\beta}]$$

Similarly,  $P(y_{i1} = 1 | \mathbf{x}_i, c_i, n_i = 1) = \Lambda[-(\mathbf{x}_{i2} - \mathbf{x}_{i1})\boldsymbol{\beta}] = 1 - \Lambda[(\mathbf{x}_{i2} - \mathbf{x}_{i1})\boldsymbol{\beta}]$ . The conditional log likelihood for observation *i* is

$$\ell_i(\boldsymbol{\beta}) = 1[n_i = 1](w_i \log \Lambda[(\mathbf{x}_{i2} - \mathbf{x}_{i1})\boldsymbol{\beta}] + (1 - w_i) \log\{1 - \Lambda[(\mathbf{x}_{i2} - \mathbf{x}_{i1})\boldsymbol{\beta}]\}) \quad (15.71)$$

where  $w_i = 1$  if  $(y_{i1} = 0, y_{i2} = 1)$  and  $w_i = 0$  if  $(y_{i1} = 1, y_{i2} = 0)$ . The conditional MLE is obtained by maximizing the sum of the  $\ell_i(\boldsymbol{\beta})$  across i. The indicator function  $1[n_i = 1]$  selects out the observations for which  $n_i = 1$ ; as stated earlier, observations for which  $n_i = 0$  or  $n_i = 2$  do not contribute to the log likelihood. Interestingly, equation (15.71) is just a standard cross-sectional logit of  $w_i$  on  $(\mathbf{x}_{i2} - \mathbf{x}_{i1})$  using the observations for which  $n_i = 1$ . (This approach is analogous to differencing in the linear case with T = 2.)

The conditional MLE from equation (15.71) is usually called the **fixed effects logit estimator**. We must emphasize that the FE logit estimator does *not* arise by treating the  $c_i$  as parameters to be estimated along with  $\beta$ . (This fact is confusing, as the FE probit estimator *does* estimate the  $c_i$  along with  $\beta$ .) As shown recently by Abrevaya


{501}------------------------------------------------

(1997), the MLE of  $\beta$  that is obtained by maximizing the log likelihood over  $\beta$  and the  $c_i$  has probability limit  $2\beta$ . (This finding extends a simple example due to Andersen, 1970; see also Hsiao, 1986, Section 7.3.)

Sometimes the conditional MLE is described as "conditioning on the unobserved effects in the sample." This description is misleading. What we have done is found a conditional density—which describes the subpopulation with  $n_i = 1$ —that depends only on observable data and the parameter  $\beta$ .

For general T the log likelihood is more complicated, but it is tractable. First,

$$P(y_{i1} = y_1, ..., y_{iT} = y_T | \mathbf{x}_i, c_i, n_i = n)$$

$$= P(y_{i1} = y_1, ..., y_{iT} = y_T | \mathbf{x}_i, c_i) / P(n_i = n | \mathbf{x}_i, c_i)$$
(15.72)

and the numerator factors as  $P(y_{i1} = y_1 | \mathbf{x}_i, c_i) \cdots P(y_{iT} = y_T | \mathbf{x}_i, c_i)$  by the conditional independence assumption. The denominator is the complicated part, but it is easy to describe:  $P(n_i = n | \mathbf{x}_i, c_i)$  is the sum of the probabilities of all possible outcomes of  $\mathbf{y}_i$  such that  $n_i = n$ . Using the specific form of the logit function we can write

$$\ell_i(\boldsymbol{\beta}) = \log \left\{ \exp \left( \sum_{t=1}^T y_{it} \mathbf{x}_{it} \boldsymbol{\beta} \right) \left[ \sum_{\mathbf{a} \in R_i} \exp \left( \sum_{t=1}^T a_t \mathbf{x}_{it} \boldsymbol{\beta} \right) \right]^{-1} \right\}$$
(15.73)

where  $R_i$  is the subset of  $\mathbb{R}^T$  defined as  $\{\mathbf{a} \in \mathbb{R}^T : a_t \in \{0,1\} \text{ and } \sum_{t=1}^T a_t = n_i\}$ . The log likelihood summed across i can be used to obtain a  $\sqrt{N}$ -asymptotically normal estimator of  $\boldsymbol{\beta}$ , and all inference follows from conditional MLE theory. Observations for which equation (15.72) is zero or unity—and which therefore do not depend on  $\boldsymbol{\beta}$ —drop out of  $\mathcal{L}(\boldsymbol{\beta})$ . See Chamberlain (1984).

The fixed effects logit estimator  $\beta$  immediately gives us the effect of each element of  $\mathbf{x}_t$  on the log-odds ratio,  $\log\{\Lambda(\mathbf{x}_t\boldsymbol{\beta}+c)/[1-\Lambda(\mathbf{x}_t\boldsymbol{\beta}+c)]\} = \mathbf{x}_t\boldsymbol{\beta}+c$ . Unfortunately, we cannot estimate the partial effects on the response probabilities unless we plug in a value for c. Because the distribution of  $c_i$  is unrestricted—in particular,  $E(c_i)$  is not necessarily zero—it is hard to know what to plug in for c. In addition, we cannot estimate average partial effects, as doing so would require finding  $E[\Lambda(\mathbf{x}_t\boldsymbol{\beta}+c_i)]$ , a task that apparently requires specifying a distribution for  $c_i$ .

The conditional logit approach also has the drawback of apparently requiring the conditional independence assumption (15.61) for consistency. As we saw in Section 15.8.2, if we are willing to make the normality assumption (15.67), the probit approach allows unrestricted serial dependence in  $y_{it}$  even after conditioning on  $\mathbf{x}_i$  and  $c_i$ . This possibility may be especially important when several time periods are available.

{502}------------------------------------------------