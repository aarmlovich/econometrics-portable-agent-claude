# Ordered Logit and Ordered Probit

> Pages: 513-517

Another kind of multinomial response is an **ordered response**. As the name suggests, if y is an ordered response, then the values we assign to each outcome are no longer arbitrary. For example, y might be a credit rating on a scale from zero to six, with y = 6 representing the highest rating and y = 0 the lowest rating. The fact that six is a better rating than five conveys useful information, even though the credit rating itself only has ordinal meaning. For example, we cannot say that the difference between four and two is somehow twice as important as the difference between one and zero.

Let y be an ordered response taking on the values  $\{0, 1, 2, \ldots, J\}$  for some known integer J. The **ordered probit model** for y (conditional on explanatory variables  $\mathbf{x}$ ) can be derived from a latent variable model. Assume that a latent variable  $y^*$  is determined by

{514}------------------------------------------------

$$y^* = \mathbf{x}\boldsymbol{\beta} + e, \qquad e \mid \mathbf{x} \sim \text{Normal}(0, 1) \tag{15.87}$$

where  $\beta$  is  $K \times 1$  and, for reasons to be seen,  $\mathbf{x}$  does not contain a constant. Let  $\alpha_1 < \alpha_2 < \cdots < \alpha_J$  be unknown **cut points** (or **threshold parameters**), and define

$$y = 0 if y^* \le \alpha_1$$

$$y = 1 if \alpha_1 < y^* \le \alpha_2$$

$$\vdots$$

$$y = J if y^* > \alpha_J$$

$$(15.88)$$

For example, if y takes on the values 0, 1, and 2, then there are two cut points,  $\alpha_1$  and  $\alpha_2$ .

Given the standard normal assumption for e, it is straightforward to derive the conditional distribution of y given  $\mathbf{x}$ ; we simply compute each response probability:

$$P(y = 0 \mid \mathbf{x}) = P(y^* \le \alpha_1 \mid \mathbf{x}) = P(\mathbf{x}\boldsymbol{\beta} + e \le \alpha_1 \mid \mathbf{x}) = \Phi(\alpha_1 - \mathbf{x}\boldsymbol{\beta})$$

$$P(y = 1 \mid \mathbf{x}) = P(\alpha_1 < y^* \le \alpha_2 \mid \mathbf{x}) = \Phi(\alpha_2 - \mathbf{x}\boldsymbol{\beta}) - \Phi(\alpha_1 - \mathbf{x}\boldsymbol{\beta})$$

$$\vdots$$

$$P(y = J - 1 \mid \mathbf{x}) = P(\alpha_{J-1} < y^* \le \alpha_J \mid \mathbf{x}) = \Phi(\alpha_J - \mathbf{x}\boldsymbol{\beta}) - \Phi(\alpha_{J-1} - \mathbf{x}\boldsymbol{\beta})$$

$$P(y = J \mid \mathbf{x}) = P(y^* > \alpha_J \mid \mathbf{x}) = 1 - \Phi(\alpha_J - \mathbf{x}\boldsymbol{\beta})$$

You can easily verify that these sum to unity. When J=1 we get the binary probit model:  $P(y=1 | \mathbf{x}) = 1 - P(y=0 | \mathbf{x}) = 1 - \Phi(\alpha_1 - \mathbf{x}\boldsymbol{\beta}) = \Phi(\mathbf{x}\boldsymbol{\beta} - \alpha_1)$ , and so  $-\alpha_1$  is the intercept inside  $\Phi$ . It is for this reason that  $\mathbf{x}$  does not contain an intercept in this formulation of the ordered probit model. (When there are only two outcomes, zero and one, we set the single cut point to zero and estimate the intercept; this approach leads to the standard probit model.)

The parameters a and  $\beta$  can be estimated by maximum likelihood. For each i, the log-likelihood function is

$$\ell_i(\boldsymbol{a}, \boldsymbol{\beta}) = 1[y_i = 0] \log[\Phi(\alpha_1 - \mathbf{x}_i \boldsymbol{\beta})] + 1[y_i = 1] \log[\Phi(\alpha_2 - \mathbf{x}_i \boldsymbol{\beta})]$$

$$- \Phi(\alpha_1 - \mathbf{x}_i \boldsymbol{\beta})] + \dots + 1[y_i = J] \log[1 - \Phi(\alpha_J - \mathbf{x}_i \boldsymbol{\beta})]$$

$$(15.89)$$

This log-likelihood function is well behaved, and many statistical packages routinely estimate ordered probit models.

Other distribution functions can be used in place of  $\Phi$ . Replacing  $\Phi$  with the logit function,  $\Lambda$ , gives the **ordered logit model**. In either case we must remember that  $\beta$ , by

{515}------------------------------------------------

itself, is of limited interest. In most cases we are not interested in Eðy j xÞ ¼ x*b*, as y is an abstract construct. Instead, we are interested in the response probabilities Pðy ¼ j j xÞ, just as in the ordered response case. For the ordered probit model

$$\partial p_0(\mathbf{x})/\partial x_k = -\beta_k \phi(\alpha_1 - \mathbf{x}\boldsymbol{\beta}), \ \partial p_J(\mathbf{x})/\partial x_k = \beta_k \phi(\alpha_J - \mathbf{x}\boldsymbol{\beta})$$

qpjðxÞ=qxk ¼ bk½fða<sup>j</sup><sup>1</sup> x*b*Þ fða<sup>j</sup> x*b*Þ-

and the formulas for the ordered logit model are similar. In making comparisons across different models—in particular, comparing ordered probit and ordered logit we must remember to compare estimated response probabilities at various values of x, such as x; the ^*b* are not directly comparable. In particular, the a^<sup>j</sup> are important determinants of the magnitudes of the estimated probabilities and partial effects. (Therefore, treatments of ordered probit that refer to the a<sup>j</sup> as ancillary, or secondary, parameters are misleading.)

; 0 < j < J

While the direction of the effect of xk on the probabilities Pðy ¼ 0 j xÞ and Pðy ¼ J j xÞ is unambiguously determined by the sign of bk, the sign of b<sup>k</sup> does not always determine the direction of the effect for the intermediate outcomes, 1; 2; ... ; J 1. To see this point, suppose there are three possible outcomes, 0, 1, and 2, and that b<sup>k</sup> > 0. Then qp0ðxÞ=qxk < 0 and qp2ðxÞ=qxk > 0, but qp1ðxÞ=qxk could be either sign. If ja<sup>1</sup> x*b*j < ja<sup>2</sup> x*b*j, the scale factor, fða<sup>1</sup> x*b*Þ fða<sup>2</sup> x*b*Þ, is positive; otherwise it is negative. (This conclusion follows because the standard normal pdf is symmetric about zero, reaches its maximum at zero, and declines monotonically as its argument increases in absolute value.)

As with multinomial logit, for ordered responses we can compute the percent correctly predicted, for each outcome as well as overall: our prediction for y is simply the outcome with the highest probability.

Ordered probit and logit can also be applied when y is given quantitative meaning but we wish to acknowledge the discrete, ordered nature of the response. For example, suppose that individuals are asked to give one of three responses on how their pension funds are invested: ''mostly bonds,'' ''mixed,'' and ''mostly stocks.'' One possibility is to assign these outcomes as 0, 1, 2 and apply ordered probit or ordered logit to estimate the effects of various factors on the probability of each outcome. Instead, we could assign the percent invested in stocks as, say 0, 50, and 100, or 25, 50, and 75. For estimating the probabilities of each category it is irrelevant how we assign the percentages as long as the order is preserved. However, if we give quantitative meaning to y, the expected value of y has meaning. We have

$$E(y | \mathbf{x}) = a_0 P(y = a_0 | \mathbf{x}) + a_1 P(y = a_1 | \mathbf{x}) + \dots + a_J P(y = a_J | \mathbf{x})$$

{516}------------------------------------------------

where a<sup>0</sup> < a<sup>1</sup> < < aJ are the J values taken on by y. Once we have estimated the response probabilities by ordered probit or ordered logit, we can easily estimate Eðy j xÞ for any value of x, for example, x. Estimates of the expected values can be compared at different values of the explanatory variables to obtain partial effects for discrete xj.

Example 15.5 (Asset Allocation in Pension Plans): The data in PENSION.RAW are a subset of data used by Papke (1998) in assessing the impact of allowing individuals to choose their own allocations on asset allocation in pension plans. Initially, Papke codes the responses ''mostly bonds,'' ''mixed,'' and ''mostly stocks'' as 0, 50, and 100, and uses a linear regression model estimated by OLS. The binary explanatory variable choice is unity if the person has choice in how his or her pension fund is invested. Controlling for age, education, gender, race, marital status, income (via a set of dummy variables), wealth, and whether the plan is profit sharing, gives the OLS estimate ^bchoice <sup>¼</sup> <sup>12</sup>:05 (se <sup>¼</sup> 6.30), where <sup>N</sup> <sup>¼</sup> 194. This result means that, other things equal, a person having choice has about 12 percentage points more assets in stocks.

The ordered probit coefficient on choice is .371 (se ¼ .184). The magnitude of the ordered probit coefficient does not have a simple interpretation, but its sign and statistical significance agree with the linear regression results. (The estimated cut points are a^<sup>1</sup> ¼ 3:087 and a^<sup>2</sup> ¼ 2:054.) To get an idea of the magnitude of the estimated effect of choice on the expected percent in stocks, we can estimate Eðy j xÞ with choice ¼ 1 and choice ¼ 0, and obtain the difference. However, we need to choose values for the other regressors. For illustration, suppose the person is 60 years old, has 13.5 years of education (roughly the averages in the sample), is a single, nonblack male, has annual income between \$50,000 and \$75,000, and had wealth in 1989 of \$200,000 (also close to the sample average). Then, for choice ¼ 1, E^ðpctstck j xÞA 50:4, and with choice ¼ 0, E^ðpctstck j xÞA37:6. The difference, 12.8, is remarkably close to the linear model estimate of the effect on choice.

For ordered probit, the percentages correctly predicted for each category are 51.6 (mostly bonds), 43.1 (mixed), and 37.9 (mostly stocks). The overall percentage correctly predicted is about 44.3.

The specification issues discussed in Section 15.7 for binary probit have analogues for ordered probit. The presence of normally distributed unobserved heterogeneity that is independent of x does not cause any problems when average partial effects are the focus. We can test for continuous endogenous variables in a manner very similar to the Rivers and Vuong (1988) procedure for binary probit, and maximum likeli-

{517}------------------------------------------------

hood estimation is possible if we make a distributional assumption for the endogenous explanatory variable.

Heteroskedasticity in the latent error e in equation (15.87) changes the form of the response probabilities and, therefore,  $E(y|\mathbf{x})$  when y has quantitative meaning. If the heteroskedasticity is modeled, for example, as  $\exp(\mathbf{x}_1\delta_1)$  where  $\mathbf{x}_1$  is a subset of  $\mathbf{x}$ , then maximum likelihood can be used to estimate  $\boldsymbol{\beta}$ ,  $\boldsymbol{\alpha}$  and  $\delta_1$ . However, as with the probit case, we must compute the partial effects on the response probabilities in comparing different models. It does not make sense to compare estimates of  $\boldsymbol{\beta}$  with and without heteroskedasticity. Score tests for heteroskedasticity are also easily derived along the lines of Section 15.5.3. Similar comments hold for deviations from normality in the latent variable model.

Unobserved effects ordered probit models can be handled by adapting Chamberlain's approach for binary probit in Section 15.8.2. The latent variable model can be written as

$$y_{it}^* = \mathbf{x}_{it}\boldsymbol{\beta} + c_i + e_{it}, e_{it} \mid \mathbf{x}_i \sim \text{Normal}(0, 1), \qquad t = 1, \dots, T$$

and  $y_{it} = 0$  if  $y_{it}^* \le \alpha_1$ ,  $y_{it} = 1$  if  $\alpha_1 < y_{it}^* \le \alpha_2$ , and so on. Certain embellishments are possible, such as letting the  $\alpha_j$  change over time. Assumption (15.67) allows estimation of the average partial effects by using a pooled ordered probit of  $y_{it}$  on 1,  $\mathbf{x}_{it}$ ,  $\overline{\mathbf{x}}_{i}$ . A full conditional MLE analysis is possible when we add assumption (15.61). The details are very similar to the probit case and are omitted.