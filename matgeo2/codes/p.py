import ctypes

# Load the shared library
lib = ctypes.CDLL('./trisection.so')

# Define the argument and return types of the C function
lib.find_trisection_points.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                                       ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                       ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]

# Define a function to call the C function and get the trisection points
def get_trisection_points(x1, y1, x2, y2):
    x1_t = ctypes.c_double()
    y1_t = ctypes.c_double()
    x2_t = ctypes.c_double()
    y2_t = ctypes.c_double()

    lib.find_trisection_points(x1, y1, x2, y2, ctypes.byref(x1_t), ctypes.byref(y1_t), ctypes.byref(x2_t), ctypes.byref(y2_t))

    return (x1_t.value, y1_t.value, x2_t.value, y2_t.value)

# Example usage
x1, y1 = 2.0, -2.0
x2, y2 = -7.0, 4.0

x1_t, y1_t, x2_t, y2_t = get_trisection_points(x1, y1, x2, y2)



print(f"Trisection points are: ({x1_t}, {y1_t}) and ({x2_t}, {y2_t})")


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




#Given points
A = np.array(([2,-2])).reshape(-1,1)
B = np.array(([-7,4])).reshape(-1,1)

P = np.array(([x1_t,y1_t])).reshape(-1,1)
Q = np.array(([x2_t,y2_t])).reshape(-1,1)
#Generating all lines
x_AB = line_gen(A,B)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')

#Labeling the coordinates
tri_coords = np.block([[A,B,P,Q]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','P','Q']
for i, txt in enumerate(vert_labels):
    #plt.annotate(txt, # this is the text
    plt.annotate(f'{txt}\n({tri_coords[0,i]:.0f}, {tri_coords[1,i]:.0f})',
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(20,-10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center
# use set_position
ax = plt.gca()
#ax.spines['top'].set_color('none')
#ax.spines['left'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
#plt.xlabel('$x$')
#plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')


plt.show()
