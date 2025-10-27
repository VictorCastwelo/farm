from files import data_load

list_inputs = data_load('inputs.json')



def register_inputs(name, quantity, unit, category):
    if len(list_inputs) >= 1:
        id = list_inputs[-1].get('ID') + 1
    else:
        id = 1
        
    register = {'ID': id,'Nome': name ,'Quantidade': quantity ,'Unidade': unit ,'Categoria': category}
    list_inputs.append(register)
    id += 1
    return list_inputs

def entry_quantity(value_entry, chosen):
    origin_value = 0
    for item in list_inputs:
        for key in item:
            if item[key] == chosen:
                
                origin_value = item.get('Quantidade') 
                new_value = value_entry + origin_value
                item['Quantidade'] = new_value

    return list_inputs

def out_quantity(value_out, chosen):
    origin_value = 0
    for item in list_inputs:
        for key in item:
            if item[key] == chosen:
                
                origin_value = item.get('Quantidade') 
                if value_out > origin_value:
                    return 'Valor acima da quantidade disponível'
            
                new_value = origin_value - value_out
                item['Quantidade'] = new_value
                
    return list_inputs
