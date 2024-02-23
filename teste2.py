'''print("Vamos criar um tabuleiro de tamanho:  N x N")
n=int(input("Valor de N: "))
y=int(input("Valor de y: "))

for linha in range(n):
    for coluna in range(y):
        print("x  ",end='')
    print()
    
    
    

soma = 0
    for i in range(nlinha):
        for y in range(ncoluna):
            if i > 6:
                soma += sum(matriz[i])'''
                
                
    for i in range(len(idades)):
        if i == 0:
            maior = idades[i]
        elif i > 0 and idades[i] > maior:
            maior = idades[i]
            
            
    for i in range(len(idades)):
        if i == 0:
            menor = idades[i]
        elif i > 0 and idades[i] < menor:
            menor = idades[i]

    qtdMulheres = 0
    for i in range(len(sexos)):
        if sexos[i] == 'F' and NumeroFilhos[i] == 3 and salarios[i] < 500:
            qtdMulheres += 1