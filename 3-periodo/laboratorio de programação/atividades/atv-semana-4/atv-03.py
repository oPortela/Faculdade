def inverter(n1):
    if n1 < 10:
        return n1
    else:
        ultimo_numero = n1 % 10
        restante = n1 // 10
        qtd = len(str(restante))
        return ultimo_numero * (10 ** qtd) + inverter(restante)
    
    
def main():
    n1 = int(input('Digite o número para inverter: '))
    
    numero_invertido = inverter(n1)
    print(f'O inverso do número {n1} é {numero_invertido}')

main()