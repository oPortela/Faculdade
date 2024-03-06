def inverter_vetor_recursivo(vetor, inicio, fim):
    if inicio < fim:
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        inverter_vetor_recursivo(vetor, inicio + 1, fim - 1)

def main():
    vetor = []
    for i in range(100):
        elemento = float(input(f'Digite o {i + 1}° elemento do vetor: '))
        vetor.append(elemento)

    inverter_vetor_recursivo(vetor, 0, 99)

    print("Vetor invertido:")

main()