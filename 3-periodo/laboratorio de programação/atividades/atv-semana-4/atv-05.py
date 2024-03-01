def somatorio(n1):
    if len(n1) == 1:
        return n1[0]
    else:
        return n1[0] + somatorio(n1[1:])

def main():
    numero = int(input('Digite quantos números deseja calcular: '))
    lista = []
    
    for i in range(numero):
        lista.append(numero)
        numero -= 1
        
    soma = somatorio(lista)    
    
    print(f'O somatório dos números digitados é: {soma}')

main()