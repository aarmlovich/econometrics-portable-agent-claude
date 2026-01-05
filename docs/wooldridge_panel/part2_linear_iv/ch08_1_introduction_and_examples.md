# Introduction and Examples

> Pages: 196-199

In Chapter 7 we covered system estimation of linear equations when the explanatory variables satisfy certain exogeneity conditions. For many applications, even the weakest of these assumptions, Assumption SOLS.1, is violated, in which case instrumental variables procedures are indispensable.

The modern approach to system instrumental variables (SIV ) estimation is based on the principle of generalized method of moments (GMM). Method of moments estimation has a long history in statistics for obtaining simple parameter estimates when maximum likelihood estimation requires nonlinear optimization. Hansen (1982) and White (1982b) showed how the method of moments can be generalized to apply to a variety of econometric models, and they derived the asymptotic properties of GMM. Hansen (1982), who coined the name ''generalized method of moments,'' treated time series data, and White (1982b) assumed independently sampled observations.

Though the models considered in this chapter are more general than those treated in Chapter 5, the derivations of asymptotic properties of system IV estimators are mechanically similar to the derivations in Chapters 5 and 7. Therefore, the proofs in this chapter will be terse, or omitted altogether.

In econometrics, the most familar application of SIV estimation is to a simultaneous equations model (SEM). We will cover SEMs specifically in Chapter 9, but it is useful to begin with a typical SEM example. System estimation procedures have applications beyond the classical simultaneous equations methods. We will also use the results in this chapter for the analysis of panel data models in Chapter 11.

Example 8.1 (Labor Supply and Wage Offer Functions): Consider the following labor supply function representing the hours of labor supply, h<sup>s</sup> , at any wage, w, faced by an individual. As usual, we express this in population form:

$$h^{s}(\omega) = \gamma_{1}\omega + \mathbf{z}_{1}\boldsymbol{\delta}_{1} + u_{1} \tag{8.1}$$

where z<sup>1</sup> is a vector of observed labor supply shifters—including such things as education, past experience, age, marital status, number of children, and nonlabor income—and u<sup>1</sup> contains unobservables affecting labor supply. The labor supply function can be derived from individual utility-maximizing behavior, and the notation in equation (8.1) is intended to emphasize that, for given z<sup>1</sup> and u1, a labor supply function gives the desired hours worked at any possible wage ðwÞ facing the worker. As a practical matter, we can only observe equilibrium values of hours worked and hourly wage. But the counterfactual reasoning underlying equation (8.1) is the proper way to view labor supply.

{197}------------------------------------------------

A wage offer function gives the hourly wage that the market will offer as a function of hours worked. (It could be that the wage offer does not depend on hours worked, but in general it might.) For observed productivity attributes z<sup>2</sup> (for example, education, experience, and amount of job training) and unobserved attributes u2, we write the wage offer function as

$$w^{o}(h) = \gamma_2 h + \mathbf{z}_2 \delta_2 + u_2 \tag{8.2}$$

Again, for given z<sup>2</sup> and u2, w<sup>o</sup>ðhÞ gives the wage offer for an individual agreeing to work h hours.

Equations (8.1) and (8.2) explain different sides of the labor market. However, rarely can we assume that an individual is given an exogenous wage offer and then, at that wage, decides how much to work based on equation (8.1). A reasonable approach is to assume that observed hours and wage are such that equations (8.1) and (8.2) both hold. In other words, letting ðh; wÞ denote the equilibrium values, we have

$$h = \gamma_1 w + \mathbf{z}_1 \boldsymbol{\delta}_1 + u_1 \tag{8.3}$$

$$w = \gamma_2 h + \mathbf{z}_2 \delta_2 + u_2 \tag{8.4}$$

Under weak restrictions on the parameters, these equations can be solved uniquely for ðh; wÞ as functions of z1, z2, u1, u2, and the parameters; we consider this topic generally in Chapter 9. Further, if z<sup>1</sup> and z<sup>2</sup> are exogenous in the sense that

$$E(u_1 | \mathbf{z}_1, \mathbf{z}_2) = E(u_2 | \mathbf{z}_1, \mathbf{z}_2) = 0$$

then, under identification assumptions, we can consistently estimate the parameters of the labor supply and wage offer functions. We consider identification of SEMs in detail in Chapter 9. We also ignore what is sometimes a practically important issue: the equilibrium hours for an individual might be zero, in which case w is not observed for such people. We deal with missing data issues in Chapter 17.

For a random draw from the population we can write

$$h_i = \gamma_1 w_i + \mathbf{z}_{i1} \boldsymbol{\delta}_1 + u_{i1} \tag{8.5}$$

$$w_i = \gamma_2 h_i + \mathbf{z}_{i2} \boldsymbol{\delta}_2 + u_{i2} \tag{8.6}$$

Except under very special assumptions, ui<sup>1</sup> will be correlated with wi, and ui<sup>2</sup> will be correlated with hi. In other words, wi is probably endogenous in equation (8.5), and hi is probably endogenous in equation (8.6). It is for this reason that we study system instrumental variables methods.

{198}------------------------------------------------

An example with the same statistical structure as Example 8.1, but with an omitted variables interpretation, is motivated by Currie and Thomas (1995).

Example 8.2 (Student Performance and Head Start): Consider an equation to test the effect of Head Start participation on subsequent student performance:

$$score_i = \gamma_1 HeadStart_i + \mathbf{z}_{i1} \boldsymbol{\delta}_1 + u_{i1}$$
(8.7)

where scorei is the outcome on a test when the child is enrolled in school and HeadStarti is a binary indicator equal to one if child i participated in Head Start at an early age. The vector z<sup>i</sup><sup>1</sup> contains other observed factors, such as income, education, and family background variables. The error term ui<sup>1</sup> contains unobserved factors that affect score—such as child's ability—that may also be correlated with HeadStart. To capture the possible endogeneity of HeadStart, we write a linear reduced form (linear projection) for HeadStarti:

$$HeadStart_i = \mathbf{z}_i \boldsymbol{\delta}_2 + u_{i2} \tag{8.8}$$

Remember, this projection always exists even though HeadStarti is a binary variable. The vector z<sup>i</sup> contains zi<sup>1</sup> and at least one factor affecting Head Start participation that does not have a direct effect on score. One possibility is distance to the nearest Head Start center. In this example we would probably be willing to assume that Eðui<sup>1</sup> j ziÞ ¼ 0—since the test score equation is structural—but we would only want to assume Eðz<sup>0</sup> <sup>i</sup>ui2Þ ¼ 0, since the Head Start equation is a linear projection involving a binary dependent variable. Correlation between u<sup>1</sup> and u<sup>2</sup> means HeadStart is endogenous in equation (8.7).

Both of the previous examples can be written for observation i as

$$y_{i1} = \mathbf{x}_{i1}\boldsymbol{\beta}_1 + u_{i1} \tag{8.9}$$

$$y_{i2} = \mathbf{x}_{i2} \boldsymbol{\beta}_2 + u_{i2} \tag{8.10}$$

which looks just like a two-equation SUR system but where x<sup>i</sup><sup>1</sup> and x<sup>i</sup><sup>2</sup> can contain endogenous as well as exogenous variables. Because x<sup>i</sup><sup>1</sup> and x<sup>i</sup><sup>2</sup> are generally correlated with ui<sup>1</sup> and ui2, estimation of these equations by OLS or FGLS, as we studied in Chapter 7, will generally produce inconsistent estimators.

We already know one method for estimating an equation such as equation (8.9): if we have sufficient instruments, apply 2SLS. Often 2SLS produces acceptable results, so why should we go beyond single-equation analysis? Not surprisingly, our interest in system methods with endogenous explanatory variables has to do with efficiency. In many cases we can obtain more efficient estimators by estimating *b*<sup>1</sup> and *b*<sup>2</sup> jointly,

{199}------------------------------------------------

that is, by using a system procedure. The efficiency gains are analogous to the gains that can be realized by using feasible GLS rather than OLS in a SUR system.