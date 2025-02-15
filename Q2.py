import numpy as np
import random
from scipy.stats import norm
from collections import Counter
import matplotlib.pyplot as plt

#discrete

# Function to compute joint probability for given (xi, yi)
def compute_joint_probability(xi, yi):
    joint_counts = Counter(zip(xi, yi))  # Count occurrences of each pair
    total_samples = len(xi)  # Total number of data points
    joint_prob = {key: value / total_samples for key, value in joint_counts.items()}  # Normalize
    return joint_prob

# Given discrete dataset (e.g., rolling two dice)
x_dis= np.random.randint(1, 7, 10000)  # Simulated dice roll (1 to 6)
y_dis = np.random.randint(1, 7, 10000)  # Another dice roll
joint_prob_discrete = compute_joint_probability(x_dis, y_dis)

# Verify: Display first 10 computed probabilities
print("Discrete Joint Probability (First 10):")
print(dict(list(joint_prob_discrete.items())[:10]))

# Visualization of discrete case
plt.figure(figsize=(10,5))
plt.hist2d(x_dis, y_dis, bins=[6,6], density=True, cmap='Blues')
plt.colorbar(label="Joint Probability Density")
plt.xlabel("X (Dice 1)")
plt.ylabel("Y (Dice 2)")
plt.title("Joint Probability Distribution (Discrete Case)")
plt.show()

# Example 2: Continuous random variables (Normal & Uniform)
xi_continuous = np.random.normal(loc=0, scale=1, size=10000)  # Normal distribution
yi_continuous = np.random.uniform(low=-2, high=2, size=10000)  # Uniform distribution

# Compute 2D histogram (joint probability)
hist, x_edges, y_edges = np.histogram2d(xi_continuous, yi_continuous, bins=30, density=True)

# Visualization of continuous case
N=10000
x=np.random.normal(5,10,N)
k=np.random.normal(0,6,N)
joint_hist,x_edg,y_edg=np.histogram2d(x,k,bins=30)
total=np.sum(joint_hist)
joint_prob=joint_hist/total
#plotting
plt.imshow(joint_prob,)
plt.colorbar(label='density')
plt.show()
