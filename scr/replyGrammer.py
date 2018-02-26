
pathReplyFile = "../data/replyFile01.txt"
pathGrammar   = "../data/grammar01.txt"

lines = []
with open(pathGrammar, "r") as inFile:
    for i in range(0,3):
        inFile.readline()
    proceed = True
    while proceed:
        line = inFile.readline()
        if "#[word:#" not in line:
            lines.append(line)
        else:
            proceed = False

#TODO: Make this file case sensitive e.g. "boat" -> "[b|B][o|O][a|A][t|T]"

outLines = []
for line in lines:
    outLines.append(line.replace("[", "").replace("]", "").replace(":  \"", ":  \"#praise# "))

with open(pathReplyFile, "w") as outFile:
    outFile.writelines(outLines)

print(outLines)