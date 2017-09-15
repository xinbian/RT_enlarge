# -*- coding: utf-8 -*-
"""
extend RT domain
@author: Xin
"""

import h5py
import numpy as np
import os.path


current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]

gamma=0.8
rhoL=1
rhoH=1.0833
g=1.0

mylist = [parent_directory,'/','temp.h5']
delimiter = ''
filepath = delimiter.join(mylist)
#nz enlarge only 
variable = ['PVx','PVy','PVz','PPress', 'Prho']
h5file = h5py.File('temp.h5','r')
mylist = [parent_directory,'/','tests_single_large.h5']
delimiter = ''
filepath = delimiter.join(mylist)
h5new = h5py.File('tests_single_new.h5','w')

istep='001000'
#read dataset dimensions
mylist = ['Fields/','Prho','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)
nz=m1.shape[0]
ny=m1.shape[1]
nx=m1.shape[2]
dz=3.2/nz



#Vx
m2=np.zeros((2*nz, ny, nx))
delimiter = ''
mylist = ['Fields/',variable[0],'/',istep]
filepath = delimiter.join(mylist)
h5new.create_dataset(filepath,data=m2)
 
#Vy
delimiter = ''
mylist = ['Fields/',variable[1],'/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)

m2=np.zeros((2*nz, ny, nx))
m2[nz/2:3*nz/2, :, :]=m1[0:nz, :, :]
h5new.create_dataset(filepath,data=m2)

#Vz
delimiter = ''
mylist = ['Fields/',variable[2],'/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)


m2=np.zeros((2*nz, ny, nx))
m2[nz/2:3*nz/2, :, :]=m1[0:nz, :, :]
h5new.create_dataset(filepath,data=m2)

#rho
delimiter = ''
mylist = ['Fields/',variable[4],'/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)


#calculate density 40 grid points away from bottom and top
rhoL=np.mean(m1[0+40,:,:])
rhoH=np.mean(m1[nz-1-40,:,:])

m2=np.zeros((2*nz, ny, nx))
m2[nz/2:3*nz/2, :, :]=m1[0:nz, :, :]
m2[0:nz/2+40, :, :]=rhoL
m2[3*nz/2-40:2*nz, :, :]=rhoH
h5new.create_dataset(filepath,data=m2)


#pressure

delimiter = ''
mylist = ['Fields/',variable[3],'/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)
m2=np.zeros((2*nz, ny, nx))
#also calcualte 40 grid points away
#largest mean pressure at lowest point  
pressLarge=np.mean(m1[0+40,:,:])
#smallest mean pressure at highest point
pressSmall=np.mean(m1[nz-1-40,:,:])
m2[nz/2:3*nz/2, :, :]=m1[0:nz, :, :]

for i in range(nz/2+40):
  m2[i]=pressLarge+rhoL*g*dz*(nz/2+40-i)
  m2[2*nz-i-1]=pressSmall-rhoH*g*dz*(nz/2+40-i)
h5new.create_dataset(filepath,data=m2)




h5file.close()
h5new.close()

#f = open('output.d','w')
#for zz_ref in range(nz):
# f.write("%4s\t%10s\n" % (zz_ref, np.mean(m1[zz_ref,:,:])))
#f.close()
    
    
    
