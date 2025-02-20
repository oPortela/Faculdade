def cria_produto(codigo, preco, quantidade):
    return {"codigo": codigo, "preco": preco, "quantidade": quantidade}

def mostra_produto(produto):
    print(f"Código: {produto['codigo']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def salvar_produtos(produtos):
    with open("C:/Users/oPortela/Documents/GitHub/Faculdade/3-periodo/laboratorio de programação/atividades/atv-semana-18/produtos.txt", "w") as file:
        for produto in produtos:
            file.write(f"{produto['codigo']},{produto['preco']},{produto['quantidade']}\n")

def carregar_produtos():
    produtos = []
    try:
        with open("C:/Users/oPortela/Documents/GitHub/Faculdade/3-periodo/laboratorio de programação/atividades/atv-semana-18/produtos.txt", "r") as file:
            for line in file:
                codigo, preco, quantidade = line.strip().split(',')
                produtos.append(cria_produto(codigo, float(preco), int(quantidade)))
    except FileNotFoundError:
        print("Nenhum produto encontrado. Iniciando novo estoque.")
    return produtos

def buscar_produto_por_codigo(produtos, codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None

def gerar_relatorio(produtos):
    quantidade_total = sum(produto['quantidade'] for produto in produtos)
    valor_total = sum(produto['preco'] * produto['quantidade'] for produto in produtos)

    print("\nRelatório do Estoque:")
    for produto in produtos:
        mostra_produto(produto)
    print(f"\nQuantidade total de itens: {quantidade_total}")
    print(f"Valor total do estoque: R${valor_total:.2f}")

def main():
    produtos = carregar_produtos()

    while len(produtos) < 10:
        codigo = input("Digite o código do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        produtos.append(cria_produto(codigo, preco, quantidade))

    salvar_produtos(produtos)
    gerar_relatorio(produtos)

    codigo_busca = input("\nDigite o código do produto a ser buscado: ")
    produto_encontrado = buscar_produto_por_codigo(produtos, codigo_busca)
    if produto_encontrado:
        print("\nProduto encontrado:")
        mostra_produto(produto_encontrado)
    else:
        print("\nProduto não encontrado.")


main()