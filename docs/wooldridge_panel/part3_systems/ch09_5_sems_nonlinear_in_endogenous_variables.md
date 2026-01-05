# SEMs Nonlinear in Endogenous Variables

> Pages: 243-250

We now study models that are nonlinear in some endogenous variables. While the general estimation methods we have covered are still applicable, identification and choice of instruments require special attention.

#### 9.5.1 Identification

The issues that arise in identifying models nonlinear in endogenous variables are most easily illustrated with a simple example. Suppose that supply and demand are

{244}------------------------------------------------

given by

$$\log(q) = \gamma_{12} \log(p) + \gamma_{13} [\log(p)]^2 + \delta_{11} z_1 + u_1$$
(9.46)

$$\log(q) = \gamma_{22} \log(p) + \delta_{22} z_2 + u_2 \tag{9.47}$$

$$\mathbf{E}(u_1 \mid \mathbf{z}) = \mathbf{E}(u_2 \mid \mathbf{z}) = 0 \tag{9.48}$$

where the first equation is the supply equation, the second equation is the demand equation, and the equilibrium condition that supply equals demand has been imposed. For simplicity, we do not include an intercept in either equation, but no important conclusions hinge on this omission. The exogenous variable  $z_1$  shifts the supply function but not the demand function;  $z_2$  shifts the demand function but not the supply function. The vector of exogenous variables appearing somewhere in the system is  $\mathbf{z} = (z_1, z_2)$ .

It is important to understand why equations (9.46) and (9.47) constitute a "non-linear" system. This system is still linear in *parameters*, which is important because it means that the IV procedures we have learned up to this point are still applicable. Further, it is *not* the presence of the logarithmic transformations of q and p that makes the system nonlinear. In fact, if we set  $\gamma_{13} = 0$ , then the model is linear for the purposes of identification and estimation: defining  $y_1 \equiv \log(q)$  and  $y_2 \equiv \log(p)$ , we can write equations (9.46) and (9.47) as a standard two-equation system.

When we include  $[\log(p)]^2$  we have the model

$$y_1 = \gamma_{12}y_2 + \gamma_{13}y_2^2 + \delta_{11}z_1 + u_1 \tag{9.49}$$

$$y_1 = \gamma_{22}y_2 + \delta_{22}z_2 + u_2 \tag{9.50}$$

With this system there is no way to define two endogenous variables such that the system is a two-equation system in two endogenous variables. The presence of  $y_2^2$  in equation (9.49) makes this model different from those we have studied up until now. We say that this is a system **nonlinear in endogenous variables**. What this statement really means is that, while the system is still linear in parameters, identification needs to be treated differently.

If we used equations (9.49) and (9.50) to obtain  $y_2$  as a function of the  $z_1, z_2, u_1, u_2$ , and the parameters, the result would not be linear in  $\mathbf{z}$  and  $\mathbf{u}$ . In this particular case we can find the solution for  $y_2$  using the quadratic formula (assuming a real solution exists). However,  $\mathrm{E}(y_2 \mid \mathbf{z})$  would not be linear in  $\mathbf{z}$  unless  $\gamma_{13} = 0$ , and  $\mathrm{E}(y_2^2 \mid \mathbf{z})$  would not be linear in  $\mathbf{z}$  regardless of the value of  $\gamma_{13}$ . These observations have important implications for identification of equation (9.49) and for choosing instruments.

{245}------------------------------------------------

Before considering equations (9.49) and (9.50) further, consider a second example where closed form expressions for the endogenous variables in terms of the exogenous variables and structural errors do not even exist. Suppose that a system describing crime rates in terms of law enforcement spending is

$$crime = \gamma_{12} \log(spending) + \mathbf{z}_{(1)}\boldsymbol{\delta}_{(1)} + u_1 \tag{9.51}$$

$$spending = \gamma_{21}crime + \gamma_{22}crime^2 + \mathbf{z}_{(2)}\boldsymbol{\delta}_{(2)} + u_2$$

$$(9.52)$$

where the errors have zero mean given z. Here, we cannot solve for either crime or spending (or any other transformation of them) in terms of z, u1, u2, and the parameters. And there is no way to define y<sup>1</sup> and y<sup>2</sup> to yield a linear SEM in two endogenous variables. The model is still linear in parameters, but Eðcrime j zÞ, E½logðspendingÞ j z, and Eðspending j zÞ are not linear in z (nor can we find closed forms for these expectations).

One possible approach to identification in nonlinear SEMs is to ignore the fact that the same endogenous variables show up differently in different equations. In the supply and demand example, define y<sup>3</sup> 1 y<sup>2</sup> <sup>2</sup> and rewrite equation (9.49) as

$$y_1 = \gamma_{12}y_2 + \gamma_{13}y_3 + \delta_{11}z_1 + u_1 \tag{9.53}$$

Or, in equations (9.51) and (9.52) define y<sup>1</sup> ¼ crime, y<sup>2</sup> ¼ spending, y<sup>3</sup> ¼ logðspendingÞ, and y<sup>4</sup> ¼ crime2, and write

$$y_1 = \gamma_{12}y_3 + \mathbf{z}_{(1)}\boldsymbol{\delta}_{(1)} + u_1 \tag{9.54}$$

$$y_2 = \gamma_{21}y_1 + \gamma_{22}y_4 + \mathbf{z}_{(2)}\boldsymbol{\delta}_{(2)} + u_2 \tag{9.55}$$

Defining nonlinear functions of endogenous variables as new endogenous variables turns out to work fairly generally, provided we apply the rank and order conditions properly. The key question is, What kinds of equations do we add to the system for the newly defined endogenous variables?

If we add linear projections of the newly defined endogenous variables in terms of the original exogenous variables appearing somewhere in the system—that is, the linear projection onto z—then we are being much too restrictive. For example, suppose to equations (9.53) and (9.50) we add the linear equation

$$y_3 = \pi_{31}z_1 + \pi_{32}z_2 + v_3 \tag{9.56}$$

where, by definition, Eðz1v3Þ ¼ Eðz2v3Þ ¼ 0. With equation (9.56) to round out the system, the order condition for identification of equation (9.53) clearly fails: we have two endogenous variables in equation (9.53) but only one excluded exogenous variable, z2.

{246}------------------------------------------------

The conclusion that equation (9.53) is not identified is too pessimistic. There are many other possible instruments available for  $y_2^2$ . Because  $E(y_2^2 | \mathbf{z})$  is not linear in  $z_1$  and  $z_2$  (even if  $\gamma_{13} = 0$ ), other functions of  $z_1$  and  $z_2$  will appear in a linear projection involving  $y_2^2$  as the dependent variable. To see what the most useful of these are likely to be, suppose that the structural system actually is linear, so that  $\gamma_{13} = 0$ . Then  $y_2 = \pi_{21}z_1 + \pi_{22}z_2 + v_2$ , where  $v_2$  is a linear combination of  $u_1$  and  $u_2$ . Squaring this reduced form and using  $E(v_2 | \mathbf{z}) = 0$  gives

$$E(y_2^2 | \mathbf{z}) = \pi_{21}^2 z_1^2 + \pi_{22}^2 z_2^2 + 2\pi_{21}\pi_{22}z_1 z_2 + E(v_2^2 | \mathbf{z})$$
(9.57)

If  $E(v_2^2 | \mathbf{z})$  is constant, an assumption that holds under homoskedasticity of the structural errors, then equation (9.57) shows that  $y_2^2$  is correlated with  $z_1^2$ ,  $z_2^2$ , and  $z_1z_2$ , which makes these functions natural instruments for  $y_2^2$ . The only case where no functions of  $\mathbf{z}$  are correlated with  $y_2^2$  occurs when both  $\pi_{21}$  and  $\pi_{22}$  equal zero, in which case the linear version of equation (9.49) (with  $y_{13} = 0$ ) is also unidentified.

Because we derived equation (9.57) under the restrictive assumptions  $\gamma_{13} = 0$  and homoskedasticity of  $v_2$ , we would not want our linear projection for  $y_2^2$  to omit the exogenous variables that originally appear in the system. In practice, we would augment equations (9.53) and (9.50) with the linear projection

$$y_3 = \pi_{31}z_1 + \pi_{32}z_2 + \pi_{33}z_1^2 + \pi_{34}z_2^2 + \pi_{35}z_1z_2 + v_3$$
(9.58)

where  $v_3$  is, by definition, uncorrelated with  $z_1$ ,  $z_2$ ,  $z_1^2$ ,  $z_2^2$ , and  $z_1z_2$ . The system (9.53), (9.50), and (9.58) can now be studied using the usual rank condition.

Adding equation (9.58) to the original system and then studying the rank condition of the first two equations is equivalent to studying the rank condition in the smaller system (9.53) and (9.50). What we mean by this statement is that we do not explicitly add an equation for  $y_3 = y_2^2$ , but we do include  $y_3$  in equation (9.53). Therefore, when applying the rank condition to equation (9.53), we use G = 2 (not G = 3). The reason this approach is the same as studying the rank condition in the three-equation system (9.53), (9.50), and (9.58) is that adding the third equation increases the rank of  $\mathbf{R}_1\mathbf{B}$  by one whenever at least one additional nonlinear function of  $\mathbf{z}$  appears in equation (9.58). (The functions  $z_1^2$ ,  $z_2^2$ , and  $z_1z_2$  appear nowhere else in the system.)

As a general approach to identification in models where the nonlinear functions of the endogenous variables depend only on a single endogenous variable—such as the two examples that we have already covered—Fisher (1965) argues that the following method is sufficient for identification:

1. Relabel the nonredundant functions of the endogenous variables to be new endogenous variables, as in equation (9.53) or (9.54) and equation (9.55).

{247}------------------------------------------------

2. Apply the rank condition to the original system *without* increasing the number of equations. If the equation of interest satisfies the rank condition, then it is identified.

The proof that this method works is complicated, and it requires more assumptions than we have made (such as  $\mathbf{u}$  being *independent* of  $\mathbf{z}$ ). Intuitively, we can expect each additional nonlinear function of the endogenous variables to have a linear projection that depends on new functions of the exogenous variables. Each time we add another function of an endogenous variable, it effectively comes with its own instruments.

Fisher's method can be expected to work in all but the most pathological cases. One case where it does not work is if  $E(v_2^2 | \mathbf{z})$  in equation (9.57) is heteroskedastic in such a way as to cancel out the squares and cross product terms in  $z_1$  and  $z_2$ ; then  $E(y_2^2 | \mathbf{z})$  would be constant. Such unfortunate coincidences are not practically important.

It is tempting to think that Fisher's rank condition is also necessary for identification, but this is not the case. To see why, consider the two-equation system

$$y_1 = \gamma_{12}y_2 + \gamma_{13}y_2^2 + \delta_{11}z_1 + \delta_{12}z_2 + u_1 \tag{9.59}$$

$$y_2 = y_{21}y_1 + \delta_{21}z_1 + u_2 \tag{9.60}$$

The first equation cleary fails the modified rank condition because it fails the order condition: there are no restrictions on the first equation except the normalization restriction. However, if  $\gamma_{13} \neq 0$  and  $\gamma_{21} \neq 0$ , then  $E(y_2 | \mathbf{z})$  is a nonlinear function of  $\mathbf{z}$  (which we cannot obtain in closed form). The result is that functions such as  $z_1^2$ ,  $z_2^2$ , and  $z_1z_2$  (and others) will appear in the linear projections of  $y_2$  and  $y_2^2$  even after  $z_1$  and  $z_2$  have been included, and these can then be used as instruments for  $y_2$  and  $y_2^2$ . But if  $\gamma_{13} = 0$ , the first equation cannot be identified by adding nonlinear functions of  $z_1$  and  $z_2$  to the instrument list: the linear projection of  $y_2$  on  $z_1$ ,  $z_2$ , and any function of  $(z_1, z_2)$  will only depend on  $z_1$  and  $z_2$ .

Equation (9.59) is an example of a **poorly identified model** because, when it is identified, it is **identified due to a nonlinearity** ( $\gamma_{13} \neq 0$  in this case). Such identification is especially tenuous because the hypothesis  $H_0$ :  $\gamma_{13} = 0$  cannot be tested by estimating the structural equation (since the structural equation is not identified when  $H_0$  holds).

There are other models where identification can be verified using reasoning similar to that used in the labor supply example. Models with interactions between exogenous variables and endogenous variables can be shown to be identified when the model without the interactions is identified (see Example 6.2 and Problem 9.6). Models with interactions among endogenous variables are also fairly easy to handle. Generally, it is good practice to check whether the most general *linear* version of the model would be identified. If it is, then the nonlinear version of the model is probably

{248}------------------------------------------------

identified. We saw this result in equation (9.46): if this equation is identified when g<sup>13</sup> ¼ 0, then it is identified for any value of g13. If the most general linear version of a nonlinear model is not identified, we should be very wary about proceeding, since identification hinges on the presence of nonlinearities that we usually will not be able to test.

# 9.5.2 Estimation

In practice, it is difficult to know which additional functions we should add to the instrument list for nonlinear SEMs. Naturally, we must always include the exogenous variables appearing somewhere in the system instruments in every equation. After that, the choice is somewhat arbitrary, although the functional forms appearing in the structural equations can be helpful.

A general approach is to always use some squares and cross products of the exogenous variables appearing somewhere in the system. If something like exper<sup>2</sup> appears in the system, additional terms such as exper<sup>3</sup> and exper<sup>4</sup> would be added to the instrument list.

Once we decide on a set of instruments, any equation in a nonlinear SEM can be estimated by 2SLS. Because each equation satisfies the assumptions of single-equation analysis, we can use everything we have learned up to now for inference and specification testing for 2SLS. A system method can also be used, where linear projections for the functions of endogenous variables are explicitly added to the system. Then, all exogenous variables included in these linear projections can be used as the instruments for every equation. The minimum chi-square estimator is generally more appropriate than 3SLS because the homoskedasticity assumption will rarely be satisfied in the linear projections.

It is important to apply the instrumental variables procedures directly to the structural equation or equations. In other words, we should directly use the formulas for 2SLS, 3SLS, or GMM. Trying to mimic 2SLS or 3SLS by substituting fitted values for some of the endogenous variables inside the nonlinear functions is usually a mistake: neither the conditional expectation nor the linear projection operator passes through nonlinear functions, and so such attempts rarely produce consistent estimators in nonlinear systems.

Example 9.6 (Nonlinear Labor Supply Function): We add ½logðwageÞ<sup>2</sup> to the labor supply function in Example 9.5:

$$hours = \gamma_{12} \log(wage) + \gamma_{13} [\log(wage)]^2 + \delta_{10} + \delta_{11} educ + \delta_{12} age$$
$$+ \delta_{13} kidslt6 + \delta_{14} kidsge6 + \delta_{15} nwifeinc + u_1$$
(9.61)

$$\log(wage) = \delta_{20} + \delta_{21}educ + \delta_{22}exper + \delta_{23}exper^{2} + u_{2}$$
(9.62)

{249}------------------------------------------------

where we have dropped *hours* from the wage offer function because it was insignificant in Example 9.5. The natural assumptions in this system are  $E(u_1|\mathbf{z}) = E(u_2|\mathbf{z}) = 0$ , where  $\mathbf{z}$  contains all variables other than *hours* and  $\log(wage)$ .

There are many possibilities as additional instruments for  $[\log(wage)]^2$ . Here, we add three quadratic terms to the list— $age^2$ ,  $educ^2$ , and  $nwifeinc^2$ —and we estimate equation (9.61) by 2SLS. We obtain  $\hat{\gamma}_{12} = 1,873.62$  (se = 635.99) and  $\hat{\gamma}_{13} = -437.29$  (se = 350.08). The t statistic on  $[\log(wage)]^2$  is about -1.25, so we would be justified in dropping it from the labor supply function. Regressing the 2SLS residuals  $\hat{u}_1$  on all variables used as instruments in the supply equation gives R-squared = .0061, and so the N-R-squared statistic is 2.61. With a  $\chi_3^2$  distribution this gives p-value = .456. Thus, we fail to reject the overidentifying restrictions.

In the previous example we may be tempted to estimate the labor supply function using a two-step procedure that appears to mimic 2SLS:

- 1. Regress log(wage) on all exogenous variables appearing in the system and obtain the predicted values. For emphasis, call these  $\hat{y}_2$ .
- 2. Estimate the labor supply function from the OLS regression *hours* on 1,  $\hat{y}_2$ ,  $(\hat{y}_2)^2$ , *educ*,..., *nwifeinc*.

This two-step procedure is *not* the same as estimating equation (9.61) by 2SLS, and, except in special circumstances, it does *not* produce consistent estimators of the structural parameters. The regression in step 2 is an example of what is sometimes called a **forbidden regression**, a phrase that describes replacing a nonlinear function of an endogenous explanatory variable with the same nonlinear function of fitted values from a first-stage estimation. In plugging fitted values into equation (9.61), our mistake is in thinking that the linear projection of the square is the square of the linear projection. What the 2SLS estimator does in the first stage is project each of  $y_2$  and  $y_2^2$  onto the original exogenous variables and the additional nonlinear functions of these that we have chosen. The fitted values from the reduced form regression for  $y_2$ , say  $\hat{y}_3$ , are not the same as the squared fitted values from the reduced form regression for  $y_2$ , ( $\hat{y}_2$ )<sup>2</sup>. This distinction is the difference between a consistent estimator and an inconsistent estimator.

If we apply the forbidden regression to equation (9.61), some of the estimates are very different from the 2SLS estimates. For example, the coefficient on *educ*, when equation (9.61) is properly estimated by 2SLS, is about -87.85 with a t statistic of -1.32. The forbidden regression gives a coefficient on *educ* of about -176.68 with a t statistic of -5.36. Unfortunately, the t statistic from the forbidden regression is generally invalid, even asymptotically. (The forbidden regression will produce consistent estimators in the special case  $\gamma_{13} = 0$ , if  $E(u_1 | \mathbf{z}) = 0$ ; see Problem 9.12.)

{250}------------------------------------------------

Many more functions of the exogenous variables could be added to the instrument list in estimating the labor supply function. From Chapter 8, we know that efficiency of GMM never falls by adding more nonlinear functions of the exogenous variables to the instrument list (even under the homoskedasticity assumption). This statement is true whether we use a single-equation or system method. Unfortunately, the fact that we do no worse asymptotically by adding instruments is of limited practical help, since we do not want to use too many instruments for a given data set. In Example 9.6, rather than using a long list of additional nonlinear functions, we might use  $(\hat{y}_2)^2$  as a single IV for  $y_2^2$ . (This method is not the same as the forbidden regression!) If it happens that  $\gamma_{13} = 0$  and the structural errors are homoskedastic, this would be the optimal IV. (See Problem 9.12.)

A general system linear in parameters can be written as

$$y_{1} = \mathbf{q}_{1}(\mathbf{y}, \mathbf{z})\boldsymbol{\beta}_{1} + u_{1}$$

$$\vdots$$

$$y_{G} = \mathbf{q}_{G}(\mathbf{y}, \mathbf{z})\boldsymbol{\beta}_{G} + u_{G}$$

$$(9.63)$$

where  $E(u_g | \mathbf{z}) = 0$ , g = 1, 2, ..., G. Among other things this system allows for complicated interactions among endogenous and exogenous variables. We will not give a general analysis of such systems because identification and choice of instruments are too abstract to be very useful. Either single-equation or system methods can be used for estimation.