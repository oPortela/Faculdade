#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vetor2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
vetor3 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
vetorFinal = []

for i in range(len(vetor1)):
    vetorFinal.append(vetor1[i])
    vetorFinal.append(vetor2[i])
    vetorFinal.append(vetor3[i])
        

print(vetorFinal)