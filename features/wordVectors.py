import numpy as np
import base
#Word Vector Feature - using a alphabetized list of words and their coresponding numerical class, calculated by using k-means clustering on word vectors, calculate frequency of words in each class in the text

#Number of word classes
LENGTH = 500

VECTOR_FILE = open("classes.goodSorted.txt")
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
print "Done"
#Precalculated Vectors using WordVectorsCalculateTwoCharFileIndexes(), used to only have to calculated once for a vector file, instead of at the begining of each run
VECTOR_FILE_INDEXES = [13, 331, 4281, 8510, 12710, 13708, 15310, 16962, 17353, 18619, 18716, 19216, 26669, 30648, 39564, 39701, 43302, 43692, 50552, 55232, 57836, 61289, 62374, 62783, 63027, 63389, 63904, 74802, 74891, 74997, 75072, 83356, 83383, 83425, 83733, 88425, 88505, 88519, 92044, 92127, 92199, 99263, 99305, 99320, 106482, 106573, 106601, 111929, 111944, 111974, 111980, 112388, 112409, 128154, 128223, 128419, 128597, 131915, 132027, 132080, 142589, 145116, 145147, 145211, 149993, 150146, 150304, 182387, 182593, 182600, 188406, 188622, 188781, 192099, 192180, 192203, 192225, 193541, 193728, 198045, 198129, 198211, 198306, 215275, 215314, 215337, 215676, 230046, 230170, 230215, 230258, 230381, 230492, 235327, 235380, 235386, 238269, 238358, 238442, 241082, 241167, 241416, 241437, 242047, 242140, 243393, 243707, 245188, 246360, 246558, 247043, 247480, 247523, 248435, 248553, 248690, 252606, 255662, 262380, 262489, 263876, 264634, 266618, 268980, 270260, 271751, 273458, 273580, 280620, 280876, 280970, 286924, 286938, 286966, 287061, 290528, 290616, 290654, 290668, 295357, 295384, 295390, 299239, 299290, 299319, 304904, -1, 304980, 310141, 310196, 310252, 312810, 312816, 312822, 312828, 312870, 312882, 318114, 318197, 318267, 318353, 323130, 323153, 323175, 323699, 325937, 325954, 325970, 328568, 328676, 328964, 332569, 332680, 332687, 338946, 339061, 339161, 342038, 342045, 342208, 342214, 342717, 342738, 352727, 352806, 352868, 352908, 360727, 360749, 360771, 360785, 364614, 364633, 364649, 364707, 364820, 364843, 371569, 371600, 371606, 371733, 371892, 371984, 374824, 374867, 374927, 374934, 377677, 377690, 377948, 378302, 379098, 380066, 380207, 380358, 380876, 380939, 381039, 381073, 381137, 382171, 386454, 407817, 408142, 408377, 408438, 409978, 411867, 412505, 412614, 412831, 412894, 412930, 412985, 413072, 415832, 415867, 415874, 415921, 417560, 417610, 417617, 417667, 418191, 418208, 418214, 418236, 418259, 418292, 420374, -1, 420422, 420444, 420493, 420541, 422690, 422704, 422710, 422716, -1, 422753, 426996, 427063, 427111, 427140, 429539, 429583, 429617, 430408, 433461, 433485, 433510, 434093, 434140, 434941, 437063, 437111, 437127, 438347, 438407, 438465, 439522, 439571, 439797, 439803, 440004, 440035, 447474, 447512, 447609, 447752, 453828, 453935, 453982, 454023, 461101, 461122, 461147, 461388, 461428, 461466, 466617, -1, 466713, 466751, 466843, 466945, 469531, 469614, 469637, 469669, 470570, 470590, 490332, 490438, 492200, 492287, 502130, 502160, 502203, 502233, 512692, 512747, 512772, 512835, 513001, 513140, 523973, 524155, 524161, 524251, 524487, 524617, 529499, 529551, 529610, 529632, 530698, 530710, 535490, 535549, 535697, 535892, 541544, 541583, 541817, 541884, 544859, 544898, 544959, 545039, 545110, 545197, 550166, 550229, 550236, 550292, 550521, 550685, 552328, 552353, 552385, 552398, 552619, 552663, 552900, 554845, 556038, 556483, 556619, 557416, 557576, 557672, 557882, 557929, 558104, 559054, 559618, 560312, 560400, -1, 562176, 565425, 566581, 566988, 568900, 571469, 571659, 572073, 572121, 572209, 583577, 583641, 583773, 583956, 592628, 592730, 592767, 597047, 600842, 600849, 600905, 604833, 604898, 605083, 613644, 613761, 613767, 629518, 630835, 631002, 634067, 634120, 634163, 634178, -1, 634696, 634932, 634949, 634963, 634978, 635000, -1, 635006, 635012, -1, -1, 635125, 635145, 635176, 635184, 635212, 635220, -1, 635235, 635245, 635251, 638782, 638790, 638811, -1, -1, 638830, 645292, 645322, 645411, 645521, 670187, 670254, 670337, 671215, 674963, 674969, 675010, 675039, 675108, 675222, 680569, 680665, 680682, 680746, 680962, 681122, 683421, 683447, 683485, 683498, 683723, 683786, 692479, 692523, 698697, 698793, 707927, 707991, 708030, 715549, 721302, 721309, 722679, 724893, 726142, 727197, 732470, 738625, 739200, 739388, 739597, 752501, 763853, 764085, 765626, 765640, 768304, 768504, 774478, 774537, 774630, 774669, 780968, 780990, 781013, 786868, 789851, 789857, 789863, 790024, 790071, 790109, 794843, -1, 794878, 804974, 805360, 805495, 807981, 808023, 808546, 808561, 809395, 809500, 809600, 809729, 809843, 810014, 810089, 810134, 810308, 810341, 810402, 810413, 810512, 811125, 811445, 823307, 823316, 824315, 824335, 825287, 826023, 826600, 826651, 826684, 826718, 826725, 826741, 826816, 830285, 830310, 830391, 830447, 834057, 834088, 834111, 834142, 838714, -1, 838721, 838915, 838964, 838977, 840879, -1, 840911, 840994, 841044, 841060, 841306, 841329, 841335, 841341, -1, 841448, 846455, 846476, 846538, 846552, 849995, 850034, 850066, 852079, -1, 856556, 856562, 856616, 856655, 856664, 859515, -1, 859547, 860370, 860377, 860425, -1, 860587, -1, 860632, 860820, 860832, 860928, 860944, 860984, 861006, 861289, 861305, 861311, 861331, 861572, 861578, 861584, 861646, 861684, 861699, 861754, -1, 861786, 861800, 861832, 861848, 861880, -1, 861924, 862108, 862165, 862186, 863120, 863127, 863134, 863140, 863840, 863847, 863868, 863877, -1, -1, 864069, 864078, 864103, 864159, 865120, -1, 865159, 865172, 865215, 865249, 865667, 865706, 865722, 865728, 865743, 865766, 866676, 866689, 866698, 866715, 867558, -1, 867573, 867800, -1, 868293, 868301, 868318, 868327, 868345, -1, 868995, 869005, 869011, 869063, 869080, 869311, 869339, 869457, 869464, 869527, 869533]

class WordVectors(base.BaseFeature):
    def __init__(self, text,  textName="", args=[], debug=True):
        base.BaseFeature.__init__(self, text, textName, args, debug)
        self.num_vector_classes = 500;
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

f = WordVectors("the anvil is good", "Test")
f.calc()
