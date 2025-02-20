#Faça um algoritmo que leia uma quantidade não determinada de números positivos. Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos números lidos. O número que encerrará a leitura será zero. 

soma = 0
somaNumPar = 0
cont = 0
numPar = 0
numImpar = 0

while True:
    n1 = float(input('Digite um número positivo: '))

    if n1 % 2 == 0:
        somaNumPar += n1
        numPar += 1
    else: 
        numImpar += 1

    soma += n1
    cont += 1

    if n1 == 0:
        numPar -= 1
        cont -= 1
        break
mediaPar = somaNumPar / numPar
media = soma / cont

print(f'foram digitados no total {cont} números, sendo {numPar} pares e {numImpar} impares. A média dos pares são {mediaPar} e a média geral é de {media}')