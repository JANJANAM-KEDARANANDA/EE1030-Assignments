#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors


import sys                                          #for path to external scripts
sys.path.insert(0, '/home/kedar/Documents/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import ctypes
from ctypes import Structure, c_double
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen


# Read values from values.dat
def read_values(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        AB = float(lines[0].split(':')[1].strip().replace('cm', ''))
        BC = float(lines[1].split(':')[1].strip().replace('cm', ''))
        angle_B = float(lines[2].split(':')[1].strip().replace('degrees', ''))
    return AB, BC, angle_B

# Call the function to read values
AB, BC, angle_B = read_values('values.dat')


# Triangle vertices computation
# Convert angleB from degrees to radians
angle_B_rad = np.radians(angle_B)

# Assume point B is at origin (0, 0)
B = np.array([0, 0])

# Assuming BC is on the x-axis, so C is at (BC, 0)
C = np.array([BC, 0])

# Calculate coordinates of A using trigonometry
A = np.array([AB * np.cos(angle_B_rad), AB * np.sin(angle_B_rad)])

# Triangle sides
a = LA.norm(B - C)
b = LA.norm(C - A)
c = LA.norm(A - B)


# Direction Vectors
def dir_vec(P1, P2):
    return P2 - P1

m1 = dir_vec(A, B)
m2 = dir_vec(B, C)
m3 = dir_vec(C, A)

# Angles
angA = np.degrees(np.arccos((-m1.T @ m3) / (b * c)))
angB = np.degrees(np.arccos((-m1.T @ m2) / (a * c)))
angC = np.degrees(np.arccos((-m2.T @ m3) / (a * b)))

# Plotting
plt.figure()

# Generating all lines
x_AB = np.linspace(A[0], B[0], 100), np.linspace(A[1], B[1], 100)
x_BC = np.linspace(B[0], C[0], 100), np.linspace(B[1], C[1], 100)
x_CA = np.linspace(C[0], A[0], 100), np.linspace(C[1], A[1], 100)

# Plot the lines
plt.plot(x_AB[0], x_AB[1], label='$AB$')
plt.plot(x_BC[0], x_BC[1], label='$BC$')
plt.plot(x_CA[0], x_CA[1], label='$CA$')

# Label the coordinates
plt.scatter([A[0], B[0], C[0]], [A[1], B[1], C[1]], color='red')
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='right')
plt.text(C[0], C[1], 'C', fontsize=12, ha='right')

# Labels and grid
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid(True)
plt.axis('equal')

plt.show()

