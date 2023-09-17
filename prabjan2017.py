import numpy as np
import time
import os
from matplotlib import pyplot as plt
import HFSStool
import pydefault24 

#
# this file should be ran after seeField.py was ran (with LOADFIL=1)
#

# parameter from Andrei Lunin's simulations
Nx=41
Ny=41
Nz=1396

Ex_para = np.zeros((Nx, Ny, Nz))
Ey_para = np.zeros((Nx, Ny, Nz))


for j in range(Nz-1):
   for i in range(Nx):
      if j>1:
         Ex_para[i,:,j]=+0.5*x[i,:,j-1]*dEzdz[j-1]
         Ey_para[i,:,j]=+0.5*y[i,:,j-1]*dEzdz[j-1]

#dE_t = np.sqrt(dEx**2+dEy**2)
E_t     = np.sqrt(reEx**2+reEy**2)
Et_para = np.sqrt(Ex_para**2+Ey_para**2)


Zslice=100 

#plt.subplot (2,2,3)
#plt.imshow(E_t[:,:,Zslice].T-Et_para[:,:,Zslice].T,aspect='auto',origin='lower', cmap='seismic')
#plt.colorbar()


cms=299798492.0

#if PLOT==1:
normalization=np.max(reEz[20,20,:])
nEz=reEz[20,20,:]/normalization
plt.subplot(2,1,1)
plt.plot(z[20,20,:], nEz,'-', lw=2)
plt.xlim(-.7,0.7)
plt.ylim(-1.1,1.1)
plt.xlabel(r'$z$ (mm)')
plt.ylabel(r'$E_z/E_0$')


plt.subplot(2,1,2)
plt.plot(z[20,20,:], reEx[20,20,:]/normalization,'b-', lw=2, label=r'${\cal R}e(E_x)$')
plt.plot(z[20,20,:], reEy[20,20,:]/normalization,'r-', lw=2, label=r'${\cal R}e(E_y)$')
plt.plot(z[20,20,:], cms*imBx[20,20,:]/normalization,'b--', lw=2, label=r'${\cal I}m(cB_x)$')
plt.plot(z[20,20,:], cms*imBy[20,20,:]/normalization,'r--', lw=2, label=r'${\cal I}m(cB_y)$')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlim(-.7,.7)
plt.ylim(-1.1e-3,1.1e-3)
#plt.tight_layout(pad=0.8, w_pad=0.0, h_pad=0.1)
plt.tight_layout(h_pad=0.0)
plt.xlabel(r'$z$ (mm)')
plt.ylabel(r'[$E_{x,y}$ \& $cB_{x,y}]/E_0$')
#plt.plot(z[20,20,:], imEz[20,20,:],'--')
#plt.show()
#plt.imshow(reEz[:,20,:],aspect='auto',cmap='seismic')
plt.legend(loc='center', fontsize='18')
plt.show()

