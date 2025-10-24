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