import numpy as np
import time
import glob
import calcAuthor
import AUTHORS
from classifiers import weighted
import sys
debug = True

authors = []
textDirs = []
unknownDir = ""
'''

#Classical texts
authors = ["Jane Austen", "Walter Scott", "Arthur Conan Doyle", "Charles Dickens", "Mark Twain", "Louisa Alcott", "Jack London", "NOT_ATTRIBUTED"]
#Index coresponds to authors array
textDirs = ["texts/Jane_Austen", "texts/Walter_Scott", "texts/Arthur_Doyle", "texts/Charles_Dickens", "texts/Mark_Twain", "texts/Louisa_Alcott", "texts/Jack_London"]
unknownDir = "texts/Unknown"
'''

#PAN Problems
#Generate authors, textDirs, and unknownDir for PAN problems automatically
def genPANArrays(dir, numCandidates):
    for i in range(1,numCandidates+1):
        authors.append("candidate" + str(i).zfill(5))
        textDirs.append(dir + "/" + authors[i-1])
    authors.append("NOT_ATTRIBUTED")
    unknownDir = dir + "/unknown"
    return unknownDir
panLens = {'a':3, 'b':3, 'c':8, 'd':8, 'i':14, 'j':14}
unknownDir = genPANArrays("pan_texts/pan12-problem-" + sys.argv[1], panLens[sys.argv[1]])


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
    real = AUTHORS.getAuthor(a[0], AUTHORS.getAttributions(unknownDir, authors))
    print "Really: " + authors[real]
    if real == a[1]:
        correct += 1
    #Don't count texts with no given author as wrong - pan has these, but this program is not designed to handle them
    if authors[real] != "NOT_ATTRIBUTED":
        numFiles+=1

print str(round((float(correct)/float(numFiles))*100)) + " % Correct"
print str(correct) + "/" + str(numFiles)
