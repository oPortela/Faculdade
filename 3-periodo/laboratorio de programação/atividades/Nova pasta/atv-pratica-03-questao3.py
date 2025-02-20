#Atividade 03

def maiorZero(numero):
    if numero > 0:
        return True
    else:
        return False

def menorZero(numero):
    if numero <= 0:
        return True
    else:
        return False

def exercicio3():
    qtd = [0] * 3
    maiores = []
    menores = []

    for i in range(len(qtd)):
        qtd[i] = int(input(f'Digite o {i + 1}° número: '))

    for y in range(len(qtd)):
        if maiorZero(qtd[y]):
            maiores.append(qtd[y])
        if menorZero(qtd[y]):
            menores.append(qtd[y])

    print(f'Os números {maiores} são maiores que 0 e os números {menores} são menores que 0.')

exercicio3()