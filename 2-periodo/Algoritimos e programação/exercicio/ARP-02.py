resposta = 's'

while resposta == 's':
    n1 = int(input('2+2'))
    if n1 == 4:
        print('correto')
    else:
        print('errou, faz novamente')
        n1 = int(input('2+2'))
        if n1 == 4:
            print('correto')
        else:
            print('errou, é 4')

    resposta = input('Deseja continuar: ')

    n2 = int(input('2+2'))
    if n2 == 4:
        print('correto')
    else:
        print('errou, faz novamente')
        n2 = int(input('2+2'))
        if n2 == 4:
            print('correto')
        else:
            print('errou, é 4')
    
    resposta = input('Deseja continuar: ')