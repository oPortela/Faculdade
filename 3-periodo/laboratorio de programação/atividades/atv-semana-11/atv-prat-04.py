#Exercicio 04
    
def preencherMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i][j] = int(input(f'Digite um valor para a posição {i + 1}x{j + 1}:'))
    
    return matriz  

def somarMatriz(matriz):
    somaMatriz = []
    
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
            
        somaMatriz.append(soma)
        
    return somaMatriz

def gerarMatrizMulti(matriz, soma):
    newMatriz = [([0] * 20) for _ in range(10)]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            newMatriz[i][j] = matriz[i][j] * soma[i]

    return newMatriz

def main():
    matrizGrande = [([0] * 20) for _ in range(10)]
    
    preencherMatriz(matrizGrande)
    valoresSomados = somarMatriz(matrizGrande)
    
    novaMatriz = gerarMatrizMulti(matrizGrande, valoresSomados)
    
    for i in range(len(novaMatriz)):
        print(novaMatriz[i])

main()