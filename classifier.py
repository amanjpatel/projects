import numpy.random as nprand
for a in range(0, 10):
    x = nprand.uniform(0, 1)
    y = nprand.uniform(0, 1)
    print(x, y)
    if x + y > 1:
        z = 1
    else:
        z = 0
    print(z)

numNeur =

class Neuron:
    connections = []
    for x in range(0, numNeur):
        w =
        connections.append(w)
    def __init__(self, number, layer):
        self.number = num
        self.layer = layer
    def activate(self, ):
        if sum(connections) =
'''
discrete:
neuron must know the states of the presynaptic neurons (0 or 1),
 and the weights of each presynaptic neuron (-1 to 1, absolute value of all weights add up to 1),
neuron will then perform a weighted sum of the presynaptic neurons
if it is above threshold, it will fire
if it is not, it will not fire

continuous:
if the presynaptic neuron fires, it adds neurotransmitter to synapse
    (-1 to 1, depending on weight, absolute value of all weights add up to 1)
neurotransmitter immediately begins to decay based on a fast decay function
neuron will then perform a weighted sum of synapses
if it is above threshold, it will fire
if it is not, it will not fire
variables (per neuron): list of connected neurons (list), list of weights (list),
 list of synapse neurotransmitter amount (list)
'''
cycles = 10
# all will be same length, neuron0 = index[0], neuron1 = index[1], neuron2 = index[2]
# 0 = no connection, 1 = connection
conxns = [0,1,1,0,1]
# -1 = max inhibitory, 1 = max excitatory
weights = [0.5,0.3,0.4,-0.7,0.2]
# no bounds
syns = [0,0,0,0,0]
# 0 or 1
fires = [0,0,0,0,0]

for x in range(0,cycles):
    for neur in range(0,len(conxns)):
        # synapse decay
        syns = syns*0.5
        sum = 0
        # firing to increase in synapse neurotransmitter
        for y in range(0,len(conxns)):
            if y != neur:
                syns[y] = (weights[y] * fires[y]) + syns[y]
                sum += syns[y]
        # firing
        if sum >= threshold:
            fires[neur] = 1
        else:
            fires[neur] = 0
        # learning
        for y in range(0,len(conxns)):
            if y != neur:
                if fires[neur] and fires[y] == 1:
                    if weights[y] >= 0:
                        weights[y] = (weights[y])**2
                    else:
                        weights[y] = -1*((weights[y])**2)
print(conxns,weights,syns,fires)