list_animals = []

id = 1
def register_animals(specie, age, weight, status):
    global id
    register = {'ID': id,'Espécie': specie ,'Anos': age ,'Peso': weight ,'Status': status}
    list_animals.append(register)
    id += 1
    return list_animals

def update_animal(new_states):
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
                          
