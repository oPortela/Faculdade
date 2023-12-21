#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


def truncate(f, n):
    #Truncates/pads a float f to n decimal places without rounding
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n).rstrip('0')
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

idades = []
alturas = []

for i in range(30):
    idade = int(input(f'Digite a idade do {i + 1}° aluno: '))
    idades.append(idade)
    altura = float(input(f'Digite a altura do {i + 1}° aluno: '))
    alturas.append(altura)

mediaAltura = sum(alturas) / len(idades)
mediaAltura_truncada = float(truncate(mediaAltura, 2))
qtd_alunos = 0

for i in range(len(idades)):
    if idades[i] > 13 and alturas[i] < mediaAltura_truncada:
        qtd_alunos += 1

print(f'Dentre os {len(idades)} alunos {qtd_alunos} são maiores de 13 anos e menores que a média da altura de todos os alunos.')
print(mediaAltura_truncada)