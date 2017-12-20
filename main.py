import numpy as np
import time
import glob
import calcAuthor
import AUTHORS
from classifiers import weighted
debug = True
authors = ["Jane Austen", "Walter Scott", "Arthur Conan Doyle", "Charles Dickens", "Mark Twain", "Louisa Alcott", "Jack London"]
#Index coresponds to authors array
textDirs = ["texts/Jane_Austen", "texts/Walter_Scott", "texts/Arthur_Doyle", "texts/Charles_Dickens", "texts/Mark_Twain", "texts/Louisa_Alcott", "texts/Jack_London"]
unknownDir = "texts/Unknown"
#List of guessed attributions in format [[name, authorNum], [name, authorNum]]
attributions = []

classifier = weighted.WeightedClassifier(len(textDirs), sum(calcAuthor.LENGTHS))

groupIndex = 0

#Features calculated for each author and text
features = []
for author in textDirs:
    authorFeatures = []
    for f in glob.glob(author + "/*.txt"):
        calculator = calcAuthor.CalcAuthorBatch(f, False, 1, True)
        authorFeatures.append(calculator.calcFeatures()[0])
    features.append(authorFeatures)
    groupIndex+=1

classifier.adjustWeights(features)

groupIndex = 0
for f in features:
    classifier.train(f, groupIndex)
    groupIndex += 1


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

print str(round((float(correct)/float(numFiles))*100)) + " % Correct"
