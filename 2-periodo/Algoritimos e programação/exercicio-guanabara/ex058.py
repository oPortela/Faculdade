import random

nsorteado = random.randint(1, 10)
n1 = int(input('Tente adivinhar o numero sorteado: '))
n2 = 1

while n1 != nsorteado:
    print('Você errou!')
    n1 = int(input('Tente novamente: '))
    n2 += 1

print(f'Parabens! O numero sorteado foi o {nsorteado} e você acertou em {n2} tentativas.')
#print(f"O número sorteado é: {numero_sorteado}")
