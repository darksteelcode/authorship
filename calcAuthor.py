import numpy as np
import glob, math

from features import base, commonWords, punctuation, sentLength, diversity

FEATURES = [commonWords.CommonWords, punctuation.Punctuation, sentLength.SentenceLength, diversity.Diversity]

LENGTHS = [commonWords.LENGTH, punctuation.LENGTH, sentLength.LENGTH, diversity.LENGTH]

class CalcAuthorBatch():
    def __init__(self, dir, sampleLength, args=[[]] * len(FEATURES), features=FEATURES, debug=True):
        self.dir = dir
        #Length of each sample, in characters
        self.sampleLength = sampleLength
        self.args = args
        self.feats = features
        self.debug = debug
        #String Containing all files in dir lumped togeather
        self.txt = ""
        for f in glob.glob(self.dir + "/*.txt"):
            file = open(f)
            self.txt += file.read()
            file.close()
        self.numSamples = int(math.floor(float(len(self.txt))/float(self.sampleLength)))
        self.f = np.zeros((self.numSamples, sum(LENGTHS)))

    def getNumSamples(self):
        return self.numSamples

    def calcFeatures(self):
        for i in range(self.numSamples):
            calculatedFeats = []
            for feat in self.feats:
                f = feat(self.txt[i*self.sampleLength:(i+1)*self.sampleLength], self.dir, [], self.debug)
                calculatedFeats.append(f.calc())
            self.f[i] = np.concatenate(calculatedFeats)
            if self.debug:
                print "Training Sample"
                print self.f[i]
        return self.f
