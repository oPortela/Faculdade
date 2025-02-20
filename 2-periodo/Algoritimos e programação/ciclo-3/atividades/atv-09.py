#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor

a = [9, 10, 8, 4, 12, 44, 65, 23, 87, 10]
quadrados = []

for i in range(len(a)):
    quadrado = a[i] ** 2
    quadrados.append(quadrado) 
    
somaQuadrados = sum(quadrados)
print(f'Os resultados do quadrados são: {quadrados}')
print(f'A soma dos quadrados da lista é: {somaQuadrados}')