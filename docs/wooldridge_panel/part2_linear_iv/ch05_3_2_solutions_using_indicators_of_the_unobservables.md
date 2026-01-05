# Solutions Using Indicators of the Unobservables

> Pages: 120-123

An alternative solution to the omitted variable problem is similar to the OLS proxy variable solution but requires IV rather than OLS estimation. In the OLS proxy variable solution we assume that we have z<sup>1</sup> such that q ¼ y<sup>0</sup> þ y1z<sup>1</sup> þ r<sup>1</sup> where r<sup>1</sup> is uncorrelated with z<sup>1</sup> (by definition) and is uncorrelated with x1; ... ; xK (the key proxy variable assumption). Suppose instead that we have two indicators of q. Like a proxy variable, an indicator of q must be redundant in equation (5.45). The key difference is that an indicator can be written as

$$q_1 = \delta_0 + \delta_1 q + a_1 \tag{5.46}$$

where

$$Cov(q, a_1) = 0, \qquad Cov(\mathbf{x}, a_1) = \mathbf{0}$$

$$(5.47)$$


{121}------------------------------------------------

This assumption contains the classical errors-in-variables model as a special case, where q is the unobservable, q<sup>1</sup> is the observed measurement, d<sup>0</sup> ¼ 0, and d<sup>1</sup> ¼ 1, in which case g in equation (5.45) can be identified.

Assumption (5.47) is very different from the proxy variable assumption. Assuming that d<sup>1</sup> 0 0—otherwise q<sup>1</sup> is not correlated with q—we can rearrange equation (5.46) as

$$q = -(\delta_0/\delta_1) + (1/\delta_1)q_1 - (1/\delta_1)a_1 \tag{5.48}$$

where the error in this equation, ð1=d1Þa1, is necessarily correlated with q1; the OLS–proxy variable solution would be inconsistent.

To use the indicator assumption (5.47), we need some additional information. One possibility is to have a second indicator of q:

$$q_2 = \rho_0 + \rho_1 q + a_2 \tag{5.49}$$

where a<sup>2</sup> satisfies the same assumptions as a<sup>1</sup> and r<sup>1</sup> 00. We still need one more assumption:

$$Cov(a_1, a_2) = 0 (5.50)$$

This implies that any correlation between q<sup>1</sup> and q<sup>2</sup> arises through their common dependence on q.

Plugging q<sup>1</sup> in for q and rearranging gives

$$y = \alpha_0 + x\beta + \gamma_1 q_1 + (v - \gamma_1 a_1)$$
(5.51)

where g<sup>1</sup> ¼ g=d1. Now, q<sup>2</sup> is uncorrelated with v because it is redundant in equation (5.45). Further, by assumption, q<sup>2</sup> is uncorrelated with a<sup>1</sup> (a<sup>1</sup> is uncorrelated with q and a2). Since q<sup>1</sup> and q<sup>2</sup> are correlated, q<sup>2</sup> can be used as an IV for q<sup>1</sup> in equation (5.51). Of course the roles of q<sup>2</sup> and q<sup>1</sup> can be reversed. This solution to the omitted variables problem is sometimes called the multiple indicator solution.

It is important to see that the multiple indicator IV solution is very different from the IV solution that leaves q in the error term. When we leave q as part of the error, we must decide which elements of x are correlated with q, and then find IVs for those elements of x. With multiple indicators for q, we need not know which elements of x are correlated with q; they all might be. In equation (5.51) the elements of x serve as their own instruments. Under the assumptions we have made, we only need an instrument for q1, and q<sup>2</sup> serves that purpose.

Example 5.5 (IQ and KWW as Indicators of Ability): We apply the indicator method to the model of Example 4.3, using the 935 observations in NLS80.RAW. In addition to IQ, we have a knowledge of the working world (KWW ) test score. If we 

{122}------------------------------------------------

write IQ ¼ d<sup>0</sup> þ d1abil þ a1, KWW ¼ r<sup>0</sup> þ r1abil þ a2, and the previous assumptions are satisfied in equation (4.29), then we can add IQ to the wage equation and use KWW as an instrument for IQ. We get

$$log(\hat{w}age) = 4.59 + .014 \ exper + .010 \ tenure + .201 \ married$$

$$(0.33) \quad (.003) \qquad (.0041)$$

$$- .051 \ south + .177 \ urban - .023 \ black + .025 \ educ + .013 \ IQ$$

$$(.031) \qquad (.028) \qquad (.074) \qquad (.017) \qquad (.005)$$

The estimated return to education is about 2.5 percent, and it is not statistically significant at the 5 percent level even with a one-sided alternative. If we reverse the roles of KWW and IQ, we get an even smaller return to education: about 1.7 percent with a t statistic of about 1.07. The statistical insignificance is perhaps not too surprising given that we are using IV, but the magnitudes of the estimates are surprisingly small. Perhaps a<sup>1</sup> and a<sup>2</sup> are correlated with each other, or with some elements of x.

In the case of the CEV measurement error model, q<sup>1</sup> and q<sup>2</sup> are measures of q assumed to have uncorrelated measurement errors. Since d<sup>0</sup> ¼ r<sup>0</sup> ¼ 0 and d<sup>1</sup> ¼ r<sup>1</sup> ¼ 1, g<sup>1</sup> ¼ g. Therefore, having two measures, where we plug one into the equation and use the other as its instrument, provides consistent estimators of all parameters in the CEV setup.

There are other ways to use indicators of an omitted variable (or a single measurement in the context of measurement error) in an IV approach. Suppose that only one indicator of q is available. Without further information, the parameters in the structural model are not identified. However, suppose we have additional variables that are redundant in the structural equation (uncorrelated with v), are uncorrelated with the error a<sup>1</sup> in the indicator equation, and are correlated with q. Then, as you are asked to show in Problem 5.7, estimating equation (5.51) using this additional set of variables as instruments for q<sup>1</sup> produces consistent estimators. This is the method proposed by Griliches and Mason (1972) and also used by Blackburn and Neumark (1992).

#### Problems

5.1. In this problem you are to establish the algebraic equivalence between 2SLS and OLS estimation of an equation containing an additional regressor. Although the result is completely general, for simplicity consider a model with a single (suspected) endogenous variable:

{123}------------------------------------------------

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + u_1$$
$$y_2 = \mathbf{z} \boldsymbol{\pi}_2 + v_2$$

For notational clarity, we use y<sup>2</sup> as the suspected endogenous variable and z as the vector of all exogenous variables. The second equation is the reduced form for y2. Assume that z has at least one more element than z1.

We know that one estimator of ð*d*1; a1Þ is the 2SLS estimator using instruments x. Consider an alternative estimator of ð*d*1; a1Þ: (a) estimate the reduced form by OLS, and save the residuals ^v2; (b) estimate the following equation by OLS:

$$y_1 = \mathbf{z}_1 \boldsymbol{\delta}_1 + \alpha_1 y_2 + \rho_1 \hat{\mathbf{v}}_2 + error \tag{5.52}$$

Show that the OLS estimates of *d*<sup>1</sup> and a<sup>1</sup> from this regression are identical to the 2SLS estimators. [Hint: Use the partitioned regression algebra of OLS. In particular, if <sup>y</sup>^ <sup>¼</sup> <sup>x</sup><sup>1</sup> ^*b*<sup>1</sup> <sup>þ</sup> <sup>x</sup><sup>2</sup> ^*b*<sup>2</sup> is an OLS regression, ^*b*<sup>1</sup> can be obtained by first regressing <sup>x</sup><sup>1</sup> on x2, getting the residuals, say x€1, and then regressing y on x€1; see, for example, Davidson and MacKinnon (1993, Section 1.4). You must also use the fact that z<sup>1</sup> and ^v<sup>2</sup> are orthogonal in the sample.]