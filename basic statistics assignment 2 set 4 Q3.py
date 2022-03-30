import numpy as np
from scipy import stats
from scipy.stats import norm
# For No investigation P(45<X<55)
# For Investigation 1-P(45<X<55)
# find z-scores at x=45; z=(s_mean-P_mean)/(p_SD/sqrt(n))
z=(45-50)/(40/100**0.5)
z
# find z-scores at x=55; z=(s_mean-P_mean)/(p_SD/sqrt(n))
z=(55-50)/(40/100**0.5)
z
# For No investigation P(45<X<55) using z_scores = P(X<50)-P(X<45)
stats.norm.cdf(1.25)-stats.norm.cdf(-1.25)
stats.norm.interval(0.7887,loc=50,scale=40/(100**0.5))
# For Investigation 1-P(45<X<55)
1-0.7887