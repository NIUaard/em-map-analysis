import numpy as np
import matplotlib.pyplot as plt
#import pydefault24
import matplotlib.gridspec as gridspec
from matplotlib import ticker


Xintt=np.loadtxt('dist.ini')
X3dtt=np.loadtxt('9-celltest.0140.001')
X1dtt=np.loadtxt('9-celltest.0140.002')

Xin= Xintt[1:,:]+Xintt[0,:]
X3d= X3dtt[1:,:]+X3dtt[0,:]
X1d= X1dtt[1:,:]+X3dtt[0,:]


Nx=51
Ny=31

print ('min/max xxx', np.min(Xintt[:,0]),np.max(Xintt[:,1]))

fig = plt.figure(9999)
gs1 = gridspec.GridSpec(2, 3)
ax1 = fig.add_subplot(gs1[0:1,2:3])
ax2 = fig.add_subplot(gs1[1:2,2:3])
ax3 = fig.add_subplot(gs1[0:2,0:2])

gs1.update(top=0.95,bottom=0.130, left=0.15, right=0.92, hspace=0.5, wspace=0.5)

print ('ave. momentum 1D', X1d[0,5])
print ('ave. momentum 3D', X3d[0,5])
xxx = Xin[:,0].reshape((Nx,Ny))*1e3
yyy = Xin[:,1].reshape((Nx,Ny))*1e3

p1x = X1d[:,3].reshape((Nx,Ny))
p1y = X1d[:,4].reshape((Nx,Ny))
p1z = X1d[:,5].reshape((Nx,Ny))
p1a = np.sqrt(p1x**2+p1y**2)

p3x = X3d[:,3].reshape((Nx,Ny))
p3y = X3d[:,4].reshape((Nx,Ny))
p3z = X3d[:,5].reshape((Nx,Ny))
p3a = np.sqrt(p3x**2+p3y**2)


dP=np.sqrt((p3x-p1x)**2+(p3y-p1y)**2)

# 1d output
M=np.hypot(X1d[:,3],X1d[:,4])
ax1.contourf(xxx,yyy,p1a, cmap='viridis')
#ax1.contour(dp1a, cmap='plasma')
#ax1.quiver(Xin[:,0], Xin[:,1], X1d[:,3],X1d[:,4],M)
ax1.set_title ('1D')
#ax1.grid()


M=np.hypot(X3d[:,3],X3d[:,4])
#ax2.quiver(Xin[:,0], Xin[:,1], X3d[:,3],X3d[:,4],M)
ax2.contourf(xxx,yyy,p3a, cmap='viridis')
#ax2.contour(dp3a, cmap='plasma')
ax2.set_title ('3D')
#ax2.grid()


M=np.hypot(X3d[:,3]-X1d[:,3],X3d[:,4]-X1d[:,4])
ax3.contourf(xxx,yyy, dP, cmap='viridis')
#ax3.imshow(dP)
ax3.quiver(Xin[::5,0]*1e3, Xin[::5,1]*1e3, X3d[::5,3]-X1d[::5,3], X3d[::5,4]-X1d[::5,4],color='white')

ax3.set_xlabel (r'$x_0$ (mm)')
ax3.set_ylabel (r'$y_0$ (mm)')
plt.show()
  
