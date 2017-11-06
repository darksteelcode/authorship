import numpy as np
import base
#Args [words, seperators]
#words ia an array of strings to look for
#seperators is an array of acceptable characters on either side of each words
#This is so that, if the word is 'he', it is not counted in 'hello'
class CommonWords(base.BaseFeature):
    def __init__(self, text,  textName="", args=[], debug=True):
        base.BaseFeature.__init__(self, text, textName, args, debug)
        self.wrds = []
        self.sprts = []

    def checkArgs(self):
        if len(self.args) != 2:
            if self.debug:
                print "No word and seperator lists found, using defaults"
            #From Google's Trillion Word Corpus - https://github.com/first20hours/google-10000-english
            self.wrds = ["the","of","and","to","a","in","for","is","on","that","by","this","with","i","you","it","not","or","be","are","from","at","as","your","all","have","new","more","an","was"]
            self.sprts = [" ", ": ", "\"", "'", "?", "!", ".", ","]
        else:
            self.wrds = self.args[0]
            self.sprts = self.args[1]

    def calc(self):
        self.debugStart()
        self.beginCalc()
        self.checkArgs()
        self.f = np.zeros(len(self.wrds), dtype=np.float32)
        #Calculations go here
        wordNum = 0
        for w in self.wrds:
            startIndex = 0
            i = self.text.find(w)
            while i != -1:
                startIndex = i+1
                #Make sure not to check character after word if nothing is after word
                if (not i + len(w) >= len(self.text)):
                    if self.text[i-1] in self.sprts and  self.text[i+len(w)] in self.sprts:
                        self.f[wordNum]+=1
                i = self.text.find(w, startIndex)
            wordNum+=1

        numOfWords = float(self.text.count(" "))
        self.f/=numOfWords
        self.endCalc()
        return self.f

    def debugStart(self):
        if self.debug:
            print "--CommonWordFrequency--"
