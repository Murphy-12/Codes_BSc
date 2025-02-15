import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

# Parameters
N, M = 1000, 10000  # Sample size and number of samples

# Generate distributions and compute means
distributions = {
    "Binomial": np.mean(np.random.binomial(10, 0.5, (M, N)), axis=1),
    "Normal": np.mean(np.random.normal(0, 1, (M, N)), axis=1),
    "Poisson": np.mean(np.random.poisson(6, (M, N)), axis=1),
    "Cauchy (CLT Violation)": np.mean(cauchy.rvs(0, 1, (M, N)), axis=1)
}

# Plot histograms
plt.figure(figsize=(10, 5))
for i, (name, data) in enumerate(distributions.items(), 1):
    plt.subplot(2, 2, i)
    plt.hist(data, bins=30, edgecolor='black', alpha=0.6)
    plt.title(f"{name} Distribution")
    plt.xlabel("Mean")
    plt.ylabel("Frequency")

plt.tight_layout()
plt.show()