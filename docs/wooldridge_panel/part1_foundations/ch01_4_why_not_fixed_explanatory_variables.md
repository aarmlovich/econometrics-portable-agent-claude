# Why Not Fixed Explanatory Variables?

> Pages: 27-31

We have seen two examples where, generally speaking, the error in an equation can be correlated with one or more of the explanatory variables. This possibility is

{28}------------------------------------------------

so prevalent in social science applications that it makes little sense to adopt an assumption—namely, the assumption of fixed explanatory variables—that rules out such correlation a priori.

In a first course in econometrics, the method of ordinary least squares (OLS) and its extensions are usually learned under the fixed regressor assumption. This is appropriate for understanding the mechanics of least squares and for gaining experience with statistical derivations. Unfortunately, reliance on fixed regressors or, more generally, fixed ''exogenous'' variables, can have unintended consequences, especially in more advanced settings. For example, in Chapters 7, 10, and 11 we will see that assuming fixed regressors or fixed instrumental variables in panel data models imposes often unrealistic restrictions on dynamic economic behavior. This is not just a technical point: estimation methods that are consistent under the fixed regressor assumption, such as generalized least squares, are no longer consistent when the fixed regressor assumption is relaxed in interesting ways.

To illustrate the shortcomings of the fixed regressor assumption in a familiar context, consider a linear model for cross section data, written for each observation i as

$$y_i = \beta_0 + \mathbf{x}_i \boldsymbol{\beta} + u_i, \qquad i = 1, 2, \dots, N$$

where x<sup>i</sup> is a 1 K vector and *b* is a K 1 vector. It is common to see the ''ideal'' assumptions for this model stated as ''The errors fui: i ¼ 1; 2; ... ; Ng are i.i.d. with EðuiÞ ¼ 0 and VarðuiÞ ¼ s2.'' (Sometimes the ui are also assumed to be normally distributed.) The problem with this statement is that it omits the most important consideration: What is assumed about the relationship between ui and xi? If the x<sup>i</sup> are taken as nonrandom—which, evidently, is very often the implicit assumption—then ui and x<sup>i</sup> are independent of one another. In nonexperimental environments this assumption rules out too many situations of interest. Some important questions, such as efficiency comparisons across models with different explanatory variables, cannot even be asked in the context of fixed regressors. (See Problems 4.5 and 4.15 of Chapter 4 for specific examples.)

In a random sampling context, the ui are always independent and identically distributed, regardless of how they are related to the xi. Assuming that the population mean of the error is zero is without loss of generality when an intercept is included in the model. Thus, the statement ''The errors fui: i ¼ 1; 2; ... ; Ng are i.i.d. with EðuiÞ ¼ 0 and VarðuiÞ ¼ s2'' is vacuous in a random sampling context. Viewing the x<sup>i</sup> as random draws along with yi forces us to think about the relationship between the error and the explanatory variables in the population. For example, in the population model y ¼ b<sup>0</sup> þ x*b* þ u, is the expected value of u given x equal to zero? Is u correlated with one or more elements of x? Is the variance of u given x constant, or

{29}------------------------------------------------

does it depend on x? These are the assumptions that are relevant for estimating *b* and for determining how to perform statistical inference.

Because our focus is on asymptotic analysis, we have the luxury of allowing for random explanatory variables throughout the book, whether the setting is linear models, nonlinear models, single-equation analysis, or system analysis. An incidental but nontrivial benefit is that, compared with frameworks that assume fixed explanatory variables, the unifying theme of random sampling actually simplifies the asymptotic analysis. We will never state assumptions in terms of full data matrices, because such assumptions can be imprecise and can impose unintended restrictions on the population model.

{30}------------------------------------------------

#### 2.1 The Role of Conditional Expectations in Econometrics

As we suggested in Section 1.1, the conditional expectation plays a crucial role in modern econometric analysis. Although it is not always explicitly stated, the goal of most applied econometric studies is to estimate or test hypotheses about the expectation of one variable—called the explained variable, the dependent variable, the regressand, or the response variable, and usually denoted y—conditional on a set of explanatory variables, independent variables, regressors, control variables, or covariates, usually denoted x ¼ ðx1; x2; ... ; xK Þ.

A substantial portion of research in econometric methodology can be interpreted as finding ways to estimate conditional expectations in the numerous settings that arise in economic applications. As we briefly discussed in Section 1.1, most of the time we are interested in conditional expectations that allow us to infer causality from one or more explanatory variables to the response variable. In the setup from Section 1.1, we are interested in the effect of a variable w on the expected value of y, holding fixed a vector of controls, c. The conditional expectation of interest is Eðy j w; cÞ, which we will call a structural conditional expectation. If we can collect data on y, w, and c in a random sample from the underlying population of interest, then it is fairly straightforward to estimate Eðy j w; cÞ—especially if we are willing to make an assumption about its functional form—in which case the effect of w on Eðy j w; cÞ, holding c fixed, is easily estimated.

Unfortunately, complications often arise in the collection and analysis of economic data because of the nonexperimental nature of economics. Observations on economic variables can contain measurement error, or they are sometimes properly viewed as the outcome of a simultaneous process. Sometimes we cannot obtain a random sample from the population, which may not allow us to estimate Eðy j w; cÞ. Perhaps the most prevalent problem is that some variables we would like to control for (elements of c) cannot be observed. In each of these cases there is a conditional expectation (CE) of interest, but it generally involves variables for which the econometrician cannot collect data or requires an experiment that cannot be carried out.

Under additional assumptions—generally called identification assumptions—we can sometimes recover the structural conditional expectation originally of interest, even if we cannot observe all of the desired controls, or if we only observe equilibrium outcomes of variables. As we will see throughout this text, the details differ depending on the context, but the notion of conditional expectation is fundamental.

In addition to providing a unified setting for interpreting economic models, the CE operator is useful as a tool for manipulating structural equations into estimable equations. In the next section we give an overview of the important features of the


{31}------------------------------------------------

conditional expectations operator. The appendix to this chapter contains a more extensive list of properties.

# 2.2 Features of Conditional Expectations