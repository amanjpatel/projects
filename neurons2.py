# weights need to be adjusted so that the total of the absolute value of all "on" weights is equal to 1
# off neurons can have very large weights, but they only factor in to the weight mix when they fire

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

    # @classmethod
    @staticmethod
    def activate(self):
        sum = 0
        # decay and addition, decay func is square root
        for x in range(0, self.index) and range(self.index + 1, len(self.syns)):
            self.syns[x] = (self.syns[x])**0.5
            self.syns[x] = (self.syns[x]) + ((self.weights[x]) * (fires[x]))
            print(self.syns[x])
            sum += self.syns[x]
            print(sum)
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

# set neuron number and initial weights
userNum = int(input("How many neurons do you want?"))
initialWeights = float(input("What initial weight?"))
cycles = int(input("How many cycles?"))

# create neurons
for x in range(0, userNum):
    neur_list.append(Neuron(Neuron.numNeur, [initialWeights] * userNum, [0] * userNum))

# set initial firing pattern
#fires = [0] * Neuron.numNeur
fires = [0, 1, 0, 0, 1]

# activate neurons
for y in range(0, cycles):
    for x in range(0, len(neur_list)):
        Neuron.activate(neur_list[x])

# print resulting neuron states
for x in range(0, len(neur_list)):
    attr.append([neur_list[x].index, neur_list[x].weights, neur_list[x].syns])
print(attr)