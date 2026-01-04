

{31}------------------------------------------------

conditional expectations operator. The appendix to this chapter contains a more extensive list of properties.

# 2.2 Features of Conditional Expectations

### 2.2.1 Definition and Examples

Let y be a random variable, which we refer to in this section as the explained variable, and let x 1ðx1; x2; ... ; xK Þ be a 1 K random vector of explanatory variables. If EðjyjÞ < y, then there is a function, say m: R<sup>K</sup> ! R, such that

$$E(y | x_1, x_2, \dots, x_K) = \mu(x_1, x_2, \dots, x_K)$$
(2.1)

or Eðy j xÞ ¼ mðxÞ. The function mðxÞ determines how the average value of y changes as elements of x change. For example, if y is wage and x contains various individual characteristics, such as education, experience, and IQ, then Eðwage j educ; exper;IQÞ is the average value of wage for the given values of educ, exper, and IQ. Technically, we should distinguish Eðy j xÞ—which is a random variable because x is a random vector defined in the population—from the conditional expectation when x takes on a particular value, such as x0: Eðy j x ¼ x0Þ. Making this distinction soon becomes cumbersome and, in most cases, is not overly important; for the most part we avoid it. When discussing probabilistic features of Eðy j xÞ, x is necessarily viewed as a random variable.

Because Eðy j xÞ is an expectation, it can be obtained from the conditional density of y given x by integration, summation, or a combination of the two (depending on the nature of y). It follows that the conditional expectation operator has the same linearity properties as the unconditional expectation operator, and several additional properties that are consequences of the randomness of mðxÞ. Some of the statements we make are proven in the appendix, but general proofs of other assertions require measure-theoretic probabability. You are referred to Billingsley (1979) for a detailed treatment.

Most often in econometrics a model for a conditional expectation is specified to depend on a finite set of parameters, which gives a parametric model of Eðy j xÞ. This considerably narrows the list of possible candidates for mðxÞ.

Example 2.1: For K ¼ 2 explanatory variables, consider the following examples of conditional expectations:

$$E(y \mid x_1, x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 \tag{2.2}$$

{32}------------------------------------------------

$$E(y \mid x_1, x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_2^2$$
(2.3)

$$E(y | x_1, x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1 x_2$$
(2.4)

$$E(y \mid x_1, x_2) = \exp[\beta_0 + \beta_1 \log(x_1) + \beta_2 x_2], \qquad y \ge 0, \ x_1 > 0$$
(2.5)

The model in equation (2.2) is linear in the explanatory variables x<sup>1</sup> and x2. Equation (2.3) is an example of a conditional expectation nonlinear in x2, although it is linear in x1. As we will review shortly, from a statistical perspective, equations (2.2) and (2.3) can be treated in the same framework because they are linear in the parameters bj. The fact that equation (2.3) is nonlinear in x has important implications for interpreting the bj, but not for estimating them. Equation (2.4) falls into this same class: it is nonlinear in x ¼ ðx1; x2Þ but linear in the bj.

Equation (2.5) differs fundamentally from the first three examples in that it is a nonlinear function of the parameters bj, as well as of the xj. Nonlinearity in the parameters has implications for estimating the bj; we will see how to estimate such models when we cover nonlinear methods in Part III. For now, you should note that equation (2.5) is reasonable only if y b0.

# 2.2.2 Partial Effects, Elasticities, and Semielasticities

If y and x are related in a deterministic fashion, say y ¼ fðxÞ, then we are often interested in how y changes when elements of x change. In a stochastic setting we cannot assume that y ¼ fðxÞ for some known function and observable vector x because there are always unobserved factors affecting y. Nevertheless, we can define the partial effects of the xj on the conditional expectation Eðy j xÞ. Assuming that mðÞ is appropriately differentiable and xj is a continuous variable, the partial derivative qmðxÞ=qxj allows us to approximate the marginal change in Eðy j xÞ when xj is increased by a small amount, holding x1; ... ; xj<sup>1</sup>; xjþ<sup>1</sup>; ... xK constant:

$$\Delta E(y \mid \mathbf{x}) \approx \frac{\partial \mu(\mathbf{x})}{\partial x_j} \cdot \Delta x_j, \text{ holding } x_1, \dots, x_{j-1}, x_{j+1}, \dots x_K \text{ fixed}$$
 (2.6)

The partial derivative of Eðy j xÞ with respect to xj is usually called the partial effect of xj on Eðy j xÞ (or, to be somewhat imprecise, the partial effect of xj on y). Interpreting the magnitudes of coefficients in parametric models usually comes from the approximation in equation (2.6).

If xj is a discrete variable (such as a binary variable), partial effects are computed by comparing Eðy j xÞ at different settings of xj (for example, zero and one when xj is binary), holding other variables fixed.

{33}------------------------------------------------

Example 2.1 (continued): In equation (2.2) we have

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_1} = \beta_1, \qquad \frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_2} = \beta_2$$

As expected, the partial effects in this model are constant. In equation (2.3),

$$\frac{\partial \mathrm{E}(y \mid \mathbf{x})}{\partial x_1} = \beta_1, \qquad \frac{\partial \mathrm{E}(y \mid \mathbf{x})}{\partial x_2} = \beta_2 + 2\beta_3 x_2$$

so that the partial effect of  $x_1$  is constant but the partial effect of  $x_2$  depends on the level of  $x_2$ . In equation (2.4),

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_1} = \beta_1 + \beta_3 x_2, \qquad \frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_2} = \beta_2 + \beta_3 x_1$$

so that the partial effect of  $x_1$  depends on  $x_2$ , and vice versa. In equation (2.5),

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_1} = \exp(\cdot)(\beta_1/x_1), \qquad \frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_2} = \exp(\cdot)\beta_2 \tag{2.7}$$

where  $\exp(\cdot)$  denotes the function  $E(y | \mathbf{x})$  in equation (2.5). In this case, the partial effects of  $x_1$  and  $x_2$  both depend on  $\mathbf{x} = (x_1, x_2)$ .

Sometimes we are interested in a particular function of a partial effect, such as an elasticity. In the determinstic case  $y = f(\mathbf{x})$ , we define the elasticity of y with respect to  $x_j$  as

$$\frac{\partial y}{\partial x_i} \cdot \frac{x_j}{y} = \frac{\partial f(\mathbf{x})}{\partial x_i} \cdot \frac{x_j}{f(\mathbf{x})} \tag{2.8}$$

again assuming that  $x_j$  is continuous. The right-hand side of equation (2.8) shows that the elasticity is a function of  $\mathbf{x}$ . When y and  $\mathbf{x}$  are random, it makes sense to use the right-hand side of equation (2.8), but where  $f(\mathbf{x})$  is the conditional mean,  $\mu(\mathbf{x})$ . Therefore, the (partial) **elasticity** of  $E(y | \mathbf{x})$  with respect to  $x_j$ , holding  $x_1, \ldots, x_{j-1}, x_{j+1}, \ldots, x_K$  constant, is

$$\frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_j} \cdot \frac{x_j}{\mathbf{E}(y \mid \mathbf{x})} = \frac{\partial \mu(\mathbf{x})}{\partial x_j} \cdot \frac{x_j}{\mu(\mathbf{x})}.$$
 (2.9)

If  $E(y | \mathbf{x}) > 0$  and  $x_j > 0$  (as is often the case), equation (2.9) is the same as

$$\frac{\partial \log[\mathbf{E}(y \mid \mathbf{x})]}{\partial \log(x_j)} \tag{2.10}$$

{34}------------------------------------------------

This latter expression gives the elasticity its interpretation as the approximate percentage change in  $E(y | \mathbf{x})$  when  $x_i$  increases by 1 percent.

Example 2.1 (continued): In equations (2.2) to (2.5), most elasticities are not constant. For example, in equation (2.2), the elasticity of  $E(y | \mathbf{x})$  with respect to  $x_1$  is  $(\beta_1 x_1)/(\beta_0 + \beta_1 x_1 + \beta_2 x_2)$ , which clearly depends on  $x_1$  and  $x_2$ . However, in equation (2.5) the elasticity with respect to  $x_1$  is constant and equal to  $\beta_1$ .

How does equation (2.10) compare with the definition of elasticity from a model linear in the natural logarithms? If y > 0 and  $x_j > 0$ , we could define the elasticity as

$$\frac{\partial \mathrm{E}[\log(y) \mid \mathbf{x}]}{\partial \log(x_i)} \tag{2.11}$$

This is the natural definition in a model such as  $\log(y) = g(\mathbf{x}) + u$ , where  $g(\mathbf{x})$  is some function of  $\mathbf{x}$  and u is an unobserved disturbance with zero mean conditional on  $\mathbf{x}$ . How do equations (2.10) and (2.11) compare? Generally, they are different (since the expected value of the log and the log of the expected value can be very different). If u is independent of  $\mathbf{x}$ , then equations (2.10) and (2.11) are the same, because then

$$E(y | \mathbf{x}) = \delta \cdot \exp[g(\mathbf{x})]$$

where  $\delta \equiv \mathrm{E}[\exp(u)]$ . (If u and x are independent, so are  $\exp(u)$  and  $\exp[g(\mathbf{x})]$ .) As a specific example, if

$$\log(y) = \beta_0 + \beta_1 \log(x_1) + \beta_2 x_2 + u \tag{2.12}$$

where u has zero mean and is independent of  $(x_1, x_2)$ , then the elasticity of y with respect to  $x_1$  is  $\beta_1$  using *either* definition of elasticity. If  $E(u \mid \mathbf{x}) = 0$  but u and  $\mathbf{x}$  are not independent, the definitions are generally different.

For the most part, little is lost by treating equations (2.10) and (2.11) as the same when y > 0. We will view models such as equation (2.12) as constant elasticity models of y with respect to  $x_1$  whenever  $\log(y)$  and  $\log(x_j)$  are well defined. Definition (2.10) is more general because sometimes it applies even when  $\log(y)$  is not defined. (We will need the general definition of an elasticity in Chapters 16 and 19.)

The percentage change in  $E(y | \mathbf{x})$  when  $x_j$  is increased by one *unit* is approximated as

$$100 \cdot \frac{\partial \mathbf{E}(y \mid \mathbf{x})}{\partial x_i} \cdot \frac{1}{\mathbf{E}(y \mid \mathbf{x})}$$
 (2.13)

which equals

{35}------------------------------------------------

$$100 \cdot \frac{\partial \log[E(y \mid \mathbf{x})]}{\partial x_i} \tag{2.14}$$

if  $E(y | \mathbf{x}) > 0$ . This is sometimes called the **semielasticity** of  $E(y | \mathbf{x})$  with respect to  $x_i$ .

Example 2.1 (continued): In equation (2.5) the semielasticity with respect to  $x_2$  is constant and equal to  $100 \cdot \beta_2$ . No other semielasticities are constant in these equations.

#### 2.2.3 The Error Form of Models of Conditional Expectations

When y is a random variable we would like to explain in terms of observable variables  $\mathbf{x}$ , it is useful to decompose y as

$$y = \mathrm{E}(y \mid \mathbf{x}) + u \tag{2.15}$$

$$E(u \mid \mathbf{x}) = 0 \tag{2.16}$$

In other words, equations (2.15) and (2.16) are *definitional*: we can always write y as its conditional expectation,  $E(y | \mathbf{x})$ , plus an **error term** or **disturbance term** that has *conditional* mean zero.

The fact that  $E(u | \mathbf{x}) = 0$  has the following important implications: (1) E(u) = 0; (2) u is uncorrelated with any function of  $x_1, x_2, \ldots, x_K$ , and, in particular, u is uncorrelated with each of  $x_1, x_2, \ldots, x_K$ . That u has zero unconditional expectation follows as a special case of the **law of iterated expectations** (LIE), which we cover more generally in the next subsection. Intuitively, it is quite reasonable that  $E(u | \mathbf{x}) = 0$  implies E(u) = 0. The second implication is less obvious but very important. The fact that u is uncorrelated with any function of  $\mathbf{x}$  is much stronger than merely saying that u is uncorrelated with  $x_1, \ldots, x_K$ .

As an example, if equation (2.2) holds, then we can write

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + u, \qquad E(u \mid x_1, x_2) = 0$$
 (2.17)

and so

$$E(u) = 0, Cov(x_1, u) = 0, Cov(x_2, u) = 0$$
 (2.18)

But we can say much more: under equation (2.17), u is also uncorrelated with any other function we might think of, such as  $x_1^2, x_2^2, x_1x_2, \exp(x_1)$ , and  $\log(x_2^2 + 1)$ . This fact ensures that we have fully accounted for the effects of  $x_1$  and  $x_2$  on the expected value of y; another way of stating this point is that we have the functional form of  $E(y | \mathbf{x})$  properly specified.

{36}------------------------------------------------

If we only assume equation (2.18), then u can be correlated with nonlinear functions of x<sup>1</sup> and x2, such as quadratics, interactions, and so on. If we hope to estimate the partial effect of each xj on Eðy j xÞ over a broad range of values for x, we want Eðu j xÞ ¼ 0. [In Section 2.3 we discuss the weaker assumption (2.18) and its uses.]

Example 2.2: Suppose that housing prices are determined by the simple model

$$hprice = \beta_0 + \beta_1 sqrft + \beta_2 distance + u,$$

where sqrft is the square footage of the house and distance is distance of the house from a city incinerator. For b<sup>2</sup> to represent qEðhprice jsqrft; distanceÞ=q distance, we must assume that Eðu jsqrft; distanceÞ ¼ 0.

# 2.2.4 Some Properties of Conditional Expectations

One of the most useful tools for manipulating conditional expectations is the law of iterated expectations, which we mentioned previously. Here we cover the most general statement needed in this book. Suppose that w is a random vector and y is a random variable. Let x be a random vector that is some function of w, say x ¼ fðwÞ. (The vector x could simply be a subset of w.) This statement implies that if we know the outcome of w, then we know the outcome of x. The most general statement of the LIE that we will need is

$$E(y \mid \mathbf{x}) = E[E(y \mid \mathbf{w}) \mid \mathbf{x}]$$
(2.19)

In other words, if we write m1ðwÞ 1 Eðy j wÞ and m2ðxÞ 1 Eðy j xÞ, we can obtain m2ðxÞ by computing the expected value of m2ðwÞ given x: m1ðxÞ ¼ E½m1ðwÞ j x-.

There is another result that looks similar to equation (2.19) but is much simpler to verify. Namely,

$$E(y \mid \mathbf{x}) = E[E(y \mid \mathbf{x}) \mid \mathbf{w}]$$
 (2.20)

Note how the positions of x and w have been switched on the right-hand side of equation (2.20) compared with equation (2.19). The result in equation (2.20) follows easily from the conditional aspect of the expection: since x is a function of w, knowing w implies knowing x; given that m2ðxÞ ¼ Eðy j xÞ is a function of x, the expected value of m2ðxÞ given w is just m2ðxÞ.

Some find a phrase useful for remembering both equations (2.19) and (2.20): ''The smaller information set always dominates.'' Here, x represents less information than w, since knowing w implies knowing x, but not vice versa. We will use equations (2.19) and (2.20) almost routinely throughout the book.

{37}------------------------------------------------

For many purposes we need the following special case of the general LIE (2.19). If x and z are any random vectors, then

$$E(y \mid \mathbf{x}) = E[E(y \mid \mathbf{x}, \mathbf{z}) \mid \mathbf{x}]$$
(2.21)

or, defining m1ðx; zÞ 1 Eðy j x; zÞ and m2ðxÞ 1Eðy j xÞ,

$$\mu_2(\mathbf{x}) = \mathbf{E}[\mu_1(\mathbf{x}, \mathbf{z}) \,|\, \mathbf{x}] \tag{2.22}$$

For many econometric applications, it is useful to think of m1ðx; zÞ ¼ Eðy j x; zÞ as a structural conditional expectation, but where z is unobserved. If interest lies in Eðy j x; zÞ, then we want the effects of the xj holding the other elements of x and z fixed. If z is not observed, we cannot estimate Eðy j x; zÞ directly. Nevertheless, since y and x are observed, we can generally estimate Eðy j xÞ. The question, then, is whether we can relate Eðy j xÞ to the original expectation of interest. (This is a version of the identification problem in econometrics.) The LIE provides a convenient way for relating the two expectations.

Obtaining E½m1ðx; zÞ j x generally requires integrating (or summing) m1ðx; zÞ against the conditional density of z given x, but in many cases the form of Eðy j x; zÞ is simple enough not to require explicit integration. For example, suppose we begin with the model

$$E(y \mid x_1, x_2, z) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 z$$
(2.23)

but where z is unobserved. By the LIE, and the linearity of the CE operator,

$$E(y | x_1, x_2) = E(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 z | x_1, x_2)$$
  
=  $\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 E(z | x_1, x_2)$  (2.24)

Now, if we make an assumption about Eðz j x1; x2Þ, for example, that it is linear in x<sup>1</sup> and x2,

$$E(z | x_1, x_2) = \delta_0 + \delta_1 x_1 + \delta_2 x_2$$
 (2.25)

then we can plug this into equation (2.24) and rearrange:

$$= \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 (\delta_0 + \delta_1 x_1 + \delta_2 x_2)$$

$$= (\beta_0 + \beta_3 \delta_0) + (\beta_1 + \beta_3 \delta_1) x_1 + (\beta_2 + \beta_3 \delta_2) x_2$$

This last expression is Eðy j x1; x2Þ; given our assumptions it is necessarily linear in ðx1; x2Þ.

{38}------------------------------------------------

Now suppose equation (2.23) contains an interaction in x<sup>1</sup> and z:

$$E(y | x_1, x_2, z) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 z + \beta_4 x_1 z$$
(2.26)

Then, again by the LIE,

$$E(y | x_1, x_2) = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 E(z | x_1, x_2) + \beta_4 x_1 E(z | x_1, x_2)$$

If Eðz j x1; x2Þ is again given in equation (2.25), you can show that Eðy j x1; x2Þ has terms linear in x<sup>1</sup> and x<sup>2</sup> and, in addition, contains x<sup>2</sup> <sup>1</sup> and x1x2. The usefulness of such derivations will become apparent in later chapters.

The general form of the LIE has other useful implications. Suppose that for some (vector) function fðxÞ and a real-valued function gðÞ, Eðy j xÞ ¼ g½fðxÞ-. Then

$$E[y | \mathbf{f}(\mathbf{x})] = E(y | \mathbf{x}) = g[\mathbf{f}(\mathbf{x})]$$
(2.27)

There is another way to state this relationship: If we define z1 fðxÞ, then Eðy j zÞ ¼ gðzÞ. The vector z can have smaller or greater dimension than x. This fact is illustrated with the following example.

Example 2.3: If a wage equation is

$$E(wage \mid educ, exper) = \beta_0 + \beta_1 educ + \beta_2 exper + \beta_3 exper^2 + \beta_4 educ \cdot exper$$
 then

Eðwage j educ; exper; exper<sup>2</sup> ; educexperÞ

$$=\beta_0+\beta_1 educ+\beta_2 exper+\beta_3 exper^2+\beta_4 educ\cdot exper.$$

In other words, once educ and exper have been conditioned on, it is redundant to condition on exper<sup>2</sup> and educexper.

The conclusion in this example is much more general, and it is helpful for analyzing models of conditional expectations that are linear in parameters. Assume that, for some functions g1ðxÞ; g2ðxÞ; ... ; gMðxÞ,

$$E(y \mid \mathbf{x}) = \beta_0 + \beta_1 g_1(\mathbf{x}) + \beta_2 g_2(\mathbf{x}) + \dots + \beta_M g_M(\mathbf{x})$$
(2.28)

This model allows substantial flexibility, as the explanatory variables can appear in all kinds of nonlinear ways; the key restriction is that the model is linear in the bj. If we define z<sup>1</sup> 1g1ðxÞ; ... ; zM 1gMðxÞ, then equation (2.27) implies that

$$E(y | z_1, z_2, \dots, z_M) = \beta_0 + \beta_1 z_1 + \beta_2 z_2 + \dots + \beta_M z_M$$
(2.29)

{39}------------------------------------------------

This equation shows that any conditional expectation linear in parameters can be written as a conditional expectation linear in parameters and linear in some conditioning variables. If we write equation (2.29) in error form as y ¼ b<sup>0</sup> þ b1z<sup>1</sup> þ b2z<sup>2</sup> þþ bMzM þ u, then, because Eðu j xÞ ¼ 0 and the zj are functions of x, it follows that u is uncorrelated with z1; ... ; zM (and any functions of them). As we will see in Chapter 4, this result allows us to cover models of the form (2.28) in the same framework as models linear in the original explanatory variables.

We also need to know how the notion of statistical independence relates to conditional expectations. If u is a random variable independent of the random vector x, then Eðu j xÞ ¼ EðuÞ, so that if EðuÞ ¼ 0 and u and x are independent, then Eðu j xÞ ¼ 0. The converse of this is not true: Eðu j xÞ ¼ EðuÞ does not imply statistical independence between u and x ( just as zero correlation between u and x does not imply independence).

### 2.2.5 Average Partial Effects

When we explicitly allow the expectation of the response variable, y, to depend on unobservables—usually called unobserved heterogeneity—we must be careful in specifying the partial effects of interest. Suppose that we have in mind the (structural) conditional mean Eðy j x; qÞ ¼ m1ðx; qÞ, where x is a vector of observable explanatory variables and q is an unobserved random variable—the unobserved heterogeneity. (We take q to be a scalar for simplicity; the discussion for a vector is essentially the same.) For continuous xj, the partial effect of immediate interest is

$$\theta_j(\mathbf{x}, q) \equiv \partial \mathbf{E}(y \mid \mathbf{x}, q) / \partial x_j = \partial \mu_1(\mathbf{x}, q) / \partial x_j$$
(2.30)

(For discrete xj, we would simply look at differences in the regression function for xj at two different values, when the other elements of x and q are held fixed.) Because yjðx; qÞ generally depends on q, we cannot hope to estimate the partial effects across many different values of q. In fact, even if we could estimate yjðx; qÞ for all x and q, we would generally have little guidance about inserting values of q into the mean function. In many cases we can make a normalization such as EðqÞ ¼ 0, and estimate yjðx; 0Þ, but q ¼ 0 typically corresponds to a very small segment of the population. (Technically, q ¼ 0 corresponds to no one in the population when q is continuously distributed.) Usually of more interest is the partial effect averaged across the population distribution of q; this is called the average partial effect (APE ).

For emphasis, let x<sup>o</sup> denote a fixed value of the covariates. The average partial effect evaluated at x<sup>o</sup> is

$$\delta_j(\mathbf{x}^o) \equiv \mathrm{E}_q[\theta_j(\mathbf{x}^o, q)] \tag{2.31}$$

{40}------------------------------------------------

where Eq½ denotes the expectation with respect to q. In other words, we simply average the partial effect yjðx<sup>o</sup>; qÞ across the population distribution of q. Definition (2.31) holds for any population relationship between q and x; in particular, they need not be independent. But remember, in definition (2.31), x<sup>o</sup> is a nonrandom vector of numbers.

For concreteness, assume that q has a continuous distribution with density function gðÞ, so that

$$\delta_j(\mathbf{x}^o) = \int_{\mathbb{R}} \theta_j(\mathbf{x}^o, \varphi) g(\varphi) \, d\varphi \tag{2.32}$$

where q is simply the dummy argument in the integration. The question we answer here is, Is it possible to estimate djðxoÞ from conditional expectations that depend only on observable conditioning variables? Generally, the answer must be no, as q and x can be arbitrarily related. Nevertheless, if we appropriately restrict the relationship between q and x, we can obtain a very useful equivalance.

One common assumption in nonlinear models with unobserved heterogeneity is that q and x are independent. We will make the weaker assumption that q and x are independent conditional on a vector of observables, w:

$$D(q \mid \mathbf{x}, \mathbf{w}) = D(q \mid \mathbf{w}) \tag{2.33}$$

where Dð j Þ denotes conditional distribution. (If we take w to be empty, we get the special case of independence between q and x.) In many cases, we can interpret equation (2.33) as implying that w is a vector of good proxy variables for q, but equation (2.33) turns out to be fairly widely applicable. We also assume that w is redundant or ignorable in the structural expectation

$$E(y \mid \mathbf{x}, q, \mathbf{w}) = E(y \mid \mathbf{x}, q) \tag{2.34}$$

As we will see in subsequent chapters, many econometric methods hinge on being able to exclude certain variables from the equation of interest, and equation (2.34) makes this assumption precise. Of course, if w is empty, then equation (2.34) is trivially true.

Under equations (2.33) and (2.34), we can show the following important result, provided that we can interchange a certain integral and partial derivative:

$$\delta_j(\mathbf{x}^o) = \mathbf{E}_w[\partial \mathbf{E}(y \mid \mathbf{x}^o, \mathbf{w})/\partial x_j] \tag{2.35}$$

where Ew½ denotes the expectation with respect to the distribution of w. Before we verify equation (2.35) for the special case of continuous, scalar q, we must understand its usefulness. The point is that the unobserved heterogeneity, q, has disappeared entirely, and the conditional expectation Eðy j x; wÞ can be estimated quite generally