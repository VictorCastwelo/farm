import json

def data_save(list_object, name):
    file = open(name, 'w')
    json.dump(list_object, file, ensure_ascii=False ,indent=2)
    file.close()

def data_load(name_file):
    try:
        file = open(name_file, 'r')
        data = json.load(file)
        file.close()
        return data
    except FileExistsError:
        data = []
        return data
    except FileNotFoundError:
        data = []
        return data