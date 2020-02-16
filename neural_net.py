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

import numpy.random
import numpy as np
#array = numpy.random.uniform(0,1,(10,10))
array = np.array([[.3, .5, .8, .5, .3], [.5, .8, .5, .8, .5], [.8, .5, .3, .5, .8]])
print(array)
# fix lack of function on rightmost and bottommost values
for k in range(0,100):
    for x in range(0,4):
        for y in range(0,2):
            averageSurround = (array[y + 1, x] + array[y - 1, x] + array[y, x + 1] + array[y, x - 1] + array[y + 1, x + 1] +
                           array[y - 1, x - 1] + array[y - 1, x + 1] + array[y + 1, x - 1]) / 8
            if array[y,x] > averageSurround:
                array[y,x] = (array[y,x])**0.5
            else:
                array[y,x] = (array[y,x])**2
print(array)
# orientation states: 8 possible orientations for a 4-pixel portion of larger array
edgeOrient = 0
# edge length
# edge motion
# shape
# shape motion


    # Jazz comment