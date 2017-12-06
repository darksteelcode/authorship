import glob
import calcAuthor
attributions = []
def getAttributions(dir, authors):
    f = open(dir+"/AUTHORS.txt")
    for line in f:
        groups = line.split(":")
        groups[1] = groups[1].replace("\n", "")
        groups[1] = authors.index(groups[1])
        attributions.append(groups)

def getAuthor(text):
    for i in range(len(attributions)):
        if attributions[i][0] == text:
            return attributions[i][1]

def getSamplesAndAuthors(dir, authors, debug):
    getAttributions(dir, authors)
    

getAttributions("texts/Unknown/",["Jane Austen", "Walter Scott", "Arthur Conan Doyle", "Charles Dickens", "Mark Twain", "Louisa Alcott"])
