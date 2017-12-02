import numpy as np
import base

LENGTH = 1

class Diversity(base.BaseFeature):
    def __init__(self, text,  textName="", args=[], debug=True):
        base.BaseFeature.__init__(self, text, textName, args, debug)

    def calc(self):
        self.debugStart()
        self.beginCalc()
        self.f = np.zeros(1, dtype=np.float32)
        words = self.text.split(' ')
        #Need to be removed from words
        puncsToRemove = [".", ",", "'", "\"", ":", ";", "?", "!", "-"]
        cleanWords = []
        for w in words:
            for p in puncsToRemove:
                w = w.replace(p,'')
            cleanWords.append(w)
        # Number of unique words over total number of words
        self.f[0] = float(len(set(cleanWords)))/float(len(cleanWords))
        self.endCalc()
        return self.f

    def debugStart(self):
        if self.debug:
            print "--Diversity--"
