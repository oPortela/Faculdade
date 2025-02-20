#2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = [''] * 10

for i in range(10):
    numeros[i] = float(input('Digite um número real: '))
numerosInvertido = list(reversed(numeros))

print(numerosInvertido)