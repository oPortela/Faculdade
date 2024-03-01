def fat(n):
    if n <= 1:
        return 1
    else:
        return (n * fat(n-1))
    
def main():
    x = int(input('Digite o número de termos: '))
    for i in range(1, x + 1):
        print(i,' --> ', fat(i))
        
main()