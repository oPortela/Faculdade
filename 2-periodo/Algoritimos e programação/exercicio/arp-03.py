nota = 0
tentativas = [0, 0, 0, 0, 0]  # Lista para contar as tentativas de cada questão

while True:
    for i in range(5):
        # Lista com Perguntas, respostas corretas e dicas para as incorretas
        perguntas = [
            "1) Qual o resultado da soma => 44 + 58: ",
            "2) Qual o resultado da multiplicação => 6 x 7: ",
            "3) Qual o resultado dessa divisão => 81 / 3: ",
            "4) Adivinhe o valor de X da equação => 2X + 5 = 15: ",
            "5) Em um projeto para a construção de um cinema, os arquitetos estão avaliando a relação entre aquantidade de fileiras e a quantidade de cadeiras em cada fileira. O projeto inicial prevê umasala para 304 pessoas. No caso de utilizarem 19 fileiras, o número de cadeiras por fileiraserá: "
        ]
        respostas_corretas = [102, 42, 27, 5, 16]
        
        dicas = [
            ' você pode primeiro somar as unidades e depois as centenas.', 
            ' você pode multiplicar 6 por 7 diretamente.',
            ' Dividir um número por 3 é o mesmo que encontrar um terço desse número. Para calcular 81 dividido por 3, pense em encontrar um terço de 81.',
            ' Para encontrar o valor de X na equação 2X + 5 = 15, comece por subtrair 5 dos dois lados da equação. Isso irá isolar o termo com X, tornando mais fácil encontrar o valor de X.',
            ' Para calcular o número de cadeiras por fileira em uma sala de cinema com 19 fileiras e uma capacidade total de 304 pessoas, você pode usar a seguinte fórmula: Número de cadeiras por fileira = Capacidade total / Número de fileiras.'
        ]

        resposta_usuario = int(input(f"{i + 1}) {perguntas[i]}"))

        if resposta_usuario == respostas_corretas[i]:
            print('Parabéns, você acertou!\n')
            nota += 1
            tentativas[i] += 1
        else:
            print(f'Ops, parece que sua resposta está incorreta. Aqui está uma dica da pergunta {i + 1}: {dicas[i]})\n')
            tentativas[i] += 1
        
        resposta_continuar = input('Deseja continuar (S para continuar, qualquer tecla para sair): ')
        if resposta_continuar.upper() == 'S':
            continue

    resposta_continuar = input('Deseja continuar (S para continuar, qualquer tecla para sair): ')
    if resposta_continuar.upper() != 'S':
        break

    
# Mensagem de encerramento
print('Fim das perguntas! Parabéns por ter chegado até aqui.')

# Cálculo da média e exibição dos resultados
media = (nota / 5) * 100

if media >= 60:
    print('\nParabéns! Você está aprovado.')
    print(f'Você acertou um total de {nota} de 5 perguntas, e sua média foi de {media}%')
else:
    print('Infelizmente você está reprovado!')
    print(f'Você acertou um total de {nota} de 5 perguntas, e sua média foi de {media}%')

# Exibição do número de tentativas por questão
for i in range(5):
    print(f'Você fez a {i + 1}ª questão em {tentativas[i]} tentativas.')
