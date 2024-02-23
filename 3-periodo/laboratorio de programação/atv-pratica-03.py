#Atividade 01

def exercicio1():
    x = 0
    y = 0
    
    s = int(input('Digite o valor de parcelas: '))
    for i in range(s):
        x += 1
        formula = (x**2 + 1) / (x + 3)
        y += formula
    return y

#print(f'{exercicio1():.2f}')

#Atvidade 02

#Função para calcular a média de salários
def mediaSalarios(soma):
    media = soma / 15
    return media

def pesquisa():
    idades = [0] * 15
    sexos = [''] * 15
    salarios = [0] * 15
    NumeroFilhos = [0] * 15
    
    for i in range(2):
        idades[i] = int(input(f'\nQual a idade da {[i + 1]}° pessoa: '))
        sexos[i] = input(f'Digite o sexo da {[i + 1]}° pessoa (M/F): ').upper()
        salarios[i] = float(input(f'Digite o salário da {[i + 1]}° pessoa: '))
        NumeroFilhos[i] = int(input(f'Digite o número de filhos da {[i + 1]}° pessoa: '))
     
    #Loop para fazer a soma do salário  
    somaSalario = 0 
    for i in range(15):
        somaSalario += salarios[i]
    
    #Loop para saber a maior e menor idade    
    for i in range(len(idades)):
        if i == 0:
            maior = idades[i]
        elif i > 0 and idades[i] > maior:
            maior = idades[i]

    for i in range(len(idades)):
        if i == 0:
            menor = idades[i]
        elif i > 0 and idades[i] < menor:
            menor = idades[i]
    
    qtdMulheres = 0
    for i in range(len(sexos)):
        if sexos[i] == 'F' and NumeroFilhos[i] == 3 and salarios[i] < 500:
            qtdMulheres += 1
    
    media = mediaSalarios(somaSalario)
    print(f'A média de salário das pessoas são: R${media:.2f}')
    print(f'A maior idade registrada é {maior} e a menor foi {menor}')
    print(f'O número de mulheres com mais de 3 filhos e que recebem até R$ 500,00 é: {qtdMulheres}.')


def main():
    print('Bem vindo ao sistema!')
    
    pesquisa()
    


#Atividade 03

def maiorZero(numero):
    if numero > 0:
        return True
    else:
        return False

def menorZero(numero):
    if numero <= 0:
        return True
    else:
        return False
    
def exercicio3():
    qtd = [0] * 3
    maiores = []
    menores = []
    
    for i in range(len(qtd)):
        qtd[i] = int(input(f'Digite o {i + 1}° número: '))
        
    for y in range(len(qtd)):
        if maiorZero(qtd[y]):
            maiores.append(qtd[y])
        if menorZero(qtd[y]):
            menores.append(qtd[y])
    
    print(f'Os números {maiores} são maiores que 0 e os números {menores} são menores que 0.')
     


#Atvidade 04

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
    