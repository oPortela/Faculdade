def soma(a, b, c):
    resultado = 0
    
    for i in range(b, c + 1):
        if i % a == 0:
            resultado += i
    
    return resultado

def main():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))
    n3 = int(input('Digite um numero: '))
    
    resul = soma(n1, n2, n3)
    
    print(f'A soma dos números entre {n2} e {n3} é {resul}')
    
main()