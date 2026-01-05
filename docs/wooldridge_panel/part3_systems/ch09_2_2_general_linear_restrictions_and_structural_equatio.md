# General Linear Restrictions and Structural Equations

> Pages: 228-237

The identification analysis of the preceding subsection is useful when reduced forms are appended to structural equations. When an entire structural system has been specified, it is best to study identification entirely in terms of the structural parameters.

To this end, we now write the G equations in the population as

$$\mathbf{y}\gamma_1 + \mathbf{z}\boldsymbol{\delta}_1 + u_1 = 0$$

$$\vdots$$

$$\mathbf{y}\gamma_G + \mathbf{z}\boldsymbol{\delta}_G + u_G = 0$$

$$(9.12)$$

where  $\mathbf{y} \equiv (y_1, y_2, \dots, y_G)$  is the  $1 \times G$  vector of *all* endogenous variables and  $\mathbf{z} \equiv (z_1, \dots, z_M)$  is still the  $1 \times M$  vector of all exogenous variables, and probably contains unity. We maintain assumption (9.2) throughout this section and also assume that  $\mathbf{E}(\mathbf{z}'\mathbf{z})$  is nonsingular. The notation here differs from that in Section 9.2.1. Here,  $\gamma_g$  is  $G \times 1$  and  $\delta_g$  is  $M \times 1$  for all  $g = 1, 2, \dots, G$ , so that the system (9.12) is the general linear system without *any* restrictions on the structural parameters.

We can write this system compactly as

$$y\Gamma + z\Delta + u = 0 \tag{9.13}$$

{229}------------------------------------------------

where  $\mathbf{u} \equiv (u_1, \dots, u_G)$  is the  $1 \times G$  vector of structural errors,  $\Gamma$  is the  $G \times G$  matrix with gth column  $\gamma_g$ , and  $\Delta$  is the  $M \times G$  matrix with gth column  $\delta_g$ . So that a reduced form exists, we assume that  $\Gamma$  is nonsingular. Let  $\Sigma \equiv \mathrm{E}(\mathbf{u}'\mathbf{u})$  denote the  $G \times G$  variance matrix of  $\mathbf{u}$ , which we assume to be nonsingular. At this point, we have placed no other restrictions on  $\Gamma$ ,  $\Delta$ , or  $\Sigma$ .

The reduced form is easily expressed as

$$\mathbf{y} = \mathbf{z}(-\Delta \Gamma^{-1}) + \mathbf{u}(-\Gamma^{-1}) \equiv \mathbf{z} \mathbf{\Pi} + \mathbf{v} \tag{9.14}$$

where  $\Pi \equiv (-\Delta \Gamma^{-1})$  and  $\mathbf{v} \equiv \mathbf{u}(-\Gamma^{-1})$ . Define  $\Lambda \equiv E(\mathbf{v}'\mathbf{v}) = \Gamma^{-1}'\Sigma\Gamma^{-1}$  as the reduced form variance matrix. Because  $E(\mathbf{z}'\mathbf{v}) = \mathbf{0}$  and  $E(\mathbf{z}'\mathbf{z})$  is nonsingular,  $\Pi$  and  $\Lambda$  are identified because they can be consistently estimated given a random sample on  $\mathbf{y}$  and  $\mathbf{z}$  by OLS equation by equation. The question is, Under what assumptions can we recover the structural parameters  $\Gamma$ ,  $\Lambda$ , and  $\Sigma$  from the reduced form parameters?

It is easy to see that, without some restrictions, we will not be able to identify any of the parameters in the structural system. Let  $\mathbf{F}$  be any  $G \times G$  nonsingular matrix, and postmultiply equation (9.13) by  $\mathbf{F}$ :

$$\mathbf{y}\mathbf{\Gamma}\mathbf{F} + \mathbf{z}\mathbf{\Delta}\mathbf{F} + \mathbf{u}\mathbf{F} = \mathbf{0}$$
 or  $\mathbf{y}\mathbf{\Gamma}^* + \mathbf{z}\mathbf{\Delta}^* + \mathbf{u}^* = \mathbf{0}$  (9.15)

where  $\Gamma^* \equiv \Gamma F$ ,  $\Delta^* \equiv \Delta F$ , and  $\mathbf{u}^* \equiv \mathbf{u} F$ ; note that  $Var(\mathbf{u}^*) = F' \Sigma F$ . Simple algebra shows that equations (9.15) and (9.13) have *identical* reduced forms. This result means that, without restrictions on the structural parameters, there are many **equivalent structures** in the sense that they lead to the same reduced form. In fact, there is an equivalent structure for each nonsingular  $\mathbf{F}$ .

Let  $\mathbf{B} \equiv \begin{pmatrix} \Gamma \\ \mathbf{\Lambda} \end{pmatrix}$  be the  $(G+M) \times G$  matrix of structural parameters in equation (9.13). If  $\mathbf{F}$  is any nonsingular  $G \times G$  matrix, then  $\mathbf{F}$  represents an admissible linear transformation if

- 1. **BF** satisfies all restrictions on **B**.
- 2.  $\mathbf{F}'\mathbf{\Sigma}\mathbf{F}$  satisfies all restrictions on  $\mathbf{\Sigma}$ .

To identify the system, we need enough prior information on the structural parameters  $(\mathbf{B}, \Sigma)$  so that  $\mathbf{F} = \mathbf{I}_G$  is the only admissible linear transformation.

In most applications identification of **B** is of primary interest, and this identification is achieved by putting restrictions directly on **B**. As we will touch on in Section 9.4.2, it is possible to put restrictions on  $\Sigma$  in order to identify **B**, but this approach is somewhat rare in practice. Until we come to Section 9.4.2,  $\Sigma$  is an unrestricted  $G \times G$  positive definite matrix.

{230}------------------------------------------------

As before, we consider identification of the first equation:

$$\mathbf{y}\boldsymbol{\gamma}_1 + \mathbf{z}\boldsymbol{\delta}_1 + u_1 = 0 \tag{9.16}$$

or  $\gamma_{11}y_1 + \gamma_{12}y_2 + \cdots + \gamma_{1G}y_G + \delta_{11}z_1 + \delta_{12}z_2 + \cdots + \delta_{1M}z_M + u_1 = 0$ . The first restriction we make on the parameters in equation (9.16) is the **normalization restriction** that one element of  $\gamma_1$  is -1. Each equation in the system (9.1) has a normalization restriction because one variable is taken to be the left-hand-side explained variable. In applications, there is usually a natural normalization for each equation. If there is not, we should ask whether the system satisfies the autonomy requirement discussed in Section 9.1. (Even in models that satisfy the autonomy requirement, we often have to choose between reasonable normalization conditions. For example, in Example 9.1, we could have specified the second equation to be a wage offer equation rather than a labor demand equation.)

Let  $\beta_1 \equiv (\gamma_1', \delta_1')'$  be the  $(G+M) \times 1$  vector of structural parameters in the first equation. With a normalization restriction there are (G+M)-1 unknown elements in  $\beta_1$ . Assume that prior knowledge about  $\beta_1$  can be expressed as

$$\mathbf{R}_1 \boldsymbol{\beta}_1 = \mathbf{0} \tag{9.17}$$

where  $\mathbf{R}_1$  is a  $J_1 \times (G+M)$  matrix of known constants, and  $J_1$  is the number of restrictions on  $\boldsymbol{\beta}_1$  (in addition to the normalization restriction). We assume that rank  $\mathbf{R}_1 = J_1$ , so that there are no redundant restrictions. The restrictions in assumption (9.17) are sometimes called **homogeneous linear restrictions**, but, when coupled with a normalization assumption, equation (9.17) actually allows for nonhomogeneous restrictions.

Example 9.2 (A Three-Equation System): Consider the first equation in a system with G = 3 and M = 4:

$$y_1 = \gamma_{12}y_2 + \gamma_{13}y_3 + \delta_{11}z_1 + \delta_{12}z_2 + \delta_{13}z_3 + \delta_{14}z_4 + u_1$$

so that  $\gamma_1 = (-1, \gamma_{12}, \gamma_{13})'$ ,  $\delta_1 = (\delta_{11}, \delta_{12}, \delta_{13}, \delta_{14})'$ , and  $\beta_1 = (-1, \gamma_{12}, \gamma_{13}, \delta_{11}, \delta_{12}, \delta_{13}, \delta_{14})'$ . (We can set  $z_1 = 1$  to allow an intercept.) Suppose the restrictions on the structural parameters are  $\gamma_{12} = 0$  and  $\delta_{13} + \delta_{14} = 3$ . Then  $J_1 = 2$  and

$$\mathbf{R}_1 = \begin{pmatrix} 0 & 1 & 0 & 0 & 0 & 0 & 0 \\ 3 & 0 & 0 & 0 & 0 & 1 & 1 \end{pmatrix}$$

Straightforward multiplication gives  $\mathbf{R}_1 \boldsymbol{\beta}_1 = (\gamma_{12}, \delta_{13} + \delta_{14} - 3)'$ , and setting this vector to zero as in equation (9.17) incorporates the restrictions on  $\boldsymbol{\beta}_1$ .


{231}------------------------------------------------

Given the linear restrictions in equation (9.17), when are these and the normalization restriction enough to identify  $\beta_1$ ? Let **F** again be any  $G \times G$  nonsingular matrix, and write it in terms of its columns as  $\mathbf{F} = (\mathbf{f}_1, \mathbf{f}_2, \dots, \mathbf{f}_G)$ . Define a linear transformation of **B** as  $\mathbf{B}^* = \mathbf{BF}$ , so that the first column of  $\mathbf{B}^*$  is  $\beta_1^* \equiv \mathbf{Bf}_1$ . We need to find a condition so that equation (9.17) allows us to distinguish  $\beta_1$  from any other  $\beta_1^*$ . For the moment, ignore the normalization condition. The vector  $\beta_1^*$  satisfies the linear restrictions embodied by  $\mathbf{R}_1$  if and only if

$$\mathbf{R}_1 \boldsymbol{\beta}_1^* = \mathbf{R}_1 (\mathbf{B} \mathbf{f}_1) = (\mathbf{R}_1 \mathbf{B}) \mathbf{f}_1 = \mathbf{0} \tag{9.18}$$

Naturally,  $(\mathbf{R}_1\mathbf{B})\mathbf{f}_1 = \mathbf{0}$  is true for  $\mathbf{f}_1 = \mathbf{e}_1 \equiv (1, 0, 0, \dots, 0)'$ , since then  $\boldsymbol{\beta}_1^* = \mathbf{B}\mathbf{f}_1 = \boldsymbol{\beta}_1$ . Since assumption (9.18) holds for  $\mathbf{f}_1 = \mathbf{e}_1$  it clearly holds for any scalar multiple of  $\mathbf{e}_1$ . The key to identification is that vectors of the form  $c_1\mathbf{e}_1$ , for some constant  $c_1$ , are the *only* vectors  $\mathbf{f}_1$  satisfying condition (9.18). If condition (9.18) holds for vectors  $\mathbf{f}_1$  other than scalar multiples of  $\mathbf{e}_1$  then we have no hope of identifying  $\boldsymbol{\beta}_1$ .

Stating that condition (9.18) holds only for vectors of the form  $c_1\mathbf{e}_1$  just means that the null space of  $\mathbf{R}_1\mathbf{B}$  has dimension unity. Equivalently, because  $\mathbf{R}_1\mathbf{B}$  has G columns,

$$\operatorname{rank} \mathbf{R}_1 \mathbf{B} = G - 1 \tag{9.19}$$

This is the **rank condition** for identification of  $\beta_1$  in the first structural equation under general linear restrictions. Once condition (9.19) is known to hold, the normalization restriction allows us to distinguish  $\beta_1$  from any other scalar multiple of  $\beta_1$ .

THEOREM 9.2 (Rank Condition for Identification): Let  $\beta_1$  be the  $(G+M) \times 1$  vector of structural parameters in the first equation, with the normalization restriction that one of the coefficients on an endogenous variable is -1. Let the additional information on  $\beta_1$  be given by restriction (9.17). Then  $\beta_1$  is identified if and only if the rank condition (9.19) holds.

As promised earlier, the rank condition in this subsection depends on the *structural* parameters, **B**. We can determine whether the first equation is identified by studying the matrix  $\mathbf{R}_1\mathbf{B}$ . Since this matrix can depend on *all* structural parameters, we must generally specify the entire structural model.

The  $J_1 \times G$  matrix  $\mathbf{R}_1 \mathbf{B}$  can be written as  $\mathbf{R}_1 \mathbf{B} = [\mathbf{R}_1 \boldsymbol{\beta}_1, \mathbf{R}_1 \boldsymbol{\beta}_2, \dots, \mathbf{R}_1 \boldsymbol{\beta}_G]$ , where  $\boldsymbol{\beta}_g$  is the  $(G+M) \times 1$  vector of structural parameters in equation g. By assumption (9.17), the first column of  $\mathbf{R}_1 \mathbf{B}$  is the zero vector. Therefore,  $\mathbf{R}_1 \mathbf{B}$  cannot have rank larger than G-1. What we must check is whether the columns of  $\mathbf{R}_1 \mathbf{B}$  other than the first form a linearly independent set.

Using condition (9.19) we can get a more general form of the order condition. Because  $\Gamma$  is nonsingular, **B** necessarily has rank G (full column rank). Therefore, for

{232}------------------------------------------------

condition (9.19) to hold, we must have rank R<sup>1</sup> bG - 1. But we have assumed that rank R<sup>1</sup> ¼ J1, which is the row dimension of R1.

theorem 9.3 (Order Condition for Identification): In system (9.12) under assumption (9.17), a necessary condition for the first equation to be identified is

$$J_1 \ge G - 1 \tag{9.20}$$

where J<sup>1</sup> is the row dimension of R1. Equation (9.20) is the general form of the order condition.

We can summarize the steps for checking whether the first equation in the system is identified.

- 1. Set one element of *g*<sup>1</sup> to -1 as a normalization.
- 2. Define the J<sup>1</sup> ðG þ MÞ matrix R<sup>1</sup> such that equation (9.17) captures all restrictions on *b*1.
- 3. If J<sup>1</sup> < G -1, the first equation is not identified.
- 4. If J<sup>1</sup> bG - 1, the equation might be identified. Let B be the matrix of all structural parameters with only the normalization restrictions imposed, and compute R1B. Now impose the restrictions in the entire system and check the rank condition (9.19).

The simplicity of the order condition makes it attractive as a tool for studying identification. Nevertheless, it is not difficult to write down examples where the order condition is satisfied but the rank condition fails.

Example 9.3 (Failure of the Rank Condition): Consider the following three-equation structural model in the population ðG ¼ 3; M ¼ 4Þ:

$$y_1 = \gamma_{12}y_2 + \gamma_{13}y_3 + \delta_{11}z_1 + \delta_{13}z_3 + u_1 \tag{9.21}$$

$$y_2 = \gamma_{21}y_1 + \delta_{21}z_1 + u_2 \tag{9.22}$$

$$y_3 = \delta_{31}z_1 + \delta_{32}z_2 + \delta_{33}z_3 + \delta_{34}z_4 + u_3 \tag{9.23}$$

where z<sup>1</sup> 1 1, EðugÞ ¼ 0, g ¼ 1; 2; 3, and each zj is uncorrelated with each ug. Note that the third equation is already a reduced form equation (although it may also have a structural interpretation). In equation (9.21) we have set g<sup>11</sup> ¼ -1, d<sup>12</sup> ¼ 0, and d<sup>14</sup> ¼ 0. Since this equation contains two right-hand-side endogenous variables and there are two excluded exogenous variables, it passes the order condition.

To check the rank condition, let *b*<sup>1</sup> denote the 7 1 vector of parameters in the first equation with only the normalization restriction imposed: *b*<sup>1</sup> ¼ ð-1; g12; g13; d11; d12; d13; d14Þ 0 . The restrictions d<sup>12</sup> ¼ 0 and d<sup>14</sup> ¼ 0 are obtained by choosing

{233}------------------------------------------------

$$\mathbf{R}_1 = \begin{pmatrix} 0 & 0 & 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{pmatrix}$$

Let **B** be the full  $7 \times 3$  matrix of parameters with only the three normalizations imposed [so that  $\beta_2 = (\gamma_{21}, -1, \gamma_{23}, \delta_{21}, \delta_{22}, \delta_{23}, \delta_{24})'$  and  $\beta_3 = (\gamma_{31}, \gamma_{32}, -1, \delta_{31}, \delta_{32}, \delta_{33}, \delta_{34})'$ ]. Matrix multiplication gives

$$\mathbf{R}_1 \mathbf{B} = \begin{pmatrix} \delta_{12} & \delta_{22} & \delta_{32} \\ \delta_{14} & \delta_{24} & \delta_{34} \end{pmatrix}$$

Now we impose all of the restrictions in the system. In addition to the restrictions  $\delta_{12} = 0$  and  $\delta_{14} = 0$  from equation (9.21), we also have  $\delta_{22} = 0$  and  $\delta_{24} = 0$  from equation (9.22). Therefore, with all restrictions imposed,

$$\mathbf{R}_1 \mathbf{B} = \begin{pmatrix} 0 & 0 & \delta_{32} \\ 0 & 0 & \delta_{34} \end{pmatrix} \tag{9.24}$$

The rank of this matrix is at most unity, and so the rank condition fails because G - 1 = 2.

Equation (9.22) easily passes the order condition. It is left to you to show that the rank condition holds if and only if  $\delta_{13} \neq 0$  and at least one of  $\delta_{32}$  and  $\delta_{34}$  is different from zero. The third equation is identified because it contains no endogenous explanatory variables.

When the restrictions on  $\beta_1$  consist entirely of normalization and exclusion restrictions, the order condition (9.20) reduces to the order condition (9.11), as can be seen by the following argument. When all restrictions are exclusion restrictions, the matrix  $\mathbf{R}_1$  consists only of zeros and ones, and the number of rows in  $\mathbf{R}_1$  equals the number of excluded right-hand-side endogenous variables,  $G - G_1 - 1$ , plus the number of excluded exogenous variables,  $M - M_1$ . In other words,  $J_1 = (G - G_1 - 1) + (M - M_1)$ , and so the order condition (9.20) becomes  $(G - G_1 - 1) + (M - M_1) \ge G - 1$ , which, upon rearrangement, becomes condition (9.11).

# 9.2.3 Unidentified, Just Identified, and Overidentified Equations

We have seen that, for identifying a single equation the rank condition (9.19) is necessary and sufficient. When condition (9.19) fails, we say that the equation is **unidentified**.

When the rank condition holds, it is useful to refine the sense in which the equation is identified. If  $J_1 = G - 1$ , then we have just enough identifying information. If we were to drop one restriction in  $\mathbf{R}_1$ , we would necessarily lose identification of the first equation because the order condition would fail. Therefore, when  $J_1 = G - 1$ , we say that the equation is **just identified**.

{234}------------------------------------------------

If  $J_1 > G - 1$ , it is often possible to drop one or more restrictions on the parameters of the first equation and still achieve identification. In this case we say the equation is **overidentified**. Necessary but not sufficient for overidentification is  $J_1 > G - 1$ . It is possible that  $J_1$  is strictly greater than G - 1 but the restrictions are such that dropping one restriction loses identification, in which case the equation is not overidentified.

In practice, we often appeal to the order condition to determine the degree of overidentification. While in special circumstances this approach can fail to be accurate, for most applications it is reasonable. Thus, for the first equation,  $J_1 - (G - 1)$  is usually intepreted as the number of **overidentifying restrictions**.

Example 9.4 (Overidentifying Restrictions): Consider the two-equation system

$$y_1 = y_{12}y_2 + \delta_{11}z_1 + \delta_{12}z_2 + \delta_{13}z_3 + \delta_{14}z_4 + u_1 \tag{9.25}$$

$$y_2 = \gamma_{21}y_1 + \delta_{21}z_1 + \delta_{22}z_2 + u_2 \tag{9.26}$$

where  $E(z_j u_g) = 0$ , all j and g. Without further restrictions, equation (9.25) fails the order condition because every exogenous variable appears on the right-hand side, and the equation contains an endogenous variable. Using the order condition, equation (9.26) is overidentified, with one overidentifying restriction. If  $z_3$  does not actually appear in equation (9.25), then equation (9.26) is just identified, assuming that  $\delta_{14} \neq 0$ .

#### 9.3 Estimation after Identification

# 9.3.1 The Robustness-Efficiency Trade-off

All SEMs with linearly homogeneous restrictions within each equation can be written with exclusion restrictions as in the system (9.1); doing so may require redefining some of the variables. If we let  $\mathbf{x}_{(g)} = (\mathbf{y}_{(g)}, \mathbf{z}_{(g)})$  and  $\boldsymbol{\beta}_{(g)} = (\mathbf{y}_{(g)}', \boldsymbol{\delta}_{(g)}')'$ , then the system (9.1) is in the general form (8.11) with the slight change in notation. Under assumption (9.2) the matrix of instruments for observation i is the  $G \times GM$  matrix

$$\mathbf{Z}_i \equiv \mathbf{I}_G \otimes \mathbf{z}_i \tag{9.27}$$

If every equation in the system passes the rank condition, a system estimation procedure—such as 3SLS or the more general minimum chi-square estimator—can be used. Alternatively, the equations of interest can be estimated by 2SLS. The bottom line is that the methods studied in Chapters 5 and 8 are directly applicable. All of the tests we have covered apply, including the tests of overidentifying restrictions in Chapters 6 and 8, and the single-equation tests for endogeneity in Chapter 6.

{235}------------------------------------------------

When estimating a simultaneous equations system, it is important to remember the pros and cons of full system estimation. If all equations are correctly specified, system procedures are asymptotically more efficient than a single-equation procedure such as 2SLS. But single-equation methods are more robust. If interest lies, say, in the first equation of a system, 2SLS is consistent and asymptotically normal provided the first equation is correctly specified and the instruments are exogenous. However, if one equation in a system is misspecified, the 3SLS or GMM estimates of all the parameters are generally inconsistent.

Example 9.5 (Labor Supply for Married, Working Women): Using the data in MROZ.RAW, we estimate a labor supply function for working, married women. Rather than specify a demand function, we specify the second equation as a wage offer function and impose the equilibrium condition:

$$hours = \gamma_{12} \log(wage) + \delta_{10} + \delta_{11}educ + \delta_{12}age + \delta_{13}kidslt6$$
$$+ \delta_{14}kidsge6 + \delta_{15}nwifeinc + u_1$$
 (9.28)

$$\log(wage) = \gamma_{21}hours + \delta_{20} + \delta_{21}educ + \delta_{22}exper + \delta_{23}exper^2 + u_2$$

$$(9.29)$$

where kidslt6 is number of children less than 6, kidsge6 is number of children between 6 and 18, and nwifeinc is income other than the woman's labor income. We assume that u<sup>1</sup> and u<sup>2</sup> have zero mean conditional on educ, age, kidslt6, kidsge6, nwifeinc, and exper.

The key restriction on the labor supply function is that exper (and exper2) have no direct effect on current annual hours. This identifies the labor supply function with one overidentifying restriction, as used by Mroz (1987). We estimate the labor supply function first by OLS [to see what ignoring the endogeneity of logðwageÞ does] and then by 2SLS, using as instruments all exogenous variables in equations (9.28) and (9.29).

There are 428 women who worked at some time during the survey year, 1975. The average annual hours are about 1,303 with a minimum of 12 and a maximum of 4,950.

We first estimate the labor supply function by OLS:

$$ho\hat{u}rs = 2,114.7 - 17.41 \log(wage) - 14.44 educ - 7.73 age$$

$$(340.1) \quad (54.22) \quad (17.97) \quad (5.53)$$

$$- 342.50 \ kidslt6 - 115.02 \ kidsge6 - 4.35 \ nwifeinc$$

$$(100.01) \quad (30.83) \quad (3.66)$$

{236}------------------------------------------------

The OLS estimates indicate a downward-sloping labor supply function, although the estimate on log(wage) is statistically insignificant.

The estimates are much different when we use 2SLS:

$$ho\hat{u}rs = 2,432.2 + 1,544.82 \log(wage) - 177.45 educ - 10.78 age$$
 $(594.2) \quad (480.74) \quad (58.14) \quad (9.58)$ 
 $- 210.83 \ kidslt6 - 47.56 \ kidsge6 - 9.25 \ nwifeinc$ 
 $(176.93) \quad (56.92) \quad (6.48)$ 

The estimated labor supply elasticity is 1,544.82/hours. At the mean hours for working women, 1,303, the estimated elasticity is about 1.2, which is quite large.

The supply equation has a single overidentifying restriction. The regression of the 2SLS residuals  $\hat{u}_1$  on all exogenous variables produces  $R_u^2 = .002$ , and so the test statistic is  $428(.002) \approx .856$  with *p*-value  $\approx .355$ ; the overidentifying restriction is not rejected.

Under the exclusion restrictions we have imposed, the wage offer function (9.29) is also identified. Before estimating the equation by 2SLS, we first estimate the reduced form for *hours* to ensure that the exogenous variables excluded from equation (9.29) are jointly significant. The *p*-value for the *F* test of joint significance of *age*, *kidslt6*, *kidsge6*, and *nwifeinc* is about .0009. Therefore, we can proceed with 2SLS estimation of the wage offer equation. The coefficient on *hours* is about .00016 (standard error  $\approx$  .00022), and so the wage offer does not appear to differ by hours worked. The remaining coefficients are similar to what is obtained by dropping *hours* from equation (9.29) and estimating the equation by OLS. (For example, the 2SLS coefficient on education is about .111 with se  $\approx$  .015.)

Interestingly, while the wage offer function (9.29) is identified, the analogous labor demand function is apparently unidentified. (This finding shows that choosing the normalization—that is, choosing between a labor demand function and a wage offer function—is not innocuous.) The labor demand function, written in equilibrium, would look like this:

$$hours = \gamma_{22} \log(wage) + \delta_{20} + \delta_{21}educ + \delta_{22}exper + \delta_{23}exper^{2} + u_{2}$$
 (9.30)

Estimating the reduced form for  $\log(wage)$  and testing for joint significance of age, kidslt6, kidsge6, and nwifeinc yields a p-value of about .46, and so the exogenous variables excluded from equation (9.30) would not seem to appear in the reduced form for  $\log(wage)$ . Estimation of equation (9.30) by 2SLS would be pointless. [You are invited to estimate equation (9.30) by 2SLS to see what happens.]

{237}------------------------------------------------

It would be more efficient to estimate equations (9.28) and (9.29) by 3SLS, since each equation is overidentified (assuming the homoskedasticity assumption SIV.5). If heteroskedasticity is suspected, we could use the general minimum chi-square estimator. A system procedure is more efficient for estimating the labor supply function because it uses the information that age, kidslt6, kidsge6, and nwifeinc do not appear in the logðwageÞ equation. If these exclusion restrictions are wrong, the 3SLS estimators of parameters in both equations are generally inconsistent. Problem 9.9 asks you to obtain the 3SLS estimates for this example.

# 9.3.2 When Are 2SLS and 3SLS Equivalent?

In Section 8.4 we discussed the relationship between 2SLS and 3SLS for a general linear system. Applying that discussion to linear SEMs, we can immediately draw the following conclusions: (1) if each equation is just identified, 2SLS equation by equation is algebraically identical to 3SLS, which is the same as the IV estimator in equation (8.22); (2) regardless of the degree of overidentification, 2SLS equation by equation and 3SLS are identical if S^ is diagonal.

Another useful equivalence result in the context of linear SEMs is as follows. Suppose that the first equation in a system is overidentified but every other equation is just identified. (A special case occurs when the first equation is a structural equation and all remaining equations are unrestricted reduced forms.) Then the 2SLS estimator of the first equation is the same as the 3SLS estimator. This result follows as a special case of Schmidt (1976, Theorem 5.2.13).