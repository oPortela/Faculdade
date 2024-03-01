#Funções recursivas

#Funções que chamam a si mesmas e tem um número de chamadas limitadas

#Cada vez que uma função é chamada de forma recursiva, são alojadas e armazenadas uma cópia de seus parâmetros, de modo a não perder os valores dos parâmetros das chamadas anteriores.

#A recursividade é uma estratégia que pode ser utilizada sempre que o calculo de uma função para o valor de n, pode ser descrita a partir do cálculo de:
#mesma função par ao termo anterior (n-1)

'''
Exemplo: Fatorial ==> 5! => 5*4*3*2*1 = 120
Fatorial: n! = n * (n-1) * (n-2) * (n-3) * (n-4)
          2! = 2*1 = 2
          3! = 3*2! = 3*(2*1) = 6
          4! = 4*3! = 4*(3*2*1) = 24
          5! = 5*4! = 5*(4*3*2*1) = 120
'''

'''
Série de Fibonacci

Fibonacci: fib(n) = fib(n - 1) + fib(n - 2) se n > 1
           fib(n)= 1 se n <= 1
           
           fib(1): 1
           fib(2): 2 -> fib(2-1) + (2-2)
           fib(3): 3 -> fib(3-1) + (3-2)
           fib(4): 4 -> fib(4-1) + (4-2)
            
'''
'''
def soma(x):
    return soma (x - 1)
'''

#Função sem recursão
def fatSrecursao(n):
    n = n if n > 1 else 1
    j = 1
    for i in range(1, n + 1):
        j = j * i
    
    return j

def main1():
    x = int(input('Digite a qtde de termos: '))
    for i in range(1, x + 1):
        print(i, '--> ', fatSrecursao(i))
        
#main1()

#Função com recursão

def fat(n):
    if n <= 1:
        return 1
    else:
        return (n * fat(n-1))
    
def main2():
    x = int(input('Digite o número de termos: '))
    for i in range(1, x + 1):
        print(i,' --> ', fat(i))
        
#main2()
    
    
def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return 1 
    
def main3():
    for i in [1,2,3,4,5]:
        print(i, " ==> ", fibonacci(i))
        
main3()