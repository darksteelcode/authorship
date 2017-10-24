import numpy as np
from features import base, commonWords, punctuation

FEATURES = [commonWords.CommonWords, punctuation.Punctuation]

class FeatureCalculator():
    def __init__(self, text, textName="", args=[[]] * len(FEATURES), features=FEATURES, debug=True):
        self.text = text
        self.textName = textName
        self.args = args
        #Features to calculate
        self.feats = features
        self.debug = debug
        #Results of calculations
        self.results = [[]] * len(self.feats)

    def calcFeatures(self):
        if self.debug:
            print "FeatureCalculator started on " + self.textName + " with " + str(len(self.feats)) + " features"
        featIndex = 0
        for f in self.feats:
            feat = self.feats[featIndex](self.text,  self.textName, self.args[featIndex], self.debug)
            self.results[featIndex] = feat.calc()
            featIndex+=1
        if self.debug:
            print "FeatureCalculator finished on " + self.textName
        return self.results
