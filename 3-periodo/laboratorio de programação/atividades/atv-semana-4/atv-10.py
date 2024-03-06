'''def qtdNumeros(k, n):
    qtd = 0
    if k == n and len(str(k)) == 1:
        k = n
        qtd = 1
        return qtd
    else: 
        return qtd + qtdNumeros(k, n)
    

def main():
    while True:
        k = int(input('Digite um número natural: '))
        if k < 0:
            print('Número invalido, digite um número positivo.')
        else:
            break
        
    n = int(input(f'Digite um número para saber quantas vezes ele ocorre no número {k}: '))
    
    qtd = qtdNumeros(k, n)
    print(f'A quantidade do número {n} presente no número {k} é de {qtd}.')
            
main()'''

def qtdNumeros(k, n):
    if k < 10:
        if k == n:
            return 1
        else:
            return 0
    else:
        last_digit = k % 10
        if last_digit == n:
            return 1 + qtdNumeros(k // 10, n)
        else:
            return qtdNumeros(k // 10, n)

def main():
    while True:
        k = int(input('Digite um número natural: '))
        if k < 0:
            print('Número invalido, digite um número positivo.')
        else:
            break
        
    n = int(input(f'Digite um número para saber quantas vezes ele ocorre no número {k}: '))
    
    qtd = qtdNumeros(k, n)
    print(f'A quantidade do número {n} presente no número {k} é de {qtd}.')
            
main()
