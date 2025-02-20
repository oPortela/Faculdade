def destinguirNumero(n1):
    if n1 > 0:
        return 1
    elif n1 == 0: 
        return 'Neutro'
    else:
        return 0
    
def main():
    n1 = int(input('Digite um número: '))
    
    resultado = destinguirNumero(n1)
    
    print(f'O número {n1} é {resultado}')
    
main()