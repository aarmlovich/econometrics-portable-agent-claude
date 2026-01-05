# Motivation: The Omitted Variables Problem

> Pages: 259-263

It is easy to see how panel data can be used, at least under certain assumptions, to obtain consistent estimators in the presence of omitted variables. Let y and x1 ðx1; x2; ... ; xK Þ be observable random variables, and let c be an unobservable random variable; the vector ðy; x1; x2; ... ; xK ; cÞ represents the population of interest. As is often the case in applied econometrics, we are interested in the partial effects of the observable explanatory variables xj in the population regression function

$$E(y | x_1, x_2, \dots, x_K, c)$$
 (10.1)

In words, we would like to hold c constant when obtaining partial effects of the observable explanatory variables. We follow Chamberlain (1984) in using c to denote the unobserved variable. Much of the panel data literature uses a Greek letter, such as a or f, but we want to emphasize that the unobservable is a random variable, not a parameter to be estimated. (We discuss this point further in Section 10.2.1.)

Assuming a linear model, with c entering additively along with the xj, we have

$$E(y \mid \mathbf{x}, c) = \beta_0 + \mathbf{x}\boldsymbol{\beta} + c \tag{10.2}$$

where interest lies in the K 1 vector *b*. On the one hand, if c is uncorrelated with each xj, then c is just another unobserved factor affecting y that is not systematically related to the observable explanatory variables whose effects are of interest. On the other hand, if Covðxj; cÞ 00 for some j, putting c into the error term can cause serious problems. Without additional information we cannot consistently estimate *b*, nor will we be able to determine whether there is a problem (except by introspection, or by concluding that the estimates of *b* are somehow ''unreasonable'').

{260}------------------------------------------------

Under additional assumptions there are ways to address the problem Covðx; cÞ 00. We have covered at least three possibilities in the context of cross section analysis: (1) we might be able to find a suitable proxy variable for c, in which case we can estimate an equation by OLS where the proxy is plugged in for c; (2) we may be able to find instruments for the elements of x that are correlated with c and use an instrumental variables method, such as 2SLS; or (3) we may be able to find indicators of c that can then be used in multiple indicator instrumental variables procedure. These solutions are covered in Chapters 4 and 5.

If we have access to only a single cross section of observations, then the three remedies listed, or slight variants of them, largely exhaust the possibilities. However, if we can observe the same cross section units at different points in time—that is, if we can collect a panel data set—then other possibilties arise.

For illustration, suppose we can observe y and x at two different time periods; call these yt, x<sup>t</sup> for t ¼ 1; 2. The population now represents two time periods on the same unit. Also, suppose that the omitted variable c is time constant. Then we are interested in the population regression function

$$E(y_t | \mathbf{x}_t, c) = \beta_0 + \mathbf{x}_t \boldsymbol{\beta} + c, \qquad t = 1, 2$$
 (10.3)

where xt*b* ¼ b1xt<sup>1</sup> þ--þ b<sup>K</sup> xtK and xtj indicates variable j at time t. Model (10.3) assumes that c has the same effect on the mean response in each time period. Without loss of generality, we set the coefficient on c equal to one. (Because c is unobserved and virtually never has a natural unit of measurement, it would be meaningless to try to estimate its partial effect.)

The assumption that c is constant over time (and has a constant partial effect over time) is crucial to the following analysis. An unobserved, time-constant variable is called an unobserved effect in panel data analysis. When t represents different time periods for the same individual, the unobserved effect is often interpreted as capturing features of an individual, such as cognitive ability, motivation, or early family upbringing, that are given and do not change over time. Similarly, if the unit of observation is the firm, c contains unobserved firm characteristics—such as managerial quality or structure—that can be viewed as being (roughly) constant over the period in question. We cover several specific examples of unobserved effects models in Section 10.2.

To discuss the additional assumptions sufficient to estimate *b*, it is useful to write model (10.3) in error form as

$$y_t = \beta_0 + \mathbf{x}_t \boldsymbol{\beta} + c + u_t \tag{10.4}$$

where, by definition,


{261}------------------------------------------------

$$E(u_t | \mathbf{x}_t, c) = 0, \qquad t = 1, 2$$
 (10.5)

One implication of condition (10.5) is

$$\mathbf{E}(\mathbf{x}_t'u_t) = \mathbf{0}, \qquad t = 1, 2 \tag{10.6}$$

If we were to assume  $E(\mathbf{x}_t'c) = \mathbf{0}$ , we could apply pooled OLS, as we covered in Section 7.8. If c is correlated with any element of  $\mathbf{x}_t$ , then pooled OLS is biased and inconsistent.

With two years of data we can difference equation (10.4) across the two time periods to eliminate the time-constant unobservable, c. Define  $\Delta y = y_2 - y_1$ ,  $\Delta \mathbf{x} = \mathbf{x}_2 - \mathbf{x}_1$ , and  $\Delta u = u_2 - u_1$ . Then, differencing equation (10.4) gives

$$\Delta y = \Delta \mathbf{x} \boldsymbol{\beta} + \Delta u \tag{10.7}$$

which is just a standard linear model in the differences of all variables (although the intercept has dropped out). Importantly, the parameter vector of interest,  $\beta$ , appears directly in equation (10.7), and its presence suggests estimating equation (10.7) by OLS. Given a panel data set with two time periods, equation (10.7) is just a standard cross section equation. Under what assumptions will the OLS estimator from equation (10.7) be consistent?

Because we assume a random sample from the population, we can apply the results in Chapter 4 directly to equation (10.7). The key conditions for OLS to consistently estimate  $\beta$  are the orthogonality condition (Assumption OLS.1)

$$E(\Delta \mathbf{x}'\Delta u) = \mathbf{0} \tag{10.8}$$

and the rank condition (Assumption OLS.2)

$$rank E(\Delta \mathbf{x}'\Delta \mathbf{x}) = K \tag{10.9}$$

Consider condition (10.8) first. It is equivalent to  $E[(\mathbf{x}_2 - \mathbf{x}_1)'(u_2 - u_1)] = \mathbf{0}$  or, after simple algebra,

$$E(\mathbf{x}_{2}'u_{2}) + E(\mathbf{x}_{1}'u_{1}) - E(\mathbf{x}_{1}'u_{2}) - E(\mathbf{x}_{2}'u_{1}) = \mathbf{0}$$
(10.10)

The first two terms in equation (10.10) are zero by condition (10.6), which holds for t = 1, 2. But condition (10.5) does *not* guarantee that  $\mathbf{x}_1$  and  $u_2$  are uncorrelated or that  $\mathbf{x}_2$  and  $u_1$  are uncorrelated. It might be reasonable to *assume* that condition (10.8) holds, but we must recognize that it does not follow from condition (10.5). Assuming that the error  $u_t$  is uncorrelated with  $\mathbf{x}_1$  and  $\mathbf{x}_2$  for t = 1, 2 is an example of a strict exogeneity assumption in unobserved components panel data models. We discuss strict exogeneity assumptions generally in Section 10.2. For now, we emphasize

{262}------------------------------------------------

that assuming Covðxt; usÞ ¼ 0 for all t and s puts no restrictions on the correlation between x<sup>t</sup> and the unobserved effect, c.

The second assumption, condition (10.9), also deserves some attention now because the elements of x<sup>t</sup> appearing in structural equation (10.3) have been differenced across time. If x<sup>t</sup> contains a variable that is constant across time for every member of the population, then Dx contains an entry that is identically zero, and condition (10.9) fails. This outcome is not surprising: if c is allowed to be arbitrarily correlated with the elements of xt, the effect of any variable that is constant across time cannot be distinguished from the effect of c. Therefore, we can consistently estimate b<sup>j</sup> only if there is some variation in xtj over time.

In the remainder of this chapter, we cover various ways of dealing with the presence of unobserved effects under different sets of assumptions. We assume we have repeated observations on a cross section of N individuals, families, firms, school districts, cities, or some other economic unit. As in Chapter 7, we assume in this chapter that we have the same time periods, denoted t ¼ 1; 2; ... ;T, for each cross section observation. Such a data set is usually called a balanced panel because the same time periods are available for all cross section units. While the mechanics of the unbalanced case are similar to the balanced case, a careful treatment of the unbalanced case requires a formal description of why the panel may be unbalanced, and the sample selection issues can be somewhat subtle. Therefore, we hold off covering unbalanced panels until Chapter 17, where we discuss sample selection and attrition issues.

We still focus on asymptotic properties of estimators, where the time dimension, T, is fixed and the cross section dimension, N, grows without bound. With large-N asymptotics it is convenient to view the cross section observations as independent, identically distributed draws from the population. For any cross section observation i—denoting a single individual, firm, city, and so on—we denote the observable variables for all T time periods by fðyit; xitÞ: t ¼ 1; 2; ... ; Tg. Because of the fixed T assumption, the asymptotic analysis is valid for arbitrary time dependence and distributional heterogeneity across t.

When applying asymptotic analysis to panel data methods it is important to remember that asymptotics are useful insofar as they provide a reasonable approximation to the finite sample properties of estimators and statistics. For example, a priori it is difficult to know whether N ! y asymptotics works well with, say, N ¼ 50 states in the United States and T ¼ 8 years. But we can be pretty confident that N ! y asymptotics are more appropriate than T ! y asymptotics, even though N is practically fixed while T can grow. With large geographical regions, the random sampling assumption in the cross section dimension is conceptually flawed. 

{263}------------------------------------------------

Nevertheless, if N is sufficiently large relative to T, and we can assume rough independence in the cross section, then our asymptotic analysis should provide suitable approximations.

If T is of the same order as N—for example, N ¼ 60 countries and T ¼ 55 post– World War II years—an asymptotic analysis that makes explicit assumptions about the nature of the time series dependence is needed. (In special cases, the conclusions about consistent estimation and approximate normality of t statistics will be the same, but not generally.) This area is just beginning to receive careful attention. If T is much larger than N, say N ¼ 5 companies and T ¼ 40 years, the framework becomes multiple time series analysis: N can be held fixed while T ! y.

# 10.2 Assumptions about the Unobserved Effects and Explanatory Variables

Before analyzing panel data estimation methods in more detail, it is useful to generally discuss the nature of the unobserved effects and certain features of the observed explanatory variables.