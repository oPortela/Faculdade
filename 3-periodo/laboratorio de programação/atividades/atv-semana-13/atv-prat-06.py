vetor = [0] * 10

for i in range(len(vetor)):
    vetor[i] = float(input('Digite um valor: '))

maior = 0
menor = 99999
  
for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
    
    if vetor[i] < menor:
        menor = vetor[i]
        
print(f'Do vetor acima o maior número é o {maior} e o menor é {menor}')