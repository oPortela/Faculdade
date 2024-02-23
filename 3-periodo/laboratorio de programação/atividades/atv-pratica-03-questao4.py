#Atividade 04

#Função para gerar uma matriz
def gerarMatriz (n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        matriz.append([0] * n_colunas)

    return matriz

#função para a soma dos elementos abaixo da sexta linha
def somaElementos(n_linhas, n_colunas, matriz):
    soma = 0
    for i in range(n_linhas):
        for y in range(n_colunas):
            if i > 5:
                soma += matriz[i][y]
                
    return soma
    

#Procedure para realizar as operações com a matriz criada
def inserirDadosMatriz():
    nlinha = int(input('Digite o número de linhas: '))
    ncoluna = int(input('Digite o número de colunas: '))
    
    matriz = gerarMatriz(nlinha, ncoluna)
    
    #Loop para digitar os valores da matriz
    for i in range(nlinha):
        for y in range(ncoluna):
            matriz[i][y] = int(input(f'Digite o número da posição {i + 1}x{y + 1}: '))
    
    #Loop para fazer a soma dos 
    soma = somaElementos(nlinha, ncoluna, matriz)
    
    for i in range(nlinha):
        print(matriz[i])
    
    print(f'A soma dos elementos da matriz a partir do sexto elemento é: {soma}')        

inserirDadosMatriz()