#1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os

numerosInteiros = [''] * 5

for i in range(5):
    numerosInteiros[i] = int(input('Digite um número: '))

print(numerosInteiros)