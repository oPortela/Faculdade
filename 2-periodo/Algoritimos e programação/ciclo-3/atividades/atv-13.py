#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).


def truncate(f, n):
    #Truncates/pads a float f to n decimal places without rounding
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n).rstrip('0')
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturaMediaMensal = []

for i in range(len(meses)):
    temperatura = float(input(f'Qual a temperatura média do mês de {meses[i]}: '))
    temperaturaMediaMensal.append(temperatura)

media = sum(temperaturaMediaMensal) / len(meses)
media_formatada = float(truncate(media, 2))

for i in range(len(meses)):
    if temperaturaMediaMensal[i] > media_formatada:
        print(f'{i + 1} - {meses[i]} = {temperaturaMediaMensal[i]}')