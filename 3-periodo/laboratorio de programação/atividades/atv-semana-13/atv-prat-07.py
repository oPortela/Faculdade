vetor = [0] * 10

for i in range(len(vetor)):
    vetor[i] = int(input('Digite um valor: '))
 
maior = 0   
for i in range(len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = vetor[i].index(maior)
        
print(f'Do vetor {vetor} o maior número é o {maior} e ele está na posição {posicao}.')