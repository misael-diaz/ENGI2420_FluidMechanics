% Fluid Mechanics                                           May 14, 2020
% ENGI 2420 FA21
% Prof. M. Diaz-Maldonado
% Revised: July 22, 2021
%
%
% Problem 1.98: Isothermal Compression
% Calculate the final pressure of air (gauge) resulting from isothermal
% compression if the final volume is equal to a third of its initial value.
%
%
% Copyright (c) 2021 Misael Diaz-Maldonado
% This file is released under the GNU General Public License as published
% by the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
%
%
% References:
% [0] B Munson, D Young, T Okiishi, and W Huebsch, Fundamentals of
%    Fluid Mechanics, 8th edition
% [1] A Gilat, MATLAB: An Introduction with Applications, 6th edition

clear
close all
clc

% Given:
% initial pressure, psi
% initial volume,   ft^3
% final volume,     ft^3

p1 = 25 + 14.7;
V1 = 1;
V2 = V1 / 3;

% Solution:
% final pressure, psi, by ideal gas law
p2 = (V1 / V2) * p1;
fprintf("Problem 1.98:\n") 
fprintf("final air pressure (gauge): %6.2f psig\n", p2 - 14.7)
