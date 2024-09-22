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
import matplotlib.image as mpimg

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen

# Read data from the values.dat file
with open('values.dat', 'r') as file:
    rain_speed = float(file.readline().strip().split(":")[1].strip().split()[0])
    cycle_speed = float(file.readline().strip().split(":")[1].strip().split()[0])
# Vectors for rain and bicycle
rain_velocity = np.array([0, 0, -rain_speed])  # Rain falling straight down (Z-axis)
bicycle_velocity = np.array([cycle_speed, 0, 0])  # Bicycle moving east (X-axis)

# Combine the rain and bicycle velocities to find the umbrella direction
umbrella_direction = rain_velocity + bicycle_velocity

# Normalize the umbrella direction for better representation
if np.linalg.norm(umbrella_direction) > 0:
    umbrella_direction_normalized = umbrella_direction / np.linalg.norm(umbrella_direction) * (rain_speed + cycle_speed)
else:
    umbrella_direction_normalized = umbrella_direction

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors
ax.quiver(0, 0, 0, rain_velocity[0], rain_velocity[1], rain_velocity[2], color='blue', label='Rain Velocity')
ax.quiver(0, 0, 0, bicycle_velocity[0], bicycle_velocity[1], bicycle_velocity[2], color='red', label='Bicycle Velocity')
ax.quiver(0, 0, 0, umbrella_direction_normalized[0], umbrella_direction_normalized[1], umbrella_direction_normalized[2], color='green', label='Umbrella Direction')

# Set labels
ax.set_title('3D Vector Directions for Rain and Bicycle')
ax.set_xlabel('X-axis (East-West)')
ax.set_ylabel('Y-axis (North-South)')
ax.set_zlabel('Z-axis (Up-Down)')

# Configure plot limits for better visualization
ax.set_xlim([-15, 15])  # Adjust as necessary for clarity
ax.set_ylim([-15, 15])  # Adjust as necessary for clarity
ax.set_zlim([-15, 5])   # Rain falls down, so limit Z to show above and below the origin
ax.legend(loc='best')
ax.grid(True)

# Show the plot
plt.show()

