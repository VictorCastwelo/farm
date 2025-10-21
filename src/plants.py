list_plants = []

id = 1
def register_plants(crop_type, area, planting_date, harvest_date, status):
    global id
    register = {'ID': id,'Tipo de cultura': crop_type ,'Área': area , 'Data de plantio': planting_date, 'Data da colheita': harvest_date , 'Status': status}
    list_plants.append(register)
    id += 1
    return list_plants
