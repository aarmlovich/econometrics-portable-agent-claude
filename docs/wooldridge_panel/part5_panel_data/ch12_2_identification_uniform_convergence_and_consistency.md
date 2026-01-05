# Identification, Uniform Convergence, and Consistency

> Pages: 356-360

We now present a formal consistency result for M-estimators under fairly weak assumptions. As mentioned previously, the conditions can be broken down into two parts. The first part is the **identification** or **identifiability** of  $\theta_o$ . For nonlinear regression, we showed how  $\theta_o$  solves the population problem (12.3). However, we did not argue that  $\theta_o$  is always the *unique* solution to problem (12.3). Whether or not this is the case depends on the distribution of  $\mathbf{x}$  and the nature of the regression function:

ASSUMPTION NLS.2: 
$$E\{[m(\mathbf{x}, \boldsymbol{\theta}_{o}) - m(\mathbf{x}, \boldsymbol{\theta})]^{2}\} > 0$$
, all  $\boldsymbol{\theta} \in \boldsymbol{\Theta}$ ,  $\boldsymbol{\theta} \neq \boldsymbol{\theta}_{o}$ .

Assumption NLS.2 plays the same role as Assumption OLS.2 in Chapter 4. It can fail if the explanatory variables  $\mathbf{x}$  do not have sufficient variation in the population. In fact, in the linear case  $m(\mathbf{x}, \boldsymbol{\theta}) = \mathbf{x}\boldsymbol{\theta}$ , Assumption NLS.2 holds if and only if rank  $E(\mathbf{x}'\mathbf{x}) = K$ , which is just Assumption OLS.2 from Chapter 4. In nonlinear models, Assumption NLS.2 can fail if  $m(\mathbf{x}, \boldsymbol{\theta}_0)$  depends on fewer parameters than are actually in  $\boldsymbol{\theta}$ . For example, suppose that we choose as our model  $m(\mathbf{x}, \boldsymbol{\theta}) = \theta_1 + \theta_2 x_2 + \theta_3 x_3^{\theta_4}$ , but the true model is linear:  $\theta_{03} = 0$ . Then  $E[(y - m(\mathbf{x}, \boldsymbol{\theta}))]^2$  is minimized for any  $\boldsymbol{\theta}$  with  $\theta_1 = \theta_{01}$ ,  $\theta_2 = \theta_{02}$ ,  $\theta_3 = 0$ , and  $\theta_4$  any value. If  $\theta_{03} \neq 0$ , Assumption NLS.2

{357}------------------------------------------------

would typically hold provided there is sufficient variation in  $x_2$  and  $x_3$ . Because identification fails for certain values of  $\theta_0$ , this is an example of a **poorly identified** model. (See Section 9.5 for other examples of poorly identified models.)

Identification in commonly used nonlinear regression models, such as exponential and logistic regression functions, holds under weak conditions, provided perfect collinearity in  $\mathbf{x}$  can be ruled out. For the most part, we will just assume that, when the model is correctly specified,  $\theta_0$  is the unique solution to problem (12.3). For the general M-estimation case, we assume that  $q(\mathbf{w}, \theta)$  has been chosen so that  $\theta_0$  is a solution to problem (12.9). Identification requires that  $\theta_0$  be the unique solution:

$$E[q(\mathbf{w}, \boldsymbol{\theta}_{0})] < E[q(\mathbf{w}, \boldsymbol{\theta})], \quad \text{all } \boldsymbol{\theta} \in \boldsymbol{\Theta}, \quad \boldsymbol{\theta} \neq \boldsymbol{\theta}_{0}$$
 (12.11)

The second component for consistency of the M-estimator is convergence of the sample average  $N^{-1}\sum_{i=1}^N q(\mathbf{w}_i, \boldsymbol{\theta})$  to its expected value. It turns out that **pointwise convergence in probability**, as stated in equation (12.10), is not sufficient for consistency. That is, it is not enough to simply invoke the usual weak law of large numbers at each  $\boldsymbol{\theta} \in \boldsymbol{\Theta}$ . Instead, **uniform convergence in probability** is sufficient. Mathematically,

$$\max_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \left| N^{-1} \sum_{i=1}^{N} q(\mathbf{w}_i, \boldsymbol{\theta}) - \mathbb{E}[q(\mathbf{w}, \boldsymbol{\theta})] \right| \stackrel{p}{\to} 0$$
 (12.12)

Uniform convergence clearly implies pointwise convergence, but the converse is not true: it is possible for equation (12.10) to hold but equation (12.12) to fail. Nevertheless, under certain regularity conditions, the pointwise convergence in equation (12.10) translates into the uniform convergence in equation (12.12).

To state a formal result concerning uniform convergence, we need to be more careful in stating assumptions about the function  $q(\cdot,\cdot)$  and the parameter space  $\Theta$ . Since we are taking expected values of  $q(\mathbf{w}, \theta)$  with respect to the distribution of  $\mathbf{w}$ ,  $q(\mathbf{w}, \theta)$  must be a random variable for each  $\theta \in \Theta$ . Technically, we should assume that  $q(\cdot, \theta)$  is a *Borel measurable function* on  $\mathscr{W}$  for each  $\theta \in \Theta$ . Since it is very difficult to write down a function that is not Borel measurable, we spend no further time on it. Rest assured that any objective function that arises in econometrics is Borel measurable. You are referred to Billingsley (1979) and Davidson (1994, Chapter 3).

The next assumption concerning q is practically more important. We assume that, for each  $\mathbf{w} \in \mathcal{W}$ ,  $q(\mathbf{w}, \cdot)$  is a *continuous function* over the parameter space  $\mathbf{\Theta}$ . All of the problems we treat in detail have objective functions that are continuous in the parameters, but these do not cover all cases of interest. For example, Manski's (1975) maximum score estimator for binary response models has an objective function that is not continuous in  $\theta$ . (We cover binary response models in Chapter 15.) It is possi-

{358}------------------------------------------------

ble to somewhat relax the continuity assumption in order to handle such cases, but we will not need that generality. See Manski (1988, Section 7.3) and Newey and McFadden (1994).

Obtaining uniform convergence is generally difficult for unbounded parameter sets, such as  $\Theta = \mathbb{R}^P$ . It is easiest to assume that  $\Theta$  is a *compact subset* of  $\mathbb{R}^P$ , which means that  $\Theta$  is closed and bounded (see Rudin, 1976, Theorem 2.41). Because the natural parameter spaces in most applications are not bounded (and sometimes not closed), the compactness assumption is unattractive for developing a general theory of estimation. However, for most applications it is not an assumption to worry about:  $\Theta$  can be defined to be such a large closed and bounded set as to always contain  $\theta_o$ . Some consistency results for nonlinear estimation without compact parameter spaces are available; see the discussion and references in Newey and McFadden (1994).

We can now state a theorem concerning uniform convergence appropriate for the random sampling environment. This result, known as the **uniform weak law of large numbers (UWLLN)**, dates back to LeCam (1953). See also Newey and McFadden (1994, Lemma 2.4).

THEOREM 12.1 (Uniform Weak Law of Large Numbers): Let  $\mathbf{w}$  be a random vector taking values in  $\mathscr{W} \subset \mathbb{R}^M$ , let  $\mathbf{\Theta}$  be a subset of  $\mathbb{R}^P$ , and let  $q:\mathscr{W} \times \mathbf{\Theta} \to \mathbb{R}$  be a real-valued function. Assume that (a)  $\mathbf{\Theta}$  is compact; (b) for each  $\theta \in \mathbf{\Theta}$ ,  $q(\cdot, \theta)$  is Borel measurable on  $\mathscr{W}$ ; (c) for each  $\mathbf{w} \in \mathscr{W}$ ,  $q(\mathbf{w}, \cdot)$  is continuous on  $\mathbf{\Theta}$ ; and (d)  $|q(\mathbf{w}, \theta)| \le b(\mathbf{w})$  for all  $\theta \in \mathbf{\Theta}$ , where b is a nonnegative function on  $\mathscr{W}$  such that  $\mathrm{E}[b(\mathbf{w})] < \infty$ . Then equation (12.12) holds.

The only assumption we have not discussed is assumption d, which requires the expected absolute value of  $q(\mathbf{w}, \boldsymbol{\theta})$  to be bounded across  $\boldsymbol{\theta}$ . This kind of moment condition is rarely verified in practice, although, with some work, it can be; see Newey and McFadden (1994) for examples.

The continuity and compactness assumptions are important for establishing uniform convergence, and they also ensure that both the sample minimization problem (12.8) and the population minimization problem (12.9) actually have solutions. Consider problem (12.8) first. Under the assumptions of Theorem 12.1, the sample average is a continuous function of  $\theta$ , since  $q(\mathbf{w}_i, \theta)$  is continuous for each  $\mathbf{w}_i$ . Since a continuous function on a compact space always achieves its minimum, the M-estimation problem is well defined (there could be more than one solution). As a technical matter, it can be shown that  $\hat{\theta}$  is actually a random variable under the measurability assumption on  $q(\cdot, \theta)$ . See, for example, Gallant and White (1988).

It can also be shown that, under the assumptions of Theorem 12.1, the function  $E[q(\mathbf{w}, \boldsymbol{\theta})]$  is continuous as a function of  $\boldsymbol{\theta}$ . Therefore, problem (12.9) also has at least

{359}------------------------------------------------

one solution; identifiability ensures that it has only one solution, and this fact implies consistency of the M-estimator.

THEOREM 12.2 (Consistency of M-Estimators): Under the assumptions of Theorem 12.1, assume that the identification assumption (12.11) holds. Then a random vector,  $\hat{\boldsymbol{\theta}}$ , solves problem (12.8), and  $\hat{\boldsymbol{\theta}} \stackrel{p}{\rightarrow} \boldsymbol{\theta}_{o}$ .

A proof of Theorem 12.2 is given in Newey and McFadden (1994). For nonlinear least squares, once Assumptions NLS.1 and NLS.2 are maintained, the practical requirement is that  $m(\mathbf{x}, \cdot)$  be a continuous function over  $\Theta$ . Since this assumption is almost always true in applications of NLS, we do not list it as a separate assumption. Noncompactness of  $\Theta$  is not much of a concern for most applications.

Theorem 12.2 also applies to **median regression**. Suppose that the conditional median of y given  $\mathbf{x}$  is  $\mathrm{Med}(y \mid \mathbf{x}) = m(\mathbf{x}, \theta_0)$ , where  $m(\mathbf{x}, \theta)$  is a known function of  $\mathbf{x}$  and  $\boldsymbol{\theta}$ . The leading case is a linear model,  $m(\mathbf{x}, \boldsymbol{\theta}) = \mathbf{x}\boldsymbol{\theta}$ , where  $\mathbf{x}$  contains unity. The **least absolute deviations (LAD) estimator** of  $\boldsymbol{\theta}_0$  solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} N^{-1} \sum_{i=1}^{N} |y_i - m(\mathbf{x}_i, \boldsymbol{\theta})|$$

If  $\Theta$  is compact and  $m(\mathbf{x},\cdot)$  is continuous over  $\Theta$  for each  $\mathbf{x}$ , a solution always exists. The LAD estimator is motivated by the fact that  $\theta_0$  minimizes  $\mathrm{E}[|y-m(\mathbf{x},\theta)|]$  over the parameter space  $\Theta$ ; this follows by the fact that for each  $\mathbf{x}$ , the conditional median is the minimum absolute loss predictor conditional on  $\mathbf{x}$ . (See, for example, Bassett and Koenker, 1978, and Manski, 1988, Section 4.2.2.) If we assume that  $\theta_0$  is the unique solution—a standard identification assumption—then the LAD estimator is consistent very generally. In addition to the continuity, compactness, and identification assumptions, it suffices that  $\mathrm{E}[|y|] < \infty$  and  $|m(\mathbf{x},\theta)| \le a(\mathbf{x})$  for some function  $a(\cdot)$  such that  $\mathrm{E}[a(\mathbf{x})] < \infty$ . [To see this point, take  $b(\mathbf{w}) \equiv |y| + a(\mathbf{x})$  in Theorem 12.2.]

Median regression is a special case of **quantile regression**, where we model quantiles in the distribution of y given x. For example, in addition to the median, we can estimate how the first and third quartiles in the distribution of y given x change with x. Except for the median (which leads to LAD), the objective function that identifies a conditional quantile is asymmetric about zero. See, for example, Koenker and Bassett (1978) and Manski (1988, Section 4.2.4). Buchinsky (1994) applies quantile regression methods to examine factors affecting the distribution of wages in the United States over time.

We end this section with a lemma that we use repeatedly in the rest of this chapter. It follows from Lemma 4.3 in Newey and McFadden (1994).

{360}------------------------------------------------

LEMMA 12.1: Suppose that  $\hat{\boldsymbol{\theta}} \stackrel{p}{\to} \boldsymbol{\theta}_0$ , and assume that  $r(\mathbf{w}, \boldsymbol{\theta})$  satisfies the same assumptions on  $q(\mathbf{w}, \boldsymbol{\theta})$  in Theorem 12.2. Then

$$N^{-1} \sum_{i=1}^{N} r(\mathbf{w}_i, \hat{\boldsymbol{\theta}}) \stackrel{p}{\to} \mathrm{E}[r(\mathbf{w}, \boldsymbol{\theta}_{\mathrm{o}})]$$
 (12.13)

That is,  $N^{-1} \sum_{i=1}^{N} r(\mathbf{w}_i, \hat{\boldsymbol{\theta}})$  is a consistent estimator of  $E[r(\mathbf{w}, \boldsymbol{\theta}_0)]$ .

Intuitively, Lemma 12.1 is quite reasonable. We know that  $N^{-1} \sum_{i=1}^{N} r(\mathbf{w}_i, \boldsymbol{\theta}_0)$  generally converges in probability to  $E[r(\mathbf{w}, \boldsymbol{\theta}_0)]$  by the law of large numbers. Lemma 12.1 shows that, if we replace  $\boldsymbol{\theta}_0$  with a consistent estimator, the convergence still holds, at least under standard regularity conditions.