print('\t ------------------- Seja Bem-vindo -------------------')
print('\t -------------------     Ao Powp    -------------------')

print("Abaixo")

nomeCompleto = input("Digite o seu nome completo: ")
idade = int(input("Qual a sua idade: "))
cpf = int(input("Digite o seu cpf: "))
rendaMensal = float(input("Qual a sua renda mensal: R$"))

print("Insira abaixo seus gastos mensais!")

agua = float(input("Informe o valor da sua conta de água: "))
energia = float(input("Informe o valor da sua conta de energia: "))
internet = float(input("Informe o valor de seu gasto mensal em internet: "))
alimentacao = float(input("Informe o valor de seu gasto mensal em alimentação: "))
saude = float(input("Informe o valor de seu gasto mensal em saúde: "))
lazer = float(input("Informe o valor de seu gasto mensal em lazer: "))

casa = input("Você possui casa própria? (sim) ou (não) ")
aluguel = 0

if casa == "sim":
  print("OK , Prossiga")
else:
  aluguel = float(input("Informe o seu aluguel: "))

ext=input("Deseja ver o seu extrato? (sim) ou (não)?")

if ext == "sim":
  extrato = rendaMensal - (agua + energia + internet + alimentacao + saude + lazer + aluguel)
  if extrato > 0:
    print(f"Seu extrato  é R$ {extrato}")
    print("Parabéns seu extrato está positivo")
  else:
     print(f"Seu saldo é R$ {extrato}")
     print("Infelizmente seu extrato está negativo")
else:
  print('Ok , tehha um ótimo dia!!')