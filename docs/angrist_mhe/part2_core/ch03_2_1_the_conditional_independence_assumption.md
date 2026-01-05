# The Conditional Independence Assumption

> Pages: 53-59

A regression is causal when the CEF it approximates is causal. This doesnít answer the question, of course. It just passes the buck up one level, since, as weíve seen, a regression inherits itís legitimacy from a CEF. Causality means di§erent things to di§erent people, but researchers working in many disciplines have found it useful to think of causal relationships in terms of the potential outcomes notation used in Chapter [2](#page-24-0) to 

{54}------------------------------------------------

describe what would happen to a given individual in a hypothetical comparison of alternative hospitalization scenarios. Di§erences in these potential outcomes were said to be the causal e§ect of hospitalization. The CEF is causal when it describes di§erences in average potential outcomes for a Öxed reference population.

Itís easiest to expand on the somewhat murky notion of a causal CEF in the context of a particular question, so letís stick with the schooling example. The causal connection between schooling and earnings can be deÖned as the functional relationship that describes what a given individual would earn if he or she obtained di§erent levels of education. In particular, we might think of schooling decisions as being made in a series of episodes where the decision-maker might realistically go one way or another, even if certain choices are more likely than others. For example, in the middle of junior year, restless and unhappy, Angrist glumly considered his options: dropping out of high school and hopefully getting a job, staying in school but taking easy classes that lead to a quick and dirty high school diploma, or plowing on in an academic track that leads to college. Although the consequences of such choices are usually unknown in advance, the idea of alternative paths leading to alternative outcomes for a given individual seems uncontroversial. Philosophers have argued over whether this personal notion of potential outcomes is precise enough to be scientiÖcally useful, but individual decision-makers seem to have no trouble thinking about their lives and choices in this manner (as in Robert Frostís celebrated The Road Not Taken: the traveller-narrator sees himself looking back on a moment of choice. He believes that the decision to follow the road less traveled "has made all the di§erence," though he also recognizes that counterfactual outcomes are unknowable).

In empirical work, the causal relationship between schooling and earnings tells us what people would earnó on averageó if we could either change their schooling in a perfectly-controlled environment, or change their schooling randomly so that those with di§erent levels of schooling would be otherwise comparable. As we discussed in Chapter [2,](#page-24-0) experiments ensure that the causal variable of interest is independent of potential outcomes so that the groups being compared are truly comparable. Here, we would like to generalize this notion to causal variables that take on more than two values, and to more complicated situations where we must hold a variety of "control variables" Öxed for causal inferences to be valid. This leads to the conditional independence assumption (CIA), a core assumption that provides the (sometimes implicit) justiÖcation for the causal interpretation of regression. This assumption is sometimes called selection-on-observables because the covariates to be held Öxed are assumed to be known and observed (e.g., in Goldberger, 1972; Barnow, Cain, and Goldberger, 1981). The big question, therefore, is what these control variables are, or should be. Weíll say more about that shortly. For now, we just do the econometric thing and call the covariates "Xi". As far as the schooling problem goes, it seems natural to imagine that X<sup>i</sup> is a vector that includes measures of ability and family background.

For starters, think of schooling as a binary decision, like whether Angrist goes to college. Denote this by a dummy variable, c<sup>i</sup> . The causal relationship between college attendance and a future outcome like earnings can be described using the same potential-outcomes notation we used to describe experiments in

{55}------------------------------------------------

Chapter 2. To address this question, we imagine two potential earnings variables:

$$potential \ outcome = \left\{ egin{array}{ll} \mathbf{Y}_{1i} & \mathrm{if} \ \mathbf{C}_i = 1 \\ \mathbf{Y}_{0i} & \mathrm{if} \ \mathbf{C}_i = 0 \end{array} 
ight. .$$

In this case,  $Y_{0i}$  is i's earnings without college, while  $Y_{1i}$  is i's earnings if he goes. We would like to know the difference between  $Y_{1i}$  and  $Y_{0i}$ , which is the causal effect of college attendance on individual i. This is what we would measure if we could go back in time and nudge i onto the road not taken. The observed outcome,  $Y_i$ , can be written in terms of potential outcomes as

<span id="page-55-0"></span>
$$Y_i = Y_{0i} + (Y_{1i} - Y_{0i})C_i$$
.

We get to see one of  $Y_{1i}$  or  $Y_{0i}$ , but never both. We therefore hope to measure the average of  $Y_{1i}-Y_{0i}$ , or the average for some group, such as those who went to college. This is  $E[Y_{1i}-Y_{0i}|C_i=1]$ .

In general, comparisons of those who do and don't go to college are likely to be a poor measure of the causal effect of college attendance. Following the logic in Chapter 2, we have

$$\underbrace{E\left[\mathbf{Y}_{i}|\mathbf{C}_{i}=1\right] - E\left[\mathbf{Y}_{i}|\mathbf{C}_{i}=0\right]}_{\text{Observed difference in earnings}} = \underbrace{E\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{C}_{i}=1\right]}_{\text{average treatment effect on the treated}} + \underbrace{E\left[\mathbf{Y}_{0i}|\mathbf{C}_{i}=1\right] - E\left[\mathbf{Y}_{0i}|\mathbf{C}_{i}=0\right]}_{\text{selection bias}}.$$
(3.2.1)

It seems likely that those who go to college would have earned more anyway. If so, selection bias is positive, and the naive comparison,  $E[Y_i|C_i=1] - E[Y_i|C_i=0]$ , exaggerates the benefits of college attendance.

The CIA asserts that conditional on observed characteristics,  $X_i$ , selection bias disappears. In this example, the CIA says,

$$\{\mathbf{Y}_{0i}, \mathbf{Y}_{1i}\} \coprod \mathbf{C}_{i} | \mathbf{X}_{i}. \tag{3.2.2}$$

Given the CIA, conditional-on- $X_i$  comparisons of average earnings across schooling levels have a causal interpretation. In other words,

$$E[Y_i|X_i, C_i = 1] - E[Y_i|X_i, C_i = 0] = E[Y_{1i} - Y_{0i}|X_i].$$

Now, we'd like to expand the conditional independence assumption to causal relations that involve variables that can take on more than two values, like years of schooling,  $s_i$ . The causal relationship between schooling and earnings is likely to be different for each person. We therefore use the individual-specific notation,

$$Y_{si} \equiv f_i(s)$$

{56}------------------------------------------------

to denote the potential earnings that person i would receive after obtaining s years of education. If s takes on only two values, 12 and 16, then we are back to the college/no college example:

$$Y_{0i} = f_i(12); Y_{1i} = f_i(16).$$

More generally, the function fi(s) tells us what i would earn for any value of schooling, s. In other words, fi(s) answers causal ìwhat ifî questions. In the context of theoretical models of the relationship between human capital and earnings, the form of fi(s) may be determined by aspects of individual behavior and/or market forces.

The CIA in this more general setup becomes

<span id="page-56-0"></span>
$$Y_{si} \coprod S_i | X_i$$
 (CIA)

In many randomized experiments, the CIA crops up because s<sup>i</sup> is randomly assigned conditional on X<sup>i</sup> (In the Tennessee STAR experiment, for example, small classes were randomly assigned within schools). In an observational study, the CIA means that s<sup>i</sup> can be said to be "as good as randomly assigned," conditional on X<sup>i</sup> .

Conditional on X<sup>i</sup> , the average causal e§ect of a one year increase in schooling is E[fi(s) fi(s 1)jX<sup>i</sup> ], while the average causal e§ect of a 4-year increase in schooling is E[fi(s) E [fi(s 4)] jX<sup>i</sup> ]. The data reveal only y<sup>i</sup> = fi(si), however, that is fi(s) for s =s<sup>i</sup> . But given the CIA, conditional-on-X<sup>i</sup> comparisons of average earnings across schooling levels have a causal interpretation. In other words,

$$E[Y_i|X_i, S_i = s] - E[Y_i|X_i, S_i = s - 1]$$

$$= E[f_i(s) - f_i(s - 1)|X_i]$$

for any value of s. For example, we can compare the earnings of those with 12 and 11 years of schooling to learn about the average causal e§ect of high school graduation:

$$E[Y_i|X_i, S_i = 12] - E[Y_i|X_i, S_i = 11] = E[f_i(12)|X_i, S_i = 12] - E[f_i(11)|X_i, S_i = 11].$$

This comparison has a causal interpretation because, given the CIA,

$$E[f_i(12)|X_i, S_i = 12] - E[f_i(11)|X_i, S_i = 11] = E[f_i(12) - f_i(11)|X_i, S_i = 12].$$

Here, the selection bias term is the average di§erence in the potential dropout-earnings of high school graduates and dropouts. Given the CIA, however, high school graduation is independent of potential earnings conditional on X<sup>i</sup> , so the selection-bias vanishes. Note also that in this case, the causal e§ect of

{57}------------------------------------------------

graduating high school on high school graduates is the population average high school graduation e§ect:

$$E[f_i(12) - f_i(11)|X_i, S_i = 12] = E[f_i(12) - f_i(11)|X_i].$$

This is important . . . but less important than the elimination of selection bias in [\(3.2.1\)](#page-55-0).

So far, we have constructed separate causal e§ects for each value taken on by the conditioning variable, X<sup>i</sup> . This leads to as many causal e§ects as there are values of X<sup>i</sup> , an embarrassment of riches. Empiricists almost always Önd it useful to boil a set of estimates down to a single summary measure, like the population average causal e§ect. By the law of iterated expectations, the population average causal e§ect of high school graduation is

$$E\{E[Y_i|X_i, S_i = 12] - E[Y_i|X_i, S_i = 11]\}$$
(3.2.3)

$$= E\{E[f_i(12) - f_i(11)|X_i]\}$$

$$= E[f_i(12) - f_i(11)] (3.2.4)$$

In the same spirit, we might be interested in the average causal e§ect of high school graduation on high school graduates:

$$E\{E[Y_i|X_i, S_i = 12] - E[Y_i|X_i, S_i = 11]|S_i = 12\}$$
(3.2.5)

<span id="page-57-0"></span>
$$= E\{E[f_i(12) - f_i(11)|X_i]|S_i = 12\}$$

$$= E[f_i(12) - f_i(11)|s_i = 12]. (3.2.6)$$

This parameter tells us how much high school graduates gained by virtue of having graduated. Likewise, for the e§ects of college graduation there is a distinction between E[fi(16) fi(12)js<sup>i</sup> = 16]; the average causal e§ect on college graduates and E[fi(16) fi(12)], the population average e§ect.

The population average e§ect, [\(3.2.3\)](#page-56-0), can be computed by averaging all of the X-speciÖc e§ects using the marginal distribution of X<sup>i</sup> ; while the average e§ect on high school or college graduates averages the X-speciÖc e§ects using the distribution of X<sup>i</sup> in these groups. In both cases, the empirical counterpart is a matching estimator: we make comparisons across schooling groups graduates for individuals with the same covariate values, compute the di§erence in their earnings, and then average these di§erences in some way.

In practice, there are many details to worry about when implementing a matching strategy. We Öll in some of the technical details on the mechanics of matching in Section [3.3.1,](#page-66-0) below. Here we note that a global drawback of the matching approach is that it is not "automatic," rather it requires two steps, matching and averaging. Estimating the standard errors of the resulting estimates may not be straightforward, either. 

{58}------------------------------------------------

A third consideration is that the two-way contrast at the heart of this subsection (high school or college completers versus dropouts) does not do full justice to the problem at hand. Since s<sup>i</sup> takes on many values, there are separate average causal e§ects for each possible increment in s<sup>i</sup> , which also must be summarized in some way.[9](#page-58-0) These considerations lead us back to regression.

Regression provides an easy-to-use empirical strategy that automatically turns the CIA into causal e§ects. Two routes can be traced from the CIA to regression. One assumes that fi(s) is both linear in s and the same for everyone except for an additive error term, in which case linear regression is a natural tool to estimate the features of fi(s). A more general but somewhat longer route recognizes that fi(s) almost certainly di§ers for di§erent people, and, moreover, need not be linear in s. Even so, allowing for random variation in fi(s) across people, and for non-linearity for a given person, regression can be thought of as strategy for the estimation of a weighted average of the individual-speciÖc di§erence, fi(s) fi(s 1). In fact, regression can be seen as a particular sort of matching estimator, capturing an average causal e§ect much like [3.2.3](#page-56-0) or [3.2.5.](#page-57-0)

At this point, we want to focus on the conditions required for regression to have a causal interpretation and not on the details of the regression-matching analog. We therefore start with the Örst route, a linear constant-e§ects causal model. Suppose that

<span id="page-58-1"></span>
$$f_i(s) = \alpha + \rho s + \eta_i. \tag{3.2.7}$$

In addition to being linear, this equation says that the functional relationship of interest is the same for everyone. Again, s is written without an i subscript to index individuals, because equation [\(3.2.7\)](#page-58-1) tells us what person i would earn for any value of s and not just the realized value, s<sup>i</sup> . In this case, however, the only individual-speciÖc and random part of fi(s) is a mean-zero error component, <sup>i</sup> , which captures unobserved factors that determine potential earnings.

Substituting the observed value s<sup>i</sup> for s in equation [\(3.2.7\)](#page-58-1), we have

<span id="page-58-2"></span>
$$Y_i = \alpha + \rho S_i + \eta_i. \tag{3.2.8}$$

Equation [\(3.2.8\)](#page-58-2) looks like a bivariate regression model, except that equation [\(3.2.7\)](#page-58-1) explicitly associates the coe¢ cients in [\(3.2.8\)](#page-58-2) with a causal relationship. Importantly, because equation [\(3.2.7\)](#page-58-1) is a causal model, s<sup>i</sup> may be correlated with potential outcomes, fi(s), or, in this case, the residual term in [\(3.2.8\)](#page-58-2), <sup>i</sup> .

$$\sum E[f_i(s) - f_i(s-1)]P(s).$$

where P(s) is the probability mass function for si: This is a discrete approximation to the average derivative, E[f i (si)]:

<span id="page-58-0"></span><sup>9</sup>For example, we might construct the average e§ect over <sup>s</sup> using the distribution of <sup>s</sup>i: In other words, estimate <sup>E</sup>[fi(s) fi(s 1)] for each s by matching, and then compute the average di§erence

{59}------------------------------------------------

Suppose now that the CIA holds given a vector of observed covariates, X<sup>i</sup> : In addition to the functional form assumption for potential outcomes embodied in [\(3.2.8\)](#page-58-2), we decompose the random part of potential earnings, <sup>i</sup> , into a linear function of observable characteristics, X<sup>i</sup> , and an error term, v<sup>i</sup> :

$$\eta_i = \mathbf{X}_i' \gamma + v_i,$$

where is a vector of population regression coe¢ cients that is assumed to satisfy E[<sup>i</sup> jX<sup>i</sup> ] =X<sup>0</sup> i . Because is deÖned by the regression of <sup>i</sup> on X<sup>i</sup> ;the residual v<sup>i</sup> and X<sup>i</sup> are uncorrelated by construction. Moreover, by virtue of the CIA, we have

$$E[f_i(s)|X_i, S_i] = E[f_i(s)|X_i] = \alpha + \rho s + E[\eta_i|X] = \alpha + \rho s + X_i'\gamma$$

Because mean-independence implies orthogonality, the residual in the linear causal model

<span id="page-59-0"></span>
$$Y_i = \alpha + \rho S_i + X_i' \gamma + v_i \tag{3.2.9}$$

is uncorrelated with the regressors, s<sup>i</sup> and X<sup>i</sup> , and the regression coe¢ cient is the causal e§ect of interest. It bears emphasizing once again that the key assumption here is that the observable characteristics, X<sup>i</sup> , are the only reason why <sup>i</sup> and s<sup>i</sup> (equivalently, fi(s) and s<sup>i</sup> ) are correlated. This is the selection-on-observables assumption for regression models discussed over a quarter century ago by Barnow, Cain, and Goldberger (1981). It remains the basis of most empirical work in Economics.