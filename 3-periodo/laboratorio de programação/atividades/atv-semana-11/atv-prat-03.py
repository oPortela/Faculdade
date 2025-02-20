#Exercicio 03

def preencherVetor(vetor):
    if len(vetor) == 4:
        for i in range(len(vetor)):
            vetor[i] = input(f'Digite o nome do {i + 1}° produto: ')
    
    if len(vetor) == 8:
        for i in range(len(vetor)):
            vetor[i] = input(f'Digite o nome da {i + 1}° loja: ')
    
    return vetor

def preencherPreco(preco, loja, produto):
    for i in range(len(preco)):
        for j in range(len(preco[i])):
            preco[i][j] = float(input(f'Digite o valor do produto {produto[j]} na loja {loja[i]}: '))
        
    return preco


def main():
    print('----------------- Bem vindo ao sistema de precificação -----------------\n')
    
    nomeLoja = [''] * 8
    nomeProdutos = [''] * 4

    precoProdutos = [([0] * 4) for _ in range(8)]
    
    preencherVetor(nomeLoja)
    preencherVetor(nomeProdutos)
    preencherPreco(precoProdutos, nomeLoja, nomeProdutos)
    
    print('----------------- Lista de produtos -----------------\n')
    for i in range(len(precoProdutos)):
        for j in range(len(precoProdutos[i])):
            if 120 > precoProdutos[i][j]:
                print(f'{nomeProdutos[j]} - {nomeLoja[i]}: R$ {precoProdutos[i][j]} ;')

main()