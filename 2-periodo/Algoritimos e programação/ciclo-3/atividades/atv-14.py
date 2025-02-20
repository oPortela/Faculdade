# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no
# crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
# "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".


perguntas = [
     "Telefonou para a vítima? ",
     "Esteve no local do crime? ",
     "Mora perto da vítima? ",
     "Devia para a vítima? ",
     "Já trabalhou com a vítima? "
]

respostas = []
suspeito = 0

for i in range(len(perguntas)):
    resposta = input(f'{perguntas[i]}(Sim/Não): ')
    respostas.append(resposta)
    if resposta == 'Sim':
        suspeito += 1
    
if suspeito == 2:
    print('Você é um suspeito.')
elif 3 <= suspeito <= 4:
    print('Você é um cumplice.')
elif suspeito == 5:
    print('Você é o Assasino!')
else:
    print('Você é inocente.')