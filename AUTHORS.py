import glob
import calcAuthor
import numpy as np
def getAttributions(dir, authors):
    attributions = []
    f = open(dir+"/AUTHORS.txt")
    for line in f:
        groups = line.split(":")
        groups[1] = groups[1].replace("\n", "")
        try:
            groups[1] = authors.index(groups[1])
        except ValueError:
            groups[1] = -1
        attributions.append(groups)
    return attributions

def getAuthor(text, attributions):
    for i in range(len(attributions)):
        if attributions[i][0] in text:
            return attributions[i][1]

def getSamplesAndAuthors(dir, authors, debug, sampleLength):
    attributions = getAttributions(dir, authors)
    featuresCalculated = []
    authorsCalculated = []
    for f in glob.glob(dir+"/*.txt"):
        if "AUTHORS.txt" in f:
            continue
        calc = calcAuthor.CalcAuthorBatch(f, False, sampleLength, False)
        featuresCalculated.append(calc.calcFeatures())
        authorsCalculated.append(np.zeros(calc.getNumSamples(), dtype=np.int))
        authorsCalculated[len(authorsCalculated)-1].fill(getAuthor(f, attributions))
    return np.concatenate(featuresCalculated), np.concatenate(authorsCalculated)

def calcAttributions(dir, authors, sampleLength, classifier):
    attributions = getAttributions(dir, authors)
    #Second element in array will be changed to guessed author
    result = np.copy(attributions)
    i = 0
    for f in glob.glob(dir+"/*.txt"):
        if "AUTHORS.txt" in f:
            continue
        calc = calcAuthor.CalcAuthorBatch(f, False, sampleLength, False)
        probs = classifier.getPredictions(calc.calcFeatures())
        probs = np.mean(probs, axis=0)
        result[i][1] = np.argmax(probs)
        i+=1
    print attributions
    return result
