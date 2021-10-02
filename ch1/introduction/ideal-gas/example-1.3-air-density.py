#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fluid Mechanics                                               July 21, 2021
ENGI 2420 FA21
Prof. M. Diaz-Maldonado

Example 1.3: Ideal Gas Law
Determine the density of compressed air.


Copyright (c) 2021 Misael Diaz-Maldonado

This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] B Munson, D Young, T Okiishi, and W Huebsch, Fundamentals of
    Fluid Mechanics, 8th edition
[1] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition
"""


"""
Given:
gc constant,                ft lbm/(lbf s^2)
acceleration of gravity,    ft/s^2
ideal gas constant,         lbf ft / (lbmol R)
molecular weight of air,    lbm/lbmol
absolute pressure,          psi (lbf/in^2)
temperature, Rankine,       R
volume, cubic feet,         ft^3
"""

gc = 32.174
g  = 32.174
R  = 1545
MW = 28.9
P  = 50 + 14.7      # gauge plus atmospheric pressure
T  = 70 + 459.67
V  = 0.84

"""
Solution:
density by ideal gas law,  lbm / ft^3
weight,                    lbf
"""

rho = MW * P / (R * T) * 144
W   = rho * g/gc * V

ans = (f"\n\nExample 1.3: Density of Compressed Air\n"
       f"density: {rho/gc:{6}.{4}} slug/ft^3 \t ({rho:{5}.{4}} lbm/ft^3)\n"
       f"weight:  {W:{6}.{4}} lbf\n"
)

print(ans)

"""
Used Conversions:
1 squared feet = 144 squared inches
1 slug         = 32.174 lbm
"""
