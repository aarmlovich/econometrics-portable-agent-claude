# Counting and Characterizing Compliers

> Pages: 138-146

Weíve seen that, except in special cases, each instrumental variable identiÖes a unique causal parameter, one speciÖc to the subpopulation of compliers for that instrument. Di§erent valid instruments for the same causal relation therefore estimate di§erent things, at least in principle (an important exception being

<span id="page-138-0"></span><sup>2 7</sup>Another application of IV to data from a randomized trial is Krueger (1999). This study uses randomly assigned class size as an instrument for actual class size with data from the Tennessee STAR experiment. For students in Örst grade and higher, actual class size di§ers from randomly assigned class size in the STAR experiment because parents and teachers move students around in years after the experiment began. Krueger 1999 also illustrates 2SLS applied to a model with variable treatment intensity, as discussed in section [4.5.3.](#page-151-0)

{139}------------------------------------------------

instruments that allow for perfect compliance on one side or the other). Although di§erent IV estimates are "weighted-up" by 2SLS to produce a single average causal e§ect, over-identiÖcation testing of the sort discussed in Section [4.2.2,](#page-120-1) where multiple instruments are validated according to whether or not they estimate the same thing, is out the window in a fully heterogeneous world.

Di§erences in compliant sub-populations might explain variability in treatment e§ects from one instrument to another. We would therefore like to learn as much as we can about the compliers for di§erent instruments. Moreover, if the compliant subpopulation is similar to other populations of interest, the case for extrapolating estimated causal e§ects to these other populations is stronger. In this spirit, Acemoglu and Angrist (2000) argue that quarter-of-birth instruments and state compulsory attendance laws (the minimum schooling required before leaving school in your state of birth when you were 14) a§ect essentially the same group of people and for the same reasons. We therefore expect IV estimates of the returns to schooling from these two sets of instruments to be similar. We might also expect the quarter of birth estimates to predict the impact of contemporary proposals to strengthen compulsory attendance laws.

On the other hand, if the compliant subpopulations associated with two or more instruments are very di§erent, yet the IV estimates they generate are similar, we might be prepared to adopt homogeneous e§ects as a working hypothesis. This revives the over-identiÖcation idea, but puts it at the service of external validity.[28](#page-139-0) This reasoning is illustrated by the study of the e§ects of family size on childrenís education by Angrist, Lavy, and Schlosser (2006). The Angrist, Lavy, and Schlosser study is motivated by the observation that children from larger families typically end up with less education than those from smaller families. A long-standing concern in research on fertility is whether the observed negative correlation between larger families and worse outcomes is causal. As it turns out, IV estimates of the e§ect of family size using a number of di§erent instruments, each with very di§erent compliant subpopulations, all generate results showing no e§ect of family size. Angrist, Lavy, and Schlosser (2006) argue that their results point to a common treatment of zero for just about everybody in the Israeli population they study.

We have already seen that the size of a complier group is easy to measure. This is just the Wald Örst-stage, since, given monotonicity, we have

$$P[D_{1i}>D_{0i}] = E[D_{1i} - D_{0i}]$$
  
=  $E[D_{1i}] - E[D_{0i}]$   
=  $E[D_{i}|Z_{i}=1] - E[D_{i}|Z_{i}=0].$ 

We can also tell what proportion of the treated are compliers since, for compliers, treatment status is

<span id="page-139-0"></span><sup>2 8</sup> In fact, maintaining the hypothesis that all instruments in an over-identiÖed model are valid, the traditional overidentiÖcation test statistic becomes a formal test for treatment-e§ect heterogeneity.

{140}------------------------------------------------

completely determined by  $z_i$ . Start with the definition of conditional probability:

<span id="page-140-0"></span>
$$P[D_{1i} > D_{0i}|D_{i}=1] = \frac{P[D_{i}=1|D_{1i}>D_{0i}]P[D_{1i}>D_{0i}]}{P[D_{i}=1]}$$

$$= \frac{P[Z_{i}=1](E[D_{i}|Z_{i}=1] - E[D_{i}|Z_{i}=0])}{P[D_{i}=1]}.$$
(4.4.7)

The second equality uses the fact that  $P[D_i=1|D_{1i}>D_{0i}]=P[Z_i=1|D_{1i}>D_{0i}]$  and that  $P[Z_i=1|D_{1i}>D_{0i}]=P[Z_i=1]$  by Independence. In other words, the proportion of the treated who are compliers is given by the first stage, times the probability the instrument is switched on, divided by the proportion treated.

Formula (4.4.7) is illustrated here by calculating the proportion of veterans who are draft-lottery compliers. The ingredients are reported in Table 4.4.2. For example, for white men born in 1950, the first stage is .159, the probability of draft-eligibility is  $\frac{195}{366}$ , and the marginal probability of treatment is .267. From these statistics, we compute that the compliant subpopulation is .32 of the veteran population in this group. The proportion of veterans who were draft-lottery compliers falls to 20 percent for non-white men born in 1950. This is not surprising since the draft-lottery first stage is considerably weaker for non-whites. The last column of the table reports the proportion of nonveterans who would have served if they had been draft-eligible. This ranges from 3 percent of non-whites to 10 percent of whites, reflecting the fact that most non-veterans were deferred, ineligible, or unqualified for military service.


{141}------------------------------------------------

{142}------------------------------------------------

The e§ect of compulsory military service is the parameter of primary interest in the Angrist (1990) study, so the fact that draft-eligibility compliers are a minority of veterans is not really a limitation of this study. Even in the Vietnam era, most soldiers were volunteers, a little-appreciated fact about Vietnam-era veterans. The LATE interpretation of IV estimates using the draft lottery highlights the fact that other identiÖcation strategies are needed to estimate e§ects of military service on volunteers (some of these are implemented in Angrist, 1998).

The remaining rows in Table [4.4.2](#page-111-0) document the size of the compliant subpopulation for the twins and sibling-sex composition instruments used by Angrist and Evans (1998) to estimate the e§ects of childbearing and for the quarter of birth instruments and compulsory attendance laws used by Angrist and Krueger (1991) and Acemoglu and Angrist (2000) to estimates the returns to schooling. In each of these studies, the compliant subpopulation is a small fraction of the treated group. For example, less than 2 percent of those who graduated from high school did so because of compulsory attendance laws or by virtue of having been born in a late quarter.

The question of whether a small compliant subpopulation is a cause for worry is context-speciÖc. In some cases, it seems fair to say, "you get what you need." With many policy interventions, for example, it is a marginal group that is of primary interest, a point emphasized in McClellanís (1994) landmark IV study of the e§ects of surgery on heart attack patients. McClellan uses the relative distance to cardiac care facilities to construct instruments for whether an elderly heart-attack patient is treated with a surgical intervention. Most patients get the same treatment either way, but for some, the case for major surgery is marginal. In such cases, providers or patients opt for a less invasive strategy if the nearest surgical facility is far away. McClellan Önds little beneÖt from surgical procedures for this marginal group. Similarly, an increase in the compulsory attendance age to age 18 is clearly irrelevant for the vast majority of American high school students, but it will a§ect a few who would otherwise drop out. IV estimates suggest the economic returns to schooling for this marginal group are substantial.

The last column of Table [4.4.2](#page-111-0) illustrates the special feature of twins instruments alluded to at the end of the previous subsection. As before, let d<sup>i</sup> = 0 for women with two children in a sample of women with at least two children, while d<sup>i</sup> = 1 indicates women who have more than two. Because there are no never-takers in response to the event of a multiple birth, i.e., all mothers who have twins at second birth end up with (at least) three children, the probability of compliance among those with d<sup>i</sup> = 0 is virtually one (the table shows an entry of .97). LATE is therefore the e§ect on the non-treated, E[y1<sup>i</sup>y0<sup>i</sup> jd<sup>i</sup> = 0], in this case.

Unlike the size of the complier group, information on the characteristics of compliers seems like a tall order because the compliers cannot be individually identiÖed. Because we canít see both d1<sup>i</sup> and d0<sup>i</sup> for each individual, we canít just list those with d1<sup>i</sup> >d0<sup>i</sup> and then calculate the distribution of characteristics for this group. Nevertheless, itís easy to describe the distribution of complier characteristics. To simplify, 

{143}------------------------------------------------

we focus here on characteristics - like race or degree completion - that can be described by dummy variables. In this case, everything we need to know can be learned from variation in the first stage across covariate groups.

Let  $x_{1i}$  be a Bernoulli-distributed characteristic, say a dummy indicating college graduates. Are sexcomposition compliers more or less likely to be college graduates than other women with two children? This question is answered by the following calculation:

$$\frac{P[x_{1i} = 1 | D_{1i} > D_{0i}]}{P[x_{1i} = 1]} = \frac{P[D_{1i} > D_{0i} | x_{1i} = 1]}{P[D_{1i} > D_{0i}]} = \frac{E[D_{i} | Z_{i} = 1, x_{1i} = 1] - E[D_{i} | Z_{i} = 0, x_{1i} = 1]}{E[D_{i} | Z_{i} = 1] - E[D_{i} | Z_{i} = 0]}.$$
 (4.4.8)

In other words, the relative likelihood a complier is a college graduate is given by the ratio of the first stage for college graduates to the overall first stage.<sup>29</sup>

This calculation is illustrated in Table 4.4.3, which reports compliers' characteristics ratios for age at first birth, nonwhite race, and degree completion using twins and same-sex instruments. The table was constructed from the Angrist and Evans (1998) 1980 census extract. Twins compliers are much more likely to be over 30 than the average mother in the sample, reflecting the fact that younger women who had a multiple birth were likely to go on to have additional children anyway. Twins compliers are also more educated than the average mother, while sex-composition compliers are less educated. This helps to explain the smaller 2SLS estimates generated by twins instruments (reported here in Table 4.1.4), since Angrist and Evans (1998) show that the labor supply consequences of childbearing decline with mother's schooling.

$$E[\mathbf{X}_i|\mathbf{D}_{1i} > \mathbf{D}_{0i}] = \frac{E[\kappa_i \mathbf{X}_i]}{E[\kappa_i]},$$

where

$$\kappa_i = 1 - \frac{D_i(1 - Z_i)}{1 - P(Z_i = 1 | X_i)} - \frac{(1 - D_i)Z_i}{P(Z_i = 1 X_i)}.$$

This works because the weighting function,  $\kappa_i$ , "finds compliers," in a sense discussed in Section (4.5.2), below.

<span id="page-143-0"></span><sup>&</sup>lt;sup>29</sup> A general method for constructing the mean or other features of the distribution of covariates for compliers uses Abadie's (2003) kappa-weighting scheme. For example,

{144}------------------------------------------------

<table><tbody><tr><th>4.4.3:<br/>Table</th><th>Complier-characteristics</th><th>ratios</th><th>sex-composition<br/>and<br/>twins<br/>for</th><th>instruments</th><th></th></tr><tr><td></td><td></td><td>Twins</td><td>birth<br/>second<br/>at</td><td>two<br/>First</td><td>same<br/>are<br/>children</td></tr><tr><td>Variable</td><td>[x]<br/>(1)<br/>E</td><td>d0]<br/>&gt;<br/>(2)<br/>[xjd1<br/>E</td><td>X]<br/>d0] =P [<br/>(3)<br/>&gt;<br/>[xjd1<br/>P</td><td>d0]<br/>&gt;<br/>(6)<br/>[xjd1<br/>E</td><td>X]<br/>sex<br/>d0] =P [<br/>(5)<br/>&gt;<br/>[xjd1<br/>P</td></tr><tr><td>birth<br/>Örst<br/>at<br/>older<br/>or<br/>30<br/>Age</td><td>0.00291</td><td>0.00404</td><td>(0.0201)<br/>1.39</td><td>0.00233</td><td>(0.374)<br/>0.995</td></tr><tr><td>hispanic<br/>or<br/>Black</td><td>0.125</td><td>0.103</td><td>(0.00421)<br/>0.822</td><td>0.102</td><td>(0.0775)<br/>0.814</td></tr><tr><td>graduate<br/>school<br/>High</td><td>0.822</td><td>0.861</td><td>(0.000772)<br/>1.048</td><td>0.815</td><td>(0.0140)<br/>0.998</td></tr><tr><td>graduate<br/>College</td><td>0.132</td><td>0.151</td><td>(0.00376)<br/>1.14</td><td>0.0904</td><td>(0.0692)<br/>0.704</td></tr><tr><td>an<br/>reports<br/>table<br/>The<br/>Notes:</td><td>complier<br/>of<br/>analysis</td><td>characteristics</td><td>sex-composition<br/>and<br/>twins<br/>for</td><td>instru-</td><td></td></tr><tr><td>columns<br/>in<br/>ratios<br/>The<br/>ments.</td><td>give<br/>5<br/>and<br/>3</td><td>likelihood<br/>relative<br/>the</td><td>the<br/>have<br/>compliers</td><td>characteristic</td><td></td></tr><tr><td>are<br/>Data<br/>row.<br/>each<br/>in<br/>indicated</td><td>1980<br/>the<br/>from</td><td>5%<br/>Census</td><td>married<br/>including<br/>sample,</td><td>age<br/>mothers</td><td></td></tr><tr><td>children,<br/>two<br/>least<br/>at<br/>with<br/>21-35</td><td>Angrist<br/>in<br/>as</td><td>(1998).<br/>Evans<br/>and</td><td>is<br/>size<br/>sample<br/>The</td><td>all<br/>for<br/>254,654</td><td></td></tr><tr><td>columns.</td><td></td><td></td><td></td><td></td><td></td></tr></tbody></table>

{145}------------------------------------------------

# 4.5 Generalizing LATE

The LATE theorem applies to a stripped-down causal model where a single dummy instrument is used to estimate the impact of a dummy treatment with no covariates. We can generalize this in three important ways: multiple instruments (e.g., a set of quarter-of-birth dummies), models with covariates (e.g., controls for year of birth), and models with variable and continuous treatment intensity (e.g., years of schooling). In all three cases, the IV estimand is a weighted average of causal e§ects for instrument-speciÖc compliers. The econometric tool remains 2SLS and the interpretation remains fundamentally similar to the basic LATE result, with a few bells and whistles. 2SLS with multiple instruments produces a causal e§ect that averages IV estimands using the instruments one at a time; 2SLS with covariates produces an average of covariatespeciÖc LATEs; 2SLS with variable or continuous treatment intensity produces a weighted average derivative along the length of a possibly nonlinear causal response function.

# 4.5.1 LATE with Multiple Instruments

The multiple-instruments extension is easy to see. This is essentially the same as a result we discussed in the grouped-data context. Consider a pair of dummy instruments, z1<sup>i</sup> and z2<sup>i</sup> . Without loss of generality, assume these dummies are mutually exclusive (if not, then we can work with a mutually exclusive set of three dummies, z1<sup>i</sup>(1z2<sup>i</sup>);z2<sup>i</sup>(1z1<sup>i</sup>), and z1<sup>i</sup>z2<sup>i</sup>). The two dummies can be used to construct Wald estimators. Again, without loss of generality assume monotonicity is satisÖed for each with a positive Örst stage (if not, we can recode the dummies so this is true). Both therefore estimate a version of E[y1<sup>i</sup>y0<sup>i</sup> jd1<sup>i</sup> >d0<sup>i</sup> ]; though the population with d1<sup>i</sup> >d0<sup>i</sup> di§ers for z1<sup>i</sup> and z2<sup>i</sup> .

Instead of Wald estimators, we can use z1<sup>i</sup> and z2<sup>i</sup> together in a 2SLS procedure. Since these two dummies and a constant exhaust the information in the instrument set, this 2SLS procedure is the same as grouped-data estimation using conditional means deÖned given z1<sup>i</sup> and z2<sup>i</sup> (whether or not the instruments are correlated). As in Angrist (1991), the resulting grouped-data estimator is a linear combination of the underlying Wald estimators. In other words, it is a linear combination of the instrument-speciÖc LATEs using the instruments one at a time (in fact, it is the e¢ cient linear combination in a traditional homoskedastic linear constant-e§ects model).

This argument is not quite complete since we havenít shown that the linear combination of LATEs produced by 2SLS is also a weighted average (i.e., the weights are non-negative and sum to one). The relevant weighting formulas appear in Imbens and Angrist (1994) and Angrist and Imbens (1995). The formulas are a little messy, so here we lay out a simple version based on the two-instrument example. The example shows that 2SLS using z1<sup>i</sup> and z2<sup>i</sup> together is a weighted average of IV estimates using z1<sup>i</sup> and z2<sup>i</sup> one at a time. Let

$$\rho_j = \frac{Cov(\mathbf{Y}_i, \mathbf{Z}_{ji})}{Cov(\mathbf{D}_i, \mathbf{Z}_{ji})}; j = 1, 2$$

{146}------------------------------------------------

denote the two IV estimands using z1<sup>i</sup> and z2<sup>i</sup> :

The (population) Örst stage Ötted values for 2SLS are dà<sup>i</sup> = 11z1<sup>i</sup> + 12z2<sup>i</sup> . By virtue of the IV interpretation of 2SLS, the 2SLS estimand is

$$\begin{split} \rho_{2SLS} &= \frac{Cov(\mathbf{Y}_i, \hat{\mathbf{D}}_i)}{Cov(\mathbf{D}_i, \hat{\mathbf{D}}_i)} = \frac{\pi_{11}Cov(\mathbf{Y}_i, \mathbf{Z}_{1i})}{Cov(\mathbf{D}_i, \hat{\mathbf{D}}_i)} + \frac{\pi_{12}Cov(\mathbf{Y}_i, \mathbf{Z}_{2i})}{Cov(\mathbf{D}_i, \hat{\mathbf{D}}_i)} \\ &= \left[\frac{\pi_{11}Cov(\mathbf{D}_i, \mathbf{Z}_{1i})}{Cov(\mathbf{D}_i, \hat{\mathbf{D}}_i)}\right] \left[\frac{Cov(\mathbf{Y}_i, \mathbf{Z}_{1i})}{Cov(\mathbf{D}_i, \mathbf{Z}_{1i})}\right] + \left[\frac{\pi_{21}Cov(\mathbf{D}_i, \mathbf{Z}_{2i})}{Cov(\mathbf{D}_i, \hat{\mathbf{D}}_i)}\right] \left[\frac{Cov(\mathbf{Y}_i, \mathbf{Z}_{2i})}{Cov(\mathbf{D}_i, \mathbf{Z}_{2i})}\right] \\ &= \psi \rho_1 + (1 - \psi)\rho_2, \end{split}$$

where

$$\psi = \frac{\pi_{11}Cov(\mathbf{D}_i, \mathbf{Z}_{1i})}{\pi_{11}Cov(\mathbf{D}_i, \mathbf{Z}_{1i}) + \pi_{21}Cov(\mathbf{D}_i, \mathbf{Z}_{2i})}$$

is a number between zero and one that depends on the relative strength of each instrument in the Örst stage. Thus, we have shown that 2SLS is a weighted average of causal e§ects for instrument-speciÖc compliant subpopulations. Suppose, for example, that z1<sup>i</sup> denotes twins births and z2<sup>i</sup> indicates same-sex sibships in families with two or more children, both instruments for family size as in Angrist and Evans (1998). A multiple second birth increases the likelihood of having a third child by about :6 while a same-sex sibling pair increases the likelihood of a third birth by about :07. When these two instruments are used together, the resulting 2SLS estimates are a weighted average of the Wald estimates produced by using the instruments one at a time.[30](#page-146-1)