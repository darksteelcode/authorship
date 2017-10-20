import numpy as np
'''
This is a simple classifier, better ones will be used
TRAINING
take data for each group, calculate the mean of the data for each group
RUNNING
classify data by which group mean it is closest to
'''
#numGroups is the number of sets of data, dataSize is length of data
#train - data is numpy array [ [[group1-data1], [group1-data2], [group1-data3]], [[group2-data1], [group2-data2], [group2-data3]], etc]
#run - data is numpy array [data]
class SimpleClassifier():
    def __init__(self, numGroups, dataSize, debug=True):
        self.numGroups = numGroups
        self.dataSize = dataSize
        self.means = np.empty(shape=[numGroups, dataSize])
        self.debug = debug

    def train(self, data):
        if self.debug:
            print "SimpleClassifier Training Started"
        #for each group of data
        for g in range(self.numGroups):
            #Average that data into one array
            self.means[g] = np.mean(data[g], axis=0)
        if self.debug:
            print "SimpleClassifier Trained Successfully"
        return self.means

    def dist(self, p1, p2):
        #get size of diferrence matrix/vector
        return np.linalg.norm(p1-p2)

    def run(self, data):
        if self.debug:
            print "SimpleClassifier Classification Started"
        #set minDist to infinity
        minDist = np.inf
        minGroupIndex = 0
        for g in range(self.numGroups):
            d = self.dist(data, self.means[g])
            if d < minDist:
                minDist = d
                minGroupIndex = g
        if self.debug:
            print "SimpleClassifier Classification Finished"
            print "Data classified to group " + str(minGroupIndex)
        return minGroupIndex
