# Multiple Treatments

> Pages: 649-652

Sometimes the treatment variable is not simply a scalar. For example, for the population of working high school graduates, w<sup>1</sup> could be credit hours at two-year colleges and w<sup>2</sup> credit hours at four-year colleges. If we make ignorability assumptions of the kind in Section 18.3.1, equation (18.15) extends in a natural way: each treatment variable appears by itself and interacted with the (demeaned) covariates. This approach does not put any restrictions on the nature of the treatments. Alternatively, as in Wooldridge (1999c), Assumption 18.5 extends to a vector w, which leads to an extension of condition (18.60) for multiple treatments.

Wooldridge (2000f ) shows how the IV methods in Section 18.4.1 extend easily to multiple treatments, binary or otherwise. For multiple binary treatments, a reducedform probit is estimated for each treatment, and then terms wijðx<sup>i</sup> xÞ and ^ fij for each treatment j are added to equation (18.47). See Wooldridge (2000f ) for further discussion. An approach based on finding Eðy j w1; ... ; wM; x; zÞ, for M treatments, is difficult but perhaps tractable in some cases.

#### Problems

- 18.1. Consider the difference-in-means estimator, d ¼ y<sup>1</sup> y0, where yg is the sample average of the yi with wi ¼ g, g ¼ 0; 1.
- a. Show that, as an estimator of ATE1, the bias in y<sup>1</sup> y<sup>0</sup> is Eðy<sup>0</sup> j w ¼ 1Þ Eðy<sup>0</sup> j w ¼ 0Þ.
- b. Let y<sup>0</sup> be the earnings someone would earn in the absence of job training, and let w ¼ 1 denote the job training indicator. Explain the meaning of Eðy<sup>0</sup> j w ¼ 1Þ < Eðy<sup>0</sup> j w ¼ 0Þ. Intuitively, does it make sense that Eðd Þ < ATE1?
- 18.2. Show that ATE1ðxÞ is identified under Assumption ATE.1<sup>0</sup> a; Assumption ATE.1<sup>0</sup> b is not needed.
- 18.3. Using the data in JTRAIN2.RAW, repeat the analysis in Example 18.2, using unem78 as the response variable. For comparison, use the same x as in Example 18.2.

{650}------------------------------------------------

Compare the estimates from regressions (18.23) and (18.24), along with the estimate of ATE from linear regression unem78 on 1, train, x.

- 18.4. Carefully derive equation (18.45).
- 18.5. Use the data in JTRAIN2.RAW for this question.
- a. As in Example 18.2, run a probit of train on 1, x, where x contains the covariates from Example 18.2. Obtain the probit fitted values, say F^ <sup>i</sup>.
- b. Estimate the equation re78i ¼ g<sup>0</sup> þ a traini þ xi*g* þ ui by IV, using instruments ð1; F^ <sup>i</sup>; xiÞ. Comment on the estimate of a and its standard error.
- c. Regress F^ <sup>i</sup> on x<sup>i</sup> to obtain the R-squared. What do you make of this result?
- d. Does the nonlinearity of the probit model for train allow us to estimate a when we do not have an additional instrument? Explain.
- 18.6. In Procedure 18.2, explain why it is better to estimate equation (18.36) by IV rather than to run the OLS regression yi on 1, G^i, xi, G^iðx<sup>i</sup> xÞ, i ¼ 1; ... ; N.
- 18.7. Use the data in JTRAIN2.RAW for this question.
- a. In the ignorability setup of Section 18.5.3, let w ¼ mostrn, the number of months spent in job training. Assume that Eðw j xÞ ¼ expðg<sup>0</sup> þ x*g*Þ, where x contains the same covariates as in Example 18.2. Estimate the parameters by nonlinear least squares, and let m^<sup>i</sup> be the fitted values. Which elements of x are significant? (You may use the usual NLS standard errors.)
- b. Suppose that Varðw j xÞ ¼ hðxÞ ¼ d<sup>0</sup> þ d1Eðw j xÞ þ d2½Eðwj xÞ-2 . Use the estimates from part a to estimate the dj. (Hint: Regress the squared NLS residuals on a quadratic in the NLS fitted values.) Are any of ^hi—the estimated variances—negative?
- c. Form ^ri ¼ ðwi m^iÞ=^hi. Estimate equation (18.62) using ^ri as an IV for wi, where gðxÞ¼ð1; xÞ and y ¼ re78. Compare ^b with the OLS estimate of b.
- 18.8. In the IV setup of Section 18.5.3, suppose that b ¼ b, and therefore we can write

$$y = a + \beta w + e$$
,  $E(e \mid a, \mathbf{x}, \mathbf{z}) = 0$ 

Assume that conditions (18.64) and (18.65) hold for a.

a. Suppose w is a corner solution outcome, such as hours spent in a job training program. If z is used as IVs for w in y ¼ g<sup>0</sup> þ bw þ x*g* þ r, what is the identification condition?


{651}------------------------------------------------

b. If w given  $(\mathbf{x}, \mathbf{z})$  follows a standard Tobit model, propose an IV estimator that uses the Tobit fitted values for w.

- c. If  $Var(e \mid a, \mathbf{x}, \mathbf{z}) = \sigma_e^2$  and  $Var(a \mid \mathbf{x}, \mathbf{z}) = \sigma_a^2$ , argue that the IV estimator from part b is asymptotically efficient.
- d. What is an alternative to IV estimation that would use the Tobit fitted values for w? Which method do you prefer?
- e. If  $b \neq \beta$ , but assumptions (18.64) and (18.65) hold, how would you estimate  $\beta$ ?
- **18.9.** Consider the IV approach in Section 18.5.3, under assumptions (18.60), (18.63), (18.64), and (18.65). In place of assumption (18.67), assume that  $E(w | \mathbf{x}, \mathbf{z}, v) = \exp(\pi_0 + \mathbf{x}\pi_1 + \mathbf{z}\pi_2 + \pi_3 v)$ , where v is independent of  $(\mathbf{x}, \mathbf{z})$  with  $E[\exp(\pi_3 v)] = 1$ . (Therefore, w is some nonnegative treatment.)
- a. Show that we can write

$$y = \eta_0 + \mathbf{x}\mathbf{y} + \beta w + w \cdot (\mathbf{x} - \mathbf{\psi})\boldsymbol{\delta} + \xi \mathbf{E}(w \mid \mathbf{x}, \mathbf{z}) + r$$

where  $E(w | \mathbf{x}, \mathbf{z}) = \exp(\eta_0 + \mathbf{x}\boldsymbol{\pi}_1 + \mathbf{z}\boldsymbol{\pi}_2)$  for some  $\pi_0$ , and  $E(r | \mathbf{x}, \mathbf{z}) = 0$ .

- b. Use part a to show that  $\beta$  is not identified. {Hint: Let  $q \equiv E(w \mid \mathbf{x}, \mathbf{z})$ , and let h be any other function of  $(\mathbf{x}, \mathbf{z})$ . Does the linear projection of w on  $[1, \mathbf{x}, h, h \cdot (\mathbf{x} \boldsymbol{\psi}), q]$  depend on h?}
- c. For w > 0 (strictly positive treatment), add the assumption that  $E(u | v, x, z) = \rho v$ . Find E(v | w, x, z) = E(v | v, x, z) and propose a two-step estimator of  $\beta$ .

{652}------------------------------------------------