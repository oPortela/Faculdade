#5. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores
    
    
numerosInteiros = []
numerosPares = []
numerosImpares = []

for i in range(5):
    numeros = int(input('Digite um número inteiro: '))
    numerosInteiros.append(numeros)

for i in range(len(numerosInteiros)):
    if numerosInteiros[i] % 2 == 0:
        numerosPares.append(numerosInteiros[i])
    else:
        numerosImpares.append(numerosInteiros[i])
        
print(numerosInteiros)
print(numerosPares)
print(numerosImpares)