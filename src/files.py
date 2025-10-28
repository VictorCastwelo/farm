import json
data_folder = 'data'

def data_save(list_object, name):
    file_path = f'{data_folder}/{name}'

    file = open(file_path, 'w')
    json.dump(list_object, file, ensure_ascii=False, indent=2)
    file.close()

def data_load(name_file):
    file_path = f'{data_folder}/{name_file}'
    
    try:
        file = open(file_path, 'r')
        data = json.load(file)
        file.close()
        return data
    except FileExistsError:
        data = []
        return data
    except FileNotFoundError:
        data = []
        return data
    