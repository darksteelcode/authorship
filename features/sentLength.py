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
                print "No ending mark found, using period"
                self.ending = "."
        else:
            self.endings = self.args[0]

    def calc(self):
        self.debugStart()
        self.beginCalc()
        self.checkArgs()
        self.f = np.zeros(1, dtype=np.float32)
        numSents = 0
        #Index of next ending mark (a period)
        endIndex = self.text.find(self.ending)
        #Index of previous ending mark-used to find sentence length
        prevIndex = 0
        while endIndex != -1:
            numSents += 1
            self.f[0] += endIndex - prevIndex
            prevIndex = endIndex
            endIndex = self.text.find(self.ending, prevIndex+1)
        self.f /= numSents
        self.endCalc()
        return self.f

    def debugStart(self):
        if self.debug:
            print "--SentenceLength--"
