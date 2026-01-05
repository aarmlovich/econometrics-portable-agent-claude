# A. Average Education by Quarter of Birth (first stage)

> Pages: 103-104

![](_page_103_Figure_3.jpeg)

# B. Average Weekly Wage by Quarter of Birth (reduced form)

![](_page_103_Figure_5.jpeg)

<span id="page-103-0"></span>Figure 4.1.1: Graphical depiction of first stage and reduced form for IV estimates of the economic return to schooling using quarter of birth (from Angrist and Krueger 1991).

{104}------------------------------------------------

X<sup>i</sup> . The parameter <sup>21</sup> in equation [\(4.1.4b\)](#page-102-1) captures the reduced-form e§ect of z<sup>i</sup> on y<sup>i</sup> , adjusting for these same covariates. In the language of the SEM, the dependent variables in these two equations are said to be the endogenous variables (where they are determined jointly within the system) while the variables on the right-hand side are said to be the exogenous variables (determined outside the system). The instruments, z<sup>i</sup> , are a subset of the exogenous variables. The exogenous variables that are not instruments are said to be exogenous covariates. Although weíre not estimating a traditional supply and demand system in this case, these SEM variable labels are still widely used in empirical practice.

The covariate-adjusted IV estimator is the sample analog of the ratio <sup>21</sup> <sup>11</sup> . To see this, note that the denominators of the reduced-form and Örst-stage e§ects are the same. Hence, their ratio is

<span id="page-104-0"></span>
$$\rho = \frac{\pi_{21}}{\pi_{11}} = \frac{Cov(\mathbf{Y}_i, \tilde{\mathbf{z}}_i)}{Cov(\mathbf{S}_i, \tilde{\mathbf{z}}_i)},\tag{4.1.5}$$

where z~<sup>i</sup> is the residual from a regression of z<sup>i</sup> on the exogenous covariates, X<sup>i</sup> . The right-hand side of [\(4.1.5\)](#page-104-0) therefore swaps z~<sup>i</sup> for z<sup>i</sup> in the general IV formula, [\(4.1.3\)](#page-101-0). Econometricians call the sample analog of the left-hand side of equation [\(4.1.5\)](#page-104-0) an Indirect Least Squares (ILS) estimator of in the causal model with covariates,

<span id="page-104-2"></span>
$$Y_i = \alpha' X_i + \rho S_i + \eta_i, \tag{4.1.6}$$

where <sup>i</sup> is the compound error term, A<sup>0</sup> i + v<sup>i</sup> [5](#page-104-1) . Itís easy to use equation [\(4.1.6\)](#page-104-2) to conÖrm directly that Cov(y<sup>i</sup> ; z~i) = Cov(s<sup>i</sup> ; z~i) since z~<sup>i</sup> is uncorrelated with X<sup>i</sup> by construction and with <sup>i</sup> by assumption. In Angrist and Krueger (1991), the instrument, z<sup>i</sup> , is quarter of birth (or dummies indicating quarters of birth) and the covariates are dummies for year of birth, state of birth, and race.