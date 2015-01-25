parsecairfoils.py
=================


What is it
----------
`parsecairfoils.py` is a python script that generates, plots, and exports the contour of an airfoil using the *PARSEC* parameterization. 

PARSEC is a common method for airfoil parameterization. 
It has the advantange of strict control over important aerodynamic features, and it allows independent control over the airfoil geometry by imposing shape constraints. 
More on the PARSEC parameterization can be found in the following article:
[H. Sobieczky, *'Parametric airfoils and wings'* in *Notes on Numerical Fluid Mechanics*, Vol. 68, pp 71-88](www.as.dlr.de/hs/h-pdf/H141.pdf) 


Main features
-------------

The script, using as input data the following *11* airfoil geometric characteristics:

* leading edge radius (r_LE)
* pressure and suction surface crest locations (x_pre, y_pre, x_suc, y_suc)
* curvatures at the pressure and suction surface crest locations (d2y/dx2_pre, d2y/dx2_suc)
* trailing edge coordinates (x_TE, y_TE)
* trailing edge angles between the pressure and suction surface and the horizontal axis (th_pre, th_suc)

Generates and plots the contour of an airfoil - as shown in [this example](https://github.com/dqsis/parsec-airfoils/blob/master/data/parsec_airfoil.png). 
Is also able to export the airfoil's coordinates, as shown in [this plain coordinate file](https://github.com/dqsis/parsec-airfoils/blob/master/data/parsec_airfoil.dat).


Where to get it
---------------

The source code is hosted on GitHub at: [http://github.com/dqsis/parsec-airfoils](http://github.com/dqsis/parsec-airfoils).


Dependencies
------------

* [NumPy](http://www.numpy.org) - for array objects and mathematical operations
* [matplotlib](http://matplotlib.org) - for plots


Documentation
-------------

The only input required by `parsecairfoils.py` are the 11 PARSEC parameters (found in the file [data/parsec_parameters.csv](http://github.com/dqsis/parsec-airfoils/blob/master/data/parsec_parameters.csv)).
Note that `parsecairfoils.py` uses additionally the module `parseccoef.py` which contains the user function *pcoef*. 
`pcoef` formulates and solves the system that generates the coefficients of the PARSEC polynomial.  


Discussion and development
--------------------------

Currently, the script is considered complete. No additional development ideas. 


Licence
-------

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US).


Contact
-------

[Mail](http://dqsis.com/contact/)

[Twitter (@dqsis)](http://twitter.com/dqsis)
