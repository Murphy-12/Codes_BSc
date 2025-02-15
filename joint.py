import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Define sample space for discrete variables
sample_space_x = [1, 2, 3]
sample_space_y = [1, 2]

# Probability distributions for x and y
prob_x = [0.2, 0.5, 0.3]  # P(x)
prob_y = [0.6, 0.4]       # P(y)

# Compute joint probabilities assuming independence
joint_prob = np.outer(prob_x, prob_y)

print("Joint Probability (Discrete):")
joint_prob = np.outer(prob_x, prob_y)

print("Joint Probability (Discrete):")
for i, x in enumerate(sample_space_x):
    for j, y in enumerate(sample_space_y):
        print(f"P(X={x}, Y={y}) = {joint_prob[i, j]:.3f}")
        
