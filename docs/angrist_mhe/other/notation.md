# Notation

> Pages: 269-280

- $X_i$  a K×1 vector of covariates, with elements  $x_{ki}$ ; k = 1, ..., K
- $x_i$  the single regressor in a bivariate regression
- $Y_i$  an outcome or dependent variable
- $\varepsilon_i \equiv Y_i E[Y_i|X_i]$ , the CEF residual
- $\beta \equiv \underset{b}{\operatorname{arg\,min}} E\left[\left(\mathbf{Y}_{i} \mathbf{X}_{i}'b\right)^{2}\right], \quad \text{the population regression vector;} \quad \beta = E\left[\mathbf{X}_{i}\mathbf{X}_{i}'\right]^{-1} E\left[\mathbf{X}_{i}\mathbf{Y}_{i}\right]$
- $e_i \equiv Y_i X_i'\beta$ , a population regression residual
- $\tilde{x}_{ki}$  the residual from a regression of regressor  $x_{ki}$  on all other covariates in the model
- $w_i$  the inverse probability of sampling observation i
- $\hat{\beta} \equiv \left[\sum_{i} X_{i} X_{i}'\right]^{-1} \sum_{i} X_{i} Y_{i}$ , the OLS estimator
- $\hat{e}_i \equiv Y_i X_i' \hat{\beta}$ , the estimated residual
- $f_i(s)$  an individual-specific causal relationship between schooling and earnings, e.g., the amount i would earn with s years of schooling
- $\delta_{TOT} \equiv E[Y_{1i} Y_{0i}|D_i = 1], \text{ the effect of treatment on the treated}$
- $\delta_{ATE} \equiv E \left[ \mathbf{Y}_{1i} \mathbf{Y}_{0i} \right], \text{ the average treatment effect}$
- $h(s) \equiv E[Y_i|S_i = s]$ , the CEF of  $Y_i$  given schooling equal to s
  - $\mu_t \equiv \{E[\mathbf{s}_i|\mathbf{s}_i \geq t] E[\mathbf{s}_i|\mathbf{s}_i < t]\}\{P(\mathbf{s}_i \geq t)[1 P(\mathbf{s}_i \geq t)]\}, \text{ the implicit weight on } \mathbf{s}_i \text{ when the population regression of } \mathbf{y}_i \text{ on } \mathbf{s}_i \text{ is interpreted as a weighted average of } h'(s)$
  - $\delta_R$  the population regression of Y<sub>i</sub> on D<sub>i</sub>, controlling for a saturated model for covariates
  - $\mathbf{Y}_i^*$  —a latent outcome variable, related to the observed outcome variable by  $\mathbf{Y}_i = \mathbf{1}[\mathbf{Y}_i^* > 0]$
  - $A_i$  a vector of omitted variables in a regression (e.g., "ability" in a regression of wages on schooling)
  - $z_i$  a dummy instrumental variable; if more than one instrument,  $z_{qi}; q = 1, ..., Q$ . In a vector combining instruments with exogenous covariates,  $Z_i \equiv \begin{bmatrix} X_i' & z_{1i} & ... & z_{Qi} \end{bmatrix}'$
  - $\hat{s}_i$  fitted values in a population regression of  $s_i$  on covariates and instruments,  $X_i'\hat{\pi}_{10} + \hat{\pi}_{11}Z_i$
- $D_{0i}, D_{1i}$  a pair of potential treatment assignments indexed against  $Z_i$ 
  - $D_i$  the observed treatment variable, equal to  $(1-Z_i)D_{0i} + Z_iD_{1i}$  in an IV set-up

{270}------------------------------------------------

 $\Gamma \equiv \left[\begin{array}{cc} \alpha' & \rho \end{array}\right]'$ , the vector of coefficients in a 2SLS second stage equation, where the coefficient of interest is  $\rho$ 

$$\hat{\Gamma}_{2SLS} \equiv \left[\sum_{i} V_{i} V_{i}'\right]^{-1} \sum_{i} V_{i} \mathbf{Y}_{i}, \text{ a 2SLS estimator}$$
$$= \left[W' P_{Z} W\right]^{-1} W' P_{Z} \mathbf{Y}$$

- $Y_i(d, z)$  the potential outcome of individual i were this person to have treatment status  $D_i = d$  and instrument value  $Z_i = z$ .
  - $\rho_i \equiv Y_{1i} Y_{0i},$  the individual treatment effect in a random coefficients setup with a binary treatment  $D_i$
  - $\pi_{1i}$  heterogeneous causal effect of an instrument on  $D_i$  in random coefficients setup:  $D_i = D_{0i} + (D_{1i} D_{0i})Z_i = \pi_0 + \pi_{1i}Z_i + v_i$ .
  - $\kappa_i$  Abadie kappa,  $\kappa_i = 1 \frac{D_i(1-Z_i)}{1-P(Z_i=1|X_i)} \frac{(1-D_i)Z_i}{P(Z_i=1X_i)}$ , the weight used to find the expectation of any function of the data for compliers
  - $\eta_i$  error term in a causal model, e.g.,  $y_i = \beta x_i + \eta_i$
  - $\xi_i$  error term in a 1st stage regression, e.g.,  $x_i = Z_i'\pi + \xi_i$
- $\varepsilon_{it}, \varepsilon_{ist}$  population regression errors in panel data in chapter 5
  - $\Phi\left[\cdot\right]$  standard normal cumulative distribution function (CDF)
    - $\phi[\cdot]$  standard normal density
- $\Phi_b(\cdot,\cdot;\rho_{\varepsilon\nu})$  bivariate standard normal CDF with correlation coefficient  $\rho_{\varepsilon\nu}$ 
  - $Y_{it-h}$  observation on the dependent variable h periods ago
    - $\Delta$  difference operator, e.g.  $\Delta Y_{it} = Y_{it} Y_{it-1}$
- $F_Y(y|X_i)$  the distribution function for  $Y_i$  conditional on  $X_i$ .
- $Q_{\tau}(\mathbf{Y}_{i}|\mathbf{X}_{i}) \equiv F_{V}^{-1}(\tau|\mathbf{X}_{i}), \text{ conditional quantile function (CQF)}$ 
  - $\rho_{\tau}(u) = (\tau 1(u \leq 0))u$ , check function, the expectation of which is minimized by the COF
    - $\boldsymbol{\beta}_{\tau} \quad \equiv \mathop{\arg\min}_{\iota} \, E \left[ \rho_{\tau} (\mathbf{Y}_i \mathbf{X}_i' b) \right], \, \text{population quantile regression vector}$
- $\Delta_{\tau}(X_i, \beta_{\tau}) \equiv X_i' \beta_{\tau} Q_{\tau}(Y_i | X_i)$ , quantile regression specification error
  - $\Omega$  asymptotic covariance matrix of the OLS estimator
  - $\Psi \equiv E[ee']$ , variance matrix of residuals, with diagonal elements  $\psi_i$
  - $e_{ig} \equiv \nu_g + \eta_{ig}$ , error with a group structure in chapter 8
  - $\hat{\Omega}_c = (X'X)^{-1} \left(\sum \frac{\hat{e}_i^2}{N}\right)$ , conventional variance estimator
  - $\hat{\Omega}_r = (X'X)^{-1} \left(\sum_{i=1}^{N} \frac{X_i X_i \hat{e}_i^2}{N}\right) (X'X)^{-1}$ , robust variance estimator
  - $H \equiv X(X'X)^{-1}X'$ , covariate projection matrix
  - $h_{ii} \equiv X_i'(X'X)^{-1}X_i$ , the leverage of the ith observation, the ith diagonal element of H
  - $M \equiv I_N H$ , the residual maker matrix

{271}------------------------------------------------

NOTATION

{272}------------------------------------------------

# References

- Abadie, Alberto (2003): ìSemiparametric Instrumental Variable Estimation of Treatment Response Models,îJournal of Econometrics, 113, 231ñ263.
- Abadie, Alberto, Joshua D. Angrist, and Guido Imbens (2002): ìInstrumental Variables Estimates of the E§ect of Subsidized Training on the Quantiles of Trainee Earnings,îEconometrica, 70, 91ñ117.
- Abadie, Alberto, Alexis Diamond, and Jens Hainmueller (2007): ìSynthetic Control Methods for Comparative Case Studies: Estimating the E§ect of Californiaís Tobacco Control Program,î National Bureau of Economic Research, Working Paper No. 12831.
- Abadie, Alberto, and Guido Imbens (2006): ìLarge Sample Properties of Matching Estimators for Average Treatment E§ects,îEconometrica, 74, 235ñ67.
- (2008): ìBias-Corrected Matching Estimators for Average Treatment E§ects,îHarvard University, Department of Economics, mimeo.
- Acemoglu, Daron, and Joshua Angrist (2000): ìHow Large are the Social Returns to Education? Evidence from Compulsory Schooling Laws,î in National Bureau of Economics Macroeconomics Annual 2000, ed. by Ben S. Bernanke, and Kenneth S. Rogo§, pp. 9ñ58. The MIT Press, Cambridge.
- Acemoglu, Daron, Simon Johnson, and James A. Robinson (2001): ìThe Colonial Origins of Comparative Development: An Empirical Investigation,îThe American Economic Review, 91, 1369ñ1401.
- Adams, Douglas (1979): The Hitchhikerís Guide to the Galaxy. Pocket Books, New York.
- (1990): Dirk Gentlyís Holistic Detective Agency. Simon & Schuster, New York.
- (1995): Mostly Harmless. Harmony Books, New York.
- Altonji, Joseph G., and Lewis M. Segal (1996): ìSmall-Sample Bias in GMM Estimation of Covariance Structures,îJournal of Business and Economic Statistics, 14, 353ñ366.
- Ammermueller, Andreas, and Jorn-Steffan Pischke (2006): ìPeer E§ects in European Primary Schools: Evidence from PIRLS,î Institute for the Study of Labor (IZA), Discussion Paper No. 2077.

{273}------------------------------------------------

Ananat, Elizabeth, and Guy Michaels (2008): ìThe E§ect of Marital Breakup on the Income Distribution of Women with Children,îJournal of Human Resources, forthcoming.

- Anderson, Michael (2008): ìMultiple Inference and Gender Di§erences in the E§ect of Early Intervention: A Reevaluation of the Abecedarian, Perry Preschool, and Early Training Projects,î Journal of the American Statistical Association, forthcoming.
- Angrist, Joshua, Eric Bettinger, Erik Bloom, Elizabeth King, and Michael Kremer (2002): ìVouchers for Private Schooling in Colombia: Evidence from a Randomized Natural Experiment,î The American Economic Review, 92, 1535ñ1558.
- Angrist, Joshua D. (1988): ìGrouped Data Estimation and Testing in Simple Labor Supply Models,î Princeton University, Industrial Section, Working Paper No. 234.
- (1990): ìLifetime Earnings and the Vietnam Era Draft Lottery: Evidence from Social Security Administrative Records,îAmerican Economic Review, 80, 313ñ335.
- (1991): ìGrouped Data Estimation and Testing in Simple Labor Supply Models,î Journal of Econometrics, 47, 243ñ266.
- (1998): ìEstimating the Labor Market Impact on Voluntary Military Service Using Social Security Data on Military Applicants,îEconometrica, 66, 249ñ288.
- (2001): ìEstimations of Limited Dependent Variable Models with Dummy Endogenous Regressors: Simple Strategies for Empirical Practice,îJournal of Business and Economic Statistics, 19, 2ñ16.
- (2004): ìAmerican Education Research Changes Track,î Oxford Review of Economic Policy, 20, 198ñ212.
- (2006): ìInstrumental Variables Methods in Experimental Criminological Research: What, Why and How,îJournal of Experimental Criminology, 2, 22ñ44.
- Angrist, Joshua D., Victor Chernozhukov, and Ivan Fernandez-Val (2006): ìQuantile Regression Under MisspeciÖcation, with an Application to the U.S. Wage Structure,îEconometrica, 74, 539ñ563.
- Angrist, Joshua D., and William N. Evans (1998): ìChildren and Their Parentsí Labor Supply: Evidence from Exogenous Variation in Family Size,îAmerican Economic Review, 88, 450ñ477.
- (1999): ìSchooling and Labor Market Consequences of the 1970 State Abortion Reforms,îin Research in Labor Economics, ed. by Solomon W. Polachek, vol. 18, pp. 75ñ113. Elsevier Science, Amsterdam.
- Angrist, Joshua D., Kathryn Graddy, and Guido W. Imbens (2000): ìThe Interpretation of Instrumental Variables Estimators in Simultaneous Equations Models with an Application to the Demand for Fish,îReview of Economic Studies, 67, 499ñ527.

{274}------------------------------------------------

Angrist, Joshua D., and Jinyong Hahn (2004): ìWhen to Control for Covariates? Panel Asymptotics for Estimates of Treatment E§ects,îReview of Economics and Statistics, 86, 58ñ72.

- Angrist, Joshua D., Guido Imbens, and Donald B. Rubin (1996): ìIdentiÖcation of Causal E§ects Using Instrumental Variables,îJournal of the American Statistical Association, 91, 444ñ472.
- Angrist, Joshua D., and Guido W. Imbens (1995): ìTwo-Stage Least Squares Estimation of Average Causal E§ects in Models with Variable Treatment Intensity,î Journal of the American Statistical Association, 90, 430ñ442.
- Angrist, Joshua D., and Alan B. Krueger (1991): ìDoes Compulsory Schooling Attendance A§ect Schooling and Earnings?,îQuarterly Journal of Economics, 106, 976ñ1014.
- (1992): ìThe E§ect of Age at School Entry on Educational Attainment: An Application of Instrumental Variables with Moments from Two Samples,îJournal of the American Statistical Association, 418, 328ñ36.
- (1995): ìSplit-Sample Instrumental Variables Estimates of the Return to Schooling,î Journal of Business and Economic Statistics, 13, 225ñ35.
- (1999): ìEmpirical Strategies in Labor Economics,î in Handbook of Labor Economics, ed. by Orley C. Ashenfelter, and David Card, vol. 3. North Holland, Amsterdam.
- (2001): ìInstrumental Variables and the Search for IdentiÖcation: From Supply and Demand to Natural Experiments,îJournal of Economic Perspectives, 15, 69ñ85.
- Angrist, Joshua D., and Guido Kuersteiner (2004): ìSemiparametric Causality Tests Using the Policy Propensity Score,îNational Bureau of Economic Research, Working Paper No. 10975.
- Angrist, Joshua D., and Kevin Lang (2004): ìDoes School Integration Generate Peer E§ects? Evidence from Bostonís Metco Program,îThe American Economic Review, 94, 1613ñ1634.
- Angrist, Joshua D., and Victor Lavy (1999): ìUsing MaimonidesíRule to Estimate the E§ect of Class Size on Scholastic Achievement,îQuarterly Journal of Economics, 114, 533ñ575.
- (2007): ìThe E§ects of High Stakes High School Achievement Awards: Evidence from a Group-Randomized Trial,îunpublished paper, Department of Economics, Massachusetts Institute of Technology.
- Angrist, Joshua D., Victor Lavy, and Analia Schlosser (2006): ìMultiple Experiments for the Causal Link Between the Quantity and Quality of Children,î MIT Department of Economics Working Paper No. 06-26.

{275}------------------------------------------------

ARELLANO, MANUEL, AND STEPHEN BOND (1991): "Some Tests of Specification for Panel Data: Monte Carlo Evidence and an Application to Employment Equations," The Review of Economic Studies, 58, 277–297.

- ASHENFELTER, ORLEY A. (1978): "Estimating the Effect of Training Programs on Earnings," Review of Economics and Statistics, 60, 47–57.
- ——————————————————————————————————————
- ASHENFELTER, ORLEY A., AND DAVID CARD (1985): "Using the Longitudinal Structure of Earnings to Estimate the Effect of Training Programs," The Review of Economics and Statistics, 67, 648–660.
- ASHENFELTER, ORLEY A., AND ALAN B. KRUEGER (1994): "Estimates of the Economic Return to Schooling from a New Sample of Twins," *American Economic Review*, 84, 1157–1173.
- ASHENFELTER, ORLEY A., AND CECILIA ROUSE (1998): "Income, Schooling, and Ability: Evidence from a New Sample of Identical Twins," *Quarterly Journal of Economics*, 113, 253–284.
- ATHEY, SUSAN, AND GUIDO IMBENS (2006): "Identification and Inference in Nonlinear Difference-in-Difference Models," *Econometrica*, 74, 431–497.
- ATKINSON, ANTHONY B. (1970): "On the Measurement of Inequality," *Journal of Economic Theory*, 2, 244–263.
- Autor, David (2003): "Outsourcing at Will: The Contribution of Unjust Dismissal Doctrine to the Growth of Employment Outsourcing," *Journal of Labor Economics*, 21, 1–42.
- Autor, David, Lawrence F. Katz, and Melissa S. Kearney (2005): "Rising Wage Inequality: The Role of Composition and Prices," National Bureau of Economic Research, Working Paper No. 11628.
- BARNETT, STEVEN W. (1992): "Benefits of Compensatory Preschool Education," *Journal of Human Resources*, 27, 279–312.
- BARNOW, BURT S., GLEN G. CAIN, AND ARTHUR GOLDBERGER (1981): "Selection on Observables," Evaluation Studies Review Annual, 5, 43–59.
- Bekker, Paul A. (1994): "Alternative Approximations to the Distributions of Instrumental Variable Estimators," *Econometrica*, 62, 657–681.
- Bell, Robert M., and Daniel F. McCaffrey (2002): "Bias Reduction in Standard Errors for Linear Regression with Multistage Samples," Survey Methodology, 28, 169–181.

{276}------------------------------------------------

Bennedsen, Morten, Kasper M. Nielsen, Francisco Pérez-González, and Daniel Wolfenzon (2007): "Inside the Family Firm: The Role of Families in Succession Decisions and Performance," *The Quarterly Journal of Economics*, 122, 647–692.

- BERTRAND, MARIANNE, ESTHER DUFLO, AND SENDHIL MULLAINATHAN (2004): "How Much Should We Trust Differences-in-Differences Estimates?," Quarterly Journal of Economics, 119, 249–275.
- BERTRAND, MARIANNE, AND SENDHIL MULLAINATHAN (2004): "Are Emily and Greg More Employable than Lakisha and Jamal? A Field Experiment on Labor Market Discrimination," *The American Economic Review*, 94, 991–1013.
- Besley, Timothy, and Robin Burgess (2004): "Can Labour Market Regulation Hinder Economic Performance? Evidence from India," Quarterly Journal of Economics, 113, 91–134.
- BJORKLUND, ANDERS, AND MARKUS JANTTI (1997): "Intergenerational Income Mobility in Sweden Compared to the United States," *The American Economic Review*, 87, 1009–1018.
- BLACK, DAN A., JEFFREY A. SMITH, MARK C. BERGER, AND BRETT J. NOEL (2003): "Is the Threat of Reemployment Services More Effective than the Services Themselves? Evidence from Random Assignment in the UI System," *The American Economic Review*, 93, 1313–1327.
- BLOOM, HOWARD S. (1984): "Estimating the Effect of Job-Training Programs, Using Longitudinal Data: Ashenfelter's Findings Reconsidered," *The Journal of Human Resources*, 19, 544–556.
- BLOOM, HOWARD S., LARRY L. ORR, STEPHEN H. BELL, GEORGE CAVE, FRED DOOLITTLE, WINSTON LIN, AND JOHANNES M. BOS (1997): "The Benefits and Costs of JTPA Title II-A Programs: Key Findings from the National Job Training Partnership Act Study," *The Journal of Human Resources*, 32, 549–576.
- Blundell, Richard, and Stephen Bond (1998): "Initial Conditions and Moment Restrictions in Dynamic Panel Data Models," *Journal of Econometrics*, 87, 115–143.
- BORJAS, GEORGE (1992): "Ethnic Capital and Intergenerational Mobility," Quarterly Journal of Economics, 107, 123–150.
- ——— (2005): Labor Economics, 3rd edn. McGraw-Hill/Irwin, New York.
- BOUND, JOHN, DAVID JAEGER, AND REGINA BAKER (1995): "Problems with Instrumental Variables Estimation when the Correlation between the Instruments and the Endogenous Variables is Weak," *Journal of American Statistical Association*, 90, 443–450.
- BOUND, JOHN, AND GARY SOLON (1999): "Double Trouble: On the Value of Twins-based Estimation of the Returns of Schooling," *Economics of Education Review*, 18, 169–182.

{277}------------------------------------------------

Bronars, Stephen G., and Jeff Grogger (1994): ìThe Economic Consequences of Unwed Motherhood: Using Twin Births as a Natural Experiment,îAmerican Economic Review, 84, 1141ñ1156.

- Buchinsky, Moshe (1994): ìChanges in the U.S. Wage Structure 1963-1987: Application of Quantile Regression,îEconometrica, 62, 405ñ458.
- Buse, A. (1992): ìThe Bias of Instrumental Variable Estimators,îEconometrica, 60, 173ñ180.
- Cameron, Colin, Jonah Gelbach, and Douglas L. Miller (2008): ìBootstrap-Based Improvements for Inference with Clustered Errors,îThe Review of Economics and Statistics, forthcoming, unpublished paper, Department of Economics, The University of California at Davis.
- Campbell, Donald Thomas (1969): ìReforms as Experiments,îAmerican Psychologist, 24, 409ñ429.
- Campbell, Donald Thomas, and Julian C. Stanley (1963): Experimental and Quasi-experimental Designs for Research. Rand McNally, Chicago.
- Card, David (1992): ìUsing Regional Variation to Measure the E§ect of the Federal Minimum Wage,î Industrial and Labor Relations Review, 46, 22ñ37.
- (1995): ìEarnings, Schooling and Ability Revisited,î in Research in Labor Economics, ed. by Solomon W. Polachek, vol. 14, pp. 23ñ48. JAI Press, Greenwich, Connecticut.
- (1999): ìThe Causal E§ect of Education on Earnings,î in Handbook of Labor Economics, ed. by Orley C. Ashenfelter, and David Card, vol. 3. North Holland, Amsterdam.
- Card, David, and Alan Krueger (1994): ìMinimum Wages and Employment: A Case Study of the Fast Food Industry in New Jersey and Pennsylvania,îAmerican Economic Review, 84, 772ñ784.
- (2000): ìMinimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania: Reply,îAmerican Economic Review, 90, 1397ñ420.
- Card, David, and David S. Lee (2008): ìRegression Discontinuity Inference with SpeciÖcation Error,î Journal of Econometrics, 142, 655ñ674.
- Card, David, and Thomas Lemieux (1996): ìWage Dispersion, Returns to Skill, and Black-White Differentials,îJournal of Econometrics, 74, 316ñ361.
- Card, David E., and Daniel Sullivan (1988): ìMeasuring the E§ect of Subsidized Training on Movements In and Out of Employment,îEconometrica, 56, 497ñ530.
- Cardell, Nicholas Scott, and Mark Myron Hopkins (1977): ìEducation, Income, and Ability: A Comment,îJournal of Political Economy, 85, 211ñ215.

{278}------------------------------------------------

Chamberlain, Gary (1977): "Education, Income, and Ability Revisited," *Journal of Econometrics*, 5, 241–57.

- ——————————————————————————————————————
- ——————————————————————————————————————
- ——————————————————————————————————————
- Chamberlain, Gary, and Edward E. Leamer (1976): "Matrix Weighted Averages and Posterior Bounds," Journal of the Royal Statistical Society, Series B, 38, 73–84.
- CHERNOZHUKOV, VICTOR, AND CHRISTIAN HANSEN (2005): "An IV Model of Quantile Treatment Effects," Econometrica, 73, 245–261.
- ———— (2007): "A Simple Approach to Heteroskedasticity and Autocorrelation Robust Inference with Weak Instruments," unpublished paper, Department of Economics, Massachusetts Institute of Technology.
- Chesher, Andrew, and Gerald Austin (1991): "The Finite-Sample Distributions of Heteroskedasticity Robust Wald Statistics," *Journal of Econometrics*, 47, 153–173.
- CHESHER, ANDREW, AND IAN JEWITT (1987): "The Bias of the Heteroskedasticity Consistent Covariance Estimator," *Econometrica*, 55, 1217–1222.
- Cochran, William G. (1965): "The Planning of Observational Studies of Human Populations," *Journal* of the Royal Statistical Society, Series A, 128, 234–65.
- COOK, THOMAS D. (2008): "Waiting for Life to Arrive: A History of the Regression-Discontinuity Design in Psychology, Statistics, and Economics," *Journal of Econometrics*, 142, 636–654, forthcoming.
- COOK, THOMAS D., AND VIVIAN C. WONG (2008): "Empirical Tests of the Validity of the Regression-Discontinuity Design," Annales d'Economie et de Statistique, forthcoming.
- CRUMP, RICHARD K., V. JOSEPH HOTZ, GUIDO W. IMBENS, AND OSCAR A. MITNIK (2006): "Moving the Goalposts: Addressing Limited Overlap in the Estimation of Average Treatment Effects by Changing the Estimand," National Bureau of Economic Research, Technical Working Paper No. 330.
- CRUZ, LUIZ M., AND MARCELO J. MOREIRA (2005): "On the Validity of Econometric Techniques with Weak Instruments: Inference on Returns to Education Using Compulsory School Attendance Laws," *Journal of Human Resources*, 40, 393–410.

{279}------------------------------------------------

Currie, Janet, and Aaron Yelowitz (2000): "Are Public Housing Projects Good for Kids?," *Journal of Public Economics*, 75, 99–124.

- DAVIDON, RUSSELL, AND JAMES G. MACKINNON (1993): Estimation and Inference in Econometrics. Oxford University Press, New York.
- DEARDEN, LORRAINE, SUE MIDDLETON, SUE MAGUIRE, KARL ASHWORTH, KATE LEGGE, TRACEY ALLEN, KIM PERRIN, ERICH BATTISTIN, CARL EMMERSON, EMLA FITZSIMONS, AND COSTAS MEGHIR (2004): "The Evaluation of Education Maintenance Allowance Pilots: Three Years' Evidence. A Quantitative Evaluation," Department for Education and Skills, Research Report No. 499.
- Deaton, Angus (1997): The Analysis of Household Surveys: A Microeconometric Approach to Development Policy. Johns Hopkins University Press for the World Bank, Baltimore, MD.
- DEE, THOMAS S., AND WILLIAM N. EVANS (2003): "Teen Drinking and Educational Attainment: Evidence from Two-Sample Instrumental Variables Estimates," *Journal of Labor Economics*, 21, 178–209.
- Degroot, Morris H., and Mark J. Schervish (2001): *Probability and Statistics*, 3rd edn. Addison-Wesley, Boston.
- Dehejia, Rajeev H. (2005): "Practical Propensity Score Matching: A Reply to Smith and Todd," *Journal of Econometrics*, 125, 355–364.
- Dehejia, Rajeev H., and Sadek Wahba (1999): "Causal Effects in Nonexperimental Studies: Reevaluating the Evaluation of Training Programs," *Journal of the American Statistical Association*, 94, 1053–62.
- Donald, Stephen G., and Kevin Lang (2007): "Inference with Difference-in-Differences and Other Panel Data," *Review of Economics and Statistics*, 89, 221–233.
- Duan, Naihua, Willard D. Manning, Jr., Carl N. Morris, and Joseph P. Newhouse (1983): "A Comparison of Alternative Models for the Models for the Demand for Medical Care," *Journal of Business & Economic Statistics*, 1, 115–126.
- ———— (1984): "Choosing Between the Sample-Selection Model and the Multi-Part Model," *Journal of Business & Economic Statistics*, 2, 283–289.
- Durbin, James (1954): "Errors in Variables," Review of the International Statistical Institute, 22, 23–32.
- EICKER, FRIEDHELM (1967): "Limit Theorems for Regressions with Unequal and Dependent Errors," in Proceedings of the Fifth Berkeley Symposium on Mathematical Statistics and Probability, vol. 1, pp. 59–82. University of California Press, Berkeley.

{280}------------------------------------------------

Elder, Todd E., and Darren H. Lubotsky (2008): ìKindergarten Entrance Age and Childrenís Achievement: Impacts of State Policies, Family Background, and Peers,îJournal of Human Resources, forthcoming, forthcoming.

- Finn, Jeremy D., and Charles M. Achilles (1990): ìAnswers and Questions About Class Size: A Statewide Experiment,îAmerican Educational Research Journal, 28, 557ñ77.
- Firpo, Sergio (2007): ìE¢ cient Semiparametric Estimation of Quantile Treatment E§ects,îEconometrica, 75, 259ñ276.
- Flores-Lagunes, Alfonso (2007): ìFinite Sample Evidence of IV Estimators under Weak Instruments,î Journal of Applied Econometrics, 22, 677ñ694.
- Freedman, David (2005): ìLinear Statistical Models for Causation: A Critical Review,î in The Wiley Encyclopedia of Statistics in Behavioral Science, ed. by B. Everitt, and D. Howell. John Wiley, Chichester, UK.
- Freeman, Richard (1984): ìLongitudinal Analyses of the E§ect of Trade Unions,î Journal of Labor Economics, 3, 1ñ26.
- Frisch, Ragnar, and Frederick V. Waugh (1933): ìPartial Time Regression as Compared with Individual Trends,îEconometrica, 1, 387ñ401.
- Frolich, Markus, and Blaise Melly (2007): ìUnconditional Quantile Treatment E§ects Under Endogeneity,îCentre for Microdata Methods and Practice, Working Paper No. CWP32/07.
- Fryer, Roland G., and Steven D. Levitt (2004): ìThe Causes and Consequences of Distinctively Black Names,îThe Quarterly Journal of Economics, 119, 767ñ805.
- Goldberger, Arthur S. (1972): ìSelection Bias in Evaluating Treatment E§ects: Some Formal Illustrations,îUniversity of Wisconsin, Department of Economics, Working Paper.
- (1991): A Course in Econometrics. Harvard University Press, Cambridge, MA.
- Gosling, Amanda, Stephen Machin, and Costas Meghir (2000): ìThe Changing Distribution of Male Wages in the U.K.,îReview of Economic Studies, 67, 635ñ66.
- Granger, Clive W. J. (1969): ìInvestigating Causal Relation by Econometric and Cross-Sectional Method,îEconometrica, 37, 424ñ438.
- Griliches, Zvi (1977): ìEstimating the Returns to Schooling: Some Econometric Problems,îEconometrica, 45, 1ñ22.