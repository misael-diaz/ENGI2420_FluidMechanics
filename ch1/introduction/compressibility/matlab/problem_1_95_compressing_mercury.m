% Fluid Mechanics                                              May 07, 2020
% ENGI 2420 FA21  
% Prof. M. Diaz-Maldonado
% Revised: July 25, 2021
%
%
% Problem 1.95: Compressibility
% Determine the pressure change to compress a volume of mercury
% by 0.1 %. Properties of mercury are taken from table 1.5 from
% the 6th edition of Munson et al., Fundamentals of Fluid Mechanics.
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
% bulk modulus, psi
% volume change
Ev = 4.14e6;
phi = -0.1e-2; 

% Solution:
dp = -Ev * phi;
fprintf("Problem 1.95: \n") 
fprintf("pressure change: %6.2f psi\n", dp)
