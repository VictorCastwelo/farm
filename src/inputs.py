list_inputs = []

id = 1
def register_inputs(name, quantity, unit, category):
    global id
    register = {'ID': id,'Name': name ,'Quantity': quantity ,'Unit': unit ,'Category': category}
    list_inputs.append(register)
    id += 1
    return list_inputs
