import requests
import pickle

# Obtain objects form dataset
with open("../data/objects_dataset.txt") as f:
    file = f.readlines()
    f.close()
objects = list(set([object.strip().replace("/","_").lower() for object in file]))

# Web scraping
url_conceptnet = "http://api.conceptnet.io/c/en/"


object_dict = dict()
n = len(objects)
m = 0

for object in objects:
    response = requests.get(url_conceptnet+object)
    objson = response.json()
    properties = dict()

    cell_len = len(objson['edges'])
    for cell in range(0,cell_len):
        propDef = objson['edges'][cell]['rel']['label']
        propVal = objson['edges'][cell]['end']['label'].lower().replace("the ", "").replace("an ", "").replace("a ", "").strip()

        if propDef not in properties:
            properties[propDef] = list()

            if propVal != object.replace("_", " ").strip():
                properties[propDef].append(propVal)
        else:
            if propVal != object.replace("_", " ").strip():
                properties[propDef].append(propVal)

    for property in list(properties):
        if not properties[property]:
            del properties[property]
        else:
            properties[property] = list(set(properties[property]))

    if properties:
        object_dict[object] = properties

    m+=1
    print(str(m)+"/"+str(n))

with open('../data/objectDict.pkl', 'wb') as f:
    pickle.dump(object_dict, f, 0)

# loading the dict
#with open('../data/objectDict.pkl', 'rb') as f:
#    object_dict = pickle.load(f)