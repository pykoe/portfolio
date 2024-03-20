import numpy as np
import pandas as pd
import statsmodels.api as sm

# Generate simulated data for two groups (A and B)
np.random.seed(42)

# Simulated click-through data (number of successes and total trials)
clicks_A = np.random.randint(50, 100, size=1000)
views_A = np.random.randint(500, 1000, size=1000)

clicks_B = np.random.randint(60, 110, size=1000)
views_B = np.random.randint(500, 1000, size=1000)

# Create a DataFrame
data = pd.DataFrame({
    'Group': ['A'] * 1000 + ['B'] * 1000,
    'Clicks': np.concatenate([clicks_A, clicks_B]),
    'Views': np.concatenate([views_A, views_B])
})

# Perform a proportion test using statsmodels
proportions = np.array([clicks_A.sum(), clicks_B.sum()])
trials = np.array([views_A.sum(), views_B.sum()])

z_score, p_value = sm.stats.proportions_ztest(proportions, trials, alternative='two-sided')

# Output the results
print("A/B Test Results:")
print(f"Z-score: {z_score}")
print(f"P-value: {p_value}")

# Check if the results are statistically significant
alpha = 0.05
if p_value < alpha:
    print("Results are statistically significant. Reject the null hypothesis.")
else:
    print("Results are not statistically significant. Fail to reject the null hypothesis.")
