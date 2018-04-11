import pickle
import json


with open('../data/objectDict.pkl', 'rb') as f:
    object_dict = pickle.load(f)


def filter_underspecified(dictio, threshold):
    counter = 0

    for object in list(dictio.keys()):
        allUniqueInfos = list()
        allUniqueInfos = [dictio[object][field] for field in dictio[object]]
        allUniqueInfos = [elem for elems in allUniqueInfos for elem in elems if not elem.lower().replace("the ","").replace("a ","").strip() == object.replace("_"," ").strip()]
        # there is not enough information to create a poem
        if len(allUniqueInfos) < threshold:
            dictio.pop(object, None)
            counter += 1

    print(str(counter)+" objects filtered out.")# "+str(len(list(dictio.keys()))-counter)+" remain.")
    return dictio


print("Number of objects: "+str(len(object_dict)))
object_dict = filter_underspecified(object_dict,6)
GR_origin = "{\"origin\": [\"#praise# #poemObject#\"],"
GR_praise = "\"praise\": [\"Oh, \", \"My dear \", \"Precious \",  \"Beloved \",  \"I love you \",  \"My dearest \",  \"I'm obsessed with you, \",  \"I cannot stop to think about you, \",  \"Dear \",  \"I adore you \",  \"All my thoughts are about you, \"],"



# Generate object line --- START
list_of_objects = list(object_dict.keys())
list_of_objects_spaced = [obj.replace("_"," ") for obj in list_of_objects]
GR_poemObject = "\"poemObject\": ["
for val in list_of_objects_spaced:
    GR_poemObject += "\"#"+val.replace(" ","_")+"#\","
GR_poemObject = GR_poemObject[:-1]
GR_poemObject += "],"
# Generate object line --- STOP

GR_propertyList = list()
GR_defineProperty = list()
GR_terminalProperties = list()
GR_terminalObjectRelations = list()

properties = set()
for object in list(object_dict.keys()):
    list_of_properties = object_dict[object]
    for elem in list_of_properties:
        properties.add(elem)
for elem in properties:
    GR_terminalProperties.append("\""+elem+"\" : [\"DEFINE\"]")

too_long = 0
too_long_threshold = 5

for object in list(object_dict.keys()):

    # "object": [ "object. #AtLocationPhrase_object#, #ReceivesActionPhrase_object#,
    propString = "\"" + object + "\" : [ \"" + object.replace("_"," ") + ". "
    list_of_properties = object_dict[object]
    count = 0

    for proper in list_of_properties:
        if count < too_long_threshold:

            propString += "#" + proper + "Phrase_" + object + "# "
            defString = "\""+ proper + "Phrase_" + object + "\" : [ \"#[word:#" + proper + "_" + object + "#]" + proper + "#.\"]"
            GR_defineProperty.append(defString)
            temp = [val.replace("\"","") for val in object_dict[object][proper]]
            GR_terminalObjectRelations.append("\""+ proper + "_" + object + "\" : [ \""+"\",\"".join(temp)+"\"]")

        else:
            too_long += 1

        count+=1

    propString = propString[:-1] + "\" @HatingBot "+object+"]"
    GR_propertyList.append(propString)

print("Too many information for "+str(too_long)+" objects (threshold: "+str(too_long_threshold)+").")

#print(GR_propertyList)
#print(GR_terminalProperties)
#print(GR_defineProperty)
#print(GR_terminalObjectRelations)

with open("../data/grammar01.txt", "w") as out:
    out.write(GR_origin + "\n")
    out.write(GR_praise + "\n")
    out.write(GR_poemObject+"\n")

    def writeOut(GR_list):
        for elem in GR_list:
            for line in elem:
                out.write(line+",\n")

    writeOut([GR_propertyList, GR_defineProperty, GR_terminalProperties])

    # add bracket "}" and omit "," for very last element
    lastLine = len(GR_terminalObjectRelations)-1
    for lineNum, line in enumerate(GR_terminalObjectRelations):
        if lineNum<lastLine:
            out.write(line+",\n")
        else:
            out.write(line+"\n}")

