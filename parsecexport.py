"""
Export PARSEC airfoil in plain coordinate format, for use with e.g. XFOIL.
No file saving is performed, that is left to the user.
"""


from __future__ import division
import numpy as np
import parseccoef as pc


def ppointsplain(*args, **kwargs):
    '''Alias for ppoints that returns a string with plain data format'''
    coords = ppoints(*args, **kwargs)
    # Iterate over coordinates, making a list of strings
    coordstrlist = ["{:.6f} {:.6f}".format(coord[0], coord[1])
                    for coord in coords]
    # Now join these strings with linebreaks in between
    return '\n'.join(coordstrlist)


def ppoints(cf_pre, cf_suc, npts=121, xte=1.0):
    '''
    Takes PARSEC coefficients, number of points, and returns list of
    [x,y] coordinates starting at trailing edge pressure side.
    Assumes trailing edge x position is 1.0 if not specified.
    Returns 121 points if 'npts' keyword argument not specified.
    '''
    # Using cosine spacing to concentrate points near TE and LE,
    # see http://airfoiltools.com/airfoil/naca4digit
    xpts = (1 - np.cos(np.linspace(0, 1, np.ceil(npts/2))*np.pi)) / 2
    # Take TE x-position into account
    xpts *= xte

    # Powers to raise coefficients to
    pwrs = (1/2, 3/2, 5/2, 7/2, 9/2, 11/2)
    # Make [[1,1,1,1],[2,2,2,2],...] style array
    xptsgrid = np.meshgrid(np.arange(len(pwrs)), xpts)[1]
    # Evaluate points with concise matrix calculations. One x-coordinate is
    # evaluated for every row in xptsgrid
    evalpts = lambda cf: np.sum(cf*xptsgrid**pwrs, axis=1)
    # Move into proper order: start at TE, over bottom, then top
    # Avoid leading edge pt (0,0) being included twice by slicing [1:]
    ycoords = np.append(evalpts(cf_pre)[::-1], evalpts(cf_suc)[1:])
    xcoords = np.append(xpts[::-1], xpts[1:])
    # Return 2D list of coordinates [[x,y],[x,y],...] by transposing .T
    return np.array((xcoords, ycoords)).T


def _example():
    '''Runs some examples. Underscore means it's a local function.'''
    # Sample coefficients
    rle = .01
    x_pre = .45
    y_pre = -0.006
    d2ydx2_pre = -.2
    th_pre = 2
    x_suc = .35
    y_suc = .055
    d2ydx2_suc = -.35
    th_suc = -10

    # Trailing edge x and y position
    xte = .9
    yte = -0.05

    # Evaluate pressure (lower) surface coefficients
    cf_pre = pc.pcoef(xte, yte, rle,
                      x_pre, y_pre, d2ydx2_pre, th_pre,
                      'pre')
    # Evaluate suction (upper) surface coefficients
    cf_suc = pc.pcoef(xte, yte, rle,
                      x_suc, y_suc, d2ydx2_suc, th_suc,
                      'suc')

    # Get and print plain list of coordinates
    print ppointsplain(cf_pre, cf_suc, 121, xte=xte)
    # Get list of coordinates
    pts = ppoints(cf_pre, cf_suc, 121, xte=xte)
    # Plot this airfoil, transposing pts to get list of x's and list of y's
    import matplotlib.pyplot as plt
    plt.plot(pts.T[0], pts.T[1], 'o--')
    plt.gca().axis('equal')
    plt.show()


# If this file is run, execute example
if __name__ == "__main__":
    _example()
