# IV and causality

> Pages: 99-103

We like to tell the IV story in two iterations, Örst in a restricted model with constant e§ects, then in a framework with unrestricted heterogeneous potential outcomes, in which case causal e§ects must also be heterogeneous. The introduction of heterogeneous e§ects enriches the interpretation of IV estimands, without changing the mechanics of the core statistical methods we are most likely to use in practice (typically, twostage least squares). An initial focus on constant e§ects allows us to explain the mechanics of IV with a

<span id="page-99-1"></span><span id="page-99-0"></span><sup>2</sup>Key historical references here are Wald (1940) and Durbin (1954), both discussed below.

<sup>3</sup> See Angrist and Krueger (2001) for a brief exposition of the history and uses of IV; Stock and Trebbi (2003) for a detailed account of the birth of IV; and Morgan (1990) for an extended history of econometric ideas, including the simultaneous equations model.

{100}------------------------------------------------

4.1. IV AND CAUSALITY 85

minimum of fuss.

To motivate the constant-e§ects setup as a framework for the causal link between schooling and wages, suppose, as before, that potential outcomes can be written

$$Y_{si} \equiv f_i(s)$$
,

and that

$$f_i(s) = \pi_0 + \pi_1 s + \eta_i,$$
 (4.1.1)

as in the introduction to regression in Chapter [3.](#page-36-0) Also, as in the earlier discussion, imagine that there is a vector of control variables, A<sup>i</sup> , called ìabilityî, that gives a selection-on-observables story:

$$\eta_i = A_i' \gamma + v_i,$$

where is again a vector of population regression coe¢ cients, so that v<sup>i</sup> and A<sup>i</sup> are uncorrelated by construction. For now, the variables A<sup>i</sup> , are assumed to be the only reason why <sup>i</sup> and s<sup>i</sup> are correlated, so that

$$E[\mathbf{s}_i v_i] = 0.$$

In other words if A<sup>i</sup> were observed, we would be happy to include it in the regression of wages on schooling; thereby producing a long regression that can be written

<span id="page-100-0"></span>
$$Y_i = \alpha + \rho S_i + A_i' \gamma + v_i. \tag{4.1.2}$$

Equation [\(4.1.2\)](#page-100-0) is a version of the linear causal model, [\(3.2.9\)](#page-59-0). The error term in this equation is the random part of potential outcomes, v<sup>i</sup> , left over after controlling for A<sup>i</sup> . This error term is uncorrelated with schooling by assumption. If this assumption turns out to be correct, the population regression of y<sup>i</sup> on s<sup>i</sup> and A<sup>i</sup> produces the coe¢ cients in [\(4.1.2\)](#page-100-0).

The problem we initially want to tackle is how to estimate the long-regression coe¢ cient, , when A<sup>i</sup> is unobserved. Instrumental variables methods can be used to accomplish this when the researcher has access to a variable (the instrument, which weíll call zi), that is correlated with the causal variable of interest, s<sup>i</sup> , but uncorrelated with any other determinants of the dependent variable. Here, the phrase "uncorrelated with any other determinants of the dependent variables" is like saying Cov(<sup>i</sup> ;zi) = 0; or, equivalently, z<sup>i</sup> is uncorrelated with both A<sup>i</sup> and v<sup>i</sup> . This statement is called an exclusion restriction since z<sup>i</sup> can be said to be excluded from the causal model of interest. The exclusion restriction is a version of the conditional independence assumption of the previous chapter, except that now it is the instrument which is independent of potential outcomes, instead of schooling itself (the "conditional" in conditional independence enters into


{101}------------------------------------------------

the discussion when we consider IV models with covariates).

Given the exclusion restriction, it follows from equation [\(4.1.2\)](#page-100-0) that

<span id="page-101-0"></span>
$$\rho = \frac{Cov(\mathbf{Y}_i, \mathbf{Z}_i)}{Cov(\mathbf{S}_i, \mathbf{Z}_i)} = \frac{Cov(\mathbf{Y}_i, \mathbf{Z}_i)/V(\mathbf{Z}_i)}{Cov(\mathbf{S}_i, \mathbf{Z}_i)/V(\mathbf{Z}_i)}.$$
(4.1.3)

The second equality in [\(4.1.3\)](#page-101-0) is useful because itís usually easier to think in terms of regression coe¢ cients than in terms of covariances. The coe¢ cient of interest, , is the ratio of the population regression of y<sup>i</sup> on z<sup>i</sup> (the reduced form) to the population regression of s<sup>i</sup> on z<sup>i</sup> (the Örst stage). The IV estimator is the sample analog of expression [\(4.1.3\)](#page-101-0). Note that the IV estimand is predicated on the notion that the Örst stage is not zero, but this is something you can check in the data. As a rule, if the Örst stage is only marginally signiÖcantly di§erent from zero, the resulting IV estimates are unlikely to be informative, a point we return to later.

Itís worth recapping the assumptions needed for the ratio of covariances in [\(4.1.3\)](#page-101-0) to equal the casual e§ect, : First, the instrument must have a clear e§ect on s<sup>i</sup> . This is the Örst stage. Second, the only reason for the relationship between y<sup>i</sup> and z<sup>i</sup> is the Örst-stage. For the moment, weíre calling this second assumption the exclusion restriction, though as weíll see in the discussion of models with heterogeneous e§ects, this assumption really has two parts: the Örst is the statement that the instrument is as good as randomly assigned (i.e., independent of potential outcomes, conditional on covariates), while the second is that the instrument has no e§ect on outcomes other than through the Örst-stage channel.

So where can you Önd an instrumental variable? Good instruments come from institutional knowledge and your ideas about the processes determining the variable of interest. For example, the economic model of education suggests that educational attainment is determined by comparing the costs and beneÖts of alternative choices. Thus, one possible source of instruments for schooling is di§erences in costs due, say, to loan policies or other subsidies that vary independently of ability or earnings potential. A second source of variation in schooling is institutional constraints. A set of institutional constraints relevant for schooling are compulsory schooling laws. Angrist and Krueger (1991) exploit the variation induced by compulsory schooling in a paper that typiÖes the use of ìnatural experimentsîto try to eliminate omitted variables bias

The starting point for the Angrist and Krueger (1991) quarter-of-birth strategy is the observation that most states required students to enter school in the calendar year in which they turn 6. School start age is therefore a function of date of birth. SpeciÖcally, those born late in the year are young for their grade. In states with a December 31st birthday cuto§, children born in the fourth quarter enter school shortly before they turn 6, while those born in the Örst quarter enter school at around age 6 2 . Furthermore, because compulsory schooling laws typically require students to remain in school only until their 16th birthday, these groups of students will be in di§erent grades or through a given grade to di§erent degree, when they reach the legal dropout age. In essence, the combination of school start age policies and compulsory schooling laws

{102}------------------------------------------------

creates a natural experiment in which children are compelled to attend school for di§erent lengths of time depending on their birthdays.

Angrist and Krueger looked at the relationship between educational attainment and quarter of birth using US census data. Panel A of Figure [4.1.1](#page-103-0) (adapted from Angrist and Krueger, 2001) displays the education-quarter-of-birth pattern for men in the 1980 Census who were born in the 1930s. The Ögure clearly shows that men born earlier in the calendar year tend to have lower average schooling levels. Panel A of Figure [4.1.1](#page-103-0) is a graphical representation of the Örst-stage. The Örst-stage in a general IV framework is the regression of the causal variable of interest on covariates and the instrument(s). The plot summarizes this regression because average schooling by year and quarter of birth is what you get for Ötted values from a regression of schooling on a full set of year-of-birth and quarter-of-birth dummies.

Panel B of Figure [4.1.1](#page-103-0) displays average earnings by quarter of birth for the same sample used to construct panel A. This panel illustrates what econometricians call the ìreduced formîrelationship between the instruments and the dependent variable. The reduced form is the regression of the dependent variable on any covariates in the model and the instrument(s). Panel B shows that older cohorts tend to have higher earnings, because earnings rise with work experience. The Ögure also shows that men born in early quarters almost always earned less, on average, than those born later in the year, even after adjusting for year of birth, which plays the role of an exogenous covariate in the Angrist and Krueger (1991) setup. Importantly, this reduced-form relation parallels the quarter-of-birth pattern in schooling, suggesting the two patterns are closely related. Because an individualís date of birth is probably unrelated to his or her innate ability, motivation, or family connections, it seems credible to assert that the only reason for the up-and-down quarter-of-birth pattern in earnings is indeed the up-and-down quarter-of-birth pattern in schooling. This is the critical assumption that drives the quarter-of-birth IV story.[4](#page-102-0)

A mathematical representation of the story told by Figure [4.1.1](#page-103-0) comes from the Örst-stage and reducedform regression equations, spelled out below:

<span id="page-102-1"></span>
$$S_i = X_i' \pi_{10} + \pi_{11} Z_i + \xi_{1i}$$
 (4.1.4a)

$$Y_i = X_i' \pi_{20} + \pi_{21} Z_i + \xi_{2i}$$
 (4.1.4b)

The parameter <sup>11</sup> in equation [\(4.1.4a\)](#page-102-1) captures the Örst-stage e§ect of z<sup>i</sup> on s<sup>i</sup> , adjusting for covariates,

<span id="page-102-0"></span><sup>4</sup>Other explanations are possible, the most likely being some sort of family background e§ect associated with season of birth (see, e.g., Bound, Jaeger, and Baker, 1995). Weighing against the possibility of omitted family background e§ects is the fact that the quarter of birth pattern in average schooling is much more pronounced at the schooling levels most a§ected by compulsory attendance laws. Another possible concern is a pure age-at-entry e§ect which operates through channels other than highest grade completed (e.g., achievement). The causal e§ect of age-at-entry on learning is di¢ cult, if not impossible, to separate from pure age e§ects, as noted in Chapter [1\)](#page-18-0). A recent study by Elder and Lubotsky (2008) argues that the evolution of putative age-at-entry e§ects over time is more consistent with e§ects due to age di§erences per se than to a within-school learning advantage for older students.

{103}------------------------------------------------