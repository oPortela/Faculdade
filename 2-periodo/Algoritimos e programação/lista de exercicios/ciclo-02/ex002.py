#Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e mostrar:
#a) A menor altura do grupo;
#b) A maior altura do grupo; 
pessoas = 1

while pessoas <= 3:
    nome = input('Digite o nome: ')
    altura = float(input('Digite a altura: '))

    pessoas +=1

    if pessoas == 1:
        nomeMaior = nome
        altMaior = altura
        nomeMenor = nome
        altMenor = altura
    elif pessoas > 1:
        if altura > altMaior:
            nomeMaior = nome
            altMaior = altura
        elif altura < altMenor:
            altMenor = altura
            nomeMenor = nome
        else: 
            print('ERRO!')
    else:
        print('ERRO!')

print(f'A pessoa mais alta é {nomeMaior} com {altMaior}m.')
print(f'A pessoa mais baixa é {nomeMenor} com {altMenor}m.')