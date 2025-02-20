alunoCont = 0  # Variável para contar quantos alunos tem na turma
mediaTurma = 0  # Variável para a média da turma
mediaAluno = 0
nomes_alunos = []  # Lista para armazenar os nomes dos alunos
medias_alunos = []  # Lista para armazenar as médias dos alunos

print('--------------------------------------------------------')
print("Bem-vindo ao Sistema de Análise de Desempenho de Alunos!")
print('--------------------------------------------------------')

# Loop para inserção das notas dos alunos
while True:
    nome = input('Digite o nome do aluno: ')
    print(f'Digite as notas de cada matéria do aluno {nome}')
    port = float(input('Português: '))
    while port < 0 or port > 100:
        port = float(input('Digite novamente a nota de português: '))  # Verifica se as notas estão dentro do intervalo.

    mat = float(input('Matemática: '))
    while mat < 0 or mat > 100:
        mat = float(input('Digite novamente a nota de matemática: '))  # Verifica se as notas estão dentro do intervalo.

    hist = float(input('História: '))
    while hist < 0 or hist > 100:
        hist = float(input('Digite novamente a nota de história: '))  # Verifica se as notas estão dentro do intervalo.

    geo = float(input('Geografia: '))
    while geo < 0 or geo > 100:
        geo = float(input('Digite novamente a nota de geografia: '))  # Verifica se as notas estão dentro do intervalo.

    cie = float(input('Ciências: '))
    while cie < 0 or cie > 100:
        cie = float(input('Digite novamente a nota de ciências: '))  # Verifica se as notas estão dentro do intervalo.

    # Cálculo da média do aluno
    mediaAluno = (port + mat + hist + geo + cie) / 5
    print('--------------------------------------------------------')

    mediaTurma += mediaAluno
    alunoCont += 1

    mediaTurma = mediaTurma / alunoCont

    #Verificação para saber qual o aluno que tem a maior nota e a menor nota
    if alunoCont == 1:
        maiorMedia = mediaAluno
        nomeMaior = nome
        menorMedia = mediaAluno
        nomeMenor = nome
    elif alunoCont > 1:
        if mediaAluno > maiorMedia:
            maiorMedia = mediaAluno
            nomeMaior = nome
        elif mediaAluno < menorMedia:
            menorMedia = mediaAluno
            nomeMenor = nome
        else:
            print('ERRO')
    else: 
        print('ERRO')

    nomes_alunos.append(nome)  # Adiciona o nome do aluno à lista
    medias_alunos.append(mediaAluno)  # Adiciona a média do aluno à lista

    resposta = input('Deseja continuar (S para continuar, qualquer tecla para sair): ').upper()
    if resposta != 'S':
        for i in range(alunoCont):
            if medias_alunos[i] < mediaTurma:
                print(f'O aluno {nomes_alunos[i]} está abaixo da média da turma')
            else:
                print(f'O aluno {nomes_alunos[i]} está acima da média')
        break

print('----------------------------------------------------------------------')
print(f'O número de alunos da turma é {alunoCont};')
print(f'A média da turma é {mediaTurma:.2f};')
print(f'A maior média é do aluno {nomeMaior} com a média de {maiorMedia:.2f};')
print(f'A menor média é do aluno {nomeMenor} com a média de {menorMedia:.2f}.')
print('----------------------------------------------------------------------')