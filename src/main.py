from reports import search_animal, search_inputs, search_plant
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
                    pass
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
                  register_animals(name, quantity, unity, category)
                
        elif option == '0':
            break
        else:
            print('Opção inválida. Tente novamente!')
            continue
def report_menu():
    def method_search():
        methods_options = ('1','2')
        print('Escolha o método de busca')
        print('1.Buscar por ID')
        print('2.Buscar por Nome')
                
        method = input('\n> ')
        if method in methods_options:
            return method
        else:
            print('Método inválido. Tente novamente!')
            method = input('\n> ')
            return method
    while True:
        print('Selecione uma opção')

        print('1.Gerar relatório geral')
        print('2.Pesquisar registros')
        print('0.Voltar ao menu')
        option = input('\n> ')
        
        if option == '1':
            pass
        elif option == '2':
            
            print('Escolha uma das categorias a ser listada')
            print('1.Animais')
            print('2.Plantas')
            print('3.Insumos')
            print('0.Voltar')
            choice = input('\n> ')
            if choice == '1':
                method = method_search()
                
                print(search_animal(method),'\n')     

            elif choice == '2':
                method = method_search()

                print(search_plant(method))
            elif choice == '3':
                method = method_search()

                print(search_inputs(method))
            elif choice == '0':
                print('Voltando...\n')
                continue 
        elif option == '0':
            print('Voltando...\n')
            break
            
def movements_menu():
    pass


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



