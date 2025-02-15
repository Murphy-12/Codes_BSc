import numpy as np
import matplotlib.pyplot as plt

m=9.1*1e-31
l=1e-13
hbar=1.05*1e-34
N=1000
v0=50*1.6*1e-19
a=l/N

x=np.linspace(-l/2,l/2,N)
#potential array
v=np.zeros(N)
v[x<-l/4]=v0
v[x>l/4]=v0
#finite difference hamiltonian matrix
H=np.zeros((N,N))
for i in range(1,N-1):
    H[i,i]=-2
    H[i,i-1]=1
    H[i-1,i]=1
H[0,0]=-2
H[0,1]=1
H[N-1,N-2]=1
H[N-1,N-1]=-2
H=-H*hbar**2/(2*m*(a**2))
v_matrix=np.diag(v)
H+=v_matrix
E,psi=np.linalg.eigh(H)
print(H)
print(E)
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.plot(x,psi[:,i])
plt.show()

