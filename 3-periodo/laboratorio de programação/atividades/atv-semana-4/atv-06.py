def potencia(k, n):
    if n == 0:
        return 1
    elif n == 1:
        return k
    elif n % 2 == 0:
        temp = potencia(k, n // 2)
        return temp * temp
    else:
        temp = potencia(k, (n - 1) // 2)
        return k * temp * temp
    
def main():
    k = int(input('Digite o valor de k: '))
    n = int(input('Digite o valor de n: '))
            
    multi = potencia(k, n)
    print(f'O resultado de {k} elevado à {n} é de {multi}')

main()