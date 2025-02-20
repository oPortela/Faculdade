'''
qtd_nomes = int(input('Quantos nomes deseja digitar: '))
nomes = [''] * qtd_nomes
print(nomes)

for i in range(qtd_nomes):
    nomes[i] = input('Digite um nome: ')
print(nomes)
'''

notas = []
nota = float(input('Digite as notas no sistema (digite -1 para sair): '))


while (nota >= 0):
    notas.append(nota)
    nota = float(input('Digite as notas no sistema (digite -1 para sair): '))
    
    if nota < 0 :
        print('Notas Lançadas no sistema')
print(notas)

valorProcurado = float(input('Qual o valor deseja encontrar: '))

if valorProcurado in notas:
    print('Nota Lançada!')
else: 
    print('Nota não encontrada')