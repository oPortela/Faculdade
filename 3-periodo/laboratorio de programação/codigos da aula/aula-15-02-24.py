def palestra(msg):
    print("msg")

def soma(a, b):
    sm = a + b
    return sm

def subtracao(x, valor):
    sub = x - valor
    return sub

def multi(a, b):
    mul = a * b
    return mul

def divi(a, b):
    if b == 0:
      print('Não existe divisão por zero')
    else:
        div = a / b
    return div

def menu():
    print('*** Selecione uma das opções abaixo: ***')
    print('1- Soma de dois valores')
    print('2- Diferença de dois valores')
    print('3- Multiplicação de dois valores')
    print('4- Divisão de dois valores')
    print('0- Sair do programa')

def main():
    while True:
        menu()
        op = int(input('Digite a operação desejada (0 à 4): '))
        n1 = int(input('Digite um número inteiro: '))
        n2 = int(input('Digite outro número inteiro: '))

        match op:
            case 1:
                print(f'\nResultado da soma dos números é: {soma(n1, n2)}\n')
            case 2:
                print(f'\nA diferença dos dois números é: {subtracao(n1, n2)}\n')
            case 3:
                print(f'\nO resultado da multiplicação dos números é: {multi(n1, n2)}\n')
            case 4:
                print(f'\nO resultado da divisão dos números é: {divi(n1, n2)}\n')
            case 0:
                print('Até a próxima!')
                break
            case _:
                print('ERRO!')

main()

a = int(input("Digite um valor para somar: "))
b = int(input("Digite um valor para somar: "))
c = int(input("Digite um valor qualquer: "))

teste = soma(a, b)
#print(teste)
sub = subtracao(teste, c)

print(sub)