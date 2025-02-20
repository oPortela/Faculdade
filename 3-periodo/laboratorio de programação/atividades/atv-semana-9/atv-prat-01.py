#1 - Faça um programa que preencha um vetor com 10 valores e calcule e mostre a média desses valores

print('-------------- Bem vindo ao sistema de médias --------------')

lista = [0] * 10

for i in range(10):
    lista[i] = int(input(f'Digite o {i + 1}° número: '))

soma = 0
for i in range(10):
    soma += lista[i]

media = soma / 10

print(f'A média dos números digitados é de {media}.')
print('-------------- Até a proxima!!! --------------')