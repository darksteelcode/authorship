import numpy as np
import time
import os
import glob
import calcFeatures
from classifiers import simple
debug = False
authors = ["Jane Austen", "Walter Scott", "Arthur Conan Doyle"]
#Number of samples per author
numSamples = 5
#Data for classifier training
calculatedData = [[[]]*numSamples for i in range(len(authors))]
#Text format [authorNum, path]
texts = [[0, "texts/Jane_Austen/sense_and_sensibility"], [0, "texts/Jane_Austen/emma"], [0,"texts/Jane_Austen/northanger_abbey"], [0,"texts/Jane_Austen/persuasion"], [0,"texts/Jane_Austen/pride_and_prejudice"],
[1,"texts/Walter_Scott/ivanhoe"], [1,"texts/Walter_Scott/lady_of_the_lake"], [1,"texts/Walter_Scott/letters_on_demonology_and_witchcraft"], [1,"texts/Walter_Scott/talisman"], [1,"texts/Walter_Scott/waverley"],
[2, "texts/Arthur_Doyle/hounds_of_baskervilles"], [2, "texts/Arthur_Doyle/lost_world"], [2, "texts/Arthur_Doyle/sign_of_four"], [2, "texts/Arthur_Doyle/study_in_scarlet"], [2, "texts/Arthur_Doyle/valley_of_fear"]]
featureCalcs = []
#Create a FeatureCalculator for each text
for t in texts:
    f = open(t[1] + ".txt", 'r')
    fullText = f.read()
    f.close()
    featureCalcs.append(calcFeatures.FeatureCalculator(fullText,t[1], debug=debug))

unknownDir = "texts/Unknown"
unknownAttributions = []

startTime = time.time()

def calcUnknownFeats(classifier):
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
        print "Guessed Author for " + f + " is Number " + str(guess) + ", " + authors[guess]
        unknownAttributions.append([f, authors[guess]])
        i+=1

def listTexts():
    if debug:
        print "--TEXTS--"
        for t in texts:
            print t
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
    textIndex = 0
    authorIndexes = [0] * len(authors)
    for c in featureCalcs:
        featData = c.calcFeatures()
        #Flatten to classify using one dimensional classifier
        featData = [item for items in featData for item in items]
        auth = texts[textIndex][0]
        calculatedData[auth][authorIndexes[auth]] = featData
        authorIndexes[auth]+=1
        textIndex+=1
    classifier = simple.SimpleClassifier(len(authors), len(featData), debug)
    classifier.train(calculatedData)
    calcUnknownFeats(classifier)
    print
    for f in unknownAttributions:
        print f[0] + " attributed to " + f[1]
        print
    print
    finish()

run()
