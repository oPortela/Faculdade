def avaliar_resposta(pergunta, resposta_correta):
    resposta_usuario = input(f"Pergunta: {pergunta}\nSua resposta: ")

    if resposta_usuario == resposta_correta:
        print("Parabéns, você acertou!")
        return True
    else:
        dica = input("Ops, parece que sua resposta está incorreta. Quer uma dica? (Sim/Não): ")
        if dica.lower() == "sim":
            print(f"Dica: ... (aqui seria a dica relacionada à pergunta)")
        return False

def main():
    resultados = []

    while True:
        pergunta = "Qual é a capital do Brasil?"
        resposta_correta = "brasília"

        acertou = avaliar_resposta(pergunta, resposta_correta)

        resultados.append({
            "pergunta": pergunta,
            "resposta_usuario": input("Sua resposta: "),
            "correta": acertou
        })

        continuar = input("Deseja continuar respondendo? (Sim/Não): ")
        if continuar.lower() != "sim":
            break

    with open("resultados.txt", "w") as arquivo:
        for resultado in resultados:
            arquivo.write(f"Pergunta: {resultado['pergunta']}\n"
                          f"Resposta do usuário: {resultado['resposta_usuario']}\n"
                          f"Correta: {resultado['correta']}\n\n")

if __name__ == "__main__":
    main()
