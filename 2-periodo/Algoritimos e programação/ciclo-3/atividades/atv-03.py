#3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = [''] * 4
media = 0

for i in range(4):
    notas[i] = float(input(f'Digite a {i + 1}° nota: '))
    media += notas[i]

media = media / 4
for i in range(4):
    print(f'A nota da {i + 1}° prova foi: {notas[i]}')
    
    
print(f'A média final dele foi {media} ')
if media >= 6:
    print('Parabéns, você está aprovado!')
else:
    print('Infelizmente você está reprovado.')