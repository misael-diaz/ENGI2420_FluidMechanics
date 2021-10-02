#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fluid Mechanics                                               July 21, 2021
ENGI 2420 FA21
Prof. M. Diaz-Maldonado


Problem 1.47: Ideal Gas Law
Determine the molecular weight and "identity" of the unknown gas.


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
volume, cubic feet,         ft^3
ideal gas constant,         lbf ft / (lbmol R)
mass of gas,                lbm
pressure,                   psi (lbf/in^2)
temperature, Rankine,       R
"""

V  = 2
R  = 1545
m  = 0.30
P  = 12 + 14.7
T  = 80 + 459.67

"""
Solution:
molecular weight of air,    lbm/lbmol
"""
MW = m *  (R * T) / (P * V * 144)    # from ideal gas law

ans = (
    f"\n\nProblem 1.47: Unknown Gas\n"
    f"molecular weight:        {MW:{6}.{4}} lbm/lbmol\n"
    f"identity:                 molecular oxygen, O2\n"
)
print(ans)
