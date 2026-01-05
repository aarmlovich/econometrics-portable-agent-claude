# The Selection Problem

> Pages: 25-27

We take a brief time-out for a more formal discussion of the role experiments play in uncovering causal e§ects. Suppose you are interested in a causal ìif-thenî question. To be concrete, consider a simple example: Do hospitals make people healthier? For our purposes, this question is allegorical, but it is surprisingly close to the sort of causal question health economists care about. To make this question more realistic, imagine weíre studying a poor elderly population that uses hospital emergency rooms for primary care. Some of these patients are admitted to the hospital. This sort of care is expensive, crowds hospital facilities, and is, perhaps, not very e§ective (see, e.g., Grumbach, Keane, and Bindman, 1993). In fact, exposure to other sick patients by those who are themselves vulnerable might have a net negative impact on their health.

Since those admitted to the hospital get many valuable services, the answer to the hospital-e§ectiveness question still seems likely to be "yes". But will the data back this up? The natural approach for an empirically-minded person is to compare the health status of those who have been to the hospital to the health of those who have not. The National Health Interview Survey (NHIS) contains the information needed to make this comparison. SpeciÖcally, it includes a question ìDuring the past 12 months, was the respondent a patient in a hospital overnight?î which we can use to identify recent hospital visitors. The NHIS also asks ìWould you say your health in general is excellent, very good, good, fair, poor?î The following table displays the mean health status (assigning a 1 to excellent health and a 5 to poor health) among those who have been hospitalized and those who have not (tabulated from the 2005 NHIS):

<table><tbody><tr><th>Group</th><th>Sample Size</th><th>Mean health status</th><th>Std. Error</th></tr><tr><td>Hospital</td><td>7774</td><td>2.79</td><td>0.014</td></tr><tr><td>No Hospital</td><td>90049</td><td>2.07</td><td>0.003</td></tr></tbody></table>

The di§erence in the means is 0.71, a large and highly signiÖcant contrast in favor of the non-hospitalized, with a t-statistic of 58.9.

Taken at face value, this result suggests that going to the hospital makes people sicker. Itís not impossible this is the right answer: hospitals are full of other sick people who might infect us, and dangerous machines and chemicals that might hurt us. Still, itís easy to see why this comparison should not be taken at face value: people who go to the hospital are probably less healthy to begin with. Moreover, even after hospitalization people who have sought medical care are not as healthy, on average, as those who never get hospitalized in the Örst place, though they may well be better than they otherwise would have been.

To describe this problem more precisely, think about hospital treatment as described by a binary random variable, d<sup>i</sup> = f0; 1g. The outcome of interest, a measure of health status, is denoted by y<sup>i</sup> . The question is whether y<sup>i</sup> is a§ected by hospital care. To address this question, we assume we can imagine what might have happened to someone who went to the hospital if they had not gone and vice versa. Hence, for any individual there are two potential health variables:

{26}------------------------------------------------

$$potential \ outcome = \left\{ egin{array}{ll} \mathbf{Y}_{1i} & ext{if } \mathbf{D}_i = 1 \\ \mathbf{Y}_{0i} & ext{if } \mathbf{D}_i = 0 \end{array} 
ight. .$$

In other words,  $Y_{0i}$  is the health status of an individual had he not gone to the hospital, irrespective of whether he actually went, while  $Y_{1i}$  is the individual's health status if he goes. We would like to know the difference between  $Y_{1i}$  and  $Y_{0i}$ , which can be said to be the causal effect of going to the hospital for individual i. This is what we would measure if we could go back in time and change a person's treatment status.<sup>2</sup>

The observed outcome,  $Y_i$ , can be written in terms of potential outcomes as

<span id="page-26-1"></span>
$$Y_{i} = \begin{cases} Y_{1i} & \text{if } D_{i} = 1 \\ Y_{0i} & \text{if } D_{i} = 0 \end{cases}$$
$$= Y_{0i} + (Y_{1i} - Y_{0i})D_{i}. \tag{2.1.1}$$

This notation is useful because  $Y_{1i} - Y_{0i}$  is the causal effect of hospitalization for an individual. In general, there is likely to be a distribution of both  $Y_{1i}$  and  $Y_{0i}$  in the population, so the treatment effect can be different for different people. But because we never see both potential outcomes for any one person, we must learn about the effects of hospitalization by comparing the average health of those who were and were not hospitalized.

A naive comparison of averages by hospitalization status tells us something about potential outcomes, though not necessarily what we want to know. The comparison of average health conditional on hospitalization status is formally linked to the average causal effect by the equation below:

$$\underbrace{E\left[\mathbf{Y}_{i}|\mathbf{D}_{i}=1\right]-E\left[\mathbf{Y}_{i}|\mathbf{D}_{i}=0\right]}_{\text{Observed difference in average health}} = \underbrace{E\left[\mathbf{Y}_{1i}|\mathbf{D}_{i}=1\right]-E\left[\mathbf{Y}_{0i}|\mathbf{D}_{i}=1\right]}_{\text{average treatment effect on the treated}} + \underbrace{E\left[\mathbf{Y}_{0i}|\mathbf{D}_{i}=1\right]-E\left[\mathbf{Y}_{0i}|\mathbf{D}_{i}=0\right]}_{\text{selection bias}}$$

The term

$$E[Y_{1i}|D_i = 1] - E[Y_{0i}|D_i = 1] = E[Y_{1i} - Y_{0i}|D_i = 1]$$

is the average causal effect of hospitalization on those who were hospitalized. This term captures the averages difference between the health of the hospitalized,  $E[Y_{1i}|D_i = 1]$ , and what would have happened to them had they not been hospitalized,  $E[Y_{0i}|D_i = 1]$ . The observed difference in health status however, adds to this causal effect a term called selection bias. This term is the difference in average  $Y_{0i}$  between those who

<span id="page-26-0"></span><sup>&</sup>lt;sup>2</sup>The potential outcomes idea is a fundamental building block in modern research on causal effects. Important references developing this idea are Rubin (1974, 1977), and Holland (1986), who refers to a causal framework involving potential outcomes as the Rubin Causal Model.

{27}------------------------------------------------

were and were not hospitalized. Because the sick are more likely than the healthy to seek treatment, those who were hospitalized have worse y0<sup>i</sup>ís, making selection bias negative in this example. The selection bias may be so large (in absolute value) that it completely masks a positive treatment e§ect. The goal of most empirical economic research is to overcome selection bias, and therefore to say something about the causal e§ect of a variable like d<sup>i</sup> .