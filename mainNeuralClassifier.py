import numpy as np
import calcFeatures
import calcAuthor
debug = True
authors = ["Jane Austen", "Walter Scott", "Arthur Conan Doyle", "Charles Dickens", "Mark Twain", "Louisa Alcott"]
#Index coresponds to authors array
textDirs = ["texts/Jane_Austen", "texts/Walter_Scott", "texts/Arthur_Doyle", "texts/Charles_Dickens", "texts/Mark_Twain", "texts/Louisa_Alcott"]
sampleLength = 1000000
#array of CalcAuthorBatch results
featuresCalculated = []
#Features Authors
featuresAuthors = []
authorNum = 0
for directory in textDirs:
    c = calcAuthor.CalcAuthorBatch(directory, sampleLength)
    featuresCalculated.append(c.calcFeatures())
    featuresAuthors.append(np.zeros(c.getNumSamples()))
    featuresAuthors[len(featuresAuthors)-1].fill(authorNum)
    authorNum+=1

#Numpy Array of feature samples
samples = np.concatenate(featuresCalculated)
#Numpy Array of feature sample's authors
authors = np.concatenate(featuresAuthors)
