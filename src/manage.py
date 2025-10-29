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
                    try:
                        while True:
                            options_status = ('ativo','vendido','morto')    
                            specie = input('Digite o nome da especie: ')
                            age = int(input('Digite a idade do animal (ANOS): '))
                            weight = float(input('Digite o peso do animal (KG): '))
                            status = input('Digite a situação do animal (ATIVO, VENDIDO OU MORTO): ').lower()
                                
                            if status not in options_status:
                                print('\nStatus inválido! Tente novamente\n')
                                continue
                                
                            register_animals(specie, age, weight, status)
                            print('\nAnimal cadastrado com sucesso!\n')
                            break
                        
                    except ValueError:
                        print('\nInformação Invalida, Tente Novamente!\n')
                        continue
                    
                elif choice == '2':
                    from animals import update_animal
                    method = method_selection()
                    options_status = ('ativo','vendido','morto') 
                    new_status = input('Digite um novo Status (ATIVO, VENDIDO OU MORTO): ')
                    
                    if new_status not in options_status:
                        print('\nStatus inválido! Tente novamente\n')
                        continue

                    update_animal(new_status,method)
                    print("\nStatus atualizado com sucesso!\n")

                elif choice == '0':
                    print('\nVoltando...\n')
                    break
                else:
                    print('\nOpção inválida! Tente novamente\n')
                    continue

        elif option == '2':
            while True:
                print('O que deseja realizar?')
                print('1.Cadastrar plantação')
                print('0.Voltar')
                choice = input('\n> ')
                
                if choice == '1':
                    from plants import register_plants
                    status_options = ('plantada', 'colhida', 'rotação', 'inativa')
                    try:
                        while True:
                            crop_type = input('Digite o tipo de cultura : ')
                            area = float(input('Tamanho de área cultivada em hectare: '))
                            planting_date = input('Digite a data de plantio(YYYY-MM-DD): ')
                            harvest_date = input('Digite a data de colheita(YYYY-MM-DD): ')
                                    
                            if planting_date.isnumeric() and harvest_date.isnumeric():
                                print('\nDatas preenchidas incorretamente! Tente novamente e siga o formato YYYY-MM-DD\n')
                                continue

                            status = input('Digite a situação atual da cultura (PLANTADA, COLHIDA, ROTAÇÃO, INATIVA): ').lower()

                            if status not in status_options:
                                print('\nStatus inválido! Tente novamente\n')
                                continue

                            register_plants(crop_type, area, planting_date, harvest_date, status)
                            print('\nPlantação cadastrada com sucesso!\n')
                            break

                    except ValueError:
                        print('\nDado preenchido incorretamente! Tente novamente e utilize números\n')
                    except:
                        print('\nInformação preenchida incorretamente! Tente novamente\n')
                        continue
                    
                elif choice == '0':
                    print('\nVoltando...\n')
                    break
                else:
                    print('\nOpção inválida! Tente novamente\n')
                    continue

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
                    category_inputs = ('ração','semente','fertilizante')
                    try:
                        while True:
                            name = input('Digite o nome do insumo: ')
                            quantity = float(input('Quantidade disponível: '))
                            unity = input('Unidade de medida: ')
                            category = input('Classificação do insumo (RAÇÃO, SEMENTE, FERTILIZANTE OU MEDICAMENTO): ').lower()
                            
                            if category not in category_inputs:
                                print('\nOpção de categoria inválida! Tente novamente\n')
                                continue
                            
                            register_inputs(name, quantity, unity, category)
                            print('\nInsumo cadastrado!\n')
                            break
                    
                    except ValueError:
                        print('\nValor numérico inválido! Tente novamente\n')
                        continue

                elif choice == '2':
                    from inputs import entry_quantity
                    method = method_selection()
                    try:
                        value_entry = int(input('Digite o valor de entrada: '))
                        if method == '1':
                            id_choice = int(input('Digite o id do insumo: '))
                            entry_quantity(value_entry, id_choice)
                            print('\nOperação realizada com sucesso!\n')

                        elif method == '2':
                            name_choice = input('Digite o nome do insumo: ')
                            entry_quantity(value_entry, name_choice)
                            print('\nOperação realizada com sucesso!\n')
                    except ValueError:
                        print('\nValor numérico inválido! Tente novamente\n')
                        continue

                elif choice == '3':
                    from inputs import out_quantity
                    method = method_selection()
                    try:
                        value_out = int(input('Digite o valor de saída: '))
                            
                        if method == '1':
                            id_choice = int(input('Digite o id do insumo: '))
                            out_quantity(value_out, id_choice)
                            
                            if type(out_quantity) != list:
                                print('\nValor acima da quantidade disponível! Tente outro valor\n')
                                continue
                            
                            print('\nOperação realizada com sucesso!\n')

                        elif method == '2':
                            name_choice = input('Digite o nome do insumo: ')
                            out_quantity(value_out, name_choice)
                            
                            if type(out_quantity) != list:
                                print('\nValor acima da quantidade disponível! Tente outro valor\n')
                                continue

                            print('\nOperação realizada com sucesso!\n')
                            
                    except ValueError:
                        print('\nValor numérico inválido! Tente novamente\n')
                        continue

                elif choice == '0':
                    print('\nVoltando...\n')
                    break
                
                else:
                    print('\nOpção inválida! Tente novamente\n')
                    continue

        elif option == '0':
            print('\nVoltando ao menu principal...\n')
            break
        
        else:
            print('\nOpção inválida. Tente novamente!\n')
            continue