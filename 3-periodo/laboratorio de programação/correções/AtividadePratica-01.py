# 1ª Aula de Laboratório de Programação Turmas A, B e C - 2024-01
#import math

print("Hello World!!!!")

while True:
    print(" MENU DE OPÇÕES  ")
    print(" 1 - Soma:       ")
    print(" 2 - Subtração:  ")
    print(" 0 - Sair        ")

    op = int(input("Digite uma das Opções acima: "))

    match op:
        case 1:
            print(f"Você escolheu a Opção {op}.")    
        case 2:
            print(f"Você Escolheu a Opção {op}")
        case _:
            return "Saindo..."    
