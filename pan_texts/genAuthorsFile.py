import json
import sys

#Convert groudn-truth json files used in pan dataset to AUTHORS.txt that thi project uses

#Command used as so: python genAuthorsFile.py path/to/ground-truth.json path/to/AUTHORS.txt

if len(sys.argv) < 3:
    print "Usage: python genAuthorsFile.py path/to/ground-truth.json path/to/AUTHORS.txt"
    exit()

jsonPath = sys.argv[1]
authorsPath = sys.argv[2]
#Text to write to authors file
out = ""


jsonFile = open(jsonPath)
jsonData = json.loads(jsonFile.read())
jsonFile.close()
attributions = jsonData['ground-truth']
for w in attributions:
    out += w["unknown-text"] + ":" + w["true-author"] + "\n"

outFile = open(authorsPath, 'w')
outFile.write(out)
outFile.close()
