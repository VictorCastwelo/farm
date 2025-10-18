def search(method, list_object):
    if method == '1':
        choice = int(input('Digite o ID: '))
        
        for item in list_object:
            for key in item:
                if item[key] == choice:
                    return item
    elif method == '2':
        choice = input('Digite o nome: ')

        for item in list_object:
            for key in item:
                if item[key] == choice:
                    return item

def search_animal(method):
    from animals import list_animals
    register = search(method, list_animals)
    return register
    
                
def search_plant(method):
    from plants import list_plants
    register = search(method, list_plants)
    return register

def search_inputs(method):
    from inputs import list_inputs
    register = search(method, list_inputs)
    return register