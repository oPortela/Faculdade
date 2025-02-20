nota = 0
cont = 1
repeat = ''
#variaveis para contar as tentativas de cada questão
tentativ1 = 0
tentativ2 = 0
tentativ3 = 0
tentativ4 = 0
tentativ5 = 0


while cont < 5: #loop para delimitar quantas perguntas irão rodar

    #pergunta 1
    n1 = int(input('1) Qual o resultado da soma => 44 + 58: '))
    if n1 == 102:
        print('Parabéns. você acertou\n')
        nota += 1
        cont += 1
        tentativ1 += 1
    else:
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar as unidades e depois as centenas.\n')
        repeat = input('Deseja refazer a questão [S/N]: ').upper()
        tentativ1 += 1
        while repeat == 'S': #loop para quando o usuário quiser refazer a questão
            tentativ1 += 1
            n1 = int(input('1) Qual o resultado da soma => 44 + 58: '))
            if n1 == 102:
                print('Parabéns. você acertou\n')
                nota += 1
                cont += 1
                break
            else:
                print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar as unidades e depois as centenas.\n')
                repeat = input('Deseja refazer a questão [S/N]: ').upper()
    
    #condicional pro usuário responder se deseja continuar respondendo mais questões ou deseja sair
    resposta = input('Deseja continuar (S para continuar, qualquer tecla para sair): ')
    if resposta.upper() != 'S':
        break


    #pergunta 2
    n2 = int(input('2) Qual o resultado da multiplicação => 6 x 7: '))

    if n2 == 42:
        print('Parabéns. você acertou\n')
        nota += 1
        cont += 1
        tentativ2 += 1
    else:
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode multiplicar 6 por 7 diretamente.\n')
        repeat = input('Deseja refazer a questão [S/N]: ').upper()
        tentativ2 += 1
        while repeat == 'S': #loop para quando o usuário quiser refazer a questão
            tentativ2 += 1
            n2 = int(input('2) Qual o resultado da multiplicação => 6 x 7: '))
            if n2 == 42:
                print('Parabéns. você acertou\n')
                nota += 1
                cont += 1
                break
            else:
                print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode multiplicar 6 por 7 diretamente.\n')
                repeat = input('Deseja refazer a questão [S/N]: ').upper()

    resposta = input('Deseja continuar (S para continuar, qualquer tecla para sair): ')
    if resposta.upper() != 'S':
        break


    #pergunta 3
    n3 = float(input('3) Qual o resultado dessa divisão => 81 / 3: '))

    if n3 == 27:
        print('Parabéns. você acertou\n')
        nota += 1
        cont += 1
        tentativ3 += 1
    else:
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Dividir um número por 3 é o mesmo que encontrar um terço desse número. Para calcular 81 dividido por 3, pense em encontrar um terço de 81.\n')
        tentativ3 += 1
        repeat = input('Deseja refazer a questão [S/N]: ').upper()
        while repeat == 'S': #loop para quando o usuário quiser refazer a questão
            tentativ3 += 3
            n3 = float(input('3) Qual o resultado dessa divisão => 81 / 3: '))
            if n3 == 27:
                print('Parabéns. você acertou\n')
                nota += 1
                cont += 1
                break
            else:
                print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Dividir um número por 3 é o mesmo que encontrar um terço desse número. Para calcular 81 dividido por 3, pense em encontrar um terço de 81.\n')
            repeat = input('Deseja refazer a questão [S/N]: ').upper()


    resposta = input('Deseja continuar (S para continuar, qualquer tecla para sair): ')
    if resposta.upper() != 'S':
        break

    #pergunta 4
    n4 = int(input('4) Adivinhe o valor de X da equação => 2X + 5 = 15: '))
        
    if n4 == 5:
        print('Parabéns. você acertou\n')
        nota += 1
        cont += 1
        tentativ4 += 1
    else:
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Para encontrar o valor de X na equação 2X + 5 = 15, comece por subtrair 5 dos dois lados da equação. Isso irá isolar o termo com X, tornando mais fácil encontrar o valor de X.\n')
        tentativ4 += 1
        repeat = input('Deseja refazer a questão [S/N]: ').upper()
        while repeat == 'S': #loop para quando o usuário quiser refazer a questão
            tentativ4 += 1
            n4 = int(input('4) Adivinhe o valor de X da equação => 2X + 5 = 15: '))
            if n4 == 5:
                print('Parabéns. você acertou\n')
                nota += 1
                cont += 1
                break
            else:
                print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Para encontrar o valor de X na equação 2X + 5 = 15, comece por subtrair 5 dos dois lados da equação. Isso irá isolar o termo com X, tornando mais fácil encontrar o valor de X.\n')
                repeat = input('Deseja refazer a questão [S/N]: ').upper()

    resposta = input('Deseja continuar (S para continuar, qualquer tecla para sair): ')
    if resposta.upper() != 'S':
        break

    #Pergunta 5
    n5 =  int(input('5) Em um projeto para a construção de um cinema, os arquitetos estão avaliando a relação entre a quantidade de fileiras e a quantidade de cadeiras \n em cada fileira. O projeto inicial prevê uma sala para 304 pessoas. No caso de utilizarem 19 fileiras, \n o número de cadeiras por fileira será: '))

    if n5 == 16:
        print('Parabéns. você acertou\n')
        nota += 1
        cont +=1
        tentativ5 += 1
    else:
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Para calcular o número de cadeiras por fileira em uma sala de cinema com 19 fileiras e uma capacidade total de 304 pessoas, você pode usar a seguinte fórmula: Número de cadeiras por fileira = Capacidade total / Número de fileiras.\n')
        tentativ5 += 1
        repeat = input('Deseja refazer a questão [S/N]: ').upper()
        while repeat == 'S': #loop para quando o usuário quiser refazer a questão
            tentativ5 += 1
            n5 =  int(input('5) Em um projeto para a construção de um cinema, os arquitetos estão avaliando a relação entre a quantidade de fileiras e a quantidade de cadeiras \n em cada fileira. O projeto inicial prevê uma sala para 304 pessoas. No caso de utilizarem 19 fileiras, \n o número de cadeiras por fileira será: '))
            if n5 == 16:
                print('Parabéns. você acertou\n')
                nota += 1
                cont += 1
                break
            else:
                print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Para calcular o número de cadeiras por fileira em uma sala de cinema com 19 fileiras e uma capacidade total de 304 pessoas, você pode usar a seguinte fórmula: Número de cadeiras por fileira = Capacidade total / Número de fileiras.\n')
                repeat = input('Deseja refazer a questão [S/N]: ').upper()
    print('Fim das perguntas! Parabéns por ter chegado até aqui.')#mensagem que irá aparecer se o usuário tiver feito as 5 questões
    break
    

media = (nota / 5) * 100

if media >= 60:
    print('\nParabens! você está aprovado.')
    print(f'Você acertou um total de {nota} de 5 perguntas, e sua média foi de {media}%')
else: 
    print('Infelizmente você está reprovado!')
    print(f'Você acertou um total de {nota} de 5 perguntas, e sua média foi de {media}%')

print(f'Você fez a primeira questão em {tentativ1} tentativas.')
print(f'Você fez a segunda questão em {tentativ2} tentativas.')
print(f'Você fez a terceira questão em {tentativ3} tentativas.')
print(f'Você fez a quarta questão em {tentativ4} tentativas.')
print(f'Você fez a quinta questão em {tentativ5} tentativas.')