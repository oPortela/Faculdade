n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
calc = 1

while calc != 5:
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair do programa')
    calc = int(input('DIgite o número da operação desejada: '))
    match calc:
        case 1:
            soma = n1 + n2
            print(f'A soma dos números são: {soma}')
        case 2:
            multi = n1 * n2
            print(f'O resultado da multiplicação foi de {multi}')
        case 3:
            if n1 > n2:
                maior = n1
                print(f'O número maior é o {maior}')
            else:
                maior = n2
                print(f'O número maior é o {maior}')
        case 4:
            
            n1 = int(input('Digite outro número: '))
            n2 = int(input('Digite outro número: '))
        case _:
            print('Opção invalida! Digite a opção desejada!')
