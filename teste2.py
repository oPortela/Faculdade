'''print("Vamos criar um tabuleiro de tamanho:  N x N")
n=int(input("Valor de N: "))
y=int(input("Valor de y: "))

for linha in range(n):
    for coluna in range(y):
        print("x  ",end='')
    print()
    
    
    

soma = 0
    for i in range(nlinha):
        for y in range(ncoluna):
            if i > 6:
                soma += sum(matriz[i])'''
                

def gerarMatriz(n_linhas, n_colunas):
    matriz = []
    for _ in range(n_linhas):
        matriz.append([0] * n_colunas)
    return matriz

def somaElementos(n_linhas, n_colunas, matriz):
    soma = 0
    for i in range(n_linhas):
        for y in range(n_colunas):
            if i >= 1:
                soma += matriz[i][y]
    return soma

def inserirDadosMatriz():
    nlinha = int(input('Digite o número de linhas: '))
    ncoluna = int(input('Digite o número de colunas: '))
    
    matriz = gerarMatriz(nlinha, ncoluna)
    
    for i in range(nlinha):
        for y in range(ncoluna):
            matriz[i][y] = int(input(f'Digite o número da posição {i + 1}x{y + 1}: '))
    
    soma = somaElementos(nlinha, ncoluna, matriz)
    
    for i in range(nlinha):
        print(matriz[i])
    
    print(f'A soma de todos os elementos da matriz é: {soma}')        

inserirDadosMatriz()