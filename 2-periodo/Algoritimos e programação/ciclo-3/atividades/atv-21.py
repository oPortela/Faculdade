#Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
#a. O modelo do carro mais econômico;
#b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

carros = ['Golf', 'Astra', 'i30', 'Jetta', '320i']
km_por_litro = [10.5, 8.1, 9.6, 11, 10.9]
distancia = 1000
gasolina = 2.25

def calcular_litros(distancia, km_por_litro):
    return (distancia / km_por_litro)

for i in range(len(carros)):
    print(f'Veiculo {i + 1}')
    print(f'Nome: {carros[i]}')
    print(f'Km por litro: {km_por_litro[i]}')

print('Relátorio final')
for i in range(len(carros)):
    total_litros = calcular_litros(distancia, km_por_litro[i])
    valor = total_litros * gasolina
    
    if i == 0:
        menor = carros[i]
        menor_valor = valor 
    elif i > 0 and valor < menor_valor:
        menor = carros[i]
        menor_valor = valor
    
    print(f'{i + 1} - {carros[i]:<15} - {km_por_litro[i]:<5} -  {total_litros:.1f} litros - R$ {valor:.2f}')
    
    if i == len(carros) - 1:
        print(f'O menor consumo é do {menor}')
