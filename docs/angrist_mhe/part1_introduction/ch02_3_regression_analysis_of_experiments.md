# Regression Analysis of Experiments

> Pages: 31-36

Regression is a useful tool for the study of causal questions, including the analysis of data from experiments. Suppose (for now) that the treatment e§ect is the same for everyone, say y1<sup>i</sup> y0<sup>i</sup> = , a constant. With

extremely well implemented randomized trial. Kruegerís (1999) analysis suggests that none of these implementation problems a§ected the main conclusions of the study.

<span id="page-31-0"></span><sup>5</sup> The Angrist-Lavy (1999) results turn up again in Chapter [6,](#page-204-0) as an illustration of the quasi-experimental regressiondiscontinuity research design.

{32}------------------------------------------------

constant treatment effects, we can rewrite equation (2.1.1) in the form

<span id="page-32-0"></span>
$$Y_{i} = \alpha + \rho \quad D_{i} + \eta_{i},$$

$$H \quad H \quad H \quad H \quad (2.3.1)$$

$$E(Y_{0i}) \quad (Y_{1i} - Y_{0i}) \quad Y_{0i} - E(Y_{0i})$$

where  $\eta_i$  is the random part of  $Y_{0i}$ . Evaluating the conditional expectation of this equation with treatment status switched off and on gives

$$E[Y_i|D_i = 1] = \alpha + \rho + E[\eta_i|D_i = 1]$$

$$E[Y_i|D_i = 0] = \alpha + E[\eta_i|D_i = 0],$$

so that,

$$E[Y_i|D_i = 1] - E[Y_i|D_i = 0] = \underbrace{\rho}_{\text{treatment effect}}$$

$$+\underbrace{E[\eta_i|\mathbf{D}_i=1]-E[\eta_i|\mathbf{D}_i=0]}_{\text{selection bias}} \ .$$

Thus, selection bias amounts to correlation between the regression error term,  $\eta_i$ , and the regressor,  $D_i$ . Since

$$E[\eta_i|D_i = 1] - E[\eta_i|D_i = 0] = E[Y_{0i}|D_i = 1] - E[Y_{0i}|D_i = 0],$$

this correlation reflects the difference in (no-treatment) potential outcomes between those who get treated and those who don't. In the hospital allegory, those who were treated had poorer health outcomes in the no-treatment state, while in the Angrist and Lavy (1999) study, students in smaller classes tend to have intrinsically lower test scores.

In the STAR experiment, where  $D_i$  is randomly assigned, the selection term disappears, and a regression of  $Y_i$  on  $D_i$  estimates the causal effect of interest,  $\rho$ . The remainder of Table 2.2.2 shows different regression specifications, some of which include covariates other than the random assignment indicator,  $D_i$ . Covariates play two roles in regression analyses of experimental data. First, the STAR experimental design used conditional random assignment. In particular, assignment to classes of different sizes was random within schools, but not across schools. Students attending schools of different types (say, urban versus rural) were a bit more or less likely to be assigned to a small class. The comparison in column 1 of Table 2.2.2, which makes no adjustment for this, might therefore be contaminated by differences in achievement in schools of different types. To adjust for this, some of Krueger's regression models include school fixed effects, i.e., a separate intercept for each school in the STAR data. In practice, the consequences of adjusting for school

{33}------------------------------------------------

Öxed e§ects is rather minor, but we wouldnít know this without taking a look. We will have more to say about regression models with Öxed e§ects in Chapter [5.](#page-180-0)

The other controls in Kruegerís table describe student characteristics such as race, age, and free lunch status. We saw before that these individual characteristics are balanced across class types, i.e. they are not systematically related to the class-size assignment of the student. If these controls, call them X<sup>i</sup> , are uncorrelated with the treatment d<sup>i</sup> , then they will not a§ect the estimate of . In other words, estimates of in the long regression,

$$Y_i = \alpha + \rho D_i + X_i' \gamma + \eta_i \tag{2.3.2}$$

will be close to estimates of in the short regression, [\(2.3.1\)](#page-32-0). This is a point we expand on in Chapter [3.](#page-36-0)

Nevertheless, inclusion of the variables X<sup>i</sup> may generate more precise estimates of the causal e§ect of interest. Notice that the standard error of the estimated treatment e§ects in column 3 is smaller than the corresponding standard error in column 2. Although the control variables, X<sup>i</sup> , are uncorrelated with di , they have substantial explanatory power for y<sup>i</sup> . Including these control variables therefore reduces the residual variance, which in turn lowers the standard error of the regression estimates. Similarly, the standard errors of the estimates of are reduced by the inclusion of school Öxed e§ects because these too explain an important part of the variance in student performance. The last column adds teacher characteristics. Because teachers were randomly assigned to classes, and teacher characteristics appear to have little to do with student achievement in these data, both the estimated e§ect of small classes and itís standard error are unchanged by the addition of teacher variables.

Regression plays an exceptionally important role in empirical economic research. Some regressions are simply descriptive tools, as in much of the research on earnings inequality. As weíve seen in this chapter, regression is well-suited to the analysis of experimental data. In some cases, regression can also be used to approximate experiments in the absence of random assignment. But before we can get into the important question of when a regression is likely to have a causal interpretation, it is useful to review a number of fundamental regression facts and properties. These facts and properties are reliably true for any regression, regardless of your purpose in running it.

{34}------------------------------------------------

Part II

The Core

{35}------------------------------------------------

<table><tbody><tr><th></th><th></th><th></th></tr><tr><th></th><th></th><th></th></tr><tr><th></th><th></th><th></th></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td></tr></tbody></table>

{36}------------------------------------------------