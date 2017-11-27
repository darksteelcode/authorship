import numpy as np
'''
Training is the same as the SimpleClassifier
Classification is done by comparing the unknown to each author's mean, in a similair way to the SimpleClassifier
The unknown and author's mean are subtracted, but each element is multiplied by a weight to give each different feature equal importance
'''
#numGroups is the number of sets of data, dataSize is length of data
#train - data is numpy array [ [[group1-data1], [group1-data2], [group1-data3]], [[group2-data1], [group2-data2], [group2-data3]], etc]
#run - data is numpy array [data]
class WeightedClassifier():
    def __init__(self, numGroups, dataSize, debug=True):
        self.numGroups = numGroups
        self.dataSize = dataSize
        self.means = np.empty(shape=[numGroups, dataSize])
        self.debug = debug
        #Lengths of each feature 30 for commonWords, 9 for punctuation, 1 for sentLength, 1 for diversity
        self.featureGroups = [30, 9, 1, 1] #NEEDS TO BE UPDATED FOR NEW FEATURES
        self.weights = np.empty(shape=[dataSize])
        weightIndex = 0
        for g in self.featureGroups:
            for w in range(g):
                self.weights[weightIndex] = (1.0/g)
                weightIndex+=1

    def train(self, data):
        if self.debug:
            print "WeightedClassifier Training Started"
        #for each group of data
        for g in range(self.numGroups):
            #Average that data into one array
            self.means[g] = np.multiply(np.mean(data[g], axis=0), self.weights)
        if self.debug:
            print "WeightedClassifier Trained Successfully"
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
        for g in range(self.numGroups):
            d = self.dist(data, self.means[g])
            if d < minDist:
                minDist = d
                minGroupIndex = g
        if self.debug:
            print "WeightedClassifier Classification Finished"
            print "Data classified to group " + str(minGroupIndex)
        return minGroupIndex
