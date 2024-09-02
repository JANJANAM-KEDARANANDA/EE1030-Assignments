import ctypes

# Load the shared library
lib = ctypes.CDLL('./det.so')

# Define the argument and return types of the C function
lib.det.argtypes = [ctypes.c_double, ctypes.c_double,
                                ctypes.c_double, ctypes.c_double,
                                ctypes.c_double, ctypes.c_double]
lib.det.restype = ctypes.c_double

# Define a function to call the C function and get the determinant
def get_determinant(a, b, d, e, g, h):
    return lib.det(a, b,  d, e,  g, h)

# Example usage
det = get_determinant(2,0,1,2,0,4)
print(f"The determinant of the matrix is: {det:.2f}")



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
A = np.array(([2,0])).reshape(-1,1)
B = np.array(([1,2])).reshape(-1,1)
C = np.array(([0,4])).reshape(-1,1)
#Generating all lines
x_AC = line_gen(A,C)
#Plotting all lines
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')

#Labeling the coordinates
tri_coords = np.block([[A,B,C]])
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C']
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
