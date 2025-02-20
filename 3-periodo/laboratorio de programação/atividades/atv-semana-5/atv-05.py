def percAcrescimo(a, b):
    aumento = (b - a) / a
    taxa = 1 + aumento
    return taxa

def main():
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    
    perc = percAcrescimo(n1, n2)
    
    print(f'O percentula de acréscimo entre {n1} e {n2} é: {perc}%')
    
main()