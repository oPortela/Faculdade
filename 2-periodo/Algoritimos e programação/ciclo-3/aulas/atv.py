# Recebe o nome completo do usuário
nome_completo = input("Digite seu nome completo: ")

# Divide o nome completo em partes usando o espaço como delimitador
partes = nome_completo.split()

# Inverte a ordem das partes
nome_invertido = ' '.join(reversed(partes))

# Exibe o nome invertido
print("Nome invertido:", nome_invertido)
