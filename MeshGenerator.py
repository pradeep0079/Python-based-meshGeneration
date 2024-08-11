import math
import numpy as np
import matplotlib.pyplot as plt

L = 1.2
H = 0.5
Element = 100
angle = 15
angle_rad = math.radians(angle)

'''I want to make ramp
 TODO that the starting point is taken as x1 from where it will begin to slope.'''

x1 = 0.5

'''Assuming the y axis is at origin so, it start at zero.'''
y1 = 0

node = []
slope = math.tan(angle_rad)


for y in np.linspace(0, H, num=Element):
    for x in np.linspace(0, L, num = Element):
        # x0 = (y + 3.333319)/0.59998
        x0 = ((y - y1)/slope) + x1
        if(x>x0 and x0!=L):
            node.append([x0, y])
        else:
            node.append([x,y])

points = np.array(node)
from scipy.spatial import Delaunay
tri = Delaunay(points)

plt.triplot(points[:,0], points[:,1], tri.simplices)
plt.plot(points[:,0], points[:,1], 'o')
plt.show()
plt.close()

np_point = len(points)
np_element = len(tri.simplices)
file = open("test.h5", 'w')
file.write("Total Number of Points and Total Number of Element:\n")
file.write("{}  {}\n".format(np_point, np_element))
file.write("Node in x-Direction and y-Direction:\n")
for i,Nodes in enumerate(node):
    file.write("{}  {}  {}\n".format(i,Nodes[0], Nodes[1]))
file.write("Element form by three Node:\n")
for j, elem in enumerate(tri.simplices):
    file.write("{} {} {} {}\n". format(j, elem[0], elem[1], elem[2]))
file.close()


