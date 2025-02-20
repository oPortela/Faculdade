def somar(n1, n2):
    return n1 + n2

def multiplicar(n1, n2):
    return n1 * n2

def encontrar_maior(n1, n2):
    return max(n1, n2)

while True:
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Encontrar o Maior")
    print("[4] Novos números")
    print("[5] Sair do programa")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = somar(n1, n2)
        print(f"A soma de {n1} e {n2} é igual a {resultado}")
    elif escolha == '2':
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        resultado = multiplicar(n1, n2)
        print(f"O produto de {n1} e {n2} é igual a {resultado}")
    elif escolha == '3':
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
        maior = encontrar_maior(n1, n2)
        print(f"O maior número entre {n1} e {n2} é {maior}")
    elif escolha == '4':
        n1 = float(input("Digite um novo número: "))
        n2 = float(input("Digite outro novo número: "))
    elif escolha == '5':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
