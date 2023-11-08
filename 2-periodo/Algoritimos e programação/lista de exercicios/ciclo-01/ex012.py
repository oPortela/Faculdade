print("Pense em um animal e responda com 'sim' ou 'não' às perguntas a seguir:")

pergunta1 = input("O animal voa? ")
if pergunta1.lower() == "sim":
    pergunta2 = input("O animal é uma ave de rapina? ")
    if pergunta2.lower() == "sim":
        animal = "águia"
    else:
        animal = "pato"
elif pergunta1.lower() == "não":
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
                    pergunta8 = input("O animal é um ornitorrinco? ")
                    if pergunta8.lower() == "sim":
                        animal = "ornitorrinco"
                    else:
                        animal = "onça pintada"
            else:
                pergunta9 = input("O animal vive na água? ")
                if pergunta9.lower() == "sim":
                    pergunta10 = input("O animal é um peixe? ")
                    if pergunta10.lower() == "sim":
                        pergunta11 = input("O animal é um tubarão? ")
                        if pergunta11.lower() == "sim":
                            animal = "tubarão"
                        else:
                            animal = "lambari"
                    else:
                        pergunta12 = input("O animal é uma enguia? ")
                        if pergunta12.lower() == "sim":
                            animal = "enguia"
                        else:
                            pergunta13 = input("O animal é uma arraia? ")
                            if pergunta13.lower() == "sim":
                                animal = "arraia"
                            else:
                                animal = "pinguim"
                else:
                    pergunta14 = input("O animal é um morcego? ")
                    if pergunta14.lower() == "sim":
                        animal = "morcego"
                    else:
                        pergunta15 = input("O animal é uma galinha? ")
                        if pergunta15.lower() == "sim":
                            animal = "galinha"
                        else:
                            pergunta16 = input("O animal é um avestruz? ")
                            if pergunta16.lower() == "sim":
                                animal = "avestruz"
                            else:
                                animal = "onça pintada"
else:
    animal = "animal não identificado"

print(f"O animal que você está pensando é um(a) {animal} certo.")
