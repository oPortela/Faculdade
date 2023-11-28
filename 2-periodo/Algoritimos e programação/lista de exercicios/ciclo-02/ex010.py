#Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120 

n1 = int(input('DIgite o número que deseje fatorar: '))
fatorar  = 1

while n1 >= 1:
    fatorar *= n1
    n1 -= 1

print(fatorar)


# Ler o valor inicial (A)
A = int(input("Digite o valor inicial (A): "))

# Inicializar as variáveis para o cálculo do fatorial
resultado_fatorial = 1
sequencia_fatorial = []

# Calcular o fatorial e obter a sequência
while A >= 1:
    resultado_fatorial *= A
    sequencia_fatorial.append(str(A))
    A -= 1

# Imprimir a sequência e o resultado
sequencia_formatada = " X ".join(sequencia_fatorial)
print(f"{A}! = {sequencia_formatada} = {resultado_fatorial}")
