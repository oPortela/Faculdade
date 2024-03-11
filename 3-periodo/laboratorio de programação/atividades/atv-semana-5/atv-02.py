def soma(a, b):
    soma = 0
    for i in range(a + 1, b):
        soma += i
    return soma

def main():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: ')) 
    
    resultado = soma(x, y)
    
    print(f'A soma de {x} + {y} é {resultado}.')   

main()