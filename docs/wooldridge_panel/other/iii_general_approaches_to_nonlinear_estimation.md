# III GENERAL APPROACHES TO NONLINEAR ESTIMATION

> Pages: 350-352

In this part we begin our study of nonlinear econometric methods. What we mean by nonlinear needs some explanation because it does not necessarily mean that the underlying model is what we would think of as nonlinear. For example, suppose the population model of interest can be written as y ¼ x*b* þ u, but, rather than assuming Eðu j xÞ ¼ 0, we assume that the median of u given x is zero for all x. This assumption implies Medðy j xÞ ¼ x*b*, which is a linear model for the conditional median of y given x. [The conditional mean, Eðy j xÞ, may or may not be linear in x.] The standard estimator for a conditional median turns out to be least absolute deviations (LAD), not ordinary least squares. Like OLS, the LAD estimator solves a minimization problem: it minimizes the sum of absolute residuals. However, there is a key difference between LAD and OLS: the LAD estimator cannot be obtained in closed form. The lack of a closed-form expression for LAD has implications not only for obtaining the LAD estimates from a sample of data, but also for the asymptotic theory of LAD.

All the estimators we studied in Part II were obtained in closed form, a fact which greatly facilitates asymptotic analysis: we needed nothing more than the weak law of large numbers, the central limit theorem, and the basic algebra of probability limits. When an estimation method does not deliver closed-form solutions, we need to use more advanced asymptotic theory. In what follows, ''nonlinear'' describes any problem in which the estimators cannot be obtained in closed form.

The three chapters in this part provide the foundation for asymptotic analysis of most nonlinear models encountered in applications with cross section or panel data. We will make certain assumptions concerning continuity and differentiability, and so problems violating these conditions will not be covered. In the general development of M-estimators in Chapter 12, we will mention some of the applications that are ruled out and provide references.

This part of the book is by far the most technical. We will not dwell on the sometimes intricate arguments used to establish consistency and asymptotic normality in nonlinear contexts. For completeness, we do provide some general results on consistency and asymptotic normality for general classes of estimators. However, for specific estimation methods, such as nonlinear least squares, we will only state assumptions that have real impact for performing inference. Unless the underlying regularity conditions—which involve assuming that certain moments of the population random variables are finite, as well as assuming continuity and differentiability of the regression function or log-likelihood function—are obviously false, they are usually just assumed. Where possible, the assumptions will correspond closely with those given previously for linear models.


{351}------------------------------------------------

340 Part III

The analysis of maximum likelihood methods in Chapter 13 is greatly simplified once we have given a general treatment of M-estimators. Chapter 14 contains results for generalized method of moments estimators for models nonlinear in parameters. We also briefly discuss the related topic of minimum distance estimation in Chapter 14.

Readers who are not interested in general approaches to nonlinear estimation might use these chapters only when needed for reference in Part IV.

{352}------------------------------------------------