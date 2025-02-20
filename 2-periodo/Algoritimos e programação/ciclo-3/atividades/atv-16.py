'''Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor
recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas
brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa
(usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante
Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.'''

vendedores = []
vendas = []
salarioSemanal = 200.00

print('\n ----------------- Bem vindo ao sistema de premiação de vendedores -----------------\n')

while True:
    nome = input('\n1- Digite o nome do vendedor: ')
    vendedores.append(nome)
    valorVenda = float(input('2- Digite o valor da venda semanal: '))
    vendas.append(valorVenda)
    
    verificacao = input('\nDeseja lançar mais um funcionário (Clique em S para continuar, aperte qualquer tecla para sair): ').upper()
    if verificacao != 'S':
        break

salarioFinal = []

for i in range(len(vendedores)):
    salario = salarioSemanal + ((vendas[i] * 9) / 100)
    salarioFinal.append(salario)
    
print(salarioFinal)

for i in range():