#Faça um programa que preencha um vetor com nove números inteiros, calcule e mostre os números primos e suas respectivas posições.

print('-------------- Bem vindo ao sistema de números primos --------------')

listaNumeros = []
count = 0

for i in range(3):
    numero = int(input(f'Digite o {i + 1}° número: '))
    listaNumeros.append(numero)
    for y in range(len(listaNumeros)):
        if listaNumeros[i] % i != 0: #and listaNumeros[i] % listaNumeros[i] == 1: 
            count += 1
            print(f'O número {listaNumeros[i]} é primo e está na posição {i}.')


'''
number = 2

if number > 0:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')
'''