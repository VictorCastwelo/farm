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
                
                method = method_selection()
                if method == '1':
                    chosen_id = int(input('Digite o ID: '))
                    sell_animal(chosen_id)
                    print('Operação realizada!\n')
                    break
                elif method == '2':
                    chosen_name = input('Digite o nome da espécie: ')
                    sell_animal(chosen_name)
                    print('Operação realizada!\n')
                    break
                else:
                    print('Opção inválida! Tente novamente\n')
                    continue
        elif option == '2':
            while True:
                from movements import harvested_plant
                
                method = method_selection()
                if method == '1':
                    chosen_id = int(input('Digite o ID: '))
                    harvested_plant(chosen_id)
                    print('Operação realizada!\n')
                    break
                elif method == '2':
                    chosen_name = input('Digite o nome da cultura: ')
                    harvested_plant(chosen_name)
                    print('Operação realizada!\n')
                    break
                else:
                    print('Opção inválida! Tente novamente\n')
                    continue
        elif option == '3':
             while True:
                from movements import consumption_input
                
                method = method_selection()
                if method == '1':
                    chosen_id = int(input('Digite o ID: '))
                    consumption_input(chosen_id)
                    print('Operação realizada!\n')
                    break
                elif method == '2':
                    chosen_name = input('Digite o nome do insumo: ')
                    consumption_input(chosen_name)
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
