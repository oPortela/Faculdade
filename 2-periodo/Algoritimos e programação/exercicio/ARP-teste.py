nota = 0  # Pontuação inicial do usuário

questao1 = input('1) Realize o cálculo e indique a alternativa correta => 44 + 58: \n(a)42 \n(b)65\n(c)150\n(d)102\nQual a alternativa correta: ')

match questao1:
    case 'a':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar as unidades e depois as centenas.\n')
        questao1 = input('1) Realize o cálculo novamente e indique a alternativa correta => 44 + 58: \n(a)42 \n(b)65\n(c)150\n(d)102\nQual a alternativa correta: ')
        if questao1 == 'd':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (d)102.\n")
    case 'b':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar as unidades e depois as centenas.\n')
        questao1 = input('1) Realize o cálculo novamente e indique a alternativa correta => 44 + 58: \n(a)42 \n(b)65\n(c)150\n(d)102\nQual a alternativa correta: ')
        if questao1 == 'd':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (d)102.\n")
    case 'c':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar as unidades e depois as centenas.\n')
        questao1 = input('1) Realize o cálculo novamente e indique a alternativa correta => 44 + 58: \n(a)42 \n(b)65\n(c)150\n(d)102\nQual a alternativa correta: ')
        if questao1 == 'd':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (d)102.\n")
    case 'd':
        print('Parabéns. você acertou\n')
        nota += 1
    case _:
        print('ERRO.')


questao2 = input('2) Realize o seguinte cálculo => 6 x 7: \n(a)42\n(b)56\n(c)91\n(d)40\nQual a alternativa correta: ')

match questao2:
    case 'a':
        print('Parabéns. você acertou\n')
        nota += 1
    case 'b':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar o número 6 sete vezes.\n')
        questao2 = input('2) Realize novamente o seguinte cálculo => 6 x 7: \n(a)42\n(b)56\n(c)91\n(d)40\nQual a alternativa correta: ')
        if questao1 == 'a':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (a)42.\n")
    case 'c':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar o número 6 sete vezes.\n')
        questao2 = input('2) Realize novamente o seguinte cálculo => 6 x 7: \n(a)42\n(b)56\n(c)91\n(d)40\nQual a alternativa correta: ')
        if questao1 == 'a':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (a)42.\n")
    case 'd':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar o número 6 sete vezes.\n')
        questao2 = input('2) Realize novamente o seguinte cálculo => 6 x 7: \n(a)42\n(b)56\n(c)91\n(d)40\nQual a alternativa correta: ')
        if questao1 == 'a':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (a)42.\n")
    case _:
        print('ERRO!')

questao3 = input('3) Realize essa divisão => 81 / 3: \n(a)29\n(b)27\n(c)36\n(d)25\nQual a alternativa correta: ')

match questao3:
    case 'a':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Dividir um número por 3 é o mesmo que encontrar um terço desse número. Para calcular 81 dividido por 3, pense em encontrar um terço de 81.\n')
        questao3 = input('3) Realize novamente essa divisão => 81 / 3: \n(a)29\n(b)27\n(c)36\n(d)25\nQual a alternativa correta: ')
        if questao1 == 'b':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (b)27.\n")
    case 'b':
        print('Parabéns. você acertou\n')
        nota += 1
    case 'c':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Dividir um número por 3 é o mesmo que encontrar um terço desse número. Para calcular 81 dividido por 3, pense em encontrar um terço de 81.\n')
        questao3 = input('3) Realize novamente essa divisão => 81 / 3: \n(a)29\n(b)27\n(c)36\n(d)25\nQual a alternativa correta: ')
        if questao1 == 'b':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (b)27.\n")
    case 'd':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Dividir um número por 3 é o mesmo que encontrar um terço desse número. Para calcular 81 dividido por 3, pense em encontrar um terço de 81.\n')
        questao3 = input('3) Realize novamente essa divisão => 81 / 3: \n(a)29\n(b)27\n(c)36\n(d)25\nQual a alternativa correta: ')
        if questao1 == 'b':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (b)27.\n")
    case _:
        print('ERRO!')

questao4 = input('4) Adivinhe o valor de X da equação => 2X + 5 = 15: \n(a)5\n(b)10\n(c)3,5\n(d)5,5\nQual alternativa corresponde ao valor de X: ')

match questao4:
    case 'a':
        print('Parabéns. você acertou\n')
        nota += 1
    case 'b':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Para encontrar o valor de X na equação 2X + 5 = 15, comece por subtrair 5 dos dois lados da equação. Isso irá isolar o termo com X, tornando mais fácil encontrar o valor de X.\n')
        questao4 = input('4) Tente adivinhar novamente o valor de X da equação => 2X + 5 = 15: \n(a)5\n(b)10\n(c)3,5\n(d)5,5\nQual alternativa corresponde ao valor de X: ')
        if questao4 == 'a':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (a)5.\n")
    case 'c':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Para encontrar o valor de X na equação 2X + 5 = 15, comece por subtrair 5 dos dois lados da equação. Isso irá isolar o termo com X, tornando mais fácil encontrar o valor de X.\n')
        questao4 = input('4) Tente adivinhar novamente o valor de X da equação => 2X + 5 = 15: \n(a)5\n(b)10\n(c)3,5\n(d)5,5\nQual alternativa corresponde ao valor de X: ')
        if questao4 == 'a':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (a)5.\n")
    case 'd':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Para encontrar o valor de X na equação 2X + 5 = 15, comece por subtrair 5 dos dois lados da equação. Isso irá isolar o termo com X, tornando mais fácil encontrar o valor de X.\n')
        questao4 = input('4) Tente adivinhar novamente o valor de X da equação => 2X + 5 = 15: \n(a)5\n(b)10\n(c)3,5\n(d)5,5\nQual alternativa corresponde ao valor de X: ')
        if questao4 == 'a':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (a)5.\n")
    case _:
        print('ERRO!')
        
questao5 = input('5) Realize a seguinte multiplicação => 24 x 13: \n(a)512\n(b)622\n(c)312\n(d)224\nQual a alternativa correta: ')

match questao5:
    case 'a':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Uma maneira de realizar essa multiplicação é quebrá-la em etapas menores. Por exemplo, você pode multiplicar 4 por 13, depois 20 por 13 e, finalmente, somar os dois resultados.\n')
        questao5 = input('5) Realize novamente a seguinte multiplicação => 24 x 13: \n(a)512\n(b)622\n(c)312\n(d)224\nQual a alternativa correta: ')
        if questao5 == 'c':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (c)312.\n")
    case 'b':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Uma maneira de realizar essa multiplicação é quebrá-la em etapas menores. Por exemplo, você pode multiplicar 4 por 13, depois 20 por 13 e, finalmente, somar os dois resultados.\n')
        questao5 = input('5) Realize novamente a seguinte multiplicação => 24 x 13: \n(a)512\n(b)622\n(c)312\n(d)224\nQual a alternativa correta: ')
        if questao5 == 'c':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (c)312.\n")
    case 'c':
        print('Parabéns. você acertou\n')
        nota += 1
    case 'd':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Uma maneira de realizar essa multiplicação é quebrá-la em etapas menores. Por exemplo, você pode multiplicar 4 por 13, depois 20 por 13 e, finalmente, somar os dois resultados.\n')
        questao5 = input('5) Realize novamente a seguinte multiplicação => 24 x 13: \n(a)512\n(b)622\n(c)312\n(d)224\nQual a alternativa correta: ')
        if questao5 == 'c':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (c)312.\n")
    case _:
        print('ERRO!')

questao6 = input('6) Qual o resultado da seguinte operação => (15 + 8) x (4 - 2) ÷ 2: \n(a)36\n(b)24\n(c)12\n(d)23\nQual a alternativa correta: ')

match questao6:
    case 'a':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: primeiro realize as operações dentro dos parênteses e depois faça o cálculo da esquerda para a direita.\n')
        questao6 = input('6) Calcule de novo resultado da seguinte operação => (15 + 8) x (4 - 2) ÷ 2: \n(a)36\n(b)24\n(c)12\n(d)23\nQual a alternativa correta: ')
        if questao6 == 'd':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (d)23.\n")
    case 'b':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: primeiro realize as operações dentro dos parênteses e depois faça o cálculo da esquerda para a direita.\n')
        questao6 = input('6) Calcule de novo resultado da seguinte operação => (15 + 8) x (4 - 2) ÷ 2: \n(a)36\n(b)24\n(c)12\n(d)23\nQual a alternativa correta: ')
        if questao6 == 'd':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (d)23.\n")
    case 'c':
        print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: primeiro realize as operações dentro dos parênteses e depois faça o cálculo da esquerda para a direita.\n')
        questao6 = input('6) Calcule de novo resultado da seguinte operação => (15 + 8) x (4 - 2) ÷ 2: \n(a)36\n(b)24\n(c)12\n(d)23\nQual a alternativa correta: ')
        if questao6 == 'd':
            print('Parabéns. você acertou\n')
            nota += 1
        else:
            print("Infelizmente você errou, a resposta correta seria (d)23.\n")
    case 'd':
        print('Parabéns. você acertou\n')
        nota += 1
    case _:
        print('ERRO!')

perAcerto = (nota / 6) * 100
perAcerto = round(perAcerto, 2)

if perAcerto >= 50:
    print(f'Parabéns você acertou {perAcerto}% de 6 questões!')
else:
    print(f'Infelizmente você acertou somente {perAcerto}% de 6 questões, precisa se dedicar mais aos estudos!')