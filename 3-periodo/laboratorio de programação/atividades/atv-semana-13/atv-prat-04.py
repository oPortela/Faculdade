vetor = [0] * 8

for i in range(len(vetor)):
    vetor[i] = int(input('Digite um valor: '))
    
x = int(input('Digite o valor de X: '))
y = int(input('Digite o valor de Y: '))

soma = vetor[x] + vetor[y]

print(f'A soma dos vetores {vetor[x]} + {vetor[y]} = {soma}')