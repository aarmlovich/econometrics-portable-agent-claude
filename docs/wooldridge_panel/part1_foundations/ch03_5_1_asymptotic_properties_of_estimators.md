# Asymptotic Properties of Estimators

> Pages: 57-60

DEFINITION 3.8: Let  $\{\hat{\boldsymbol{\theta}}_N : N = 1, 2, ...\}$  be a sequence of estimators of the  $P \times 1$  vector  $\boldsymbol{\theta} \in \boldsymbol{\Theta}$ , where N indexes the sample size. If

$$\hat{\boldsymbol{\theta}}_N \stackrel{p}{\to} \boldsymbol{\theta}$$
 (3.2)

for any value of  $\theta$ , then we say  $\hat{\theta}_N$  is a **consistent estimator** of  $\theta$ .

Because there are other notions of convergence, in the theoretical literature condition (3.2) is often referred to as *weak consistency*. This is the only kind of consistency we will be concerned with, so we simply call condition (3.2) *consistency*. (See White, 1984, Chapter 2, for other kinds of convergence.) Since we do not know  $\theta$ , the consistency definition requires condition (3.2) for any possible value of  $\theta$ .

DEFINITION 3.9: Let  $\{\hat{\boldsymbol{\theta}}_N: N=1,2,\ldots\}$  be a sequence of estimators of the  $P\times 1$  vector  $\boldsymbol{\theta} \in \boldsymbol{\Theta}$ . Suppose that

$$\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) \stackrel{d}{\to} \text{Normal}(\mathbf{0}, \mathbf{V})$$
 (3.3)

where **V** is a  $P \times P$  positive semidefinite matrix. Then we say that  $\hat{\boldsymbol{\theta}}_N$  is  $\sqrt{\mathbf{N}}$ -asymptotically normally distributed and **V** is the asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})$ , denoted Avar  $\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) = \mathbf{V}$ .

Even though  $V/N = Var(\hat{\theta}_N)$  holds only in special cases, and  $\hat{\theta}_N$  rarely has an exact normal distribution, we treat  $\hat{\theta}_N$  as if

{58}------------------------------------------------

$$\hat{\boldsymbol{\theta}}_N \sim \text{Normal}(\boldsymbol{\theta}, \mathbf{V}/N)$$
 (3.4)

whenever statement (3.3) holds. For this reason, V/N is called the **asymptotic variance** of  $\hat{\theta}_N$ , and we write

$$Avar(\hat{\boldsymbol{\theta}}_N) = \mathbf{V}/N \tag{3.5}$$

However, the only sense in which  $\hat{\theta}_N$  is approximately normally distributed with mean  $\theta$  and variance V/N is contained in statement (3.3), and this is what is needed to perform inference about  $\theta$ . Statement (3.4) is a heuristic statement that leads to the appropriate inference.

When we discuss consistent estimation of asymptotic variances—a topic that will arise often—we should technically focus on estimation of  $\mathbf{V} \equiv \operatorname{Avar} \sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})$ . In most cases, we will be able to find at least one, and usually more than one, consistent estimator  $\hat{\mathbf{V}}_N$  of  $\mathbf{V}$ . Then the corresponding estimator of  $\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)$  is  $\hat{\mathbf{V}}_N/N$ , and we write

$$Avar(\hat{\boldsymbol{\theta}}_N) = \hat{\mathbf{V}}_N/N \tag{3.6}$$

The division by N in equation (3.6) is practically very important. What we call the asymptotic variance of  $\hat{\theta}_N$  is estimated as in equation (3.6). Unfortunately, there has not been a consistent usage of the term "asymptotic variance" in econometrics.

Taken literally, a statement such as " $\hat{\mathbf{V}}_N/N$  is consistent for  $\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)$ " is not very meaningful because  $\mathbf{V}/N$  converges to  $\mathbf{0}$  as  $N \to \infty$ ; typically,  $\hat{\mathbf{V}}_N/N \overset{p}{\to} \mathbf{0}$  whether or not  $\hat{\mathbf{V}}_N$  is not consistent for  $\mathbf{V}$ . Nevertheless, it is useful to have an admittedly imprecise shorthand. In what follows, if we say that " $\hat{\mathbf{V}}_N/N$  consistently estimates  $\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)$ ," we mean that  $\hat{\mathbf{V}}_N$  consistently estimates  $\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)$ .

DEFINITION 3.10: If  $\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) \stackrel{a}{\sim} \text{Normal}(0, \mathbf{V})$  where  $\mathbf{V}$  is positive definite with jth diagonal  $v_{jj}$ , and  $\hat{\mathbf{V}}_N \stackrel{p}{\rightarrow} \mathbf{V}$ , then the **asymptotic standard error** of  $\hat{\theta}_{Nj}$ , denoted  $\text{se}(\hat{\theta}_{Nj})$ , is  $(\hat{v}_{Njj}/N)^{1/2}$ .

In other words, the asymptotic standard error of an estimator, which is almost always reported in applied work, is the square root of the appropriate diagonal element of  $\hat{\mathbf{V}}_N/N$ . The asymptotic standard errors can be loosely thought of as estimating the standard deviations of the elements of  $\hat{\boldsymbol{\theta}}_N$ , and they are the appropriate quantities to use when forming (asymptotic) t statistics and confidence intervals. Obtaining valid asymptotic standard errors (after verifying that the estimator is asymptotically normally distributed) is often the biggest challenge when using a new estimator.

If statement (3.3) holds, it follows by Lemma 3.5 that  $\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) = O_p(1)$ , or  $\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta} = O_p(N^{-1/2})$ , and we say that  $\hat{\boldsymbol{\theta}}_N$  is a  $\sqrt{N}$ -consistent estimator of  $\boldsymbol{\theta}$ .  $\sqrt{N}$ -

{59}------------------------------------------------

consistency certainly implies that plim  $\hat{\boldsymbol{\theta}}_N = \boldsymbol{\theta}$ , but it is much stronger because it tells us that the rate of convergence is almost the square root of the sample size N:  $\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta} = o_p(N^{-c})$  for any  $0 \le c < \frac{1}{2}$ . In this book, almost every consistent estimator we will study—and every one we consider in any detail—is  $\sqrt{N}$ -asymptotically normal, and therefore  $\sqrt{N}$ -consistent, under reasonable assumptions.

If one  $\sqrt{N}$ -asymptotically normal estimator has an asymptotic variance that is smaller than another's asymptotic variance (in the matrix sense), it makes it easy to choose between the estimators based on asymptotic considerations.

DEFINITION 3.11: Let  $\hat{\boldsymbol{\theta}}_N$  and  $\tilde{\boldsymbol{\theta}}_N$  be estimators of  $\boldsymbol{\theta}$  each satisfying statement (3.3), with asymptotic variances  $\mathbf{V} = \operatorname{Avar} \sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})$  and  $\mathbf{D} = \operatorname{Avar} \sqrt{N}(\tilde{\boldsymbol{\theta}}_N - \boldsymbol{\theta})$  (these generally depend on the value of  $\boldsymbol{\theta}$ , but we suppress that consideration here). (1)  $\hat{\boldsymbol{\theta}}_N$  is asymptotically efficient relative to  $\tilde{\boldsymbol{\theta}}_N$  if  $\mathbf{D} - \mathbf{V}$  is positive semidefinite for all  $\boldsymbol{\theta}$ ; (2)  $\hat{\boldsymbol{\theta}}_N$  and  $\tilde{\boldsymbol{\theta}}_N$  are  $\sqrt{N}$ -equivalent if  $\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \tilde{\boldsymbol{\theta}}_N) = o_p(1)$ .

When two estimators are  $\sqrt{N}$ -equivalent, they have the same limiting distribution (multivariate normal in this case, with the same asymptotic variance). This conclusion follows immediately from the asymptotic equivalence lemma (Lemma 3.7). Sometimes, to find the limiting distribution of, say,  $\sqrt{N}(\hat{\theta}_N - \theta)$ , it is easiest to first find the limiting distribution of  $\sqrt{N}(\tilde{\theta}_N - \theta)$ , and then to show that  $\hat{\theta}_N$  and  $\tilde{\theta}_N$  are  $\sqrt{N}$ -equivalent. A good example of this approach is in Chapter 7, where we find the limiting distribution of the feasible generalized least squares estimator, after we have found the limiting distribution of the GLS estimator.

DEFINITION 3.12: Partition  $\hat{\boldsymbol{\theta}}_N$  satisfying statement (3.3) into vectors  $\hat{\boldsymbol{\theta}}_{N1}$  and  $\hat{\boldsymbol{\theta}}_{N2}$ . Then  $\hat{\boldsymbol{\theta}}_{N1}$  and  $\hat{\boldsymbol{\theta}}_{N2}$  are **asymptotically independent** if

$$\mathbf{V} = \begin{pmatrix} \mathbf{V}_1 & \mathbf{0} \\ \mathbf{0} & \mathbf{V}_2 \end{pmatrix}$$

where  $V_1$  is the asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{\theta}}_{N1} - \boldsymbol{\theta}_1)$  and similarly for  $V_2$ . In other words, the asymptotic variance of  $\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})$  is block diagonal.

Throughout this section we have been careful to index estimators by the sample size, N. This is useful to fix ideas on the nature of asymptotic analysis, but it is cumbersome when applying asymptotics to particular estimation methods. After this chapter, an estimator of  $\theta$  will be denoted  $\hat{\theta}$ , which is understood to depend on the sample size N. When we write, for example,  $\hat{\theta} \stackrel{p}{\rightarrow} \theta$ , we mean convergence in probability as the sample size N goes to infinity.

{60}------------------------------------------------