import numpy as np

# generate a grid beam x,y with particle at the vertex of the beam
# the particle has zero momentum


def dumpAstra(AnArray, fname):
   f=open(fname,'w')
   sh=np.shape(AnArray)
   for i in range(sh[0]):
      f.write('%.4e' %AnArray[i,0]+'\t'+'%.4e' %AnArray[i,1]+'\t'+'%.4e' %AnArray[i,2]+'\t'+ \
              '%.4e' %AnArray[i,3]+'\t'+'%.4e' %AnArray[i,4]+'\t'+'%.4e' %AnArray[i,5]+'\t'+ \
              '%.4e' %AnArray[i,6]+'\t'+'%.4e' %AnArray[i,7]+'\t'+'%d' %AnArray[i,8]+'\t'+   \
              '%d' %AnArray[i,9]+ '\n')
   f.close()
   
      
Nx=31
Ny=31
#total momentum
TotalEnergyMeV=10.
Momentum=np.sqrt(TotalEnergyMeV**2-0.511**2)*1e6
# total chage
charge=1e-9
# total numbe of particles 
N=Nx*Ny


bound=9e-3
xmin=-bound
xmax= bound
ymin=-bound
ymax= bound


dx= (xmax-xmin)/(Nx-1)
dy= (ymax-ymin)/(Ny-1)

v=np.array([0.,0.,0.,0.,0.,Momentum])

for i in range (Nx):
  for j in range (Ny):
     xloc=xmin+i*dx
     yloc=ymin+j*dy
     a=np.array([xloc, yloc, 0., 0., 0., 0.])
#     print '**      ', a 
#     v=np.concatenate((v,a), axis=0)
     v=np.vstack((v,a))
 
print (v[0,:])

ASTRAFLAG=np.ones((N+1,4),dtype=object)
# time
ASTRAFLAG[:,0]=np.ones((N+1))*0
# charge per macro
ASTRAFLAG[:,1]=np.ones((N+1))*charge/(float(N))
# flag 1
ASTRAFLAG[:,2]=int(1)
# flag 2
ASTRAFLAG[:,3]=int(5)

AstraArray=np.hstack((v,ASTRAFLAG))


print (np.shape(AstraArray))
print ('-------------------')
print (AstraArray)
print ('-------------------')


dumpAstra(AstraArray,"grid_distrib.ini")
