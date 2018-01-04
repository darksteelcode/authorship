#Tests right now for word2vec vectors and sorting, not good for use as feature yet
import time
f = open("classes.goodSorted.txt")
text = open("../texts/Charles_Dickens/bleak_house.txt")

def getClass(word, fileData):
    word = word.lower()
    f.seek(0, 0)
    loc = fileData.find(word + ' ')
    if loc == -1:
        return -1
    wordClass = int(fileData[fileData.find(' ', loc)+1:fileData.find('\n', loc)])
    return wordClass


data = text.read()
marks = [".", ",", "'", "\"", ":", ";", "?", "!", "-"]
data = data.replace("\n", " ")
for i in marks:
    data = data.replace(i, "")
data = data.split(' ')


total = len(data)
miss = 0
index = 0

start = time.time()

fileData = f.read()

for i in data:
    index += 1
    if index % 100 == 1:
        print float(index) / float(total)
        print float(miss) / float(index)
    if getClass(i, fileData) == -1:
        miss += 1

print "Time:"
print time.time() - start
