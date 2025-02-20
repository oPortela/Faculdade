numeroVoo = [0] * 12
origemVoo = [''] * 12
destinoVoo = [''] * 12

listaAvioes = [[0] * 10 for _ in range(12)]

def poltronaVazias(aviao, posicao):
    quantidade = 0
    for i in range(10):
        if listaAvioes[posicao][i] == 0:
            quantidade += 1
    
    return quantidade

def mainEmpresaAerea():
    for i in range(len(numeroVoo)):
        numeroVoo[i] = int(input(f'Digite o número do {i + 1}° voo: '))
        origemVoo[i] = input(f'Digite o local de origem do {i + 1}° voo: ')
        destinoVoo[i] = input(f'Digite o local de destino do {i + 1}° voo: ')
        

def mainUsuario():
    print('---------------- Bem vindo ao sistema de reserva de Voo ----------------\n')
    
    while True:
        print('1- Consultar')
        print('2- Efetuar Reserva')
        print('3- Sair.')
        op = int(input('\nDigite a opção desejada: '))
        match op:
            case 1:
                print('Seleciono uma das opções abaixo: ')
                print('1- Número de Voo')
                print('2- Origem')
                print('3- Destino')
                
                opcaoConsulta = int(input('Qual a opção de consulta desejada: '))
                match opcaoConsulta:
                    case 1:
                        consultaNumeroVoo = int(input('Digite o número do Voo desejado: '))
                        for i in range(len(numeroVoo)):
                            if consultaNumeroVoo == numeroVoo[i]:
                                posicao = numeroVoo.index(consultaNumeroVoo)
                                print(f'Este voo sai de {origemVoo[i]} até {destinoVoo[i]} e possui {poltronaVazias(listaAvioes, posicao)} poltronas vazias.')
                                break
                        else:
                            print('\nNúmero de voo não encontrado.')
                    case 2:
                        consultaOrigemVoo = input('Digite o local de origem: ')
                        for i in range(len(numeroVoo)):
                            if consultaOrigemVoo == origemVoo[i]:
                                posicao = origemVoo.index(consultaOrigemVoo)
                                print(f'Este voo sai de {origemVoo[i]} até {destinoVoo[i]} e possui {poltronaVazias(listaAvioes, posicao)} poltronas vazias.')
                                break
                        else:
                            print('\nOrigem de voo não encontrado.')
                    case 3:
                        consultaDestinoVoo = input('Digite o local de origem: ')
                        for i in range(len(numeroVoo)):
                            if consultaDestinoVoo == origemVoo[i]:
                                posicao = destinoVoo.index(consultaDestinoVoo)
                                print(f'Este voo sai de {origemVoo[i]} até {destinoVoo[i]} e possui {poltronaVazias(listaAvioes, posicao)} poltronas vazias.')
                                break
                        else:
                            print('\nDestino de voo não encontrado.')
                    case _:
                        print('ERRO!')
                        
                               
            case 2:
                numeroVooReserva = int(input('Digite o número de voo para a reserva: '))
                
                for i in range(len(numeroVoo)):
                    if numeroVooReserva == numeroVoo[i]:
                        for j in range(len(listaAvioes[i])):
                            if listaAvioes[i][j] == 0:
                                listaAvioes[i][j] = 1
                                print(f'Reserva com origem de {origemVoo[i]} e destino de {destinoVoo[i]} efetuada com sucesso!')
                                break
                        else:
                            print('\nNão há poltronas disponíveis para este voo.')
                        break

            case 3:
                print('Até a próxima!')          
                break
            
            case _:
                print('ERRO!')
                
                
                
mainEmpresaAerea()                
mainUsuario()