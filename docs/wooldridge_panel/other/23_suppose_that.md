# 2.3. Suppose that

> Pages: 45-48

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