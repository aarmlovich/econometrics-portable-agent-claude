# Convergence in Distribution

> Pages: 55-57

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