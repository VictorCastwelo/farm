def selection_operation(selected, list_object, operation):
        for item in list_object:
            for key in item:
                if item[key] == selected:
                    item['Status'] = operation
        return list_object

    

def sell_animal(selected):
    from animals import list_animals
    movement = selection_operation(selected, list_animals, operation= 'Vendido')
    return movement

def harvested_plant(selected):
     from plants import list_plants
     movement = selection_operation(selected, list_plants, operation= 'Colhido')
     return movement

def consumption_input(selected):
     from inputs import list_inputs
     movement = selection_operation(selected, list_inputs, operation= 'Consumido')
     return movement