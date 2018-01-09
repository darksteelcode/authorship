import numpy as np
import base
#Word Vector Feature - using a alphabetized list of words and their coresponding numerical class, calculated by using k-means clustering on word vectors, calculate frequency of words in each class in the text

#Number of word classes
LENGTH = 50

VECTOR_FILE = open("features/classes_sorted.txt")
VECTOR_FILE_DATA = VECTOR_FILE.read()

#Calculated the index of each two char combination of lowercase letters in the vector file, then, when searching for word class, start at index of first two chras of word and serach from there
def WordVectorsCalculateTwoCharFileIndexes():
    indexes = []
    #First Char
    #97-122 is ascii for lowercase characters
    for c1 in range(97, 123):
        #Second Char
        for c2 in range(97, 123):
            VECTOR_FILE.seek(0, 0)
            prefix = chr(c1) + chr(c2)
            l = VECTOR_FILE.readline()
            #Use last index, as .tell() returns position at end of current line, index table needs position before beginning of line
            p_index = 0
            while l != '':
                if l[:2] == prefix:
                    indexes.append(p_index)
                    break
                #If location in file is past prefix, no words with prefix are in file, set index to -1
                if (ord(l[0])-97)*26 + (ord(l[1])-97) > (ord(prefix[0])-97)*26 + (ord(prefix[1])-97):
                    indexes.append(-1)
                    break
                p_index = VECTOR_FILE.tell()
                l = VECTOR_FILE.readline()
    #Add End of file index
    indexes.append(VECTOR_FILE.tell())
    return indexes

print "Generating Word Vector Optomization table..."
#VECTOR_FILE_INDEXES = WordVectorsCalculateTwoCharFileIndexes()
#print VECTOR_FILE_INDEXES
#exit()
print "Done"
#Precalculated Vectors using WordVectorsCalculateTwoCharFileIndexes(), used to only have to calculated once for a vector file, instead of at the begining of each run
VECTOR_FILE_INDEXES = [12, 306, 3962, 7859, 11726, 12628, 14101, 15587, 15935, 17104, 17189, 17645, 24513, 28154, 36396, 36517, 39864, 40215, 46565, 50860, 53249, 56472, 57469, 57829, 58051, 58383, 58856, 68896, 68979, 69072, 69139, 76764, 76791, 76829, 77112, 81430, 81503, 81516, 84749, 84827, 84891, 91370, 91412, 91425, 98034, 98122, 98149, 103019, 103032, 103060, 103066, 103434, 103453, 118013, 118075, 118253, 118413, 121457, 121556, 121605, 131343, 133665, 133693, 133750, 138139, 138278, 138419, 168283, 168463, 168468, 173790, 173986, 174128, 177188, 177259, 177280, 177300, 178495, 178664, 182605, 182686, 182759, 182848, 198441, 198476, 198497, 198808, 212114, 212225, 212264, 212305, 212417, 212516, 216919, 216968, 216974, 219585, 219668, 219747, 222163, 222236, 222461, 222481, 223044, 223128, 224267, 224550, 225903, 226975, 227150, 227592, 227990, 228030, 228869, 228977, 229098, 232720, 235522, 241683, 241775, 243052, 243752, 245527, 247703, 248881, 250257, 251820, 251928, 258447, 258675, 258758, 264162, 264175, 264201, 264283, 267463, 267540, 267575, 267588, 271926, 271950, 271956, 275500, 275544, 275570, 280699, -1, 280767, 285551, 285600, 285647, 287986, 287992, 287998, 288004, 288043, 288054, 292853, 292929, 292993, 293072, 297483, 297503, 297522, 298004, 300068, 300083, 300096, 302470, 302568, 302831, 306130, 306230, 306236, 311997, 312100, 312188, 314829, 314834, 314983, 314989, 315461, 315479, 324650, 324721, 324776, 324810, 331988, 332008, 332027, 332040, 335559, 335575, 335590, 335641, 335742, 335761, 341941, 341969, 341975, 342087, 342228, 342310, 344882, 344918, 344971, 344977, 347526, 347536, 347764, 348083, 348803, 349699, 349828, 349966, 350428, 350484, 350575, 350607, 350660, 351611, 355574, 375420, 375713, 375930, 375985, 377392, 379123, 379714, 379811, 380011, 380067, 380100, 380151, 380228, 382739, 382773, 382779, 382820, 384329, 384375, 384380, 384425, 384897, 384913, 384919, 384939, 384958, 384986, 386884, -1, 386926, 386946, 386993, 387036, 389004, 389018, 389024, 389030, -1, 389065, 392945, 393004, 393047, 393073, 395261, 395299, 395332, 396060, 398881, 398903, 398924, 399456, 399498, 400228, 402164, 402208, 402222, 403325, 403377, 403427, 404393, 404435, 404637, 404643, 404825, 404852, 411670, 411706, 411793, 411917, 417484, 417580, 417622, 417656, 424157, 424174, 424195, 424414, 424450, 424485, 429189, -1, 429274, 429308, 429391, 429478, 431846, 431918, 431937, 431970, 432783, 432801, 451007, 451106, 452718, 452794, 461863, 461889, 461929, 461955, 471629, 471677, 471702, 471757, 471911, 472034, 482022, 482182, 482188, 482264, 482477, 482595, 487102, 487151, 487203, 487223, 488191, 488202, 492565, 492618, 492752, 492923, 498138, 498172, 498375, 498433, 501165, 501199, 501251, 501322, 501386, 501460, 506045, 506103, 506109, 506158, 506361, 506512, 508024, 508046, 508074, 508087, 508287, 508323, 508529, 510317, 511413, 511816, 511938, 512662, 512805, 512890, 513080, 513122, 513281, 514159, 514675, 515308, 515385, -1, 517040, 520031, 521085, 521450, 523197, 525563, 525724, 526103, 526146, 526227, 536747, 536807, 536922, 537083, 545082, 545175, 545209, 549173, 552664, 552670, 552717, 556324, 556383, 556550, 564461, 564566, 564572, 579174, 580418, 580567, 583382, 583430, 583467, 583480, -1, 583954, 584171, 584187, 584199, 584213, 584233, -1, 584239, 584245, -1, -1, 584347, 584365, 584394, 584401, 584426, 584433, -1, 584448, 584457, 584463, 587726, 587733, 587752, -1, -1, 587769, 593672, 593700, 593783, 593880, 616588, 616649, 616724, 617532, 620961, 620967, 621002, 621029, 621089, 621188, 626088, 626173, 626188, 626242, 626431, 626571, 628668, 628689, 628721, 628734, 628939, 628994, 636974, 637014, 642734, 642821, 651233, 651292, 651326, 658168, 663461, 663466, 664724, 666743, 667891, 668835, 673690, 679362, 679884, 680052, 680234, 692046, 702527, 702738, 704140, 704153, 706619, 706791, 712229, 712280, 712364, 712399, 718210, 718230, 718250, 723624, 726350, 726356, 726361, 726507, 726549, 726581, 730923, -1, 730954, 740271, 740621, 740741, 743016, 743054, 743539, 743552, 744321, 744416, 744504, 744624, 744726, 744873, 744942, 744987, 745144, 745173, 745231, 745241, 745333, 745899, 746193, 757196, 757204, 758115, 758133, 758988, 759660, 760177, 760223, 760253, 760283, 760289, 760304, 760374, 763599, 763624, 763698, 763748, 767081, 767108, 767129, 767157, 771382, -1, 771388, 771565, 771609, 771622, 773379, -1, 773407, 773481, 773528, 773542, 773768, 773787, 773793, 773799, -1, 773897, 778428, 778448, 778504, 778517, 781702, 781737, 781765, 783596, -1, 787714, 787720, 787767, 787801, 787809, 790420, -1, 790448, 791203, 791209, 791249, -1, 791399, -1, 791441, 791610, 791621, 791709, 791723, 791761, 791782, 792040, 792055, 792061, 792079, 792302, 792308, 792314, 792382, 792417, 792431, 792480, -1, 792510, 792523, 792553, 792567, 792595, -1, 792639, 792834, 792887, 792908, 793755, 793761, 793767, 793773, 794405, 794411, 794429, 794437, -1, -1, 794612, 794621, 794641, 794689, 795566, -1, 795603, 795615, 795653, 795684, 796067, 796102, 796115, 796121, 796135, 796157, 796976, 796988, 796996, 797012, 797786, -1, 797799, 798008, -1, 798453, 798460, 798473, 798480, 798496, -1, 799082, 799091, 799096, 799143, 799158, 799367, 799393, 799500, 799506, 799563, 799569]

class WordVectors(base.BaseFeature):
    def __init__(self, text,  textName="", args=[], debug=True):
        base.BaseFeature.__init__(self, text, textName, args, debug)
        self.num_vector_classes = 50;
        self.words = []

    def preProcessText(self):
        if self.debug:
            print "Preprosessing Text"
        marks = [".", ",", "'", "\"", ":", ";", "?", "!", "-"]
        self.text = self.text.replace("\n", " ")
        for i in marks:
            self.text = self.text.replace(i, "")
        self.words = self.text.split(' ')

    def getClass(self, word):
        word = word.lower()
        #Don't count words less than two chars, and only use words with first two chars being characters (97-122 is ascii for lowercase chars)
        if len(word) < 2 or ord(word[0]) < 97 or ord(word[0]) > 122 or ord(word[1]) < 97 or ord(word[1]) > 122:
            return -1
        indexLoc = (ord(word[0])-97)*26 + (ord(word[1])-97)
        index = VECTOR_FILE_INDEXES[indexLoc]
        if index == -1:
            return -1
        #Start looking for the word at index specified by the index lookup table
        loc = VECTOR_FILE_DATA.find(word + ' ', index)
        if loc == -1:
            return -1
        #Extracts class as int from line with word
        wordClass = int(VECTOR_FILE_DATA[VECTOR_FILE_DATA.find(' ', loc)+1:VECTOR_FILE_DATA.find('\n', loc)])
        return wordClass

    def calc(self):
        self.debugStart()
        self.beginCalc()
        self.f = np.zeros(self.num_vector_classes)
        self.preProcessText()
        for w in self.words:
            wordClass = self.getClass(w)
            if wordClass != -1:
                self.f[wordClass] += 1
        self.f /= len(self.words)
        self.endCalc()
        return self.f

    def debugStart(self):
        if self.debug:
            print "--WordVectors--"
