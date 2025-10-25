from manage import manage_menu
from reports import report_menu
from movements import movements_menu


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
            print('\nEncerrando...\n')
            break    
    else:
        print('Opção inválida. Tente novamente!\n')
        continue
