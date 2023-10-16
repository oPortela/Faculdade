'''
for c in range(1,7):
    print(c)
print('Fim!')

for a in range(6,0,-1):
    print(a)
print('Fim!')

for b in range(0,7,2):
    print(b)
print('Fim!')
'''

#inicio = int(input('Digite um númerio inicial: '))
#fim = int(input('Digite um númerio final: '))
#intervalo = int(input('Digite um númerio do intervalo: '))

#for c in range(inicio, fim+1, intervalo):
#    print(c)
#print('Fim!')

soma = 0

for c in range(0,4): 
    n = int(input('Digite um valor: '))
    soma += n
print(f'O somatório de todos os valores são {soma}')


dia = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digie o ano: '))

match mes:
    case 1:
        mes = 'Janeiro'
    case 2:
        mes = 'Fevereiro'
    case _:
        print('ERRO!')

print(f'{dia}/{mes}/{ano}')