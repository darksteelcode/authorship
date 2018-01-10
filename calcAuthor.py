import numpy as np
import glob, math

#Calculate features for a directory of texts, or text, ditermined by isDir with a given sample length - or whole file, ditermined by oneSample - results are inpts to neural netrwork classifier

from features import base, commonWords, punctuation, sentLength, diversity, wordLength, wordVectors

FEATURES = [commonWords.CommonWords, punctuation.Punctuation, sentLength.SentenceLength, diversity.Diversity, wordLength.WordLength, wordVectors.WordVectors]

LENGTHS = [commonWords.LENGTH, punctuation.LENGTH, sentLength.LENGTH, diversity.LENGTH, wordLength.LENGTH, wordVectors.LENGTH]

class CalcAuthorBatch():
    def __init__(self, file, isDir, sampleLength, oneSample, args=[[]] * len(FEATURES), features=FEATURES, debug=True):
        self.dir = file
        #Length of each sample, in characters
        self.sampleLength = sampleLength
        self.args = args
        self.feats = features
        self.debug = debug
        self.isDir = isDir
        self.oneSample = oneSample
        #Used to limit length of text for testing
        self.limitLength = False
        self.lengthLimit = 50000
        #String Containing all files in dir lumped togeather
        self.txt = ""
        if self.isDir:
            for f in glob.glob(self.dir + "/*.txt"):
                file = open(f)
                self.txt += file.read()
                file.close()
        else:
            file = open(self.dir)
            self.txt += file.read()
            file.close()
        if self.limitLength:
            self.txt = self.txt[:self.lengthLimit]
        self.numSamples = int(math.floor(float(len(self.txt))/float(self.sampleLength)))
        if self.oneSample:
            self.numSamples = 1
        self.f = np.zeros((self.numSamples, sum(LENGTHS)))

    def getNumSamples(self):
        return self.numSamples

    def calcFeatures(self):
        for i in range(self.numSamples):
            calculatedFeats = []
            for feat in self.feats:
                if not self.oneSample:
                    f = feat(self.txt[i*self.sampleLength:(i+1)*self.sampleLength], self.dir, [], self.debug)
                else:
                    f = feat(self.txt, self.dir, [], self.debug)
                calculatedFeats.append(f.calc())
            self.f[i] = np.concatenate(calculatedFeats)
            if self.debug:
                print "Training Sample"
                print self.f[i]
        return self.f
