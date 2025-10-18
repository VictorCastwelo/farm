from reports import search_animal, search_inputs, search_plant

def register_menu():
    pass
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
            
def manage_input():
    pass
def movements_menu():
    pass


while True:
    title = 'Sistema de Controle de Inventário de uma Fazenda Digital'
    line = '-' * len(title)
    options = ('0', '1', '2', '3', '4', '5')

    print(f'{title}\n{line}')
    print('Escolha uma opção')

    print('1.Cadastrar (animais, plantas e insumos)')
    print('2.Gerenciar relatórios')
    print('3.Gerenciar insumos')
    print('4.Registrar movimentações')
    print('0.Sair\n')

    option = input('> ')
    if option in options:
        if option == '1':
            register_menu()
        elif option == '2':
            report_menu()
        elif option == '3':
            manage_input()
        elif option == '4':
            movements_menu()
        elif option == '0':
            break    
    else:
        print('Opção inválida. Tente novamente!\n')