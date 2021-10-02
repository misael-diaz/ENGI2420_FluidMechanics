#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fluid Mechanics                                            October 02, 2021
ENGI 2420 FA21
Prof. M. Diaz-Maldonado


Problem 1.96: Compressing Liquid Water.
Determines the volume change (in percentage) that water undergoes when
compressed. The properties of water were taken from table 1.6 of
Munson et al., Fundamentals of Fluid Mechanics, 6th edition.


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
Ev = 2.15e3 # bulk modulus,    MPa
dP = 35     # pressure change, MPa

"""
Solution:
"""
phi = -dP / Ev * 100    # volume change (percentage)

ans = (
    f"\n\nProblem 1.96: Compressing Liquid Water\n"
    f"volume change percentage: {phi:6.2f} %\n"
)

print(ans)
