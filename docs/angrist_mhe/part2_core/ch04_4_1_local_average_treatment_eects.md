# Local Average Treatment E§ects

> Pages: 127-134

In an IV framework, the engine that drives causal inference is the instrument, z<sup>i</sup> , but the variable of interest is still d<sup>i</sup> . This feature of the IV setup leads us to adopt a generalized potential-outcomes concept, indexed against both instruments and treatment status. Let yi(d; z) denote the potential outcome of individual i were this person to have treatment status d<sup>i</sup> = d and instrument value z<sup>i</sup> = z. This tells us, for example, what the earnings of i would be given alternative combinations of veteran status and draft-eligibility status. The causal e§ect of veteran status given iís realized draft-eligibility status is yi(1;zi)yi(0;zi), while the causal e§ect of draft-eligibility status given iís veteran status is yi(d<sup>i</sup> ; 1)yi(d<sup>i</sup> ; 0).

We can think of instrumental variables as initiating a causal chain where the instrument, z<sup>i</sup> , a§ects the variable of interest, d<sup>i</sup> , which in turn a§ects outcomes, y<sup>i</sup> . To make this precise, we need notation to express the idea that the instrument has a causal e§ect on d<sup>i</sup> . Let d1<sup>i</sup> be iís treatment status when z<sup>i</sup> = 1, while d0<sup>i</sup> is iís treatment status when z<sup>i</sup> = 0: Observed treatment status is therefore

$$D_i = D_{0i} + (D_{1i} - D_{0i})Z_i = \pi_0 + \pi_{1i}Z_i + \xi_i.$$
(4.4.1)

In random-coe¢ cients notation, <sup>0</sup> E[d0<sup>i</sup> ] and 1<sup>i</sup> (d1<sup>i</sup>d0<sup>i</sup>), so 1<sup>i</sup> is the heterogeneous causal e§ect of the instrument on d<sup>i</sup> . As with potential outcomes, only one of the potential treatment assignments, d1<sup>i</sup> and d0<sup>i</sup> , is ever observed for any one person. In the draft lottery example, d0<sup>i</sup> tells us whether i would serve in the military if he draws a high (draft-ineligible) lottery number, while d1<sup>i</sup> tells us whether i would serve if he draws a low (draft-eligible) lottery number. We get to see one or the other of these potential assignments depending on z<sup>i</sup> . The average causal e§ect of z<sup>i</sup> on d<sup>i</sup> is E[1<sup>i</sup> ].

The Örst assumption in the heterogeneous framework is that the instrument is as good as randomly assigned: it is independent of the vector of potential outcomes and potential treatment assignments. Formally, this can be written

$$[\{Y_i(d,z); \forall d,z\}, D_{1i}, D_{0i}] \coprod Z_i,$$
 (4.4.2)

Independence is su¢ cient for a causal interpretation of the reduced form, i.e., the regression of y<sup>i</sup> on z<sup>i</sup> .

<span id="page-127-0"></span><sup>2 2</sup> The distinction between internal and external validity is relatively new to applied econometrics but has a long history in social science. See, for example, the chapter-length discussion in Shadish, Cook, and Campbell (2002), the successor to a classic text on research methods by Campbell and Stanley (1963).

{128}------------------------------------------------

SpeciÖcally,

$$\begin{split} E\left[\mathbf{Y}_{i}|\mathbf{Z}_{i}=1\right] - E\left[\mathbf{Y}_{i}|\mathbf{Z}_{i}=0\right] &= E\left[\mathbf{Y}_{i}(\mathbf{D}_{1i},1)|\mathbf{Z}_{i}=1\right] - E\left[\mathbf{Y}_{i}(\mathbf{D}_{0i},0)|\mathbf{Z}_{i}=0\right] \\ &= E\left[\mathbf{Y}_{i}(\mathbf{D}_{1i},1) - \mathbf{Y}_{i}(\mathbf{D}_{0i},0)\right], \end{split}$$

the causal e§ect of the instrument on y<sup>i</sup> . Independence also means that

$$E[D_i|Z_i = 1] - E[D_i|Z_i = 0] = E[D_{1i}|Z_i = 1] - E[D_{0i}|Z_i = 0]$$
  
=  $E[D_{1i} - D_{0i}],$ 

in other words, the Örst-stage from our earlier discussion of 2SLS captures the causal e§ect of z<sup>i</sup> on d<sup>i</sup> :

The second key assumption in the heterogeneous-outcomes framework is the presumption that yi(d; z) is only a function of d. [23](#page-128-0) To be speciÖc, while draft-eligibility clearly a§ects veteran status, an individualís potential earnings as a veteran are assumed to be unchanged by draft-eligibility status; while potential earnings as a nonveteran are similarly una§ected. In general, the claim that an instrument operates through a single known causal channel is called an exclusion restriction. In a linear model with constant e§ects, the exclusion restriction is expressed by the omission of the instrument from the causal equation of interest, or, equivalently, E[zi<sup>i</sup> ] = 0 in equation [\(4.1.14\)](#page-116-1). Itís worth noting that the traditional error-term notation used for simultaneous equations models doesnít lend itself to a clear distinction between independence and exclusion. We need z<sup>i</sup> and <sup>i</sup> to be uncorrelated in this equation, but the reasoning that lies behind this assumption is unclear until we consider both the independence and exclusion restrictions.

The exclusion restriction fails for draft-lottery instruments if men with low draft lottery numbers were a§ected in some way other than through an increased likelihood of service. For example, Angrist and Krueger (1992) looked for an association between draft lottery numbers and schooling. Their idea was that educational draft deferments would have led men with low lottery numbers to stay in college longer than they would have otherwise desired. If so, draft lottery numbers are correlated with earnings for at least two reasons: an increased likelihood of military service and an increased likelihood of college attendance. The fact that the lottery number is randomly assigned (and therefore satisÖes the independence assumption) does not make this possibility less likely. The exclusion restriction is distinct from the claim that the instrument is (as good as) randomly assigned. Rather, it is a claim about a unique channel for causal e§ects of the instrument.[24](#page-128-1)

Using the exclusion restriction, we can deÖne potential outcomes indexed solely against treatment status

<span id="page-128-0"></span><sup>2 3</sup>Hirano, Imbens, Rubin and Zhou (2000) note that the exclusion restriction that yi(d; z) equals yi(d; z<sup>0</sup> ) can be weakened to require only that the distributions of yi(d; z) and yi(d; z<sup>0</sup> ) be the same.

<span id="page-128-1"></span><sup>2 4</sup>As it turns out, there is not much of a relationship between schooling and lottery numbers in the Angrist and Krueger (1992) data, probably because educational deferments were phased out during the lottery period.

{129}------------------------------------------------

using the single-index (y1<sup>i</sup> ;y0<sup>i</sup>) notation we have been using all along. In particular,

$$Y_{1i} \equiv Y_i(1,1) = Y_i(1,0);$$
  
 $Y_{0i} \equiv Y_i(0,1) = Y_i(0,0).$  (4.4.3)

The observed outcome, y<sup>i</sup> , can therefore be written in terms of potential outcomes as:

<span id="page-129-0"></span>
$$Y_{i} = Y_{i}(0, Z_{i}) + [Y_{i}(1, Z_{i}) - Y_{i}(0, Z_{i})]D_{i}$$

$$= Y_{0i} + (Y_{1i} - Y_{0i})D_{i}.$$
(4.4.4)

A random-coe¢ cients notation for this is

$$Y_i = \alpha_0 + \rho_i D_i + \eta_i,$$

a compact version of [\(4.4.4\)](#page-129-0) with <sup>0</sup> E[y0<sup>i</sup> ] and <sup>i</sup> y1<sup>i</sup>y0<sup>i</sup> .

A Önal assumption needed for heterogeneous IV models is that either 1<sup>i</sup> 0 for all i or 1<sup>i</sup> 0 for all i. This monotonicity assumption, introduced by Imbens and Angrist (1994), means that while the instrument may have no e§ect on some people, all of those who are a§ected are a§ected in the same way. In other words, either d1<sup>i</sup> d0<sup>i</sup> or d1<sup>i</sup> d0<sup>i</sup> for all i. In what follows, we assume monotonicity holds with d1<sup>i</sup> d0<sup>i</sup> . In the draft-lottery example, this means that although draft-eligibility may have had no e§ect on the probability of military service for some men, there is no one who was actually kept out of the military by being drafteligible. Without monotonicity, instrumental variables estimators are not guaranteed to estimate a weighted average of the underlying individual causal e§ects, y1<sup>i</sup>y0<sup>i</sup> .

Given the exclusion restriction, the independence of instruments and potential outcomes, the existence of a Örst stage, and monotonicity, the Wald estimand can be interpreted as the e§ect of veteran status on those whose treatment status can be changed by the instrument. This parameter is called the local average treatment e§ect ((LATE); Imbens and Angrist, 1994). Here is a formal statement:

#### Theorem 4.4.1 THE LATE THEOREM. Suppose

- (A1, Independence) fyi(d1<sup>i</sup> ; 1);y0<sup>i</sup>(d0<sup>i</sup> ; 0);d1<sup>i</sup> ;d0<sup>i</sup>gqzi;
- (A2, Exclusion) yi(d; 0) =yi(d; 1) ydi for d = 0; 1;
- (A3, First-stage), E[d1<sup>i</sup>d0<sup>i</sup> ] 6= 0
- (A4, Monotonicity) d1<sup>i</sup>d0<sup>i</sup> 08i, or vice versa;

Then

$$\frac{E[\mathbf{Y}_i|\mathbf{Z}_i=1] - E[\mathbf{Y}_i|\mathbf{Z}_i=0]}{E[\mathbf{D}_i|\mathbf{Z}_i=1] - E[\mathbf{D}_i|\mathbf{Z}_i=0]} = E[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{D}_{1i} > \mathbf{D}_{0i}] = E[\rho_i|\pi_{1i} > 0].$$

Proof. Use the exclusion restriction to write E[y<sup>i</sup> jz<sup>i</sup> = 1] = E[y0<sup>i</sup> + (y1<sup>i</sup>y0<sup>i</sup>)d<sup>i</sup> jz<sup>i</sup> = 1], which equals 

{130}------------------------------------------------

E[y0<sup>i</sup> + (y1<sup>i</sup>y0<sup>i</sup>)d1<sup>i</sup> ] by independence. Likewise E[y<sup>i</sup> jz<sup>i</sup> = 0] = E[y0<sup>i</sup> + (y1<sup>i</sup>y0<sup>i</sup>)d0<sup>i</sup> ], so the numerator of the Wald estimator is E[(y1<sup>i</sup>y0<sup>i</sup>)(d1<sup>i</sup>d0<sup>i</sup>)]. Monotonicity means d1<sup>i</sup>d0<sup>i</sup> equals one or zero, so

$$E[(Y_{1i} - Y_{0i})(D_{1i} - D_{0i})] = E[Y_{1i} - Y_{0i}|D_{1i} > D_{0i}]P[D_{1i} > D_{0i}].$$

A similar argument shows

$$E[D_i|Z_i = 1] - E[D_i|Z_i = 0] = E[D_{1i} - D_{0i}] = P[D_{1i} > D_{0i}].$$

This theorem says that an instrument which is as good as randomly assigned, a§ects the outcome through a single known channel, has a Örst-stage, and a§ects the causal channel of interest only in one direction, can be used to estimate the average causal e§ect on the a§ected group. Thus, IV estimates of e§ects of military service using the draft lottery estimate the e§ect of military service on men who served because they were draft-eligible, but would not otherwise have served. This obviously excludes volunteers and men who were exempted from military service for medical reasons, but it includes men for whom draft policy was binding.

How useful is LATE? No theorem answers this question, but itís always worth discussing. Part of the interest in the e§ects of Vietnam-era service revolves around the question of whether veterans (especially, conscripts) were adequately compensated for their service. Internally valid draft lottery estimates answer this question. Draft lottery estimates of the e§ects of Vietnam-era conscription may also be relevant for discussions of any future conscription policy. On the other hand, while draft lottery instruments produce internally valid estimates of the causal e§ect of Vietnam-era conscription, the external validity - i.e., the predictive value of these estimates for military service in other times and places - is not directly addressed by the IV framework. There is nothing in IV formulas to explain why Vietnam-era service a§ects earnings; for that, you need a theory.[25](#page-130-0)

You might wonder why we need monotonicity for the LATE theorem, an assumption that plays no role in the traditional simultaneous-equations framework with constant e§ects. A failure of monotonicity means the instrument pushes some people into treatment while pushing others out. Angrist, Imbens, and Rubin (1996) call the latter group deÖers. DeÖers complicate the link between LATE and the reduced form. To see why, go back to the step in the proof of the LATE theorem which shows the reduced form is

$$E[Y_i|Z_i = 1] - E[Y_i|Z_i = 0] = E[(Y_{1i} - Y_{0i})(D_{1i} - D_{0i})].$$

<span id="page-130-0"></span><sup>2 5</sup>Angrist (1990) interprets draft lottery estimates as the penalty for lost labor market experience. This suggests draft lottery estimates should have external validity for the e§ects of conscription in other periods, a conjecture born out by the results for WWII draftees in Angrist and Krueger (1994).

{131}------------------------------------------------

Without monotonicity, this is equal to

$$E[Y_{1i} - Y_{0i}|D_{1i} > D_{0i}]P[D_{1i} > D_{0i}] - E[Y_{1i} - Y_{0i}|D_{1i} < D_{0i}]P[D_{1i} < D_{0i}].$$

We might therefore have a scenario where treatment e§ects are positive for everyone yet the reduced form is zero because e§ects on compliers are canceled out by e§ects on deÖers. This doesnít come up in a constant-e§ects model because the reduced form is always the constant e§ect times the Örst stage regardless of whether the Örst stage includes deÖant behavior.[26](#page-131-0)

A deeper understanding of LATE can be had by linking it to a workhorse of contemporary econometrics, the latent-index model for "dummy endogenous variables" like assignment to treatment. These models describe individual choices as determined by a comparison of partly observed and partly unknown (ìlatentî) utilities and costs (see, e.g., Heckman, 1978). Typically, these unobservables are thought of as being related to outcomes, in which case the treatment variable is said to be endogenous (though it is not really endogenous in a simultanenous-equations sense). For example (ignoring covariates), we might model veteran status as

$$\mathbf{D}_i = \left\{ \begin{array}{ll} 1 & \text{if } \gamma_0 + \gamma_1 \mathbf{Z}_i > v_i \\ \\ 0 & \text{otherwise} \end{array} \right.,$$

where v<sup>i</sup> is a random factor involving unobserved costs and beneÖts of military service assumed to be independent of z<sup>i</sup> . This latent-index model characterizes potential treatment assignments as:

$$D_{0i} = 1[\gamma_0 > v_i]$$
 and  $D_{1i} = 1[\gamma_0 + \gamma_1 > v_i]$ .

Note that in this model, monotonicity is automatically satisÖed since <sup>1</sup> is a constant. Assuming <sup>1</sup> > 0, LATE can be written

$$E[Y_{1i} - Y_{0i}|D_{1i} > D_{0i}] = E[Y_{1i} - Y_{0i}|\gamma_0 + \gamma_1 > v_i > \gamma_0],$$

which is a function of the latent Örst-stage parameters, <sup>0</sup> and <sup>1</sup> , as well as the joint distribution of y1<sup>i</sup>y0<sup>i</sup> and v<sup>i</sup> . This is not, in general, the same as the population average treatment e§ect, E[y1<sup>i</sup>y0<sup>i</sup> ], or the

$$\begin{split} E[\mathbf{Y}_{1i} - \mathbf{Y}_{0i} | \mathbf{D}_{1i} &> \mathbf{D}_{0i}] P[\mathbf{D}_{1i} > \mathbf{D}_{0i}] \\ -E[\mathbf{Y}_{1i} - \mathbf{Y}_{0i} | \mathbf{D}_{1i} &< \mathbf{D}_{0i}] P[\mathbf{D}_{1i} < \mathbf{D}_{0i}]. \\ &= \rho \{ P[\mathbf{D}_{1i} > \mathbf{D}_{0i}] - P[\mathbf{D}_{1i} < \mathbf{D}_{0i}] \} \\ &= \rho \{ E[\mathbf{D}_{1i} - \mathbf{D}_{0i}] \}. \end{split}$$

So a zero reduced form e§ect means either the Örst stage is zero or = 0.

<span id="page-131-0"></span><sup>2 6</sup>With a constant e§ect, ;

{132}------------------------------------------------

effect on the treated,  $E[Y_{1i}-Y_{0i}|D_i=1]$ . We explore the distinction between different average causal effects in Section 4.4.2.

#### <span id="page-132-0"></span>4.4.2 The Compliant Subpopulation

The LATE framework partitions any population with an instrument into a set of three instrument-dependent subgroups, defined by the manner in which members of the population react to the instrument:

**Definition 4.4.1** Compliers. The subpopulation with  $D_{1i} = 1$  and  $D_{0i} = 0$ .

Always-takers. The subpopulation with  $D_{1i} = D_{0i} = 1$ .

Never-takers. The subpopulation with  $D_{1i} = D_{0i} = 0$ .

LATE is the effect of treatment on the population of compliers. The term "compliers" comes from an analogy with randomized trials where some experimental subjects comply with the randomly assigned treatment protocol (e.g., take their medicine) but some do not, while some control subjects obtain access to the experimental treatment even though they were not supposed to. Those who don't take their medicine when randomly assigned to do so are never-takers while those who take the medicine even when put into the control group are always-takers. Without adding further assumptions (e.g., constant causal effects), LATE is not informative about effects on never-takers and always-takers because, by definition, treatment status for these two groups is unchanged by the instrument (random assignment). The analogy between IV and a randomized trial with partial compliance is more than allegorical - IV solves the problem of causal inference in a randomized trial with partial compliance. This important point merits a separate subsection, below.

Before turning to this important special case, we make a few general points. First, the average causal effect on compliers is not usually the same as the average treatment effect on the treated. From the simple fact that  $D_i = D_{0i} + (D_{1i} - D_{0i})Z_i$ , we learn that the treated population consists of two non-overlapping groups. By monotonicity, we cannot have both  $D_{0i} = 1$  and  $D_{1i} - D_{0i} = 1$  since  $D_{0i} = 1$  implies  $D_{1i} = 1$ . The treated therefore have either  $D_{0i} = 1$  or  $D_{1i} - D_{0i} = 1$  and  $Z_i = 1$ , and hence  $D_i$  can be written as the sum of two mutually-exclusive dummies,  $D_{i0}$  and  $(D_{1i} - D_{0i})Z_i$ . The treated consist of either always-takers or compliers with the instrument switched on. Since the instrument is as good as randomly assigned, compliers with the instrument switched on are representative of all compliers. From here we get

<span id="page-132-1"></span>
$$E[Y_{1i} - Y_{0i}|D_{i} = 1]$$
effect on the treated
$$= E[Y_{1i} - Y_{0i}|D_{0i} = 1]P[D_{0i} = 1|D_{i} = 1]$$

$$+ E[Y_{1i} - Y_{0i}|D_{1i} > D_{0i}, Z_{i} = 1]P[D_{1i} > D_{0i}, Z_{i} = 1|D_{i} = 1]$$

$$= \underbrace{E[Y_{1i} - Y_{0i}|D_{0i} = 1]P[D_{0i} = 1|D_{i} = 1]}_{\text{effect on always-takers}}$$

$$+ \underbrace{E[Y_{1i} - Y_{0i}|D_{1i} > D_{0i}]P[D_{1i} > D_{0i}, Z_{i} = 1|D_{i} = 1]}_{\text{effect on compliers}}$$
(4.4.5)

{133}------------------------------------------------

Since  $P[D_{0i} = 1|D_i = 1]$  and  $P[D_{1i} > D_{0i}, Z_i = 1|D_i = 1]$  add up to one, this means that the effect of treatment on the treated is a weighted average of effects on always-takers and compliers.

Likewise, LATE is not the average causal effect of treatment on the non-treated,  $E[Y_{1i}-Y_{0i}|D_i=0]$ . In the draft-lottery example, the average effect on the non-treated is the average causal effect of military service on the population of non-veterans from the Vietnam-era cohorts. The average effect of treatment on the non-treated is a weighted average of effects on never-takers and compliers. In particular,

<span id="page-133-0"></span>
$$E\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{D}_{i} = 0\right]$$
effect on the non-treated
$$= \underbrace{E\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{D}_{1i} = 0\right]}_{\text{effect on never-takers}} P\left[\mathbf{D}_{1i} = 0|\mathbf{D}_{i} = 0\right]$$

$$+ \underbrace{E\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{D}_{1i} > \mathbf{D}_{0i}\right]}_{\text{effect on compliers}} P\left[\mathbf{D}_{1i} > \mathbf{D}_{0i}, \mathbf{Z}_{i} = 0|\mathbf{D}_{i} = 0\right],$$

$$\underbrace{\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{D}_{1i} > \mathbf{D}_{0i}\right]}_{\text{effect on compliers}} P\left[\mathbf{D}_{1i} > \mathbf{D}_{0i}, \mathbf{Z}_{i} = 0|\mathbf{D}_{i} = 0\right],$$

where we use the fact that, by monotonicity, those with  $D_{1i} = 0$  must be never-takers.

Finally, averaging (4.4.5) and (4.4.6) using

$$E[Y_{1i} - Y_{0i}] = E[Y_{1i} - Y_{0i}|D_i = 1]P[D_i = 1] + E[Y_{1i} - Y_{0i}|D_i = 0]P[D_i = 0]$$

shows the overall population average treatment effect to be a weighted average of effects on compliers, alwaystakers, and never-takers. Of course, this is a conclusion we could have reached directly given monotonicity and the definition at the beginning of this subsection.

Because an instrumental variable is not directly informative about effects on always-takers and nevertakers, instruments do not usually capture the average causal effect on all of the treated or on all of the non-treated. There are important exceptions to this rule, however: instrumental variables that allow no always-takers or no never-takers. Although this scenario is not typical, it is an important special case. One example is the twins instrument for fertility, used by Rosenzweig and Wolpin (1980), Bronars and Grogger (1994), Angrist and Evans (1998), and Angrist, Lavy, and Schlosser (2006). Another is Oreopoulos' (2006) recent study using changes in compulsory attendance laws as instruments for schooling in Britain.

To see how this special case works with twins instruments, let  $T_i$  be a dummy variable indicating multiple second births. Angrist and Evans (1998) used this instrument to estimate the causal effect of having three children on earnings in the population of women with at least two children. The third child is especially interesting because reduced fertility for American wives in the 1960s and 1970s meant a switch from three children to two. Multiple second births provide quasi-experimental variation on this margin. Let  $Y_{0i}$  denote potential earnings if a woman has only two children while  $Y_{1i}$  denotes her potential earnings if she has three, an event indicated by  $D_i$ . Assuming that  $T_i$  is randomly assigned, i.e., that fertility increases by at most one child in response to a multiple birth, and that multiple births affect outcomes only by increasing fertility,

{134}------------------------------------------------

LATE using the twins instrument, t<sup>i</sup> , is also E[y1<sup>i</sup>y0<sup>i</sup> jd<sup>i</sup> = 0], the average causal e§ect on women who are not treated (i.e., have two children only). This is because all women who have a multiple second birth end up with three children, i.e., there are no never-takers in response to the twins instrument.

Oreopoulos (2006) also uses IV to estimate an average causal e§ect of treatment on the non-treated. His study estimates the economic returns to schooling using an increase in the British compulsory attendance age from 14 to 15. Compliance with the Britainís new compulsory attendance law was near perfect, though many teens would previously have dropped out of school at age 14. The causal e§ect of interest in this case is the earnings premium for an additional year of high-school. Finishing this year can be thought of as the treatment. Since everybody in Oreopoulosí British sample Önishes the additional year when compulsory schooling laws are made stricter, OreopoulosíIV strategy captures the average causal e§ect of obtaining one more year of high school on all those who leave school at 14. This turns on the fact that British teens are remarkably law-abiding people - Oreopoulosí IV strategy wouldnít estimate the e§ect of treatment on the non-treated in, say, Israel, where teenagers get more leeway when it comes to compulsory school attendance. Israeli econometricians using changes in compulsory attendance laws as instruments must therefore make do with LATE.