#Algoritimo para verificar um número

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

print('Escolha uma operação:')
print('1- Soma (+)')
print('2- subtração (-)')
print('3- Multiplicação (*)')
print('4- Divisão (/)')
op = int(input('Digite o número da operação desejada: '))

match op:
    case 1:
        resultado = n1 + n2
    case 2:
        resultado = n1 - n2
    case 3:
        resultado = n1 * n2
    case 4: 
        #if n1 == 0 or n2 == 0:
            #print('Não é possível realizar divisão com zero')
        #else:
        resultado = n1 / n2
    case _:
        print('Operação inválida!')
        resultado = 0

if resultado > 0:
    tipo1 = 'Positivo'
else:
    tipo1 = 'Negativo'

if resultado % 2 == 0:
    tipo2 = 'Par'
else: 
    tipo2 = 'Ímpar'

if resultado.is_integer():
    tipo3 = 'Inteiro'
else: 
    tipo3 = 'Decimal'


print(f'O resultado da operação foi de {resultado}, este número é {tipo1}, além de ser {tipo2} e {tipo3}.')