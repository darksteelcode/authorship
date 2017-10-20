import numpy as np
import time
import calcFeatures
from classifiers import simple
debug = True
authors = ["Jane Austen", "Walter Scott"]
#Number of samples per author
numSamples = 5
#Data for classifier training - needs to be changed for use with more than one feature
calculatedData = np.empty(shape=(len(authors),numSamples,30))
#Text format [authorNum, path]
texts = [[0, "texts/Jane_Austen/sense_and_sensibility"], [0, "texts/Jane_Austen/emma"], [0,"texts/Jane_Austen/northanger_abbey"], [0,"texts/Jane_Austen/persuasion"], [0,"texts/Jane_Austen/pride_and_prejudice"], [1,"texts/Walter_Scott/ivanhoe"], [1,"texts/Walter_Scott/lady_of_the_lake"], [1,"texts/Walter_Scott/letters_on_demonology_and_witchcraft"], [1,"texts/Walter_Scott/talisman"], [1,"texts/Walter_Scott/waverley"]]
featureCalcs = []
#Create a FeatureCalculator for each text
for t in texts:
    f = open(t[1] + ".txt", 'r')
    fullText = f.read()
    f.close()
    featureCalcs.append(calcFeatures.FeatureCalculator(fullText,t[1]))

unknownText = "texts/Unknown/old_mortality.txt"

startTime = time.time()
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
        featData = c.calcFeatures()[0]
        auth = texts[textIndex][0]
        calculatedData[auth][authorIndexes[auth]] = featData
        authorIndexes[auth]+=1
        textIndex+=1
    classifier = simple.SimpleClassifier(len(authors), 30, debug)
    classifier.train(calculatedData)
    unF = open(unknownText, 'r')
    unCalc = calcFeatures.FeatureCalculator(unF.read(), 'Unknown')
    unF.close()
    unFeats = unCalc.calcFeatures()[0]
    guess = classifier.run(unFeats)
    print "Guessed Author is Number " + str(guess) + ", " + authors[guess]
    finish()

run()
