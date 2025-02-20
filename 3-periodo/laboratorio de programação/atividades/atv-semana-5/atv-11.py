'''
. Elabore uma sub-rotina que retorne um vetor com os três primeiros números perfeitos.
Sabe-se que um número é perfeito quando é igual à soma de seus divisores (exceto ele
mesmo). Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito
'''

def numeroPerfeito(a, b, c):
    soma = a + b + c
    
    if soma % a == 0 and soma % b == 0 and soma % c == 0:
        return soma
    else:
        return (f'O número {soma} não é perfeito!')

def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite um número: '))
    n3 = int(input('Digite um número: '))
    
    resultado = numeroPerfeito(n1, n2, n3)
    
    print(f'{resultado}')
    

main()    