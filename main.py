import numpy as np
import time
import glob
import calcFeatures
import calcAuthor
debug = True
authors = ["Jane Austen", "Walter Scott", "Arthur Conan Doyle", "Charles Dickens", "Mark Twain", "Louisa Alcott"]
#Index coresponds to authors array
textDirs = ["texts/Jane_Austen", "texts/Walter_Scott", "texts/Arthur_Doyle", "texts/Charles_Dickens", "texts/Mark_Twain", "texts/Louisa_Alcott"]
#Number of samples per author
numSamples = 5
#Data for classifier training
calculatedData = [[[]]*numSamples for i in range(len(authors))]
featureCalcs = []
#Create a FeatureCalculator for each text
for d in textDirs:
    featureCalcs.append([])
    for f in glob.glob(d + "/*.txt"):
        textFile = open(f, 'r')
        featureCalcs[len(featureCalcs)-1].append(calcFeatures.FeatureCalculator(textFile.read(),f,debug=debug))
        textFile.close()

unknownDir = "texts/Unknown"
unknownAttributions = []
#Used only to measure accuracy, not required(set to False if authors not known)
realAttributionsFile = "texts/Unknown/AUTHORS.txt"
realAttributions = []
startTime = time.time()

def calcUnknownFeats(classifier):
    #Run on each work
    i = 0
    for f in glob.glob(unknownDir + "/*.txt"):
        if f in realAttributionsFile:
            continue
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

def readAttributionsFile():
    if realAttributionsFile:
        f = open(realAttributionsFile, 'r')
        for l in f:
            work = l.split(":")[0]
            author = l.split(":")[1].replace("\n", "")
            realAttributions.append([work, author])
    if debug:
        print "Recorded known attributions from " + realAttributionsFile

def findRealAttributed(work):
    for w in realAttributions:
        if w[0] in work:
            return w[1]
    return "NOT_ATTRIBUTED"

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
    classifier = weighted.WeightedClassifier(len(authors), len(featData), debug)
    classifier.train(calculatedData)
    calcUnknownFeats(classifier)
    readAttributionsFile()
    print "--- Results ---"
    correct = 0
    for f in unknownAttributions:
        print "------------------------------------"
        print f[0] + " attributed to " + f[1]
        print "Really: " + findRealAttributed(f[0])
        if findRealAttributed(f[0]) == f[1]:
            correct += 1
    print
    print str(correct) + " of " + str(len(unknownAttributions)) + " attributed correctly."
    print
    percent = str(round(float(correct)/float(len(unknownAttributions))*100))
    print "*-----*\n|" + percent.ljust(5) + "|\n*-----*"
    print  "% Correct"
    print
    finish()
run()
