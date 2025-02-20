#Atividade 01
def exercicio1():
    x = 0
    y = 0
    
    s = int(input('Digite o valor de parcelas: '))
    for i in range(s):
        x += 1
        formula = (x**2 + 1) / (x + 3)
        y += formula
    return y

print(f'{exercicio1():.2f}')