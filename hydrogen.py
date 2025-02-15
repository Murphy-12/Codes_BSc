import numpy as np
import matplotlib.pyplot as plt

xf=1e-6
m=0.511*1e6
hc=1973
e=3.795
N=1000

x=np.linspace(-xf,20,N)
dx=x[1]-x[0]
v=-e**2/(x)
A=np.zeros((N,N))
for i in range(N):
    A[i,i]=-2
    A[i,i-1]=1
    A[i-1,i]=1
A[0,N-1]=0
A[N-1,0]=0
k=-hc**2/(2*m*(dx**2))
T=k*A
H=T+np.diag(v)
E,psi=np.linalg.eigh(H)
print(E[0],'in eV',E[0]/1.6*1e-19 )
for i in range(3):
    plt.plot(x,psi[:,i])
plt.show()