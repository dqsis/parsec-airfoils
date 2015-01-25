# Generate and plot the contour of an airfoil 
# using the PARSEC parameterization

# Repository & documentation:
# http://github.com/dqsis/parsec-airfoils
# -------------------------------------


# Import libraries
from __future__ import division
import os

import numpy as np
import matplotlib.pyplot as plt

import parseccoef as pc
import parsecexport


# I/O files path
path = 'data/'


# Read parsec parameters (user input) & assign to array
pp = 'parsec_parameters.csv'
pparray = np.genfromtxt(os.path.join(path,pp), delimiter=';', 
                        dtype = float, skiprows=1)


# TE & LE of airfoil (normalized, chord = 1)
xle = 0.0
yle = 0.0
xte = 1.0
yte = 0.0

# LE radius
rle = pparray[0]

# Pressure (lower) surface parameters 
x_pre = pparray[1]
y_pre = pparray[2]
d2ydx2_pre = pparray[3]
th_pre = pparray[4]

# Suction (upper) surface parameters
x_suc = pparray[5]
y_suc = pparray[6]
d2ydx2_suc = pparray[7]
th_suc = pparray[8]


# Evaluate pressure (lower) surface coefficients
cf_pre = pc.pcoef(xte,yte,rle,
                  x_pre,y_pre,d2ydx2_pre,th_pre,
                  'pre')

# Evaluate suction (upper) surface coefficients
cf_suc = pc.pcoef(xte,yte,rle,
                  x_suc,y_suc,d2ydx2_suc,th_suc,
                  'suc')


# Evaluate pressure (lower) surface points
xx_pre = np.linspace(xte,xle,101)
yy_pre = (cf_pre[0]*xx_pre**(1/2) + 
          cf_pre[1]*xx_pre**(3/2) + 
          cf_pre[2]*xx_pre**(5/2) + 
          cf_pre[3]*xx_pre**(7/2) + 
          cf_pre[4]*xx_pre**(9/2) + 
          cf_pre[5]*xx_pre**(11/2)
         ) 

# Evaluate suction (upper) surface points
xx_suc = np.linspace(xle,xte,101)
yy_suc = (cf_suc[0]*xx_suc**(1/2) + 
          cf_suc[1]*xx_suc**(3/2) + 
          cf_suc[2]*xx_suc**(5/2) + 
          cf_suc[3]*xx_suc**(7/2) + 
          cf_suc[4]*xx_suc**(9/2) + 
          cf_suc[5]*xx_suc**(11/2)
         )

# Use parsecexport to save coordinate file
fpath = os.path.join(path, 'parsec_airfoil.dat')
# with ... as ... executes the block, then closes file
with open(fpath, 'w') as f:
    plain_coords = parsecexport.ppointsplain(cf_pre, cf_suc, 121, xte=xte)
    f.write(plain_coords)
         
# Plot airfoil contour
plt.figure()

plt.plot(xx_suc,yy_suc,'ro--',
         xx_pre,yy_pre,'bo--'
        )

plt.grid(True)
plt.xlim([0,1])
plt.yticks([])
plt.xticks(np.arange(0,1.1,0.1))

# Show & save graphs
plt.show()

plt.savefig(os.path.join(path,'parsec_airfoil.pdf'))
plt.savefig(os.path.join(path,'parsec_airfoil.png'))
