def dif_dates(date_initial, date_final):
    date_final = date_final.split('-')
    date_initial = date_initial.split('-')

    dif_day = int(date_final[2]) - int(date_initial[2])
    dif_month = int(date_final[1]) - int(date_initial[1])
    dif_year = int(date_final[0]) - int(date_initial[0])

    total = (dif_year * 365) + (dif_month * 30) + dif_day
    return total



list_plants = []

id = 1
def register_plants(crop_type, area, planting_date, harvest_date, status):
    global id
    day_haverst = dif_dates(planting_date,harvest_date)

    register = {'ID': id,'Tipo de cultura': crop_type ,'Área': area ,'Data de plantio': planting_date ,'Data da colheita': harvest_date ,'Status': status, 'Dia para a colheita': day_haverst}
    
    list_plants.append(register)
    id += 1
    return list_plants
