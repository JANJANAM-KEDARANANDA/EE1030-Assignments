# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# released under GNU GPL
# Point Vectors

import sys                                          # for path to external scripts
sys.path.insert(0, '/home/kedar/Documents/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# local imports (not used in the provided code)
# from line.funcs import *
# from triangle.funcs import *
# from conics.funcs import circ_gen

# Given points
data = np.genfromtxt('values.dat', delimiter='\t', names=True)
xx = data['x']
yy = data['y']
zz = data['z']

# Ensure there are at least 4 points in the data
if len(xx) < 4:
    raise ValueError("Data file must contain at least 4 points.")

# Reshape vectors to be 1D arrays
A = np.array([xx[0], yy[0], zz[0]])
B = np.array([xx[1], yy[1], zz[1]])
C = np.array([xx[2], yy[2], zz[2]])
D = np.array([xx[3], yy[3], zz[3]])
origin = np.array([0, 0, 0])

# Create a figure and a 3D Axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
ax.quiver(*origin, *A, color='r', arrow_length_ratio=0.1)  # Adjusted arrow length ratio
ax.quiver(*origin, *B, color='g', arrow_length_ratio=0.1)  # Adjusted arrow length ratio
ax.quiver(*origin, *C, color='b', arrow_length_ratio=0.1)  # Adjusted arrow length ratio
ax.quiver(*origin, *D, color='k', arrow_length_ratio=0.1)  # Adjusted arrow length ratio
ax.text(xx[0], yy[0], zz[0], 'A', color='red', fontsize=12)
ax.text(xx[1], yy[1], zz[1], 'B', color='green', fontsize=12)
ax.text(xx[2], yy[2], zz[2], 'C', color='blue', fontsize=12)
ax.text(xx[3], yy[3], zz[3], 'D', color='black', fontsize=12)

# Set limits and aspect ratio
ax.set_xlim(-10, 10)  # Adjust limits based on your data
ax.set_ylim(-10, 10)  # Adjust limits based on your data
ax.set_zlim(-10, 10)  # Adjust limits based on your data
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio for x, y, and z axes

# Set labels and title
ax.set_xlabel('$X$-Axis')
ax.set_ylabel('$Y$-Axis')
ax.set_zlabel('$Z$-Axis')

plt.grid(True)
plt.title(' ||C|| = ||A+B|| = 1', loc='right', pad=15)
plt.title(' ||D|| = ||A-B|| = √3', loc='left', pad=15)  # Changed to 'left' to avoid overlap
plt.show()

