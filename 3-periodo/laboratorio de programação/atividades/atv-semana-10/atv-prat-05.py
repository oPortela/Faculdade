#lista para fazer a ordem crescente
def ordemCrescente(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

#Função para preencher a lista em sequencia
def preencherLista(lista1, lista2):
    listaNova = []
    for i in range(len(lista1)):
        listaNova.append(lista1[i])
        listaNova.append(lista2[i])
    
    return listaNova


def main():
    lista1 = [0] * 5
    lista2 = [0] * 5
    
    #Loop da primeira lista
    for i in range(5):
        n1 = int(input(f'Digite o {i + 1}° número da primeira lista: '))
        lista1[i] = n1
    
    #loop da segunda lista
    for i in range(5):
        n2 = int(input(f'Digite o {i + 1}° número da segunda lista: '))
        lista2[i] = n2
    
    listaCrescente1 = ordemCrescente(lista1)
    listaCrescente2 = ordemCrescente(lista2)
    
    print(f'Está é a lista 1 ordenada: {listaCrescente1}')
    print(f'Está é a lista 2 ordenada: {listaCrescente2}')
    
    listaNova = ordemCrescente(preencherLista(listaCrescente1, listaCrescente2))
    
    print(f'Está é lista com todos os vetores {listaNova}')
    
main()