import numpy as np
import base

class Punctuation(base.BaseFeature):
    def __init__(self, text,  textName="", args=[], debug=True):
        base.BaseFeature.__init__(self, text, textName, args, debug)
        self.puncs = []

    def checkArgs(self):
        if len(self.args) != 1:
            if self.debug:
                print "No punctuation marks found, using defaults"
                self.puncs = [".", ",", "'", "\"", ":", ";", "?", "!", "-"]
        else:
            self.puncs = self.args[0]

    def calc(self):
        self.debugStart()
        self.beginCalc()
        self.checkArgs()
        #Add Calcs here for punctuation
        self.endCalc()
        return self.f

    def debugStart(self):
        if self.debug:
            print "--PunctuationFrequency--"
