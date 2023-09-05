print("Pense em um animal e responda com 'sim' ou 'não' às perguntas a seguir:")

pergunta1 = input("O animal voa? ")
if pergunta1.lower() == "sim":
    pergunta2 = input("O animal é uma ave de rapina? ")
    if pergunta2.lower() == "sim":
        animal = "águia"
    else:
        animal = "pato"
else:
    pergunta3 = input("O animal é um mamífero? ")
    if pergunta3.lower() == "sim":
        pergunta4 = input("O animal é um carnívoro? ")
        if pergunta4.lower() == "sim":
            pergunta5 = input("O animal é grande? ")
            if pergunta5.lower() == "sim":
                animal = "leão"
            else:
                animal = "gato"
        else:
            pergunta6 = input("O animal é um mamífero aquático? ")
            if pergunta6.lower() == "sim":
                pergunta7 = input("O animal é uma baleia? ")
                if pergunta7.lower() == "sim":
                    animal = "baleia"
                else:
                    animal = "ornitorrinco"
            else:
                animal = "ornitorrinco"
    else:
        pergunta7 = input("O animal vive na água? ")
        if pergunta7.lower() == "sim":
            pergunta8 = input("O animal é um peixe? ")
            if pergunta8.lower() == "sim":
                pergunta9 = input("O animal é um tubarão? ")
                if pergunta9.lower() == "sim":
                    animal = "tubarão"
                else:
                    animal = "lambari"
            else:
                pergunta10 = input("O animal é uma enguia? ")
                if pergunta10.lower() == "sim":
                    animal = "enguia"
                else:
                    pergunta11 = input("O animal é uma arraia? ")
                    if pergunta11.lower() == "sim":
                        animal = "arraia"
                    else:
                        animal = "pinguim"
        else:
            pergunta12 = input("O animal é um morcego? ")
            if pergunta12.lower() == "sim":
                animal = "morcego"
            else:
                animal = "galinha"

print(f"O animal que você está pensando é um(a) {animal}.")
