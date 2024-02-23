#função para calcular a média de salários
def mediaSalarios(soma):
    media = soma / 15
    return media

#Função para descobrir qual a maior idade
def maiorIdade(idade):
    for i in range(15):
        if i == 0:
            maior = idade[i]
        elif i > 0 and idade[i] > maior:
            maior = idade[i]
    
    return maior

#Função para descobrir qual a menor idade
def menorIdade(idade):
    for i in range(15):
        if i == 0:
            menor = idade[i]
        elif i > 0 and idade[i] < menor:
            menor = idade[i]
    
    return menor
#Função para saber quantas mulheres ganham menos de R$ 500,00 e possuem 3 filhos
def qtdMulheres(sexo, numeroFilho, salario):
    qtdMulher = 0
    for i in range(15):
        if sexo[i] == 'F' and numeroFilho[i] == 3 and salario[i] < 500:
            qtdMulher += 1
    
    return qtdMulher

#Procedures que chama o programa
def pesquisa():
    idades = [0] * 15 
    sexos = [''] * 15
    salarios = [0] * 15
    NumeroFilhos = [0] * 15
    
    for i in range(15):
        idades[i] = int(input(f'\nQual a idade da {[i + 1]}° pessoa: '))
        sexos[i] = input(f'Digite o sexo da {[i + 1]}° pessoa (M/F): ').upper()
        salarios[i] = float(input(f'Digite o salário da {[i + 1]}° pessoa: '))
        NumeroFilhos[i] = int(input(f'Digite o número de filhos da {[i + 1]}° pessoa: '))
     
    #Loop para fazer a soma do salário  
    somaSalario = 0 
    for i in range(15):
        somaSalario += salarios[i]
    
    #Variavel para saber a maior e menor idade    
    maior = maiorIdade(idades)      
    menor = menorIdade(idades) 
    mulheres = qtdMulheres(sexos, NumeroFilhos, salarios)
    
    media = mediaSalarios(somaSalario)
    print(f'A média de salário das pessoas são: R${media:.2f}')
    print(f'A maior idade registrada é {maior} e a menor foi {menor}')
    print(f'O número de mulheres com mais de 3 filhos e que recebem até R$ 500,00 é: {mulheres}.')


def main():
    print('Bem vindo ao sistema!')
    
    pesquisa()
    
main()