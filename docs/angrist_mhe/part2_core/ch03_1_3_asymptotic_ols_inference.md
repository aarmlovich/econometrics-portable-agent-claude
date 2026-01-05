# Asymptotic OLS Inference

> Pages: 45-47

In practice, we don't usually know what the CEF or the population regression vector is. We therefore draw statistical inferences about these quantities using samples. Statistical inference is what much of traditional econometrics is about. Although this material is covered in any Econometrics text, we don't want to skip the inference step completely. A review of basic asymptotic theory allows us to highlight the important fact that the process of statistical inference is entirely distinct from the question of how a particular set of regression

{46}------------------------------------------------

![](_page_46_Figure_2.jpeg)

<span id="page-46-0"></span>Sample is limited to white men, age 40-49. Data is from Census IPUMS 1980, 5% sample.

Figure 3.1.2: Regression threads the CEF of average weekly wages given schooling

estimates should be interpreted. Whatever a regression coefficient may mean, it has a sampling distribution that is easy to describe and use for statistical inference.<sup>3</sup>

We are interested in the distribution of the sample analog of

$$\beta = E[X_i X_i']^{-1} E[X_i Y_i]$$

in repeated samples. Suppose the vector  $W_i \equiv \begin{bmatrix} Y_i; & X_i' \end{bmatrix}'$  is independently and identically distributed in a sample of size N. A natural estimator of the first population moment,  $E[W_i]$ , is the sum,  $\frac{1}{N} \sum_{i=1}^{N} W_i$ . By the law of large numbers, this sample moment gets arbitrarily close to the corresponding population moment as the sample size grows. We might similarly consider higher-order moments of the elements of  $W_i$ , e.g., the matrix of second moments,  $E[W_iW_i']$ , with sample analog  $\frac{1}{N} \sum_{i=1}^{N} W_iW_i'$ . Following this principle, the method of moments estimator of  $\beta$  replaces each expectation by a sum. This logic leads to the Ordinary Least Squares (OLS) estimator

$$\hat{\beta} = \left[\sum_{i} \mathbf{X}_{i} \mathbf{X}_{i}'\right]^{-1} \sum_{i} \mathbf{X}_{i} \mathbf{Y}_{i}.$$

Although we derived  $\hat{\beta}$  as a method of moments estimator, it is called the OLS estimator of  $\beta$  because it solves the sample analog of the least-squares problem described at the beginning of Section 3.1.2.<sup>4</sup>

<span id="page-46-1"></span><sup>&</sup>lt;sup>3</sup>The discussion of asymptotic OLS inference in this section is largely a condensation of material in Chamberlain (1984). Important pitfalls and problems with this asymptotic theory are covered in the last chapter.

<span id="page-46-2"></span><sup>&</sup>lt;sup>4</sup>Econometricians like to use matrices because the notation is so compact. Sometimes (not very often) we do too. Suppose

{47}------------------------------------------------