# Code by GVV Sharma
# September 12, 2023
# Revised July 21, 2024
# Released under GNU GPL
# Point Vectors
import sys                                          # for path to external scripts
sys.path.insert(0, '/home/kedar/Documents/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt

# Read values from values.tex using np.loadtxt
data = np.loadtxt('values.tex', delimiter=':', dtype=str, comments='%')

# Extract and clean the values for direction and normal vectors
direction_vector = np.array([
    float(data[0][1].strip().replace('cm', '')),  # Adjust based on your data structure
    float(data[1][1].strip().replace('cm', ''))
])

normal_vector = np.array([
    float(data[2][1].strip().replace('cm', '')),  # Adjust based on your data structure
    float(data[3][1].strip().replace('cm', ''))
])

# Define points for the line
x_values = np.linspace(-5, 10, 100)
y_values = (x_values - 2)

# Create a figure
plt.figure(figsize=(8, 6))

# Plot the line
plt.plot(x_values, y_values, label='Line: $y = x - 2$', color='cyan')

# Origin point
origin = np.array([2, 0])

# Plot the direction vector
plt.quiver(*origin, *direction_vector, angles='xy', scale_units='xy', scale=1, color='green', label='Direction Vector')

# Plot the normal vector
plt.quiver(*origin, *normal_vector, angles='xy', scale_units='xy', scale=1, color='blue', label='Normal Vector')

# Set limits and labels
plt.xlim(-5, 10)
plt.ylim(-5, 10)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')

# Set labels and title
plt.xlabel('$X$-Axis')
plt.ylabel('$Y$-Axis')
plt.title('Plot of the Line: $y = x - 2$ with Direction and Normal Vectors')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()

