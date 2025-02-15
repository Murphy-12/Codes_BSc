import numpy as np
import random
from scipy.stats import binomtest

q=0.6
n=100
toss=np.random.binomial(1,q,n)
print(toss)

qn=0.5
num=np.sum(toss)
result=binomtest(num,n,qn)
print(result)

alpha=0.05
if(result<alpha):
    print("Coin is biased(rejected)")
else:
    print("coin is unbiased(accepted)")