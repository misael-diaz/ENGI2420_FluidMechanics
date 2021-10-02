#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fluid Mechanics                                              May 07, 2020
ENGI 2420 FA21
Prof. M. Diaz-Maldonado
Revised: July 25, 2021


Problem 1.95: Compressibility
Determine the pressure change to compress a volume of mercury
by 0.1 %. Properties of mercury are taken from table 1.5 from
the 6th edition of Munson et al., Fundamentals of Fluid Mechanics.


Copyright (c) 2021 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] B Munson, D Young, T Okiishi, and W Huebsch, Fundamentals of
   Fluid Mechanics, 8th edition.
[1] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition.
"""

"""
Given:
"""
Ev = 4.14e6     # bulk modulus, psi
phi = -0.1e-2   # volume change fraction (non-dimensional)

# Solution:
dp = -Ev * phi

ans = (
    f"\n\nProblem 1.95: Compressing Mercury\n"
    f"pressure change: {dp:6.2f} psi\n"
)
print(ans)
