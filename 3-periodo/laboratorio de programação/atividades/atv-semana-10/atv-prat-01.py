def preencherLista(lista1, lista2):
    listaNova = []
    for i in range(10):
        listaNova.append(lista1[i])
        listaNova.append(lista2[i])
    
    return listaNova
        
def main():  
    lista1 = [3,5,4,2,2,5,3,2,5,9]
    lista2 = [7,15,20,0,18,4,55,23,8,6]

    listaTotal = preencherLista(lista1, lista2)
    
    print(listaTotal)

main()