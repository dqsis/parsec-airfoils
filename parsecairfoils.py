# title: 
# parsec airfoils

# purpose:
# 

# repository:
# http://github.com/dqsis/xxx

# -------------------------------------

# START +++

# import libraries
from __future__ import division
import os
from sys import exit

import numpy as np
import matplotlib.pyplot as plt

import parseccoef as pc

# i/o files path
path = 'data/'

# read PARSEC parameters
pp = 'parsec_parameters.csv'
pparray = np.genfromtxt(os.path.join(path,pp), delimiter=';', dtype = float, skiprows=1)

# 'normalized' airfoil (chord = 1)
xle = 0.0
yle = 0.0
xte = 1.0
yte = 0.0

# leading edge
rle = pparray[0]

# pressure side (down)
x_pre = pparray[1]
y_pre = pparray[2]
d2ydx2_pre = pparray[3]
th_pre = pparray[4]

# suction side (up)
x_suc = pparray[5]
y_suc = pparray[6]
d2ydx2_suc = pparray[7]
th_suc = pparray[8]

# evaluate pressure (lower) surface parsec coefficients
cf_pre = pc.pcoef(xte,yte,rle,
                  x_pre,y_pre,d2ydx2_pre,th_pre,
                  'pre')

# evaluate suction (upper) surface parsec coefficients
cf_suc = pc.pcoef(xte,yte,rle,
                  x_suc,y_suc,d2ydx2_suc,th_suc,
                  'suc')

# pressure (lower) surface points
xx_pre = np.linspace(xte,xle,101)
yy_pre = (cf_pre[0]*xx_pre**(1/2) + 
          cf_pre[1]*xx_pre**(3/2) + 
          cf_pre[2]*xx_pre**(5/2) + 
          cf_pre[3]*xx_pre**(7/2) + 
          cf_pre[4]*xx_pre**(9/2) + 
          cf_pre[5]*xx_pre**(11/2) 
         ) 
         

# suction (upper) surface points
xx_suc = np.linspace(xle,xte,101)
yy_suc = (cf_suc[0]*xx_suc**(1/2) + 
          cf_suc[1]*xx_suc**(3/2) + 
          cf_suc[2]*xx_suc**(5/2) + 
          cf_suc[3]*xx_suc**(7/2) + 
          cf_suc[4]*xx_suc**(9/2) + 
          cf_suc[5]*xx_suc**(11/2)
         ) 
         
# plots
plt.figure()

# age vs weight
plt.plot(\
xx_suc,yy_suc,'r--',
xx_pre,yy_pre,'b--')

plt.grid(True)
plt.xlim([0,1])

# show graphs
plt.show()

plt.savefig(os.path.join(path,'parsec_airfoil.pdf'))
plt.savefig(os.path.join(path,'parsec_airfoil.png'))

# END +++
