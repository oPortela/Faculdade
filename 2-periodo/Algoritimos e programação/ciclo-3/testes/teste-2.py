#decimoTerceiro = 0

def teste_matheus(salario, mesesTrabalhados):
    valor = float(salario)
    meses = float(mesesTrabalhados)

    valorMensal = valor / 12

    decimo = valorMensal * meses

    return decimo

str_salario = input('Digite seu salário: ')
str_meses = input('Digite quantos meses trabalhou: ')

total = teste_matheus(str_salario, str_meses)

print(f'Você receberá R${total} de decimo terceiro')