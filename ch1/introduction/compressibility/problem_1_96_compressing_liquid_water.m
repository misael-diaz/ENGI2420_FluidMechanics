% Fluid Mechanics                                              May 07, 2020
% ENGI 2420 FA21
% Prof. M. Diaz-Maldonado
% Revised: July 22, 2021
%
%
% Problem 1.96: Compressibility.
% Determine the volume change (in percentage) that water undergoes when
% compressed. The properties of water were taken from table 1.6 of
% Munson et al., Fundamentals of Fluid Mechanics, 6th edition.
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
% bulk modulus,    MPa
% pressure change, MPa
Ev = 2.15e3;
dP = 35;

% Solution:
% volume change percentage
phi = -dP/Ev * 100;
fprintf("Problem 1.96: \n")
fprintf("volume change percentage: %6.2f %%\n", phi)
