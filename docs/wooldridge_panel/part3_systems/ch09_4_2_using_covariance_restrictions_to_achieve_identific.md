# Using Covariance Restrictions to Achieve Identification

> Pages: 240-242

In most applications of linear SEMs, identification is obtained by putting restrictions on the matrix of structural parameters B. Occasionally, we are willing to put restrictions on the variance matrix S of the structural errors. Such restrictions, which are almost always zero covariance assumptions, can help identify the structural parameters in some equations. For general treatments see Hausman (1983) and Hausman, Newey, and Taylor (1987). We give a couple of examples to show how identification with covariance restrictions works.

The first example is the two-equation system

$$y_1 = \gamma_{12}y_2 + \delta_{11}z_1 + \delta_{13}z_3 + u_1 \tag{9.35}$$

$$y_2 = y_{21}y_1 + \delta_{21}z_1 + \delta_{22}z_2 + \delta_{23}z_3 + u_2 \tag{9.36}$$

Equation (9.35) is just identified if d<sup>22</sup> 00, which we assume, while equation (9.36) is unidentified without more information. Suppose that we have one piece of additional information in terms of a covariance restriction:

$$Cov(u_1, u_2) = E(u_1 u_2) = 0 (9.37)$$

In other words, if S is the 2 2 structural variance matrix, we are assuming that S is diagonal. Assumption (9.37), along with d<sup>22</sup> 0 0, is enough to identify equation (9.36).

Here is a simple way to see how assumption (9.37) identifies equation (9.36). First, because g12, d11, and d<sup>13</sup> are identified, we can treat them as known when studying identification of equation (9.36). But if the parameters in equation (9.35) are known, u<sup>1</sup> is effectively known. By assumption (9.37), u<sup>1</sup> is uncorrelated with u2, and u<sup>1</sup> is certainly partially correlated with y1. Thus, we effectively have ðz1; z2; z3; u1Þ as instruments available for estimating equation (9.36), and this result shows that equation (9.36) is identified.

We can use this method for verifying identification to obtain consistent estimators. First, estimate equation (9.35) by 2SLS using instruments ðz1; z2; z3Þ and save the 2SLS residuals, u^1. Then estimate equation (9.36) by 2SLS using instruments ðz1; z2; z3; u^1Þ. The fact that u^<sup>1</sup> depends on estimates from a prior stage does not affect consistency. But inference is complicated because of the estimation of u1: condition (6.8) does not hold because u<sup>1</sup> depends on y2, which is correlated with u2.

The most efficient way to use covariance restrictions is to write the entire set of orthogonality conditions as E½z<sup>0</sup> u1ð*b*1Þ ¼ 0, E½z<sup>0</sup> u2ð*b*2Þ ¼ 0, and

$$E[u_1(\beta_1)u_2(\beta_2)] = 0 (9.38)$$


{241}------------------------------------------------

where the notation  $u_1(\beta_1)$  emphasizes that the errors are functions of the structural parameters  $\beta_1$ —with normalization and exclusion restrictions imposed—and similarly for  $u_2(\beta_2)$ . For example, from equation (9.35),  $u_1(\beta_1) = y_1 - y_{12}y_2 - \delta_{11}z_1 - \delta_{13}z_3$ . Equation (9.38), because it is nonlinear in  $\beta_1$  and  $\beta_2$ , takes us outside the realm of linear moment restrictions. In Chapter 14 we will use nonlinear moment conditions in GMM estimation.

A general example with covariance restrictions is a **fully recursive system**. First, a **recursive system** can be written as

$$y_{1} = \mathbf{z}\delta_{1} + u_{1}$$

$$y_{2} = \gamma_{21}y_{1} + \mathbf{z}\delta_{2} + u_{2}$$

$$y_{3} = \gamma_{31}y_{1} + \gamma_{32}y_{2} + \mathbf{z}\delta_{3} + u_{3}$$

$$\vdots$$

$$y_{G} = \gamma_{G1}y_{1} + \dots + \gamma_{G,G-1}y_{G-1} + \mathbf{z}\delta_{G} + u_{G}$$

$$(9.39)$$

so that in each equation only endogenous variables from previous equations appear on the right-hand side. We have allowed all exogenous variables to appear in each equation, and we maintain assumption (9.2).

The first equation in the system (9.39) is clearly identified and can be estimated by OLS. Without further exclusion restrictions none of the remaining equations is identified, but each is identified if we assume that the structural errors are pairwise uncorrelated:

$$Cov(u_g, u_h) = 0, \qquad g \neq h \tag{9.40}$$

This assumption means that  $\Sigma$  is a  $G \times G$  diagonal matrix. Equations (9.39) and (9.40) define a fully recursive system. Under these assumptions, the right-hand-side variables in equation g are each uncorrelated with  $u_g$ ; this fact is easily seen by starting with the first equation and noting that  $y_1$  is a linear function of  $\mathbf{z}$  and  $u_1$ . Then, in the second equation,  $y_1$  is uncorrelated with  $u_2$  under assumption (9.40). But  $y_2$  is a linear function of  $\mathbf{z}$ ,  $u_1$ , and  $u_2$ , and so  $y_2$  and  $y_1$  are both uncorrelated with  $u_3$  in the third equation. And so on. It follows that each equation in the system is consistently estimated by ordinary least squares.

It turns out that OLS equation by equation is not necessarily the most efficient estimator in fully recursive systems, even though  $\Sigma$  is a diagonal matrix. Generally, efficiency can be improved by adding the zero covariance restrictions to the orthogonality conditions, as in equation (9.38), and applying nonlinear GMM estimation. See Lahiri and Schmidt (1978) and Hausman, Newey, and Taylor (1987).

{242}------------------------------------------------