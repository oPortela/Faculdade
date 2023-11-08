##Algoritimo para verificar se o aluno está aprovado e validar a media ponderada das notas informadas

somaPesos = 0

while somaPesos != 10:
    peso1 = float(input('\nInforme o peso da primeira nota: '))
    peso2 = float(input('Informe o peso da segunda nota: '))
    peso3 = float(input('Informe o peso da terceira nota: '))
    peso4 = float(input('Informe o peso da quarta nota: '))

    somaPesos = peso1 + peso2 + peso3 + peso4

    if somaPesos != 10:
        print('\nA soma de pesos tem que ser igual a 10. Por favor informe novamente os valores.')

print('\n Agora informe os valores das notas de cada avaliação.')
nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
nota3 = float(input('Informe sua terceira nota: '))
nota4 = float(input('Informe sua quarta nota: '))

somaNotas = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3) + (nota4 * peso4)
mediaPonderada = somaNotas / somaPesos

if mediaPonderada >= 60:
    print(f'\nParabéns! A sua média foi de {mediaPonderada} você foi aprovado.')
else:
    print(f'Você está reprovado. A sua média foi de {mediaPonderada}')