import numpy as np
import base

#Sentence length by number of characters

class SentenceLength(base.BaseFeature):
    def __init__(self, text,  textName="", args=[], debug=True):
        base.BaseFeature.__init__(self, text, textName, args, debug)
        self.endings = []

    def checkArgs(self):
        if len(self.args) != 1:
            if self.debug:
                print "No ending marks found, using defaults"
                self.endings = [".", "!", "?"]
        else:
            self.endings = self.args[0]

    def calc(self):
        self.debugStart()
        self.beginCalc()
        self.checkArgs()
        self.f = np.zeros(1, dtype=np.float32)
        numSents = 0;
        for c in self.text:
            if not c in self.endings:
                self.f[0]+=1.0
            else:
                numSents+=1
        self.f /= numSents
        self.endCalc()
        return self.f

    def debugStart(self):
        if self.debug:
            print "--SentenceLength--"
