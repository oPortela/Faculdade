#solicitando ao usuário a quantidade de valores que ele deseja inserir
qtdValores = int(input("Digite a quantidade de valores a inserir"))
# inicializando um vetor(lista) vazia
notas = []
#laço de repetição para armazenar os valores digitados
for i in range(qtdValores):
    nota = float(input("Digite o valor {}: ".format(i + 1)))
    notas.append(nota)
#faz a soma dos valores
soma = 0
for nota in notas:
    soma += nota
#calculando a média
media = soma/qtdValores

print("A média dos valores digitados é: ",media)
