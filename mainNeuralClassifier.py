import numpy as np
import calcFeatures
import calcAuthor
import AUTHORS
from classifiers import neural
debug = True
authors = ["Jane Austen", "Walter Scott", "Arthur Conan Doyle", "Charles Dickens", "Mark Twain", "Louisa Alcott"]
#Index coresponds to authors array
textDirs = ["texts/Jane_Austen", "texts/Walter_Scott", "texts/Arthur_Doyle", "texts/Charles_Dickens", "texts/Mark_Twain", "texts/Louisa_Alcott"]
unknownDir = "texts/Unknown"
sampleLength = 100000
#array of CalcAuthorBatch results
featuresCalculated = []
#Features Authors
featuresAuthors = []
authorNum = 0
for directory in textDirs:
    c = calcAuthor.CalcAuthorBatch(directory, True, sampleLength, False)
    featuresCalculated.append(c.calcFeatures())
    featuresAuthors.append(np.zeros(c.getNumSamples(), dtype=np.int))
    featuresAuthors[len(featuresAuthors)-1].fill(authorNum)
    authorNum+=1

#Numpy Array of feature samples
samples = np.concatenate(featuresCalculated)
#Numpy Array of feature sample's authors
sampleAuthors = np.concatenate(featuresAuthors)

classifier = neural.NeuralNetworkClassifier(sum(calcAuthor.LENGTHS), len(textDirs))
classifier.train(samples, sampleAuthors)
trainingAccuracy = classifier.testAccuracy(samples, sampleAuthors)

testSamples, testSamplesAuthors = AUTHORS.getSamplesAndAuthors("texts/Unknown", authors, debug)

unknownAccuracy = classifier.testAccuracy(testSamples, testSamplesAuthors)

print str(round(trainingAccuracy*100)) + "% Accuracy on short training samples with noise"
print str(round(unknownAccuracy*100)) + "% Accuracy on Unknown Texts"
