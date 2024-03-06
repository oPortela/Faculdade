def maximoDivisorComum(x, y):
    if y == 0:
        return x
    else:
        return maximoDivisorComum(y, x % y)

def main():
    while True:
        dividendo = float(input('Digite o dividendo: '))
        divisor = float(input('Digite o divisor: '))
        
        mdc = maximoDivisorComum(dividendo, divisor)
        
        print(f'MDC de {dividendo} e {divisor} é igual a {mdc}')

        op = input('Deseja realizar outro calculo? (S para sim e aperte qualquer tecla para sair) ').upper()
        if op != 'S':
            break
   
main() 