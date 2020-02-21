import numpy.random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

imagename = input("What is the image name? (with file extension)")

im = Image.open(imagename)
im_arr = np.array(im)
print(im_arr.shape)

y_dim = im_arr.shape[0]
x_dim = im_arr.shape[1]

array = np.zeros((y_dim,x_dim))

for x in range(0, x_dim):
    for y in range(0, y_dim):
        rgb = im_arr[y,x]
        bw = 0
        for z in range(0,3):
            bw += int(rgb[z])
        avg = (bw/(3*255))
        array[y,x] = avg
#array = numpy.random.uniform(0,1,(10,10))
#array = np.array([[.3, .5, .8, .5, .3], [.5, .8, .5, .8, .5], [.8, .5, .3, .5, .8]])
#array = np.array([[.01, .02, .01, .03, .01], [0.02, 0.03, 0.01, 0.02, 0.01], [.7, .7, .4, .7, .2]])
a = 0

for k in range(0,5):
    for x in range(0,x_dim):
        for y in range(0,y_dim):
            if x == (x_dim-1) and y != y_dim-1:
                averageSurround = (array[y + 1, x] + array[y - 1, x] + array[y, x - 1] + array[y - 1, x - 1] + array[y + 1, x - 1]) / 5
            elif y == (y_dim-1) and x != x_dim-1:
                averageSurround = (array[y - 1, x] + array[y, x + 1] + array[y, x - 1] + array[y - 1, x - 1] + array[y - 1, x + 1]) / 5
            elif x == (x_dim-1) and y == (y_dim-1):
                averageSurround = (array[y - 1, x] + array[y, x - 1] + array[y - 1, x - 1]) / 3
            elif x != x_dim and y != y_dim:
                averageSurround = (array[y + 1, x] + array[y - 1, x] + array[y, x + 1] + array[y, x - 1] + array[y + 1, x + 1] +
                           array[y - 1, x - 1] + array[y - 1, x + 1] + array[y + 1, x - 1]) / 8
            if array[y,x] > averageSurround:
                array[y,x] = (array[y,x])**0.01
            else:
                array[y,x] = (array[y,x])**100
print(array)
#fin = Image.fromarray(array)
#Image.Image.show(fin)
plt.imshow(array, cmap="gray")
plt.show()
# orientation states
# edge length
# edge motion
# shape
# shape motion


#must be updating spike rate at all times
#must keep track of neurotransmitter in synapse
#must keep track of how much neurotransmitter is left in presynaptic neuron
#must know how many ion channels on synapse
#must be able to control either neurotransmitter or number of ion channels
#must have a free neurotransmitter decay rate
#must have a specified spike length

# center-surround
# orientation
# orientation, motion, direction, position
# orientation, motion, direction, length, position
#
# initial dimensions: (pixel x-value, pixel y-value, shading, time)
# second-step dimensions: (edge x-coordinate, edge y-coordinate, edge z-coordinate, edge motion vector x-component,
# edge motion vector y-component, edge motion vector z-component, edge length, edge width, edge depth)
# third-intermediate dimensions: (object name, coordinated movement)
# final dimensions: (gesture word)
# final final dimensions: (sentences)
