# Leaving the Omitted Factors in the Error Term

> Pages: 120

Consider again the omitted variable model

$$y = \beta_0 + \beta_1 x_1 + \dots + \beta_K x_K + \gamma q + v$$
 (5.45)

where q represents the omitted variable and Eðv j x; qÞ ¼ 0. The solution that would follow from Section 5.1.1 is to put q in the error term, and then to find instruments for any element of x that is correlated with q. It is useful to think of the instruments satisfying the following requirements: (1) they are redundant in the structural model Eðy j x; qÞ; (2) they are uncorrelated with the omitted variable, q; and (3) they are sufficiently correlated with the endogenous elements of x (that is, those elements that are correlated with q). Then 2SLS applied to equation (5.45) with u1 gq þ v produces consistent and asymptotically normal estimators.