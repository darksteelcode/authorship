import numpy as np
'''
Training is the same as the SimpleClassifier
Classification is done by comparing the unknown to each author's mean, in a similair way to the SimpleClassifier
The unknown and author's mean are subtracted, but each element is multiplied by a weight to give each different feature different importances
'''
class WeightedClassifier():
    def __init__(self, numAuthors, dataSize, debug=True):
        self.dataSize = dataSize
        self.numAuthors = numAuthors
        self.means = np.empty(shape=[numAuthors, dataSize])
        self.debug = debug
        #Lengths of each feature 30 for commonWords, 10 for punctuation, 1 for sentLength, 1 for diversity, 1 for wordLength
        self.featureGroups = [30, 10, 1, 1, 1] #NEEDS TO BE UPDATED FOR NEW FEATURES
        #Weights to adjust importance of different features - used to test accuracy of individual features
        self.featureWeights = [1.0, 1.0, 1.0, 1.0, 1.0]
        #When weighting, new = (input + biases) * weights
        #Weights to multiply by
        self.weights = np.zeros(self.dataSize)
        #Biases to add
        self.biases = np.zeros(self.dataSize)

    def recalcWeights(self):
        weightIndex = 0
        featureIndex = 0
        for g in self.featureGroups:
            for w in range(g):
                self.weights[weightIndex] = np.multiply(self.weights[weightIndex], self.featureWeights[featureIndex])
                weightIndex+=1
            featureIndex+=1

    def adjustWeights(self, data):
        #For each value in the features, map range of values to 0 to 1
        #Flatten data, as author doesn't matter
        feats = np.concatenate(data)
        maxes = np.max(feats, axis=0)
        mins = np.min(feats, axis=0)
        #Set biases to move min value to zero
        self.biases = np.negative(mins)
        self.weights = np.reciprocal(np.subtract(maxes,mins))
        self.recalcWeights()

    def applyWeighting(self, data):
        return np.multiply(np.add(data, self.biases), self.weights)

    def train(self, data, group):
        if self.debug:
            print "WeightedClassifier Training Started"
            self.means[group] = self.applyWeighting(np.mean(data, axis=0))
        return self.means

    def setGroupAvg(self, avg, group):
        self.means[group] = self.applyWeighting(avg)
        return self.means

    def dist(self, p1, p2):
        #get size of diferrence matrix/vector
        return np.linalg.norm(p1-p2)

    def run(self, data):
        if self.debug:
            print "WeightedClassifier Classification Started"
        data = self.applyWeighting(data)
        #set minDist to infinity
        minDist = np.inf
        minGroupIndex = 0
        for g in range(self.numAuthors):
            d = self.dist(data, self.means[g])
            if d < minDist:
                minDist = d
                minGroupIndex = g
        if self.debug:
            print "WeightedClassifier Classification Finished"
            print "Data classified to group " + str(minGroupIndex)
        return minGroupIndex
