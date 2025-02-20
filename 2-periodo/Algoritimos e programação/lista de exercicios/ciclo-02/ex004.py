#4. Escrever um algoritmo que leia uma quantidade desconhecida de números e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deve terminar quando for lido um número negativo. 

intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0
cont = 0 


while True: 
    n1 = float(input('Digite um número: '))
    while n1 > 100:
        cont -= 1
        print('Digite um número dentro do intervalo.')
        n1 = float(input('Digite um número: '))

    if n1 >= 0 and n1 <=25:
        intervalo1 += 1
    elif n1 >= 26 and n1 <= 50:
        intervalo2 += 1
    elif n1 >= 51 and n1 <= 75:
        intervalo3 += 1
    elif n1 >= 76 and n1 <= 100:
        intervalo4 += 1
    else:
        print('ERRO!')
    
    cont += 1

    if n1 < 0:
        cont -= 1
        break

print(f'Você digitou {cont} números, sendo que {intervalo1} está entre [0-25], {intervalo2} está entre [26-50], {intervalo3} está entre [51-75] e {intervalo4} está entre [76-100].')