from reports import search_animal, search_inputs, search_plant
def method_selection():
        options_method = ('1','2')
        while True:
            print('Escolha o modo de seleção')
            print('1.ID')
            print('2.Nome, Espécie ou Cultura')
            
            choice = input('\n> ')
            if choice in options_method:
                return choice
            else:
                print('Opção inválida! Tente novamente\n')
                continue
def method_search():
        while True:
            methods_options = ('1','2')
            print('Escolha o método de busca')
            print('1.Buscar por ID')
            print('2.Buscar por Nome')
                    
            method = input('\n> ')
            if method in methods_options:
                return method
            else:
                print('Método inválido. Tente novamente!\n')
                continue
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
            pass
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
                
        elif option == '0':
            break
        else:
            print('Opção inválida. Tente novamente!')
            continue
def report_menu():
    while True:
        print('Selecione uma opção')

        print('1.Gerar relatório geral')
        print('2.Pesquisar registros')
        print('0.Voltar ao menu')
        option = input('\n> ')
        
        if option == '1': #GERA RELATÓRIO GERAL
            pass
        elif option == '2': #FAZ PESQUISA DE REGISTRO
            
            print('Escolha uma das categorias a ser listada')
            print('1.Animais')
            print('2.Plantas')
            print('3.Insumos')
            print('0.Voltar')
            choice = input('\n> ')
            if choice == '1':
                method = method_search()
                
                if method == '1': #BUSCAR POR ID
                    chosen_id = int(input('Digite o ID: '))
                    print(search_animal(chosen_id),'\n')     

                elif method == '2': #BUSCAR POR NOME
                    chosen_name = input('Digite o nome da espécie: ')
                    print(search_animal(chosen_name),'\n')
            
            elif choice == '2':
                method = method_search()
                
                if method == '1': #BUSCAR POR ID
                    chosen_id = int(input('Digite o ID: '))
                    print(search_plant(chosen_id),'\n')     

                elif method == '2': #BUSCAR POR NOME
                    chosen_name = input('Digite o nome da espécie: ')
                    print(search_plant(chosen_name),'\n')
                
            elif choice == '3':
                method = method_search()

                if method == '1': #BUSCAR POR ID
                    chosen_id = int(input('Digite o ID: '))
                    print(search_inputs(chosen_id),'\n')     

                elif method == '2': #BUSCAR POR NOME
                    chosen_name = input('Digite o nome da espécie: ')
                    print(search_inputs(chosen_name),'\n')


            elif choice == '0': #VOLTA PARA O MENU DE RELATÓRIOS
                print('Voltando...\n')
                continue 
        
        elif option == '0': #VOLTA AO MENU PRINCIPAL
            print('Voltando ao menu principal...\n')
            break
            
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

while True:
    title = 'Sistema de Controle de Inventário de uma Fazenda Digital'
    line = '-' * len(title)
    options = ('0', '1', '2', '3', '4', '5')

    print(f'{title}\n{line}')
    print('Escolha uma opção')

    print('1.Gerenciar animais, plantas e insumos')
    print('2.Gerenciar relatórios')
    print('3.Registrar movimentações')
    print('0.Sair\n')

    option = input('> ')
    if option in options:
        if option == '1':
            manage_menu()
        elif option == '2':
            report_menu()
        elif option == '3':
            movements_menu()
        elif option == '0':
            break    
    else:
        print('Opção inválida. Tente novamente!\n')
        continue



