# Estimating the Reduced Form Parameters

> Pages: 237-240

So far, we have discussed estimation of the structural parameters. The usual justifications for focusing on the structural parameters are as follows: (1) we are interested in estimates of ''economic parameters'' (such as labor supply elasticities) for curiosity's sake; (2) estimates of structural parameters allow us to obtain the effects of a variety of policy interventions (such as changes in tax rates); and (3) even if we want to estimate the reduced form parameters, we often can do so more efficiently by first estimating the structural parameters. Concerning the second reason, if the goal is to estimate, say, the equilibrium change in hours worked given an exogenous change in a marginal tax rate, we must ultimately estimate the reduced form.

As another example, we might want to estimate the effect on county-level alcohol consumption due to an increase in exogenous alcohol taxes. In other words, we are interested in qEðyg j zÞ=qzj ¼ pgj, where yg is alcohol consumption and zj is the tax on alcohol. Under weak assumptions, reduced form equations exist, and each equation of the reduced form can be estimated by ordinary least squares. Without placing any restrictions on the reduced form, OLS equation by equation is identical to SUR 

{238}------------------------------------------------

estimation (see Section 7.7). In other words, we do not need to analyze the structural equations at all in order to consistently estimate the reduced form parameters. Ordinary least squares estimates of the reduced form parameters are robust in the sense that they do not rely on any identification assumptions imposed on the structural system.

If the structural model is correctly specified and at least one equation is overidentified, we obtain asymptotically more efficient estimators of the reduced form parameters by deriving the estimates from the structural parameter estimates. In particular, given the structural parameter estimates  $\hat{\bf \Delta}$  and  $\hat{\bf \Gamma}$ , we can obtain the reduced form estimates as  $\hat{\bf \Pi} = -\hat{\bf \Delta}\hat{\bf \Gamma}^{-1}$  [see equation (9.14)]. These are consistent,  $\sqrt{N}$ -asymptotically normal estimators (although the asymptotic variance matrix is somewhat complicated). From Problem 3.9, we obtain the most efficient estimator of  $\bf \Pi$  by using the most efficient estimators of  $\bf \Delta$  and  $\bf \Gamma$  (minimum chi-square or, under system homoskedasticity, 3SLS).

Just as in estimating the structural parameters, there is a robustness-efficiency trade-off in estimating the  $\pi_{gj}$ . As mentioned earlier, the OLS estimators of each reduced form are robust to misspecification of any restrictions on the structural equations (although, as always, each element of z should be exogenous for OLS to be consistent). The estimators of the  $\pi_{gj}$  derived from estimators of  $\Delta$  and  $\Gamma$ —whether the latter are 2SLS or system estimators—are generally nonrobust to incorrect restrictions on the structural system. See Problem 9.11 for a simple illustration.

#### 9.4 Additional Topics in Linear SEMs

# 9.4.1 Using Cross Equation Restrictions to Achieve Identification

So far we have discussed identification of a single equation using only within-equation parameter restrictions [see assumption (9.17)]. This is by far the leading case, especially when the system represents a simultaneous equations model with truly autonomous equations. Nevertheless, occasionally economic theory implies parameter restrictions across different equations in a system that contains endogenous variables. Not surprisingly, such **cross equation restrictions** are generally useful for identifying equations. A general treatment is beyond the scope of our analysis. Here we just give an example to show how identification and estimation work.

Consider the two-equation system

$$y_1 = \gamma_{12}y_2 + \delta_{11}z_1 + \delta_{12}z_2 + \delta_{13}z_3 + u_1 \tag{9.31}$$

$$y_2 = \gamma_{21}y_1 + \delta_{21}z_1 + \delta_{22}z_2 + u_2 \tag{9.32}$$

{239}------------------------------------------------

where each  $z_j$  is uncorrelated with  $u_1$  and  $u_2$  ( $z_1$  can be unity to allow for an intercept). Without further information, equation (9.31) is unidentified, and equation (9.32) is just identified if and only if  $\delta_{13} \neq 0$ . We maintain these assumptions in what follows.

Now suppose that  $\delta_{12} = \delta_{22}$ . Because  $\delta_{22}$  is identified in equation (9.32) we can treat it as known for studying identification of equation (9.31). But  $\delta_{12} = \delta_{22}$ , and so we can write

$$y_1 - \delta_{12}z_2 = y_{12}y_2 + \delta_{11}z_1 + \delta_{13}z_3 + u_1 \tag{9.33}$$

where  $y_1 - \delta_{12}z_2$  is effectively known. Now the right-hand side of equation (9.33) has one endogenous variable,  $y_2$ , and the two exogenous variables  $z_1$  and  $z_3$ . Because  $z_2$  is excluded from the right-hand side, we can use  $z_2$  as an instrument for  $y_2$ , as long as  $z_2$  appears in the reduced form for  $y_2$ . This is the case provided  $\delta_{12} = \delta_{22} \neq 0$ .

This approach to showing that equation (9.31) is identified also suggests a consistent estimation procedure: first, estimate equation (9.32) by 2SLS using  $(z_1, z_2, z_3)$  as instruments, and let  $\hat{\delta}_{22}$  be the estimator of  $\delta_{22}$ . Then, estimate

$$y_1 - \hat{\delta}_{22}z_2 = \gamma_{12}y_2 + \delta_{11}z_1 + \delta_{13}z_3 + error$$

by 2SLS using  $(z_1, z_2, z_3)$  as instruments. Since  $\hat{\delta}_{22} \xrightarrow{P} \delta_{12}$  when  $\delta_{12} = \delta_{22} \neq 0$ , this last step produces consistent estimators of  $\gamma_{12}$ ,  $\delta_{11}$ , and  $\delta_{13}$ . Unfortunately, the usual 2SLS standard errors obtained from the final estimation would not be valid because of the preliminary estimation of  $\delta_{22}$ .

It is easier to use a system procedure when cross equation restrictions are present because the asymptotic variance can be obtained directly. We can always rewrite the system in a linear form with the restrictions imposed. For this example, one way to do so is to write the system as

$$\begin{pmatrix} y_1 \\ y_2 \end{pmatrix} = \begin{pmatrix} y_2 & z_1 & z_2 & z_3 & 0 & 0 \\ 0 & 0 & z_2 & 0 & y_1 & z_1 \end{pmatrix} \boldsymbol{\beta} + \begin{pmatrix} u_1 \\ u_2 \end{pmatrix}$$
(9.34)

where  $\beta = (\gamma_{12}, \delta_{11}, \delta_{12}, \delta_{13}, \gamma_{21}, \delta_{21})'$ . The parameter  $\delta_{22}$  does not show up in  $\beta$  because we have imposed the restriction  $\delta_{12} = \delta_{22}$  by appropriate choice of the matrix of explanatory variables.

The matrix of instruments is  $I_2 \otimes z$ , meaning that we just use all exogenous variables as instruments in each equation. Since  $I_2 \otimes z$  has six columns, the order condition is exactly satisfied (there are six elements of  $\beta$ ), and we have already seen when the rank condition holds. The system can be consistently estimated using GMM or 3SLS.

{240}------------------------------------------------