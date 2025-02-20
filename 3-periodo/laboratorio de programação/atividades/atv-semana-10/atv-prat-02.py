def separarNumeros(lista):
    listaPositiva = []
    listaNegativa = []
    
    for i in range(8):
        if lista[i] > 0:
            listaPositiva.append(lista[i])
        else:
            listaNegativa.append(lista[i])

    return listaPositiva, listaNegativa

def main():
    lista = [0] * 8

    listaPositiva = []
    listaNegativa = []
    
    for i in range(8):
        n1 = int(input(f'Digite o {i + 1}° número: '))
        lista[i] = n1
        
    listaPositiva, listaNegativa = separarNumeros(lista)
    
    print(f'Aqui está a lista positiva: {listaPositiva}')
    print(f'Aqui está a lista negativa: {listaNegativa}')
        
main()   