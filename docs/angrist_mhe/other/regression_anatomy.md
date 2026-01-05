# REGRESSION ANATOMY

> Pages: 42-45

<span id="page-42-0"></span>
$$\beta_{k} = \frac{Cov\left(\mathbf{Y}_{i}, \tilde{\mathbf{x}}_{ki}\right)}{V\left(\tilde{\mathbf{x}}_{ki}\right)},\tag{3.1.3}$$

where x~ki is the residual from a regression of xki on all the other covariates.

In other words, E XiX 0 i <sup>1</sup> E [Xiy<sup>i</sup> ] is the k-1 vector with k-th element Cov(yi;x~ki) V (~xki) . This important formula is said to describe the ìanatomy of a multivariate regression coe¢ cientî because it reveals much more than the matrix formula  = E -XiX 0 i <sup>1</sup> E [Xiy<sup>i</sup> ] : It shows us that each coe¢ cient in a multivariate regression is the bivariate slope coe¢ cient for the corresponding regressor, after "partialling out" all the other variables in the model.

To verify the regression-anatomy formula, substitute

$$\mathbf{Y}_i = \boldsymbol{\beta}_0 + \boldsymbol{\beta}_1 \boldsymbol{x}_{1i} + \dots + \boldsymbol{\beta}_k \boldsymbol{x}_{ki} + \dots + \boldsymbol{\beta}_{\mathbf{K}} \boldsymbol{x}_{\mathbf{K}i} + \boldsymbol{e}_i$$

in the numerator of [\(3.1.3\)](#page-42-0). Since x~ki is a linear combination of the regressors, it is uncorrelated with e<sup>i</sup> : Also, since x~ki is a residual from a regression on all the other covariates in the model, it must be uncorrelated these covariates. Finally, for the same reason, the covariance of x~ki with xki is just the variance of x~ki. We 

{43}------------------------------------------------

therefore have that Cov (y<sup>i</sup> ; x~ki) = <sup>k</sup>V (~xki): [2](#page-43-0)

The regression-anatomy formula is probably familiar to you from a regression or statistics course, perhaps with one twist: the regression coe¢ cients deÖned in this section are not estimators, but rather they are nonstochastic features of the joint distribution of dependent and independent variables. The joint distribution is what you would observe if you had a complete enumeration of the population of interest (or knew the stochastic process generating the data). You probably donít have such information. Still, itís kosheró even desirableó to think about what a set of population parameters might mean, without initially worrying about how to estimate them.

Below we discuss three reasons why the vector of population regression coe¢ cients might be of interest. These reasons can be summarized by saying that you are interested in regression parameters if you are interested in the CEF.

Theorem 3.1.4 The Linear CEF Theorem (Regression-justiÖcation I)

Suppose the CEF is linear. Then the population regression function is it.

Proof. Suppose E [y<sup>i</sup> jX<sup>i</sup> ] =X<sup>0</sup> i for a k-1 vector of coe¢ cients,  . Recall that E [X<sup>i</sup> (y<sup>i</sup> E [y<sup>i</sup> jX<sup>i</sup> ])] = 0 by the CEF-decomposition property. Substitute using E [y<sup>i</sup> jX<sup>i</sup> ] =X<sup>0</sup> i to Önd that  = E -XiX 0 i <sup>1</sup> E [Xiy<sup>i</sup> ] = .

The linear CEF theorem raises the question of under what circumstances a CEF is linear. The classic scenario is joint Normality, i.e., the vector (y<sup>i</sup> ; x<sup>0</sup> i ) 0 has a multivariate Normal distribution. This is the scenario considered by Galton (1886), father of regression, who was interested in the intergenerational link between Normally distributed traits such as height and intelligence. The Normal case is clearly of limited empirical relevance since regressors and dependent variables are often discrete, while Normal distributions are continuous. Another linearity scenario arises when regression models are saturated. As reviewed in Section [3.1.4,](#page-51-0) the saturated regression model has a separate parameter for every possible combination of values that the set of regressors can take on. For example a saturated regression model with two dummy covariates includes both covariates (with coe¢ cients known as the main e§ects) and their product (known as an interaction term). Such models are inherently linear, a point we also discuss in Section [3.1.4.](#page-51-0)

$$\beta_k = \frac{Cov\left(\tilde{\mathbf{Y}}_{ki}, \tilde{\mathbf{x}}_{ki}\right)}{V\left(\tilde{\mathbf{x}}_{ki}\right)},$$

where yòki is the residual from a regression of y<sup>i</sup> on every covariate except xki. This works because the Ötted values removed from yòki are uncorrelated with x~ki. Often itís useful to plot yòki against x~ki; the slope of the least-squares Öt in this scatterplot is your estimate of the multivariate <sup>k</sup> , even though the plot is two-dimensional. Note, however, that itís not enough to partial the other covariates out of y<sup>i</sup> only. That is,

$$\frac{Cov\left(\mathbf{\tilde{Y}}_{ki},x_{ki}\right)}{V\left(x_{ki}\right)} = \left[\frac{Cov\left(\mathbf{\tilde{Y}}_{ki},\tilde{x}_{ki}\right)}{V\left(\tilde{x}_{ki}\right)}\right] \left[\frac{V\left(\tilde{x}_{ki}\right)}{V\left(x_{ki}\right)}\right] \neq \beta_{k},$$

unless xki is uncorrelated with the other covariates.

<span id="page-43-0"></span><sup>2</sup> The regression-anatomy formula is usually attributed to Frisch and Waugh (1933). You can also do regression anatomy this way:

{44}------------------------------------------------

The following two reasons for focusing on regression are relevant when the linear CEF theorem does not apply.

Theorem 3.1.5 The Best Linear Predictor Theorem (Regression-justiÖcation II)

The function X<sup>0</sup> <sup>i</sup> is the best linear predictor of y<sup>i</sup> given X<sup>i</sup> in a MMSE sense.

Proof.  = E[XiX<sup>0</sup> i ] <sup>1</sup>E[Xiy<sup>i</sup> ] solves the population least squares problem, [\(3.1.2\)](#page-42-1).

In other words, just as the CEF, E [y<sup>i</sup> jX<sup>i</sup> ], is the best (i.e., MMSE) predictor of y<sup>i</sup> given X<sup>i</sup> in the class of all functions of X<sup>i</sup> , the population regression function is the best we can do in the class of linear functions.

Theorem 3.1.6 The Regression-CEF Theorem (Regression-justiÖcation III)

The function X<sup>0</sup> <sup>i</sup> provides the MMSE linear approximation to E[y<sup>i</sup> jX<sup>i</sup> ], that is,

<span id="page-44-0"></span>
$$\beta = \underset{b}{\arg\min} E\{ (E[Y_i|X_i] - X_i'b)^2 \}.$$
(3.1.4)

Proof. Write

$$(\mathbf{Y}_{i} - \mathbf{X}_{i}'b)^{2} = \{(\mathbf{Y}_{i} - E[\mathbf{Y}_{i}|\mathbf{X}_{i}]) + (E[\mathbf{Y}_{i}|\mathbf{X}_{i}] - \mathbf{X}_{i}'b)\}^{2}$$

$$= (\mathbf{Y}_{i} - E[\mathbf{Y}_{i}|\mathbf{X}_{i}])^{2} + (E[\mathbf{Y}_{i}|\mathbf{X}_{i}] - \mathbf{X}_{i}'b)^{2}$$

$$+ 2(\mathbf{Y}_{i} - E[\mathbf{Y}_{i}|\mathbf{X}_{i}])(E[\mathbf{Y}_{i}|\mathbf{X}_{i}] - \mathbf{X}_{i}'b).$$

The Örst term doesnít involve b and the last term has expectation zero by the CEF-decomposition property (ii). The CEF-approximation problem, [\(3.1.4\)](#page-44-0), therefore has the same solution as the population least squares problem, [\(3.1.2\)](#page-42-1).

These two theorems show us two more ways to view regression. Regression provides the best linear predictor for the dependent variable in the same way that the CEF is the best unrestricted predictor of the dependent variable. On the other hand, if we prefer to think about approximating E[y<sup>i</sup> jX<sup>i</sup> ], as opposed to predicting y<sup>i</sup> , the Regression-CEF theorem tells us that even if the CEF is nonlinear, regression provides the best linear approximation to it.

The regression-CEF theorem is our favorite way to motivate regression. The statement that regression approximates the CEF lines up with our view of empirical work as an e§ort to describe the essential features of statistical relationships, without necessarily trying to pin them down exactly. The linear CEF theorem is for special cases only. The best linear predictor theorem is satisfyingly general, but it encourages an overly clinical view of empirical research. Weíre not really interested in predicting individual y<sup>i</sup> ; itís the distribution of y<sup>i</sup> that we care about.

Figure [3.1.2](#page-46-0) illustrates the CEF approximation property for the same schooling CEF plotted in Figure [3.1.1.](#page-39-0) The regression line Öts the somewhat bumpy and nonlinear CEF as if we were estimating a model 

{45}------------------------------------------------

for  $E[Y_i|X_i]$  instead of a model for  $Y_i$ . In fact, that is exactly what's going on. An implication of the regression-CEF theorem is that regression coefficients can be obtained by using  $E[Y_i|X_i]$  as a dependent variable instead of  $Y_i$  itself. To see this, suppose that  $X_i$  is a discrete random variable with probability mass function,  $g_x(u)$  when  $X_i = u$ . Then

$$E\{(E[Y_i|X_i] - X_i'b)^2\} = \sum_{u} (E[Y_i|X_i = u] - u'b)^2 g_x(u).$$

This means that  $\beta$  can be constructed from the weighted least squares regression of  $E[Y_i|X_i=u]$  on u, where u runs over the values taken on by  $X_i$ . The weights are given by the distribution of  $X_i$ , i.e.,  $g_x(u)$  when  $X_i = u$ . Another way to see this is to iterate expectations in the formula for  $\beta$ :

$$\beta = E[X_i X_i']^{-1} E[X_i Y_i] = E[X_i X_i']^{-1} E[X_i E(Y_i | X_i)]. \tag{3.1.5}$$

The CEF or grouped-data version of the regression formula is of practical use when working on a project that precludes the analysis of micro data. For example, Angrist (1998), studies the effect of voluntary military service on earnings later in life. One of the estimation strategies used in this project regresses civilian earnings on a dummy for veteran status, along with personal characteristics and the variables used by the military to screen soldiers. The earnings data come from the US Social Security system, but Social Security earnings records cannot be released to the public. Instead of individual earnings, Angrist worked with average earnings conditional on race, sex, test scores, education, and veteran status.

An illustration of the grouped-data approach to regression appears below. We estimated the schooling coefficient in a wage equation using 21 conditional means, the sample CEF of earnings given schooling. As the Stata output reported here shows, a grouped-data regression, weighted by the number of individuals at each schooling level in the sample, produces coefficients identical to what would be obtained using the underlying microdata sample with hundreds of thousands of observations. Note, however, that the standard errors from the grouped regression do not correctly reflect the asymptotic sampling variance of the slope estimate in repeated micro-data samples; for that you need an estimate of the variance of  $Y_i - X_i'\beta$ . This variance depends on the microdata, in particular, the second-moments of  $W_i \equiv \begin{bmatrix} Y_i; & X_i' \end{bmatrix}'$ , a point we elaborate on in the next section.