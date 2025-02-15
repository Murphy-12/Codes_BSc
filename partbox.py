import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

m=9.1*1e-31
l=1e-13
hbar=1.05*1e-31
N=1000

x=np.linspace(0,l,N)
dx=(x[1]-x[0])
H=np.zeros((N,N))
for i in range(1,N-1):
    H[i,i]=-2
    H[i,i-1]=1
    H[i-1,i]=1
H[0,0]=H[-1,-1]=1
H[0,1]=H[N-1,N-2]=0
H=-H*hbar**2/(2*m*dx**2)
energy,psi=eigh(H)
print(H)
print('energy eigen values are',energy)
for i in range(3):
    print(energy[i])
    plt.plot(x,psi[:,i])
plt.show()