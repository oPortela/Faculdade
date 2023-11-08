alunoCont = 0 #Variável para contar quantos alunos tem na turma
mediaAluno = 0 #Variável para a média do aluno
mediaTurma = 0 #Variável para a média da turma

print('--------------------------------------------------------')
print("Bem-vindo ao Sistema de Análise de Desempenho de Alunos!")
print('--------------------------------------------------------')

#Loop para inserção das notas dos alunos
while True:
    nome = input('Digite o nome do aluno: ')
    print(f'Digite as notas de cada máteria do aluno {nome}')
    port = float(input('Português: '))
    while port < 0 or port > 100:
        port = float(input('Digite novamente a nota de português: ')) #Verifica se as notas estão dentro do intervalo.
       
    mat = float(input('Matemática: '))
    while mat < 0 or mat > 100:
        mat = float(input('Digite novamenete a nota de matemática: ')) #Verifica se as notas estão dentro do intervalo.
       
    hist = float(input('História: '))
    while hist < 0 or hist > 100:
        hist = float(input('Digite novamenete a nota de história: ')) #Verifica se as notas estão dentro do intervalo.
       
    geo = float(input('Geografia: '))
    while geo < 0 or geo > 100:
        geo = float(input('Digite novamenete a nota de geografia: ')) #Verifica se as notas estão dentro do intervalo.
       
    cie = float(input('Ciências: '))
    while cie < 0 or cie > 100:
        cie = float(input('Digite novamenete a nota de ciências: ')) #Verifica se as notas estão dentro do intervalo.

    # Calculo da média do aluno
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
            


    resposta = input('Deseja continuar (S para continuar, qualquer tecla para sair): ').upper()
    if resposta != 'S':
        for i in range(alunoCont):
            if mediaAluno < mediaTurma:
                print(f'O aluno {nome} está abaixo da média da turma')
            else:
                print(f'O aluno {nome} está acima da média')
        break

print('----------------------------------------------------------------------')
print(f'O numero de alunos da turma é {alunoCont};')
print(f'A media da turma é {mediaTurma:.2f};')
print(f'A maior média é do aluno {nomeMaior} com a média de {maiorMedia:.2f};')
print(f'A menor média é do aluno {nomeMenor} com a média de {menorMedia:.2f}.')
print('----------------------------------------------------------------------')


print('----------------------------------------------------------------------')
nome =  input('Digite o nome do aluno para a verificação de desempenho: ')
