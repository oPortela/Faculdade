#Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
#a. O total de votos computados;
#b. Os númeos e respectivos votos de todos os jogadores que receberam votos;
#c. O percentual de votos de cada um destes jogadores;
#d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
#§ Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador através de uma função. Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.


#Função para calcular o percentual dos votos
def calcular_percentual(jogadores, total_votos):
    return (jogadores / total_votos) * 100 if total_votos > 0 else 0

max_jogadores = 23
jogadores = [0] * max_jogadores #aqui cria uma lista com 23 strings zeradas
voto = 1
total_votos = 0

print('-------------------- Seja bem vindo! --------------------')
print('\nEnquete: Quem foi o melhor jogador da partida:')

while voto != 0:
    jogador = int(input('Digite o número do jogador (0 para sair): '))
    
    if jogador == 0:
        break
    elif 1 <= jogador <= 23:
        jogadores[jogador - 1] += 1 #aqui adiciona sempre mais um para a posição do jogador na lista, aonde diminui mais um que é posição que ele ocupa
        total_votos += 1
    else:
        print('Número inválido, digite novamente')

for i in range(len(jogadores)):
    if i == 0:
        maior = jogadores[i]
        posicao = i + 1
    elif i > 0  and jogadores[i] > maior:
        maior = jogadores[i]
        posicao = i + 1
        
media_melhor_jogador = calcular_percentual(maior, total_votos)  #media do melhor jogador       
       
print(jogadores)
print('\nResultado da votação:\n')
print(f'Foram apurados {sum(jogadores)} votos.')
print('Jogador\tVotos\tPerc(%)')
for i in range(len(jogadores)):
    media = calcular_percentual(jogadores[i], total_votos)
    if jogadores[i] != 0:
        print(f'{i + 1}\t{jogadores[i]}\t{media:.2f}')
    
    if i == 22:
        print(f'O melhor jogador foi o número {posicao}, com {maior} votos, correspondendo a {media_melhor_jogador:.2f}% do total de votos.')   