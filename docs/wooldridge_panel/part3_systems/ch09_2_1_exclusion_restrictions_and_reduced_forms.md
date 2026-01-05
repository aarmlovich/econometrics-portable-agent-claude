# Exclusion Restrictions and Reduced Forms

> Pages: 224-228

Write a system of linear simultaneous equations for the population as

$$y_{1} = \mathbf{y}_{(1)} \boldsymbol{\gamma}_{(1)} + \mathbf{z}_{(1)} \boldsymbol{\delta}_{(1)} + u_{1}$$

$$\vdots$$

$$y_{G} = \mathbf{y}_{(G)} \boldsymbol{\gamma}_{(G)} + \mathbf{z}_{(G)} \boldsymbol{\delta}_{(G)} + u_{G}$$

$$(9.1)$$

where  $\mathbf{y}_{(h)}$  is  $1 \times G_h$ ,  $\gamma_{(h)}$  is  $G_h \times 1$ ,  $\mathbf{z}_{(h)}$  is  $1 \times M_h$ , and  $\delta_{(h)}$  is  $M_h \times 1$ ,  $h = 1, 2, \ldots, G$ . These are **structural equations** for the **endogenous variables**  $y_1, y_2, \ldots, y_G$ . We will assume that, if the system (9.1) represents a true simultaneous equations model, then equilibrium conditions have been imposed. Hopefully, each equation is autonomous, but, of course, they do not need to be for the statistical analysis.

The vector  $\mathbf{y}_{(h)}$  denotes endogenous variables that appear on the right-hand side of the *h*th structural equation. By convention,  $\mathbf{y}_{(h)}$  can contain any of the endogenous variables  $y_1, y_2, \ldots, y_G$  except for  $y_h$ . The variables in  $\mathbf{z}_{(h)}$  are the **exogenous variables** appearing in equation *h*. Usually there is some overlap in the exogenous variables

{225}------------------------------------------------

across different equations; for example, except in special circumstances each zðh<sup>Þ</sup> would contain unity to allow for nonzero intercepts. The restrictions imposed in system (9.1) are called exclusion restrictions because certain endogenous and exogenous variables are excluded from some equations.

The 1 M vector of all exogenous variables z is assumed to satisfy

$$E(\mathbf{z}'u_g) = \mathbf{0}, \qquad g = 1, 2, \dots, G \tag{9.2}$$

When all of the equations in system (9.1) are truly structural, we are usually willing to assume

$$E(u_g | \mathbf{z}) = 0, \qquad g = 1, 2, \dots, G$$
 (9.3)

However, we know from Chapters 5 and 8 that assumption (9.2) is sufficient for consistent estimation. Sometimes, especially in omitted variables and measurement error applications, one or more of the equations in system (9.1) will simply represent a linear projection onto exogenous variables, as in Example 8.2. It is for this reason that we use assumption (9.2) for most of our identification and estimation analysis. We assume throughout that Eðz<sup>0</sup> zÞ is nonsingular, so that there are no exact linear dependencies among the exogenous variables in the population.

Assumption (9.2) implies that the exogenous variables appearing anywhere in the system are orthogonal to all the structural errors. If some elements in, say, zð1Þ, do not appear in the second equation, then we are explicitly assuming that they do not enter the structural equation for y2. If there are no reasonable exclusion restrictions in an SEM, it may be that the system fails the autonomy requirement.

Generally, in the system (9.1), the error ug in equation g will be correlated with yðg<sup>Þ</sup> (we show this correlation explicitly later), and so OLS and GLS will be inconsistent. Nevertheless, under certain identification assumptions, we can estimate this system using the instrumental variables procedures covered in Chapter 8.

In addition to the exclusion restrictions in system (9.1), another possible source of identifying information is on the G G variance matrix S 1VarðuÞ. For now, S is unrestricted and therefore contains no identifying information.

To motivate the general analysis, consider specific labor supply and demand functions for some population:

$$h^{s}(\omega) = \gamma_{1} \log(\omega) + \mathbf{z}_{(1)} \boldsymbol{\delta}_{(1)} + u_{1}$$
$$h^{d}(\omega) = \gamma_{2} \log(\omega) + \mathbf{z}_{(2)} \boldsymbol{\delta}_{(2)} + u_{2}$$

where w is the dummy argument in the labor supply and labor demand functions. We assume that observed hours, h, and observed wage, w, equate supply and demand:

{226}------------------------------------------------

$$h = h^s(w) = h^d(w)$$

The variables in  $\mathbf{z}_{(1)}$  shift the labor supply curve, and  $\mathbf{z}_{(2)}$  contains labor demand shifters. By defining  $y_1 = h$  and  $y_2 = \log(w)$  we can write the equations in equilibrium as a linear simultaneous equations model:

$$y_1 = \gamma_1 y_2 + \mathbf{z}_{(1)} \boldsymbol{\delta}_{(1)} + u_1 \tag{9.4}$$

$$y_1 = y_2 y_2 + \mathbf{z}_{(2)} \boldsymbol{\delta}_{(2)} + u_2 \tag{9.5}$$

Nothing about the general system (9.1) rules out having the same variable on the left-hand side of more than one equation.

What is needed to identify the parameters in, say, the supply curve? Intuitively, since we observe only the equilibrium quantities of hours and wages, we cannot distinguish the supply function from the demand function if  $\mathbf{z}_{(1)}$  and  $\mathbf{z}_{(2)}$  contain exactly the same elements. If, however,  $\mathbf{z}_{(2)}$  contains an element *not* in  $\mathbf{z}_{(1)}$ —that is, if there is some factor that exogenously shifts the demand curve but not the supply curve—then we can hope to estimate the parameters of the supply curve. To identify the demand curve, we need at least one element in  $\mathbf{z}_{(1)}$  that is not also in  $\mathbf{z}_{(2)}$ .

To formally study identification, assume that  $\gamma_1 \neq \gamma_2$ ; this assumption just means that the supply and demand curves have different slopes. Subtracting equation (9.5) from equation (9.4), dividing by  $\gamma_2 - \gamma_1$ , and rearranging gives

$$y_2 = \mathbf{z}_{(1)}\pi_{21} + \mathbf{z}_{(2)}\pi_{22} + v_2 \tag{9.6}$$

where  $\pi_{21} \equiv \delta_{(1)}/(\gamma_2 - \gamma_1)$ ,  $\pi_{22} = -\delta_{(2)}/(\gamma_2 - \gamma_1)$ , and  $v_2 \equiv (u_1 - u_2)/(\gamma_2 - \gamma_1)$ . This is the **reduced form** for  $y_2$  because it expresses  $y_2$  as a linear function of all of the exogenous variables and an error  $v_2$  which, by assumption (9.2), is orthogonal to all exogenous variables:  $E(\mathbf{z}'v_2) = \mathbf{0}$ . Importantly, the reduced form for  $y_2$  is obtained from the two structural equations (9.4) and (9.5).

Given equation (9.4) and the reduced form (9.6), we can now use the identification condition from Chapter 5 for a linear model with a single right-hand-side endogenous variable. This condition is easy to state: the reduced form for  $y_2$  must contain at least one exogenous variable not also in equation (9.4). This means there must be at least one element of  $\mathbf{z}_{(2)}$  not in  $\mathbf{z}_{(1)}$  with coefficient in equation (9.6) different from zero. Now we use the structural equations. Because  $\pi_{22}$  is proportional to  $\delta_{(2)}$ , the condition is easily restated in terms of the *structural* parameters: in equation (9.5) at least one element of  $\mathbf{z}_{(2)}$  not in  $\mathbf{z}_{(1)}$  must have nonzero coefficient. In the supply and demand example, identification of the supply function requires at least one exogenous variable appearing in the demand function that does not also appear in the supply function; this conclusion corresponds exactly with our earlier intuition.

{227}------------------------------------------------

The condition for identifying equation (9.5) is just the mirror image: there must be at least one element of zð1<sup>Þ</sup> actually appearing in equation (9.4) that is not also an element of zð2Þ.

Example 9.1 (Labor Supply for Married Women): Consider labor supply and demand equations for married women, with the equilibrium condition imposed:

$$hours = \gamma_1 \log(wage) + \delta_{10} + \delta_{11}educ + \delta_{12}age + \delta_{13}kids + \delta_{14}othinc + u_1$$

$$hours = \gamma_2 \log(wage) + \delta_{20} + \delta_{21}educ + \delta_{22}exper + u_2$$

The supply equation is identified because, by assumption, exper appears in the demand function (assuming d<sup>22</sup> 00) but not in the supply equation. The assumption that past experience has no direct affect on labor supply can be questioned, but it has been used by labor economists. The demand equation is identified provided that at least one of the three variables age, kids, and othinc actually appears in the supply equation.

We now extend this analysis to the general system (9.1). For concreteness, we study identification of the first equation:

$$y_1 = \mathbf{y}_{(1)} \mathbf{y}_{(1)} + \mathbf{z}_{(1)} \boldsymbol{\delta}_{(1)} + u_1 = \mathbf{x}_{(1)} \boldsymbol{\beta}_{(1)} + u_1$$
(9.7)

where the notation used for the subscripts is needed to distinguish an equation with exclusion restrictions from a general equation that we will study in Section 9.2.2. Assuming that the reduced forms exist, write the reduced form for yð1<sup>Þ</sup> as

$$\mathbf{y}_{(1)} = \mathbf{z} \mathbf{\Pi}_{(1)} + \mathbf{v}_{(1)} \tag{9.8}$$

where E½z<sup>0</sup> vð<sup>1</sup>Þ ¼ 0. Further, define the M M<sup>1</sup> matrix selection matrix Sð1Þ, which consists of zeros and ones, such that zð1<sup>Þ</sup> ¼ zSð1Þ. The rank condition from Chapter 5, Assumption 2SLS.2b, can be stated as

$$\operatorname{rank} E[\mathbf{z}'\mathbf{x}_{(1)}] = K_1 \tag{9.9}$$

where K<sup>1</sup> 1 G<sup>1</sup> þ M1. But E½z<sup>0</sup> xð<sup>1</sup>Þ ¼ E½z<sup>0</sup> ðzPð1Þ; zSð<sup>1</sup>ÞÞ ¼ Eðz<sup>0</sup> zÞ½Pð1<sup>Þ</sup> j Sð<sup>1</sup>Þ. Since we always assume that Eðz<sup>0</sup> zÞ has full rank M, assumption (9.9) is the same as

$$rank[\mathbf{\Pi}_{(1)} | \mathbf{S}_{(1)}] = G_1 + M_1 \tag{9.10}$$

In other words, ½Pð1<sup>Þ</sup> j Sð<sup>1</sup>Þ must have full column rank. If the reduced form for yð1<sup>Þ</sup> has been found, this condition can be checked directly. But there is one thing we can conclude immediately: because ½Pð1<sup>Þ</sup> j Sð<sup>1</sup>Þ is an M ðG<sup>1</sup> þ M1Þ matrix, a necessary 

{228}------------------------------------------------

condition for assumption (9.10) is  $M \ge G_1 + M_1$ , or

$$M - M_1 \ge G_1 \tag{9.11}$$

We have already encountered condition (9.11) in Chapter 5: the number of exogenous variables not appearing in the first equation,  $M - M_1$ , must be at least as great as the number of endogenous variables appearing on the right-hand side of the first equation,  $G_1$ . This is the **order condition** for identification of equation one. We have proven the following theorem:

THEOREM 9.1 (Order Condition with Exclusion Restrictions): In a linear system of equations with exclusion restrictions, a *necessary* condition for identifying any particular equation is that the number of excluded exogenous variables from the equation must be at least as large as the number of included right-hand-side endogenous variables in the equation.

It is important to remember that the order condition is only necessary, not sufficient, for identification. If the order condition fails for a particular equation, there is no hope of estimating the parameters in that equation. If the order condition is met, the equation *might* be identified.