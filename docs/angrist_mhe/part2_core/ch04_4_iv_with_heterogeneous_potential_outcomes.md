# IV with Heterogeneous Potential Outcomes

> Pages: 126-127

The discussion of IV up to this point postulates a constant causal effect. In the case of a dummy variable like veteran status, this means  $Y_{1i}-Y_{0i}=\rho$  for all i, while with a multi-valued treatment like schooling, this means  $Y_{si}-Y_{s-1,i}=\rho$  for all s and all i. Both are highly stylized views of the world, especially the multi-valued case which imposes linearity as well as homogeneity. To focus on one thing at a time in a heterogeneous-effects model, we start with a zero-one causal variable. In this context, we'd like to allow for treatment-effect heterogeneity, in other words, a distribution of causal effects across individuals.

Why is treatment-effect heterogeneity important? The answer lies in the distinction between the two types of validity that characterize a research design. *Internal validity* is the question of whether a given design successfully uncovers causal effects for the population being studied. A randomized clinical trial or, for that matter, a good IV study, has a strong claim to internal validity. *External validity* is the predictive value of the study's findings in a different context. For example, if the study population in a randomized trial is especially likely to benefit from treatment, the resulting estimates may have little external validity. Likewise,

$$\{B[(\sigma_{11} + \kappa \Gamma' \Sigma_{22} \Gamma) A]^{-1} B\}^{-1}$$

where  $B=plim\left(\frac{Z_2'W_2}{N_2}\right)=plim\left(\frac{Z_1'W_1}{N_1}\right)$ ,  $A=plim\left(\frac{Z_1'Z_1}{N_1}\right)=plim\left(\frac{Z_2Z_2}{N_2}\right)$ ,  $plim\left(\frac{N_2}{N_1}\right)=\kappa$ ,  $\sigma_{11}$  is the variance of the reduced-form residual in data set 1, and  $\Sigma_{22}$  is the variance of the first-stage residual in data set 2. In principle, these pieces are easy enough to calculate. Other approaches to SSIV inference include those of Dee and Evans (2003), who calculate standard errors for just-identified models using the delta-method, and Bjorklund and Jantti (1997), who use a bootstrap.

<span id="page-126-0"></span><sup>&</sup>lt;sup>20</sup> Angrist and Krueger called this estimator SSIV because they were concerned with a scenario where a single data set is deliberately split in two. As discussed in Section (4.6.4), the resulting estimator may have less bias than conventional 2SLS. Inoue and Solon (2005) refer to the estimator Angrist and Krueger (1995) called SSIV as Two-sample 2SLS or TS2SLS.

<span id="page-126-1"></span><sup>&</sup>lt;sup>21</sup>This shortcut formula uses the standard errors from the manual SSIV second stage. The correct asymptotic covariance matrix formula, from Inoue and Solon (2005), is

{127}------------------------------------------------

draft-lottery estimates of the e§ects of conscription for service in the Vietnam era need not be a good measure of the consequences of voluntary military service. An econometric framework with heterogeneous treatment e§ects helps us to assess both the internal and external validity of IV estimates.[22](#page-127-0)