# Linear Projections

> Pages: 41-44

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