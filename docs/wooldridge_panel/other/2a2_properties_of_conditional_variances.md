# 2.A.2 Properties of Conditional Variances

> Pages: 48-49

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