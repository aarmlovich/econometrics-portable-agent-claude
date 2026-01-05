# Tests against More General Alternatives

> Pages: 472-479

In addition to testing for omitted variables, sometimes we wish to test the probit or logit model against a more general functional form. When the alternatives are not standard binary response models, the Wald and LR statistics are cumbersome to apply, whereas the LM approach is convenient because it only requires estimation of the null model.

As an example of a more complicated binary choice model, consider the latent variable model (15.9) but assume that  $e \mid \mathbf{x} \sim \text{Normal}[0, \exp(2\mathbf{x}_1\boldsymbol{\delta})]$ , where  $\mathbf{x}_1$  is  $1 \times K_1$  subset of  $\mathbf{x}$  that excludes a constant and  $\boldsymbol{\delta}$  is a  $K_1 \times 1$  vector of additional parameters. (In many cases we would take  $\mathbf{x}_1$  to be all nonconstant elements of  $\mathbf{x}$ .) Therefore, there is heteroskedasticity in the latent variable model, so that e is no longer independent of  $\mathbf{x}$ . The standard deviation of e given  $\mathbf{x}$  is simply  $\exp(\mathbf{x}_1\boldsymbol{\delta})$ . Define  $r = e/\exp(\mathbf{x}_1\boldsymbol{\delta})$ , so that r is independent of  $\mathbf{x}$  with a standard normal distribution. Then

{473}------------------------------------------------

$$P(y = 1 \mid \mathbf{x}) = P(e > -\mathbf{x}\boldsymbol{\beta} \mid \mathbf{x}) = P[\exp(-\mathbf{x}_1\boldsymbol{\delta})e > -\exp(-\mathbf{x}_1\boldsymbol{\delta})\mathbf{x}\boldsymbol{\beta}]$$
$$= P[r > -\exp(-\mathbf{x}_1\boldsymbol{\delta})\mathbf{x}\boldsymbol{\beta}] = \Phi[\exp(-\mathbf{x}_1\boldsymbol{\delta})\mathbf{x}\boldsymbol{\beta}]$$
(15.24)

The partial effects of  $x_j$  on  $P(y = 1 | \mathbf{x})$  are much more complicated in equation (15.24) than in equation (15.8). When  $\delta = \mathbf{0}$ , we obtain the standard probit model. Therefore, a test of the probit functional form for the response probability is a test of  $H_0$ :  $\delta = \mathbf{0}$ .

To obtain the LM test of  $\delta = 0$  in equation (15.24), it is useful to derive the LM test for an index model against a more general alternative. Consider

$$P(y = 1 \mid \mathbf{x}) = m(\mathbf{x}\boldsymbol{\beta}, \mathbf{x}, \boldsymbol{\delta})$$
 (15.25)

where  $\delta$  is a  $Q \times 1$  vector of parameters. We wish to test  $H_0$ :  $\delta = \delta_0$ , where  $\delta_0$  is often (but not always) a vector of zeros. We assume that, under the null, we obtain a standard index model (probit or logit, usually):

$$G(\mathbf{x}\boldsymbol{\beta}) = m(\mathbf{x}\boldsymbol{\beta}, \mathbf{x}, \boldsymbol{\delta}_0) \tag{15.26}$$

In the previous example,  $G(\cdot) = \Phi(\cdot)$ ,  $\delta_0 = 0$ , and  $m(\mathbf{x}\boldsymbol{\beta}, \mathbf{x}, \boldsymbol{\delta}) = \Phi[\exp(-\mathbf{x}_1\boldsymbol{\delta})\mathbf{x}\boldsymbol{\beta}]$ .

Let  $\hat{\boldsymbol{\beta}}$  be the probit or logit estimator of  $\boldsymbol{\beta}$  obtained under  $\boldsymbol{\delta} = \boldsymbol{\delta}_0$ . Define  $\hat{\boldsymbol{u}}_i \equiv y_i - G(\mathbf{x}_i\hat{\boldsymbol{\beta}})$ ,  $\hat{G}_i \equiv G(\mathbf{x}_i\hat{\boldsymbol{\beta}})$ , and  $\hat{g}_i \equiv g(\mathbf{x}_i\hat{\boldsymbol{\beta}})$ . The gradient of the mean function  $m(\mathbf{x}_i\boldsymbol{\beta},\mathbf{x}_i,\boldsymbol{\delta})$  with respect to  $\boldsymbol{\beta}$ , evaluated at  $\boldsymbol{\delta}_0$ , is simply  $g(\mathbf{x}_i\boldsymbol{\beta})\mathbf{x}_i$ . The only other piece we need is the gradient of  $m(\mathbf{x}_i\boldsymbol{\beta},\mathbf{x}_i,\boldsymbol{\delta})$  with respect to  $\boldsymbol{\delta}$ , evaluated at  $\boldsymbol{\delta}_0$ . Denote this  $1 \times Q$  vector as  $\nabla_{\delta}m(\mathbf{x}_i\boldsymbol{\beta},\mathbf{x}_i,\boldsymbol{\delta}_0)$ . Further, set  $\nabla_{\delta}\hat{m}_i \equiv \nabla_{\delta}m(\mathbf{x}_i\hat{\boldsymbol{\beta}},\mathbf{x}_i,\boldsymbol{\delta}_0)$ . The LM statistic can be obtained as the explained sum of squares or  $NR_u^2$  from the regression

$$\frac{\hat{u}_i}{\sqrt{\hat{G}_i(1-\hat{G}_i)}} \text{ on } \frac{\hat{g}_i}{\sqrt{\hat{G}_i(1-\hat{G}_i)}} \mathbf{x}_i, \qquad \frac{\nabla_{\delta} \hat{m}_i}{\sqrt{\hat{G}_i(1-\hat{G}_i)}}$$
(15.27)

which is quite similar to regression (15.22). The null distribution of the LM statistic is  $\chi_Q^2$ , where Q is the dimension of  $\delta$ .

When applying this test to the preceding probit example, we have only  $\nabla_{\delta}\hat{m}_i$  left to compute. But  $m(\mathbf{x}_i\boldsymbol{\beta},\mathbf{x}_i,\boldsymbol{\delta}) = \Phi[\exp(-\mathbf{x}_{il}\boldsymbol{\delta})\mathbf{x}_i\boldsymbol{\beta}]$ , and so

$$\nabla_{\delta} m(\mathbf{x}_{i}\boldsymbol{\beta}, \mathbf{x}_{i}, \boldsymbol{\delta}) = -(\mathbf{x}_{i}\boldsymbol{\beta}) \exp(-\mathbf{x}_{i1}\boldsymbol{\delta}) \mathbf{x}_{i1} \phi [\exp(-\mathbf{x}_{i1}\boldsymbol{\delta}) \mathbf{x}_{i}\boldsymbol{\beta}]$$

When evaluated at  $\beta = \hat{\beta}$  and  $\delta = 0$  (the null value), we get  $\nabla_{\delta} \hat{m}_i = -(\mathbf{x}_i \hat{\beta}) \phi(\mathbf{x}_i \hat{\beta}) \mathbf{x}_{i1}$  $\equiv -(\mathbf{x}_i \hat{\beta}) \hat{\phi}_i \mathbf{x}_{i1}$ , a 1 ×  $K_1$  vector. Regression (15.27) becomes

$$\frac{\hat{u}_i}{\sqrt{\hat{\Phi}_i(1-\hat{\Phi}_i)}} \text{ on } \frac{\hat{\phi}_i}{\sqrt{\hat{\Phi}_i(1-\hat{\Phi}_i)}} \mathbf{x}_i, \qquad \frac{(\mathbf{x}_i\hat{\boldsymbol{\beta}})\hat{\phi}_i}{\sqrt{\hat{\Phi}_i(1-\hat{\Phi}_i)}} \mathbf{x}_{i1}$$
(15.28)

{474}------------------------------------------------

(We drop the minus sign because it does not affect the value of the explained sum of squares or  $R_u^2$ .) Under the null hypothesis that the probit model is correctly specified,  $LM \sim \chi_{K_1}^2$ . This statistic is easy to compute after estimation by probit.

For a one-degree-of-freedom test regardless of the dimension of  $\mathbf{x}_i$ , replace the last term in regression (15.28) with  $(\mathbf{x}_i\hat{\boldsymbol{\beta}})^2\hat{\phi}_i/\sqrt{\hat{\Phi}_i(1-\hat{\Phi}_i)}$ , and then the explained sum of squares is distributed asymptotically as  $\chi_1^2$ . See Davidson and MacKinnon (1984) for further examples.

#### 15.6 Reporting the Results for Probit and Logit

Several statistics should be reported routinely in any probit or logit (or other binary choice) analysis. The  $\hat{\beta}_j$ , their standard errors, and the value of the likelihood function are reported by all software packages that do binary response analysis. The  $\hat{\beta}_j$  give the signs of the partial effects of each  $x_j$  on the response probability, and the statistical significance of  $x_j$  is determined by whether we can reject  $H_0$ :  $\beta_j = 0$ .

One measure of goodness of fit that is usually reported is the **percent correctly predicted**. For each i, we compute the predicted probability that  $y_i = 1$ , given the explanatory variables,  $\mathbf{x}_i$ . If  $G(\mathbf{x}_i\hat{\boldsymbol{\beta}}) > .5$ , we predict  $y_i$  to be unity; if  $G(\mathbf{x}_i\hat{\boldsymbol{\beta}}) \leq .5$ ,  $y_i$  is predicted to be zero. The percentage of times the predicted  $y_i$  matches the actual  $y_i$  is the percent correctly predicted. In many cases it is easy to predict one of the outcomes and much harder to predict another outcome, in which case the percent correctly predicted can be misleading as a goodness-of-fit statistic. More informative is to compute the percent correctly predicted for each outcome, y = 0 and y = 1. The overall percent correctly predicted is a weighted average of the two, with the weights being the fractions of zero and one outcomes, respectively. Problem 15.7 provides an illustration.

Various **pseudo R-squared** measures have been proposed for binary response. McFadden (1974) suggests the measure  $1 - \mathcal{L}_{ur}/\mathcal{L}_o$ , where  $\mathcal{L}_{ur}$  is the log-likelihood function for the estimated model and  $\mathcal{L}_o$  is the log-likelihood function in the model with only an intercept. Because the log likelihood for a binary response model is always negative,  $|\mathcal{L}_{ur}| \leq |\mathcal{L}_o|$ , and so the pseudo R-squared is always between zero and one. Alternatively, we can use a sum of squared residuals measure:  $1 - \text{SSR}_{ur}/\text{SSR}_o$ , where  $\text{SSR}_{ur}$  is the sum of squared residuals  $\hat{u}_i = y_i - G(\mathbf{x}_i\hat{\boldsymbol{\beta}})$  and  $\text{SSR}_o$  is the total sum of squares of  $y_i$ . Several other measures have been suggested (see, for example, Maddala, 1983, Chapter 2), but goodness of fit is not as important as statistical and economic significance of the explanatory variables. Estrella (1998) contains a recent comparison of goodness-of-fit measures for binary response.

{475}------------------------------------------------

Often we want to estimate the effects of the variables xj on the response probabilities Pðy ¼ 1 j xÞ. If xj is (roughly) continuous then

$$\Delta \hat{\mathbf{P}}(y = 1 \mid \mathbf{x}) \approx [g(\mathbf{x}\hat{\boldsymbol{\beta}})\hat{\beta}_j]\Delta x_j \tag{15.29}$$

for small changes in xj. (As usual when using calculus, the notion of ''small'' here is somewhat vague.) Since gðx ^*b*Þ depends on x, we must compute gðx ^*b*Þ at interesting values of x. Often the sample averages of the xj's are plugged in to get gðx ^*b*Þ. This factor can then be used to adjust each of the ^b<sup>j</sup> (at least those on continuous variables) to obtain the effect of a one-unit increase in xj. If x contains nonlinear functions of some explanatory variables, such as natural logs or quadratics, there is the issue of using the log of the average versus the average of the log (and similarly with quadratics). To get the effect for the ''average'' person, it makes more sense to plug the averages into the nonlinear functions, rather than average the nonlinear functions. Software packages (such as Stata with the dprobit command) necessarily average the nonlinear functions. Sometimes minimum and maximum values of key variables are used in obtaining gðx ^*b*Þ, so that we can see how the partial effects change as some elements of x get large or small.

Equation (15.29) also suggests how to roughly compare magnitudes of the probit and logit estimates. If x ^*b* is close to zero for logit and probit, the scale factor we use can be gð0Þ. For probit, gð0ÞA:4, and for logit, gð0Þ ¼ :25. Thus the logit estimates can be expected to be larger by a factor of about :4=:25 ¼ 1:6. Alternatively, multiply the logit estimates by .625 to make them comparable to the probit estimates. In the linear probability model, gð0Þ is unity, and so logit estimates should be divided by four to compare them with LPM estimates, while probit estimates should be divided by 2.5 to make them roughly comparable to LPM estimates. More accurate comparisons are obtained by using the scale factors gðx ^*b*Þ for probit and logit. Of course, one of the potential advantages of using probit or logit is that the partial effects vary with x, and it is of some interest to compute gðx ^*b*Þ at values of x other than the sample averages.

If, say, x<sup>2</sup> is a binary variable, it perhaps makes more sense to plug in zero or one for x2, rather than x<sup>2</sup> (which is the fraction of ones in the sample). Putting in the averages for the binary variables means that the effect does not really correspond to a particular individual. But often the results are similar, and the choice is really based on taste.

To obtain standard errors of the partial effects in equation (15.29) we use the delta method. Consider the case j ¼ K for notational simplicity, and for given x, define d<sup>K</sup> ¼ b<sup>K</sup> gðx*b*Þ ¼ qPðy ¼ 1 j xÞ=qxK . Write this relation as d<sup>K</sup> ¼ hð*b*Þ to denote that this is a (nonlinear) function of the vector *b*. We assume x<sup>1</sup> ¼ 1. The gradient of hð*b*Þ is

{476}------------------------------------------------

$$\nabla_{\beta}h(\boldsymbol{\beta}) = \left[\beta_K \frac{\mathrm{d}g}{\mathrm{d}z}(\mathbf{x}\boldsymbol{\beta}), \beta_K x_2 \frac{\mathrm{d}g}{\mathrm{d}z}(\mathbf{x}\boldsymbol{\beta}), \dots, \beta_K x_{K-1} \frac{\mathrm{d}g}{\mathrm{d}z}(\mathbf{x}\boldsymbol{\beta}), \beta_K x_K \frac{\mathrm{d}g}{\mathrm{d}z}(\mathbf{x}\boldsymbol{\beta}) + g(\mathbf{x}\boldsymbol{\beta})\right]$$

where dg/dz is simply the derivative of g with respect to its argument. The delta method implies that the asymptotic variance of  $\hat{\delta}_K$  is estimated as

$$[\nabla_{\beta}h(\hat{\boldsymbol{\beta}})]\hat{\mathbf{V}}[\nabla_{\beta}h(\hat{\boldsymbol{\beta}})]' \tag{15.30}$$

where  $\hat{\mathbf{V}}$  is the asymptotic variance estimate of  $\hat{\boldsymbol{\beta}}$ . The asymptotic standard error of  $\hat{\delta}_K$  is simply the square root of expression (15.30). This calculation allows us to obtain a large-sample confidence interval for  $\hat{\delta}_K$ . The program Stata does this calculation for the probit model using the *dprobit* command.

If  $x_K$  is a discrete variable, then we can estimate the change in the predicted probability in going from  $c_K$  to  $c_K + 1$  as

$$\hat{\delta}_K = G[\hat{\beta}_1 + \hat{\beta}_2 \bar{x}_2 + \dots + \hat{\beta}_{K-1} \bar{x}_{K-1} + \hat{\beta}_K (c_K + 1)] - G(\hat{\beta}_1 + \hat{\beta}_2 \bar{x}_2 + \dots + \hat{\beta}_{K-1} \bar{x}_{K-1} + \hat{\beta}_K c_K)$$
(15.31)

In particular, when  $x_K$  is a binary variable, set  $c_K = 0$ . Of course, the other  $x_j$ 's can be evaluated anywhere, but the use of sample averages is typical. The delta method can be used to obtain a standard error of equation (15.31). For probit, Stata does this calculation when  $x_K$  is a binary variable. Usually the calculations ignore the fact that  $\bar{x}_j$  is an estimate of  $E(x_j)$  in applying the delta method. If we are truly interested in  $\beta_K g(\mu_x \beta)$ , the estimation error in  $\bar{x}$  can be accounted for, but it makes the calculation more complicated, and it is unlikely to have a large effect.

An alternative way to summarize the estimated marginal effects is to estimate the average value of  $\beta_K g(\mathbf{x}\boldsymbol{\beta})$  across the population, or  $\beta_K \mathrm{E}[g(\mathbf{x}\boldsymbol{\beta})]$ . A consistent estimator is

$$\hat{\boldsymbol{\beta}}_{K} \left[ N^{-1} \sum_{i=1}^{N} g(\mathbf{x}_{i} \hat{\boldsymbol{\beta}}) \right]$$
 (15.32)

when  $x_K$  is continuous or

$$N^{-1} \sum_{i=1}^{N} \left[ G(\hat{\beta}_{1} + \hat{\beta}_{2} x_{i2} + \dots + \hat{\beta}_{K-1} x_{i,K-1} + \hat{\beta}_{K}) - G(\hat{\beta}_{1} + \hat{\beta}_{2} x_{i2} + \dots + \hat{\beta}_{K-1} x_{i,K-1}) \right]$$
(15.33)

if  $x_K$  is binary. The delta method can be used to obtain an asymptotic standard error of expression (15.32) or (15.33). Costa (1995) is a recent example of average effects obtained from expression (15.33).

{477}------------------------------------------------

Table 15.1 LPM, Logit, and Probit Estimates of Labor Force Participation

<table><tbody><tr><th colspan="4">Dependent Variable: inlf</th></tr><tr><th>Independent Variable</th><th>LPM</th><th>Logit</th><th>Probit</th></tr><tr><td></td><td>(OLS)</td><td>(MLE)</td><td>(MLE)</td></tr><tr><td>nwifeinc</td><td>.0034</td><td>.021</td><td>.012</td></tr><tr><td></td><td>(.0015)</td><td>(.008)</td><td>(.005)</td></tr><tr><td>educ</td><td>.038</td><td>.221</td><td>.131</td></tr><tr><td></td><td>(.007)</td><td>(.043)</td><td>(.025)</td></tr><tr><td>exper</td><td>.039</td><td>.206</td><td>.123</td></tr><tr><td></td><td>(.006)</td><td>(.032)</td><td>(.019)</td></tr><tr><td>exper2</td><td>.00060</td><td>.0032</td><td>.0019</td></tr><tr><td></td><td>(.00019)</td><td>(.0010)</td><td>(.0006)</td></tr><tr><td>age</td><td>.016</td><td>.088</td><td>.053</td></tr><tr><td></td><td>(.002)</td><td>(.015)</td><td>(.008)</td></tr><tr><td>kidslt6</td><td>.262</td><td>1.443</td><td>.868</td></tr><tr><td></td><td>(.032)</td><td>(0.204)</td><td>(.119)</td></tr><tr><td>kidsge6</td><td>.013</td><td>.060</td><td>.036</td></tr><tr><td></td><td>(.013)</td><td>(.075)</td><td>(.043)</td></tr><tr><td>constant</td><td>.586</td><td>.425</td><td>.270</td></tr><tr><td></td><td>(.151)</td><td>(.860)</td><td>(.509)</td></tr><tr><td>Number of observations</td><td>753</td><td>753</td><td>753</td></tr><tr><td>Percent correctly predicted</td><td>73.4</td><td>73.6</td><td>73.4</td></tr><tr><td>Log-likelihood value</td><td>—</td><td>401.77</td><td>401.30</td></tr><tr><td>Pseudo R-squared</td><td>.264</td><td>.220</td><td>.221</td></tr></tbody></table>

Example 15.2 (Married Women's Labor Force Participation): We now estimate logit and probit models for women's labor force participation. For comparison we report the linear probability estimates. The results, with standard errors in parentheses, are given in Table 15.1 (for the LPM, these are heteroskedasticity-robust).

The estimates from the three models tell a consistent story. The signs of the coefficients are the same across models, and the same variables are statistically significant in each model. The pseudo R-squared for the LPM is just the usual R-squared reported for OLS; for logit and probit the pseudo R-squared is the measure based on the log likelihoods described previously. In terms of overall percent correctly predicted, the models do equally well. For the probit model, it correctly predicts ''out of the labor force'' about 63.1 percent of the time, and it correctly predicts ''in the labor force'' about 81.3 percent of the time. The LPM has the same overall percent correctly predicted, but there are slight differences within each outcome.

As we emphasized earlier, the magnitudes of the coefficients are not directly comparable across the models. Using the rough rule of thumb discussed earlier, we can 

{478}------------------------------------------------

divide the logit estimates by four and the probit estimates by 2.5 to make all estimates comparable to the LPM estimates. For example, for the coefficients on kidslt6, the scaled logit estimate is about .361, and the scaled probit estimate is about .347. These are larger in magnitude than the LPM estimate (for reasons we will soon discuss). The scaled coefficient on educ is .055 for logit and .052 for probit.

If we evaluate the standard normal probability density function, <sup>f</sup><sup>ð</sup> ^b<sup>0</sup> <sup>þ</sup> ^b1x<sup>1</sup> þ <sup>þ</sup> ^bkxkÞ, at the average values of the independent variables in the sample (including the average of exper2), we obtain about .391; this value is close enough to .4 to make the rough rule of thumb for scaling the probit coefficients useful in obtaining the effects on the response probability. In other words, to estimate the change in the response probability given a one-unit increase in any independent variable, we multiply the corresponding probit coefficient by .4.

The biggest difference between the LPM model on one hand, and the logit and probit models on the other, is that the LPM assumes constant marginal effects for educ, kidslt6, and so on, while the logit and probit models imply diminishing marginal magnitudes of the partial effects. In the LPM, one more small child is estimated to reduce the probability of labor force participation by about .262, regardless of how many young children the woman already has (and regardless of the levels of the other dependent variables). We can contrast this finding with the estimated marginal effect from probit. For concreteness, take a woman with nwifeinc ¼ 20:13, educ ¼ 12:3, exper ¼ 10:6, age ¼ 42:5—which are roughly the sample averages—and kidsge6 ¼ 1. What is the estimated fall in the probability of working in going from zero to one small child? We evaluate the standard normal cdf, <sup>F</sup><sup>ð</sup> ^b<sup>0</sup> <sup>þ</sup> ^b1x<sup>1</sup> þþ ^bkxk<sup>Þ</sup> with kidslt6 ¼ 1 and kidslt6 ¼ 0, and the other independent variables set at the values given. We get roughly :373 :707 ¼ :334, which means that the labor force participation probability is about .334 lower when a woman has one young child. This is not much different from the scaled probit coefficient of .347. If the woman goes from one to two young children, the probability falls even more, but the marginal effect is not as large: :117 :373 ¼ :256. Interestingly, the estimate from the linear probability model, which we think can provide a good estimate near the average values of the covariates, is in fact between the probit estimated partial effects starting from zero and one children.

Binary response models apply with little modification to independently pooled cross sections or to other data sets where the observations are independent but not necessarily identically distributed. Often year or other time-period dummy variables are included to account for aggregate time effects. Just as with linear models, probit can be used to evaluate the impact of certain policies in the context of a natural experiment; see Problem 15.13. An application is given in Gruber and Poterba (1994).

{479}------------------------------------------------

# 15.7 Specification Issues in Binary Response Models

We now turn to several issues that can arise in applying binary response models to economic data. All of these topics are relevant for general index models, but features of the normal distribution allow us to obtain concrete results in the context of probit models. Therefore, our primary focus is on probit models.