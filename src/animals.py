list_animals = []

id = 1
def register_animals(specie, age, weight, status):
    global id
    register = {'ID': id,'Espécie': specie ,'Idade': age ,'Peso': weight ,'Status': status}
    list_animals.append(register)
    id += 1
    return list_animals