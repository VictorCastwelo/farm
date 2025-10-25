from datetime import datetime
from reports import search
list_movements = []

def selection_operation(selected, list_object, operation):
    for item in list_object:
        for key in item:
            if item[key] == selected:
                item['Status'] = operation
    return list_object

def operation_register(chosen, list_object, description, operation, type_name):
    item = search(chosen, list_object)
    date = datetime.now()
    formatted_date = date.strftime("%Y-%m-%d")

    operation_registration = {'Data': formatted_date, 'ID': item.get('ID'), 'Nome': item.get(type_name), 'Operação': operation, 'Descrição': description}

    list_movements.append(operation_registration)
    return list_movements

def sell_animal(selected):
    from animals import list_animals
    movement = selection_operation(selected, list_animals, operation= 'Vendido')
    return movement

def harvested_plant(selected):
     from plants import list_plants
     movement = selection_operation(selected, list_plants, operation= 'Colhido')
     return movement

def consumption_input(selected):
     from inputs import list_inputs, out_quantity
     from reports import search
     item = search(selected, list_inputs)
     value_out = item.get('Quantidade')

     movement = out_quantity(value_out, selected)
     return movement

from utils import method_selection
def movements_menu():
    while True:
        print('Selecione uma opção')
        print('1.Venda de Animais')
        print('2.Colheita de Plantas')
        print('3.Consumo de Insumos')
        print('0.Voltar ao menu principal')

        option = input('\n> ')

        if option == '1':
            while True:
                from movements import sell_animal
                from animals import list_animals

                method = method_selection()
                description = input('Digite uma descrição para a operação: ')

                if method == '1':
                    chosen_id = int(input('Digite o ID: '))
                    sell_animal(chosen_id)
                    operation_register(chosen_id, list_animals, description, operation='Venda', type_name='Espécie')

                    print('Operação realizada!\n')
                    break
                elif method == '2':
                    chosen_name = input('Digite o nome da espécie: ')
                    sell_animal(chosen_name)
                    operation_register(chosen_name, list_animals, description, operation='Venda', type_name='Espécie')

                    print('Operação realizada!\n')
                    break
                else:
                    print('Opção inválida! Tente novamente\n')
                    continue
        elif option == '2':
            while True:
                from movements import harvested_plant
                from plants import list_plants

                method = method_selection()
                description = input('Digite uma descrição para a operação: ')

                if method == '1':
                    chosen_id = int(input('Digite o ID: '))
                    harvested_plant(chosen_id)
                    operation_register(chosen_id, list_plants, description, operation='Colheita', type_name='Tipo de cultura')

                    print('Operação realizada!\n')
                    break
                elif method == '2':
                    chosen_name = input('Digite o nome da cultura: ')
                    harvested_plant(chosen_name)
                    operation_register(chosen_name, list_plants, description, operation='Colheita', type_name='Tipo de cultura')

                    print('Operação realizada!\n')
                    break
                else:
                    print('Opção inválida! Tente novamente\n')
                    continue
        elif option == '3':
             while True:
                from movements import consumption_input
                from inputs import list_inputs

                method = method_selection()
                description = input('Digite uma descrição para a operação: ')

                if method == '1':
                    chosen_id = int(input('Digite o ID: '))
                    consumption_input(chosen_id)
                    operation_register(chosen_id, list_inputs, description, operation='Consumo de insumo', type_name='Nome')

                    print('Operação realizada!\n')
                    break
                elif method == '2':
                    chosen_name = input('Digite o nome do insumo: ')
                    consumption_input(chosen_name)
                    operation_register(chosen_name, list_inputs, description, operation='Consumo de insumo', type_name='Nome')

                    print('Operação realizada!\n')
                    break
                else:
                    print('Opção inválida! Tente novamente\n')
                    continue
        elif option == '0':
            print('Voltando...\n')
            break
        else:
            print('Opção inválida! Tente novamente.\n')
            continue
