#Faça um Programa que peça as 4 notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

media = 0
nomeAlunos = []
notasAlunos = []
alunosAcimaMedia = []
mediasAlunos = []

for i in range(10):
    nome = input(f'Digite o nome do {i + 1}° aluno: ')
    nomeAlunos.append(nome)
    
    nota = []
    
    for y in range(4):
        notas = float(input(f'Digite a {y + 1}° nota do aluno {nome}: '))
        nota.append(notas)
        
    media = sum(nota) / len(nota)    
    mediasAlunos.append(media)
    
    notasAlunos.append(nota)
    
    if media >= 7.0:
        alunosAcimaMedia.append(media)
    
    
print(nomeAlunos)
print(notasAlunos)
print(mediasAlunos)
print(len(alunosAcimaMedia))

''' #Código GPT
# Inicializando a lista de médias
medias_alunos = []

# Pedindo as 4 notas de 10 alunos
for i in range(10):
    nome = input(f'Digite o nome do {i + 1}° aluno: ')
    notas = []

    for j in range(4):
        nota = float(input(f'Digite a {j + 1}° nota do aluno {nome}: '))
        notas.append(nota)

    # Calculando a média e armazenando no vetor
    media = sum(notas) / len(notas)
    medias_alunos.append(media)

# Contando o número de alunos com média maior ou igual a 7.0
alunos_acima_media = sum(1 for media in medias_alunos if media >= 7.0)

# Imprimindo o resultado
print(f'\nNúmero de alunos com média maior ou igual a 7.0: {alunos_acima_media}')

'''