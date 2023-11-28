qtd_nomes = int(input('Quantos nomes deseja digitar: '))
nomes = [''] * qtd_nomes
print(nomes)

for i in range(qtd_nomes):
    nomes[i] = input('Digite um nome: ')
print(nomes)