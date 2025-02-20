def soma(a, b):
    sm = 0
    for i in range(a+1, b):
        sm += i
    return sm

def main():
    n1 = int(input("Digite o valor do 1º Termo: "))
    n2 = int(input("Digite o valor do 2º Termo: "))

    if n1 <= 0 or n2 <= 0:
        print("\n Digite somente números positivos!")
    
    if n1 < n2:
        resp = soma(n1, n2)
        print(f"\nA soma dos números entre {n1} e {n2} é: {resp}")
    else:
        resp = soma(n2, n1)
        print(f"\nA soma dos números entre {n2} e {n1} é: {resp}")

#chamando a função principal - main()
main()
        