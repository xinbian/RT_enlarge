# -*- coding: utf-8 -*-
"""
extend RT domain
@author: Xin
"""

import h5py
import numpy as np
import pylab
import matplotlib.pyplot as plt

nx=2
ny=256
nz=1024
gamma=0.8
rhoL=1
rhoH=1.0833
dz=3.2/nz

#nz enlarge only 
variable = ['PVx','PVy','PVz','PPress', 'Prho']
h5file = h5py.File('tests_single.h5','r')
h5new = h5py.File('tests_single_large.h5','w-')

step=['070000','080000','090000']

for istep in step:
  #Vx
  m1=np.zeros((2*nz, ny, nx))
   
  #Vy
  delimiter = ''
  mylist = ['Fields/',variable[1],'/',istep]
  filepath = delimiter.join(mylist)
  databk = h5file.get(filepath)
  m1 = np.array(databk)
  m1=np_data

  m2=np.zeros((2*nz, ny, nx))
  m2[nz/2-1:3*nz/2, ny, nx]=m1
  h5new.create_dataset(filepath,data=m2)

  #Vz
  delimiter = ''
  mylist = ['Fields/',variable[2],'/',istep]
  filepath = delimiter.join(mylist)
  databk = h5file.get(filepath)
  m1 = np.array(databk)
  m1=np_data

  m2=np.zeros((2*nz, ny, nx))
  m2[nz/2-1:3*nz/2, ny, nx]=m1
  h5new.create_dataset(filepath,data=m2)

  #pressure

  delimiter = ''
  mylist = ['Fields/',variable[3],'/',istep]
  filepath = delimiter.join(mylist)
  databk = h5file.get(filepath)
  m1 = np.array(databk)
  m1=np_data

  m2=np.zeros((2*nz, ny, nx))

  #largest mean pressure at lowest point  
  pressLarge=np.mean(m1[0,:,:])
  #smallest mean pressure at highest point
  pressHigh=np.mean(m1[nz,:,:])
  m2[nz/2-1:3*nz/2, ny, nx]=m1

  for i in range(nz/2):

    m2[i]=pressLarge+rhoL*g*dz*(nz/2-i)
    m2[2*nz-i-1]=pressHigh-rhoH*g*dz*(nz/2-i)
  h5new.create_dataset(filepath,data=m2)



  #rho
  delimiter = ''
  mylist = ['Fields/',variable[4],'/',istep]
  filepath = delimiter.join(mylist)
  databk = h5file.get(filepath)
  m1 = np.array(databk)
  m1=np_data

  m2=np.zeros((2*nz, ny, nx))
  m2[nz/2-1:3*nz/2, ny, nx]=m1
  h5new.create_dataset(filepath,data=m2)

h5file.close()
h5new.close()

#f = open('output.d','w')
#for zz_ref in range(nz):
# f.write("%4s\t%10s\n" % (zz_ref, np.mean(m1[zz_ref,:,:])))
#f.close()
    
    
    
