# add better version of locality
# add layers
# add nonlinear weighting, so that it is more difficult for unconnected neurons to become connected
# add a more accurate decay function
# synchronize timescales
# create types of neurons by tweaking parameters: local-only neurons, wide neurons, etc.
# (next major phase): organize neurons into homeostatic microcolumns
# outstanding questions:
#   1. How should the initial weights be defined, in order to preserve homeostasis?
#   2. What form should the inputs take?

import numpy.random as nprand

# list of neuron objects
neur_list = []

# list of all attributes of objects
neur_attr_list = []
attr = []

# set firing threshold
threshold = float(input("What should the threshold be?"))

# set distance for locality
locality_thresh = float(input("What is the maximum distance to be considered local?"))

class Neuron:

    # counter for number of neurons instantiated
    numNeur = 0
    # constructor for neuron, with an index, a weight list, a synapse list, and a 3D location tuple
    # Weight list contains all presynaptic weights, synapse list contains amount of neurotransmitter in each synapse
    def __init__(self, index, weights, syns, pos):
        self.index = index
        self.weights = weights
        self.syns = syns
        self.pos = pos
        Neuron.numNeur += 1
        neur_attr_list.append([self.index, self.weights, self.syns, self.pos])
    # activation method
    @staticmethod
    def activate(self):
        # sum of all inputs
        sum = 0
        # decay and addition, decay function is *0.25
        for x in [j for j in range(0, len(self.syns)) if j != self.index]:
            # new list of weights adjusted to only include "on" presynaptic neurons
            adj_weights = []
            # sum of all the weights of both "on" and "off" presynaptic neurons
            weight_tot = 0
            # loop to add weights for each presynaptic neuron to adj_weights and weight_tot
            for q in range(0, len(self.syns)):
                if fires[q] == 1:
                    adj_weights.append(self.weights[q])
                    weight_tot += abs(self.weights[q])
                else:
                    adj_weights.append(0)
            # normalizing adj_weights to a range between -1 and 1
            for k in range(0, len(adj_weights)):
                if weight_tot > 0:
                    adj_weights[k] = adj_weights[k] / weight_tot
            # decay of leftover neurotransmitter
            self.syns[x] = self.syns[x]*0.25
            # adding new neurotransmitter to synapse
            self.syns[x] = self.syns[x] + ((adj_weights[x]) * (fires[x]))
            # correcting below-zero neurotransmitter amount to zero
            if self.syns[x] < 0:
                self.syns[x] = 0
            # adding neurotransmitter from each synapse to sum
            sum += self.syns[x]
        # firing, with refractory period of 1 cycle
        # if the sum is bigger than threshold and the neuron did not fire in the last cycle, make the neuron fire
        if sum >= threshold and fires[self.index] == 0:
            fires[self.index] = 1
        else:
            fires[self.index] = 0

    # learning, learning func is square/square root

    @staticmethod
    def learn(self):
        for x in range(0, self.index) and range(self.index + 1, len(self.syns)):
            # if the neurons are close together, then execute the learning function
            # calculate distance between presynaptic and postsynaptic neuron
            dist = (((self.pos[0] - neur_list[x].pos[0]) ** 2) + ((self.pos[1] - neur_list[x].pos[1]) ** 2) + ((self.pos[0] - neur_list[x].pos[0]) ** 2)) ** 0.5
            if dist <= locality_thresh:
                # if a presynaptic neuron fires and the self fires, increase the weight of the presynaptic neuron
                if fires[x] and fires[self.index] == 1:
                    if self.weights[x] >= 0:
                        self.weights[x] = self.weights[x] ** 0.5
                    else:
                        self.weights[x] = -1 * ((abs(self.weights[x])) ** 0.5)
                # if not, then reduce the weight
                elif fires[x] != fires[self.index]:
                    if self.weights[x] >= 0:
                        self.weights[x] = self.weights[x] ** 2
                    else:
                        self.weights[x] = -1 * (self.weights[x] ** 2)
            else:
                # if they aren't local, weights should be zero
                self.weights[x] = 0


# set neuron number and number of timesteps
userNum = int(input("How many neurons do you want?"))
cycles = int(input("How many cycles?"))

# ~create neurons~
for x in range(0, userNum):
    #set initial weights
    #print("What initial weight list? Must have " + str(userNum) + " items")
    initialWeights = []
    #initialWeights = [0.5] * userNum
    # add a random number between -1 and 1 to the weight list
    for z in range(0, userNum):
        #initialWeights.append(float(input("Weight for element " + str(z) + "? (from -1 to 1)")))
        initialWeights.append(nprand.uniform(-1, 1))

    # create a random position tuple with three random numbers, for a space with bounds of -1 and 1 for each dimension
    pos_tuple = (float(nprand.uniform(-1, 1)), float(nprand.uniform(-1, 1)), float(nprand.uniform(-1, 1)))

    # instantiate neurons with arguments numNeur, list initialWeights, and an empty neurotransmitter list for each synapse
    # and three spatial coordinates
    neur_list.append(Neuron(Neuron.numNeur, initialWeights, [0] * userNum, pos_tuple))

# set initial firing pattern (must be same length as numNeur)
#fires = [0] * Neuron.numNeur
#fires = [0, 1]
# create a random initial firing pattern
fires = []
for x in range(0, userNum):
    w = int(nprand.randint(0, 2, 1))
    fires.append(w)
print(fires)

# activate neurons
for y in range(0, cycles):
    for x in range(0, len(neur_list)):
        Neuron.activate(neur_list[x])
        Neuron.learn(neur_list[x])
    print(fires)

# print resulting neuron states
for x in range(0, len(neur_list)):
    attr.append([neur_list[x].index, neur_list[x].weights, neur_list[x].syns, neur_list[x].pos])
#print(attr)
print(fires)