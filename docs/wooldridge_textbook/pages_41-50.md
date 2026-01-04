

{41}------------------------------------------------

because we assume that a random sample can be obtained on ðy; x; wÞ. [Alternatively, when we write down parametric econometric models, we will be able to derive Eðy j x; wÞ.] Then, estimating the average partial effect at any chosen x<sup>o</sup> amounts to averaging qm^2ðx<sup>o</sup>; wiÞ=qxj across the random sample, where m2ðx; wÞ 1Eðy j x; wÞ.

Proving equation (2.35) is fairly simple. First, we have

$$\mu_2(\mathbf{x}, \mathbf{w}) = \mathrm{E}[\mathrm{E}(y \mid \mathbf{x}, q, \mathbf{w}) \mid \mathbf{x}, \mathbf{w}] = \mathrm{E}[\mu_1(\mathbf{x}, q) \mid \mathbf{x}, \mathbf{w}] = \int_{\mathbb{R}} \mu_1(\mathbf{x}, q) g(\mathbf{y} \mid \mathbf{w}) d\mathbf{y}$$

where the first equality follows from the law of iterated expectations, the second equality follows from equation (2.34), and the third equality follows from equation (2.33). If we now take the partial derivative with respect to xj of the equality

$$\mu_2(\mathbf{x}, \mathbf{w}) = \int_{\mathbb{R}} \mu_1(\mathbf{x}, q) g(\mathbf{y} \mid \mathbf{w}) d\mathbf{y}$$
 (2.36)

and interchange the partial derivative and the integral, we have, for any ðx; wÞ,

$$\partial \mu_2(\mathbf{x}, \mathbf{w}) / \partial x_j = \int_{\mathbb{R}} \theta_j(\mathbf{x}, \varphi) g(\varphi \mid \mathbf{w}) \, d\varphi \tag{2.37}$$

For fixed xo, the right-hand side of equation (2.37) is simply E½yjðx<sup>o</sup>; qÞ j w-, and so another application of iterated expectations gives, for any xo,

$$\mathbf{E}_{w}[\partial \mu_{2}(\mathbf{x}^{o}, \mathbf{w})/\partial x_{j}] = \mathbf{E}\{\mathbf{E}[\theta_{j}(\mathbf{x}^{o}, q) \mid \mathbf{w}]\} = \delta_{j}(\mathbf{x}^{o})$$

which is what we wanted to show.

As mentioned previously, equation (2.35) has many applications in models where unobserved heterogeneity enters a conditional mean function in a nonadditive fashion. We will use this result (in simplified form) in Chapter 4, and also extensively in Part III. The special case where q is independent of x—and so we do not need the proxy variables w—is very simple: the APE of xj on Eðy j x; qÞ is simply the partial effect of xj on m2ðxÞ ¼ Eðy j xÞ. In other words, if we focus on average partial effects, there is no need to introduce heterogeneity. If we do specify a model with heterogeneity independent of x, then we simply find Eðy j xÞ by integrating Eðy j x; qÞ over the distribution of q.

## 2.3 Linear Projections

In the previous section we saw some examples of how to manipulate conditional expectations. While structural equations are usually stated in terms of CEs, making 

{42}------------------------------------------------

linearity assumptions about CEs involving unobservables or auxiliary variables is undesirable, especially if such assumptions can be easily relaxed.

By using the notion of a linear projection we can often relax linearity assumptions in auxiliary conditional expectations. Typically this is done by first writing down a structural model in terms of a CE and then using the linear projection to obtain an estimable equation. As we will see in Chapters 4 and 5, this approach has many applications.

Generally, let y; x1; ... ; xK be random variables representing some population such that Eðy<sup>2</sup>Þ < y, Eðx<sup>2</sup> <sup>j</sup> Þ < y, j ¼ 1; 2; ... ; K. These assumptions place no practical restrictions on the joint distribution of ðy; x1; x2; ... ; xK Þ: the vector can contain discrete and continuous variables, as well as variables that have both characteristics. In many cases y and the xj are nonlinear functions of some underlying variables that are initially of interest.

Define x1 ðx1; ... ; xK Þ as a 1 K vector, and make the assumption that the K K variance matrix of x is nonsingular (positive definite). Then the linear projection of y on 1; x1; x2; ... ; xK always exists and is unique:

$$L(y | 1, x_1, \dots x_K) = L(y | 1, \mathbf{x}) = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K = \beta_0 + \mathbf{x} \boldsymbol{\beta}$$
 (2.38)

where, by definition,

$$\boldsymbol{\beta} \equiv [\operatorname{Var}(\mathbf{x})]^{-1} \operatorname{Cov}(\mathbf{x}, y) \tag{2.39}$$

$$\beta_0 \equiv \mathbf{E}(y) - \mathbf{E}(\mathbf{x})\boldsymbol{\beta} = \mathbf{E}(y) - \beta_1 \mathbf{E}(x_1) - \dots - \beta_K \mathbf{E}(x_K)$$
(2.40)

The matrix VarðxÞ is the K K symmetric matrix with ðj; kÞth element given by Covðxj; xkÞ, while Covðx; yÞ is the K 1 vector with jth element Covðxj; yÞ. When K ¼ 1 we have the familiar results b<sup>1</sup> 1Covðx1; yÞ=Varðx1Þ and b<sup>0</sup> 1 EðyÞ b1Eðx1Þ. As its name suggests, Lðy j 1; x1; x2; ... ; xK Þ is always a linear function of the xj.

Other authors use a different notation for linear projections, the most common being E ð j Þ and Pð j Þ. [For example, Chamberlain (1984) and Goldberger (1991) use E ð j Þ.] Some authors omit the 1 in the definition of a linear projection because it is assumed that an intercept is always included. Although this is usually the case, we put unity in explicitly to distinguish equation (2.38) from the case that a zero intercept is intended. The linear projection of y on x1; x2; ... ; xK is defined as

$$L(y | \mathbf{x}) = L(y | x_1, x_2, ..., x_K) = \gamma_1 x_1 + \gamma_2 x_2 + \cdots + \gamma_K x_K = \mathbf{x} \gamma$$

where *g*1ðEðx<sup>0</sup> xÞÞ<sup>1</sup> Eðx<sup>0</sup> yÞ. Note that *g* 0*b* unless EðxÞ ¼ 0. Later, we will include unity as an element of x, in which case the linear projection including an intercept can be written as Lðy j xÞ.

{43}------------------------------------------------

The linear projection is just another way of writing down a population linear model where the disturbance has certain properties. Given the linear projection in equation (2.38) we can always write

$$y = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + u \tag{2.41}$$

where the error term u has the following properties (by definition of a linear projection): Eðu<sup>2</sup>Þ < y and

$$E(u) = 0,$$
  $Cov(x_j, u) = 0,$   $j = 1, 2, ..., K$  (2.42)

In other words, u has zero mean and is uncorrelated with every xj. Conversely, given equations (2.41) and (2.42), the parameters b<sup>j</sup> in equation (2.41) must be the parameters in the linear projection of y on 1; x1; ... ; xK given by definitions (2.39) and (2.40). Sometimes we will write a linear projection in error form, as in equations (2.41) and (2.42), but other times the notation (2.38) is more convenient.

It is important to emphasize that when equation (2.41) represents the linear projection, all we can say about u is contained in equation (2.42). In particular, it is not generally true that u is independent of x or that Eðu j xÞ ¼ 0. Here is another way of saying the same thing: equations (2.41) and (2.42) are definitional. Equation (2.41) under Eðu j xÞ ¼ 0 is an assumption that the conditional expectation is linear.

The linear projection is sometimes called the minimum mean square linear predictor or the least squares linear predictor because b<sup>0</sup> and *b* can be shown to solve the following problem:

$$\min_{b_0, \mathbf{b} \in \mathbb{R}^K} E[(y - b_0 - \mathbf{x}\mathbf{b})^2]$$
 (2.43)

(see Property LP.6 in the appendix). Because the CE is the minimum mean square predictor—that is, it gives the smallest mean square error out of all (allowable) functions (see Property CE.8)—it follows immediately that if Eðy j xÞ is linear in x then the linear projection coincides with the conditional expectation.

As with the conditional expectation operator, the linear projection operator satisfies some important iteration properties. For vectors x and z,

$$L(y | 1, \mathbf{x}) = L[L(y | 1, \mathbf{x}, \mathbf{z}) | 1, \mathbf{x}]$$
(2.44)

This simple fact can be used to derive omitted variables bias in a general setting as well as proving properties of estimation methods such as two-stage least squares and certain panel data methods.

Another iteration property that is useful involves taking the linear projection of a conditional expectation:

{44}------------------------------------------------

$$L(y \mid 1, \mathbf{x}) = L[E(y \mid \mathbf{x}, \mathbf{z}) \mid 1, \mathbf{x}]$$
(2.45)

Often we specify a structural model in terms of a conditional expectation Eðy j x; zÞ (which is frequently linear), but, for a variety of reasons, the estimating equations are based on the linear projection Lðy j 1; xÞ. If Eðy j x; zÞ is linear in x and z, then equations (2.45) and (2.44) say the same thing.

For example, assume that

$$E(y | x_1, x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1 x_2$$

and define z<sup>1</sup> 1 x1x2. Then, from Property CE.3,

$$E(y \mid x_1, x_2, z_1) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 z_1$$
(2.46)

The right-hand side of equation (2.46) is also the linear projection of y on 1; x1; x2, and z1; it is not generally the linear projection of y on 1; x1; x2.

Our primary use of linear projections will be to obtain estimable equations involving the parameters of an underlying conditional expectation of interest. Problems 2.2 and 2.3 show how the linear projection can have an interesting interpretation in terms of the structural parameters.

## Problems

2.1. Given random variables y, x1, and x2, consider the model

$$E(y | x_1, x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_2^2 + \beta_4 x_1 x_2$$

- a. Find the partial effects of x<sup>1</sup> and x<sup>2</sup> on Eðy j x1; x2Þ.
- b. Writing the equation as

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_2^2 + \beta_4 x_1 x_2 + u$$

what can be said about Eðu j x1; x2Þ? What about Eðu j x1; x2; x<sup>2</sup> <sup>2</sup> ; x1x2Þ?

- c. In the equation of part b, what can be said about Varðu j x1; x2Þ?
- 2.2. Let y and x be scalars such that

$$E(y | x) = \delta_0 + \delta_1(x - \mu) + \delta_2(x - \mu)^2$$

where m ¼ EðxÞ.

- a. Find qEðy j xÞ=qx, and comment on how it depends on x.
- b. Show that d<sup>1</sup> is equal to qEðy j xÞ=qx averaged across the distribution of x.

{45}------------------------------------------------

c. Suppose that x has a symmetric distribution, so that E½ðx mÞ 3 ¼ 0. Show that Lðy j 1; xÞ ¼ a<sup>0</sup> þ d1x for some a0. Therefore, the coefficient on x in the linear projection of y on ð1; xÞ measures something useful in the nonlinear model for Eðy j xÞ: it is the partial effect qEðy j xÞ=qx averaged across the distribution of x.

## 2.3. Suppose that

$$E(y \mid x_1, x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1 x_2$$
(2.47)

- a. Write this expectation in error form (call the error u), and describe the properties of u.
- b. Suppose that x<sup>1</sup> and x<sup>2</sup> have zero means. Show that b<sup>1</sup> is the expected value of qEðy j x1; x2Þ=qx<sup>1</sup> (where the expectation is across the population distribution of x2). Provide a similar interpretation for b2.
- c. Now add the assumption that x<sup>1</sup> and x<sup>2</sup> are independent of one another. Show that the linear projection of y on ð1; x1; x2Þ is

$$L(y | 1, x_1, x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2$$
(2.48)

(Hint: Show that, under the assumptions on x<sup>1</sup> and x2, x1x<sup>2</sup> has zero mean and is uncorrelated with x<sup>1</sup> and x2.)

- d. Why is equation (2.47) generally more useful than equation (2.48)?
- 2.4. For random scalars u and v and a random vector x, suppose that Eðu j x; vÞ is a linear function of ðx; vÞ and that u and v each have zero mean and are uncorrelated with the elements of x. Show that Eðu j x; vÞ ¼ Eðu j vÞ ¼ r1v for some r1.
- 2.5. Consider the two representations

$$y = \mu_1(\mathbf{x}, \mathbf{z}) + u_1,$$
  $E(u_1 \mid \mathbf{x}, \mathbf{z}) = 0$   
 $y = \mu_2(\mathbf{x}) + u_2,$   $E(u_2 \mid \mathbf{x}) = 0$ 

Assuming that Varðy j x; zÞ and Varðy j xÞ are both constant, what can you say about the relationship between Varðu1Þ and Varðu2Þ? (Hint: Use Property CV.4 in the appendix.)

2.6. Let x be a 1 K random vector, and let q be a random scalar. Suppose that q can be expressed as q ¼ q þ e, where EðeÞ ¼ 0 and Eðx<sup>0</sup> eÞ ¼ 0. Write the linear projection of q onto ð1; xÞ as q ¼ d<sup>0</sup> þ d1x<sup>1</sup> þþ d<sup>K</sup> xK þ r, where EðrÞ ¼ 0 and Eðx<sup>0</sup> rÞ ¼ 0.

{46}------------------------------------------------

a. Show that

$$L(q \mid 1, \mathbf{x}) = \delta_0 + \delta_1 x_1 + \dots + \delta_K x_K$$

b. Find the projection error  $r \equiv q - L(q \mid 1, \mathbf{x})$  in terms of  $r^*$  and e.

# **2.7.** Consider the conditional expectation

$$E(y | \mathbf{x}, \mathbf{z}) = g(\mathbf{x}) + \mathbf{z}\boldsymbol{\beta}$$

where  $g(\cdot)$  is a general function of **x** and  $\beta$  is a  $1 \times M$  vector. Show that

$$E(\tilde{y} | \tilde{z}) = \tilde{z}\beta$$

where 
$$\tilde{y} \equiv y - E(y \mid \mathbf{x})$$
 and  $\tilde{\mathbf{z}} \equiv \mathbf{z} - E(\mathbf{z} \mid \mathbf{x})$ .

#### Appendix 2A

#### **2.A.1** Properties of Conditional Expectations

PROPERTY CE.1: Let  $a_1(\mathbf{x}), \dots, a_G(\mathbf{x})$  and  $b(\mathbf{x})$  be scalar functions of  $\mathbf{x}$ , and let  $y_1, \dots, y_G$  be random scalars. Then

$$E\left(\sum_{j=1}^{G} a_j(\mathbf{x}) y_j + b(\mathbf{x}) \mid \mathbf{x}\right) = \sum_{j=1}^{G} a_j(\mathbf{x}) E(y_j \mid \mathbf{x}) + b(\mathbf{x})$$

provided that  $E(|y_j|) < \infty$ ,  $E[|a_j(\mathbf{x})y_j|] < \infty$ , and  $E[|b(\mathbf{x})|] < \infty$ . This is the sense in which the conditional expectation is a linear operator.

PROPERTY CE.2: 
$$E(y) = E[E(y | \mathbf{x})] \equiv E[\mu(\mathbf{x})].$$

Property CE.2 is the simplest version of the law of iterated expectations. As an illustration, suppose that  $\mathbf{x}$  is a discrete random vector taking on values  $\mathbf{c}_1, \mathbf{c}_2, \dots, \mathbf{c}_M$  with probabilities  $p_1, p_2, \dots, p_M$ . Then the LIE says

$$E(y) = p_1 E(y \mid \mathbf{x} = \mathbf{c}_1) + p_2 E(y \mid \mathbf{x} = \mathbf{c}_2) + \dots + p_M E(y \mid \mathbf{x} = \mathbf{c}_M)$$
(2.49)

In other words, E(y) is simply a weighted average of the  $E(y | \mathbf{x} = \mathbf{c}_j)$ , where the weight  $p_j$  is the probability that  $\mathbf{x}$  takes on the value  $\mathbf{c}_j$ .

PROPERTY CE.3: (1)  $E(y | \mathbf{x}) = E[E(y | \mathbf{w}) | \mathbf{x}]$ , where  $\mathbf{x}$  and  $\mathbf{w}$  are vectors with  $\mathbf{x} = \mathbf{f}(\mathbf{w})$  for some nonstochastic function  $\mathbf{f}(\cdot)$ . (This is the general version of the law of iterated expectations.)

(2) As a special case of part 1,  $E(y | \mathbf{x}) = E[E(y | \mathbf{x}, \mathbf{z}) | \mathbf{x}]$  for vectors  $\mathbf{x}$  and  $\mathbf{z}$ .

{47}------------------------------------------------

PROPERTY CE.4: If  $\mathbf{f}(\mathbf{x}) \in \mathbb{R}^J$  is a function of  $\mathbf{x}$  such that  $\mathrm{E}(y \mid \mathbf{x}) = g[\mathbf{f}(\mathbf{x})]$  for some scalar function  $g(\cdot)$ , then  $\mathrm{E}[y \mid \mathbf{f}(\mathbf{x})] = \mathrm{E}(y \mid \mathbf{x})$ .

PROPERTY CE.5: If the vector  $(\mathbf{u}, \mathbf{v})$  is independent of the vector  $\mathbf{x}$ , then  $E(\mathbf{u} \mid \mathbf{x}, \mathbf{v}) = E(\mathbf{u} \mid \mathbf{v})$ .

PROPERTY CE.6: If  $u \equiv y - \mathrm{E}(y \mid \mathbf{x})$ , then  $\mathrm{E}[\mathbf{g}(\mathbf{x})u] = \mathbf{0}$  for any function  $\mathbf{g}(\mathbf{x})$ , provided that  $\mathrm{E}[|g_j(\mathbf{x})u|] < \infty$ ,  $j = 1, \ldots, J$ , and  $\mathrm{E}(|u|) < \infty$ . In particular,  $\mathrm{E}(u) = 0$  and  $\mathrm{Cov}(x_j, u) = 0$ ,  $j = 1, \ldots, K$ .

**Proof:** First, note that

$$E(u | \mathbf{x}) = E[(v - E(v | \mathbf{x})) | \mathbf{x}] = E[(v - \mu(\mathbf{x})) | \mathbf{x}] = E(v | \mathbf{x}) - \mu(\mathbf{x}) = 0$$

Next, by property CE.2,  $E[\mathbf{g}(\mathbf{x})u] = E(E[\mathbf{g}(\mathbf{x})u \mid \mathbf{x}]) = E[\mathbf{g}(\mathbf{x})E(u \mid \mathbf{x})]$  (by property CE.1) = **0** because  $E(u \mid \mathbf{x}) = 0$ .

PROPERTY CE.7 (Conditional Jensen's Inequality): If  $c: \mathbb{R} \to \mathbb{R}$  is a convex function defined on  $\mathbb{R}$  and  $E[|y|] < \infty$ , then

$$c[E(y \mid \mathbf{x})] \le E[c(y) \mid \mathbf{x}]$$

Technically, we should add the statement "almost surely- $P_x$ ," which means that the inequality holds for all x in a set that has probability equal to one. As a special case,  $[E(y)]^2 \le E(y^2)$ . Also, if y > 0, then  $-\log[E(y)] \le E[-\log(y)]$ , or  $E[\log(y)] \le \log[E(y)]$ .

PROPERTY CE.8: If  $E(y^2) < \infty$  and  $\mu(\mathbf{x}) \equiv E(y | \mathbf{x})$ , then  $\mu$  is a solution to

$$\min_{m \in \mathcal{M}} E[(y - m(\mathbf{x}))^2]$$

where  $\mathcal{M}$  is the set of functions  $m: \mathbb{R}^K \to \mathbb{R}$  such that  $\mathrm{E}[m(\mathbf{x})^2] < \infty$ . In other words,  $\mu(\mathbf{x})$  is the best mean square predictor of y based on information contained in  $\mathbf{x}$ .

*Proof:* By the conditional Jensen's inequality, if follows that  $E(y^2) < \infty$  implies  $E[\mu(\mathbf{x})^2] < \infty$ , so that  $\mu \in \mathcal{M}$ . Next, for any  $m \in \mathcal{M}$ , write

$$E[(y - m(\mathbf{x}))^{2}] = E[\{(y - \mu(\mathbf{x})) + (\mu(\mathbf{x}) - m(\mathbf{x}))\}^{2}]$$
  
=  $E[(y - \mu(\mathbf{x}))^{2}] + E[(\mu(\mathbf{x}) - m(\mathbf{x}))^{2}] + 2E[(\mu(\mathbf{x}) - m(\mathbf{x}))u]$ 

where  $u \equiv y - \mu(\mathbf{x})$ . Thus, by CE.6,

$$E[(y - m(\mathbf{x}))^2] = E(u^2) + E[(\mu(\mathbf{x}) - m(\mathbf{x}))^2].$$

The right-hand side is clearly minimized at  $m \equiv \mu$ .

{48}------------------------------------------------

## 2.A.2 Properties of Conditional Variances

The conditional variance of y given x is defined as

$$Var(y \mid \mathbf{x}) \equiv \sigma^2(\mathbf{x}) \equiv E[\{y - E(y \mid \mathbf{x})\}^2 \mid \mathbf{x}] = E(y^2 \mid \mathbf{x}) - [E(y \mid \mathbf{x})]^2$$

The last representation is often useful for computing Varðy j xÞ. As with the conditional expectation, s<sup>2</sup>ðxÞ is a random variable when x is viewed as a random vector.

PROPERTY CV.1: 
$$\operatorname{Var}[a(\mathbf{x})y + b(\mathbf{x}) \mid \mathbf{x}] = [a(\mathbf{x})]^2 \operatorname{Var}(y \mid \mathbf{x}).$$

PROPERTY CV.2: 
$$\operatorname{Var}(y) = \operatorname{E}[\operatorname{Var}(y \mid \mathbf{x})] + \operatorname{Var}[\operatorname{E}(y \mid \mathbf{x})] = \operatorname{E}[\sigma^2(\mathbf{x})] + \operatorname{Var}[\mu(\mathbf{x})].$$

Proof:

$$Var(y) = E[(y - E(y))^{2}] = E[(y - E(y | \mathbf{x}) + E(y | \mathbf{x}) + E(y))^{2}]$$

$$= E[(y - E(y | \mathbf{x}))^{2}] + E[(E(y | \mathbf{x}) - E(y))^{2}]$$

$$+ 2E[(y - E(y | \mathbf{x}))(E(y | \mathbf{x}) - E(y))]$$

By CE.6, 
$$E[(y - E(y | \mathbf{x}))(E(y | \mathbf{x}) - E(y))] = 0$$
; so

$$Var(y) = E[(y - E(y | \mathbf{x}))^{2}] + E[(E(y | \mathbf{x}) - E(y))^{2}]$$
  
=  $E\{E[(y - E(y | \mathbf{x}))^{2} | \mathbf{x}]\} + E[(E(y | \mathbf{x}) - E[E(y | \mathbf{x})]$ 

by the law of iterated expectations

$$\equiv E[Var(y | \mathbf{x})] + Var[E(y | \mathbf{x})]$$

An extension of Property CV.2 is often useful, and its proof is similar:

PROPERTY CV.3: 
$$Var(y | \mathbf{x}) = E[Var(y | \mathbf{x}, \mathbf{z}) | \mathbf{x}] + Var[E(y | \mathbf{x}, \mathbf{z}) | \mathbf{x}].$$

Consequently, by the law of iterated expectations CE.2,

PROPERTY CV.4: 
$$E[Var(y | \mathbf{x})] \ge E[Var(y | \mathbf{x}, \mathbf{z})].$$

For any function mðÞ define the mean squared error as MSEðy; mÞ 1 E½ðy mðxÞÞ<sup>2</sup> . Then CV.4 can be loosely stated as MSE½y; Eðy j xÞ bMSE½y; Eðy j x; zÞ-. In other words, in the population one never does worse for predicting y when additional variables are conditioned on. In particular, if Varðy j xÞ and Varðy j x; zÞ are both constant, then Varðy j xÞ bVarðy j x; zÞ.

Þ2

{49}------------------------------------------------

### 2.A.3 Properties of Linear Projections

In what follows, y is a scalar,  $\mathbf{x}$  is a  $1 \times K$  vector, and  $\mathbf{z}$  is a  $1 \times J$  vector. We allow the first element of  $\mathbf{x}$  to be unity, although the following properties hold in either case. All of the variables are assumed to have finite second moments, and the appropriate variance matrices are assumed to be nonsingular.

PROPERTY LP.1: If  $E(y | \mathbf{x}) = \mathbf{x}\boldsymbol{\beta}$ , then  $L(y | \mathbf{x}) = \mathbf{x}\boldsymbol{\beta}$ . More generally, if

$$E(y \mid \mathbf{x}) = \beta_1 g_1(\mathbf{x}) + \beta_2 g_2(\mathbf{x}) + \dots + \beta_M g_M(\mathbf{x})$$

then

$$L(y | w_1, ..., w_M) = \beta_1 w_1 + \beta_2 w_2 + \cdots + \beta_M w_M$$

where  $w_j \equiv g_j(\mathbf{x}), \ j=1,2,\ldots,M$ . This property tells us that, if  $\mathrm{E}(y \mid \mathbf{x})$  is known to be linear in some functions  $g_j(\mathbf{x})$ , then this linear function also represents a linear projection.

PROPERTY LP.2: Define 
$$u \equiv y - L(y \mid \mathbf{x}) = y - \mathbf{x}\boldsymbol{\beta}$$
. Then  $E(\mathbf{x}'u) = \mathbf{0}$ .

PROPERTY LP.3: Suppose  $y_j$ ,  $j=1,2,\ldots,G$  are each random scalars, and  $a_1,\ldots,a_G$  are constants. Then

$$L\left(\sum_{j=1}^{G} a_j y_j \mid \mathbf{x}\right) = \sum_{j=1}^{G} a_j L(y_j \mid \mathbf{x})$$

Thus, the linear projection is a linear operator.

PROPERTY LP.4 (Law of Iterated Projections):  $L(y | \mathbf{x}) = L[L(y | \mathbf{x}, \mathbf{z}) | \mathbf{x}]$ . More precisely, let

$$L(y | \mathbf{x}, \mathbf{z}) \equiv \mathbf{x}\boldsymbol{\beta} + \mathbf{z}\boldsymbol{\gamma}$$
 and  $L(y | \mathbf{x}) = \mathbf{x}\boldsymbol{\delta}$ 

For each element of  $\mathbf{z}$ , write  $L(z_j | \mathbf{x}) = \mathbf{x}\boldsymbol{\pi}_j$ , j = 1, ..., J, where  $\boldsymbol{\pi}_j$  is  $K \times 1$ . Then  $L(\mathbf{z} | \mathbf{x}) = \mathbf{x}\boldsymbol{\Pi}$  where  $\boldsymbol{\Pi}$  is the  $K \times J$  matrix  $\boldsymbol{\Pi} \equiv (\boldsymbol{\pi}_1, \boldsymbol{\pi}_2, ..., \boldsymbol{\pi}_J)$ . Property LP.4 implies that

$$L(y \mid \mathbf{x}) = L(\mathbf{x}\boldsymbol{\beta} + \mathbf{z}\boldsymbol{\gamma} \mid \mathbf{x}) = L(\mathbf{x} \mid \mathbf{x})\boldsymbol{\beta} + L(\mathbf{z} \mid \mathbf{x})\boldsymbol{\gamma} \qquad \text{(by LP.3)}$$
$$= \mathbf{x}\boldsymbol{\beta} + (\mathbf{x}\boldsymbol{\Pi})\boldsymbol{\gamma} = \mathbf{x}(\boldsymbol{\beta} + \boldsymbol{\Pi}\boldsymbol{\gamma}) \qquad (2.50)$$

Thus, we have shown that  $\delta = \beta + \Pi \gamma$ . This is, in fact, the population analogue of the omitted variables bias formula from standard regression theory, something we will use in Chapter 4.

{50}------------------------------------------------

Another iteration property involves the linear projection and the conditional expectation:

PROPERTY LP.5: 
$$L(y | \mathbf{x}) = L[E(y | \mathbf{x}, \mathbf{z}) | \mathbf{x}].$$

Proof: Write y ¼ mðx; zÞ þ u, where mðx; zÞ ¼ Eðy j x; zÞ. But Eðu j x; zÞ ¼ 0; so Eðx<sup>0</sup> uÞ ¼ 0, which implies by LP.3 that Lðy j xÞ ¼ L½mðx; zÞ j x þ Lðu j xÞ ¼ L½mðx; zÞ j x- ¼ L½Eðy j x; zÞ j x-.

A useful special case of Property LP.5 occurs when z is empty. Then Lðy j xÞ ¼ L½Eðy j xÞ j x-.

property LP.6: *b* is a solution to

$$\min_{\mathbf{b} \in \mathbb{R}^K} E[(y - \mathbf{x}\mathbf{b})^2] \tag{2.51}$$

If Eðx<sup>0</sup> xÞ is positive definite, then *b* is the unique solution to this problem.

Proof: For any b, write y xb ¼ ðy x*b*Þþðx*b* xbÞ. Then

$$(y - \mathbf{x}\mathbf{b})^2 = (y - \mathbf{x}\boldsymbol{\beta})^2 + (\mathbf{x}\boldsymbol{\beta} - \mathbf{x}\mathbf{b})^2 + 2(\mathbf{x}\boldsymbol{\beta} - \mathbf{x}\mathbf{b})(y - \mathbf{x}\boldsymbol{\beta})$$
$$= (y - \mathbf{x}\boldsymbol{\beta})^2 + (\boldsymbol{\beta} - \mathbf{b})'\mathbf{x}'\mathbf{x}(\boldsymbol{\beta} - \mathbf{b}) + 2(\boldsymbol{\beta} - \mathbf{b})'\mathbf{x}'(y - \mathbf{x}\boldsymbol{\beta})$$

Therefore,

$$E[(y - \mathbf{x}\mathbf{b})^{2}] = E[(y - \mathbf{x}\boldsymbol{\beta})^{2}] + (\boldsymbol{\beta} - \mathbf{b})' E(\mathbf{x}'\mathbf{x})(\boldsymbol{\beta} - \mathbf{b})$$

$$+ 2(\boldsymbol{\beta} - \mathbf{b})' E[\mathbf{x}'(y - \mathbf{x}\boldsymbol{\beta})]$$

$$= E[(y - \mathbf{x}\boldsymbol{\beta})^{2}] + (\boldsymbol{\beta} - \mathbf{b})' E(\mathbf{x}'\mathbf{x})(\boldsymbol{\beta} - \mathbf{b})$$
(2.52)

because E½x<sup>0</sup> ðy x*b*Þ- ¼ 0 by LP.2. When b ¼ *b*, the right-hand side of equation (2.52) is minimized. Further, if Eðx<sup>0</sup> xÞ is positive definite, ð*b* bÞ 0 Eðx<sup>0</sup> xÞð*b* bÞ > 0 if b 0*b*; so in this case *b* is the unique minimizer.

Property LP.6 states that the linear projection is the minimum mean square linear predictor. It is not necessarily the minimum mean square predictor: if Eðy j xÞ ¼ mðxÞ is not linear in x, then

$$E[(y - \mu(\mathbf{x}))^2] < E[(y - \mathbf{x}\boldsymbol{\beta})^2]$$
(2.53)

property LP.7: This is a partitioned projection formula, which is useful in a variety of circumstances. Write

$$L(y \mid \mathbf{x}, \mathbf{z}) = \mathbf{x}\boldsymbol{\beta} + \mathbf{z}\boldsymbol{\gamma} \tag{2.54}$$