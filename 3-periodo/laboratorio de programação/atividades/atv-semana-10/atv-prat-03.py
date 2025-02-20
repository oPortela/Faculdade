def ordemDecrescente(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def main():
    lista = [0] * 10
    
    for i in range(10):
        n1 = int(input(f'Digite o {i + 1}° número: '))
        lista[i] = n1
    
    listaDecrescente = ordemDecrescente(lista)
    
    print(f'A lista em ordem decrescente é: {listaDecrescente}') 
    
main()