

{21}------------------------------------------------

## 1.1 Causal Relationships and Ceteris Paribus Analysis

The goal of most empirical studies in economics and other social sciences is to determine whether a change in one variable, say w, causes a change in another variable, say y. For example, does having another year of education cause an increase in monthly salary? Does reducing class size cause an improvement in student performance? Does lowering the business property tax rate cause an increase in city economic activity? Because economic variables are properly interpreted as random variables, we should use ideas from probability to formalize the sense in which a change in w causes a change in y.

The notion of ceteris paribus—that is, holding all other (relevant) factors fixed—is at the crux of establishing a causal relationship. Simply finding that two variables are correlated is rarely enough to conclude that a change in one variable causes a change in another. This result is due to the nature of economic data: rarely can we run a controlled experiment that allows a simple correlation analysis to uncover causality. Instead, we can use econometric methods to effectively hold other factors fixed.

If we focus on the average, or expected, response, a ceteris paribus analysis entails estimating Eðy j w; cÞ, the expected value of y conditional on w and c. The vector c whose dimension is not important for this discussion—denotes a set of control variables that we would like to explicitly hold fixed when studying the effect of w on the expected value of y. The reason we control for these variables is that we think w is correlated with other factors that also influence y. If w is continuous, interest centers on qEðy j w; cÞ=qw, which is usually called the partial effect of w on Eðy j w; cÞ. If w is discrete, we are interested in Eðy j w; cÞ evaluated at different values of w, with the elements of c fixed at the same specified values.

Deciding on the list of proper controls is not always straightforward, and using different controls can lead to different conclusions about a causal relationship between y and w. This is where establishing causality gets tricky: it is up to us to decide which factors need to be held fixed. If we settle on a list of controls, and if all elements of c can be observed, then estimating the partial effect of w on Eðy j w; cÞ is relatively straightforward. Unfortunately, in economics and other social sciences, many elements of c are not observed. For example, in estimating the causal effect of education on wage, we might focus on Eðwage j educ; exper; abilÞ where educ is years of schooling, exper is years of workforce experience, and abil is innate ability. In this case, c ¼ ðexper; abilÞ, where exper is observed but abil is not. (It is widely agreed among labor economists that experience and ability are two factors we should hold fixed to obtain the causal effect of education on wages. Other factors, such as years

{22}------------------------------------------------

with the current employer, might belong as well. We can all agree that something such as the last digit of one's social security number need not be included as a control, as it has nothing to do with wage or education.)

As a second example, consider establishing a causal relationship between student attendance and performance on a final exam in a principles of economics class. We might be interested in Eðscore j attend; SAT; priGPAÞ, where score is the final exam score, attend is the attendance rate, SAT is score on the scholastic aptitude test, and priGPA is grade point average at the beginning of the term. We can reasonably collect data on all of these variables for a large group of students. Is this setup enough to decide whether attendance has a causal effect on performance? Maybe not. While SAT and priGPA are general measures reflecting student ability and study habits, they do not necessarily measure one's interest in or aptitude for econonomics. Such attributes, which are difficult to quantify, may nevertheless belong in the list of controls if we are going to be able to infer that attendance rate has a causal effect on performance.

In addition to not being able to obtain data on all desired controls, other problems can interfere with estimating causal relationships. For example, even if we have good measures of the elements of c, we might not have very good measures of y or w. A more subtle problem—which we study in detail in Chapter 9—is that we may only observe equilibrium values of y and w when these variables are simultaneously determined. An example is determining the causal effect of conviction rates ðwÞ on city crime rates ðyÞ.

A first course in econometrics teaches students how to apply multiple regression analysis to estimate ceteris paribus effects of explanatory variables on a response variable. In the rest of this book, we will study how to estimate such effects in a variety of situations. Unlike most introductory treatments, we rely heavily on conditional expectations. In Chapter 2 we provide a detailed summary of properties of conditional expectations.

#### 1.2 The Stochastic Setting and Asymptotic Analysis

#### 1.2.1 Data Structures

In order to give proper treatment to modern cross section and panel data methods, we must choose a stochastic setting that is appropriate for the kinds of cross section and panel data sets collected for most econometric applications. Naturally, all else equal, it is best if the setting is as simple as possible. It should allow us to focus on

{23}------------------------------------------------

interpreting assumptions with economic content while not having to worry too much about technical regularity conditions. (Regularity conditions are assumptions involving things such as the number of absolute moments of a random variable that must be finite.)

For much of this book we adopt a random sampling assumption. More precisely, we assume that (1) a population model has been specified and (2) an independent, identically distributed (i.i.d.) sample can be drawn from the population. Specifying a population model—which may be a model of Eðy j w; cÞ, as in Section 1.1—requires us first to clearly define the population of interest. Defining the relevant population may seem to be an obvious requirement. Nevertheless, as we will see in later chapters, it can be subtle in some cases.

An important virtue of the random sampling assumption is that it allows us to separate the sampling assumption from the assumptions made on the population model. In addition to putting the proper emphasis on assumptions that impinge on economic behavior, stating all assumptions in terms of the population is actually much easier than the traditional approach of stating assumptions in terms of full data matrices.

Because we will rely heavily on random sampling, it is important to know what it allows and what it rules out. Random sampling is often reasonable for cross section data, where, at a given point in time, units are selected at random from the population. In this setup, any explanatory variables are treated as random outcomes along with data on response variables. Fixed regressors cannot be identically distributed across observations, and so the random sampling assumption technically excludes the classical linear model. This result is actually desirable for our purposes. In Section 1.4 we provide a brief discussion of why it is important to treat explanatory variables as random for modern econometric analysis.

We should not confuse the random sampling assumption with so-called experimental data. Experimental data fall under the fixed explanatory variables paradigm. With experimental data, researchers set values of the explanatory variables and then observe values of the response variable. Unfortunately, true experiments are quite rare in economics, and in any case nothing practically important is lost by treating explanatory variables that are set ahead of time as being random. It is safe to say that no one ever went astray by assuming random sampling in place of independent sampling with fixed explanatory variables.

Random sampling does exclude cases of some interest for cross section analysis. For example, the identical distribution assumption is unlikely to hold for a pooled cross section, where random samples are obtained from the population at different

{24}------------------------------------------------

points in time. This case is covered by independent, not identically distributed (i.n.i.d.) observations. Allowing for non-identically distributed observations under independent sampling is not difficult, and its practical effects are easy to deal with. We will mention this case at several points in the book after the analyis is done under random sampling. We do not cover the i.n.i.d. case explicitly in derivations because little is to be gained from the additional complication.

A situation that does require special consideration occurs when cross section observations are not independent of one another. An example is spatial correlation models. This situation arises when dealing with large geographical units that cannot be assumed to be independent draws from a large population, such as the 50 states in the United States. It is reasonable to expect that the unemployment rate in one state is correlated with the unemployment rate in neighboring states. While standard estimation methods—such as ordinary least squares and two-stage least squares—can usually be applied in these cases, the asymptotic theory needs to be altered. Key statistics often (although not always) need to be modified. We will briefly discuss some of the issues that arise in this case for single-equation linear models, but otherwise this subject is beyond the scope of this book. For better or worse, spatial correlation is often ignored in applied work because correcting the problem can be difficult.

Cluster sampling also induces correlation in a cross section data set, but in most cases it is relatively easy to deal with econometrically. For example, retirement saving of employees within a firm may be correlated because of common (often unobserved) characteristics of workers within a firm or because of features of the firm itself (such as type of retirement plan). Each firm represents a group or cluster, and we may sample several workers from a large number of firms. As we will see later, provided the number of clusters is large relative to the cluster sizes, standard methods can correct for the presence of within-cluster correlation.

Another important issue is that cross section samples often are, either intentionally or unintentionally, chosen so that they are not random samples from the population of interest. In Chapter 17 we discuss such problems at length, including sample selection and stratified sampling. As we will see, even in cases of nonrandom samples, the assumptions on the population model play a central role.

For panel data (or longitudinal data), which consist of repeated observations on the same cross section of, say, individuals, households, firms, or cities, over time, the random sampling assumption initially appears much too restrictive. After all, any reasonable stochastic setting should allow for correlation in individual or firm behavior over time. But the random sampling assumption, properly stated, does allow for temporal correlation. What we will do is assume random sampling in the cross

{25}------------------------------------------------

section dimension. The dependence in the time series dimension can be entirely unrestricted. As we will see, this approach is justified in panel data applications with many cross section observations spanning a relatively short time period. We will also be able to cover panel data sample selection and stratification issues within this paradigm.

A panel data setup that we will not adequately cover—although the estimation methods we cover can be usually used—is seen when the cross section dimension and time series dimensions are roughly of the same magnitude, such as when the sample consists of countries over the post–World War II period. In this case it makes little sense to fix the time series dimension and let the cross section dimension grow. The research on asymptotic analysis with these kinds of panel data sets is still in its early stages, and it requires special limit theory. See, for example, Quah (1994), Pesaran and Smith (1995), Kao (1999), and Phillips and Moon (1999).

## 1.2.2 Asymptotic Analysis

Throughout this book we focus on asymptotic properties, as opposed to finite sample properties, of estimators. The primary reason for this emphasis is that finite sample properties are intractable for most of the estimators we study in this book. In fact, most of the estimators we cover will not have desirable finite sample properties such as unbiasedness. Asymptotic analysis allows for a unified treatment of estimation procedures, and it (along with the random sampling assumption) allows us to state all assumptions in terms of the underlying population. Naturally, asymptotic analysis is not without its drawbacks. Occasionally, we will mention when asymptotics can lead one astray. In those cases where finite sample properties can be derived, you are sometimes asked to derive such properties in the problems.

In cross section analysis the asymptotics is as the number of observations, denoted N throughout this book, tends to infinity. Usually what is meant by this statement is obvious. For panel data analysis, the asymptotics is as the cross section dimension gets large while the time series dimension is fixed.

## 1.3 Some Examples

In this section we provide two examples to emphasize some of the concepts from the previous sections. We begin with a standard example from labor economics.

Example 1.1 (Wage Offer Function): Suppose that the natural log of the wage offer, wage<sup>o</sup>, is determined as

{26}------------------------------------------------

$$\log(wage^o) = \beta_0 + \beta_1 educ + \beta_2 exper + \beta_3 married + u \tag{1.1}$$

where educ is years of schooling, exper is years of labor market experience, and married is a binary variable indicating marital status. The variable u, called the error term or disturbance, contains unobserved factors that affect the wage offer. Interest lies in the unknown parameters, the bj.

We should have a concrete population in mind when specifying equation (1.1). For example, equation (1.1) could be for the population of all working women. In this case, it will not be difficult to obtain a random sample from the population.

All assumptions can be stated in terms of the population model. The crucial assumptions involve the relationship between u and the observable explanatory variables, educ, exper, and married. For example, is the expected value of u given the explanatory variables educ, exper, and married equal to zero? Is the variance of u conditional on the explanatory variables constant? There are reasons to think the answer to both of these questions is no, something we discuss at some length in Chapters 4 and 5. The point of raising them here is to emphasize that all such questions are most easily couched in terms of the population model.

What happens if the relevant population is all women over age 18? A problem arises because a random sample from this population will include women for whom the wage offer cannot be observed because they are not working. Nevertheless, we can think of a random sample being obtained, but then wage<sup>o</sup> is unobserved for women not working.

For deriving the properties of estimators, it is often useful to write the population model for a generic draw from the population. Equation (1.1) becomes

$$\log(wage_i^o) = \beta_0 + \beta_1 educ_i + \beta_2 exper_i + \beta_3 married_i + u_i, \tag{1.2}$$

where i indexes person. Stating assumptions in terms of ui and x<sup>i</sup> 1ðeduci; experi; marriediÞ is the same as stating assumptions in terms of u and x. Throughout this book, the i subscript is reserved for indexing cross section units, such as individual, firm, city, and so on. Letters such as j, g, and h will be used to index variables, parameters, and equations.

Before ending this example, we note that using matrix notation to write equation (1.2) for all N observations adds nothing to our understanding of the model or sampling scheme; in fact, it just gets in the way because it gives the mistaken impression that the matrices tell us something about the assumptions in the underlying population. It is much better to focus on the population model (1.1).

The next example is illustrative of panel data applications.

{27}------------------------------------------------

Example 1.2 (Effect of Spillovers on Firm Output): Suppose that the population is all manufacturing firms in a country operating during a given three-year period. A production function describing output in the population of firms is

$$\log(output_t) = \delta_t + \beta_1 \log(labor_t) + \beta_2 \log(capital_t)$$

$$+ \beta_3 spillover_t + quality + u_t, \qquad t = 1, 2, 3$$
(1.3)

Here, spillovert is a measure of foreign firm concentration in the region containing the firm. The term quality contains unobserved factors—such as unobserved managerial or worker quality—which affect productivity and are constant over time. The error ut represents unobserved shocks in each time period. The presence of the parameters dt, which represent different intercepts in each year, allows for aggregate productivity to change over time. The coefficients on labort, capitalt, and spillovert are assumed constant across years.

As we will see when we study panel data methods, there are several issues in deciding how best to estimate the bj. An important one is whether the unobserved productivity factors (quality) are correlated with the observable inputs. Also, can we assume that spillovert at, say, t ¼ 3 is uncorrelated with the error terms in all time periods?

For panel data it is especially useful to add an i subscript indicating a generic cross section observation—in this case, a randomly sampled firm:

$$\log(output_{it}) = \delta_t + \beta_1 \log(labor_{it}) + \beta_2 \log(capital_{it})$$

$$+ \beta_3 spillover_{it} + quality_i + u_{it}, \qquad t = 1, 2, 3$$
(1.4)

Equation (1.4) makes it clear that qualityi is a firm-specific term that is constant over time and also has the same effect in each time period, while uit changes across time and firm. Nevertheless, the key issues that we must address for estimation can be discussed for a generic i, since the draws are assumed to be randomly made from the population of all manufacturing firms.

Equation (1.4) is an example of another convention we use throughout the book: the subscript t is reserved to index time, just as i is reserved for indexing the cross section.

### 1.4 Why Not Fixed Explanatory Variables?

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