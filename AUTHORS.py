import glob
import calcAuthor
import numpy as np
attributions = []
def getAttributions(dir, authors):
    f = open(dir+"/AUTHORS.txt")
    for line in f:
        groups = line.split(":")
        groups[1] = groups[1].replace("\n", "")
        groups[1] = authors.index(groups[1])
        attributions.append(groups)

def getAuthor(text):
    for i in range(len(attributions)):
        if attributions[i][0] in text:
            return attributions[i][1]

def getSamplesAndAuthors(dir, authors, debug):
    getAttributions(dir, authors)
    featuresCalculated = []
    authorsCalculated = []
    for f in glob.glob(dir+"/*.txt"):
        if "AUTHORS.txt" in f:
            continue
        calc = calcAuthor.CalcAuthorBatch(f, False, 1, True)
        featuresCalculated.append(calc.calcFeatures())
        authorsCalculated.append(np.zeros(calc.getNumSamples(), dtype=np.int))
        authorsCalculated[len(authorsCalculated)-1].fill(getAuthor(f))
    return np.concatenate(featuresCalculated), np.concatenate(authorsCalculated)
