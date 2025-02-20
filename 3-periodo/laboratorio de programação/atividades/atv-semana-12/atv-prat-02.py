#Exercicio 02

matriz01 = [([0] * 7), ([0] * 7)]

def preencherMatriz(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            matriz[i][j] = int(input(f'Digite um valor para a posição {i + 1}x{j + 1}: '))
    
    return matriz

def pontoSela(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == min(matriz[i]) and matriz[i][j] == max([row[j] for row in matriz]):
                return (i, j, matriz[i][j])
    return None
            
def main():
    print('----------------- Bem vindo ao sistema de ponto de Sela -----------------')
    
    matrizPreenchida = preencherMatriz(matriz01)
    
    resultado = pontoSela(matrizPreenchida)
    
    if resultado:
        x, y, ponto = resultado
        print(f'O ponto de sela está na posição {x + 1}x{y + 1} e o valor é de {ponto}.')
    else:
        print('Não existe ponto flutuante!')
    
main()

'''def ponto_de_sela(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == min(matriz[i]) and matriz[i][j] == max([row[j] for row in matriz]):
                return (i, j, matriz[i][j])
    return None

# Exemplo de uso
matriz = [[5, 3, 4, 1, 2, 6, 7], [6, 3, 1, 8, 7, 2, 5], [7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]]
ponto = ponto_de_sela(matriz)
if ponto:
    print(f'O ponto de sela está na posição {ponto[0]+1},{ponto[1]+1} e seu valor é {ponto[2]}')
else:
    print('Não há ponto de sela na matriz.')'''