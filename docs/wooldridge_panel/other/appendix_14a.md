# Appendix 14A

> Pages: 459-462

*Proof of Lemma* 14.1: Given condition (14.55),  $\mathbf{A}_1 = (1/\rho)\mathbf{E}(\mathbf{s}_1\mathbf{s}_1')$ , a  $P \times P$  symmetric matrix, and

$$\mathbf{V}_1 = \mathbf{A}_1^{-1} \mathbf{E}(\mathbf{s}_1 \mathbf{s}_1') \mathbf{A}_1^{-1} = \rho^2 [\mathbf{E}(\mathbf{s}_1 \mathbf{s}_1')]^{-1}$$

where we drop the argument **w** for notational simplicity. Next, under condition (14.56),  $\mathbf{A}_2 = (1/\rho)\mathbf{E}(\mathbf{s}_2'\mathbf{s}_1)$ , and so

$$\mathbf{V}_2 = \mathbf{A}_2^{-1} \mathrm{E}(\mathbf{s}_2 \mathbf{s}_2') (\mathbf{A}_2')^{-1} = \rho^2 [\mathrm{E}(\mathbf{s}_2 \mathbf{s}_1')]^{-1} \mathrm{E}(\mathbf{s}_2 \mathbf{s}_2') [\mathrm{E}(\mathbf{s}_1 \mathbf{s}_2')]^{-1}$$

{460}------------------------------------------------

Now we use the standard result that  $V_2 - V_1$  is positive semidefinite if and only if  $V_1^{-1} - V_2^{-1}$  is p.s.d. But, dropping the term  $\rho^2$  (which is simply a positive constant), we have

$$\boldsymbol{V}_{1}^{-1} - \boldsymbol{V}_{2}^{-1} = E(\boldsymbol{s}_{1}\boldsymbol{s}_{1}') - E(\boldsymbol{s}_{1}\boldsymbol{s}_{2}')[E(\boldsymbol{s}_{2}\boldsymbol{s}_{2}')]^{-1}E(\boldsymbol{s}_{2}\boldsymbol{s}_{1}') \equiv E(\boldsymbol{r}_{1}\boldsymbol{r}_{1}')$$

where  $\mathbf{r}_1$  is the  $P \times 1$  population residual from the population regression  $\mathbf{s}_1$  on  $\mathbf{s}_2$ . As  $E(\mathbf{r}_1\mathbf{r}_1')$  is necessarily p.s.d., this step completes the proof.


{461}------------------------------------------------

# IV NONLINEAR MODELS AND RELATED TOPICS

We now apply the general methods of Part III to study specific nonlinear models that often arise in applications. Many nonlinear econometric models are intended to explain limited dependent variables. Roughly, a limited dependent variable is a variable whose range is restricted in some important way. Most variables encountered in economics are limited in range, but not all require special treatment. For example, many variables—wage, population, and food consumption, to name just a few—can only take on positive values. If a strictly positive variable takes on numerous values, special econometric methods are rarely called for. Often, taking the log of the variable and then using a linear model suffices.

When the variable to be explained, y, is discrete and takes on a finite number of values, it makes little sense to treat it as an approximately continuous variable. Discreteness of y does not in itself mean that a linear model for Eðy j xÞ is inappropriate. However, in Chapter 15 we will see that linear models have certain drawbacks for modeling binary responses, and we will treat nonlinear models such as probit and logit. We also cover basic multinomial response models in Chapter 15, including the case when the response has a natural ordering.

Other kinds of limited dependent variables arise in econometric analysis, especially when modeling choices by individuals, families, or firms. Optimizing behavior often leads to corner solutions for some nontrivial fraction of the population. For example, during any given time, a fairly large fraction of the working age population does not work outside the home. Annual hours worked has a population distribution spread out over a range of values, but with a pileup at the value zero. While it could be that a linear model is appropriate for modeling expected hours worked, a linear model will likely lead to negative predicted hours worked for some people. Taking the natural log is not possible because of the corner solution at zero. In Chapter 16 we will discuss econometric models that are better suited for describing these kinds of limited dependent variables.

We treat the problem of sample selection in Chapter 17. In many sample selection contexts the underlying population model is linear, but nonlinear econometric methods are required in order to correct for nonrandom sampling. Chapter 17 also covers testing and correcting for attrition in panel data models, as well as methods for dealing with stratified samples.

In Chapter 18 we provide a modern treatment of switching regression models and, more generally, random coefficient models with endogenous explanatory variables. We focus on estimating average treatment effects.

We treat methods for count-dependent variables, which take on nonnegative integer values, in Chapter 19. An introduction to modern duration analysis is given in Chapter 20.

{462}------------------------------------------------