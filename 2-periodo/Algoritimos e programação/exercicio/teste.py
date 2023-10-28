nota = 0
cont = 0
refazer = 'S'

while cont < 2: #esse loop delimita o número de perguntas a serem realizadas
    while True:
        n1 = int(input('1) Qual o resultado da soma => 44 + 58: '))
        if refazer != 'S':
            break
        while n1 != 102:
            print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar as unidades e depois as centenas.\n')
            refazer = input('Deseja refazer a questão [S/N]: ').upper()
            if refazer == 'S':
                n1 = int(input('1) Qual o resultado da soma => 44 + 58: '))
        
        
        





        resposta = input('Deseja continuar: ').upper()
        if resposta != 's':
            break
        cont += 1

    