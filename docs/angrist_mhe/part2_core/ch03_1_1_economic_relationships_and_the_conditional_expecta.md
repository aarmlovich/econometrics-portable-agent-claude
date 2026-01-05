# Economic Relationships and the Conditional Expectation Function

> Pages: 38-41

Empirical economic research in our Öeld of Labor Economics is typically concerned with the statistical analysis of individual economic circumstances, and especially di§erences between people that might account for di§erences in their economic fortunes. Such di§erences in economic fortune are notoriously hard to explain; they are, in a word, random. As applied econometricians, however, we believe we can summarize and interpret randomness in a useful way. An example of ìsystematic randomnessîmentioned in the introduction is the connection between education and earnings. On average, people with more schooling earn more than people with less schooling. The connection between schooling and average earnings has considerable predictive power, in spite of the enormous variation in individual circumstances that sometimes clouds this fact. Of course, the fact that more educated people earn more than less educated people does not mean that schooling causes earnings to increase. The question of whether the earnings-schooling relationship is causal is of enormous importance, and we will come back to it many times. Even without resolving the di¢ cult question of causality, however, itís clear that education predicts earnings in a narrow statistical sense. This predictive power is compellingly summarized by the conditional expectation function (CEF).

The CEF for a dependent variable, y<sup>i</sup> given a k-1 vector of covariates, X<sup>i</sup> (with elements xki) is the expectation, or population average of y<sup>i</sup> with X<sup>i</sup> held Öxed. The population average can be thought of as the mean in an inÖnitely large sample, or the average in a completely enumerated Önite population. The CEF is written E [y<sup>i</sup> jX<sup>i</sup> ] and is a function of X<sup>i</sup> . Because X<sup>i</sup> is random, the CEF is random, though sometimes we work with a particular value of the CEF, say E[y<sup>i</sup> jXi=42], assuming 42 is a possible value for X<sup>i</sup> . In Chapter [2,](#page-24-1) we brieáy considered the CEF E[y<sup>i</sup> jdi ], where d<sup>i</sup> is a zero-one variable. This CEF takes on two values, E[y<sup>i</sup> jd<sup>i</sup> = 1] and E[y<sup>i</sup> jd<sup>i</sup> = 0]: Although this special case is important, we are most often interested in CEFs that are functions of many variables, conveniently subsumed in the vector, X<sup>i</sup> : For a speciÖc value of X<sup>i</sup> , say X<sup>i</sup> = x, we write E [y<sup>i</sup> jX<sup>i</sup> = x]. For continuous y<sup>i</sup> with conditional density f<sup>y</sup> (jX<sup>i</sup> = x), the CEF is

$$E\left[\mathbf{Y}_{i}|\mathbf{X}_{i}=x\right] = \int t f_{y}\left(t|\mathbf{X}_{i}=x\right) dt.$$

If y<sup>i</sup> is discrete, E [y<sup>i</sup> <sup>j</sup>X<sup>i</sup> <sup>=</sup> <sup>x</sup>] equals the sum <sup>P</sup> t tf<sup>y</sup> (tjX<sup>i</sup> = x).

Expectation is a population concept. In practice, data usually come in the form of samples and rarely consist of an entire population. We therefore use samples to make inferences about the population. For example, the sample CEF is used to learn about the population CEF. This is always necessary but we postpone a discussion of the formal inference step taking us from sample to population until Section [3.1.3.](#page-45-0) Our ìpopulation Örstîapproach to econometrics is motivated by the fact that we must deÖne the objects of

{39}------------------------------------------------

interest before we can use data to study them.[1](#page-39-0)

Figure [3.1.1](#page-39-1) plots the CEF of log weekly wages given schooling for a sample of middle-aged white men from the 1980 Census. The distribution of earnings is also plotted for a few key values: 4, 8, 12, and 16 years of schooling. The CEF in the Ögure captures the fact tható the enormous variation individual circumstances notwithstandingó people with more schooling generally earn more, on average. The average earnings gain associated with a year of schooling is typically about 10 percent.

![](_page_39_Figure_4.jpeg)

<span id="page-39-1"></span>Figure 3.1.1: Raw data and the CEF of average log weekly wages given schooling. The sample includes white men aged 40-49 in the 1980 IPUMS 5 percent Öle.

An important complement to the CEF is the law of iterated expectations. This law says that an unconditional expectation can be written as the population average of the CEF. In other words

$$E[\mathbf{Y}_i] = E\{E[\mathbf{Y}_i|\mathbf{X}_i]\},\tag{3.1.1}$$

where the outer expectation uses the distribution of X<sup>i</sup> . Here is proof of the law of iterated expectations for continuously distributed (X<sup>i</sup> ; yi) with joint density fxy (u; t), where f<sup>y</sup> (tjX<sup>i</sup> = x) is the conditional

<span id="page-39-0"></span><sup>1</sup>Examples of pedagogical writing using the ìpopulation-Örstî approach to econometrics include Chamberlain (1984), Goldberger (1991), and Manski (1991).

{40}------------------------------------------------

distribution of y<sup>i</sup> given X<sup>i</sup> = x and gy(t) and gx(u) are the marginal densities:

$$\begin{split} E\{E\left[\mathbf{Y}_{i}|\mathbf{X}_{i}\right]\} &= \int E\left[\mathbf{Y}_{i}|\mathbf{X}_{i}=u\right]g_{x}(u)du \\ &= \int \left[\int tf_{y}\left(t|\mathbf{X}_{i}=u\right)dt\right]g_{x}(u)du \\ &= \int \int tf_{y}\left(t|\mathbf{X}_{i}=u\right)g_{x}(u)dudt \\ &= \int t\left[\int f_{y}\left(t|\mathbf{X}_{i}=u\right)g_{x}(u)du\right]dt = \int t\left[\int f_{xy}\left(u,t\right)du\right]dt \\ &= \int tg_{y}(t)dt. \end{split}$$

The integrals in this derivation run over the possible values of X<sup>i</sup> and y<sup>i</sup> (indexed by u and t). Weíve laid out these steps because the CEF and its properties are central to the rest of this chapter.

The power of the law of iterated expectations comes from the way it breaks a random variable into two pieces.

#### Theorem 3.1.1 The CEF-Decomposition Property

$$\mathbf{Y}_i = E\left[\mathbf{Y}_i | \mathbf{X}_i\right] + \varepsilon_i,$$

where (i) "<sup>i</sup> is mean-independent of Xi, i.e., E["<sup>i</sup> jX<sup>i</sup> ] = 0;and, therefore, (ii) "<sup>i</sup> is uncorrelated with any function of Xi.

Proof. (i) E["<sup>i</sup> jX<sup>i</sup> ] = E[y<sup>i</sup> E [y<sup>i</sup> jX<sup>i</sup> ] j X<sup>i</sup> ] = E [y<sup>i</sup> jX<sup>i</sup> ] E [y<sup>i</sup> jX<sup>i</sup> ] = 0;(ii) This follows from (i): Let h(Xi) be any function of X<sup>i</sup> . By the law of iterated expectations, E[h(Xi)"<sup>i</sup> ] = Efh(Xi)E["<sup>i</sup> jX<sup>i</sup> ]g and by mean-independence, E["<sup>i</sup> jX<sup>i</sup> ] = 0:

This theorem says that any random variable, y<sup>i</sup> , can be decomposed into a piece thatís ìexplained by Xiî, i.e., the CEF, and a piece left over which is orthogonal to (i.e., uncorrelated with) any function of X<sup>i</sup> .

The CEF is a good summary of the relationship between y<sup>i</sup> and X<sup>i</sup> for a number of reasons. First, we are used to thinking of averages as providing a representative value for a random variable. More formally, the CEF is the best predictor of y<sup>i</sup> given X<sup>i</sup> in the sense that it solves a Minimum Mean Squared Error (MMSE) prediction problem. This CEF-prediction property is a consequence of the CEF-decomposition property:

#### Theorem 3.1.2 The CEF-Prediction Property.

Let m (Xi) be any function of Xi. The CEF solves

$$E\left[\mathbf{Y}_{i} \middle| \mathbf{X}_{i}\right] = \underset{m\left(\mathbf{X}_{i}\right)}{\arg\min} E\left[\left(\mathbf{Y}_{i} - m\left(\mathbf{X}_{i}\right)\right)^{2}\right],$$

so it is the MMSE predictor of y<sup>i</sup> given X<sup>i</sup> :


{41}------------------------------------------------

Proof. Write

$$\begin{split} \left( {{{\bf{Y}}_i} - m\left( {{{\bf{X}}_i}} \right)} \right)^2 &= & \left( {{{\left( {{{\bf{Y}}_i} - E\left[ {{{\bf{Y}}_i}|{{\bf{X}}_i}} \right] + \left( {E\left[ {{{\bf{Y}}_i}|{{\bf{X}}_i}} \right] - m\left( {{{\bf{X}}_i}} \right)} \right)} \right)^2} \\ &= & \left( {{{\bf{Y}}_i} - E\left[ {{{\bf{Y}}_i}|{{\bf{X}}_i}} \right]} \right)^2 + 2\left( {E\left[ {{{\bf{Y}}_i}|{{\bf{X}}_i}} \right] - m\left( {{{\bf{X}}_i}} \right)} \right)\left( {{{\bf{Y}}_i} - E\left[ {{{\bf{Y}}_i}|{{\bf{X}}_i}} \right]} \right) \\ &+ \left( {E\left[ {{{\bf{Y}}_i}|{{\bf{X}}_i}} \right] - m\left( {{{\bf{X}}_i}} \right)} \right)^2} \end{split}$$

The Örst term doesnít matter because it doesnít involve m (Xi). The second term can be written h(Xi)"<sup>i</sup> , where h(Xi) 2 (E [y<sup>i</sup> jX<sup>i</sup> ] m (Xi)), and therefore has expectation zero by the CEF-decomposition property. The last term is minimized at zero when m (Xi) is the CEF.

A Önal property of the CEF, closely related to both the CEF decomposition and prediction properties, is the Analysis-of-Variance (ANOVA) Theorem:

Theorem 3.1.3 The ANOVA Theorem

$$V\left(\mathbf{Y}_{i}\right) = V\left(E\left[\mathbf{Y}_{i} \middle| \mathbf{X}_{i}\right]\right) + E\left[V\left(\mathbf{Y}_{i} \middle| \mathbf{X}_{i}\right)\right]$$

where V () denotes variance and V (y<sup>i</sup> jXi) is the conditional variance of y<sup>i</sup> given X<sup>i</sup> :

Proof. The CEF-decomposition property implies the variance of y<sup>i</sup> is the variance of the CEF plus the variance of the residual, "<sup>i</sup> y<sup>i</sup> E [y<sup>i</sup> jX<sup>i</sup> ] since "<sup>i</sup> and E [y<sup>i</sup> jX<sup>i</sup> ] are uncorrelated. The variance of "<sup>i</sup> is

$$E\left[\varepsilon_{i}^{2}\right] = E\left[E\left[\varepsilon_{i}^{2}|\mathbf{X}_{i}\right]\right] = E\left[V\left[\mathbf{Y}_{i}|\mathbf{X}_{i}\right]\right]$$

where 
$$E\left[\varepsilon_i^2|\mathbf{X}_i\right] = V\left[\mathbf{Y}_i|\mathbf{X}_i\right]$$
 because  $\varepsilon_i \equiv \mathbf{Y}_i - E\left[\mathbf{Y}_i|\mathbf{X}_i\right]$ .

The two CEF properties and the ANOVA theorem may have a familiar ring. You might be used to seeing an ANOVA table in your regression output, for example. ANOVA is also important in research on inequality where labor economists decompose changes in the income distribution into parts that can be accounted for by changes in worker characteristics and changes in whatís left over after accounting for these factors (See, e.g., Autor, Katz, and Kearney, 2005). What may be unfamiliar is the fact that the CEF properties and ANOVA variance decomposition work in the population as well as in samples, and do not turn on the assumption of a linear CEF. In fact, the validity of linear regression as an empirical tool does not turn on linearity either.