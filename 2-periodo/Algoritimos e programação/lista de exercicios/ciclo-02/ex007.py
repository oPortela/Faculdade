#Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e calcule a tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N, 2 x N = 2N, ..., 10 x N = 10N. 

n1 = int(input('Digite o número da tabuada: '))

for i in range (0, 11):
    print(f'{n1} x {i} = {n1 * i}')