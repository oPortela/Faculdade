alunoCont = 0
mediaTurma = 0

print('--------------------------------------------------------')
print("Bem-vindo ao Sistema de Análise de Desempenho de Alunos!")
print('--------------------------------------------------------')

notas_alunos = []  # Lista para armazenar as médias dos alunos

while True:
    nome = input('Digite o nome do aluno: ')
    print(f'Digite as notas de cada matéria do aluno {nome}')
    port = float(input('Português: '))
    while port < 0 or port > 100:
        port = float(input('Digite novamente a nota de português: '))

    mat = float(input('Matemática: '))
    while mat < 0 or mat > 100:
        mat = float(input('Digite novamente a nota de matemática: '))

    hist = float(input('História: '))
    while hist < 0 or hist > 100:
        hist = float(input('Digite novamente a nota de história: '))

    geo = float(input('Geografia: '))
    while geo < 0 or geo > 100:
        geo = float(input('Digite novamente a nota de geografia: '))

    cie = float(input('Ciências: '))
    while cie < 0 or cie > 100:
        cie = float(input('Digite novamente a nota de ciências: '))

    mediaAluno = (port + mat + hist + geo + cie) / 5
    notas_alunos.append(mediaAluno)  # Adicione a média do aluno à lista
    print('--------------------------------------------------------')

    mediaTurma += mediaAluno
    alunoCont += 1

    resposta = input('Deseja continuar (S para continuar, qualquer tecla para sair): ').upper()
    if resposta != 'S':
        break

if alunoCont > 0:
    mediaTurma = mediaTurma / alunoCont
    maiorMedia = max(notas_alunos)
    menorMedia = min(notas_alunos)
    nomeMaior = nomeMenor = ""

    for i in range(alunoCont):
        if notas_alunos[i] == maiorMedia:
            nomeMaior = nome
        if notas_alunos[i] == menorMedia:
            nomeMenor = nome

    print('----------------------------------------------------------------------')
    print(f'O número de alunos da turma é {alunoCont};')
    print(f'A média da turma é {mediaTurma:.2f};')

    if nomeMaior and nomeMenor:
        print(f'A maior média é do aluno {nomeMaior} com a média de {maiorMedia:.2f};')
        print(f'A menor média é do aluno {nomeMenor} com a média de {menorMedia:.2f}.')
    else:
        print('Não foi possível determinar o aluno com a maior ou menor média.')
    print('----------------------------------------------------------------------')
else:
    print('Não foram inseridos dados de alunos.')