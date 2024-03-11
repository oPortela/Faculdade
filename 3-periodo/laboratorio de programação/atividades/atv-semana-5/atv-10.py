def mediaOlhos(idade, corOlho, corCabelo):
    soma = 0
    qtd = 0
    
    for i in range(len(idade)):
        if corOlho[i] == 'C' and corCabelo[i] == 'P':
            soma += idade[i]
            qtd += 1
            
    if qtd > 0:
        media = soma / qtd
    else:
        media = 0
    
    return media

def maiorIdade(idade):
    maior = 0
    for i in range(len(idade)):
        if idade[i] > maior:
            maior = idade[i]
    
    return maior

def contagemMulheresJovens(idade, sexo, corOlho, corCabelos):
    soma = 0
    
    for i in range(len(idade)):
        if sexo[i] == 'F' and 18 >= idade[i] <= 35 and corOlho[i] == 'A' and corCabelos[i] == 'L':
            soma += 1
            
    return soma

def main():
    sexos = []
    corOlhos = []
    corCabelos = []
    idades = []
    
    for i in range(5):
        sexo = input('Informe o sexo (M/F): ').upper()
        corOlho = input('Informa cor do olho: ').upper()
        corCabelo = input('Informe a cor do cabelo: ').upper()
        idade = int(input('Digite a idade: '))
        
        sexos.append(sexo)
        corOlhos.append(corOlho)
        corCabelos.append(corCabelo)
        idades.append(idade)
        
    media_olhos = mediaOlhos(idades, corOlhos, corCabelos)
    maior_idade = maiorIdade(idade)
    contagem_mulheres = contagemMulheresJovens(idades, sexos, corOlhos, corCabelos)
    
    print(f'A média da idade dos habitantes que possuem a cor de olho castanho e cabelo preto é {media_olhos} anos.')
    print(f'A maior idade entre os habitantes é de {maior_idade} anos.')
    print(f'O número de mulheres que estão entre 18 e 35 anos e que tenham olhos azuis e cabelos louros é de {contagem_mulheres} habitantes.')

main()