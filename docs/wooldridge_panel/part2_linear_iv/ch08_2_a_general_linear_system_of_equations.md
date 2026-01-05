# A General Linear System of Equations

> Pages: 199-201

We now discuss estimation of a general linear model of the form

$$\mathbf{y}_i = \mathbf{X}_i \boldsymbol{\beta} + \mathbf{u}_i \tag{8.11}$$

where y<sup>i</sup> is a G 1 vector, X<sup>i</sup> is a G K matrix, and u<sup>i</sup> is the G 1 vector of errors. This model is identical to equation (7.9), except that we will use different assumptions. In writing out examples, we will often omit the observation subscript i, but for the general analysis carrying it along is a useful notational device. As in Chapter 7, the rows of yi, Xi, and u<sup>i</sup> can represent different time periods for the same crosssectional unit (so G ¼ T, the total number of time periods). Therefore, the following analysis applies to panel data models where T is small relative to the cross section sample size, N; for an example, see Problem 8.8. We cover general panel data applications in Chapter 11. (As in Chapter 7, the label ''systems of equations'' is not especially accurate for basic panel data models because we have only one behavioral equation over T different time periods.)

The following orthogonality condition is the basis for estimating *b*:

assumption SIV.1: EðZ<sup>0</sup> <sup>i</sup>uiÞ ¼ 0, where Z<sup>i</sup> is a G L matrix of observable instrumental variables.

(The acronym SIV stands for ''system instrumental variables.'') For the purposes of discussion, we assume that EðuiÞ ¼ 0; this assumption is almost always true in practice anyway.

From what we know about IV and 2SLS for single equations, Assumption SIV.1 cannot be enough to identify the vector *b*. An assumption sufficient for identification is the rank condition:

assumption SIV.2: rank EðZ<sup>0</sup> <sup>i</sup>XiÞ ¼ K.

Assumption SIV.2 generalizes the rank condition from the single-equation case. (When G ¼ 1, Assumption SIV.2 is the same as Assumption 2SLS.2b.) Since EðZ<sup>0</sup> <sup>i</sup>XiÞ is an L K matrix, Assumption SIV.2 requires the columns of this matrix to be linearly independent. Necessary for the rank condition is the order condition: L bK. We will investigate the rank condition in detail for a broad class of models in Chapter 9. For now, we just assume that it holds.

{200}------------------------------------------------

In what follows, it is useful to carry along a particular example that applies to simultaneous equations models and other models with potentially endogenous explanatory variables. Write a G equation system for the population as

$$y_1 = \mathbf{x}_1 \boldsymbol{\beta}_1 + u_1$$

$$\vdots$$

$$y_G = \mathbf{x}_G \boldsymbol{\beta}_G + u_G$$
(8.12)

where, for each equation g,  $\mathbf{x}_g$  is a  $1 \times K_g$  vector that can contain both exogenous and endogenous variables. For each g,  $\boldsymbol{\beta}_g$  is  $K_g \times 1$ . Because this looks just like the SUR system from Chapter 7, we will refer to it as a SUR system, keeping in mind the crucial fact that some elements of  $\mathbf{x}_g$  are thought to be correlated with  $u_g$  for at least some g.

For each equation we assume that we have a set of instrumental variables, a  $1 \times L_g$  vector  $\mathbf{z}_g$ , that are exogenous in the sense that

$$E(\mathbf{z}_{q}^{\prime}u_{q}) = 0, \qquad g = 1, 2, \dots, G$$
 (8.13)

In most applications unity is an element of  $\mathbf{z}_g$  for each g, so that  $\mathrm{E}(u_g) = 0$ , all g. As we will see, and as we already know from single-equation analysis, if  $\mathbf{x}_g$  contains some elements correlated with  $u_g$ , then  $\mathbf{z}_g$  must contain more than just the exogenous variables appearing in equation g. Much of the time the same instruments, which consist of all exogenous variables appearing anywhere in the system, are valid for every equation, so that  $\mathbf{z}_g = \mathbf{z}, g = 1, 2, \ldots, G$ . Some applications require us to have different instruments for different equations, so we allow that possibility here.

Putting an i subscript on the variables in equations (8.12), and defining

$$\mathbf{y}_{i} \equiv \begin{pmatrix} y_{i1} \\ y_{i2} \\ \vdots \\ y_{iG} \end{pmatrix}, \quad \mathbf{X}_{i} \equiv \begin{pmatrix} \mathbf{x}_{i1} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\ \mathbf{0} & \mathbf{x}_{i2} & \mathbf{0} & \cdots & \mathbf{0} \\ \vdots & & & & \vdots \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{x}_{iG} \end{pmatrix}, \quad \mathbf{u}_{i} \equiv \begin{pmatrix} u_{i1} \\ u_{i2} \\ \vdots \\ u_{iG} \end{pmatrix}$$
(8.14)

and  $\beta = (\beta'_1, \beta'_2, \dots, \beta'_G)'$ , we can write equation (8.12) in the form (8.11). Note that  $K = K_1 + K_2 + \dots + K_G$  is the total number of parameters in the system.

The matrix of instruments has a structure similar to  $X_i$ :

$$\mathbf{Z}_{i} \equiv \begin{pmatrix} \mathbf{z}_{i1} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\ \mathbf{0} & \mathbf{z}_{i2} & \mathbf{0} & \cdots & \mathbf{0} \\ \vdots & & & \vdots \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{z}_{iG} \end{pmatrix}$$
(8.15)


{201}------------------------------------------------

which has dimension  $G \times L$ , where  $L = L_1 + L_2 + \cdots + L_G$ . Then, for each i,

$$\mathbf{Z}_{i}'\mathbf{u}_{i} = (\mathbf{z}_{i1}u_{i1}, \mathbf{z}_{i2}u_{i2}, \dots, \mathbf{z}_{iG}u_{iG})'$$

$$(8.16)$$

and so  $E(\mathbf{Z}_i'\mathbf{u}_i) = \mathbf{0}$  reproduces the orthogonality conditions (8.13). Also,

$$E(\mathbf{Z}_{i}'\mathbf{X}_{i}) = \begin{pmatrix} E(\mathbf{z}_{i1}'\mathbf{x}_{i1}) & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\ \mathbf{0} & E(\mathbf{z}_{i2}'\mathbf{x}_{i2}) & \mathbf{0} & \cdots & \mathbf{0} \\ \vdots & & & & \vdots \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & E(\mathbf{z}_{iG}'\mathbf{x}_{iG}) \end{pmatrix}$$
(8.17)

where  $\mathrm{E}(\mathbf{z}_{ig}'\mathbf{x}_{ig})$  is  $L_g \times K_g$ . Assumption SIV.2 requires that this matrix have full column rank, where the number of columns is  $K = K_1 + K_2 + \cdots + K_G$ . A well-known result from linear algebra says that a block diagonal matrix has full column rank if and only if each block in the matrix has full column rank. In other words, Assumption SIV.2 holds in this example if and only if

rank 
$$E(\mathbf{z}'_{ia}\mathbf{x}_{ig}) = K_g, \qquad g = 1, 2, ..., G$$
 (8.18)

This is *exactly* the rank condition needed for estimating each equation by 2SLS, which we know is possible under conditions (8.13) and (8.18). Therefore, identification of the SUR system is equivalent to identification equation by equation. This reasoning assumes that the  $\beta_g$  are unrestricted across equations. If some prior restrictions are known, then identification is more complicated, something we cover explicitly in Chapter 9.

In the important special case where the same instruments,  $\mathbf{z}_i$ , can be used for every equation, we can write definition (8.15) as  $\mathbf{Z}_i = \mathbf{I}_G \otimes \mathbf{z}_i$ .

#### **8.3** Generalized Method of Moments Estimation