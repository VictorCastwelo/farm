import json
def list_recording(list_object, name):
    file = open(name, 'w')
    json.dump(list_object, file)
    file.close()