# Systems of Nonlinear Equations

> Pages: 439-447

A leading application of the results in Section 14.2 is to estimation of the parameters in an implicit set of nonlinear equations, such as a nonlinear simultaneous equations model. Partition  $\mathbf{w}_i$  as  $\mathbf{y}_i \in \mathbb{R}^J$ ,  $\mathbf{x}_i \in \mathbb{R}^K$  and, for  $h = 1, \dots, G$ , suppose we have

$$q_{1}(\mathbf{y}_{i}, \mathbf{x}_{i}, \boldsymbol{\theta}_{01}) = u_{i1}$$

$$\vdots$$

$$q_{G}(\mathbf{y}_{i}, \mathbf{x}_{i}, \boldsymbol{\theta}_{0G}) = u_{iG}$$

$$(14.33)$$

where  $\theta_{oh}$  is a  $P_h \times 1$  vector of parameters. As an example, write a two-equation SEM in the population as

{440}------------------------------------------------

$$y_1 = \mathbf{x}_1 \delta_1 + \gamma_1 y_2^{\gamma_2} + u_1 \tag{14.34}$$

$$y_2 = \mathbf{x}_2 \delta_2 + \gamma_3 y_1 + u_2 \tag{14.35}$$

(where we drop "o" to index the parameters). This model, unlike those covered in Section 9.5, is nonlinear in the *parameters* as well as the endogenous variables. Nevertheless, assuming that  $E(u_g | \mathbf{x}) = 0$ , g = 1, 2, the parameters in the system can be estimated by GMM by defining  $q_1(\mathbf{y}, \mathbf{x}, \boldsymbol{\theta}_1) = y_1 - \mathbf{x}_1 \boldsymbol{\delta}_1 - \gamma_1 y_2^{\gamma_2}$  and  $q_2(\mathbf{y}, \mathbf{x}, \boldsymbol{\theta}_2) = y_2 - \mathbf{x}_2 \boldsymbol{\delta}_2 - \gamma_3 y_1$ .

Generally, the equations (14.33) need not actually determine  $\mathbf{y}_i$  given the exogenous variables and disturbances; in fact, nothing requires J = G. Sometimes equations (14.33) represent a system of orthogonality conditions of the form  $\mathrm{E}[q_g(\mathbf{y}, \mathbf{x}, \boldsymbol{\theta}_{0g}) \,|\, \mathbf{x}] = 0, g = 1, \ldots, G$ . We will see an example later.

Denote the  $P \times 1$  vector of all parameters by  $\theta_0$ , and the parameter space by  $\Theta \subset \mathbb{R}^P$ . To identify the parameters we need the errors  $u_{ih}$  to satisfy some orthogonality conditions. A general assumption is, for some subvector  $\mathbf{x}_{ih}$  of  $\mathbf{x}_i$ ,

$$E(u_{ih} | \mathbf{x}_{ih}) = \mathbf{0}, \qquad h = 1, 2, \dots, G$$
 (14.36)

This allows elements of  $\mathbf{x}_i$  to be correlated with some errors, a situation that sometimes arises in practice (see, for example, Chapter 9 and Wooldridge, 1996). Under assumption (14.36), let  $\mathbf{z}_{ih} \equiv \mathbf{f}_h(\mathbf{x}_{ih})$  be a  $1 \times L_h$  vector of possibly nonlinear functions of  $\mathbf{x}_i$ . If there are no restrictions on the  $\theta_{oh}$  across equations we should have  $L_h \ge P_h$  so that each  $\theta_{oh}$  is identified. By iterated expectations, for all  $h = 1, \dots, G$ ,

$$\mathbf{E}(\mathbf{z}_{ih}^{\prime}u_{ih}) = \mathbf{0} \tag{14.37}$$

provided appropriate moments exist. Therefore, we obtain a set of orthogonality conditions by defining the  $G \times L$  matrix  $\mathbf{Z}_i$  as the block diagonal matrix with  $\mathbf{z}_{ig}$  in the gth block:

$$\mathbf{Z}_{i} \equiv \begin{bmatrix} \mathbf{z}_{i1} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{0} \\ \mathbf{0} & \mathbf{z}_{i2} & \mathbf{0} & \cdots & \mathbf{0} \\ \vdots & & & \vdots \\ \mathbf{0} & \mathbf{0} & \mathbf{0} & \cdots & \mathbf{z}_{iG} \end{bmatrix}$$
(14.38)

where  $L \equiv L_1 + L_2 + \cdots + L_G$ . Letting  $\mathbf{r}(\mathbf{w}_i, \boldsymbol{\theta}) \equiv \mathbf{q}(\mathbf{y}_i, \mathbf{x}_i, \boldsymbol{\theta}) \equiv [q_{i1}(\boldsymbol{\theta}_1), \dots, q_{iG}(\boldsymbol{\theta}_G)]'$ , equation (14.22) holds under assumption (14.36).

When there are no restrictions on the  $\theta_g$  across equations and  $\mathbf{Z}_i$  is chosen as in matrix (14.38), the system 2SLS estimator reduces to the **nonlinear 2SLS (N2SLS) estimator** (Amemiya, 1974) equation by equation. That is, for each h, the N2SLS estimator solves


{441}------------------------------------------------

$$\min_{\boldsymbol{\theta}_{h}} \left[ \sum_{i=1}^{N} \mathbf{z}'_{ih} q_{ih}(\boldsymbol{\theta}_{h}) \right]' \left( N^{-1} \sum_{i=1}^{N} \mathbf{z}'_{ih} \mathbf{z}_{ih} \right)^{-1} \left[ \sum_{i=1}^{N} \mathbf{z}'_{ih} q_{ih}(\boldsymbol{\theta}_{h}) \right]$$
(14.39)

Given only the orthogonality conditions (14.37), the N2SLS estimator is the efficient estimator of  $\theta_{oh}$  if

$$E(u_{ih}^2 \mathbf{z}_{ih}' \mathbf{z}_{ih}) = \sigma_{oh}^2 E(\mathbf{z}_{ih}' \mathbf{z}_{ih}) \tag{14.40}$$

where  $\sigma_{oh}^2 \equiv E(u_{ih}^2)$ ; sufficient for condition (14.40) is  $E(u_{ih}^2 | \mathbf{x}_{ih}) = \sigma_{oh}^2$ . Let  $\hat{\boldsymbol{\theta}}_h$  denote the N2SLS estimator. Then a consistent estimator of  $\sigma_{oh}^2$  is

$$\hat{\sigma}_h^2 \equiv N^{-1} \sum_{i=1}^N \hat{\hat{u}}_{ih}^2 \tag{14.41}$$

where  $\hat{\boldsymbol{u}}_{ih} \equiv q_h(\mathbf{y}_i, \mathbf{x}_i, \hat{\boldsymbol{\theta}}_h)$  are the N2SLS residuals. Under assumptions (14.37) and (14.40), the asymptotic variance of  $\hat{\boldsymbol{\theta}}_h$  is estimated as

$$\hat{\sigma}_{h}^{2} \left\{ \left[ \sum_{i=1}^{N} \mathbf{z}_{ih}^{\prime} \nabla_{\theta_{h}} q_{ih}(\hat{\hat{\boldsymbol{\theta}}}_{h}) \right]^{\prime} \left( \sum_{i=1}^{N} \mathbf{z}_{ih}^{\prime} \mathbf{z}_{ih} \right)^{-1} \left[ \sum_{i=1}^{N} \mathbf{z}_{ih}^{\prime} \nabla_{\theta_{h}} q_{ih}(\hat{\hat{\boldsymbol{\theta}}}_{h}) \right] \right\}^{-1}$$

$$(14.42)$$

where  $\nabla_{\theta_h} q_{ih}(\hat{\hat{\boldsymbol{\theta}}}_h)$  is the  $1 \times P_h$  gradient.

If assumption (14.37) holds but assumption (14.40) does not, the N2SLS estimator is still  $\sqrt{N}$ -consistent, but it is not the efficient estimator that uses the orthogonality condition (14.37) whenever  $L_h > P_h$  [and expression (14.42) is no longer valid]. A more efficient estimator is obtained by solving

$$\min_{\boldsymbol{\theta}_h} \left[ \sum_{i=1}^{N} \mathbf{z}_{ih}' q_{ih}(\boldsymbol{\theta}_h) \right]' \left( N^{-1} \sum_{i=1}^{N} \hat{\boldsymbol{u}}_{ih}^2 \mathbf{z}_{ih}' \mathbf{z}_{ih} \right)^{-1} \left[ \sum_{i=1}^{N} \mathbf{z}_{ih}' q_{ih}(\boldsymbol{\theta}_h) \right]$$

with asymptotic variance estimated as

$$\left\{ \left[ \sum_{i=1}^{N} \mathbf{z}_{ih}' \nabla_{\theta_h} q_{ih}(\hat{\hat{\boldsymbol{\theta}}}_h) \right]' \left( \sum_{i=1}^{N} \hat{\hat{\boldsymbol{u}}}_{ih}^2 \mathbf{z}_{ih}' \mathbf{z}_{ih} \right)^{-1} \left[ \sum_{i=1}^{N} \mathbf{z}_{ih}' \nabla_{\theta_h} q_{ih}(\hat{\hat{\boldsymbol{\theta}}}_h) \right] \right\}^{-1}$$

This estimator is asymptotically equivalent to the N2SLS estimator if assumption (14.40) happens to hold.

Rather than focus on one equation at a time, we can increase efficiency if we estimate the equations simultaneously. One reason for doing so is to impose cross equation restrictions on the  $\theta_{oh}$ . The system 2SLS estimator can be used for these

{442}------------------------------------------------

purposes, where  $\mathbf{Z}_i$  generally has the form (14.38). But this estimator does not exploit correlation in the errors  $u_{ia}$  and  $u_{ih}$  in different equations.

The efficient estimator that uses all orthogonality conditions in equation (14.37) is just the GMM estimator with  $\hat{\mathbf{\Lambda}}$  given by equation (14.25), where  $\mathbf{r}_i(\hat{\boldsymbol{\theta}})$  is the  $G \times 1$  vector of system 2SLS residuals,  $\hat{\mathbf{u}}_i$ . In other words, the efficient GMM estimator solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{q}_{i}(\boldsymbol{\theta}) \right]' \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\mathbf{q}}_{i} \hat{\mathbf{u}}_{i}' \mathbf{Z}_{i} \right)^{-1} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{q}_{i}(\boldsymbol{\theta}) \right]$$
(14.43)

The asymptotic variance of  $\hat{\theta}$  is estimated as

$$\left\{ \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \nabla_{\theta} \mathbf{q}_{i}(\hat{\boldsymbol{\theta}}) \right]' \left( \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\hat{\mathbf{u}}}_{i} \hat{\mathbf{u}}_{i}' \mathbf{Z}_{i} \right)^{-1} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \nabla_{\theta} \mathbf{q}_{i}(\hat{\boldsymbol{\theta}}) \right] \right\}^{-1}$$

Because this is the efficient GMM estimator, the QLR statistic can be used to test hypotheses about  $\theta_0$ . The Wald statistic can also be applied.

Under the homoskedasticity assumption (14.26) with  $\mathbf{r}_i(\boldsymbol{\theta}_o) = \mathbf{u}_i$ , the nonlinear 3SLS estimator, which solves

$$\min_{\boldsymbol{\theta} \in \boldsymbol{\Theta}} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{q}_{i}(\boldsymbol{\theta}) \right]' \left( N^{-1} \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\boldsymbol{\Omega}} \mathbf{Z}_{i} \right)^{-1} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \mathbf{q}_{i}(\boldsymbol{\theta}) \right]$$

is efficient, and its asymptotic variance is estimated as

$$\left\{ \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \nabla_{\theta} \mathbf{r}_{i}(\hat{\boldsymbol{\theta}}) \right]' \left( \sum_{i=1}^{N} \mathbf{Z}_{i}' \hat{\boldsymbol{\Omega}} \mathbf{Z}_{i} \right)^{-1} \left[ \sum_{i=1}^{N} \mathbf{Z}_{i}' \nabla_{\theta} \mathbf{r}_{i}(\hat{\boldsymbol{\theta}}) \right] \right\}^{-1}$$

The N3SLS estimator is used widely for systems of the form (14.33), but, as we discussed in Section 9.6, there are many cases where assumption (14.26) must fail when different instruments are needed for different equations.

As an example, we show how a **hedonic price system** fits into this framework. Consider a linear demand and supply system for *G* attributes of a good or service (see Epple, 1987; Kahn and Lang, 1988; and Wooldridge, 1996). The demand and supply system is written as

$$demand_g = \eta_{1g} + \mathbf{w}a_{1g} + \mathbf{x}_1\boldsymbol{\beta}_{1g} + u_{1g}, \qquad g = 1, \dots, G$$
  
 $supply_g = \eta_{2g} + \mathbf{w}a_{2g} + \mathbf{x}_2\boldsymbol{\beta}_{2g} + u_{2g}, \qquad g = 1, \dots, G$ 

{443}------------------------------------------------

where w ¼ ðw1; ... ; wGÞ is the 1 G vector of attribute prices. The demand equations usually represent an individual or household; the supply equations can represent an individual, firm, or employer.

There are several tricky issues in estimating either the demand or supply function for a particular g. First, the attribute prices wg are not directly observed. What is usually observed are the equilibrium quantities for each attribute and each cross section unit i; call these qig, g ¼ 1; ... ; G. (In the hedonic systems literature these are often denoted zig, but we use qig here because they are endogenous variables, and we have been using z<sup>i</sup> to denote exogenous variables.) For example, the qig can be features of a house, such as size, number of bathrooms, and so on. Along with these features we observe the equilibrium price of the good, pi, which we assume follows a quadratic hedonic price function:

$$p_i = \gamma + \mathbf{q}_i \boldsymbol{\psi} + \mathbf{q}_i \boldsymbol{\Pi} \mathbf{q}_i' / 2 + \mathbf{x}_{i3} \boldsymbol{\delta} + \mathbf{x}_{i3} \boldsymbol{\Gamma} \mathbf{q}_i' + u_{i3}$$
(14.44)

where xi<sup>3</sup> is a vector of variables that affect pi, P is a G G symmetric matrix, and G is a G G matrix.

A key point for identifying the demand and supply functions is that w<sup>i</sup> ¼ qpi=qqi, which, under equation (14.44), becomes w<sup>i</sup> ¼ qiP þ xi3G, or wig ¼ qi*p*<sup>g</sup> þ xi3*g*<sup>g</sup> for each g. By substitution, the equilibrium estimating equations can be written as equation (14.44) plus

$$q_{ig} = \eta_{1g} + (\mathbf{q}_i \mathbf{\Pi} + \mathbf{x}_{i3} \mathbf{\Gamma}) \mathbf{a}_{1g} + \mathbf{x}_{i1} \mathbf{\beta}_{1g} + u_{i1g}, \qquad g = 1, \dots, G$$
(14.45)

$$q_{ig} = \eta_{2g} + (\mathbf{q}_i \mathbf{\Pi} + \mathbf{x}_{i3} \mathbf{\Gamma}) \mathbf{\alpha}_{2g} + \mathbf{x}_{i2} \mathbf{\beta}_{2g} + u_{i2g}, \qquad g = 1, \dots, G$$
(14.46)

These two equations are linear in qi; xi1; xi2, and xi<sup>3</sup> but nonlinear in the parameters. Let ui<sup>1</sup> be the G 1 vector of attribute demand disturbances and ui<sup>2</sup> the G 1 vector of attribute supply disturbances. What are reasonable assumptions about ui1; ui2, and ui3? It is almost always assumed that equation (14.44) represents a conditional expectation with no important unobserved factors; this assumption means Eðui<sup>3</sup> j qi; xiÞ ¼ 0, where x<sup>i</sup> contains all elements in x<sup>i</sup>1; xi2, and xi3. The properties of u<sup>i</sup><sup>1</sup> and u<sup>i</sup><sup>2</sup> are more subtle. It is clear that these cannot be uncorrelated with qi, and so equations (14.45) and (14.46) contain endogenous explanatory variables if P 00. But there is another problem, pointed out by Bartik (1987), Epple (1987), and Kahn and Lang (1988): because of matching that happens between individual buyers and sellers, x<sup>i</sup><sup>2</sup> is correlated with ui1, and x<sup>i</sup><sup>1</sup> is correlated with ui2. Consequently, what would seem to be the obvious IVs for the demand equations (14.45)—the factors shifting the supply curve—are endogenous to equation (14.45). Fortunately, all is not lost: if x<sup>i</sup><sup>3</sup> contains exogenous factors that affect pi but do not appear in the struc

{444}------------------------------------------------

tural demand and supply functions, we can use these as instruments in both the demand and supply equations. Specifically, we assume

$$E(\mathbf{u}_{i1} | \mathbf{x}_{i1}, \mathbf{x}_{i3}) = \mathbf{0}, \qquad E(\mathbf{u}_{i2} | \mathbf{x}_{i2}, \mathbf{x}_{i3}) = \mathbf{0}, \qquad E(u_{i3} | \mathbf{q}_{i}, \mathbf{x}_{i}) = 0$$
 (14.47)

Common choices for  $\mathbf{x}_{i3}$  are geographical or industry dummy indicators (for example, Montgomery, Shaw, and Benedict, 1992; Hagy, 1998), where the assumption is that the demand and supply functions do not change across region or industry but the type of matching does, and therefore  $p_i$  can differ systematically across region or industry. Bartik (1987) discusses how a randomized experiment can be used to create the elements of  $\mathbf{x}_{i3}$ .

For concreteness, let us focus on estimating the set of demand functions. If  $\Pi = \mathbf{0}$ , so that the quadratic in  $\mathbf{q}_i$  does not appear in equation (14.44), a simple two-step procedure is available: (1) estimate equation (14.44) by OLS, and obtain  $\hat{w}_{ig} = \hat{\psi}_g + \mathbf{x}_{i3}\hat{\gamma}_g$  for each i and g; (2) run the regression  $q_{ig}$  on 1,  $\hat{\mathbf{w}}_i, \mathbf{x}_{i1}, i = 1, \dots, N$ . Under assumptions (14.47) and identification assumptions, this method produces  $\sqrt{N}$ -consistent, asymptotically normal estimators of the parameters in demand equation g. Because the second regression involves generated regressors, the standard errors and test statistics should be adjusted.

It is clear that, without restrictions on  $a_{1g}$ , the order condition necessary for identifying the demand parameters is that the dimension of  $\mathbf{x}_{i3}$ , say  $K_3$ , must exceed G. If  $K_3 < G$  then  $\mathrm{E}[(\mathbf{w}_i, \mathbf{x}_{i1})'(\mathbf{w}_i, \mathbf{x}_{i1})]$  has less than full rank, and the OLS rank condition fails. If we make exclusion restrictions on  $a_{1g}$ , fewer elements are needed in  $\mathbf{x}_{i3}$ . In the case that only  $w_{ig}$  appears in the demand equation for attribute g,  $\mathbf{x}_{i3}$  can be a scalar, provided its interaction with  $q_{ig}$  in the hedonic price system is significant  $(\gamma_{gg} \neq 0)$ . Checking the analogue of the rank condition in general is somewhat complicated; see Epple (1987) for discussion.

When  $\mathbf{w}_i = \mathbf{q}_i \mathbf{\Pi} + \mathbf{x}_{i3} \mathbf{\Gamma}$ ,  $\mathbf{w}_i$  is correlated with  $u_{i1g}$ , so we must modify the two-step procedure. In the second step, we can use instruments for  $\hat{\mathbf{w}}_i$  and perform 2SLS rather than OLS. Assuming that  $\mathbf{x}_{i3}$  has enough elements, the demand equations are still identified. If only  $w_{ig}$  appears in  $demand_{ig}$ , sufficient for identification is that an element of  $\mathbf{x}_{i3}$  appears in the linear projection of  $w_{ig}$  on  $\mathbf{x}_{i1}$ ,  $\mathbf{x}_{i3}$ . This assumption can hold even if  $\mathbf{x}_{i3}$  has only a single element. For the matching reasons we discussed previously,  $\mathbf{x}_{i2}$  cannot be used as instruments for  $\hat{\mathbf{w}}_i$  in the demand equation.

Whether  $\Pi = 0$  or not, more efficient estimators are obtained from the full demand system and the hedonic price function. Write

$$\mathbf{q}_i' = \boldsymbol{\eta}_1 + (\mathbf{q}_i \boldsymbol{\Pi} + \mathbf{x}_{i3} \boldsymbol{\Gamma}) \mathbf{A}_1 + \mathbf{x}_{i1} \mathbf{B}_1 + \mathbf{u}_{i1}$$

{445}------------------------------------------------

along with equation (14.44). Then  $(\mathbf{x}_{i1}, \mathbf{x}_{i3})$  (and functions of these) can be used as instruments in any of the G demand equations, and  $(\mathbf{q}_i, \mathbf{x}_i)$  act as IVs in equation (14.44). (It may be that the supply function is not even specified, in which case  $\mathbf{x}_i$  contains only  $\mathbf{x}_{i1}$  and  $\mathbf{x}_{i3}$ .) A first-stage estimator is the nonlinear system 2SLS estimator. Then the system can be estimated by the minimum chi-square estimator that solves problem (14.43). When restricting attention to demand equations plus the hedonic price equation, or supply equations plus the hedonic price equation, nonlinear 3SLS is efficient under certain assumptions. If the demand and supply equations are estimated together, the key assumption (14.26) that makes nonlinear 3SLS asymptotically efficient cannot be expected to hold; see Wooldridge (1996) for discussion.

If one of the demand functions is of primary interest, it may make sense to estimate it along with equation (14.44), by GMM or nonlinear 3SLS. If the demand functions are written in inverse form, the resulting system is linear in the parameters, as shown in Wooldridge (1996).

#### 14.4 Panel Data Applications

As we saw in Chapter 11, system IV methods are needed in certain panel data contexts. In the current case, our interest is in nonlinear panel data models that cannot be estimated using linear methods. We hold off on discussing nonlinear panel data models explicitly containing unobserved effects until Part IV.

One increasingly popular use of panel data is to test rationality in economic models of individual, family, or firm behavior (see, for example, Shapiro, 1984; Zeldes, 1989; Keane and Runkle, 1992; Shea, 1995). For a random draw from the population we assume that T time periods are available. Suppose that an economic theory implies that

$$E[r_t(\mathbf{w}_t, \boldsymbol{\theta}_0) \mid \mathbf{w}_{t-1}, \dots, \mathbf{w}_1) = 0, \qquad t = 1, \dots, T$$
(14.48)

where, for simplicity,  $r_t$  is a scalar. These conditional moment restrictions are often implied by rational expectations, under the assumption that the decision horizon is the same length as the sampling period. For example, consider a standard life-cycle model of consumption. Let  $c_{it}$  denote consumption of family i at time t, let  $\mathbf{h}_{it}$  denote taste shifters, let  $\delta_0$  denote the common rate of time preference, and let  $a_{it}^j$  denote the return for family i from holding asset j from period t-1 to t. Under the assumption that utility is given by

$$\mathbf{u}(c_{it}, \theta_{it}) = \exp(\mathbf{h}_{it}\boldsymbol{\beta}_{o})c_{it}^{1-\lambda_{o}}/(1-\lambda_{o})$$
(14.49)

the Euler equation is

{446}------------------------------------------------

$$E[(1+a_{it}^{j})(c_{it}/c_{i,t-1})^{-\lambda_{o}} | \mathcal{I}_{i,t-1}] = (1+\delta_{o})^{-1} \exp(\mathbf{x}_{it}\boldsymbol{\beta}_{o})$$
(14.50)

where  $\mathcal{I}_{it}$  is family i's information set at time t and  $\mathbf{x}_{it} \equiv \mathbf{h}_{i,t-1} - \mathbf{h}_{it}$ ; equation (14.50) assumes that  $\mathbf{h}_{it} - \mathbf{h}_{i,t-1} \in \mathcal{I}_{i,t-1}$ , an assumption which is often reasonable. Given equation (14.50), we can define a residual function for each t:

$$r_{it}(\boldsymbol{\theta}) = (1 + a_{it}^j)(c_{it}/c_{i,t-1})^{-\lambda} - \exp(\mathbf{x}_{it}\boldsymbol{\beta})$$
(14.51)

where  $(1 + \delta)^{-1}$  is absorbed in an intercept in  $\mathbf{x}_{it}$ . Let  $\mathbf{w}_{it}$  contain  $c_{it}$ ,  $c_{i,t-1}$ ,  $a_{it}$ , and  $\mathbf{x}_{it}$ . Then condition (14.48) holds, and  $\lambda_0$  and  $\boldsymbol{\beta}_0$  can be estimated by GMM.

Returning to condition (14.48), valid instruments at time t are functions of information known at time t-1:

$$\mathbf{z}_t = \mathbf{f}_t(\mathbf{w}_{t-1}, \dots, \mathbf{w}_1) \tag{14.52}$$

The  $T \times 1$  residual vector is  $\mathbf{r}(\mathbf{w}, \boldsymbol{\theta}) = [r_1(\mathbf{w}_1, \boldsymbol{\theta}), \dots, r_T(\mathbf{w}_T, \boldsymbol{\theta})]'$ , and the matrix of instruments has the same form as matrix (14.38) for each i (with G = T). Then, the minimum chi-square estimator can be obtained after using the system 2SLS estimator, although the choice of instruments is a nontrivial matter. A common choice is linear and quadratic functions of variables lagged one or two time periods.

Estimation of the optimal weighting matrix is somewhat simplified under the conditional moment restrictions (14.48). Recall from Section 14.2 that the optimal estimator uses the inverse of a consistent estimator of  $\Lambda_o = E[\mathbf{Z}_i'\mathbf{r}_i(\theta_o)\mathbf{r}_i(\theta_o)'\mathbf{Z}_i]$ . Under condition (14.48), this matrix is block diagonal. Dropping the *i* subscript, the (s, t) block is  $E[r_s(\theta_o)r_t(\theta_o)\mathbf{z}_s'\mathbf{z}_t]$ . For concreteness, assume that s < t. Then  $\mathbf{z}_t, \mathbf{z}_s$ , and  $r_s(\theta_o)$  are all functions of  $\mathbf{w}_{t-1}, \mathbf{w}_{t-2}, \ldots, \mathbf{w}_1$ . By iterated expectations it follows that

$$E[r_s(\boldsymbol{\theta}_{o})r_t(\boldsymbol{\theta}_{o})\mathbf{z}_{s}'\mathbf{z}_{t}] = E\{r_s(\boldsymbol{\theta}_{o})\mathbf{z}_{s}'\mathbf{z}_{t}E[r_t(\boldsymbol{\theta}_{o}) \mid \mathbf{w}_{t-1}, \dots, \mathbf{w}_{1}]\} = 0$$

and so we only need to estimate the diagonal blocks of  $E[\mathbf{Z}_i'\mathbf{r}_i(\theta_o)\mathbf{r}_i(\theta_o)'\mathbf{Z}_i]$ :

$$N^{-1} \sum_{i=1}^{N} \hat{\mathbf{r}}_{it}^2 \mathbf{z}_{it}' \mathbf{z}_{it} \tag{14.53}$$

is a consistent estimator of the *t*th block, where the  $\hat{r}_{it}$  are obtained from an inefficient GMM estimator.

In cases where the data frequency does not match the horizon relevant for decision making, the optimal matrix does not have the block diagonal form: some off-diagonal blocks will be nonzero. See Hansen (1982) for the pure time series case.

Ahn and Schmidt (1995) apply nonlinear GMM methods to estimate the linear, unobserved effects AR(1) model. Some of the orthogonality restrictions they use are nonlinear in the parameters of interest. In Part IV we will cover nonlinear panel data

{447}------------------------------------------------

models with unobserved effects. For the consumption example, we would like to allow for a family-specific rate of time preference, as well as unobserved family tastes. Orthogonality conditions can often be obtained in such cases, but they are not as straightforward to obtain as in the previous example.

#### 14.5 Efficient Estimation

In Chapter 8 we obtained the efficient weighting matrix for GMM estimation of linear models, and we extended that to nonlinear models in Section 14.1. In Chapter 13 we asserted that maximum likelihood estimation has some important efficiency properties. We are now in a position to study a framework that allows us to show the efficiency of an estimator within a particular class of estimators, and also to find efficient estimators within a stated class. Our approach is essentially that in Newey and McFadden (1994, Section 5.3), although we will not use the weakest possible assumptions. Bates and White (1993) proposed a very similar framework and also considered time series problems.