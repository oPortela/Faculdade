'''
Funções:
Modularização, programação em módulos ou blocos separa a função principal das outras funções.

Função que recebe parametros e retorna
Função que não recebe parametros e retorna
Função que recebe parametros e não retorna
Função que não recebe parametros e não retorna

'''

def soma(x, y): #Função que recebe parametros e retorna
    return x + y

def sub(x, y): #Função que recebe parametros e retorna
    return x - y

def somar(): #Função que recebe parametros e não retorna
    x = int(input('X: '))
    y = int(input('y: '))
    return x + y

def teste(a, b): #Função que recebe parametros e não retorna
    resp = a + b
    print(f'A soma é: {resp}')

def main(): #Função que não recebe parametros e não retorna
    
    x = int(input('X: '))
    y = int(input('y: '))
    
    teste(x, y)


def main2():
    x = int(input('X: '))
    y = int(input('y: '))
    
    teste(4,9)
    
    resp = soma(4,5) + sub(9, 1)
    resp2 = soma(x, y) + 10
    
    print(resp, resp2)
    
    resp3 = somar()
    print(resp3)

    
main()
main2()


def soma2():
    x = int(input('X: '))
    y = int(input('y: '))
    
    resp = x + y
    print(f'A soma é: {resp}')
    
def main3():
    soma2()
    
main3()