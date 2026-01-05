# Subtleties Concerning Identification and Efficiency in Linear Systems

> Pages: 242-243

So far we have discussed identification and estimation under the assumption that each exogenous variable appearing in the system,  $z_j$ , is *uncorrelated* with each structural error,  $u_g$ . It is important to assume only zero correlation in the general treatment because we often add a reduced form equation for an endogenous variable to a structural system, and zero correlation is all we should impose in linear reduced forms.

For entirely structural systems, it is often natural to assume that the structural errors satisfy the zero conditional mean assumption

$$E(u_q | \mathbf{z}) = 0, \qquad g = 1, 2, \dots, G$$
 (9.41)

In addition to giving the parameters in the structural equations the appropriate partial effect interpretations, assumption (9.41) has some interesting statistical implications: any function of  $\mathbf{z}$  is uncorrelated with each error  $u_g$ . Therefore, in the labor supply example (9.28),  $age^2$ ,  $\log(age)$ ,  $educ \cdot exper$ , and so on (there are too many functions to list) are all uncorrelated with  $u_1$  and  $u_2$ . Realizing this fact, we might ask, Why not use nonlinear functions of  $\mathbf{z}$  as additional instruments in estimation?

We need to break the answer to this question into two parts. The first concerns identification, and the second concerns efficiency. For identification, the bottom line is this: adding nonlinear functions of **z** to the instrument list *cannot* help with identification in linear systems. You were asked to show this generally in Problem 8.4, but the main points can be illustrated with a simple model:

$$y_1 = \gamma_{12}y_2 + \delta_{11}z_1 + \delta_{12}z_2 + u_1 \tag{9.42}$$

$$y_2 = \gamma_{21}y_1 + \delta_{21}z_1 + u_2 \tag{9.43}$$

$$\mathbf{E}(u_1|\mathbf{z}) = \mathbf{E}(u_2|\mathbf{z}) = 0 \tag{9.44}$$

From the order condition in Section 9.2.2, equation (9.42) is not identified, and equation (9.43) is identified if and only if  $\delta_{12} \neq 0$ . Knowing properties of conditional expectations, we might try something clever to identify equation (9.42): since, say,  $z_1^2$  is uncorrelated with  $u_1$  under assumption (9.41), and  $z_1^2$  would appear to be correlated with  $y_2$ , we can use it as an instrument for  $y_2$  in equation (9.42). Under this reasoning, we would have enough instruments— $z_1, z_2, z_1^2$ —to identify equation (9.42). In fact, any number of functions of  $z_1$  and  $z_2$  can be added to the instrument list.

The fact that this argument is faulty is fortunate because our identification analysis in Section 9.2.2 says that equation (9.42) is not identified. In this example it is clear that  $z_1^2$  cannot appear in the reduced form for  $y_2$  because  $z_1^2$  appears nowhere in the

{243}------------------------------------------------

system. Technically, because  $E(y_2 | \mathbf{z})$  is linear in  $z_1$  and  $z_2$  under assumption (9.44), the linear projection of  $y_2$  onto  $(z_1, z_2, z_1^2)$  does not depend on  $z_1^2$ :

$$L(y_2 | z_1, z_2, z_1^2) = L(y_2 | z_1, z_2) = \pi_{21} z_1 + \pi_{22} z_2$$
(9.45)

In other words, there is no partial correlation between  $y_2$  and  $z_1^2$  once  $z_1$  and  $z_2$  are included in the projection.

The zero conditional mean assumptions (9.41) can have some relevance for choosing an efficient estimator, although not always. If assumption (9.41) holds and  $Var(\mathbf{u} \mid \mathbf{z}) = Var(\mathbf{u}) = \mathbf{\Sigma}$ , 3SLS using instruments  $\mathbf{z}$  for each equation is the asymptotically efficient estimator that uses the orthogonality conditions in assumption (9.41); this conclusion follows from Theorem 8.5. In other words, if  $Var(\mathbf{u} \mid \mathbf{z})$  is constant, it does not help to expand the instrument list beyond the functions of the exogenous variables actually appearing in the system.

However, if assumption (9.41) holds but  $Var(\mathbf{u} \mid \mathbf{z})$  is not constant, we can do better (asymptotically) than 3SLS. If  $\mathbf{h}(\mathbf{z})$  is some additional functions of the exogenous variables, the minimum chi-square estimator using  $[\mathbf{z}, \mathbf{h}(\mathbf{z})]$  as instruments in each equation is, generally, more efficient than 3SLS or minimum chi-square using only  $\mathbf{z}$  as IVs. This result was discovered independently by Hansen (1982) and White (1982b), and it follows from the discussion in Section 8.6. Expanding the IV list to arbitrary functions of  $\mathbf{z}$  and applying full GMM is not used very much in practice: it is usually not clear how to choose  $\mathbf{h}(\mathbf{z})$ , and, if we use too many additional instruments, the finite sample properties of the GMM estimator can be poor, as we discussed in Section 8.6.

For SEMs linear in the parameters but nonlinear in endogenous variables (in a sense to be made precise), adding nonlinear functions of the exogenous variables to the instruments not only is desirable, but is often needed to achieve identification. We turn to this topic next.