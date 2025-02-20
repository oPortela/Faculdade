def incluirProdutos(lista):
    for i in range(2):
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

def buscarProdutoPorCodigo(lista, codigo):
    for produto in lista:
        if produto['Codigo'] == codigo:
            return produto
    return None

def main():
    print('-------------- Bem vindo ao sistema --------------')
    estoque = []
    incluirProdutos(estoque)
    
    mostraProduto(estoque)
    
    codigo_busca = int(input('Digite o código do produto que deseja buscar: '))
    produto_encontrado = buscarProdutoPorCodigo(estoque, codigo_busca)
    
    if produto_encontrado:
        print('Produto encontrado:')
        print('----------------------------')
        print(f'Código: {produto_encontrado["Codigo"]}')
        print(f'Preço: {produto_encontrado["Preco"]}')
        print(f'Quantidade: {produto_encontrado["Quantidade"]}')
        print('----------------------------')
    else:
        print('Produto não encontrado.')

main()
