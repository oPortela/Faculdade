#Exercicio 02

def preencherMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i][j] = int(input(f'Digite a nota do {i + 1}° aluno e da {j + 1}° prova: '))
    
    return matriz

def menorNota(matriz):
    provaComMenor = 0
    
    prova1 = 0
    prova2 = 0
    prova3 = 0
    
    for i in range(len(matriz)):
        menor = 999
        for j in range(len(matriz[i])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
                provaComMenor = matriz[i].index(menor) + 1
            
        if provaComMenor == 1:
            prova1 += 1
        elif provaComMenor == 2:
            prova2 += 1
        else:
            prova3 += 1
            
        print(f'A menor nota do aluno {i + 1} foi de {menor} na {provaComMenor}° prova.')
    
    print(f'\nNa primeira prova {prova1} alunos tiraram a menor nota.')
    print(f'Na segunda prova {prova2} alunos tiraram a menor nota.')
    print(f'Na terceira prova {prova3} alunos tiraram a menor nota.')
         
                
def main():
    notas = [([0] * 3) for _ in range(10)]
    
    preencherMatriz(notas)
    menorNota(notas)
    
main()