# Systems with Cross Equation Restrictions

> Pages: 180-182

So far we have studied SUR under the assumption that the *b*<sup>g</sup> are unrelated across equations. When systems of equations are used in economics, especially for modeling consumer and producer theory, there are often cross equation restrictions on the parameters. Such models can still be written in the general form we have covered, and so they can be estimated by system OLS and FGLS. We still refer to such systems as SUR systems, even though the equations are now obviously related, and system OLS is no longer OLS equation by equation.

Example 7.4 (SUR with Cross Equation Restrictions): Consider the two-equation population model

$$y_1 = \gamma_{10} + \gamma_{11}x_{11} + \gamma_{12}x_{12} + \alpha_1x_{13} + \alpha_2x_{14} + u_1 \tag{7.54}$$

$$y_2 = \gamma_{20} + \gamma_{21}x_{21} + \alpha_1x_{22} + \alpha_2x_{23} + \gamma_{24}x_{24} + u_2 \tag{7.55}$$

where we have imposed cross equation restrictions on the parameters in the two equations because a<sup>1</sup> and a<sup>2</sup> show up in each equation. We can put this model into the form of equation (7.9) by appropriately defining X<sup>i</sup> and *b*. For example, define *b* ¼ ðg10; g11; g12; a1; a2; g20; g21; g24Þ 0 , which we know must be an 8 1 vector because there are 8 parameters in this system. The order in which these elements appear in *b* is up to us, but once *b* is defined, X<sup>i</sup> must be chosen accordingly. For each observation i, define the 2 8 matrix

$$\mathbf{X}_{i} = \begin{pmatrix} 1 & x_{i11} & x_{i12} & x_{i13} & x_{i14} & 0 & 0 & 0 \\ 0 & 0 & 0 & x_{i22} & x_{i23} & 1 & x_{i21} & x_{i24} \end{pmatrix}$$

Multiplying X<sup>i</sup> by *b* gives the equations (7.54) and (7.55).

In applications such as the previous example, it is fairly straightforward to test the cross equation restrictions, especially using the sum of squared residuals statistics [equation (7.52) or (7.53)]. The unrestricted model simply allows each explanatory variable in each equation to have its own coefficient. We would use the unrestricted estimates to obtain W^ , and then obtain the restricted estimates using W^ .

# 7.7.3 Singular Variance Matrices in SUR Systems

In our treatment so far we have assumed that the variance matrix W of u<sup>i</sup> is nonsingular. In consumer and producer theory applications this assumption is not always true in the original structural equations, because of additivity constraints.

Example 7.5 (Cost Share Equations): Suppose that, for a given year, each firm in a particular industry uses three inputs, capital (K ), labor (L), and materials (M ).


{181}------------------------------------------------

Because of regional variation and differential tax concessions, firms across the United States face possibly different prices for these inputs: let  $p_{iK}$  denote the price of capital to firm i,  $p_{iL}$  be the price of labor for firm i, and  $s_{iM}$  denote the price of materials for firm i. For each firm i, let  $s_{iK}$  be the cost share for capital, let  $s_{iL}$  be the cost share for labor, and let  $s_{iM}$  be the cost share for materials. By definition,  $s_{iK} + s_{iL} + s_{iM} = 1$ .

One popular set of cost share equations is

$$s_{iK} = \gamma_{10} + \gamma_{11} \log(p_{iK}) + \gamma_{12} \log(p_{iL}) + \gamma_{13} \log(p_{iM}) + u_{iK}$$

$$(7.56)$$

$$s_{iL} = \gamma_{20} + \gamma_{12} \log(p_{iK}) + \gamma_{22} \log(p_{iL}) + \gamma_{23} \log(p_{iM}) + u_{iL}$$

$$(7.57)$$

$$s_{iM} = \gamma_{30} + \gamma_{13} \log(p_{iK}) + \gamma_{23} \log(p_{iL}) + \gamma_{33} \log(p_{iM}) + u_{iM}$$
(7.58)

where the symmetry restrictions from production theory have been imposed. The errors  $u_{ig}$  can be viewed as unobservables affecting production that the economist cannot observe. For an SUR analysis we would assume that

$$\mathbf{E}(\mathbf{u}_i \mid \mathbf{p}_i) = \mathbf{0} \tag{7.59}$$

where  $\mathbf{u}_i \equiv (u_{iK}, u_{iL}, u_{iM})'$  and  $\mathbf{p}_i \equiv (p_{iK}, p_{iL}, p_{iM})$ . Because the cost shares must sum to unity for each i,  $\gamma_{10} + \gamma_{20} + \gamma_{30} = 1$ ,  $\gamma_{11} + \gamma_{12} + \gamma_{13} = 0$ ,  $\gamma_{12} + \gamma_{22} + \gamma_{23} = 0$ ,  $\gamma_{13} + \gamma_{23} + \gamma_{33} = 0$ , and  $u_{iK} + u_{iL} + u_{iM} = 0$ . This last restriction implies that  $\Omega \equiv \text{Var}(\mathbf{u}_i)$  has rank two. Therefore, we can drop one of the equations—say, the equation for materials—and analyze the equations for labor and capital. We can express the restrictions on the gammas in these first two equations as

$$\gamma_{13} = -\gamma_{11} - \gamma_{12} \tag{7.60}$$

$$\gamma_{23} = -\gamma_{12} - \gamma_{22} \tag{7.61}$$

Using the fact that  $\log(a/b) = \log(a) - \log(b)$ , we can plug equations (7.60) and (7.61) into equations (7.56) and (7.57) to get

$$s_{iK} = \gamma_{10} + \gamma_{11} \log(p_{iK}/p_{iM}) + \gamma_{12} \log(p_{iL}/p_{iM}) + u_{iK}$$

$$s_{iL} = \gamma_{20} + \gamma_{12} \log(p_{iK}/p_{iM}) + \gamma_{22} \log(p_{iL}/p_{iM}) + u_{iL}$$

We now have a two-equation system with variance matrix of full rank, with unknown parameters  $\gamma_{10}$ ,  $\gamma_{20}$ ,  $\gamma_{11}$ ,  $\gamma_{12}$ , and  $\gamma_{22}$ . To write this in the form (7.9), redefine  $\mathbf{u}_i = (u_{iK}, u_{iL})'$  and  $\mathbf{y}_i \equiv (s_{iK}, s_{iL})'$ . Take  $\boldsymbol{\beta} \equiv (\gamma_{10}, \gamma_{11}, \gamma_{12}, \gamma_{20}, \gamma_{22})'$  and then  $\mathbf{X}_i$  must be

$$\mathbf{X}_{i} \equiv \begin{pmatrix} 1 & \log(p_{iK}/p_{iM}) & \log(p_{iL}/p_{iM}) & 0 & 0\\ 0 & 0 & \log(p_{iK}/p_{iM}) & 1 & \log(p_{iL}/p_{iM}) \end{pmatrix}$$
(7.62)

This formulation imposes all the conditions implied by production theory.

{182}------------------------------------------------

This model could be extended in several ways. The simplest would be to allow the intercepts to depend on firm characteristics. For each firm i, let  $\mathbf{z}_i$  be a  $1 \times J$  vector of observable firm characteristics, where  $\mathbf{z}_{i1} \equiv 1$ . Then we can extend the model to

$$s_{iK} = \mathbf{z}_{i}\delta_{1} + \gamma_{11}\log(p_{iK}/p_{iM}) + \gamma_{12}\log(p_{iL}/p_{iM}) + u_{iK}$$
(7.63)

$$s_{iL} = \mathbf{z}_{i}\delta_{2} + \gamma_{12}\log(p_{iK}/p_{iM}) + \gamma_{22}\log(p_{iL}/p_{iM}) + u_{iL}$$
(7.64)

where

$$E(u_{ig} | \mathbf{z}_i, p_{iK}, p_{iL}, p_{iM}) = 0, \qquad g = K, L$$
(7.65)

Because we have already reduced the system to two equations, theory implies no restrictions on  $\delta_1$  and  $\delta_2$ . As an exercise, you should write this system in the form (7.9). For example, if  $\beta \equiv (\delta'_1, \gamma_{11}, \gamma_{12}, \delta'_2, \gamma_{22})'$  is  $(2J+3) \times 1$ , how should  $\mathbf{X}_i$  be defined?

Under condition (7.65), system OLS and FGLS estimators are both consistent. (In this setup system OLS is *not* OLS equation by equation because  $\gamma_{12}$  shows up in both equations). FGLS is asymptotically efficient if  $Var(\mathbf{u}_i | \mathbf{z}_i, \mathbf{p}_i)$  is constant. If  $Var(\mathbf{u}_i | \mathbf{z}_i, \mathbf{p}_i)$  depends on  $(\mathbf{z}_i, \mathbf{p}_i)$ —see Brown and Walker (1995) for a discussion of why we should expect it to—then we should at least use the robust variance matrix estimator for FGLS.

We can easily test the symmetry assumption imposed in equations (7.63) and (7.64). One approach is to first estimate the system without *any* restrictions on the parameters, in which case FGLS reduces to OLS estimation of each equation. Then, compute the t statistic of the difference in the estimates on  $\log(p_{iL}/p_{iM})$  in equation (7.63) and  $\log(p_{iK}/p_{iM})$  in equation (7.64). Or, the F statistic from equation (7.53) can be used;  $\hat{\Omega}$  would be obtained from the unrestricted OLS estimation of each equation.

System OLS has no robustness advantages over FGLS in this setup because we cannot relax assumption (7.65) in any useful way.