import sys                                          # for path to external scripts
sys.path.insert(0, '/home/kedar/Documents/matgeo/codes/CoordGeo')  # path to my scripts
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Custom function to mimic "load.tex" behavior
def load_tex(filename):
    try:
        data = np.genfromtxt(filename, delimiter=' ', names=True)
        return data
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return None

# Load data from the 'values.tex' file using the custom "load.tex" command
data = load_tex('values.tex')
if data is None:
    sys.exit("Failed to load data from values.tex")

# Define points for the line
x_values = np.linspace(-5, 10, 100)
y_values = (x_values - 2)

# Create a figure
plt.figure(figsize=(8, 6))

# Plot the line
plt.plot(x_values, y_values, label='Line: $y = x - 2$', color='cyan')

# Extract direction vector and normal vector
x = data['d']
y = data['n']
direction_vector = np.array([x[0], x[1]])  
normal_vector = np.array([y[0], y[1]])
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

