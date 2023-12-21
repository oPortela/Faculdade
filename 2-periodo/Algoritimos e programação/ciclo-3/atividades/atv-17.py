#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

distanciaSaltos = []
nomes = []

print('\n ------------- Bem Vindo! ------------- \n')

while True:
    nome = input('Digite o nome do Atleta: ')
    nomes.append(nome)

    for i in range(5):
        salto = float(input(f'Digite a distância do {i + 1}° salto: '))
        distanciaSaltos.append(salto)
        
    continuar = input('Deseja continuar: (S para sim, ou aperte qualquer tecla para sair): ').upper()
    if continuar != 'S':
        break

for i in range(len(nomes)):    
    print(f'\nAtleta: {nomes[i]}\n')
    for i in range(5):
        print(f'{i + 1}° salto: {distanciaSaltos[i]} m.')
    print('\nResultado final: \n')
    print(f'Atleta: {nome}')
    print("Saltos:", " - ".join(map(str, distanciaSaltos)))
    media = sum(distanciaSaltos) / len(distanciaSaltos)
    print(f'Média dos saltos: {media}')