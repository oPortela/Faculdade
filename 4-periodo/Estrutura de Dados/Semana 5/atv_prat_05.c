#include<stdio.h>
#include<locale.h>

int soma(int a, int b){
	int soma;
	
	a = a *2;
	b = b * 2;
	
	soma = a + b;
	
	return soma;
}

main(){
    setlocale(LC_ALL, "Portuguese");
    
    int n1, n2, result;
    
    printf("Digite o valor de n1: ");
    scanf("%i", &n1);
    printf("DIgite o valor de n2: ");
    scanf("%i", &n2);
    
    result = soma(n1, n2);
    
    printf("O valor da soma do dobro dos valores é %i", result);
}