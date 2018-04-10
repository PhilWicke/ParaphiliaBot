
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

def wordToInvariantWord(normWord):
    invWord = ""
    for cha in normWord:
        if cha == "_":
            invWord = invWord + "[ ]?"
        else:
            invWord = invWord + "[" + cha.lower() + "|" + cha.upper() + "]"
    return invWord

outLines = []
for line in lines:
    word = line[1:].split("\"")[0]
    word = wordToInvariantWord(word)
    line = line.replace("[", "").replace("]", "").replace(":  \"", ":  \"#praise# ").split(":")[1]
    line = "\""+word+"\" :"+line
    outLines.append(line)

with open(pathReplyFile, "w") as outFile:
    outFile.writelines(outLines)

print(outLines)