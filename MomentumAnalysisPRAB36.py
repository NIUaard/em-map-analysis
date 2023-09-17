'''
  This script analyze the coupler kick in term of conventional 
     moments strength (dipole, quadrupole and solenoidal 
     
  here I fit P=d+M*X,
  
  where d is 2x1 and M is 2x2 matrix
  
  from M one gets the values of the focusing strengths
  
'''

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.gridspec as gridspec
from matplotlib import ticker
import matplotlib.cm as cm
import matplotlib.ticker as ticker

def lin_regr_2d (y, x1, x2):
  x=[x1, x2]
  X = np.column_stack(x+[[1]*len(x[0])])
#  print X
  beta_hat = np.linalg.lstsq(X,y)[0]
  fit= beta_hat
  res= np.dot(X,beta_hat)
  return(fit)


Phi=np.linspace(-100,100, 41)

m11=np.zeros((len(Phi)))
m12=np.zeros((len(Phi)))
dx=np.zeros((len(Phi)))
m21=np.zeros((len(Phi)))
m22=np.zeros((len(Phi)))
dy=np.zeros((len(Phi)))
nrj=np.zeros((len(Phi)))
for i in range(len(Phi)):
   rund=i+1
   run="%03d" % rund
   fname='9-cell3D.0140.'+run
   Xin=np.loadtxt('grid_distrib.ini')
   X3d=np.loadtxt(fname)

    
   Xin[:,0]*=1e3
   Xin[:,1]*=1e3

#-------------------------------------
   xin = Xin[1:,0]
   yin = Xin[1:,1]
   px3d= X3d[1:,3]
   py3d= X3d[1:,4]
   p3d=np.sqrt(px3d**2+py3d**2)
   print(np.mean(p3d))
#-------------------------------------

   respx3d=lin_regr_2d(px3d, xin, yin)
   m11[i]=respx3d[0]
   m12[i]=respx3d[1]
   dx[i]=respx3d[2]
   respy3d=lin_regr_2d(py3d, xin, yin)
   m21[i]=respy3d[0]
   m22[i]=respy3d[1]
   dy[i]=respy3d[2]
   nrj[i]=X3d[0,5]-Xin[0,5]

# dipole terms
dx=dx
dy=dy
# ponderomotive terms
p=(m11+m22)/2.
# quadrupole terms
q=(m11-m22)/2.
# skew quadrupole terms
sk=(m12+m21)/2.
# solenoidal terms
s=(m12-m21)/2.

fig=plt.figure(9999)
gs1 = gridspec.GridSpec(2, 2)
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])
ax3 = fig.add_subplot(gs1[2])
ax4 = fig.add_subplot(gs1[3])
gs1.update(top=0.95,bottom=0.150, left=0.15, right=0.95, hspace=0.4, wspace=0.4)

#plt.figure()
#plt.plot (Phi,m11,'o--',label='m11')
#plt.plot (Phi,m12,'s--',label='m12')
#plt.plot (Phi,dx,'x--',label='dx')
#plt.plot (Phi,m21,'o:',label='m21')
#plt.plot (Phi,m22,'s:',label='m22')
#plt.plot (Phi,dy,'x:',label='dy')
#plt.legend()
#plt.figure

ax1.plot (Phi,nrj*1e-6,'-',label='q')
ax1.set_xlabel (r'$\phi$ (deg)', fontsize=22)
ax1.set_ylabel (r'energy gain (MeV)', fontsize=22)
ax1.text (65,12,r'{\bf (a)}', fontsize=28)
start, end = ax1.get_xlim()
ax1.xaxis.set_ticks(np.arange(-90, end, 90.))
ax1.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
start, end = ax1.get_ylim()
ax1.yaxis.set_ticks(np.arange(0, end, 5.))

ax2.plot (Phi,dx*1e-3,'-',label=r'$d_x$')
ax2.plot (Phi,dy*1e-3,'--',label=r'$d_y$')
ax2.set_xlabel (r'$\phi$ (deg)', fontsize=22)
ax2.set_ylabel (r'dipole kick (keV/c)', fontsize=22)
ax2.text (65,0.2,r'{\bf (b)}', fontsize=28)
ax2.legend(fontsize=14,loc=3)
start, end = ax2.get_xlim()
ax2.xaxis.set_ticks(np.arange(-90, end, 90.))
ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
start, end = ax2.get_ylim()
ax2.yaxis.set_ticks(np.arange(-2, end, 1.))

ax3.plot (Phi,q*1e-3, '-',label=r'$k_q$')
ax3.plot (Phi,sk*1e-3,'--',label=r'$k_{sk}$')
ax3.plot (Phi,s*1e-3, ':',label=r'$k_s$')
ax3.set_xlabel (r'$\phi$ (deg)', fontsize=22)
ax3.set_ylabel (r'focusing (keV/(c$\cdot$m))', fontsize=22)
ax3.legend(fontsize=14,loc=2)
ax3.text (65,0.08,r'{\bf (c)}', fontsize=28)
start, end = ax3.get_xlim()
ax3.xaxis.set_ticks(np.arange(-90, end, 90.))
ax3.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))


ax4.plot (Phi,q/p*100., '-',label=r'$k_q/k_p$')
ax4.plot (Phi,sk/p*100.,'--',label=r'$k_{sk}/k_p$')
ax4.plot (Phi,s/p*100., ':',label=r'$k_s/k_p$')
ax4.set_xlabel (r'$\phi$ (deg)', fontsize=22)
ax4.set_ylabel (r'relative focusing (\%)', fontsize=22)
ax4.text (65,0.27,r'{\bf (d)}', fontsize=28)
start, end = ax4.get_xlim()
ax4.xaxis.set_ticks(np.arange(-90, end, 90.))
ax4.xaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
start, end = ax4.get_ylim()
ax4.yaxis.set_ticks(np.arange(-2, end, 1.))
#ax4.yaxis.set_major_formatter(ticker.FormatStrFormatter('f'))
plt.legend(fontsize=14, loc=10)
plt.show()


