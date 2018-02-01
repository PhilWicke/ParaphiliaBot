import pickle
import json


with open('../data/objectDict.pkl', 'rb') as f:
    object_dict = pickle.load(f)


def filter_underspecified(dictio, threshold):
    counter = 0
    for object in list(dictio.keys()):
        allUniqueInfos = list()
        allUniqueInfos = [dictio[object][field] for field in dictio[object]]
        allUniqueInfos = [elem for elems in allUniqueInfos for elem in elems if not elem == object]

        # there is not enough information to create a poem
        if len(allUniqueInfos) < threshold:
            dictio.pop(object, None)
            counter += 1

    print(str(counter)+" objects filtered out. "+str(len(list(dictio.keys()))-counter)+" remain.")
    print()
    return dictio



object_dict = filter_underspecified(object_dict,7)
#objects = (object_dict.keys())


# Generate object line --- START
list_of_objects = list(object_dict.keys())
list_of_objects_spaced = [obj.replace("_"," ") for obj in list_of_objects]
GR_poemObject = "\"poemObject\": ["
for val in list_of_objects_spaced:
    GR_poemObject += "#"+val+"#,"
GR_poemObject = GR_poemObject[:-1]
GR_poemObject += "],"
print(GR_poemObject)
print()
# Generate object line --- STOP

GR_propertyList = list()

for object in list(object_dict.keys())[0:5]:

    # "object": [ "object. #AtLocationPhrase_object#, #ReceivesActionPhrase_object#,
    finalString = "\""+object+"\" : [ \""+object+". "

    #print(object)
    #print(len(object_dict[object]))
    list_of_properties = object_dict[object]
    #print(list_of_properties)
    for proper in list_of_properties:
        finalString += "#"+proper+"_"+object+"#, "
        #print(proper)
    finalString = finalString[:-1]+"]"
    print(finalString)

# [print(field) for field in object_dict[key]]
# [print(object_dict[object][field]) for field in object_dict[object]]
# print(allUniqueInfos)"object001": [ "object001. #AtLocationPhrase001#, #ReceivesActionPhrase001#,

#print(object_dict)
#
# temp={}
# for k,v in object_dict.items():
#     data = "\""+k+'. '+', '.join(["#" + k1 + "_" + k + "#" for k1,v1 in v.items()])
#     #print(data)
#     temp[k]=data
# #    break
#
#
# json_data = json.dumps(temp)
#
# print("HERE: "+json_data)