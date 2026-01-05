# Appendix 6A

> Pages: 153-156

We derive the asymptotic distribution of the 2SLS estimator in an equation with generated regressors and generated instruments. The tools needed to make the proof rigorous are introduced in Chapter 12, but the key components of the proof can be given here in the context of the linear model. Write the model as

$$v = \mathbf{x}\boldsymbol{\beta} + u, \qquad \mathbf{E}(u \,|\, \mathbf{v}) = 0$$

where  $\mathbf{x} = \mathbf{f}(\mathbf{w}, \boldsymbol{\delta})$ ,  $\boldsymbol{\delta}$  is a  $Q \times 1$  vector, and  $\boldsymbol{\beta}$  is  $K \times 1$ . Let  $\hat{\boldsymbol{\delta}}$  be a  $\sqrt{N}$ -consistent estimator of  $\boldsymbol{\delta}$ . The instruments for each i are  $\hat{\mathbf{z}}_i = \mathbf{g}(\mathbf{v}_i, \hat{\boldsymbol{\lambda}})$  where  $\mathbf{g}(\mathbf{v}, \boldsymbol{\lambda})$  is a  $1 \times L$  vector,  $\boldsymbol{\lambda}$  is an  $S \times 1$  vector of parameters, and  $\hat{\boldsymbol{\lambda}}$  is  $\sqrt{N}$ -consistent for  $\boldsymbol{\lambda}$ . Let  $\hat{\boldsymbol{\beta}}$  be the 2SLS estimator from the equation

$$y_i = \hat{\mathbf{x}}_i \boldsymbol{\beta} + error_i$$

where  $\hat{\mathbf{x}}_i = \mathbf{f}(\mathbf{w}_i, \hat{\boldsymbol{\delta}})$ , using instruments  $\hat{\mathbf{z}}_i$ :

$$\hat{\boldsymbol{\beta}} = \left[ \left( \sum_{i=1}^{N} \hat{\mathbf{x}}_{i}' \hat{\mathbf{z}}_{i} \right) \left( \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}' \hat{\mathbf{z}}_{i} \right)^{-1} \left( \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}' \hat{\mathbf{x}}_{i} \right) \right]^{-1} \left( \sum_{i=1}^{N} \hat{\mathbf{x}}_{i}' \hat{\mathbf{z}}_{i} \right) \left( \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}' \hat{\mathbf{z}}_{i} \right)^{-1} \left( \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}' y_{i} \right)$$

Write  $y_i = \hat{\mathbf{x}}_i \boldsymbol{\beta} + (\mathbf{x}_i - \hat{\mathbf{x}}_i) \boldsymbol{\beta} + u_i$ , where  $\mathbf{x}_i = \mathbf{f}(\mathbf{w}_i, \boldsymbol{\delta})$ . Plugging this in and multiplying through by  $\sqrt{N}$  gives

{154}------------------------------------------------

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = (\hat{\mathbf{C}}'\hat{\mathbf{D}}^{-1}\hat{\mathbf{C}})^{-1}\hat{\mathbf{C}}'\hat{\mathbf{D}}^{-1} \left\{ N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}'[(\mathbf{x}_{i} - \hat{\mathbf{x}}_{i})\boldsymbol{\beta} + u_{i}] \right\}$$

where

$$\hat{\mathbf{C}} \equiv N^{-1} \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}' \hat{\mathbf{x}}_{i}$$
 and  $\hat{\mathbf{D}} = N^{-1} \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}' \hat{\mathbf{z}}_{i}$ 

Now, using Lemma 12.1 in Chapter 12,  $\hat{\mathbf{C}} \xrightarrow{p} \mathrm{E}(\mathbf{z}'\mathbf{x})$  and  $\hat{\mathbf{D}} \xrightarrow{p} \mathrm{E}(\mathbf{z}'\mathbf{z})$ . Further, a mean value expansion of the kind used in Theorem 12.3 gives

$$N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{z}}_i' u_i = N^{-1/2} \sum_{i=1}^{N} \mathbf{z}_i' u_i + \left[ N^{-1} \sum_{i=1}^{N} \nabla_{\lambda} \mathbf{g}(\mathbf{v}_i, \lambda) u_i \right] \sqrt{N} (\hat{\lambda} - \lambda) + o_p(1)$$

where  $\nabla_{\lambda} \mathbf{g}(\mathbf{v}_i, \lambda)$  is the  $L \times S$  Jacobian of  $\mathbf{g}(\mathbf{v}_i, \lambda)'$ . Because  $\mathrm{E}(u_i | \mathbf{v}_i) = 0$ ,  $\mathrm{E}[\nabla_{\lambda} \mathbf{g}(\mathbf{v}_i, \lambda)'u_i] = \mathbf{0}$ . It follows that  $N^{-1} \sum_{i=1}^N \nabla_{\lambda} \mathbf{g}(\mathbf{v}_i, \lambda)u_i = \mathrm{o}_p(1)$  and, since  $\sqrt{N}(\hat{\lambda} - \lambda) = \mathrm{O}_p(1)$ , it follows that

$$N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}' u_{i} = N^{-1/2} \sum_{i=1}^{N} \mathbf{z}_{i}' u_{i} + o_{p}(1)$$

Next, using similar reasoning,

$$N^{-1/2} \sum_{i=1}^{N} \hat{\mathbf{z}}_{i}'(\mathbf{x}_{i} - \hat{\mathbf{x}}_{i})\boldsymbol{\beta} = -\left[N^{-1} \sum_{i=1}^{N} (\boldsymbol{\beta} \otimes \mathbf{z}_{i})' \nabla_{\delta} \mathbf{f}(\mathbf{w}_{i}, \boldsymbol{\delta})\right] \sqrt{N} (\hat{\boldsymbol{\delta}} - \boldsymbol{\delta}) + o_{p}(1)$$
$$= -\mathbf{G} \sqrt{N} (\hat{\boldsymbol{\delta}} - \boldsymbol{\delta}) + o_{p}(1)$$

where  $\mathbf{G} = \mathrm{E}[(\boldsymbol{\beta} \otimes \mathbf{z}_i)' \nabla_{\delta} \mathbf{f}(\mathbf{w}_i, \boldsymbol{\delta})]$  and  $\nabla_{\delta} \mathbf{f}(\mathbf{w}_i, \boldsymbol{\delta})$  is the  $K \times Q$  Jacobian of  $\mathbf{f}(\mathbf{w}_i, \boldsymbol{\delta})'$ . We have used a mean value expansion and  $\hat{\mathbf{z}}_i'(\mathbf{x}_i - \hat{\mathbf{x}}_i)\boldsymbol{\beta} = (\boldsymbol{\beta} \otimes \hat{\mathbf{z}}_i)'(\mathbf{x}_i - \hat{\mathbf{x}}_i)'$ . Now, assume that

$$\sqrt{N}(\hat{\boldsymbol{\delta}} - \boldsymbol{\delta}) = N^{-1/2} \sum_{i=1}^{N} \mathbf{r}_i(\boldsymbol{\delta}) + o_p(1)$$

where  $E[\mathbf{r}_i(\boldsymbol{\delta})] = \mathbf{0}$ . This assumption holds for all estimators discussed so far, and it also holds for most estimators in nonlinear models; see Chapter 12. Collecting all terms gives

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) = (\mathbf{C}'\mathbf{D}^{-1}\mathbf{C})^{-1}\mathbf{C}'\mathbf{D}^{-1}\left\{N^{-1/2}\sum_{i=1}^{N}\left[\mathbf{z}_{i}'u_{i} - \mathbf{Gr}_{i}(\boldsymbol{\delta})\right]\right\} + o_{p}(1)$$

{155}------------------------------------------------

By the central limit theorem,

$$\sqrt{N}(\hat{\boldsymbol{\beta}} - \boldsymbol{\beta}) \stackrel{a}{\sim} \text{Normal}[\mathbf{0}, (\mathbf{C}'\mathbf{D}^{-1}\mathbf{C})^{-1}\mathbf{C}'\mathbf{D}^{-1}\mathbf{M}\mathbf{D}^{-1}\mathbf{C}(\mathbf{C}'\mathbf{D}^{-1}\mathbf{C})^{-1}]$$

where

$$\mathbf{M} = \operatorname{Var}[\mathbf{z}_i' u_i - \mathbf{Gr}_i(\boldsymbol{\delta})]$$

The asymptotic variance of  $\hat{\beta}$  is estimated as

$$(\hat{\mathbf{C}}'\hat{\mathbf{D}}^{-1}\hat{\mathbf{C}})^{-1}\hat{\mathbf{C}}'\hat{\mathbf{D}}^{-1}\hat{\mathbf{M}}\hat{\mathbf{D}}^{-1}\hat{\mathbf{C}}(\hat{\mathbf{C}}'\hat{\mathbf{D}}^{-1}\hat{\mathbf{C}})^{-1}/N,$$
(6.36)

where

$$\hat{\mathbf{M}} = N^{-1} \sum_{i=1}^{N} (\hat{\mathbf{z}}_i' \hat{\mathbf{u}}_i - \hat{\mathbf{G}} \hat{\mathbf{r}}_i) (\hat{\mathbf{z}}_i' \hat{\mathbf{u}}_i - \hat{\mathbf{G}} \hat{\mathbf{r}}_i)'$$

$$(6.37)$$

$$\hat{\mathbf{G}} = N^{-1} \sum_{i=1}^{N} (\hat{\boldsymbol{\beta}} \otimes \hat{\mathbf{z}}_{i})' \nabla_{\delta} \mathbf{f}(\mathbf{w}_{i}, \hat{\boldsymbol{\delta}})$$
(6.38)

and

$$\hat{\mathbf{r}}_i = \mathbf{r}_i(\hat{\boldsymbol{\delta}}), \qquad \hat{\mathbf{u}}_i = y_i - \hat{\mathbf{x}}_i \hat{\boldsymbol{\beta}} \tag{6.39}$$

A few comments are in order. First, estimation of  $\lambda$  does not affect the asymptotic distribution of  $\hat{\beta}$ . Therefore, if there are no generated regressors, the usual 2SLS inference procedures are valid [ $\mathbf{G} = \mathbf{0}$  in this case and so  $\mathbf{M} = \mathrm{E}(u_i^2 \mathbf{z}_i' \mathbf{z}_i)$ ]. If  $\mathbf{G} = \mathbf{0}$  and  $\mathrm{E}(u^2 \mathbf{z}' \mathbf{z}) = \sigma^2 \mathrm{E}(\mathbf{z}' \mathbf{z})$ , then the usual 2SLS standard errors and test statistics are valid. If Assumption 2SLS.3 fails, then the heteroskedasticity-robust statistics are valid.

If  $G \neq 0$ , then the asymptotic variance of  $\hat{\beta}$  depends on that of  $\hat{\delta}$  [through the presence of  $\mathbf{r}_i(\delta)$ ]. Neither the usual 2SLS variance matrix estimator nor the heteroskedasticity-robust form is valid in this case. The matrix  $\hat{\mathbf{M}}$  should be computed as in equation (6.37).

In some cases,  $\mathbf{G} = \mathbf{0}$  under the null hypothesis that we wish to test. The *j*th row of  $\mathbf{G}$  can be written as  $\mathrm{E}[z_{ij}\boldsymbol{\beta}'\nabla_{\delta}\mathbf{f}(\mathbf{w}_{i},\boldsymbol{\delta})]$ . Now, suppose that  $\hat{x}_{ih}$  is the only generated regressor, so that only the *h*th row of  $\nabla_{\delta}\mathbf{f}(\mathbf{w}_{i},\boldsymbol{\delta})$  is nonzero. But then if  $\beta_{h} = 0$ ,  $\boldsymbol{\beta}'\nabla_{\delta}\mathbf{f}(\mathbf{w}_{i},\boldsymbol{\delta}) = \mathbf{0}$ . It follows that  $\mathbf{G} = \mathbf{0}$  and  $\mathbf{M} = \mathrm{E}(u_{i}^{2}\mathbf{z}_{i}'\mathbf{z}_{i})$ , so that no adjustment for the preliminary estimation of  $\boldsymbol{\delta}$  is needed. This observation is very useful for a variety of specification tests, including the test for endogeneity in Section 6.2.1. We will also use it in sample selection contexts later on.

{156}------------------------------------------------