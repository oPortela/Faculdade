while True:
    print('Bem vindo ao sistema de resolução de problemas!')
    print('Selecione uma das opções abaixo: ')
    print('1 - Calcule a área de um triângulo. ')
    print('2 - Ordene de forma crescente 3 valores digitados.')
    print('3 - Ordene de forma decrescente 3 valores digitados.')
    print('4 - Equação de segundo grau (Ax²+Bx+C).\n')

    opcao = int(input('Qual operação deseja realizar: '))

    match opcao:
        case 1:
            base = float(input('Digite o valor da base: '))
            altura = float(input('Digite o valor da altura: '))
            
            area = base * altura

            print(f'O valor da área deste triângulo é {area}.')
        case 2:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite um número: '))
            n3 = int(input('Digite um número: '))

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

            print(f'Os números en ordem crescente são: {menor}, {meio}, {maior}')

        case 3:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite um número: '))
            n3 = int(input('Digite um número: '))

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

            print(f'Os números en ordem decrescente são: {maior}, {meio}, {menor}')

        case 4:
            a = float(input('Digite um número para A: '))
            b = float(input('Digite um número para B: '))
            c = float(input('Digite um número para C: '))

            funcao = (b**2 - 4*a*c)

            x1 = (-b + funcao**(1/2)) / (2*a)
            x2 = (-b - funcao**(1/2)) / (2*a)

            funcao1 = ((a**2) + (b*x1) + c)
            funcao2 = ((a**2) + (b*x2) + c)

            print(f'O valor de x1 é de {x1} e o valor para x2 é {x2}')
            print(f'O resultado da equação com x1 é {funcao1} e com x2 é {funcao2}')

        case _:
            print('Opção Inválida!')


    continuar = input('\nDeseja continuar: (S para sim, ou clique qualquer tecla para sair.)').upper()
    if continuar != 'S':
        break
       