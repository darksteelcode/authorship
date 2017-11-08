import numpy as np
import time
import os, sys
import glob
import calcFeatures
from classifiers import simple
debug = True
authors = ["Jane Austen", "Walter Scott", "Arthur Conan Doyle", "Charles Dickens"]
#Index coresponds to authors array
textDirs = ["texts/Jane_Austen", "texts/Walter_Scott", "texts/Arthur_Doyle", "texts/Charles_Dickens"]
#Number of samples per author
numSamples = 5
#Data for classifier training
calculatedData = [[[]]*numSamples for i in range(len(authors))]
featureCalcs = []
#Create a FeatureCalculator for each text
'''for t in texts:
    f = open(t[1] + ".txt", 'r')
    fullText = f.read()
    f.close()
    featureCalcs.append(calcFeatures.FeatureCalculator(fullText,t[1], debug=debug))'''
for d in textDirs:
    #Start at directory script run from
    os.chdir(sys.path[0])
    #Go to directory of texts
    os.chdir(d)
    featureCalcs.append([])
    for f in glob.glob("*.txt"):
        textFile = open(f, 'r')
        featureCalcs[len(featureCalcs)-1].append(calcFeatures.FeatureCalculator(textFile.read(),f,debug=debug))
        textFile.close()

unknownDir = "texts/Unknown"
unknownAttributions = []

startTime = time.time()

def calcUnknownFeats(classifier):
    #Start at directory script run from
    os.chdir(sys.path[0])
    #Go to directory of texts
    os.chdir(unknownDir)
    #Run on each work
    i = 0
    for f in glob.glob("*.txt"):
        unF = open(f, 'r')
        unCalc = calcFeatures.FeatureCalculator(unF.read(), f)
        unF.close()
        unFeats = unCalc.calcFeatures()
        #Flatten to classify using one dimensional classifier
        unFeats = [item for items in unFeats for item in items]
        guess = classifier.run(unFeats)
        if debug:
            print "Guessed Author for " + f + " is Number " + str(guess) + ", " + authors[guess]
        unknownAttributions.append([f, authors[guess]])
        i+=1

def listTexts():
    if debug:
        print "--TEXTS--"
        for d in textDirs:
            print d
        print ""

def start():
    if debug:
        print "Started"
        print ""

def finish():
    if debug:
        print "Finished in " + str(time.time()-startTime) + " Seconds"

def startFeatureCalc():
    if debug:
        print "--FEATURE CALCULATIONS--"

def run():
    start()
    listTexts()
    startFeatureCalc()
    authorIndex = 0
    #Used only for setting up classifer out of loop - used ot get length of flattened features
    featData = []
    for author in featureCalcs:
        textIndex = 0
        for text in author:
            featData = text.calcFeatures()
            #Flatten to classify using one dimensional classifier
            featData = [item for items in featData for item in items]
            calculatedData[authorIndex][textIndex] = featData
            textIndex+=1
        authorIndex+=1
    classifier = simple.SimpleClassifier(len(authors), len(featData), debug)
    classifier.train(calculatedData)
    calcUnknownFeats(classifier)
    print "--- Results ---"
    for f in unknownAttributions:
        print f[0] + " attributed to " + f[1]
        print
    print
    finish()

run()
