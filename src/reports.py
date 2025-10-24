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
    for item in list_object:
        return item 

#Relatorio Geral
from datetime import datetime
from animals import list_animals
from plants import list_plants
from inputs import list_inputs
def summary():
     archive_name = ['report.txt']
     file = open('report.text', "w", encoding="utf-8")
     generate = datetime.now()
     file.write(str(generate + '\n'))
     file.write("=" * 60)
     file.write(f"{'RELATÓRIO DE STATUS DA FAZENDA':^60}")
     file.write("=" * 60)
     
     file.writelines(all_list(str(list_animals)))

     file.writelines(all_list(str(list_plants)))

     file.writelines(all_list(str(list_inputs)))


     file.close()




     
          
