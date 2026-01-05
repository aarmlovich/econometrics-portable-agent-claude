# Analysis of Single-Spell Data with Time-Invariant Covariates

> Pages: 699-701

We assume that the population of interest is individuals entering the initial state during a given interval of time, say ½0; b, where b > 0 is a known constant. (Naturally, ''individual'' can be replaced with any population unit of interest, such as ''family'' or ''firm.'') As in all econometric contexts, it is very important to be explicit about the

{700}------------------------------------------------

underlying population. By convention, we let zero denote the earliest calendar date that an individual can enter the initial state, and b is the last possible date. For example, if we are interested in the population of U.S. workers who became unemployed at any time during 1998, and unemployment duration is measured in years (with .5 meaning half a year), then b ¼ 1. If duration is measured in weeks, then b ¼ 52; if duration is measured in days, then b ¼ 365; and so on.

In using the methods of this section, we typically ignore the fact that durations are often grouped into discrete intervals—for example, measured to the nearest week or month—and treat them as continuously distributed. If we want to explicitly recognize the discreteness of the measured durations, we should treat them as grouped data, as we do in Section 20.4.

We restrict attention to single-spell data. That is, we use, at most, one completed spell per individual. If, after leaving the initial state, an individual subsequently reenters the initial state in the interval ½0; b, we ignore this information. In addition, the covariates in the analysis are time invariant, which means we collect covariates on individuals at a given point in time—usually, at the beginning of the spell—and we do not re-collect data on the covariates during the course of the spell. Time-varying covariates are more naturally handled in the context of grouped duration data in Section 20.4.

We study two general types of sampling from the population that we have described. The most common, and the easiest to handle, is flow sampling. In Section 20.3.3 we briefly consider various kinds of stock sampling.

# 20.3.1 Flow Sampling

With flow sampling, we sample individuals who enter the state at some point during the interval ½0; b, and we record the length of time each individual is in the initial state. We collect data on covariates known at the time the individual entered the initial state. For example, suppose we are interested in the population of U.S. workers who became unemployed at any time during 1998, and we randomly sample from U.S. male workers who became unemployed during 1998. At the beginning of the unemployment spell we might obtain information on tenure in last job, wage on last job, gender, marital status, and information on unemployment benefits.

There are two common ways to collect flow data on unemployment spells. First, we may randomly sample individuals from a large population, say, all working-age individuals in the United States for a given year, say, 1998. Some fraction of these people will be in the labor force and will become unemployed during 1998—that is, enter the initial state of unemployment during the specified interval—and this group of people who become unemployed is our random sample of all workers who become


{701}------------------------------------------------

unemployed during 1998. Another possibility is retrospective sampling. For example, suppose that, for a given state in the United States, we have access to unemployment records for 1998. We can then obtain a random sample of all workers who became unemployed during 1998.

Flow data are usually subject to right censoring. That is, after a certain amount of time, we stop following the individuals in the sample, which we must do in order to analyze the data. (Right censoring is the only kind that occurs with flow data, so we will often refer to right censoring as ''censoring'' in this and the next subsection.) For individuals who have completed their spells in the initial state, we observe the exact duration. But for those still in the initial state, we only know that the duration lasted as long as the tracking period. In the unemployment duration example, we might follow each individual for a fixed length of time, say, two years. If unemployment spells are measured in weeks, we would have right censoring at 104 weeks. Alternatively, we might stop tracking individuals at a fixed calendar date, say, the last week in 1999. Because individuals can become unemployed at any time during 1998, calendar-date censoring results in censoring times that differ across individuals.