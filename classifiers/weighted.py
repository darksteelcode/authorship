import numpy as np
'''
Training is the same as the SimpleClassifier
Classification is done by comparing the unknown to each author's mean, in a similair way to the SimpleClassifier
The unknown and author's mean are subtracted, but each element is multiplied by a weight to give each different feature equal importance
'''
class WeightedClassifier():
    def __init__(self, numAuthors, dataSize, debug=True):
        self.dataSize = dataSize
        self.numAuthors = numAuthors
        self.means = np.empty(shape=[numAuthors, dataSize])
        self.debug = debug
        #Lengths of each feature 30 for commonWords, 9 for punctuation, 1 for sentLength, 1 for diversity
        self.featureGroups = [30, 9, 1, 1] #NEEDS TO BE UPDATED FOR NEW FEATURES
        #Weights to make values closer to one - just aprox from sample
        self.featureWeights = [20.0, 3.0, 0.01, 6.6]
        self.weights = np.empty(shape=[dataSize])
        weightIndex = 0
        featureIndex = 0
        for g in self.featureGroups:
            for w in range(g):
                self.weights[weightIndex] = self.featureWeights[featureIndex]
                weightIndex+=1
            featureIndex+=1

    def train(self, data, group):
        if self.debug:
            print "WeightedClassifier Training Started"
            self.means[group] = np.multiply(np.mean(data, axis=0), self.weights)
        return self.means

    def setGroupAvg(self, avg, group):
        self.means[group] = np.multiply(avg, self.weights)
        return self.means

    def dist(self, p1, p2):
        #get size of diferrence matrix/vector
        return np.linalg.norm(p1-p2)

    def run(self, data):
        if self.debug:
            print "WeightedClassifier Classification Started"
        data = np.multiply(data, self.weights)
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
