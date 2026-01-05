# Convergence of Deterministic Sequences

> Pages: 52-53

Asymptotic analysis is concerned with the various kinds of convergence of sequences of estimators as the sample size grows. We begin with some definitions regarding nonstochastic sequences of numbers. When we apply these results in econometrics, N is the sample size, and it runs through all positive integers. You are assumed to have some familiarity with the notion of a limit of a sequence.

DEFINITION 3.1: (1) A sequence of nonrandom numbers  $\{a_N: N=1,2,\ldots\}$  converges to a (has limit a) if for all  $\varepsilon>0$ , there exists  $N_\varepsilon$  such that if  $N>N_\varepsilon$  then  $|a_N-a|<\varepsilon$ . We write  $a_N\to a$  as  $N\to\infty$ .

(2) A sequence  $\{a_N: N=1,2,\ldots\}$  is *bounded* if and only if there is some  $b<\infty$  such that  $|a_N| \le b$  for all  $N=1,2,\ldots$  Otherwise, we say that  $\{a_N\}$  is *unbounded*.

These definitions apply to vectors and matrices element by element.

Example 3.1: (1) If  $a_N = 2 + 1/N$ , then  $a_N \to 2$ . (2) If  $a_N = (-1)^N$ , then  $a_N$  does not have a limit, but it is bounded. (3) If  $a_N = N^{1/4}$ ,  $a_N$  is not bounded. Because  $a_N$  increases without bound, we write  $a_N \to \infty$ .

DEFINITION 3.2: (1) A sequence  $\{a_N\}$  is  $O(N^{\lambda})$  (at most of order  $N^{\lambda}$ ) if  $N^{-\lambda}a_N$  is bounded. When  $\lambda = 0$ ,  $\{a_N\}$  is bounded, and we also write  $a_N = O(1)$  (big oh one). (2)  $\{a_N\}$  is  $O(N^{\lambda})$  if  $N^{-\lambda}a_N \to 0$ . When  $\lambda = 0$ ,  $a_N$  converges to zero, and we also write  $a_N = O(1)$  (little oh one).

From the definitions, it is clear that if  $a_N = o(N^{\lambda})$ , then  $a_N = O(N^{\lambda})$ ; in particular, if  $a_N = o(1)$ , then  $a_N = O(1)$ . If each element of a sequence of vectors or matrices is  $O(N^{\lambda})$ , we say the sequence of vectors or matrices is  $O(N^{\lambda})$ , and similarly for  $o(N^{\lambda})$ .

Example 3.2: (1) If  $a_N = \log(N)$ , then  $a_N = o(N^{\lambda})$  for any  $\lambda > 0$ . (2) If  $a_N = 10 + \sqrt{N}$ , then  $a_N = O(N^{1/2})$  and  $a_N = o(N^{(1/2+\gamma)})$  for any  $\gamma > 0$ .

{53}------------------------------------------------