# A General FGLS Analysis

> Pages: 275-276

If the idiosyncratic errors  $\{u_{it}: t = 1, 2, ..., T\}$  are generally heteroskedastic and serially correlated across t, a more general estimator of  $\Omega$  can be used in FGLS:

$$\hat{\mathbf{\Omega}} = N^{-1} \sum_{i=1}^{N} \hat{\hat{\mathbf{v}}}_i \hat{\hat{\mathbf{v}}}_i' \tag{10.38}$$

where the  $\hat{\mathbf{v}}_i$  would be the pooled OLS residuals. The FGLS estimator is consistent under Assumptions RE.1 and RE.2, and, if we assume that  $\mathrm{E}(\mathbf{v}_i\mathbf{v}_i'\mid\mathbf{x}_i)=\mathbf{\Omega}$ , then the FGLS estimator is asymptotically efficient and its asymptotic variance estimator takes the usual form.

Using equation (10.38) is more general than the RE analysis. In fact, with large N asymptotics, the general FGLS estimator is just as efficient as the random effects estimator under Assumptions RE.1–RE.3. Using equation (10.38) is asymptotically more efficient if  $E(\mathbf{v}_i\mathbf{v}_i'|\mathbf{x}_i) = \mathbf{\Omega}$ , but  $\mathbf{\Omega}$  does not have the random effects form. So why not always use FGLS with  $\hat{\mathbf{\Omega}}$  given in equation (10.38)? There are historical reasons for using random effects methods rather than a general FGLS analysis. The structure of  $\mathbf{\Omega}$  in the matrix (10.30) was once synonomous with unobserved effects models: any correlation in the composite errors  $\{v_{it}: t=1,2,\ldots,T\}$  was assumed to be caused by the presence of  $c_i$ . The idiosyncratic errors,  $u_{it}$ , were, by definition, taken to be serially uncorrelated and homoskedastic.

If N is not several times larger than T, an unrestricted FGLS analysis can have poor finite sample properties because  $\hat{\Omega}$  has T(T+1)/2 estimated elements. Even though estimation of  $\Omega$  does not affect the asymptotic distribution of the FGLS estimator, it certainly affects its finite sample properties. Random effects estimation requires estimation of only two variance parameters for any T.

{276}------------------------------------------------

With very large N, using the general estimate of  $\Omega$  is an attractive alternative, especially if the estimate in equation (10.38) appears to have a pattern different from the random effects pattern. As a middle ground between a traditional random effects analysis and a full-blown FGLS analysis, we might specify a particular structure for the idiosyncratic error variance matrix  $E(\mathbf{u}_i\mathbf{u}_i')$ . For example, if  $\{u_{it}\}$  follows a stable first-order autoregressive process with autocorrelation coefficient  $\rho$  and variance  $\sigma_u^2$ , then  $\Omega = E(\mathbf{u}_i\mathbf{u}_i') + \sigma_c^2\mathbf{j}_T\mathbf{j}_T'$  depends in a known way on only three parameters,  $\sigma_u^2$ ,  $\sigma_c^2$ , and  $\rho$ . These parameters can be estimated after initial pooled OLS estimation, and then an FGLS procedure using the particular structure of  $\Omega$  is easy to implement. We do not cover such possibilities explicitly; see, for example, MaCurdy (1982).