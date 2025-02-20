def incluirProdutos(lista):
    for i in range(1):
        estoqueProdutos = {}
        estoqueProdutos['Codigo'] = int(input(f'Digite o código do {i + 1}° produto: '))
        estoqueProdutos['Preco'] = float(input(f'Digite o preço do {i + 1}° produto: '))
        estoqueProdutos['Quantidade'] = float(input(f'Digite a quantidade de estoque do {i + 1}° produto: '))
        lista.append(estoqueProdutos)

def mostraProduto(lista):
    for produto in lista:
        print('----------------------------')
        print(f'Código: {produto["Codigo"]}')
        print(f'Preço: {produto["Preco"]}')
        print(f'Quantidade: {produto["Quantidade"]}')
        print('----------------------------')

def main():
    print('-------------- Bem vindo ao sistema --------------')
    estoque = []
    incluirProdutos(estoque)
    
    mostraProduto(estoque)
    
main()