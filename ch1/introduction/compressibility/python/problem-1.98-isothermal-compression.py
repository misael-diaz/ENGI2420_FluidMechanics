#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fluid Mechanics                                            October 02, 2021
ENGI 2420 FA21
Prof. M. Diaz-Maldonado


Problem 1.98: Isothermal Compression
Calculate the final pressure of air (gauge) resulting from isothermal
compression if the final volume is equal to a third of its initial value.


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
p1 = 25 + 14.7      # initial pressure, psi
V1 = 1              # initial volume,   ft^3
V2 = V1 / 3         # final volume,     ft^3

"""
Solution:
obtains final pressure (in psi gauge) by applying the ideal gas law
"""
p2 = (V1 / V2) * p1

ans = (
    f"\n\nProblem 1.98: Isothermal Compression of an Ideal Gas\n"
    f"final air pressure (gauge): {(p2 - 14.7):6.2f} psig\n"
)
print(ans)
