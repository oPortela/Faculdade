nomes_estudantes = ['Matheus Marques', 'Laura dos Anjos', 'Ana Barbara', 'João Pedro', 'Luiz Henrique', 'Marcos Gomes', 'José Pereira', 'Thais Costa'] #Lista com nomes dos estudantes

def inverter_nomes(nomes_estudantes):  #essa função ficará responsável por inverter cada nome da lista nomes_estudantes
    nomes_invertidos = []  #aqui ele cria uma nova lista com os nomes invertidos 
    for nome_completo in nomes_estudantes:  #Loop para inverter cada nome da lista
        parte = nome_completo.split()
        nome_invertido = ' '.join(reversed(parte))
        nomes_invertidos.append(nome_invertido)
    return nomes_invertidos
nomes_invertidos = inverter_nomes(nomes_estudantes)    


def filtrar_por_letra(nomes_estudantes):   #Função para trazer somente os estudantes que comece com a letra que o usuário desejar
    return nomes_estudantes[0].lower() in filtro  
filtro = input('Digite a letra que deseja pesquisar: ')
nomes_filtrados = filter(filtrar_por_letra, nomes_estudantes)


def ordem_alfabetica(nomes_estudantes):  #Função para trazer os nomes da lista em ordem alfabetica
    nomes_estudantes.sort()   #Utilizei a função Sort que graças a ela retorna as Strings em ordem alfabetica
    return nomes_estudantes
nomes_ordenados = ordem_alfabetica(nomes_estudantes)



print(f'Os nomes filtradoes que começam pela letra {filtro} são os {list(nomes_filtrados)}\n')
print(nomes_ordenados, '\n')
print("Nome invertido:", nomes_invertidos)
for nome in nomes_invertidos:
    print('Nomes invertidos: ', nome)