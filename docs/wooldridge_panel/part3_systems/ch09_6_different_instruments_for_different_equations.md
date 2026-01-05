# Different Instruments for Different Equations

> Pages: 250-252

There are general classes of SEMs where the same instruments cannot be used for every equation. We already encountered one such example, the fully recursive system. Another general class of models is SEMs where, in addition to simultaneous determination of some variables, some equations contain variables that are endogenous as a result of omitted variables or measurement error.

As an example, reconsider the labor supply and wage offer equations (9.28) and (9.62), respectively. On the one hand, in the supply function it is not unreasonable to assume that variables other than  $\log(wage)$  are uncorrelated with  $u_1$ . On the other hand, ability is a variable omitted from the  $\log(wage)$  equation, and so *educ* might be correlated with  $u_2$ . This is an omitted variable, not a simultaneity, issue, but the statistical problem is the same: correlation between the error and an explanatory variable.


{251}------------------------------------------------

Equation (9.28) is still identified as it was before, because educ is exogenous in equation (9.28). What about equation (9.62)? It satisfies the order condition because we have excluded four exogenous variables from equation (9.62): age, kidslt6, kidsge6, and nwifeinc. How can we analyze the rank condition for this equation? We need to add to the system the linear projection of educ on all exogenous variables:

$$educ = \delta_{30} + \delta_{31}exper + \delta_{32}exper^{2} + \delta_{33}age$$

$$+ \delta_{34}kidslt6 + \delta_{35}kidsge6 + \delta_{36}nwifeinc + u_{3}$$

$$(9.64)$$

Provided the variables other than exper and exper<sup>2</sup> are sufficiently partially correlated with educ, the logðwageÞ equation is identified. However, the 2SLS estimators might be poorly behaved if the instruments are not very good. If possible, we would add other exogenous factors to equation (9.64) that are partially correlated with educ, such as mother's and father's education. In a system procedure, because we have assumed that educ is uncorrelated with u1, educ can, and should, be included in the list of instruments for estimating equation (9.28).

This example shows that having different instruments for different equations changes nothing for single-equation analysis: we simply determine the valid list of instruments for the endogenous variables in the equation of interest and then estimate the equations separately by 2SLS. Instruments may be required to deal with simultaneity, omitted variables, or measurement error, in any combination.

Estimation is more complicated for system methods. First, if 3SLS is to be used, then the GMM 3SLS version must be used to produce consistent estimators of any equation; the more traditional 3SLS estimator discussed in Section 8.3.5 is generally valid only when all instruments are uncorrelated with all errors. When we have different instruments for different equations, the instrument matrix has the form in equation (8.15).

There is a more subtle issue that arises in system analysis with different instruments for different equations. While it is still popular to use 3SLS methods for such problems, it turns out that the key assumption that makes 3SLS the efficient GMM estimator, Assumption SIV.5, is often violated. In such cases the GMM estimator with general weighting matrix enhances asymptotic efficiency and simplifies inference.

As a simple example, consider a two-equation system

$$y_1 = \delta_{10} + \gamma_{12}y_2 + \delta_{11}z_1 + u_1 \tag{9.65}$$

$$y_2 = \delta_{20} + \gamma_{21}y_1 + \delta_{22}z_2 + \delta_{23}z_3 + u_2 \tag{9.66}$$

where ðu1; u2Þ has mean zero and variance matrix S. Suppose that z1, z2, and z<sup>3</sup> are uncorrelated with u<sup>2</sup> but we can only assume that z<sup>1</sup> and z<sup>3</sup> are uncorrelated with u1. 

{252}------------------------------------------------

In other words,  $z_2$  is not exogenous in equation (9.65). Each equation is still identified by the order condition, and we just assume that the rank conditions also hold. The instruments for equation (9.65) are  $(1, z_1, z_3)$ , and the instruments for equation (9.66) are  $(1, z_1, z_2, z_3)$ . Write these as  $\mathbf{z}_1 \equiv (1, z_1, z_3)$  and  $\mathbf{z}_2 \equiv (1, z_1, z_2, z_3)$ . Assumption SIV.5 requires the following three conditions:

$$E(u_1^2 \mathbf{z}_1' \mathbf{z}_1) = \sigma_1^2 E(\mathbf{z}_1' \mathbf{z}_1) \tag{9.67}$$

$$E(u_2^2 \mathbf{z}_2' \mathbf{z}_2) = \sigma_2^2 E(\mathbf{z}_2' \mathbf{z}_2) \tag{9.68}$$

$$E(u_1u_2\mathbf{z}_1'\mathbf{z}_2) = \sigma_{12}E(\mathbf{z}_1'\mathbf{z}_2) \tag{9.69}$$

The first two conditions hold if  $E(u_1|\mathbf{z}_1) = E(u_2|\mathbf{z}_2) = 0$  and  $Var(u_1|\mathbf{z}_1) = \sigma_1^2$ ,  $Var(u_2|\mathbf{z}_2) = \sigma_2^2$ . These are standard zero conditional mean and homoskedasticity assumptions. The potential problem comes with condition (9.69). Since  $u_1$  is correlated with one of the elements in  $\mathbf{z}_2$ , we can hardly just assume condition (9.69). Generally, there is no conditioning argument that implies condition (9.69). One case where condition (9.69) holds is if  $E(u_2|u_1,z_1,z_2,z_3)=0$ , which implies that  $u_2$  and  $u_1$  are uncorrelated. The left-hand side of condition (9.69) is also easily shown to equal zero. But 3SLS with  $\sigma_{12}=0$  imposed is just 2SLS equation by equation. If  $u_1$  and  $u_2$  are correlated, we should not expect condition (9.69) to hold, and therefore the general minimum chi-square estimator should be used for estimation and inference.

Wooldridge (1996) provides a general discussion and contains other examples of cases in which Assumption SIV.5 can and cannot be expected to hold. Whenever a system contains linear projections for nonlinear functions of endogenous variables, we should expect Assumption SIV.5 to fail.