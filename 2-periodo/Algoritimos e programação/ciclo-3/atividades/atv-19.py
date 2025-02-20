#Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

def percentual(votos, total_votos):
    return (votos / total_votos) * 100 if total_votos > 0 else 0

sistema_operacional = [
    'Windows Server',
    'Unix',
    'Linux',
    'Netware',
    'Mac OS',
    'Outro'
    ]

votos = [0] * len(sistema_operacional)
voto = 1
total_votos = 0

print('-------------- Bem Vindo ao sistema de pesquisa --------------\n') #loop para imprimir os sistemas operacionais
for i in range(len(sistema_operacional)):
    print(f'{i + 1}- {sistema_operacional[i]}')

while voto != 0:
    voto = int(input('Digite o número do jogador (0 para sair): '))
    
    if voto == 0:
        break
    elif 1 <= voto <= 6:
        votos[voto - 1] += 1 #aqui adiciona sempre mais um para a posição do jogador na lista, aonde diminui mais um que é posição que ele ocupa
        total_votos += 1
    else:
        print('Número inválido, digite novamente')

for i in range(len(sistema_operacional)):
    if i == 0:
        maior = votos[i]
        nomeMaior = sistema_operacional[i]
    elif i > 0 and votos[i] > maior:
        maior = votos[i]
        nomeMaior = sistema_operacional[i] 
                
maior_media = percentual(maior, total_votos)

print('\nSistema Operacional\t Votos\t %')
print('-------------------\t -----\t ---')

for i in range(len(sistema_operacional)):
    print(f'{sistema_operacional[i]:<25} {votos[i]:<3}\t {percentual(votos[i], total_votos):.2f}%')#Loop para imprimir todos os itens pesquisados com seu respectivos votos e porcentagens, além de ter (:<9) para colocar os espaços.
    
print('-------------------\t -----')
print(f'Total\t\t {sum(votos)}')
print(f'O Sistema Operacional mais votado foi o {nomeMaior}, com {maior} votos, correspondendo a {maior_media}% dos votos.')