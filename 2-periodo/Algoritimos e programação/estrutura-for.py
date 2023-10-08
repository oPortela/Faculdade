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