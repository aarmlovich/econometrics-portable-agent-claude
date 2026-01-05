# Bad Control

> Pages: 62-66

Weíve made the point that control for covariates can make the CIA more plausible. But more control is not always better. Some variables are bad controls and should not be included in a regression model even when their inclusion might be expected to change the short regression coe¢ cients. Bad controls are variables that are themselves outcome variables in the notional experiment at hand. That is, bad controls might just as well be dependent variables too. Good controls are variables that we can think of as having been Öxed at the time the regressor of interest was determined.

The essence of the bad control problem is a version of selection bias, albeit somewhat more subtle than

<span id="page-62-0"></span><sup>1 3</sup> This program appears to raise earnings, primarily because workers in the training group went back to work more quickly.

<span id="page-62-1"></span><sup>1 4</sup>Lotteries have been used to distribute private school tuition subsidies; see, e.g., Angrist, et al. (2002).

{63}------------------------------------------------

the selection bias discussed in Chapter [\(2\)](#page-24-0) and Section [\(3.2\)](#page-53-0). To illustrate, suppose we are interested in the e§ects of a college degree on earnings and that people can work in one of two occupations, white collar and blue collar. A college degree clearly opens the door to higher-paying white collar jobs. Should occupation therefore be seen as an omitted variable in a regression of wages on schooling? After all, occupation is highly correlated with both education and pay. Perhaps itís best to look at the e§ect of college on wages for those within an occupation, say white collar only. The problem with this argument is that once we acknowledge the fact that college a§ects occupation, comparisons of wages by college degree status within an occupation are no longer apples-to-apples, even if college degree completion is randomly assigned.

Here is a formal illustration of the bad control problem in the college/occupation example.[15](#page-63-0) Let w<sup>i</sup> be a dummy variable that denotes white collar workers and let y<sup>i</sup> denote earnings. The realization of these variables is determined by college graduation status and potential outcomes that are indexed against c<sup>i</sup> . We have

$$Y_i = C_i Y_{1i} + (1 - C_i) Y_{0i}$$
  
 $W_i = C_i W_{1i} + (1 - C_i) W_{0i}$ 

where c<sup>i</sup> = 1 for college graduates and is zero otherwise, {y1<sup>i</sup> ,y0<sup>i</sup>} denotes potential earnings, and {w1<sup>i</sup> ,w0<sup>i</sup>} denotes potential white-collar status. We assume that c<sup>i</sup> is randomly assigned, so it is independent of all potential outcomes. We have no trouble estimating the causal e§ect of c<sup>i</sup> on either y<sup>i</sup> or w<sup>i</sup> since independence gives us

$$\begin{split} E\left[\mathbf{Y}_{i}|\mathbf{C}_{i}=1\right] - E\left[\mathbf{Y}_{i}|\mathbf{C}_{i}=0\right] &= E\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}\right], \\ E\left[\mathbf{W}_{i}|\mathbf{C}_{i}=1\right] - E\left[\mathbf{W}_{i}|\mathbf{C}_{i}=0\right] &= E\left[\mathbf{W}_{1i} - \mathbf{W}_{0i}\right]. \end{split}$$

In practice, we might estimate these average treatment e§ects by regressing y<sup>i</sup> and w<sup>i</sup> and on c<sup>i</sup> :

Bad control means that a comparison of earnings conditional on w<sup>i</sup> does not have a causal interpretation. Consider the di§erence in mean earnings between college graduates and others conditional on working at a white collar job. We can compute this in a regression model that includes w<sup>i</sup> or by regressing y<sup>i</sup> on c<sup>i</sup> in the sample where w<sup>i</sup> = 1: The estimand in the latter case is the di§erence in means with c<sup>i</sup> switched o§ and on, conditional on w<sup>i</sup> = 1:

<span id="page-63-1"></span>
$$E\left[\mathbf{Y}_{i} \middle| \mathbf{W}_{i} = 1, \mathbf{C}_{i} = 1\right] - E\left[\mathbf{Y}_{i} \middle| \mathbf{W}_{i} = 1, \mathbf{C}_{i} = 0\right] = E\left[\mathbf{Y}_{1i} \middle| \mathbf{W}_{1i} = 1, \mathbf{C}_{i} = 1\right] - E\left[\mathbf{Y}_{0i} \middle| \mathbf{W}_{0i} = 1, \mathbf{C}_{i} = 0\right] \quad (3.2.12)$$

<span id="page-63-0"></span><sup>1 5</sup> The same problem arises in "conditional-on-positive" comparisons, discussed in detail in section [\(3.4.2\)](#page-88-0), below.

{64}------------------------------------------------

By the joint independence of  $\{Y_{1i}, W_{1i}, Y_{0i}, W_{0i}\}$  and  $C_i$ , we have

$$E\left[\mathbf{Y}_{1i} \middle| \mathbf{W}_{1i} = 1, \mathbf{C}_i = 1\right] - E\left[\mathbf{Y}_{0i} \middle| \mathbf{W}_{0i} = 1, \mathbf{C}_i = 0\right] = E\left[\mathbf{Y}_{1i} \middle| \mathbf{W}_{1i} = 1\right] - E\left[\mathbf{Y}_{0i} \middle| \mathbf{W}_{0i} = 1\right].$$

This expression illustrates the apples-to-oranges nature of the bad-control problem:

$$\begin{split} &E\left[\mathbf{Y}_{1i}|\mathbf{W}_{1i}=1\right] - E\left[\mathbf{Y}_{0i}|\mathbf{W}_{0i}=1\right] \\ &= \underbrace{E\left[\mathbf{Y}_{1i} - \mathbf{Y}_{0i}|\mathbf{W}_{1i}=1\right]}_{\text{causal effect on college grads}} + \underbrace{\left\{E\left[\mathbf{Y}_{0i}|\mathbf{W}_{1i}=1\right] - E\left[\mathbf{Y}_{0i}|\mathbf{W}_{0i}=1\right]\right\}}_{\text{selection bias}}. \end{split}$$

In other words, the difference in wages between those with and without a college degree conditional on working in a white collar job equals the causal effect of college on those with  $W_{1i} = 1$  (people who work at a white collar job when they have a college degree) and a selection-bias term which reflects the fact that college changes the composition of the pool of white collar workers.

The selection-bias in this context can be positive or negative, depending on the relation between occupational choice, college attendance, and potential earnings. The main point is that even if  $Y_{1i} = Y_{0i}$ , so that there is no causal effect of college on wages, the conditional comparison in (3.2.12) will not tell us this (the regression of  $Y_i$  on  $W_i$  and  $C_i$  has exactly the same problem). It is also incorrect to say that the conditional comparison captures the part of the effect of college that is "not explained by occupation." In fact, the conditional comparison does not tell us much that is useful without a more elaborate model of the links between college, occupation, and earnings. <sup>16</sup>

As an empirical illustration, we see that the addition of two-digit occupation dummies indeed reduces the schooling coefficient in the NLSY models reported in Table 3.2.1, in this case from .087 to .066. However, it's hard to say what we should make of this decline. The change in schooling coefficients when we add occupation dummies may simply be an artifact of selection bias. So we would do better to control only for variables that are not themselves caused by education.

A second version of the bad control scenario involves *proxy control*, that is, the inclusion of variables that might partially control for omitted factors, but are themselves affected by the variable of interest. A simple version of the proxy-control scenario goes like this: Suppose you are interested in a long regression, similar to equation (3.2.10),

<span id="page-64-1"></span>
$$Y_i = \alpha + \rho S_i + \gamma a_i + \varepsilon_i, \tag{3.2.13}$$

where for the purposes of this discussion we've replaced the vector of controls  $A_i$ , with a scalar ability measure  $a_i$ . Think of this as an IQ score that measures innate ability in eighth grade, before any relevant

<span id="page-64-0"></span><sup>&</sup>lt;sup>16</sup>In this example, selection bias is probably negative, that is  $E[Y_{0i}|W_{1i}=1] < E[Y_{0i}|W_{0i}=1]$ . It seems reasonable to think that any college graduate can get a white collar job, so  $E[Y_{0i}|W_{1i}=1]$  is not too far from  $E[Y_{0i}]$ . But someone who gets a white collar without benefit of a college degree (i.e.,  $W_{0i}=1$ ) is probably special, i.e., has a better than average  $Y_{0i}$ .

{65}------------------------------------------------

schooling choices are made (assuming everyone completes eighth grade). The error term in this equation satisÖes E[si"<sup>i</sup> ] = E[ai"<sup>i</sup> ] = 0 by deÖnition. Since a<sup>i</sup> is measured before s<sup>i</sup> is determined, it is a good control.

Equation [\(3.2.13\)](#page-64-1) is the regression of interest, but unfortunately, data on a<sup>i</sup> are unavailable. However, you have a second ability measure collected later, after schooling is completed (say, the score on a test used to screen job applicants). Call this variable "late ability," ali. In general, schooling increases late ability relative to innate ability. To be speciÖc, suppose

<span id="page-65-0"></span>
$$a_{li} = \pi_0 + \pi_1 S_i + \pi_2 a_i. (3.2.14)$$

By this, we mean to say that both schooling and innate ability increase late or measured ability. There is almost certainly some randomness in measured ability as well, but we can make our point more simply via the deterministic link, [\(3.2.14\)](#page-65-0).

Youíre worried about OVB in the regression of y<sup>i</sup> on s<sup>i</sup> alone, so you propose to regress y<sup>i</sup> on s<sup>i</sup> and late ability, ali since the desired control, a<sup>i</sup> , is unavailable. Using [\(3.2.14\)](#page-65-0) to substitute for a<sup>i</sup> in [\(3.2.13\)](#page-64-1), the regression on s<sup>i</sup> and ali is

<span id="page-65-1"></span>
$$Y_i = (\alpha - \gamma \frac{\pi_0}{\pi_2}) + (\rho - \gamma \frac{\pi_1}{\pi_2})S_i + \frac{\gamma}{\pi_2}a_{li} + \varepsilon_i.$$
(3.2.15)

In this scenario, , 1, and <sup>2</sup> are all positive, so <sup>1</sup> <sup>2</sup> is too small unless <sup>1</sup> turns out to be zero. In other words, use of a proxy control that is increased by the variable of interest generates a coe¢ cient below the desired e§ect. Importantly, <sup>1</sup> can be investigated to some extent: if the regression of ali on s<sup>i</sup> is zero, you might feel better about assuming that <sup>1</sup> is zero in [\(3.2.14\)](#page-65-0).

There is an interesting ambiguity in the proxy-control story that is not present in the Örst bad-control story. Control for outcome variables is simply misguided; you do not want to control for occupation in a schooling regression if the regression is to have a causal interpretation. In the proxy-control scenario, however, your intentions are good. And while proxy control does not generate the regression coe¢ cient of interest, it may be an improvement on no control at all. Recall that the motivation for proxy control is equation [\(3.2.13\)](#page-64-1). In terms of the parameters in this model, the OVB formula tells us that a regression on s<sup>i</sup> with no controls generates a coe¢ cient of + as, where as is slope coe¢ cient from a regression of a<sup>i</sup> on s<sup>i</sup> . The schooling coe¢ cient in [\(3.2.15\)](#page-65-1) might be closer to than the coe¢ cient you estimate with no control at all. Moreover, assuming as is positive, you can safely say that the causal e§ect of interest lies between these two.

One moral of both the bad-control and the proxy-control stories is that when thinking about controls, timing matters. Variables measured before the variable of interest was determined are generally good controls. In particular, because these variables were determined before the variable of interest, they cannot themselves 

{66}------------------------------------------------

be outcomes in the causal nexus. In many cases, however, the timing is uncertain or unknown. In such cases, clear reasoning about causal channels requires explicit assumptions about what happened Örst, or the assertion that none of the control variables are themselves caused by the regressor of interest.[17](#page-66-0)

# 3.3 Heterogeneity and Nonlinearity

As we saw in the previous section, a linear causal model in combination with the CIA leads to a linear CEF with a causal interpretation. Assuming the CEF is linear, the population regression is it. In practice, however, the assumption of a linear CEF is not really necessary for a causal interpretation of regression. For one thing, as discussed in Section [3.1.2,](#page-41-0) we can think of the regression of y<sup>i</sup> on X<sup>i</sup> and s<sup>i</sup> as providing the best linear approximation to the underlying CEF, regardless of its shape. Therefore, if the CEF is causal, the fact that regression approximates it gives regression coe¢ cients a causal áavor. This claim is a little vague, however, and the nature of the link between regression and the CEF is worth exploring further. This exploration leads us to an understanding of regression as a computationally attractive matching estimator.