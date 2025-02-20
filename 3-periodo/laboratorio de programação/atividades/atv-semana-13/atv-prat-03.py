vetor1 = [0] * 10
vetor2 = [0] * len(vetor1)

for i in range(len(vetor1)):
    vetor1[i] = float(input('Digite um valor: '))
    
for i in range(len(vetor1)):
    vetor2[i] = (vetor1[i] * vetor1[i])

print(vetor2)