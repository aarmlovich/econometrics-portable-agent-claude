# Standard Stratified Sampling and Variable Probability Sampling

> Pages: 598-600

The two most common kinds of stratification used in obtaining data sets in the social sciences are standard stratified sampling (SS sampling) and variable probability sam

{599}------------------------------------------------

pling (VP sampling). In SS sampling, the population is first partitioned into J groups, W1;W2; ... ;W<sup>J</sup> , which we assume are nonoverlapping and exhaustive. We let w denote the random variable representing the population of interest.

standard stratified sampling: For j ¼ 1; ... ; J, draw a random sample of size Nj from stratum j. For each j, denote this random sample by fwij: i ¼ 1; 2; ... ; Njg.

The strata sample sizes Nj are nonrandom. Therefore, the total sample size, N ¼ N<sup>1</sup> þ--þ NJ , is also nonrandom. A randomly drawn observation from stratum j; wij, has distribution Dðwj w A WjÞ. Therefore, while observations within a stratum are identically distributed, observations across strata are not. A scheme that is similar in nature to SS sampling is called multinomial sampling, where a stratum is first picked at random and then an observation is randomly drawn from the stratum. This does result in i.i.d. observations, but it does not correspond to how stratified samples are obtained in practice. It also leads to the same estimators as under SS sampling, so we do not discuss it further; see Cosslett (1993) or Wooldridge (1999b) for further discussion.

Variable probability samples are obtained using a different scheme. First, an observation is drawn at random from the population. If the observation falls into stratum j, it is kept with probability pj. Thus, random draws from the population are discarded with varying frequencies depending on which stratum they fall into. This kind of sampling is appropriate when information on the variable or variables that determine the strata is relatively easy to obtain compared with the rest of the information. Survey data sets, including initial interviews to collect panel or longitudinal data, are good examples. Suppose we want to oversample individuals from, say, lower income classes. We can first ask an individual her or his income. If the response is in income class j, this person is kept in the sample with probability pj, and then the remaining information, such as education, work history, family background, and so on can be collected; otherwise, the person is dropped without further interviewing.

A key feature of VP sampling is that observations within a stratum are discarded randomly. As discussed by Wooldridge (1999b), VP sampling is equivalent to the following:

variable probability sampling: Repeat the following steps N times:

- 1. Draw an observation w<sup>i</sup> at random from the population.
- 2. If w<sup>i</sup> is in stratum j, toss a (biased) coin with probability pj of turning up heads. Let hij ¼ 1 if the coin turns up heads and zero otherwise.
- 3. Keep observation i if hij ¼ 1; otherwise, omit it from the sample.

{600}------------------------------------------------

The number of observations falling into stratum j is denoted Nj, and the number of data points we actually have for estimation is N<sup>0</sup> ¼ N<sup>1</sup> þ N<sup>2</sup> þ--þ NJ . Notice that if N—the number of times the population is sampled—is fixed, then N<sup>0</sup> is a random variable: we do not know what each Nj will be prior to sampling. Also, we will not use information on the number of discarded observations in each stratum, so that N is not required to be known.

The assumption that the probability of the coin turning up heads in step 2 depends only on the stratum ensures that sampling is random within each stratum. This roughly reflects how samples are obtained for certain large cross-sectional and panel data sets used in economics, including the panel study of income dynamics and the national longitudinal survey.

To see that a VP sample can be analyzed as a random sample, we construct a population that incorporates the stratification. The VP sampling scheme is equivalent to first tossing all J coins before actually observing which stratum w<sup>i</sup> falls into; this gives ðhi1; ... ; hiJ Þ. Next, w<sup>i</sup> is observed to fall into one of the strata. Finally, the outcome is kept or not depending on the coin flip for that stratum. The result is that the vector ðwi; hiÞ, where h<sup>i</sup> is the J-vector of binary indicators hij, is a random sample from a new population with sample space W H, where W is the original sample space and H denotes the sample space associated with outcomes from flipping J coins. Under this alternative way of viewing the sampling scheme, h<sup>i</sup> is independent of wi. Treating ðwi; hiÞ as a random draw from the new population is not at odds with the fact that our estimators are based on a nonrandom sample from the original population: we simply use the vector h<sup>i</sup> to determine which observations are kept in the estimation procedure.