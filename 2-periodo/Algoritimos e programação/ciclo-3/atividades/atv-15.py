'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
'''

notas = []
nota = 0

print('\n ----------------- Bem Vindo ao Sistema de lançamento de notas ----------------- \n')

while nota != -1:
    nota = float(input('Digite uma nota (Digite -1 para sair do programa): '))
    notas.append(nota)
    
    if nota == -1:
        del notas[-1]

#a. Mostre a quantidade de valores que foram lidos;
print(f'Foram digitadas {len(notas)} notas no sistema')

#b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;

#c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
for i in range(len(notas)):
    notas.reverse()
    print(notas[i])  
    
#d. Calcule e mostre a soma dos valores;
print(f'A soma das notas digitadas é: {sum(notas)}')

#e. Calcule e mostre a média dos valores;
media = sum(notas) / len(notas)
print(f'A média das notas digitadas foi de {media}.')

#f. Calcule e mostre a quantidade de valores acima da média calculada;
acimaMedia = 0
for i in range(len(notas)):
    if notas[i] > media:
        acimaMedia += 1
print(f'{acimaMedia} notas estão acima da média.')

#g. Calcule e mostre a quantidade de valores abaixo de sete;
abaixo7 = 0
for i in range(len(notas)):
    if notas[i] < 7:
        abaixo7 += 1
print(f'{abaixo7} notas estão abaixo de 7.')

#h. Encerre o programa com uma mensagem;
print('\n ----------------- Fim do Programa -----------------')