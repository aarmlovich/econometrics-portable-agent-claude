# A Counterfactual Setting and the Self-Selection Problem

> Pages: 610-614

The modern literature on treatment effects begins with a counterfactual, where each individual (or other agent) has an outcome with and without treatment (where


{611}------------------------------------------------

''treatment'' is interpreted very broadly). This section draws heavily on Heckman (1992, 1997), Imbens and Angrist (1994), and Angrist, Imbens, and Rubin (1996) (hereafter AIR). Let y<sup>1</sup> denote the outcome with treatment and y<sup>0</sup> the outcome without treatment. Because an individual cannot be in both states, we cannot observe both y<sup>0</sup> and y1; in effect, the problem we face is one of missing data.

It is important to see that we have made no assumptions about the distributions of y<sup>0</sup> and y1. In many cases these may be roughly continuously distributed (such as salary), but often y<sup>0</sup> and y<sup>1</sup> are binary outcomes (such as a welfare participation indicator), or even corner solution outcomes (such as married women's labor supply). However, some of the assumptions we make will be less plausible for discontinuous random variables, something we discuss after introducing the assumptions.

The following discussion assumes that we have an independent, identically distributed sample from the population. This assumption rules out cases where the treatment of one unit affects another's outcome (possibly through general equilibrium effects, as in Heckman, Lochner, and Taber, 1998). The assumption that treatment of unit i affects only the outcome of unit i is called the stable unit treatment value assumption (SUTVA) in the treatment literature (see, for example, AIR). We are making a stronger assumption because random sampling implies SUTVA.

Let the variable w be a binary treatment indicator, where w ¼ 1 denotes treatment and w ¼ 0 otherwise. The triple ðy0; y1; wÞ represents a random vector from the underlying population of interest. For a random draw i from the population, we write ðyi0; yi1; wiÞ. However, as we have throughout, we state assumptions in terms of the population.

To measure the effect of treatment, we are interested in the difference in the outcomes with and without treatment, y<sup>1</sup> y0. Because this is a random variable (that is, it is individual specific), we must be clear about what feature of its distribution we want to estimate. Several possibilities have been suggested in the literature. In Rosenbaum and Rubin (1983), the quantity of interest is the average treatment effect (ATE),

$$ATE \equiv E(y_1 - y_0) \tag{18.1}$$

ATE is the expected effect of treatment on a randomly drawn person from the population. Some have criticized this measure as not being especially relevant for policy purposes: because it averages across the entire population, it includes in the average units who would never be eligible for treatment. Heckman (1997) gives the example of a job training program, where we would not want to include millionaires in computing the average effect of a job training program. This criticism is somewhat misleading, as we can—and would—exclude people from the population who would never be eligible. For example, in evaluating a job training program, we might re

{612}------------------------------------------------

strict attention to people whose pretraining income is below a certain threshold; wealthy people would be excluded precisely because we have no interest in how job training affects the wealthy. In evaluating the benefits of a program such as Head Start, we could restrict the population to those who are actually eligible for the program or are likely to be eligible in the future. In evaluating the effectiveness of enterprise zones, we could restrict our analysis to block groups whose unemployment rates are above a certain threshold or whose per capita incomes are below a certain level.

A second quantity of interest, and one that has received much recent attention, is the average treatment effect on the treated, which we denote ATE1:

$$ATE_1 \equiv E(y_1 - y_0 \mid w = 1)$$
(18.2)

That is, ATE<sup>1</sup> is the mean effect for those who actually participated in the program. As we will see, in some special cases equations (18.1) and (18.2) are equivalent, but generally they differ.

Imbens and Angrist (1994) define another treatment effect, which they call a local average treatment effect (LATE). LATE has the advantage of being estimable using instrumental variables under very weak conditions. It has two potential drawbacks: (1) it measures the effect of treatment on a generally unidentifiable subpopulation; and (2) the definition of LATE depends on the particular instrumental variable that we have available. We will discuss LATE in the simplest setting in Section 18.4.2.

We can expand the definition of both treatment effects by conditioning on covariates. If x is an observed covariate, the ATE conditional on x is simply Eðy<sup>1</sup> y<sup>0</sup> j xÞ; similarly, equation (18.2) becomes Eðy<sup>1</sup> y<sup>0</sup> j x; w ¼ 1Þ. By choosing x appropriately, we can define ATEs for various subsets of the population. For example, x can be pretraining income or a binary variable indicating poverty status, race, or gender. For the most part, we will focus on ATE and ATE<sup>1</sup> without conditioning on covariates.

As noted previously, the difficulty in estimating equation (18.1) or (18.2) is that we observe only y<sup>0</sup> or y1, not both, for each person. More precisely, along with w, the observed outcome is

$$y = (1 - w)y_0 + wy_1 = y_0 + w(y_1 - y_0)$$
(18.3)

Therefore, the question is, How can we estimate equation (18.1) or (18.2) with a random sample on y and w (and usually some observed covariates)?

First, suppose that the treatment indicator w is statistically independent of ðy0; y1Þ, as would occur when treatment is randomized across agents. One implication of independence between treatment status and the potential outcomes is that ATE and ATE<sup>1</sup> are identical: Eðy<sup>1</sup> y<sup>0</sup> j w ¼ 1Þ ¼ Eðy<sup>1</sup> y0Þ. Furthermore, estimation of

{613}------------------------------------------------

ATE is simple. Using equation (18.3), we have

$$E(y | w = 1) = E(y_1 | w = 1) = E(y_1)$$

where the last equality follows because y<sup>1</sup> and w are independent. Similarly,

$$E(y | w = 0) = E(y_0 | w = 0) = E(y_0)$$

It follows that

$$ATE = ATE_1 = E(y \mid w = 1) - E(y \mid w = 0)$$
(18.4)

The right-hand side is easily estimated by a difference in sample means: the sample average of y for the treated units minus the sample average of y for the untreated units. Thus, randomized treatment guarantees that the difference-in-means estimator from basic statistics is unbiased, consistent, and asymptotically normal. In fact, these properties are preserved under the weaker assumption of mean independence: Eðy<sup>0</sup> j wÞ ¼ Eðy0Þ and Eðy<sup>1</sup> j wÞ ¼ Eðy1Þ.

Randomization of treatment is often infeasible in program evaluation (although randomization of eligibility often is feasible; more on this topic later). In most cases, individuals at least partly determine whether they receive treatment, and their decisions may be related to the benefits of treatment, y<sup>1</sup> y0. In other words, there is self-selection into treatment.

It turns out that ATE<sup>1</sup> can be consistently estimated as a difference in means under the weaker assumption that w is independent of y0, without placing any restriction on the relationship between w and y1. To see this point, note that we can always write

$$E(y | w = 1) - E(y | w = 0) = E(y_0 | w = 1) - E(y_0 | w = 0) + E(y_1 - y_0 | w = 1)$$
$$= [E(y_0 | w = 1) - E(y_0 | w = 0)] + ATE_1$$
(18.5)

If y<sup>0</sup> is mean independent of w, that is,

$$E(y_0 | w) = E(y_0) \tag{18.6}$$

then the first term in equation (18.5) disappears, and so the difference in means estimator is an unbiased estimator of ATE1. Unfortunately, condition (18.6) is a strong assumption. For example, suppose that people are randomly made eligible for a voluntary job training program. Condition (18.6) effectively implies that the participation decision is unrelated to what people would earn in the absence of the program.

A useful expression relating ATE<sup>1</sup> and ATE is obtained by writing y<sup>0</sup> ¼ m<sup>0</sup> þ v<sup>0</sup> and y<sup>1</sup> ¼ m<sup>1</sup> þ v1, where m<sup>g</sup> ¼ EðygÞ, g ¼ 0; 1. Then

$$y_1 - y_0 = (\mu_1 - \mu_0) + (v_1 - v_0) = ATE + (v_1 - v_0)$$

{614}------------------------------------------------

Taking the expectation of this equation conditional on w ¼ 1 gives

$$ATE_1 = ATE + E(v_1 - v_0 | w = 1)$$

We can think of v<sup>1</sup> v<sup>0</sup> as the person-specific gain from participation, and so ATE<sup>1</sup> differs from ATE by the expected person-specific gain for those who participated. If y<sup>1</sup> y<sup>0</sup> is not mean independent of w, ATE<sup>1</sup> and ATE generally differ.

Fortunately, we can estimate ATE and ATE<sup>1</sup> under assumptions less restrictive than independence of ðy0; y1Þ and w. In most cases, we can collect data on individual characteristics and relevant pretreatment outcomes—sometimes a substantial amount of data. If, in an appropriate sense, treatment depends on the observables and not on the unobservables determining ðy0; y1Þ, then we can estimate average treatment effects quite generally, as we show in the next section.