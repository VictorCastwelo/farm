from files import data_load

list_animals = data_load('animals.json')

def register_animals(specie, age, weight, status):
    if len(list_animals) >= 1:
        id = list_animals[-1].get('ID') + 1
    else:
        id = 1

    register = {'ID': id,'Espécie': specie ,'Anos': age ,'Peso': weight ,'Status': status}
    list_animals.append(register)
    id += 1
    
    return list_animals

def update_animal(new_states, choice):
    if choice == '1':
        updates = int(input('Digite o ID: '))   
        for item in list_animals:
            for key in item:
                if item[key] == updates:
                    item['Status'] = new_states
                    return list_animals
    elif choice == '2':
        updates = input('Digite a especie do animal: ')
        for item in list_animals:
            for key in item:
                if item[key] == updates:
                    item['Status'] = new_states
                    return list_animals
                          
