from utils import method_selection
def manage_menu():
    while True:
        
        print('Selecione a categoria')

        print('1.Animais')
        print('2.Plantas')
        print('3.Insumos')
        print('0.Voltar ao menu principal')
        option = input('\n> ')

        if option == '1':
            while True:
                
                print('O que deseja realizar?')

                print('1.Cadastrar animal')
                print('2.Atualizar status de animal')
                print('0.Voltar')
                choice = input('\n> ')

                if choice == '1':
                    from animals import register_animals
                    specie = input('Digite o nome da especie: ')
                    age = int(input('Digite a idade do animal (ANOS): '))
                    weight = float(input('Digite o peso do animal (KG): '))
                    status = input('Digite a situação do animal (ATIVO, VENDIDO OU MORTO): ')
                    register_animals(specie, age, weight, status)


                    print('Animal cadastrado com sucesso!\n')
                elif choice == '2':
                    from animals import update_animal
                    method = method_selection()
                    new_states = input('Digite um novo Status:')
                    update_animal(new_states,method)
                    print("Status atualizado com sucesso!\n")


                elif choice == '0':
                    break
                
        elif option == '2':
            while True:

                print('O que deseja realizar?')
                print('1.Cadastrar plantação')
                print('0.Voltar')
                choice = input('\n> ')

                if choice == '1':
                    from plants import register_plants
                    crop_type = input('Digite o tipo de cultura : ')
                    area = float(input('Tamanho de área cultivada em hectare:' ))
                    planting_date = input('Digite a data de plantio(YYYY-MM-DD): ')
                    harvest_date = input('Digite a data de colheita(YYYY-MM-DD): ')
                    status = input('Digite a situação atual da cultura(PLANTADA, COLHIDA, ROTAÇÃO, INATIVA): ')
                    register_plants(crop_type, area, planting_date, harvest_date, status)
                    print('Plantação cadastrada com sucesso!\n')

                elif choice == '0':
                    print('\nVoltando...\n')
                    break

        elif option == '3':
            while True:
                
                print('O que deseja realizar?')
                print('1.Cadastrar insumo')
                print('2.Registrar entrada')
                print('3.Registrar saída')
                print('0.Voltar')
                choice = input('\n> ')
               
                if choice == '1':
                  from inputs import register_inputs
                  name = input('Digite o nome do insumo: ')
                  quantity = float(input('Quantidade disponível: '))
                  unity = input('Unidade de medida: ')
                  category = input('Classificação do insumo (RAÇÃO, SEMENTE, FERTILIZANTE OU MEDICAMENTO): ')
                  register_inputs(name, quantity, unity, category)
                  print('Insumo cadastrado!\n')

                elif choice == '2':
                    from inputs import entry_quantity
                    method = method_selection()
                    value_entry = int(input('Digite o valor de entrada: '))
                    if method == '1':
                        id_choice = int(input('Digite o id do insumo: '))
                        entry_quantity(value_entry, id_choice)

                    elif method == '2':
                        name_choice = input('Digite o nome do insumo: ')
                        entry_quantity(value_entry, name_choice)
                        print('\nOperação realizada com sucesso!\n')
                
                elif choice == '3':
                    from inputs import out_quantity
                    method = method_selection()
                    value_out = int(input('Digite o valor de saída: '))
                    
                    if method == '1':
                        id_choice = int(input('Digite o id do insumo: '))
                        out_quantity(value_out, id_choice)
                        print('\nOperação realizada com sucesso!\n')
                    elif method == '2':
                        name_choice = input('Digite o nome do insumo: ')
                        out_quantity(value_out, name_choice)
                
                elif choice == '0':
                    print('\nVoltando...\n')
                    break
        
        elif option == '0':
            print('\nVoltando ao menu principal...\n')
            break
        
        else:
            print('Opção inválida. Tente novamente!')
            continue