# Measurement Error in the Dependent Variable

> Pages: 87-89

We begin with the case where the dependent variable is the only variable measured with error. Let  $y^*$  denote the variable (in the population, as always) that we would like to explain. For example,  $y^*$  could be annual family saving. The regression model has the usual linear form

$$y^* = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + v \tag{4.37}$$

and we assume that it satisfies at least Assumptions OLS.1 and OLS.2. Typically, we are interested in  $E(y^* | x_1, ..., x_K)$ . We let y represent the observable measure of  $y^*$  where  $y \neq y^*$ .

The population measurement error is defined as the difference between the observed value and the actual value:

$$e_0 = y - y^* (4.38)$$

For a random draw *i* from the population, we can write  $e_{i0} = y_i - y_i^*$ , but what is important is how the measurement error in the population is related to other factors. To obtain an estimable model, we write  $y^* = y - e_0$ , plug this into equation (4.37), and rearrange:

$$y = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + v + e_0 \tag{4.39}$$

Since  $y, x_1, x_2, ..., x_K$  are observed, we can estimate this model by OLS. In effect, we just ignore the fact that y is an imperfect measure of  $y^*$  and proceed as usual.

When does OLS with y in place of  $y^*$  produce consistent estimators of the  $\beta_j$ ? Since the original model (4.37) satisfies Assumption OLS.1, v has zero mean and is uncorrelated with each  $x_j$ . It is only natural to assume that the measurement error has zero mean; if it does not, this fact only affects estimation of the intercept,  $\beta_0$ . Much more important is what we assume about the relationship between the measurement error  $e_0$  and the explanatory variables  $x_j$ . The usual assumption is that the measurement error in y is statistically independent of each explanatory variable, which implies that  $e_0$  is uncorrelated with  $\mathbf{x}$ . Then, the OLS estimators from equation (4.39) are consistent (and possibly unbiased as well). Further, the usual OLS inference procedures (t statistics, t statistics, t statistics) are asymptotically valid under appropriate homoskedasticity assumptions.

{88}------------------------------------------------

If  $e_0$  and v are uncorrelated, as is usually assumed, then  $Var(v+e_0) = \sigma_v^2 + \sigma_0^2 > \sigma_v^2$ . Therefore, measurement error in the dependent variable results in a larger error variance than when the dependent variable is not measured with error. This result is hardly surprising and translates into larger asymptotic variances for the OLS estimators than if we could observe  $y^*$ . But the larger error variance violates none of the assumptions needed for OLS estimation to have its desirable large-sample properties.

Example 4.6 (Saving Function with Measurement Error): Consider a saving function

$$E(sav^* | inc, size, educ, age) = \beta_0 + \beta_1 inc + \beta_2 size + \beta_3 educ + \beta_4 age$$

but where actual saving ( $sav^*$ ) may deviate from reported saving (sav). The question is whether the size of the measurement error in sav is systematically related to the other variables. It may be reasonable to assume that the measurement error is not correlated with inc, size, educ, and age, but we might expect that families with higher incomes, or more education, report their saving more accurately. Unfortunately, without more information, we cannot know whether the measurement error is correlated with inc or educ.

When the dependent variable is in logarithmic form, so that  $log(y^*)$  is the dependent variable, a natural measurement error equation is

$$\log(y) = \log(y^*) + e_0 \tag{4.40}$$

This follows from a **multiplicative measurement error** for y:  $y = y^*a_0$  where  $a_0 > 0$  and  $e_0 = \log(a_0)$ .

Example 4.7 (Measurement Error in Firm Scrap Rates): In Example 4.4, we might think that the firm scrap rate is mismeasured, leading us to postulate the model  $\log(scrap^*) = \beta_0 + \beta_1 grant + v$ , where  $scrap^*$  is the true scrap rate. The measurement error equation is  $\log(scrap) = \log(scrap^*) + e_0$ . Is the measurement error  $e_0$  independent of whether the firm receives a grant? Not if a firm receiving a grant is more likely to underreport its scrap rate in order to make it look as if the grant had the intended effect. If underreporting occurs, then, in the estimable equation  $\log(scrap) = \beta_0 + \beta_1 grant + v + e_0$ , the error  $u = v + e_0$  is negatively correlated with grant. This result would produce a downward bias in  $\beta_1$ , tending to make the training program look more effective than it actually was.

These examples show that measurement error in the dependent variable *can* cause biases in OLS if the measurement error is systematically related to one or more of the explanatory variables. If the measurement error is uncorrelated with the explanatory variables, OLS is perfectly appropriate.

{89}------------------------------------------------