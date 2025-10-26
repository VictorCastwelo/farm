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