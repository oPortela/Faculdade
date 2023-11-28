print("Abaixo você colocará o valor de sua venda para saber qual será a sua comissão.")

venda = float(input('Qual o valor da venda: '))

if venda >= 100000:
    pctVend = (venda/100) * 16
    comissao = 700.00 + pctVend

elif venda < 100000 and venda >= 80000:
    pctVend = (venda/100) * 14
    comissao = 650 + pctVend

elif venda < 80000 and venda >= 60000:
    pctVend = (venda/100) * 14
    comissao = 600 + pctVend

elif venda < 60000 and venda >= 40000:
    pctVend = (venda/100) * 14
    comissao = 550 + pctVend

elif venda < 40000 and venda >= 20000:
    pctVend = (venda/100) * 14
    comissao = 500 + pctVend

else :
    pctVend = (venda/100) * 14
    comissao = 400 + pctVend

print(f'O valor que será pago ao vendedor será de {comissao}')