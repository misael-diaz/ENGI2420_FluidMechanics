#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fluid Mechanics                                               July 21, 2021
ENGI 2420 FA21  
Prof. M. Diaz-Maldonado


Problem 1.46: Ideal Gas Law
Estimate the density of Mar's atmosphere via the ideal gas law by
assuming that the atmosphere is composed of pure carbon dioxide (CO2).


Copyright (c) 2021 Misael Diaz-Maldonado

This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""


"""
Given:
Mar's atmospheric conditions:
molecular weight of CO2,    kg/mol
ideal gas constant,         J / (mol K)
pressure,                   Pa
temperature,                K
"""

MW = 44.0e-3
R  =  8.314
P  =  900.0
T  = -50 + 273.15

"""
Solution:
density of Mar's atmosphere, kg/m^3, by the ideal gas law
"""

rho_Mars = MW * P / (R * T)

"""
Given:
Earth's atmospheric conditions:
molecular weight of air,    kg/mol
pressure,                   Pa
temperature,                K
"""

MW = 28.9e-3
P  = 101.6e3
T  = 18 + 273.15

"""
Solution:
density of Earth's atmosphere, kg/m^3
"""

rho_Earth = MW * P / (R * T)


ans = (f"Problem 1.46:\n"
       f"density of Mar's atmosphere:   {rho_Mars: {6}.{4}} kg/m^3\n"
       f"density of Earth's atmosphere: {rho_Earth:{6}.{4}} kg/m^3\n"
       f"Earth's to Mar's atmosphere density ratio: {rho_Earth/rho_Mars}\n"
)
print(ans)
