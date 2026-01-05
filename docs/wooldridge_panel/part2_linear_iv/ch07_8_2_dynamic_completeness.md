# Dynamic Completeness

> Pages: 186-188

While the homoskedasticity assumption, Assumption POLS.3a, can never be guaranteed to hold, there is one important case where Assumption POLS.3b must hold. Suppose that the explanatory variables x<sup>t</sup> are such that, for all t,

$$E(y_t | \mathbf{x}_t, y_{t-1}, \mathbf{x}_{t-1}, \dots, y_1, \mathbf{x}_1) = E(y_t | \mathbf{x}_t)$$
(7.71)

This assumption means that x<sup>t</sup> contains sufficient lags of all variables such that additional lagged values have no partial effect on yt. The inclusion of lagged y in equation (7.71) is important. For example, if z<sup>t</sup> is a vector of contemporaneous variables such that

$$\mathrm{E}(y_t | \mathbf{z}_t, \mathbf{z}_{t-1}, \dots, \mathbf{z}_1) = \mathrm{E}(y_t | \mathbf{z}_t, \mathbf{z}_{t-1}, \dots, \mathbf{z}_{t-L})$$

and we choose x<sup>t</sup> ¼ ðzt; zt-<sup>1</sup>; ... ; zt-<sup>L</sup>Þ, then Eðyt j xt; xt-<sup>1</sup>; ... ; x1Þ ¼ Eðyt j xtÞ. But equation (7.71) need not hold. Generally, in static and FDL models, there is no reason to expect equation (7.71) to hold, even in the absence of specification problems such as omitted variables.

We call equation (7.71) dynamic completeness of the conditional mean. Often, we can ensure that equation (7.71) is at least approximately true by putting sufficient lags of z<sup>t</sup> and yt into xt.

In terms of the disturbances, equation (7.71) is equivalent to

$$E(u_t | \mathbf{x}_t, u_{t-1}, \mathbf{x}_{t-1}, \dots, u_1, \mathbf{x}_1) = 0$$
(7.72)

and, by iterated expectations, equation (7.72) implies Eðutus j xt; xsÞ ¼ 0, s0 t. Therefore, equation (7.71) implies Assumption POLS.3b as well as Assumption POLS.1. If equation (7.71) holds along with the homoskedasticity assumption Varðyt j xtÞ ¼ s2, then Assumptions POLS.1 and POLS.3 both hold, and standard OLS statistics can be used for inference.

The following example is similar in spirit to an analysis of Maloney and McCormick (1993), who use a large random sample of students (including nonathletes) from Clemson University in a cross section analysis.

Example 7.8 (Effect of Being in Season on Grade Point Average): The data in GPA.RAW are on 366 student-athletes at a large university. There are two semesters of data (fall and spring) for each student. Of primary interest is the ''in-season'' effect on athletes' GPAs. The model—with i, t subscripts—is

$$trmgpa_{it} = \beta_0 + \beta_1 spring_t + \beta_2 cumgpa_{it} + \beta_3 crsgpa_{it} + \beta_4 frstsem_{it} + \beta_5 season_{it} + \beta_6 SAT_i \\ + \beta_7 verbmath_i + \beta_8 hsperc_i + \beta_9 hssize_i + \beta_{10} black_i + \beta_{11} female_i + u_{it}$$

{187}------------------------------------------------

The variable cumgpait is cumulative GPA at the beginning of the term, and this clearly depends on past-term GPAs. In other words, this model has something akin to a lagged dependent variable. In addition, it contains other variables that change over time (such as seasonit) and several variables that do not (such as SATi). We assume that the right-hand side (without uit) represents a conditional expectation, so that uit is necessarily uncorrelated with all explanatory variables and any functions of them. It may or may not be that the model is also dynamically complete in the sense of equation (7.71); we will show one way to test this assumption in Section 7.8.5. The estimated equation is

$$tr\hat{m}gpa_{it} = -2.07 - .012 \ spring_t + .315 \ cumgpa_{it} + .984 \ crsgpa_{it}$$
 $(0.34) \ (.046) \ (.040) \ (.096)$ 
 $+ .769 \ frstsem_{it} - .046 \ season_{it} + .00141 \ SAT_i - .113 \ verbmath_i$ 
 $(.120) \ (.047) \ (.00015) \ (.131)$ 
 $- .0066 \ hsperc_i - .000058 \ hssize_i - .231 \ black_i + .286 \ female_i$ 
 $(.0010) \ (.000099) \ (.054) \ (.051)$ 
 $N = 366, T = 2, R^2 = .519$ 

The in-season effect is small—an athlete's GPA is estimated to be .046 points lower when the sport is in season—and it is statistically insignificant as well. The other coefficients have reasonable signs and magnitudes.

Often, once we start putting any lagged values of yt into xt, then equation (7.71) is an intended assumption. But this generalization is not always true. In the previous example, we can think of the variable cumgpa as another control we are using to hold other factors fixed when looking at an in-season effect on GPA for college athletes: cumgpa can proxy for omitted factors that make someone successful in college. We may not care that serial correlation is still present in the error, except that, if equation (7.71) fails, we need to estimate the asymptotic variance of the pooled OLS estimator to be robust to serial correlation (and perhaps heteroskedasticity as well).

In introductory econometrics, students are often warned that having serial correlation in a model with a lagged dependent variable causes the OLS estimators to be inconsistent. While this statement is true in the context of a specific model of serial correlation, it is not true in general, and therefore it is very misleading. [See Wooldridge (2000a, Chapter 12) for more discussion in the context of the AR(1) model.] Our analysis shows that, whatever is included in xt, pooled OLS provides consistent estimators of *b* whenever Eðyt j xtÞ ¼ xt*b*; it does not matter that the ut might be serially correlated.

{188}------------------------------------------------

#### 7.8.3 A Note on Time Series Persistence

Theorem 7.7 imposes no restrictions on the time series persistence in the data  $\{(\mathbf{x}_{it}, y_{it}): t = 1, 2, ..., T\}$ . In light of the explosion of work in time series econometrics on asymptotic theory with persistent processes [often called *unit root processes*—see, for example, Hamilton (1994)], it may appear that we have not been careful in stating our assumptions. However, we do not need to restrict the dynamic behavior of our data in any way because we are doing fixed-T, large-N asymptotics. It is for this reason that the mechanics of the asymptotic analysis is the same for the SUR case and the panel data case. If T is large relative to N, the asymptotics here may be misleading. Fixing N while T grows or letting N and T both grow takes us into the realm of multiple time series analysis: we would have to know about the temporal dependence in the data, and, to have a general treatment, we would have to assume some form of weak dependence (see Wooldridge, 1994, for a discussion of weak dependence). Recently, progress has been made on asymptotics in panel data with large T and N when the data have unit roots; see, for example, Pesaran and Smith (1995) and Phillips and Moon (1999).

As an example, consider the simple AR(1) model

$$y_t = \beta_0 + \beta_1 y_{t-1} + u_t, \qquad E(u_t \mid y_{t-1}, \dots, y_0) = 0$$

Assumption POLS.1 holds (provided the appropriate moments exist). Also, Assumption POLS.2 can be maintained. Since this model is dynamically complete, the only potential nuisance is heteroskedasticity in  $u_t$  that changes over time or depends on  $y_{t-1}$ . In any case, the pooled OLS estimator from the regression  $y_{it}$  on 1,  $y_{i,t-1}$ , t = 1, ..., T, i = 1, ..., N, produces consistent,  $\sqrt{N}$ -asymptotically normal estimators for fixed T as  $N \to \infty$ , for any values of  $\beta_0$  and  $\beta_1$ .

In a pure time series case, or in a panel data case with  $T \to \infty$  and N fixed, we would have to assume  $|\beta_1| < 1$ , which is the stability condition for an AR(1) model. Cases where  $|\beta_1| \ge 1$  cause considerable complications when the asymptotics is done along the time series dimension (see Hamilton, 1994, Chapter 19). Here, a large cross section and relatively short time series allow us to be agnostic about the amount of temporal persistence.