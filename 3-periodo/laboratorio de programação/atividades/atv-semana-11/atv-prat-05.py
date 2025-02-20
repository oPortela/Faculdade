#Exercicio 05

def preencherMatriz():
    matriz = []
    for i in range(4):
        linha = []
        for j in range(7):
            elemento = float(input(f"Digite o elemento {i + 1}x{j + 1}: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def encontrarMenorElemento(matriz):
    menor_elemento = float("inf")
    for linha in matriz:
        for elemento in linha:
            if elemento < menor_elemento:
                menor_elemento = elemento
    return menor_elemento

def encontrarPosicaoMenorElemento(matriz, menor_elemento):
    linha_menor = None
    coluna_menor = None
    for i, linha in enumerate(matriz):
        for j, elemento in enumerate(linha):
            if elemento == menor_elemento:
                linha_menor = i
                coluna_menor = j
                break
        if linha_menor is not None:
            break
    return linha_menor, coluna_menor

def encontrarMinMax(matriz, linha_menor):
    minmax = float("-inf")
    for elemento in matriz[linha_menor]:
        if elemento > minmax:
            minmax = elemento
    return minmax

def main():
    matriz = preencherMatriz()
    menor_elemento = encontrarMenorElemento(matriz)
    linha_menor, coluna_menor = encontrarPosicaoMenorElemento(matriz, menor_elemento)
    minmax = encontrarMinMax(matriz, linha_menor)

    print(f"\nMINMAX: {minmax}")
    print(f"Posição: linha {linha_menor + 1}, coluna {coluna_menor + 1}")

main()
