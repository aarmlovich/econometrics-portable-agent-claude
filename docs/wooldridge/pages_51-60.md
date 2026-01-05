

{51}------------------------------------------------

Define the 1 K vector of population residuals from the projection of x on z as r1x Lðx j zÞ. Further, define the population residual from the projection of y on z as v 1 y Lðy j zÞ. Then the following are true:

$$L(v \mid \mathbf{r}) = \mathbf{r}\boldsymbol{\beta} \tag{2.55}$$

and

$$L(y \mid \mathbf{r}) = \mathbf{r}\boldsymbol{\beta} \tag{2.56}$$

The point is that the *b* in equations (2.55) and (2.56) is the same as that appearing in equation (2.54). Another way of stating this result is

$$\boldsymbol{\beta} = [\mathbf{E}(\mathbf{r}'\mathbf{r})]^{-1}\mathbf{E}(\mathbf{r}'v) = [\mathbf{E}(\mathbf{r}'\mathbf{r})]^{-1}\mathbf{E}(\mathbf{r}'y). \tag{2.57}$$

Proof: From equation (2.54) write

$$y = \mathbf{x}\boldsymbol{\beta} + \mathbf{z}\gamma + u, \qquad \mathbf{E}(\mathbf{x}'u) = \mathbf{0}, \qquad \mathbf{E}(\mathbf{z}'u) = \mathbf{0}$$
 (2.58)

Taking the linear projection gives

$$L(y \mid \mathbf{z}) = L(\mathbf{x} \mid \mathbf{z})\boldsymbol{\beta} + \mathbf{z}\boldsymbol{\gamma} \tag{2.59}$$

Subtracting equation (2.59) from (2.58) gives y Lðy j zÞ¼½x Lðx j zÞ*b* þ u, or

$$v = \mathbf{r}\boldsymbol{\beta} + u \tag{2.60}$$

Since r is a linear combination of ðx; zÞ, Eðr<sup>0</sup> uÞ ¼ 0. Multiplying equation (2.60) through by r<sup>0</sup> and taking expectations, it follows that

$$\boldsymbol{\beta} = [\mathbf{E}(\mathbf{r}'\mathbf{r})]^{-1}\mathbf{E}(\mathbf{r}'v)$$

[We assume that Eðr<sup>0</sup> rÞ is nonsingular.] Finally, Eðr<sup>0</sup> vÞ ¼ E½r<sup>0</sup> ðy Lðy j zÞÞ- ¼ Eðr<sup>0</sup> yÞ, since Lðy j zÞ is linear in z and r is orthogonal to any linear function of z.

{52}------------------------------------------------

This chapter summarizes some definitions and limit theorems that are important for studying large-sample theory. Most claims are stated without proof, as several require tedious epsilon-delta arguments. We do prove some results that build on fundamental definitions and theorems. A good, general reference for background in asymptotic analysis is White (1984). In Chapter 12 we introduce further asymptotic methods that are required for studying nonlinear models.

## 3.1 Convergence of Deterministic Sequences

Asymptotic analysis is concerned with the various kinds of convergence of sequences of estimators as the sample size grows. We begin with some definitions regarding nonstochastic sequences of numbers. When we apply these results in econometrics, N is the sample size, and it runs through all positive integers. You are assumed to have some familiarity with the notion of a limit of a sequence.

DEFINITION 3.1: (1) A sequence of nonrandom numbers  $\{a_N: N=1,2,\ldots\}$  converges to a (has limit a) if for all  $\varepsilon>0$ , there exists  $N_\varepsilon$  such that if  $N>N_\varepsilon$  then  $|a_N-a|<\varepsilon$ . We write  $a_N\to a$  as  $N\to\infty$ .

(2) A sequence  $\{a_N: N=1,2,\ldots\}$  is *bounded* if and only if there is some  $b<\infty$  such that  $|a_N| \le b$  for all  $N=1,2,\ldots$  Otherwise, we say that  $\{a_N\}$  is *unbounded*.

These definitions apply to vectors and matrices element by element.

Example 3.1: (1) If  $a_N = 2 + 1/N$ , then  $a_N \to 2$ . (2) If  $a_N = (-1)^N$ , then  $a_N$  does not have a limit, but it is bounded. (3) If  $a_N = N^{1/4}$ ,  $a_N$  is not bounded. Because  $a_N$  increases without bound, we write  $a_N \to \infty$ .

DEFINITION 3.2: (1) A sequence  $\{a_N\}$  is  $O(N^{\lambda})$  (at most of order  $N^{\lambda}$ ) if  $N^{-\lambda}a_N$  is bounded. When  $\lambda = 0$ ,  $\{a_N\}$  is bounded, and we also write  $a_N = O(1)$  (big oh one). (2)  $\{a_N\}$  is  $O(N^{\lambda})$  if  $N^{-\lambda}a_N \to 0$ . When  $\lambda = 0$ ,  $a_N$  converges to zero, and we also write  $a_N = O(1)$  (little oh one).

From the definitions, it is clear that if  $a_N = o(N^{\lambda})$ , then  $a_N = O(N^{\lambda})$ ; in particular, if  $a_N = o(1)$ , then  $a_N = O(1)$ . If each element of a sequence of vectors or matrices is  $O(N^{\lambda})$ , we say the sequence of vectors or matrices is  $O(N^{\lambda})$ , and similarly for  $o(N^{\lambda})$ .

Example 3.2: (1) If  $a_N = \log(N)$ , then  $a_N = o(N^{\lambda})$  for any  $\lambda > 0$ . (2) If  $a_N = 10 + \sqrt{N}$ , then  $a_N = O(N^{1/2})$  and  $a_N = o(N^{(1/2+\gamma)})$  for any  $\gamma > 0$ .

{53}------------------------------------------------

### 3.2 Convergence in Probability and Bounded in Probability

DEFINITION 3.3: (1) A sequence of random variables  $\{x_N: N=1,2,\ldots\}$  converges in **probability** to the constant a if for all  $\varepsilon > 0$ ,

$$P[|x_N - a| > \varepsilon] \to 0$$
 as  $N \to \infty$ 

We write  $x_N \stackrel{p}{\to} a$  and say that a is the **probability limit (plim)** of  $x_N$ : plim  $x_N = a$ .

- (2) In the special case where a = 0, we also say that  $\{x_N\}$  is  $o_p(1)$  (*little oh p one*). We also write  $x_N = o_p(1)$  or  $x_N \stackrel{p}{\to} 0$ .
- (3) A sequence of random variables  $\{x_N\}$  is **bounded in probability** if and only if for every  $\varepsilon > 0$ , there exists a  $b_{\varepsilon} < \infty$  and an integer  $N_{\varepsilon}$  such that

$$P[|x_N| \ge b_{\varepsilon}] < \varepsilon$$
 for all  $N \ge N_{\varepsilon}$ 

We write  $x_N = O_p(1)$  ( $\{x_N\}$  is big oh p one).

If  $c_N$  is a nonrandom sequence, then  $c_N = O_p(1)$  if and only if  $c_N = O(1)$ ;  $c_N = o_p(1)$  if and only if  $c_N = o(1)$ . A simple, and very useful, fact is that if a sequence converges in probability to any real number, then it is bounded in probability.

LEMMA 3.1: If  $x_N \stackrel{p}{\to} a$ , then  $x_N = O_p(1)$ . This lemma also holds for vectors and matrices.

The proof of Lemma 3.1 is not difficult; see Problem 3.1.

- DEFINITION 3.4: (1) A random sequence  $\{x_N: N=1,2,\ldots\}$  is  $o_p(a_N)$ , where  $\{a_N\}$  is a nonrandom, positive sequence, if  $x_N/a_N=o_p(1)$ . We write  $x_N=o_p(a_N)$ .
- (2) A random sequence  $\{x_N: N=1,2,...\}$  is  $O_p(a_N)$ , where  $\{a_N\}$  is a non-random, positive sequence, if  $x_N/a_N=O_p(1)$ . We write  $x_N=O_p(a_N)$ .

We could have started by defining a sequence  $\{x_N\}$  to be  $o_p(N^{\delta})$  for  $\delta \in \mathbb{R}$  if  $N^{-\delta}x_N \stackrel{p}{\to} 0$ , in which case we obtain the definition of  $o_p(1)$  when  $\delta = 0$ . This is where the one in  $o_p(1)$  comes from. A similar remark holds for  $O_p(1)$ .

Example 3.3: If z is a random variable, then  $x_N \equiv \sqrt{N}z$  is  $O_p(N^{1/2})$  and  $x_N = o_p(N^{\delta})$  for any  $\delta > \frac{1}{2}$ .

LEMMA 3.2: If 
$$w_N = o_p(1)$$
,  $x_N = o_p(1)$ ,  $y_N = O_p(1)$ , and  $z_N = O_p(1)$ , then (1)  $w_N + x_N = o_p(1)$ ; (2)  $y_N + z_N = O_p(1)$ ; (3)  $y_N z_N = O_p(1)$ ; and (4)  $x_N z_N = o_p(1)$ .

In derivations, we will write relationships 1 to 4 as  $o_p(1) + o_p(1) = o_p(1)$ ,  $O_p(1) + O_p(1) = O_p(1)$ ,  $O_p(1) \cdot O_p(1) = O_p(1)$ , and  $o_p(1) \cdot O_p(1) = o_p(1)$ , respectively. Be-

{54}------------------------------------------------

cause a  $o_p(1)$  sequence is  $O_p(1)$ , Lemma 3.2 also implies that  $o_p(1) + O_p(1) = O_p(1)$  and  $o_p(1) \cdot o_p(1) = o_p(1)$ .

All of the previous definitions apply element by element to sequences of random vectors or matrices. For example, if  $\{\mathbf{x}_N\}$  is a sequence of random  $K \times 1$  random vectors,  $\mathbf{x}_N \stackrel{p}{\rightarrow} \mathbf{a}$ , where  $\mathbf{a}$  is a  $K \times 1$  nonrandom vector, if and only if  $x_{Nj} \stackrel{p}{\rightarrow} a_j$ ,  $j = 1, \ldots, K$ . This is equivalent to  $\|\mathbf{x}_N - \mathbf{a}\| \stackrel{p}{\rightarrow} 0$ , where  $\|\mathbf{b}\| \equiv (\mathbf{b}'\mathbf{b})^{1/2}$  denotes the Euclidean length of the  $K \times 1$  vector  $\mathbf{b}$ . Also,  $\mathbf{Z}_N \stackrel{p}{\rightarrow} \mathbf{B}$ , where  $\mathbf{Z}_N$  and  $\mathbf{B}$  are  $M \times K$ , is equivalent to  $\|\mathbf{Z}_N - \mathbf{B}\| \stackrel{p}{\rightarrow} 0$ , where  $\|\mathbf{A}\| \equiv [\operatorname{tr}(\mathbf{A}'\mathbf{A})]^{1/2}$  and  $\operatorname{tr}(\mathbf{C})$  denotes the trace of the square matrix  $\mathbf{C}$ .

A result that we often use for studying the large-sample properties of estimators for linear models is the following. It is easily proven by repeated application of Lemma 3.2 (see Problem 3.2).

LEMMA 3.3: Let  $\{\mathbf{Z}_N: N=1,2,\ldots\}$  be a sequence of  $J\times K$  matrices such that  $\mathbf{Z}_N=o_p(1)$ , and let  $\{\mathbf{x}_N\}$  be a sequence of  $J\times 1$  random vectors such that  $\mathbf{x}_N=O_p(1)$ . Then  $\mathbf{Z}'_N\mathbf{x}_N=o_p(1)$ .

The next lemma is known as Slutsky's theorem.

LEMMA 3.4: Let  $\mathbf{g} : \mathbb{R}^K \to \mathbb{R}^J$  be a function continuous at some point  $\mathbf{c} \in \mathbb{R}^K$ . Let  $\{\mathbf{x}_N : N = 1, 2, \ldots\}$  be sequence of  $K \times 1$  random vectors such that  $\mathbf{x}_N \xrightarrow{p} \mathbf{c}$ . Then  $\mathbf{g}(\mathbf{x}_N) \xrightarrow{p} \mathbf{g}(\mathbf{c})$  as  $N \to \infty$ . In other words,

$$plim \mathbf{g}(\mathbf{x}_N) = \mathbf{g}(plim \mathbf{x}_N) \tag{3.1}$$

if  $\mathbf{g}(\cdot)$  is continuous at plim  $\mathbf{x}_N$ .

Slutsky's theorem is perhaps the most useful feature of the plim operator: it shows that the plim passes through nonlinear functions, provided they are continuous. The expectations operator does not have this feature, and this lack makes finite sample analysis difficult for many estimators. Lemma 3.4 shows that plims behave just like regular limits when applying a continuous function to the sequence.

DEFINITION 3.5: Let  $(\Omega, \mathcal{F}, P)$  be a probability space. A sequence of events  $\{\Omega_N: N=1,2,\ldots\} \subset \mathcal{F}$  is said to occur with probability approaching one (w.p.a.1) if and only if  $P(\Omega_N) \to 1$  as  $N \to \infty$ .

Definition 3.5 allows that  $\Omega_N^c$ , the complement of  $\Omega_N$ , can occur for each N, but its chance of occuring goes to zero as  $N \to \infty$ .

COROLLARY 3.1: Let  $\{\mathbf{Z}_N: N=1,2,\ldots\}$  be a sequence of random  $K\times K$  matrices, and let  $\mathbf{A}$  be a nonrandom, invertible  $K\times K$  matrix. If  $\mathbf{Z}_N\stackrel{p}{\to} \mathbf{A}$  then

{55}------------------------------------------------

- (1)  $\mathbf{Z}_N^{-1}$  exists w.p.a.1; (2)  $\mathbf{Z}_N^{-1} \xrightarrow{p} \mathbf{A}^{-1}$  or plim  $\mathbf{Z}_N^{-1} = \mathbf{A}^{-1}$  (in an appropriate sense).

*Proof:* Because the determinant is a continuous function on the space of all square matrices,  $\det(\mathbf{Z}_N) \xrightarrow{p} \det(\mathbf{A})$ . Because A is nonsingular,  $\det(\mathbf{A}) \neq 0$ . Therefore, it follows that  $P[\det(\mathbf{Z}_N) \neq 0] \to 1$  as  $N \to \infty$ . This completes the proof of part 1.

Part 2 requires a convention about how to define  $\mathbb{Z}_N^{-1}$  when  $\mathbb{Z}_N$  is nonsingular. Let  $\Omega_N$  be the set of  $\omega$  (outcomes) such that  $\mathbf{Z}_N(\omega)$  is nonsingular for  $\omega \in \Omega_N$ ; we just showed that  $P(\Omega_N) \to 1$  as  $N \to \infty$ . Define a new sequence of matrices by

$$\tilde{\mathbf{Z}}_N(\omega) \equiv \mathbf{Z}_N(\omega)$$
 when  $\omega \in \Omega_N$ ,  $\tilde{\mathbf{Z}}_N(\omega) \equiv \mathbf{I}_K$  when  $\omega \notin \Omega_N$ 

Then  $P(\tilde{\mathbf{Z}}_N = \mathbf{Z}_N) = P(\Omega_N) \to 1$  as  $N \to \infty$ . Then, because  $\mathbf{Z}_N \stackrel{p}{\to} \mathbf{A}$ ,  $\tilde{\mathbf{Z}}_N \stackrel{p}{\to} \mathbf{A}$ . The inverse operator is continuous on the space of invertible matrices, so  $\tilde{\mathbf{Z}}_{N}^{-1} \stackrel{p}{\to} \mathbf{A}^{-1}$ . This is what we mean by  $\mathbb{Z}_N^{-1} \stackrel{p}{\to} \mathbb{A}^{-1}$ ; the fact that  $\mathbb{Z}_N$  can be singular with vanishing probability does not affect asymptotic analysis.

## Convergence in Distribution

DEFINITION 3.6: A sequence of random variables  $\{x_N: N=1,2,\ldots\}$  converges in **distribution** to the continuous random variable x if and only if

$$F_N(\xi) \to F(\xi)$$
 as  $N \to \infty$  for all  $\xi \in \mathbb{R}$ 

where  $F_N$  is the cumulative distribution function (c.d.f.) of  $x_N$  and F is the (continuous) c.d.f. of x. We write  $x_N \stackrel{d}{\rightarrow} x$ .

When  $x \sim \text{Normal}(\mu, \sigma^2)$  we write  $x_N \stackrel{d}{\to} \text{Normal}(\mu, \sigma^2)$  or  $x_N \stackrel{a}{\sim} \text{Normal}(\mu, \sigma^2)$  $(x_N \text{ is asymptotically normal}).$ 

In Definition 3.6,  $x_N$  is not required to be continuous for any N. A good example of where  $x_N$  is discrete for all N but has an asymptotically normal distribution is the Demoivre-Laplace theorem (a special case of the central limit theorem given in Section 3.4), which says that  $x_N \equiv (s_N - Np)/[Np(1-p)]^{1/2}$  has a limiting standard normal distribution, where  $s_N$  has the binomial (N, p) distribution.

DEFINITION 3.7: A sequence of  $K \times 1$  random vectors  $\{\mathbf{x}_N : N = 1, 2, ...\}$  converges in distribution to the continuous random vector  $\mathbf{x}$  if and only if for any  $K \times 1$  nonrandom vector **c** such that  $\mathbf{c}'\mathbf{c} = 1$ ,  $\mathbf{c}'\mathbf{x}_N \xrightarrow{d} \mathbf{c}'\mathbf{x}$ , and we write  $\mathbf{x}_N \xrightarrow{d} \mathbf{x}$ .

When  $\mathbf{x} \sim \text{Normal}(\mathbf{m}, \mathbf{V})$  the requirement in Definition 3.7 is that  $\mathbf{c}' \mathbf{x}_N \stackrel{d}{\rightarrow}$ Normal( $\mathbf{c'm}, \mathbf{c'Vc}$ ) for every  $\mathbf{c} \in \mathbb{R}^K$  such that  $\mathbf{c'c} = 1$ ; in this case we write  $\mathbf{x}_N \xrightarrow{d}$ Normal(m, V) or  $\mathbf{x}_N \stackrel{a}{\sim} \text{Normal}(\mathbf{m}, \mathbf{V})$ . For the derivations in this book,  $\mathbf{m} = \mathbf{0}$ .

{56}------------------------------------------------

LEMMA 3.5: If  $\mathbf{x}_N \xrightarrow{d} \mathbf{x}$ , where  $\mathbf{x}$  is any  $K \times 1$  random vector, then  $\mathbf{x}_N = \mathbf{O}_p(1)$ .

As we will see throughout this book, Lemma 3.5 turns out to be very useful for establishing that a sequence is bounded in probability. Often it is easiest to first verify that a sequence converges in distribution.

LEMMA 3.6: Let  $\{\mathbf{x}_N\}$  be a sequence of  $K \times 1$  random vectors such that  $\mathbf{x}_N \xrightarrow{d} \mathbf{x}$ . If  $\mathbf{g} \colon \mathbb{R}^K \to \mathbb{R}^J$  is a continuous function, then  $\mathbf{g}(\mathbf{x}_N) \stackrel{d}{\to} \mathbf{g}(\mathbf{x})$ .

The usefulness of Lemma 3.6, which is called the **continuous mapping theorem**, cannot be overstated. It tells us that once we know the limiting distribution of  $\mathbf{x}_N$ , we can find the limiting distribution of many interesting functions of  $\mathbf{x}_N$ . This is especially useful for determining the asymptotic distribution of test statistics once the limiting distribution of an estimator is known; see Section 3.5.

The continuity of g is not necessary in Lemma 3.6, but some restrictions are needed. We will only need the form stated in Lemma 3.6.

COROLLARY 3.2: If  $\{\mathbf{z}_N\}$  is a sequence of  $K \times 1$  random vectors such that  $\mathbf{z}_N \stackrel{d}{\to}$ Normal(0, V) then

- (1) For any  $K \times M$  nonrandom matrix  $\mathbf{A}$ ,  $\mathbf{A}'\mathbf{z}_N \overset{d}{\to} \mathrm{Normal}(\mathbf{0}, \mathbf{A}'\mathbf{V}\mathbf{A})$ . (2)  $\mathbf{z}'_N \mathbf{V}^{-1} \mathbf{z}_N \overset{d}{\to} \chi_K^2$  (or  $\mathbf{z}'_N \mathbf{V}^{-1} \mathbf{z}_N \overset{a}{\sim} \chi_K^2$ ).

LEMMA 3.7: Let  $\{\mathbf{x}_N\}$  and  $\{\mathbf{z}_N\}$  be sequences of  $K \times 1$  random vectors. If  $\mathbf{z}_N \stackrel{d}{\to} \mathbf{z}$ and  $\mathbf{x}_N - \mathbf{z}_N \stackrel{p}{\to} \mathbf{0}$ , then  $\mathbf{x}_N \stackrel{d}{\to} \mathbf{z}$ .

Lemma 3.7 is called the **asymptotic equivalence lemma**. In Section 3.5.1 we discuss generally how Lemma 3.7 is used in econometrics. We use the asymptotic equivalence lemma so frequently in asymptotic analysis that after a while we will not even mention that we are using it.

# **Limit Theorems for Random Samples**

In this section we state two classic limit theorems for independent, identically distributed (i.i.d.) sequences of random vectors. These apply when sampling is done randomly from a population.

THEOREM 3.1: Let  $\{\mathbf{w}_i: i=1,2,\ldots\}$  be a sequence of independent, identically distributed  $G \times 1$  random vectors such that  $E(|w_{iq}|) < \infty$ ,  $g = 1, \ldots, G$ . Then the sequence satisfies the weak law of large numbers (WLLN):  $N^{-1} \sum_{i=1}^{N} \mathbf{w}_i \xrightarrow{p} \boldsymbol{\mu}_w$ , where  $\mu_w \equiv \mathrm{E}(\mathbf{w}_i).$ 

{57}------------------------------------------------

THEOREM 3.2 (Lindeberg-Levy): Let  $\{\mathbf{w}_i: i=1,2,\ldots\}$  be a sequence of independent, identically distributed  $G \times 1$  random vectors such that  $E(w_{ig}^2) < \infty, g=1,\ldots,G$ , and  $E(\mathbf{w}_i) = \mathbf{0}$ . Then  $\{\mathbf{w}_i: i=1,2,\ldots\}$  satisfies the **central limit theorem (CLT)**; that is,

$$N^{-1/2} \sum_{i=1}^{N} \mathbf{w}_i \stackrel{d}{\rightarrow} \text{Normal}(\mathbf{0}, \mathbf{B})$$

where  $\mathbf{B} = \mathrm{Var}(\mathbf{w}_i) = \mathrm{E}(\mathbf{w}_i \mathbf{w}_i')$  is necessarily positive semidefinite. For our purposes,  $\mathbf{B}$  is almost always positive definite.

## 3.5 Limiting Behavior of Estimators and Test Statistics

In this section, we apply the previous concepts to sequences of estimators. Because estimators depend on the random outcomes of data, they are properly viewed as random vectors.

### 3.5.1 Asymptotic Properties of Estimators

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

### 3.5.2 Asymptotic Properties of Test Statistics

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