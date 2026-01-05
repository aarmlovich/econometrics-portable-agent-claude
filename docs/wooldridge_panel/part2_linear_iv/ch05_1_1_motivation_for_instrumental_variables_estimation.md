# Motivation for Instrumental Variables Estimation

> Pages: 98-105

To motivate the need for the method of instrumental variables, consider a linear population model

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \dots + \beta_K x_K + u$$
 (5.1)

$$E(u) = 0,$$
  $Cov(x_j, u) = 0,$   $j = 1, 2, ..., K - 1$  (5.2)

but where xK might be correlated with u. In other words, the explanatory variables x1, x2; ... ; xK-<sup>1</sup> are exogenous, but xK is potentially endogenous in equation (5.1). The endogeneity can come from any of the sources we discussed in Chapter 4. To fix ideas it might help to think of u as containing an omitted variable that is uncorrelated with all explanatory variables except xK . So, we may be interested in a conditional expectation as in equation (4.18), but we do not observe q, and q is correlated with xK .

As we saw in Chapter 4, OLS estimation of equation (5.1) generally results in inconsistent estimators of all the b<sup>j</sup> if CovðxK ; uÞ 00. Further, without more information, we cannot consistently estimate any of the parameters in equation (5.1).

The method of instrumental variables (IV ) provides a general solution to the problem of an endogenous explanatory variable. To use the IV approach with xK endogenous, we need an observable variable, z1, not in equation (5.1) that satisfies two conditions. First, z<sup>1</sup> must be uncorrelated with u:

$$Cov(z_1, u) = 0 (5.3)$$

In other words, like x1; ... ; xK-1, z<sup>1</sup> is exogenous in equation (5.1).

The second requirement involves the relationship between z<sup>1</sup> and the endogenous variable, xK . A precise statement requires the linear projection of xK onto all the exogenous variables:

$$x_K = \delta_0 + \delta_1 x_1 + \delta_2 x_2 + \dots + \delta_{K-1} x_{K-1} + \theta_1 z_1 + r_K$$
(5.4)

where, by definition of a linear projection error, EðrK Þ ¼ 0 and rK is uncorrelated with x1, x2; ... ; xK-1, and z1. The key assumption on this linear projection is that the

{99}------------------------------------------------

coefficient on z<sup>1</sup> is nonzero:

$$\theta_1 \neq 0 \tag{5.5}$$

This condition is often loosely described as ''z<sup>1</sup> is correlated with xK ,'' but that statement is not quite correct. The condition y<sup>1</sup> 0 0 means that z<sup>1</sup> is partially correlated with xK once the other exogenous variables x1; ... ; xK-<sup>1</sup> have been netted out. If xK is the only explanatory variable in equation (5.1), then the linear projection is xK ¼ d<sup>0</sup> þ y1z<sup>1</sup> þ rK , where y<sup>1</sup> ¼ Covðz1; xK Þ=Varðz1Þ, and so condition (5.5) and Covðz1; xK Þ 00 are the same.

At this point we should mention that we have put no restrictions on the distribution of xK or z1. In many cases xK and z<sup>1</sup> will be both essentially continuous, but sometimes xK , z1, or both are discrete. In fact, one or both of xK and z<sup>1</sup> can be binary variables, or have continuous and discrete characteristics at the same time. Equation (5.4) is simply a linear projection, and this is always defined when second moments of all variables are finite.

When z<sup>1</sup> satisfies conditions (5.3) and (5.5), then it is said to be an instrumental variable (IV) candidate for xK . (Sometimes z<sup>1</sup> is simply called an instrument for xK .) Because x1; ... ; xK-<sup>1</sup> are already uncorrelated with u, they serve as their own instrumental variables in equation (5.1). In other words, the full list of instrumental variables is the same as the list of exogenous variables, but we often just refer to the instrument for the endogenous explanatory variable.

The linear projection in equation (5.4) is called a reduced form equation for the endogenous explanatory variable xK . In the context of single-equation linear models, a reduced form always involves writing an endogenous variable as a linear projection onto all exogenous variables. The ''reduced form'' terminology comes from simultaneous equations analysis, and it makes more sense in that context. We use it in all IV contexts because it is a concise way of stating that an endogenous variable has been linearly projected onto the exogenous variables. The terminology also conveys that there is nothing necessarily structural about equation (5.4).

From the structural equation (5.1) and the reduced form for xK , we obtain a reduced form for y by plugging equation (5.4) into equation (5.1) and rearranging:

$$y = \alpha_0 + \alpha_1 x_1 + \dots + \alpha_{K-1} x_{K-1} + \lambda_1 z_1 + v$$
 (5.6)

where v ¼ u þ b<sup>K</sup> rK is the reduced form error, a<sup>j</sup> ¼ b<sup>j</sup> þ b<sup>K</sup> dj, and l<sup>1</sup> ¼ b<sup>K</sup> y1. By our assumptions, v is uncorrelated with all explanatory variables in equation (5.6), and so OLS consistently estimates the reduced form parameters, the a<sup>j</sup> and l1.

Estimates of the reduced form parameters are sometimes of interest in their own right, but estimating the structural parameters is generally more useful. For example, at the firm level, suppose that xK is job training hours per worker and y is a measure 

{100}------------------------------------------------

of average worker productivity. Suppose that job training grants were randomly assigned to firms. Then it is natural to use for z<sup>1</sup> either a binary variable indicating whether a firm received a job training grant or the actual amount of the grant per worker (if the amount varies by firm). The parameter b<sup>K</sup> in equation (5.1) is the effect of job training on worker productivity. If z<sup>1</sup> is a binary variable for receiving a job training grant, then l<sup>1</sup> is the effect of receiving this particular job training grant on worker productivity, which is of some interest. But estimating the effect of an hour of general job training is more valuable.

We can now show that the assumptions we have made on the IV z<sup>1</sup> solve the identification problem for the b<sup>j</sup> in equation (5.1). By identification we mean that we can write the b<sup>j</sup> in terms of population moments in observable variables. To see how, write equation (5.1) as

$$y = \mathbf{x}\boldsymbol{\beta} + u \tag{5.7}$$

where the constant is absorbed into x so that x ¼ ð1; x2; ... ; xK Þ. Write the 1 K vector of all exogenous variables as

$$\mathbf{z} \equiv (1, x_2, \dots, x_{K-1}, z_1)$$

Assumptions (5.2) and (5.3) imply the K population orthogonality conditions

$$E(\mathbf{z}'u) = \mathbf{0} \tag{5.8}$$

Multiplying equation (5.7) through by z<sup>0</sup> , taking expectations, and using equation (5.8) gives

$$[\mathbf{E}(\mathbf{z}'\mathbf{x})]\boldsymbol{\beta} = \mathbf{E}(\mathbf{z}'y) \tag{5.9}$$

where Eðz<sup>0</sup> xÞ is K K and Eðz<sup>0</sup> yÞ is K 1. Equation (5.9) represents a system of K linear equations in the K unknowns b1, b2; ... ; b<sup>K</sup> . This system has a unique solution if and only if the K K matrix Eðz<sup>0</sup> xÞ has full rank; that is,

$$rank E(\mathbf{z}'\mathbf{x}) = K \tag{5.10}$$

in which case the solution is

$$\boldsymbol{\beta} = [\mathbf{E}(\mathbf{z}'\mathbf{x})]^{-1}\mathbf{E}(\mathbf{z}'y) \tag{5.11}$$

The expectations Eðz<sup>0</sup> xÞ and Eðz<sup>0</sup> yÞ can be consistently estimated using a random sample on ðx; y; z1Þ, and so equation (5.11) identifies the vector *b*.

It is clear that condition (5.3) was used to obtain equation (5.11). But where have we used condition (5.5)? Let us maintain that there are no linear dependencies among the exogenous variables, so that Eðz<sup>0</sup> zÞ has full rank K; this simply rules out perfect


{101}------------------------------------------------

collinearity in z in the population. Then, it can be shown that equation (5.10) holds if and only if  $\theta_1 \neq 0$ . (A more general case, which we cover in Section 5.1.2, is covered in Problem 5.12.) Therefore, along with the exogeneity condition (5.3), assumption (5.5) is the key identification condition. Assumption (5.10) is the **rank condition** for identification, and we return to it more generally in Section 5.2.1.

Given a random sample  $\{(\mathbf{x}_i, y_i, \mathbf{z}_{i1}): i = 1, 2, ..., N\}$  from the population, the **instrumental variables estimator** of  $\boldsymbol{\beta}$  is

$$\hat{\boldsymbol{\beta}} = \left( N^{-1} \sum_{i=1}^{N} \mathbf{z}_{i}' \mathbf{x}_{i} \right)^{-1} \left( N^{-1} \sum_{i=1}^{N} \mathbf{z}_{i}' y_{i} \right) = (\mathbf{Z}' \mathbf{X})^{-1} \mathbf{Z}' \mathbf{Y}$$

where **Z** and **X** are  $N \times K$  data matrices and **Y** is the  $N \times 1$  data vector on the  $y_i$ . The consistency of this estimator is immediate from equation (5.11) and the law of large numbers. We consider a more general case in Section 5.2.1.

When searching for instruments for an endogenous explanatory variable, conditions (5.3) and (5.5) are equally important in identifying  $\beta$ . There is, however, one practically important difference between them: condition (5.5) can be tested, whereas condition (5.3) must be maintained. The reason for this disparity is simple: the covariance in condition (5.3) involves the *unobservable u*, and therefore we cannot test anything about  $Cov(z_1, u)$ .

Testing condition (5.5) in the reduced form (5.4) is a simple matter of computing a t test after OLS estimation. Nothing guarantees that  $r_K$  satisfies the requisite homoskedasticity assumption (Assumption OLS.3), so a heteroskedasticity-robust t statistic for  $\hat{\theta}_1$  is often warranted. This statement is especially true if  $x_K$  is a binary variable or some other variable with discrete characteristics.

A word of caution is in order here. Econometricians have been known to say that "it is not possible to test for identification." In the model with one endogenous variable and one instrument, we have just seen the sense in which this statement is true: assumption (5.3) cannot be tested. Nevertheless, the fact remains that condition (5.5) can and *should* be tested. In fact, recent work has shown that the strength of the rejection in condition (5.5) (in a *p*-value sense) is important for determining the finite sample properties, particularly the bias, of the IV estimator. We return to this issue in Section 5.2.6.

In the context of omitted variables, an instrumental variable, like a proxy variable, must be redundant in the structural model [that is, the model that explicitly contains the unobservables; see condition (4.25)]. However, unlike a proxy variable, an IV for  $x_K$  should be *uncorrelated* with the omitted variable. Remember, we want a proxy variable to be highly correlated with the omitted variable.

{102}------------------------------------------------

Example 5.1 (Instrumental Variables for Education in a Wage Equation): Consider a wage equation for the U.S. working population

$$\log(wage) = \beta_0 + \beta_1 exper + \beta_2 exper^2 + \beta_3 educ + u$$
(5.12)

where u is thought to be correlated with educ because of omitted ability, as well as other factors, such as quality of education and family background. Suppose that we can collect data on mother's education, motheduc. For this to be a valid instrument for educ we must assume that motheduc is uncorrelated with u and that y<sup>1</sup> 0 0 in the reduced form equation

$$educ = \delta_0 + \delta_1 exper + \delta_2 exper^2 + \theta_1 motheduc + r$$

There is little doubt that educ and motheduc are partially correlated, and this correlation is easily tested given a random sample from the population. The potential problem with motheduc as an instrument for educ is that motheduc might be correlated with the omitted factors in u: mother's education is likely to be correlated with child's ability and other family background characteristics that might be in u.

A variable such as the last digit of one's social security number makes a poor IV candidate for the opposite reason. Because the last digit is randomly determined, it is independent of other factors that affect earnings. But it is also independent of education. Therefore, while condition (5.3) holds, condition (5.5) does not.

By being clever it is often possible to come up with more convincing instruments. Angrist and Krueger (1991) propose using quarter of birth as an IV for education. In the simplest case, let frstqrt be a dummy variable equal to unity for people born in the first quarter of the year and zero otherwise. Quarter of birth is arguably independent of unobserved factors such as ability that affect wage (although there is disagreement on this point; see Bound, Jaeger, and Baker, 1995). In addition, we must have y<sup>1</sup> 00 in the reduced form

$$educ = \delta_0 + \delta_1 exper + \delta_2 exper^2 + \theta_1 frstqrt + r$$

How can quarter of birth be (partially) correlated with educational attainment? Angrist and Krueger (1991) argue that compulsory school attendence laws induce a relationship between educ and frstqrt: at least some people are forced, by law, to attend school longer than they otherwise would, and this fact is correlated with quarter of birth. We can determine the strength of this association in a particular sample by estimating the reduced form and obtaining the t statistic for H0: y<sup>1</sup> ¼ 0.

This example illustrates that it can be very difficult to find a good instrumental variable for an endogenous explanatory variable because the variable must satisfy

{103}------------------------------------------------

two different, often conflicting, criteria. For motheduc, the issue in doubt is whether condition (5.3) holds. For frstqrt, the initial concern is with condition (5.5). Since condition (5.5) can be tested, frstqrt has more appeal as an instrument. However, the partial correlation between educ and frstqrt is small, and this can lead to finite sample problems (see Section 5.2.6). A more subtle issue concerns the sense in which we are estimating the return to education for the entire population of working people. As we will see in Chapter 18, if the return to education is not constant across people, the IV estimator that uses frstqrt as an IV estimates the return to education only for those people induced to obtain more schooling because they were born in the first quarter of the year. These make up a relatively small fraction of the population.

Convincing instruments sometimes arise in the context of program evaluation, where individuals are randomly selected to be eligible for the program. Examples include job training programs and school voucher programs. Actual participation is almost always voluntary, and it may be endogenous because it can depend on unobserved factors that affect the response. However, it is often reasonable to assume that eligibility is exogenous. Because participation and eligibility are correlated, the latter can be used as an IV for the former.

A valid instrumental variable can also come from what is called a natural experiment. A natural experiment occurs when some (often unintended) feature of the setup we are studying produces exogenous variation in an otherwise endogenous explanatory variable. The Angrist and Krueger (1991) example seems, at least initially, to be a good natural experiment. Another example is given by Angrist (1990), who studies the effect of serving in the Vietnam war on the earnings of men. Participation in the military is not necessarily exogenous to unobserved factors that affect earnings, even after controlling for education, nonmilitary experience, and so on. Angrist used the following observation to obtain an instrumental variable for the binary Vietnam war participation indicator: men with a lower draft lottery number were more likely to serve in the war. Angrist verifies that the probability of serving in Vietnam is indeed related to draft lottery number. Because the lottery number is randomly determined, it seems like an ideal IV for serving in Vietnam. There are, however, some potential problems. It might be that men who were assigned a low lottery number chose to obtain more education as a way of increasing the chance of obtaining a draft deferment. If we do not control for education in the earnings equation, lottery number could be endogenous. Further, employers may have been willing to invest in job training for men who are unlikely to be drafted. Again, unless we can include measures of job training in the earnings equation, condition (5.3) may be violated. (This reasoning assumes that we are interested in estimating the pure effect of serving in Vietnam, as opposed to including indirect effects such as reduced job training.)

{104}------------------------------------------------

Hoxby (1994) uses topographical features, in particular the natural boundaries created by rivers, as IVs for the concentration of public schools within a school district. She uses these IVs to estimate the effects of competition among public schools on student performance. Cutler and Glaeser (1997) use the Hoxby instruments, as well as others, to estimate the effects of segregation on schooling and employment outcomes for blacks. Levitt (1997) provides another example of obtaining instrumental variables from a natural experiment. He uses the timing of mayoral and gubernatorial elections as instruments for size of the police force in estimating the effects of police on city crime rates. (Levitt actually uses panel data, something we will discuss in Chapter 11.)

Sensible IVs need not come from natural experiments. For example, Evans and Schwab (1995) study the effect of attending a Catholic high school on various outcomes. They use a binary variable for whether a student is Catholic as an IV for attending a Catholic high school, and they spend much effort arguing that religion is exogenous in their versions of equation (5.7). [In this application, condition (5.5) is easy to verify.] Economists often use regional variation in prices or taxes as instruments for endogenous explanatory variables appearing in individual-level equations. For example, in estimating the effects of alcohol consumption on performance in college, the local price of alcohol can be used as an IV for alcohol consumption, provided other regional factors that affect college performance have been appropriately controlled for. The idea is that the price of alcohol, including any taxes, can be assumed to be exogenous to each individual.

Example 5.2 (College Proximity as an IV for Education): Using wage data for 1976, Card (1995) uses a dummy variable that indicates whether a man grew up in the vicinity of a four-year college as an instrumental variable for years of schooling. He also includes several other controls. In the equation with experience and its square, a black indicator, southern and urban indicators, and regional and urban indicators for 1966, the instrumental variables estimate of the return to schooling is .132, or 13.2 percent, while the OLS estimate is 7.5 percent. Thus, for this sample of data, the IV estimate is almost twice as large as the OLS estimate. This result would be counterintuitive if we thought that an OLS analysis suffered from an upward omitted variable bias. One interpretation is that the OLS estimators suffer from the attenuation bias as a result of measurement error, as we discussed in Section 4.4.2. But the classical errors-in-variables assumption for education is questionable. Another interpretation is that the instrumental variable is not exogenous in the wage equation: location is not entirely exogenous. The full set of estimates, including standard errors and t statistics, can be found in Card (1995). Or, you can replicate Card's results in Problem 5.4.

{105}------------------------------------------------