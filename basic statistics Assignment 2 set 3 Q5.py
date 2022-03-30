import numpy as np
from scipy import stats
from scipy.stats import norm

# Apply One-Sample One-Tail z-test
z_scores = (0.046 - 0.05) / (np.sqrt((0.05 * (1 - 0.05)) / 2000))
z_scores
# Find Probability assuming null hyposthesis, so as to compare with Type-1 error α = 0.05
p_value = 1 - stats.norm.cdf(abs(z_scores))
p_value
