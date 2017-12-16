import numpy as np
import time
import glob
import calcAuthor
import AUTHORS
from classifiers import weightedClean
debug = True
authors = ["Jane Austen", "Walter Scott", "Arthur Conan Doyle", "Charles Dickens", "Mark Twain", "Louisa Alcott"]
#Index coresponds to authors array
textDirs = ["texts/Jane_Austen", "texts/Walter_Scott", "texts/Arthur_Doyle", "texts/Charles_Dickens", "texts/Mark_Twain", "texts/Louisa_Alcott"]
unknownDir = "texts/Unknown"
#List of guessed attributions in format [[name, authorNum], [name, authorNum]]
attributions = []

classifier = weightedClean.WeightedClassifier(len(textDirs), sum(calcAuthor.LENGTHS))

groupIndex = 0
for author in textDirs:
    features = []
    for f in glob.glob(author + "/*.txt"):
        calculator = calcAuthor.CalcAuthorBatch(f, False, 1, True)
        features.append(calculator.calcFeatures()[0])
    classifier.train(features, groupIndex)
    groupIndex+=1

for f in glob.glob(unknownDir + "/*.txt"):
    if "AUTHORS" in f:
        continue
    calculator = calcAuthor.CalcAuthorBatch(f, False, 1, True)
    attributions.append([f, classifier.run(calculator.calcFeatures()[0])])

correct = 0
numFiles = 0

for a in attributions:
    print a[0] + " attributed to " + authors[a[1]]
    real = AUTHORS.getAuthor(a[0], AUTHORS.getAttributions("texts/Unknown", authors))
    print "Really: " + authors[real]
    if real == a[1]:
        correct += 1
    numFiles+=1

print round((float(correct)/float(numFiles))*100)
