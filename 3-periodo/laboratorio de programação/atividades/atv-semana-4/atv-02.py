def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return 1 
    
def main():
    n1 = int(input('Digite a quantidade de valores: '))
    for i in range(1, n1 + 1):
        print(i, " ==> ", fibonacci(i))
        
main()