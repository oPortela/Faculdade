#Atividade 09

'''
Crie uma sub-rotina que receba como parâmetro um valor inteiro e positivo N e retorne o
valor de S, obtido pelo seguinte cálculo:
1 + 1/1! + 1/2!...
'''

def somaFatores(n1):
    soma = 0
    fatorial = 1
    
    for i in range(1, n1 + 1):
        fatorial *= i
        div = 1 / fatorial
        soma += div
    
    return soma
    


def main():
    print(f'Bem vindo ao sistema')
    
    n1 = int(input('Digite o número a ser calculado: '))
    
    resultado = somaFatores(n1)
    
    print(f'O resultado da operação é {resultado}')

main()


'''soma = 0
fatorial = 0
    
for i in range(1, 3):
    div = 1 / fatorial
    soma += div
    print(div)
    for j in range(1, 3 + 1):
        fatorial *= j
        print(fatorial)'''