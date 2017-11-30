import numpy as np

import numpy as np
from features import base, commonWords, punctuation, sentLength, diversity

FEATURES = [commonWords.CommonWords, punctuation.Punctuation, sentLength.SentenceLength, diversity.Diversity]

class CalcAuthorBatch():
    def __init__(self, dir, sampLength, args=[[]] * len(FEATURES), features=FEATURES, debug=True):
        self.dir = dir
        #Length of each sample, in characters
        self.sampLength = sampLength
        self.args = args
        self.feats = features
        self.debug = debug
        #String Containing all files in dir lumped togeather
        self.txt = ""
        for f in glob.glob(self.dir + "/*.txt"):
            file = open(f)
            self.txt += file.read()
            file.close()
        self.numSamples = floor(len(self.txt)/self.sampLength)
