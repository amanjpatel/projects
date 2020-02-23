import numpy.random as nprand

neur_list = []
neur_attr_list = []
attr = []
threshold = float(input("What should the threshold be?"))

class Neuron:

    numNeur = 0

    def __init__(self, index, weights, syns):
        self.index = index
        self.weights = weights
        self.syns = syns
        Neuron.numNeur += 1
        neur_attr_list.append([self.index, self.weights, self.syns])

    @staticmethod
    def activate(self):
        sum = 0
        # decay and addition, decay func is square root
        for x in [j for j in range(0, len(self.syns)) if j != self.index]:
            adj_weights = []
            weight_tot = 0
            for q in range(0, len(self.syns)):
                if fires[q] == 1:
                    adj_weights.append(self.weights[q])
                    weight_tot += abs(self.weights[q])
                else:
                    adj_weights.append(0)
            for k in range(0, len(adj_weights)):
                if weight_tot > 0:
                    adj_weights[k] = adj_weights[k] / weight_tot
                else:
                    print("All weights are zero, amend threshold")
            self.syns[x] = self.syns[x]**0.5
            self.syns[x] = self.syns[x] + ((adj_weights[x]) * (fires[x]))
            if self.syns[x] < 0:
                self.syns[x] = 0
            sum += self.syns[x]
        # firing
        if sum >= threshold:
            fires[self.index] = 1
        else:
            fires[self.index] = 0
        # learning, learning func is square/square root
        for x in range(0, self.index) and range(self.index + 1, len(self.syns)):
            if fires[x] and fires[self.index] == 1:
                if self.weights[x] >= 0:
                    self.weights[x] = self.weights[x] ** 0.5
                else:
                    self.weights[x] = -1 * ((abs(self.weights[x])) ** 0.5)
            elif fires[x] != fires[self.index]:
                if self.weights[x] >= 0:
                    self.weights[x] = self.weights[x] ** 2
                else:
                    self.weights[x] = -1 * (self.weights[x] ** 2)


# set neuron number and initial weights
userNum = int(input("How many neurons do you want?"))
cycles = int(input("How many cycles?"))

# create neurons
for x in range(0, userNum):
    #print("What initial weight list? Must have " + str(userNum) + " items")
    initialWeights = []
    for z in range(0, userNum):
        #initialWeights.append(float(input("Weight for element " + str(z) + "? (from -1 to 1)")))
        initialWeights.append(nprand.uniform(-1, 1))
    neur_list.append(Neuron(Neuron.numNeur, initialWeights, [0] * userNum))

# set initial firing pattern (must be same length as numNeur)
#fires = [0] * Neuron.numNeur
#fires = [0, 1]
fires = []
for x in range(0, userNum):
    w = int(nprand.randint(0, 2, 1))
    fires.append(w)
print(fires)

# activate neurons
for y in range(0, cycles):
    for x in range(0, len(neur_list)):
        Neuron.activate(neur_list[x])

# print resulting neuron states
for x in range(0, len(neur_list)):
    attr.append([neur_list[x].index, neur_list[x].weights, neur_list[x].syns])
print(attr)
print(fires)