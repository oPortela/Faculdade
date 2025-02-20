produtos = {}

banco = [[],[]]
#fução apara realizar login
def login():

  login = input("Digite seu login: ")
  senha = input("Digite sua senha: ")

  indice_login = banco[0].index(login)
  indice_senha = indice_login

  if senha == banco[1][indice_senha]:
    print("Login realizado com sucesso")
    while True:

        print('1 - Inserir Produtos')
        print('2 - Pesquisar Produtos')
        print('3 - Editar Produtos')
        print('4 - Excluir Produtos\n')
        op = int(input('Escolha uma das opções acima: '))

        match op:
            case 1:
                codigo = int(input('Código: '))
                descricao = input('Descrição: ')
                estoque = int(input('QT. Estoque: '))
                embalagem = input('Embalagem: ')
                fornecedor = int(input('Cod. Fornecedor: '))
                codauxiliar = int(input('Cod. Barras: '))
                preco = float(input('Preço: '))

                cadastrar_Produto(codigo, descricao, preco, estoque, embalagem, fornecedor, codauxiliar)
            case 2:
                codigo = int(input('Qual produto deseja pesquisar: '))
                print(pesquisar_produto(codigo))
            case 3:
                codigo = int(input('Qual produto deseja alterar: '))
                descricao_alterada = input('Descrição: ')
                preco_alterado = float(input('Preço: '))
                estoque_alterado = int(input('Estoque: '))
                embalagem_alterada = input('Embalagem: ')
                fornecedor_alterado = int(input('Fornecedor: '))
                codauxiliar_alterado = int(input('Cod. Barras: '))

                editar_produto(codigo, descricao_alterada, preco_alterado, estoque_alterado, embalagem_alterada, fornecedor_alterado, codauxiliar_alterado)
            case 4:
                codigo = int(input('Qual produto deseja excluir: '))
                confirm = input(f'Deseja mesmo excluir o produto {codigo}? (S para sim, N para não)').upper()

                if confirm == 'S':
                    excluir_produto(codigo)
                else:
                    print('Operação abortada')
            case _:
                print('ERRO!')

        teste = input('Deseja continuar: ')
        if teste != 's':
            break

    print(produtos)
  else:
    print("dados incorretos")
#fução de cadastro usuando matriz para armazenar os dados em vetores
def registro():
  print("Cadastre-se")
  login = input("cadastrar login: ")
  banco[0].append(login)

  senha = input("Cadastrar senha: ")
  banco[1].append(senha)



#Função para cadastrar produtos
def cadastrar_Produto(codigo, nome, preco, estoque, embalagem, fornecedor, codauxiliar):
    if codigo not in produtos:
        produtos[codigo] = {'nome': nome, 'preco': preco, 'estoque': estoque, 'embalagem': embalagem, 'fornecedor': fornecedor, 'codauxiliar': codauxiliar}
        print("Produto cadastrado com sucesso!")
    else:
        print("Produto com código já existente!")

#Função para excluir produtos
def excluir_produto(codigo):
    if codigo in produtos:
        del produtos[codigo]
        print("Produto excluído com sucesso!")
    else:
        print("Produto não encontrado!")

#Função para editar produtos
def editar_produto(codigo, nome=None, preco=None, estoque=None, embalagem=None, fornecedor=None, codauxiliar=None):
    if codigo in produtos:
        if nome is not None:
            produtos[codigo]['nome'] = nome
        if preco is not None:
            produtos[codigo]['preco'] = preco
        if estoque is not None:
            produtos[codigo]['estoque'] = estoque
        if embalagem is not None:
            produtos[codigo]['embalagem'] = embalagem
        if fornecedor is not None:
            produtos[codigo]['fornecedor'] = fornecedor
        if codauxiliar is not None:
            produtos[codigo]['codauxiliar'] = codauxiliar
        print("Produto editado com sucesso!")
    else:
        print("Produto não encontrado!")

#Função para pesquisar produtos
def pesquisar_produto(codigo):
    if codigo in produtos:
        produto = produtos[codigo]
        print(f"Código: {codigo}")
        print(f"Nome: {produto['nome']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Estoque: {produto['estoque']}")
        print(f'Embalagem: {produto["embalagem"]}')
        print(f'Fornecedor: {produto["fornecedor"]}')
        print(f'Cod Barras: {produto["codauxiliar"]}')
    else:
        print("Produto não encontrado!")


#Função Principal
def main():
    registro()
    login()

main()