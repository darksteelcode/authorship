import numpy as np
import glob, math

from features import base, commonWords, punctuation, sentLength, diversity

FEATURES = [commonWords.CommonWords, punctuation.Punctuation, sentLength.SentenceLength, diversity.Diversity]

class CalcAuthorBatch():
    def __init__(self, dir, sampLength, args=[[]] * len(FEATURES), features=FEATURES, debug=True):
        self.dir = dir
        #Length of each sample, in characters
        self.sampLength = sampLength
        self.args = args
        self.feats = features
        self.debug = debug
        #String Containing all files in dir lumped togeather
        self.txt = ""
        for f in glob.glob(self.dir + "/*.txt"):
            file = open(f)
            self.txt += file.read()
            file.close()
        self.numSamples = math.floor(float(len(self.txt))/float(self.sampLength))

    def getNumSamples(self):
        return self.numSamples

    def calcFeatures(self):
        for i in range(self.numSamples):


a = CalcAuthorBatch("texts/Mark_Twain", 10000)
print a.getNumSamples()
