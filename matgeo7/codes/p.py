#Code by GVV Sharma
#September 12, 2023
#Revised July 21, 2024
#released under GNU GPL
#Point Vectors

import sys                                          #for path to external scripts
sys.path.insert(0, '/home/kedar/Documents/matgeo/codes/CoordGeo')        #path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

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
angle_B_rad = np.radians(angle_B)

# Assume point B is at origin (0, 0)
B = np.array([0, 0])

# Assuming BC is on the x-axis, so C is at (BC, 0)
C = np.array([BC, 0])

# Calculate coordinates of A using trigonometry
A = np.array([AB * np.cos(angle_B_rad), AB * np.sin(angle_B_rad)])

# Calculate lengths of the sides
a = LA.norm(B - C)  # Length BC
b = LA.norm(C - A)  # Length CA
c = LA.norm(A - B)  # Length AB

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

# Calculate AC length
AC = LA.norm(A - C)

# Update legend to show calculated side lengths
plt.legend([
    f'Side AB = {c:.2f} cm',  # Length AB
    f'Side BC = {a:.2f} cm',  # Length BC
    f'Side AC = {b:.2f} cm'   # Length AC
], loc='upper right')

# Labels and grid
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.axis('equal')

plt.show()

