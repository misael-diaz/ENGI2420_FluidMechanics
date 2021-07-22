#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fluid Mechanics                                              March 23, 2020
ENGI 2420 FA21  
Prof. M. Diaz-Maldonado
Revised: July 22, 2021


Problem 1.87: Rotating cylinder viscometer.  
Fit experimental data to obtain the viscosity of the liquid.


Copyright (c) 2021 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] B Munson, D Young, T Okiishi, and W Huebsch, Fundamentals of 
    Fluid Mechanics, 8th edition
[1] A Gilat, MATLAB: An Introduction with Applications, 6th edition
[2] A Gilat and V Subramanian, Numerical Methods for Engineers and 
    Scientists: An Introduction with Applications using MATLAB
[3] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition
[4] numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
"""


import numpy as np
from numpy import pi
import matplotlib as mpl
mpl.use("qt5agg")
import matplotlib.pyplot as plt
from scipy import linalg as la


"""
Experimental data
angular velocity, rad/s
torque,           lbf ft
"""
omega  = np.linspace(1, 6, 6) 
torque = np.array([13.1, 26, 39.5, 52.7, 64.9, 78.6])

# obtains the linear fit via least squares
A = np.vstack([omega**n for n in range(2)])
sol, r, rank, sv = la.lstsq(A.T, torque)

"""
Results
torque - angular speed plot
Newtonian viscosity from the slope of the fitted line
"""

# samples linear model for plotting
w = np.linspace(1, 6, 100)
torque_fit = sum([s * w**n for n, s in enumerate(sol)])

plt.close('all')
plt.ion()
fig, ax = plt.subplots()
ax.plot(omega, torque, 'o', color='red', label='exp')
ax.plot(w, torque_fit, color='black', linewidth=2, linestyle='--',
        label='fit')
ax.set_xlabel("angular speed, rad/s")
ax.set_ylabel("torque, lbf ft")
ax.legend(loc='upper left')


"""
Given:
Rheometer dimensions:
inner radius, ft
outer radius, ft
lenght,       ft
"""
Ri = 2.45 / 12
Ro = 2.50 / 12
L  = 5.00 / 12

s = sol[1]  # slope
""" Newtonian viscosity """
mu = s * ( (Ro - Ri) / Ri ) / (2 * pi * Ri**2 * L)
ans = f"viscosity: {mu} lbf s / ft^2"
print(ans)




"""
Comments (Theory)
Torque - angular velocity relationship for a concentric rheometer:

      T = 2 * pi * mu * Ri**2 * L * Ri / (Ro - Ri) * omega

By applying the linear fit to the theoretical model we can infer
that the slope is given by:   2 * pi * mu * Ri**2 * L * Ri / (Ro - Ri).

Solving for the viscosity, mu, yields the sought formula:

      mu = slope * (Ro - Ri) / Ri / (2 * pi * Ri**2 * L)

"""




"""
TODO:
    [x] Add references
    [x] Check units from problem statement
    [x] Indicate the units of the viscosity
    [x] Show axes labels (with units)
    [ ] Show the correlation coefficient for this fit, compare against
        the computed one (spreadsheet)
"""
