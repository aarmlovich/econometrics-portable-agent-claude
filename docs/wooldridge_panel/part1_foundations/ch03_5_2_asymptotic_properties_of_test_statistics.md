# Asymptotic Properties of Test Statistics

> Pages: 60-65

We begin with some important definitions in the large-sample analysis of test statistics.

DEFINITION 3.13: (1) The **asymptotic size** of a testing procedure is defined as the limiting probability of rejecting  $H_0$  when it is true. Mathematically, we can write this as  $\lim_{N\to\infty} P_N(\text{reject }H_0 \mid H_0)$ , where the N subscript indexes the sample size.

(2) A test is said to be **consistent** against the alternative  $H_1$  if the null hypothesis is rejected with probability approaching one when  $H_1$  is true:  $\lim_{N\to\infty} P_N$  (reject  $H_0 \mid H_1$ ) = 1.

In practice, the asymptotic size of a test is obtained by finding the limiting distribution of a test statistic—in our case, normal or chi-square, or simple modifications of these that can be used as *t* distributed or *F* distributed—and then choosing a critical value based on this distribution. Thus, testing using asymptotic methods is practically the same as testing using the classical linear model.

A test is consistent against alternative  $H_1$  if the probability of rejecting  $H_1$  tends to unity as the sample size grows without bound. Just as consistency of an estimator is a minimal requirement, so is consistency of a test statistic. Consistency rarely allows us to choose among tests: most tests are consistent against alternatives that they are supposed to have power against. For consistent tests with the same asymptotic size, we can use the notion of *local power analysis* to choose among tests. We will cover this briefly in Chapter 12 on nonlinear estimation, where we introduce the notion of *local alternatives*—that is, alternatives to  $H_0$  that converge to  $H_0$  at rate  $1/\sqrt{N}$ . Generally, test statistics will have desirable asymptotic properties when they are based on estimators with good asymptotic properties (such as efficiency).

We now derive the limiting distribution of a test statistic that is used very often in econometrics

LEMMA 3.8: Suppose that statement (3.3) holds, where **V** is positive definite. Then for any nonstochastic matrix  $Q \times P$  matrix  $\mathbf{R}$ ,  $Q \leq P$ , with rank( $\mathbf{R}$ ) = Q,

$$\sqrt{N}\mathbf{R}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) \stackrel{a}{\sim} \text{Normal}(\mathbf{0}, \mathbf{R}\mathbf{V}\mathbf{R}')$$

and

$$[\sqrt{N}\mathbf{R}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})]'[\mathbf{R}\mathbf{V}\mathbf{R}']^{-1}[\sqrt{N}\mathbf{R}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})] \stackrel{a}{\sim} \chi_Q^2$$

In addition, if plim  $\hat{\mathbf{V}}_N = \mathbf{V}$  then

$$[\sqrt{N}\mathbf{R}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})]'[\mathbf{R}\hat{\mathbf{V}}_N\mathbf{R}']^{-1}[\sqrt{N}\mathbf{R}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})]$$
  
=  $(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})'\mathbf{R}'[\mathbf{R}(\hat{\mathbf{V}}_N/N)\mathbf{R}']^{-1}\mathbf{R}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) \stackrel{a}{\sim} \chi_O^2$


{61}------------------------------------------------

For testing the null hypothesis  $H_0$ :  $\mathbf{R}\theta = \mathbf{r}$ , where  $\mathbf{r}$  is a  $Q \times 1$  nonrandom vector, define the **Wald statistic** for testing  $H_0$  against  $H_1$ :  $\mathbf{R}\theta \neq \mathbf{r}$  as

$$W_N \equiv (\mathbf{R}\hat{\boldsymbol{\theta}}_N - \mathbf{r})' [\mathbf{R}(\hat{\mathbf{V}}_N/N)\mathbf{R}']^{-1} (\mathbf{R}\hat{\boldsymbol{\theta}}_N - \mathbf{r})$$
(3.7)

Under  $H_0$ ,  $W_N \stackrel{a}{\sim} \chi_Q^2$ . If we abuse the asymptotics and treat  $\hat{\theta}_N$  as being distributed as Normal $(\theta, \hat{\mathbf{V}}_N/N)$ , we get equation (3.7) exactly.

LEMMA 3.9: Suppose that statement (3.3) holds, where **V** is positive definite. Let **c**:  $\Theta \to \mathbb{R}^Q$  be a continuously differentiable function on the parameter space  $\Theta \subset \mathbb{R}^P$ , where  $Q \leq P$ , and assume that  $\theta$  is in the interior of the parameter space. Define  $\mathbf{C}(\theta) \equiv \nabla_{\theta} \mathbf{c}(\theta)$  as the  $Q \times P$  Jacobian of **c**. Then

$$\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})] \stackrel{a}{\sim} \text{Normal}[\mathbf{0}, \mathbf{C}(\boldsymbol{\theta})\mathbf{V}\mathbf{C}(\boldsymbol{\theta})']$$
 (3.8)

and

$$\{\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})]\}'[\mathbf{C}(\boldsymbol{\theta})\mathbf{V}\mathbf{C}(\boldsymbol{\theta})']^{-1}\{\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})]\} \stackrel{a}{\sim} \chi_O^2$$

Define  $\hat{\mathbf{C}}_N \equiv \mathbf{C}(\hat{\boldsymbol{\theta}}_N)$ . Then plim  $\hat{\mathbf{C}}_N = \mathbf{C}(\boldsymbol{\theta})$ . If plim  $\hat{\mathbf{V}}_N = \mathbf{V}$ , then

$$\{\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})]\}'[\hat{\mathbf{C}}_N\hat{\mathbf{V}}_N\hat{\mathbf{C}}_N']^{-1}\{\sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})]\} \stackrel{a}{\sim} \chi_O^2$$
(3.9)

Equation (3.8) is very useful for obtaining asymptotic standard errors for nonlinear functions of  $\hat{\boldsymbol{\theta}}_N$ . The appropriate estimator of  $\operatorname{Avar}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N)]$  is  $\hat{\mathbf{C}}_N(\hat{\mathbf{V}}_N/N)\hat{\mathbf{C}}_N' = \hat{\mathbf{C}}_N[\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)]\hat{\mathbf{C}}_N'$ . Thus, once  $\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)$  and the estimated Jacobian of  $\mathbf{c}$  are obtained, we can easily obtain

$$\operatorname{Avar}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N)] = \hat{\mathbf{C}}_N[\operatorname{Avar}(\hat{\boldsymbol{\theta}}_N)]\hat{\mathbf{C}}_N'$$
(3.10)

The asymptotic standard errors are obtained as the square roots of the diagonal elements of equation (3.10). In the scalar case  $\hat{\gamma}_N = c(\hat{\boldsymbol{\theta}}_N)$ , the asymptotic standard error of  $\hat{\gamma}_N$  is  $[\nabla_{\theta}c(\hat{\boldsymbol{\theta}}_N)[\text{Avar}(\hat{\boldsymbol{\theta}}_N)]\nabla_{\theta}c(\hat{\boldsymbol{\theta}}_N)']^{1/2}$ .

Equation (3.9) is useful for testing nonlinear hypotheses of the form  $H_0$ :  $\mathbf{c}(\theta) = \mathbf{0}$  against  $H_1$ :  $\mathbf{c}(\theta) \neq \mathbf{0}$ . The Wald statistic is

$$W_N = \sqrt{N} \mathbf{c}(\hat{\boldsymbol{\theta}}_N)' [\hat{\mathbf{C}}_N \hat{\mathbf{V}}_N \hat{\mathbf{C}}_N']^{-1} \sqrt{N} \mathbf{c}(\hat{\boldsymbol{\theta}}_N) = \mathbf{c}(\hat{\boldsymbol{\theta}}_N)' [\hat{\mathbf{C}}_N (\hat{\mathbf{V}}_N/N) \hat{\mathbf{C}}_N']^{-1} \mathbf{c}(\hat{\boldsymbol{\theta}}_N)$$
(3.11)

Under  $H_0$ ,  $W_N \stackrel{a}{\sim} \chi_Q^2$ .

The method of establishing equation (3.8), given that statement (3.3) holds, is often called the **delta method**, and it is used very often in econometrics. It gets its name from its use of calculus. The argument is as follows. Because  $\theta$  is in the interior of  $\Theta$ , and because plim  $\hat{\theta}_N = \theta$ ,  $\hat{\theta}_N$  is in an open, convex subset of  $\Theta$  containing  $\theta$  with

{62}------------------------------------------------

probability approaching one, therefore w.p.a.1 we can use a mean value expansion  $\mathbf{c}(\hat{\boldsymbol{\theta}}_N) = \mathbf{c}(\boldsymbol{\theta}) + \ddot{\mathbf{C}}_N \cdot (\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta})$ , where  $\ddot{\mathbf{C}}_N$  denotes the matrix  $\mathbf{C}(\boldsymbol{\theta})$  with rows evaluated at mean values between  $\hat{\boldsymbol{\theta}}_N$  and  $\boldsymbol{\theta}$ . Because these mean values are trapped between  $\hat{\boldsymbol{\theta}}_N$  and  $\boldsymbol{\theta}$ , they converge in probability to  $\boldsymbol{\theta}$ . Therefore, by Slutsky's theorem,  $\ddot{\mathbf{C}}_N \stackrel{p}{\to} \mathbf{C}(\boldsymbol{\theta})$ , and we can write

$$\begin{split} \sqrt{N}[\mathbf{c}(\hat{\boldsymbol{\theta}}_N) - \mathbf{c}(\boldsymbol{\theta})] &= \ddot{\mathbf{C}}_N \cdot \sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) \\ &= \mathbf{C}(\boldsymbol{\theta})\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) + [\ddot{\mathbf{C}}_N - \mathbf{C}(\boldsymbol{\theta})]\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) \\ &= \mathbf{C}(\boldsymbol{\theta})\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) + o_p(1) \cdot O_p(1) = \mathbf{C}(\boldsymbol{\theta})\sqrt{N}(\hat{\boldsymbol{\theta}}_N - \boldsymbol{\theta}) + o_p(1) \end{split}$$

We can now apply the asymptotic equivalence lemma and Lemma 3.8 [with  $\mathbf{R} \equiv \mathbf{C}(\boldsymbol{\theta})$ ] to get equation (3.8).

#### **Problems**

- **3.1.** Prove Lemma 3.1.
- 3.2. Using Lemma 3.2, prove Lemma 3.3.
- **3.3.** Explain why, under the assumptions of Lemma 3.4,  $\mathbf{g}(\mathbf{x}_N) = \mathbf{O}_p(1)$ .
- **3.4.** Prove Corollary 3.2.
- **3.5.** Let  $\{y_i: i=1,2,...\}$  be an independent, identically distributed sequence with  $E(y_i^2) < \infty$ . Let  $\mu = E(y_i)$  and  $\sigma^2 = Var(y_i)$ .
- a. Let  $\bar{y}_N$  denote the sample average based on a sample size of N. Find  $Var[\sqrt{N}(\bar{y}_N \mu)]$ .
- b. What is the asymptotic variance of  $\sqrt{N}(\bar{y}_N \mu)$ ?
- c. What is the asymptotic variance of  $\bar{y}_N$ ? Compare this with  $Var(\bar{y}_N)$ .
- d. What is the asymptotic standard deviation of  $\overline{y}_N$ ?
- e. How would you obtain the asymptotic standard error of  $\bar{y}_N$ ?
- **3.6.** Give a careful (albeit short) proof of the following statement: If  $\sqrt{N}(\hat{\boldsymbol{\theta}}_N \boldsymbol{\theta}) = O_p(1)$ , then  $\hat{\boldsymbol{\theta}}_N \boldsymbol{\theta} = O_p(N^{-c})$  for any  $0 \le c < \frac{1}{2}$ .
- **3.7.** Let  $\hat{\theta}$  be a  $\sqrt{N}$ -asymptotically normal estimator for the scalar  $\theta > 0$ . Let  $\hat{\gamma} = \log(\hat{\theta})$  be an estimator of  $\gamma = \log(\theta)$ .
- a. Why is  $\hat{\gamma}$  a consistent estimator of  $\gamma$ ?

{63}------------------------------------------------

b. Find the asymptotic variance of  $\sqrt{N}(\hat{\gamma} - \gamma)$  in terms of the asymptotic variance of  $\sqrt{N}(\hat{\theta} - \theta)$ .

- c. Suppose that, for a sample of data,  $\hat{\theta} = 4$  and  $se(\hat{\theta}) = 2$ . What is  $\hat{\gamma}$  and its (asymptotic) standard error?
- d. Consider the null hypothesis  $H_0$ :  $\theta = 1$ . What is the asymptotic t statistic for testing  $H_0$ , given the numbers from part c?
- e. Now state  $H_0$  from part d equivalently in terms of  $\gamma$ , and use  $\hat{\gamma}$  and  $se(\hat{\gamma})$  to test  $H_0$ . What do you conclude?
- **3.8.** Let  $\hat{\boldsymbol{\theta}} = (\hat{\theta}_1, \hat{\theta}_2)'$  be a  $\sqrt{N}$ -asymptotically normal estimator for  $\boldsymbol{\theta} = (\theta_1, \theta_2)'$ , with  $\theta_2 \neq 0$ . Let  $\hat{\gamma} = \hat{\theta}_1/\hat{\theta}_2$  be an estimator of  $\gamma = \theta_1/\theta_2$ .
- a. Show that plim  $\hat{\gamma} = \gamma$ .
- b. Find  $\operatorname{Avar}(\hat{\gamma})$  in terms of  $\boldsymbol{\theta}$  and  $\operatorname{Avar}(\hat{\boldsymbol{\theta}})$  using the delta method.
- c. If, for a sample of data,  $\hat{\boldsymbol{\theta}} = (-1.5, .5)'$  and  $\operatorname{Avar}(\hat{\boldsymbol{\theta}})$  is estimated as  $\begin{pmatrix} 1 & -.4 \\ -.4 & 2 \end{pmatrix}$ , find the asymptotic standard error of  $\hat{\gamma}$ .
- **3.9.** Let  $\hat{\boldsymbol{\theta}}$  and  $\tilde{\boldsymbol{\theta}}$  be two consistent,  $\sqrt{N}$ -asymptotically normal estimators of the  $P \times 1$  parameter vector  $\boldsymbol{\theta}$ , with Avar  $\sqrt{N}(\hat{\boldsymbol{\theta}} \boldsymbol{\theta}) = \mathbf{V}_1$  and Avar  $\sqrt{N}(\tilde{\boldsymbol{\theta}} \boldsymbol{\theta}) = \mathbf{V}_2$ . Define a  $Q \times 1$  parameter vector by  $\gamma = \mathbf{g}(\boldsymbol{\theta})$ , where  $\mathbf{g}(\cdot)$  is a continuously differentiable function. Show that, if  $\hat{\boldsymbol{\theta}}$  is asymptotically more efficient than  $\tilde{\boldsymbol{\theta}}$ , then  $\hat{\boldsymbol{\gamma}} \equiv \mathbf{g}(\hat{\boldsymbol{\theta}})$  is asymptotically efficient relative to  $\tilde{\boldsymbol{\gamma}} \equiv \mathbf{g}(\tilde{\boldsymbol{\theta}})$ .

{64}------------------------------------------------

# II LINEAR MODELS

In this part we begin our econometric analysis of linear models for cross section and panel data. In Chapter 4 we review the single-equation linear model and discuss ordinary least squares estimation. Although this material is, in principle, review, the approach is likely to be different from an introductory linear models course. In addition, we cover several topics that are not traditionally covered in texts but that have proven useful in empirical work. Chapter 5 discusses instrumental variables estimation of the linear model, and Chapter 6 covers some remaining topics to round out our treatment of the single-equation model.

Chapter 7 begins our analysis of systems of equations. The general setup is that the number of population equations is small relative to the (cross section) sample size. This allows us to cover seemingly unrelated regression models for cross section data as well as begin our analysis of panel data. Chapter 8 builds on the framework from Chapter 7 but considers the case where some explanatory variables may be uncorrelated with the error terms. Generalized method of moments estimation is the unifying theme. Chapter 9 applies the methods of Chapter 8 to the estimation of simultaneous equations models, with an emphasis on the conceptual issues that arise in applying such models.

Chapter 10 explicitly introduces unobserved-effects linear panel data models. Under the assumption that the explanatory variables are strictly exogenous conditional on the unobserved effect, we study several estimation methods, including fixed effects, first differencing, and random effects. The last method assumes, at a minimum, that the unobserved effect is uncorrelated with the explanatory variables in all time periods. Chapter 11 considers extensions of the basic panel data model, including failure of the strict exogeneity assumption.

{65}------------------------------------------------