import json

def data_save(list_object, name):
    file = open(name, 'w')
    json.dump(list_object, file, indent=2)
    file.close()
