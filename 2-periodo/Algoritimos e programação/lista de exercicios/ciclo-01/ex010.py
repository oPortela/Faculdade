##Sistema de aprovação dos alunos de uma universidade

nota1 = float(input('Informe sua primeira nota: '))
nota2 = float(input('Informe sua segunda nota: '))
nota3 = float(input('Informe sua terceira nota: '))
nota4 = float(input('Informe sua quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 60:
    print(f'\n Parabéns! A sua média foi de {media}. Você foi aprovado.')
else:
    print(f'Você está reprovado. A sua média foi de {media}')
