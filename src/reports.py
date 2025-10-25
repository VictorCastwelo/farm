def search(chosen, list_object):
        for item in list_object:
            for key in item:
                if item[key] == chosen:
                    return item


def search_animal(chosen):
    from animals import list_animals
    item_chosen = search(chosen, list_animals)
    return item_chosen
    
                
def search_plant(chosen):
    from plants import list_plants
    item_chosen = search(chosen, list_plants)
    return item_chosen

def search_inputs(chosen):
    from inputs import list_inputs
    item_chosen = search(chosen, list_inputs)
    return item_chosen


def all_list(list_object):
    object = ''
    for item in list_object:
        object += str(item)
    return object 

def total_itens(list_object):
    total= len(list_object)
    return total



#RELATORIO GERAL
from datetime import datetime
from animals import list_animals
from plants import list_plants
from inputs import list_inputs
def summary():
     archive_name = ['report.txt']
     file = open('report.text', "w", encoding="utf-8")
     generate = str(datetime.now())
     titulo_com_quebra = [generate,'\n','RELATORIO GERAL','\n']
     file.writelines(titulo_com_quebra)
     file.write('SUMÁRIO DE ANIMAIS===')
     file.writelines(all_list(list_animals))
     file.write(str(total_itens(list_animals)))
     file.write('\n')
     file.write('\n')
     file.write('SUMÁRIO DE PLANTAS===')
     file.writelines(all_list(list_plants))
     file.write(str(total_itens(list_plants)))
     file.write('\n')
     file.write('\n')
     file.write('SUMÁRIO DE INSUMOS===')
     file.writelines(all_list(list_inputs))
     file.write(str(total_itens(list_inputs)))
     file.write('\n')

     file.close()
     


from utils import method_selection

def report_menu():
    while True:
        print('Selecione uma opção')

        print('1.Gerar relatório geral')
        print('2.Pesquisar registros')
        print('0.Voltar ao menu')
        option = input('\n> ')
        
        if option == '1': #GERA RELATÓRIO GERAL
            from reports import summary
            summary()
            print('Relatorio Gerado com Sucesso!\n')
        elif option == '2': #FAZ PESQUISA DE REGISTRO
            
            print('Escolha uma das categorias a ser listada')
            print('1.Animais')
            print('2.Plantas')
            print('3.Insumos')
            print('0.Voltar')
            choice = input('\n> ')
            if choice == '1':
                method = method_selection()
                
                if method == '1': #BUSCAR POR ID
                    chosen_id = int(input('Digite o ID: '))
                    print(search_animal(chosen_id),'\n')     

                elif method == '2': #BUSCAR POR NOME
                    chosen_name = input('Digite o nome da espécie: ')
                    print(search_animal(chosen_name),'\n')
            
            elif choice == '2':
                method = method_selection()
                
                if method == '1': #BUSCAR POR ID
                    chosen_id = int(input('Digite o ID: '))
                    print(search_plant(chosen_id),'\n')     

                elif method == '2': #BUSCAR POR NOME
                    chosen_name = input('Digite o nome da espécie: ')
                    print(search_plant(chosen_name),'\n')
                
            elif choice == '3':
                method = method_selection()

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



     
          
