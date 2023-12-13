#4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes

#vetor = input('Digite uma palavra ou 10 letras: ')

# Função para verificar se um caractere é uma consoante
def eh_consoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    return caractere.lower() in consoantes

# Função principal
def contar_e_imprimir_consoantes():
    # Inicializa um vetor de 10 caracteres
    vetor_caracteres = []

    # Lê 10 caracteres do usuário
    for i in range(10):
        caractere = input(f"Digite o {i+1}º caractere: ")
        vetor_caracteres.append(caractere)

    # Conta e imprime as consoantes
    consoantes = [c for c in vetor_caracteres if eh_consoante(c)]
    
    print(f"\nForam lidas {len(consoantes)} consoantes:")
    print("Consoantes:", ", ".join(consoantes))

# Chama a função principal
contar_e_imprimir_consoantes()
