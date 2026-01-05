# Convergence in Probability and Bounded in Probability

> Pages: 53-55

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