matriz1 = [([0] * 5), ([0] * 5), ([0] * 5), ([0] * 5)]
matriz2 = [([0] * 2), ([0] * 2), ([0] * 2), ([0] * 2), ([0] * 2)]

#matriz1 = [([0] * 2), ([0] * 2)]
#matriz2 = [[0], [0]]


def preencherMatriz(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i][j] = int(input(f'Digite um valor para a posição {i + 1}x{j + 1}: '))
    
    return matriz
  
matrizPreenchida1 = preencherMatriz(matriz1)
matrizPreenchida2 = preencherMatriz(matriz2)


def gerarMatriz(matriz1, matriz2):
    matrizMista = [([0] * 2), ([0] * 2), ([0] * 2), ([0] * 2)]
    
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for l in range(len(matriz2)):
                matrizMista[i][j] += (matriz1[i][j] * matriz2[l][j])
            
    return matrizMista

matriz3 = gerarMatriz(matriz1, matriz2)

for i in range(len(matriz3)):
    print(matriz3[i])