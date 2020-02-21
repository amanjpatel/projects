neur_list = []
neur_attr_list = []
threshold = float(input("What should the threshold be?"))

class Neuron:

    numNeur = 0

    def __init__(self, index, weights, syns):
        self.index = index
        self.weights = weights
        self.syns = syns
        Neuron.numNeur += 1
        neur_attr_list.append([self.index, self.weights, self.syns])

    def activate(self, threshold):
        sum = 0
        # decay and addition, decay func is square root
        for x in range(0, self.index) and range(self.index + 1, len(self.syns)):
            self.syns[x] = (self.syns[x])**0.5
            self.syns[x] = (self.syns[x]) + ((self.weights[x]) * (fires[x]))
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
                    self.weights[x] = (self.weights[x]) ** 0.5
                else:
                    self.weights[x] = -1 * ((abs(self.weights[x])) ** 0.5)
            elif fires[x] != fires[self.index]:
                if self.weights[x] >= 0:
                    self.weights[x] = (self.weights[x]) ** 2
                else:
                    self.weights[x] = -1 * ((self.weights[x]) ** 2)


fires = [0] * Neuron.numNeur

userNum = int(input("How many neurons do you want?"))
initialWeights = float(input("What initial weight?"))

for x in range(0, userNum):
    neur_list.append(Neuron(Neuron.numNeur, [initialWeights] * Neuron.numNeur, [0] * Neuron.numNeur))
print(neur_list)