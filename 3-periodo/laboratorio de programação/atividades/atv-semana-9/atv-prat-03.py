'''
Uma pequena loja de artesanato possui apenas um vendedor e comercializa dez tipos de objetos. O vendedor recebe, mensalmente, salário de R$ 545,00, acrescido de 5% do valor total de suas vendas. O valor unitário dos objetos deve ser informado e armazenado em um vetor; a quantidade vendida de cada peça deve ficar em outro vetor, mas na mesma posição. Crie um programa que receba os preços e as quantidades vendidas, armazenando-os em seus respectivos vetores (ambos com tamanho dez).

Depois, determine e mostre:

um relatório contendo: quantidade vendida, valor unitário e valor total de cada objeto. Ao final, deverão ser mostrados o valor geral das vendas e o valor da comissão que será paga ao vendedor; e o valor do objeto mais vendido e sua posição no vetor (não se preocupe com empates).
'''
#qtdVendida = [0] * 10
#valorUnitario = [0] * len(qtdVendida)
#valorTotal = [0] * len(qtdVendida)

def vendasRealizadas():
    qtdVendida = [0] * 10
    valorUnitario = [0] * len(qtdVendida)
    valorTotal = [0] * len(qtdVendida)
    
    for i in range(len(qtdVendida)):
        qtdVendida[i] = int(input(f'Digite a quantidade vendida do {i + 1}° item: '))
        valorUnitario[i] = float(input(f'Digite o valor unitário do {i + 1}° item: '))
        valorTotal[i] = qtdVendida[i] * valorUnitario[i]
    
    return qtdVendida, valorUnitario, valorTotal
        
def qtdVenda(qtdVendida, valorUnitario, valorTotal):
    for i in range(len(qtdVendida)):
        print(f'O produto {i + 1} vendeu {qtdVendida[i]} com o valor unitário de R$ {valorUnitario[i]} totalizando um valor total de R$ {valorTotal}.')
    
def main():
    print(' ---------------------------------------- Bem vindo ao sistema de Vendas ----------------------------------------')
    
    qtdVendida = [0] * 2
    valorUnitario = [0] * len(qtdVendida)
    valorTotal = [0] * len(qtdVendida)
    
    for i in range(len(qtdVendida)):
        qtdVendida[i] = int(input(f'Digite a quantidade vendida do {i + 1}° item: '))
        valorUnitario[i] = float(input(f'Digite o valor unitário do {i + 1}° item: '))
        valorTotal[i] = qtdVendida[i] * valorUnitario[i]
    
    
    print('\n ---------------------------------------- Relatório de Vendas ----------------------------------------\n')
    for i in range(len(qtdVendida)):
        print(f'O produto {i + 1} vendeu {qtdVendida[i]} unidades com o valor unitário de R$ {valorUnitario[i]} totalizando um valor total de R$ {valorTotal[i]}.')
    
    valorGeralVenda = 0
    for i in range(len(qtdVendida)):
        valorGeralVenda += valorTotal[i]
    
    print(f'\nO valor total vendido foi de R$ {valorGeralVenda}.')
    
    comissao = valorGeralVenda * 0.05
    salario = 545.00 + comissao
    
    print(f'\nO salário do funcionário será de R$ 545,00 mais R$ {comissao} totalizando um valor de R$ {salario}')
    
    for i in range(len(qtdVendida)):
        maior = 0
        posicao = 0
        if maior < valorTotal[i]:
            maior = valorUnitario[i]
            posicao = i
    
    print(f'\nO produto com maior valor de venda está na posicao {posicao} e possui o valor unitário de R$ {maior}')
    
main()