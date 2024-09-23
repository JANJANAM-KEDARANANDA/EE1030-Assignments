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

# Function to read values from values.tex using loadtxt
def read_values(filename):
    # Load the data, ensuring to treat it as strings
    data = np.loadtxt(filename, delimiter=':', dtype=str, comments='%')
    
    # Extract and clean the values
    side_length = float(data[0][1].strip().replace('cm', ''))
    angle_A = float(data[1][1].strip().replace('degrees', ''))
    return side_length, angle_A

# Read side length and angle from the LaTeX file
side_length, angle_A = read_values('values.tex')

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

