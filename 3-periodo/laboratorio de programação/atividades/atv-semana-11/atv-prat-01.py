#Exercicio 01

def preencherMatriz(matrizPreenchida):
    for i in range(len(matrizPreenchida)):
        for j in range(0, len(matrizPreenchida[i])):
            matrizPreenchida[i][j] = int(input(f'Digite um valor para a posição {i + 1}x{j + 1}: '))
    
    return matrizPreenchida


def maiorElemento(matriz):
    maiorNumero = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maiorNumero:
                maiorNumero = matriz[i][j]
    
    return maiorNumero
                

def preencherMatrizMulti(matriz, maiorNumero):
    maiorNumero = maiorElemento(matriz)
    #matrizPreencida = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = matriz[i][j] * maiorNumero
    
    return matriz

def main():
    matrizM = [([0] * 2), ([0] * 2)]

    preencherMatriz(matrizM)

    matrizR = preencherMatrizMulti(matrizM, maiorElemento(matrizM))

    for i in range(len(matrizR)):
        print(matrizR[i])
        
main()