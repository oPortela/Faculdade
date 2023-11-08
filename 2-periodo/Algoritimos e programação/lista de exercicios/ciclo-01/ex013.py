# Solicite três números inteiros ao usuário
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))

# Verifique qual número é o menor
if num1 <= num2 and num1 <= num3:
    menor = num1
    if num2 <= num3:
        meio = num2
        maior = num3
    else:
        meio = num3
        maior = num2
elif num2 <= num1 and num2 <= num3:
    menor = num2
    if num1 <= num3:
        meio = num1
        maior = num3
    else:
        meio = num3
        maior = num1
else:
    menor = num3
    if num1 <= num2:
        meio = num1
        maior = num2
    else:
        meio = num2
        maior = num1

# Imprima os números em ordem crescente
print("Números em ordem crescente:", menor, meio, maior)
