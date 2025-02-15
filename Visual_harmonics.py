import numpy as np
import matplotlib.pyplot as plt
from scipy.special import sph_harm
from mpl_toolkits.mplot3d import Axes3D

l=1
m=1

theta=np.linspace(0,np.pi,200)
phi=np.linspace(0,2*np.pi,200)
phi,theta=np.meshgrid(phi,theta)
Y=sph_harm(l,m,phi,theta)
prob=np.abs(Y**2)
x=prob*np.sin(theta)*np.cos(phi)
y=prob*np.sin(theta)*np.sin(phi)
z=prob*np.cos(theta)
print(x,y,z)

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z)
plt.show()