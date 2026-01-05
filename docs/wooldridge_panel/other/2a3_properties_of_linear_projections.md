# 2.A.3 Properties of Linear Projections

> Pages: 49-52

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