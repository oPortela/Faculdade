nota = 0  # Pontuação inicial do usuário

n1 = int(input('1) Qual o resultado da soma => 44 + 58: '))

if n1 == 102:
    print('Parabéns. você acertou\n')
    nota += 1
else:
    print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar as unidades e depois as centenas.\n')

n2 = int(input('2) Qual o resultado da multiplicação => 6 x 7: '))

if n2 == 42:
    print('Parabéns. você acertou\n')
    nota += 1
else:
    print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: você pode primeiro somar o número 6 sete vezes.\n')

n3 = float(input('3) Qual o resultado dessa divisão => 81 / 3: '))

if n3 == 27:
    print('Parabéns. você acertou\n')
    nota += 1
else:
    print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Dividir um número por 3 é o mesmo que encontrar um terço desse número. Para calcular 81 dividido por 3, pense em encontrar um terço de 81.\n')

n4 = int(input('4) Adivinhe o valor de X da equação => 2X + 5 = 15: '))

if n4 == 5:
    print('Parabéns. você acertou\n')
    nota += 1
else:
    print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Para encontrar o valor de X na equação 2X + 5 = 15, comece por subtrair 5 dos dois lados da equação. Isso irá isolar o termo com X, tornando mais fácil encontrar o valor de X.\n')

n5 =  int(input('5) Qual o resultado da multiplicação => 24 x 13: '))

if n5 == 312:
    print('Parabéns. você acertou\n')
    nota += 1
else:
    print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: Uma maneira de realizar essa multiplicação é quebrá-la em etapas menores. Por exemplo, você pode multiplicar 4 por 13, depois 20 por 13 e, finalmente, somar os dois resultados.\n')

n6 = int(input('6) Qual o resultado da seguinte operação => (15 + 8) x (4 - 2) ÷ 2: '))

if n6 == 23:
    print('Parabéns. você acertou\n')
    nota += 1
else:
    print('Ops, parece que sua resposta está incorreta. Aqui está uma dica: primeiro realize as operações dentro dos parênteses e depois faça o cálculo da esquerda para a direita.\n')

perAcerto = (nota / 6) * 100
perAcerto = round(perAcerto, 2)

if perAcerto >= 50:
    print(f'Parabéns você acertou {perAcerto}% de 6 questões!')
else:
    print(f'Infelizmente você acertou somente {perAcerto}% de 6 questões, precisa se dedicar mais aos estudos!')
