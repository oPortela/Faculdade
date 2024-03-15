def soma_03(a, b, c):
    sm = 0
    for i in range(b, c):
        if i % a == 0:
            sm += i
    
    return sm

def main():
    n1 = int(input("Digite o valor de a "))
    n2 = int(input("Digite o valor de b "))
    n3 = int(input("Digite o valor de c "))

    if n1 != 0 and n1 != 1 and n1 != -1:
        if n2 < n3:
            resp = soma_03(n1, n2, n3)
            print(f"\nA soma dos números divisíveis por {n1} entre {n2} e {n3} é: {resp}")
        else:
            resp = soma_03(n1, n3, n2)
            print(f"\nA soma dos números divisíveis por {n1} entre {n2} e {n3} é: {resp}")
    else:
        print("O número digitado deve ser diferente de (0), (1) ou (-1)")
    
#chamando a função main()
main()

