def search(chosen, list_object):
        for item in list_object:
            for key in item:
                if item[key] == chosen:
                    return item


def search_animal(chosen):
    from animals import list_animals
    item_chosen = search(chosen, list_animals)
    return item_chosen
    
                
def search_plant(chosen):
    from plants import list_plants
    item_chosen = search(chosen, list_plants)
    return item_chosen

def search_inputs(chosen):
    from inputs import list_inputs
    item_chosen = search(chosen, list_inputs)
    return item_chosen