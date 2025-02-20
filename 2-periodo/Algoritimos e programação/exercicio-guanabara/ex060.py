n1 = int(input('Digite um número: '))
i = 1
fat = 1

while i <= n1:
    fat *= i
    i += 1
    
print(f'O fatorial do número {n1} é {fat}')