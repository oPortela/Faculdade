def soma(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + soma(n[1:])

def main():
    numeros = int(input('Digite quantos números deseja calcular: '))
    lista = [0] * numeros
    
    for i in range(numeros):
        lista[i] = float(input('Digite um número: '))
    
    somaValores = soma(lista)
    print(f'A soma dos valores é: {somaValores}')
    
main()