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
threshold = 1
for x in range(0,cycles):
    for neur in range(0,len(conxns)):
        # synapse decay
        sum = 0
        for syn in range(0,len(syns)):
            syns[syn] = syns[syn]*0.5
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