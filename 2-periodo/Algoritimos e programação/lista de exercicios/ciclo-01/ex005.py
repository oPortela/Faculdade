print("Qual o seu nivel mediante alerta de risco")

n1 = int(input('Qual o nível que você se encontra? '))

if n1 >= 0 and n1 <= 10:
    if n1 >= 9:
        print('O seu nível é grave, procuro uma ajuda')
    else :
        print('O seu nível está normal')
else:
    print('ERRO!, o valor informado não condiz com nossos parâmetros.')