#Inclusao de novo gasto
#

print("----------Lançamentos de Contas a Pagar----------\n")
x = 0
while True:
    print('------------------------------------------------')
    print('Informações de lançamento.')
    print('------------------------------------------------')
    dataCompetencia = input('Data de competência: ')
    nota_fiscal = int(input("Nº da nota fiscal:  "))
    serieNotaFiscal = int(input('Serie: '))
    servico = str(input("Tipo de serviço: "))
    descricao = str(input("Descriçao:  "))
    valor = float(input("Valor:  "))
    categoria = input('Categoria: ')
    centroCusto = input('Centro de custo: ')
    tipoParceiro = input('Tipo de parceiro: ')
    parceiro = str(input("Parceiro:  "))

    # Verificação de codigo dos bancos
    banco = int(input("Banco:  "))
    while banco != 1 and banco != 104 and banco != 237 and banco != 341:   
        print('Banco não cadastrado no sistema.')
        banco = int(input('Informe um código de banco válido: '))


    #códigos dos bancos  
    if banco == 1 :
        nomeBanco = 'Banco do Brasil'
        #print(nomeBanco)
    elif banco == 104:
        nomeBanco = 'Caixa Economica Federal'
        #print(nomeBanco)
    elif banco == 237:
        nomeBanco = 'Bradesco'
        #print(nomeBanco)
    elif banco == 341:
        nomeBanco = 'Itaú Unibanco'
        #print(nomeBanco)
    else:
        print(banco)

    print('------------------------------------------------\n')
    forma_pagamento = str(input("Forma de pagamento:  "))
    parcelamento = input('Parcelamento: ')
    dataVencimento = input('Data de vencimento: ')
    contaPagamento = input('Conta de pagamento: ')

    print('------------------------------------------------\n')
    observacao = input('Observações: ')
    print('------------------------------------------------\n')

    realizarLancamento = input('Deseja realizar o lançamento [sim/nao]: ').upper()
    if realizarLancamento == 'SIM':
        x += 1
        print('Lançamento realizado com sucesso')
        print('------------------------------------------------')    
        print(f"----------{x}º gasto----------")
        print(f"serviço: {servico}")
        print(f"Nº nota: {nota_fiscal}")
        print(f"Descriçao: {descricao}")
        print(f"Valor: R${valor}")
        print(f"Parceiro: {parceiro}")
        print(f"Banco: {nomeBanco}")
        print(f"Forma de pagamento: {forma_pagamento}")
        print('------------------------------------------------\n')
    else: 
        break
    
    resposta = input('Deseja realizar outro lançamento (S para continuar, qualquer tecla para sair): ').upper()
    if resposta != 'S':
        break