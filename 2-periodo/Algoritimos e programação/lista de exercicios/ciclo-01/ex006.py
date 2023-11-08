print("Qual o seu nivel mediante alerta de risco")

n1 = int(input('Qual o nível que você se encontra? '))

if n1 >= 0 and n1 <= 9:
    if n1 >= 0 and n1 <= 3:
        print('O seu nível é baixo')
    elif n1 >= 4 and n1 <= 6:
        print('O seu nível é médio')
    elif n1 >= 7 and n1 <= 9:
        print('O seu nível é alto')
else:
    print('O seu nível está GRAVE!')