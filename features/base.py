import numpy as np
#numpy is used for later classifiers
#Note: this is just a template with all required methods
#text is the text represented as a string
#textName is optional, indicate sthe name of the text, used for debug
#args are aditional arguments for the feature calculator
#debug indicates wheter to display debug info
#f is features
class BaseFeature():
    def __init__(self, text,  textName="", args=[], debug=True):
        self.text = text.lower()
        self.args = args
        self.debug = debug
        self.textName = textName
        #Features, not yet calculated
        self.f = np.array([])

    def debugStart(self):
        if self.debug:
            print "--BaseFeatures--"

    def beginCalc(self):
        if self.debug:
            print "Feature calculation begining on " + self.textName
            print "------"

    def endCalc(self):
        if self.debug:
            print "Feature calculation finished on " + self.textName
            print "Features Calculated:"
            print self.f
            print

    def calc(self):
        self.debugStart()
        self.beginCalc()
        #Calculations go here
        self.endCalc()
        return self.f

    def getFeatures(self):
        return self.f

    def setText(self, text):
        if self.debug:
            print self.textName + "'s text set."
        self.text = text.lower()

    def setName(self, name):
        if self.debug:
            print "Name set to: " + self.textName
