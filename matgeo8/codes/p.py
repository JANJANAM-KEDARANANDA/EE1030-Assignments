# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# Released under GNU GPL
# Point Vectors

import sys                                          # for path to external scripts
sys.path.insert(0, '/home/kedar/Documents/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import numpy.linalg as LA
import matplotlib.pyplot as plt

# Function to read values from values.txt
def read_values(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        side_length = float(lines[0].split(':')[1].strip().replace('cm', ''))
        angle_A = float(lines[1].split(':')[1].strip().replace('degrees', ''))
    return side_length, angle_A

# Read side length and angle from the txt file
side_length, angle_A = read_values('values.txt')  # Updated to read from values.txt

# Calculate the coordinates of the vertices of the rhombus
angle_A_rad = np.radians(angle_A)

# Assume point A is at the origin (0, 0)
A = np.array([0, 0])

# Calculate coordinates of B
B = np.array([side_length * np.cos(angle_A_rad), side_length * np.sin(angle_A_rad)])

# Calculate coordinates of C
C = np.array([B[0] + side_length * np.cos(np.pi - angle_A_rad),
              B[1] + side_length * np.sin(np.pi - angle_A_rad)])

# Calculate coordinates of D
D = np.array([A[0] + side_length * np.cos(np.pi - angle_A_rad),
              A[1] + side_length * np.sin(np.pi - angle_A_rad)])

# Plotting the rhombus
plt.figure(figsize=(8, 8))

# Plot the edges of the rhombus
plt.plot([A[0], B[0]], [A[1], B[1]], label='AB')
plt.plot([B[0], C[0]], [B[1], C[1]], label='BC')
plt.plot([C[0], D[0]], [C[1], D[1]], label='CD')
plt.plot([D[0], A[0]], [D[1], A[1]], label='DA')

# Scatter plot for the vertices
plt.scatter([A[0], B[0], C[0], D[0]], [A[1], B[1], C[1], D[1]], color='red')
plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
plt.text(B[0], B[1], 'B', fontsize=12, ha='left')
plt.text(C[0], C[1], 'C', fontsize=12, ha='left')
plt.text(D[0], D[1], 'D', fontsize=12, ha='right')

# Set the legend to show side lengths
plt.legend([
    f'Side AB = {side_length:.2f} cm',  
    f'Side BC = {side_length:.2f} cm',  
    f'Side CD = {side_length:.2f} cm',
    f'Side DA = {side_length:.2f} cm'
], loc='upper right')

# Labels and grid
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.axis('equal')
plt.title('Rhombus Plot')

plt.show()

