#C:/Users/oPortela/Documents/GitHub/Faculdade/3-periodo/laboratorio de programação/atividades/atv-semana-18/produtos.txt

with open("C:/Users/oPortela/Documents/GitHub/Faculdade/3-periodo/laboratorio de programação/atividades/atv-semana-18/produtos.txt", "w") as file:
    for produto in produtos:
        file.write(f"{produto['codigo']},{produto['preco']},{produto['quantidade']}\n")
            
            
            
'''
with open('C:/Users/oPortela/Documents/GitHub/Faculdade/3-periodo/laboratorio de programação/atividades/atv-semana-18/produtos.txt', 'w') as arquivo:
    arquivo.write('Linha 1\nLinha 2\nLinha 3\n')

with open('C:/Users/oPortela/Documents/GitHub/Faculdade/3-periodo/laboratorio de programação/atividades/atv-semana-18/meu_arquivo.txt', 'a') as arquivo:
    arquivo.write('Linha 4\nLinha 5\n')

with open('meu_arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)'''