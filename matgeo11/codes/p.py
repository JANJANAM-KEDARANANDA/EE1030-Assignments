# Code by GVV Sharma
# Modified for Problem Solution
# Released under GNU GPL
# Calculating area enclosed between curves
import sys  # For path to external scripts
sys.path.insert(0, '/home/kedar/assignments/matgeo/codes/CoordGeo')  # Path to my scripts

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Read the values from the C-generated text file using numpy.loadtxt
try:
    data = np.loadtxt('data.txt')
except OSError:
    print("Error: Unable to read 'data.txt'. Please ensure the file exists.")
    sys.exit(1)

# Extracting ellipse parameters
a = data[0]  # semi-major axis
b = data[1]  # semi-minor axis
h = data[2]  # center x-coordinate (h)
k = data[3]  # center y-coordinate (k)

# Ellipse equations
def ellipse_upper(x, a, b, h, k):
    """Returns the upper part of the ellipse."""
    return k + b * np.sqrt(1 - ((x - h) ** 2) / (a ** 2))

def ellipse_lower(x, a, b, h, k):
    """Returns the lower part of the ellipse."""
    return k - b * np.sqrt(1 - ((x - h) ** 2) / (a ** 2))

# Define the limits of integration
x_min = 0
x_max = 2

# Compute the area between the curves using integration
def area_between_curves(x):
    """Calculates the difference between the upper and lower ellipse."""
    return ellipse_upper(x, a, b, h, k) - ellipse_lower(x, a, b, h, k)

# Perform the integration from x_min to x_max
area, _ = quad(area_between_curves, x_min, x_max)

print(f"Area enclosed between the ellipse and the ordinates: {area:.4f}")

# Visualization
# Generating points for the ellipse to show the complete ellipse
x_vals = np.linspace(h - a, h + a, 400)
y_upper = ellipse_upper(x_vals, a, b, h, k)
y_lower = ellipse_lower(x_vals, a, b, h, k)

# Plot the ellipse's upper and lower parts
plt.plot(x_vals, y_upper, label=f'Ellipse: $(x - {h})^2/{a**2} + (y - {k})^2/{b**2} = 1$', color='r')
plt.plot(x_vals, y_lower, color='r')

# Shade the area between the ellipse and the x-axis between x=0 and x=2 (uniform color)
y_fill_upper = ellipse_upper(np.linspace(x_min, x_max, 100), a, b, h, k)
y_fill_lower = ellipse_lower(np.linspace(x_min, x_max, 100), a, b, h, k)

# Fill the area
plt.fill_between(np.linspace(x_min, x_max, 100), y_fill_upper, y_fill_lower, color='lightblue', alpha=0.5, label='Shaded Area')

# Labels and plot settings
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.title('Area Enclosed by the Ellipse and the Ordinates')
plt.grid(True)
plt.legend(loc='upper right')

# Set the limits for y-axis to ensure complete visibility of the ellipse
plt.ylim(k - b - 1, k + b + 1)  # Slightly adjust as needed for aesthetics

# Set equal aspect ratio to avoid distortion
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()

