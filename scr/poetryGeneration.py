import pickle


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
    return dictio



object_dict = filter_underspecified(object_dict,7)
#objects = (object_dict.keys())


for object in list(object_dict.keys())[0:5]:

    #print(len(object_dict[object]))
    print(object_dict[object])

# [print(field) for field in object_dict[key]]
# [print(object_dict[object][field]) for field in object_dict[object]]
# print(allUniqueInfos)
