neur_list = []
threshold = input("What should the threshold be?")
class Neuron:
    numNeur = 0
    def __init__(self, index, weights, syns):
        self.index = index
        self.weights = weights
        self.syns = syns
        Neuron.numNeur += 1
        neur_list.append([self.index, self.weights, self.syns])

    def activate(self, threshold):


neuron1 = Neuron(Neuron.numNeur, [.5,.5,.5],[0,0,0])
neuron2 = Neuron(Neuron.numNeur, [.5,.5,.5],[0,0,0])
