vetor = [0] * 10
vetorPar = []

for i in range(len(vetor)):
    vetor[i] = int(input('Digite um valor: '))
    
for i in range(len(vetor)):
    pares = 0
    if vetor[i] % 2 == 0:
        vetorPar.append(vetor[i])
        pares += 1

print(f'No vetor {vetor} possui {pares} números pares sendo eles: {vetorPar}')