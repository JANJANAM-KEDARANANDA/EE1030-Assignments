import ctypes
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

lib = ctypes.CDLL('./det.so')

# Define the argument and return types of the `det` function
lib.det.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double))
lib.det.restype = ctypes.c_double

def pdet(p1, p2, p3):
    # Convert numpy arrays to ctypes arrays
    p1_ctypes = p1.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    p2_ctypes = p2.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    p3_ctypes = p3.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    
    return lib.det(p1_ctypes, p2_ctypes, p3_ctypes)

# Define a function to call the C function and get the determinant
data = np.genfromtxt('values.dat', delimiter=' ', names=True)
x = data['x']
y = data['y']
p1 = np.array([x[0], y[0],1], dtype=np.float64)
p2 = np.array([x[1], y[1],1], dtype=np.float64)
p3 = np.array([x[2], y[2],1], dtype=np.float64)

det = pdet(p1,p2,p3)
print(f"The determinant of the matrix is: {det:.2f}")








#Given points
A = np.array([x[0],y[0]], dtype=np.float64).reshape(-1,1)
B = np.array([x[1],y[1]], dtype=np.float64).reshape(-1,1)
C = np.array([x[2],y[2]], dtype=np.float64).reshape(-1,1)
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
