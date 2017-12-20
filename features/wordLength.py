import numpy as np
import base

LENGTH = 1

#Word length by number of characters

class WordLength(base.BaseFeature):
    def __init__(self, text,  textName="", args=[], debug=True):
        base.BaseFeature.__init__(self, text, textName, args, debug)
        self.seperator = " "

    def checkArgs(self):
        if len(self.args) != 1:
            if self.debug:
                print "No seperating mark found, using space"
                self.seperator = " "
        else:
            self.seperator = self.args[0]

    def calc(self):
        self.debugStart()
        self.beginCalc()
        self.checkArgs()
        self.f = np.zeros(1)
        numWords = 0
        #Index of next seperating mark (a space)
        endIndex = self.text.find(self.seperator)
        #Index of previous seperating mark-used to find word length
        prevIndex = 0
        while endIndex != -1:
            numWords += 1
            self.f[0] += endIndex - prevIndex
            prevIndex = endIndex
            endIndex = self.text.find(self.seperator, prevIndex+1)
        self.f /= numWords
        self.endCalc()
        return self.f

    def debugStart(self):
        if self.debug:
            print "--WordLength--"
