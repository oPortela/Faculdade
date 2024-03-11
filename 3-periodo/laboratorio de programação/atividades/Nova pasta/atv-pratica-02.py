import math

#Função para calcular área do triângulo
def areaTriangulo(base, altura):
    area = base * altura
    return area

#Função para ordenar os numeros em ordem crescente
def numeroCrescente(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        menor = n1
        if n2 <= n3:
            meio = n2
            maior = n3
        else:
            meio = n3
            maior = n2
    elif n2 <= n1 and n2 <= n3:
        menor = n2
        if n1 <= n3:
            meio = n1
            maior = n3
        else:
            meio = n3
            maior = n1
    else:
        menor = n3
        if n1 <= n2:
            meio = n1
            maior = n2
        else:
            meio = n2
            maior = n1

    return menor, meio, maior

#Função para ordenar os numeros em ordem decrescente
def numeroDecrescente(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        menor = n1
        if n2 <= n3:
            meio = n2
            maior = n3
        else:
            meio = n3
            maior = n2
    elif n2 <= n1 and n2 <= n3:
        menor = n2
        if n1 <= n3:
            meio = n1
            maior = n3
        else:
            meio = n3
            maior = n1
    else:
        menor = n3
        if n1 <= n2:
            meio = n1
            maior = n2
        else:
            meio = n2
            maior = n1

    return maior, meio, menor

#Função para achar o delta de uma equação
def equacao(a, b, c):
    funcao = (b**2 - 4*a*c)
    return funcao


#Função de Menu
def menu():
    print('\nSelecione uma das opções abaixo: ')
    print('1 - Calcule a área de um triângulo. ')
    print('2 - Ordene de forma crescente 3 valores digitados.')
    print('3 - Ordene de forma decrescente 3 valores digitados.')
    print('4 - Equação de segundo grau (Ax²+Bx+C).')
    print('0 - Para sair do programa!\n')

#Função principal
def main():
    print('Bem vindo ao sistema!\n')
    while True:
        menu()
        opcao = int(input('Digite a opção desejada: '))

        match opcao:
            case 1:
                base = float(input('Digite a base do triângulo: '))
                altura = float(input('Digite o valor da altura: '))

                print(f'A área do triângulo é {areaTriangulo(base, altura)}')
            case 2:
                n1 = int(input('Digite um número: '))
                n2 = int(input('Digite um número: '))
                n3 = int(input('Digite um número: '))

                print(f'Os valores em ordem crescente são: {numeroCrescente(n1, n2, n3)}')
            case 3:
                n1 = int(input('Digite um número: '))
                n2 = int(input('Digite um número: '))
                n3 = int(input('Digite um número: '))

                print(f'Os valores em ordem crescente são: {numeroDecrescente(n1, n2, n3)}')
            case 4:
                a = float(input('Digite um número para A: '))
                b = float(input('Digite um número para B: '))
                c = float(input('Digite um número para C: '))
                delta = equacao(a, b, c)

                x1 = (-b + math.sqrt(delta)) / (2*a)
                x2 = (-b - math.sqrt(delta)) / (2*a)

                print(f'O valor de x1 é de {x1:.2f} e o valor para x2 é {x2:.2f}')
            case 0:
                print('Até a próxima!\n')
                break
            case _:
                print('ERRO!')

#Função para saber se o ano é bissexto
def anoBissexto(ano):
    if ano % 4 == 0:
        print(f'O ano de {ano} é bissexto')
    else:
        print(f'O ano de {ano} não é bissexto')
    return ano

#Função principal 2
def main2():
    while True:
        valor = int(input('Digite uma ano para saber se ele é bissexto: '))
        anoBissexto(valor)

        resp = input('Deseja continuar no programa? (Digite S para sim ou qualquer tecla para sair): ').upper()
        if resp != 'S':
            print('Até a próxima!')
            break

main()
main2()