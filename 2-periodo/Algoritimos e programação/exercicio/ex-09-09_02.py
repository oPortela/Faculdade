
tipoImovel = input('Qual o tipo de imóvel, responda R(residências), I(industrias) ou C(comércio): ')
KWh = float(input('Quantos KWh foram gastos durante o mês: '))

preco = 0

match tipoImovel.upper():
    case 'R':
        if KWh <= 500:
            preco = 0.40
        else: 
            preco = 0.65
    case 'I':
        if KWh <= 1000:
            preco = 0.55
        else: 
            preco = 0.60
    case 'C':
        if KWh <= 5000:
            preco = 0.55
        else:
            preco = 0.60
    case _:
        print('tipo inválido!')

valor = KWh * preco

print('--------- Tabela de valores ---------')
print(f'\t KWh = {KWh}')
print(f'\t Valor = {valor}')
print('-------------------------------------')