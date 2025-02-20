#3. Desenvolver um algoritmo que leia um número não determinado de valores e calcule e escreva a média aritmética dos valores lidos, a quantidade de valores positivos, a quantidade de valores negativos e o percentual de valores negativos e positivos. 

soma = 0
cont = 0
numPositivo = 0
numNegativo = 0

while True:
    n1 = float(input('Digite um número:'))
    
    soma += n1
    cont += 1

    if n1 < 0:
        numNegativo += 1
    else: 
        numPositivo += 1

    continuar = input('Deseja continuar: ')
    if continuar != 's':
        break

percPositivo = (numPositivo * 100) / cont
percNegativo = (numNegativo * 100) / cont

media = soma / cont

print(f'Foram digitados {cont} números, a soma dos números é {soma} e a média é de {media}')
print(f'O perdentual positivo é de {percPositivo}%')
print(f'O perdentual negativo é de {percNegativo}%')