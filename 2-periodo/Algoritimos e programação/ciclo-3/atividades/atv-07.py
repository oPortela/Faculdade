#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números

numeros = []
multi = 1

for i in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    multi *= numero
    
print(numeros)
print(sum(numeros))
print(f'A multiplicação é de {multi}')


'''
numeros = []
multi = 1

for i in range(5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    multi *= numero

print(f'Números digitados: {numeros}')
print(f'Soma: {sum(numeros)}')
print(f'Multiplicação: {multi}')
'''