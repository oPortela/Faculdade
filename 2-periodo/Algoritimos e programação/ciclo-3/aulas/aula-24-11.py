'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
lista = [1,2,3]

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c] = int(input(f'Digite um valor para {i}, {c}: '))

print('-=' * 30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i] [c] :^5}]', end='')
    print()



#palavra = input('Digite uma palavra: ')
#print(len(palavra))
#print(f'A palavra {palavra} tem ' , len.palavra, ' letras.')

nome = input('Digite seu nome: ')
sexo = input('Qual seu sexo? ').upper()
idade = int(input('Digite a sua idade: '))

if sexo == 'F' and idade < 25:
    print('ACEITO!')
else:
    print('Não aceito!')

'''

lista_inteiros = [2, 4, 6, 8, 10]
i = 0

while (i < len(lista_inteiros)):
    print(lista_inteiros[i])
    i += 1

for i in range(0, len(lista_inteiros), 1):
    print(lista_inteiros[i])