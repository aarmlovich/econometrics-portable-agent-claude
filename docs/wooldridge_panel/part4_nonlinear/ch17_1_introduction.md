# Introduction

> Pages: 559-560

Up to this point, with the exception of occasionally touching on cluster samples and independently pooled cross sections, we have assumed the availability of a random sample from the underlying population. This assumption is not always realistic: because of the way some economic data sets are collected, and often because of the behavior of the units being sampled, random samples are not always available.

A selected sample is a general term that describes a nonrandom sample. There are a variety of selection mechanisms that result in nonrandom samples. Some of these are due to sample design, while others are due to the behavior of the units being sampled, including nonresponse on survey questions and attrition from social programs. Before we launch into specifics, there is an important general point to remember: sample selection can only be an issue once the population of interest has been carefully specified. If we are interested in a subset of a larger population, then the proper approach is to specify a model for that part of the population, obtain a random sample from that part of the population, and proceed with standard econometric methods.

The following are some examples with nonrandomly selected samples.

Example 17.1 (Saving Function): Suppose we wish to estimate a saving function for all families in a given country, and the population saving function is

$$saving = \beta_0 + \beta_1 income + \beta_2 age + \beta_3 married + \beta_4 kids + u$$
 (17.1)

where age is the age of the household head and the other variables are self-explanatory. However, we only have access to a survey that included families whose household head was 45 years of age or older. This limitation raises a sample selection issue because we are interested in the saving function for all families, but we can obtain a random sample only for a subset of the population.

Example 17.2 (Truncation Based on Wealth): We are interested in estimating the effect of worker eligibility in a particular pension plan [for example, a 401(k) plan] on family wealth. Let the population model be

$$wealth = \beta_0 + \beta_1 plan + \beta_2 educ + \beta_3 age + \beta_4 income + u$$
 (17.2)

where plan is a binary indicator for eligibility in the pension plan. However, we can only sample people with a net wealth less than \$200,000, so the sample is selected on the basis of wealth. As we will see, sampling based on a response variable is much more serious than sampling based on an exogenous explanatory variable.

{560}------------------------------------------------

In these two examples data were missing on all variables for a subset of the population as a result of survey design. In other cases, units are randomly drawn from the population, but data are missing on one or more variables for some units in the sample. Using a subset of a random sample because of missing data can lead to a sample selection problem. As we will see, if the reason the observations are missing is appropriately exogenous, using the subsample has no serious consequences.

Our final example illustrates a more subtle form of a missing data problem.

Example 17.3 (Wage Offer Function): Consider estimating a wage offer equation for people of working age. By definition, this equation is supposed to represent all people of working age, whether or not a person is actually working at the time of the survey. Because we can only observe the wage offer for working people, we effectively select our sample on this basis.

This example is not as straightforward as the previous two. We treat it as a sample selection problem because data on a key variable—the wage offer, wageo—are available only for a clearly defined subset of the population. This is sometimes called incidental truncation because wage<sup>o</sup> is missing as a result of the outcome of another variable, labor force participation.

The incidental truncation in this example has a strong self-selection component: people self-select into employment, so whether or not we observe wage<sup>o</sup> depends on an individual's labor supply decision. Whether we call examples like this sample selection or self-selection is largely irrelevant. The important point is that we must account for the nonrandom nature of the sample we have for estimating the wage offer equation.

In the next several sections we cover a variety of sample selection issues, including tests and corrections. Section 17.7 treats sample selection and the related problem of attrition in panel data. Stratified sampling, which arises out of sampling design, is covered in Section 17.8.

# 17.2 When Can Sample Selection Be Ignored?

In some cases, the fact that we have a nonrandom sample does not affect the way we estimate population parameters; it is important to understand when this is the case.