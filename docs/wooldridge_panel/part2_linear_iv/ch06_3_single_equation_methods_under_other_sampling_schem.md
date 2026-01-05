# Single-Equation Methods under Other Sampling Schemes

> Pages: 142-146

So far our treatment of OLS and 2SLS has been explicitly for the case of random samples. In this section we briefly discuss some issues that arise for other sampling schemes that are sometimes assumed for cross section data.

#### 6.3.1 Pooled Cross Sections over Time

A data structure that is useful for a variety of purposes, including policy analysis, is what we will call **pooled cross sections over time**. The idea is that during each year a new random sample is taken from the relevant population. Since distributions of variables tend to change over time, the identical distribution assumption is not usually valid, but the independence assumption is. This approach gives rise to **independence** 

{143}------------------------------------------------

dent, not identically distributed (i.n.i.d.) observations. It is important not to confuse a pooling of independent cross sections with a different data structure, panel data, which we treat starting in Chapter 7. Briefly, in a panel data set we follow the same group of individuals, firms, cities, and so on over time. In a pooling of cross sections over time, there is no replicability over time. (Or, if units appear in more than one time period, their recurrence is treated as coincidental and ignored.)

Every method we have learned for pure cross section analysis can be applied to pooled cross sections, including corrections for heteroskedasticity, specification testing, instrumental variables, and so on. But in using pooled cross sections, we should usually include year (or other time period) dummies to account for aggregate changes over time. If year dummies appear in a model, and it is estimated by 2SLS, the year dummies are their own instruments, as the passage of time is exogenous. For an example, see Problem 6.8. Time dummies can also appear in tests for heteroskedasticity to determine whether the unconditional error variance has changed over time.

In some cases we interact some explanatory variables with the time dummies to allow partial effects to change over time. This procedure can be very useful for policy analysis. In fact, much of the recent literature in policy analyis using natural experiments can be cast as a pooled cross section analysis with appropriately chosen dummy variables and interactions.

In the simplest case, we have two time periods, say year 1 and year 2. There are also two groups, which we will call a control group and an experimental group or treatment group. In the natural experiment literature, people (or firms, or cities, and so on) find themselves in the treatment group essentially by accident. For example, to study the effects of an unexpected change in unemployment insurance on unemployment duration, we choose the treatment group to be unemployed individuals from a state that has a change in unemployment compensation. The control group could be unemployed workers from a neighboring state. The two time periods chosen would straddle the policy change.

As another example, the treatment group might consist of houses in a city undergoing unexpected property tax reform, and the control group would be houses in a nearby, similar town that is not subject to a property tax change. Again, the two (or more) years of data would include the period of the policy change. Treatment means that a house is in the city undergoing the regime change.

To formalize the discussion, call A the control group, and let B denote the treatment group; the dummy variable dB equals unity for those in the treatment group and is zero otherwise. Letting d2 denote a dummy variable for the second (post-policychange) time period, the simplest equation for analyzing the impact of the policy change is

{144}------------------------------------------------

$$y = \beta_0 + \delta_0 d2 + \beta_1 dB + \delta_1 d2 \cdot dB + u \tag{6.31}$$

where y is the outcome variable of interest. The period dummy d2 captures aggregate factors that affect y over time in the same way for both groups. The presence of dB by itself captures possible differences between the treatment and control groups before the policy change occurs. The coefficient of interest, d1, multiplies the interaction term, d2 dB (which is simply a dummy variable equal to unity for those observations in the treatment group in the second year).

The OLS estimator, ^d1, has a very interesting interpretation. Let yA; <sup>1</sup> denote the sample average of y for the control group in the first year, and let yA; <sup>2</sup> be the average of <sup>y</sup> for the control group in the second year. Define yB; <sup>1</sup> and yB; <sup>2</sup> similarly. Then ^d<sup>1</sup> can be expressed as

$$\hat{\delta}_1 = (\bar{y}_{B,2} - \bar{y}_{B,1}) - (\bar{y}_{A,2} - \bar{y}_{A,1}) \tag{6.32}$$

This estimator has been labeled the difference-in-differences (DID) estimator in the recent program evaluation literature, although it has a long history in analysis of variance.

To see how effective ^d<sup>1</sup> is for estimating policy effects, we can compare it with some alternative estimators. One possibility is to ignore the control group completely and use the change in the mean over time for the treatment group, yB; <sup>2</sup> yB; 1, to measure the policy effect. The problem with this estimator is that the mean response can change over time for reasons unrelated to the policy change. Another possibility is to ignore the first time period and compute the difference in means for the treatment and control groups in the second time period, yB; <sup>2</sup> yA; 2. The problem with this pure cross section approach is that there might be systematic, unmeasured differences in the treatment and control groups that have nothing to do with the treatment; attributing the difference in averages to a particular policy might be misleading.

By comparing the time changes in the means for the treatment and control groups, both group-specific and time-specific effects are allowed for. Nevertheless, unbiasedness of the DID estimator still requires that the policy change not be systematically related to other factors that affect y (and are hidden in u).

In most applications, additional covariates appear in equation (6.31); for example, characteristics of unemployed people or housing characteristics. These account for the possibility that the random samples within a group have systematically different characteristics in the two time periods. The OLS estimator of d<sup>1</sup> no longer has the simple representation in equation (6.32), but its interpretation is essentially unchanged.

{145}------------------------------------------------

Example 6.5 (Length of Time on Workers' Compensation): Meyer, Viscusi, and Durbin (1995) (hereafter, MVD) study the length of time (in weeks) that an injured worker receives workers' compensation. On July 15, 1980, Kentucky raised the cap on weekly earnings that were covered by workers' compensation. An increase in the cap has no effect on the benefit for low-income workers, but it makes it less costly for a high-income worker to stay on workers' comp. Therefore, the control group is low-income workers, and the treatment group is high-income workers; high-income workers are defined as those for whom the pre-policy-change cap on benefits is binding. Using random samples both before and after the policy change, MVD are able to test whether more generous workers' compensation causes people to stay out of work longer (everything else fixed). MVD start with a difference-in-differences analysis, using log(durat) as the dependent variable. The variable afchnge is the dummy variable for observations after the policy change, and highearn is the dummy variable for high earners. The estimated equation is

$$\log(\hat{d}urat) = 1.126 + .0077 \, afchnge + .256 \, highearn$$

$$(0.031) \quad (.0447) \qquad (.047)$$

$$+ .191 \, afchnge \cdot highearn$$

$$(.069)$$

$$N = 5,626, \qquad R^2 = .021$$

$$(6.33)$$

Therefore, ^d<sup>1</sup> ¼ :191 ðt ¼ 2:77Þ, which implies that the average duration on workers' compensation increased by about 19 percent due to the higher earnings cap. The coefficient on afchnge is small and statistically insignificant: as is expected, the increase in the earnings cap had no effect on duration for low-earnings workers. The coeffi cient on highearn shows that, even in the absence of any change in the earnings cap, high earners spent much more time—on the order of 100 ½expð:256Þ - 1 ¼ 29:2 percent—on workers' compensation.

MVD also add a variety of controls for gender, marital status, age, industry, and type of injury. These allow for the fact that the kind of people and type of injuries differ systematically in the two years. Perhaps not surprisingly, controlling for these factors has little effect on the estimate of d1; see the MVD article and Problem 6.9.

Sometimes the two groups consist of people or cities in different states in the United States, often close geographically. For example, to assess the impact of changing alcohol taxes on alcohol consumption, we can obtain random samples on individuals from two states for two years. In state A, the control group, there was no

{146}------------------------------------------------

change in alcohol taxes. In state B, taxes increased between the two years. The outcome variable would be a measure of alcohol consumption, and equation (6.31) can be estimated to determine the effect of the tax on alcohol consumption. Other factors, such as age, education, and gender can be controlled for, although this procedure is not necessary for consistency if sampling is random in both years and in both states.

The basic equation (6.31) can be easily modified to allow for continuous, or at least nonbinary, ''treatments.'' An example is given in Problem 6.7, where the ''treatment'' for a particular home is its distance from a garbage incinerator site. In other words, there is not really a control group: each unit is put somewhere on a continuum of possible treatments. The analysis is similar because the treatment dummy, dB, is simply replaced with the nonbinary treatment.

For a survey on the natural experiment methodology, as well as several additional examples, see Meyer (1995).