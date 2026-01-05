# Theorem 4.5.3 AVERAGE CAUSAL RESPONSE. Suppose

> Pages: 151-153

<span id="page-151-0"></span><sup>3 4</sup>Abadie (2003) gives formulas for standard errors and Alberto Abadie has posted software to compute them. The bootstrap provides a simple alternative, which we used to construct standard errors for the Abadie estimates mentioned in this paragraph.

{152}------------------------------------------------

(ACR1, Independence and Exclusion)  $\{Y_{0i}, Y_{1i}, ..., Y_{\bar{s}i}; s_{0i}, s_{1i}\}\coprod z_i$ 

 $(ACR2, First-stage), E[s_{1i} - s_{0i}] \neq 0$ 

(ACR3, Monotonicity)  $s_{1i} - s_{0i} \ge 0 \forall i$ , or vice versa; assume the first

Then

$$\frac{E[\mathbf{Y}_i|\mathbf{Z}_i=1] - E[\mathbf{Y}_i|\mathbf{Z}_i=0]}{E[\mathbf{S}_i|\mathbf{Z}_i=1] - E[\mathbf{S}_i|\mathbf{Z}_i=0]} = \sum_{s=1}^{\bar{s}} \omega_s E[Y_{si} - Y_{s-1,i}|s_{1i} \ge s > s_{0i}]$$

where

$$\omega_s = \frac{P[s_{1i} \ge s > s_{0i}]}{\sum_{j=1}^{\bar{s}} P[s_{1i} \ge j > s_{0i}]}$$

The weights  $\omega_s$  are non-negative and sum to one.

The average causal response (ACR) theorem says that the Wald estimator with variable treatment intensity is a weighted average of the unit causal response along the length of the potentially nonlinear causal relation described by  $f_i(s)$ . The unit causal response,  $E[Y_{si} - Y_{s-1,i}|s_{1i} \ge s > s_{0i}]$ , is the average difference in potential outcomes for compliers at point s, i.e., individuals driven by the instrument from a treatment intensity less than s to at least s. For example, the quarter of birth instruments used by Angrist and Krueger (1991) push some people from  $11^{th}$  grade to finishing  $12^{th}$  or higher, and others from  $10^{th}$  grade to finishing  $11^{th}$  or higher. The Wald estimator using quarter of birth instruments combines all of these effects into a single average causal response.

The relative size of the group of compliers at point s is  $P[s_{1i} \ge s > s_{0i}]$ . By monotonicity, this must be non-negative and is given by the difference in the CDF of  $s_i$  at point s. To see this, note that

$$P[s_{1i} \ge s > s_{0i}] = P[s_{1i} \ge s] - P[s_{0i} \ge s]$$
  
=  $P[s_{0i} < s] - P[s_{1i} < s]$ ,

which is non-negative since monotonicity requires  $s_{1i} \geq s_{0i}$ . Moreover,

$$P[s_{0i} < s] - P[s_{1i} < s] = P[s_i < s | z_i = 0] - P[s_i < s | z_i = 1]$$

by Independence. Finally, note that because the mean of a non-negative random variable is one minus the CDF, we have,

$$E[\mathbf{s}_{i}|\mathbf{z}_{i} = 1] - E[\mathbf{s}_{i}|\mathbf{z}_{i} = 0]$$

$$= \sum_{j=1}^{\bar{s}} (P[\mathbf{s}_{i} < j|\mathbf{z}_{i} = 1] - P[\mathbf{s}_{i} < j|\mathbf{z}_{i} = 0]) = \sum_{j=1}^{\bar{s}} P[s_{1i} \ge j > s_{0i}]$$

Thus, the ACR weighting function can be consistently estimated by comparing the CDFs of the endogenous variables (treatment intensity) with the instrument switched off and on. The weighting function is normalized

{153}------------------------------------------------

by the Örst-stage.

The ACR theorem helps us understand what we are learning from a 2SLS estimate. For example, instrumental variables derived from compulsory attendance and child labor laws capture the causal e§ect of increases in schooling in the 6-12 grade range, but not from post-secondary schooling. This is illustrated in Figure [4.5.1,](#page-103-0) taken from Acemoglu and Angrist (2000).

The Ögure plots di§erences in the probability that educational attainment is at or exceeds the grade level on the X-axis (i.e., one minus the CDF). The di§erences are between men exposed to di§erent child labor laws and compulsory schooling laws in the a sample of white men aged 40-49 drawn from the 1960, 1970, and 1980 censuses. The instruments are coded as the number of years of schooling required either to work (Panel A) or leave school (Panel B) in the year the respondent was aged 14. Men exposed to the least restrictive laws are the reference group. Each instrument (e.g., a dummy for 7 years of schooling required before work is allowed) can be used to construct a Wald estimator by making comparisons with the reference group.

Panel A of Figure [4.5.1](#page-103-0) shows that men exposed to more restrictive child labor laws were 1-6 percentage points more likely to complete grades 8-12. The intensity of the shift depends on whether the laws required 7, 8, or 9-plus years of schooling before work was allowed. But in all cases, the CDF di§erences decline at lower grades, and drop o§ sharply after grade 12. Panel B shows a similar pattern for compulsory attendance laws, though the e§ects are a little smaller and the action here is at somewhat higher grades, consistent with the fact that compulsory attendance laws are typically binding in higher grades than child labor laws.

Before wrapping up our discussion of LATE generalizations, itís worth noting that most of the elements we have covered work in combination. For example, models with multiple instruments and variable treatment intensity generate a weighted average of the ACR for each instrument. Likewise, the saturate and weight theorem applies to models with variable treatment intensity. On the other hand, we do not yet have an extension of Abadieís Kappa for models with variable treatment intensity. A Önal important extension is to the scenario where the causal variable of interest is continuous and we can therefore think of the causal response function as having derivatives.