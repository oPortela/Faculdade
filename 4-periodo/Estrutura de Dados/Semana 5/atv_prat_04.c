#include<stdio.h>
#include<locale.h>

void trocarValores(int *a, int *b){
	int temp;

	temp = *b;
	*b = *a;
	*a = temp;
}

main(){
    setlocale(LC_ALL, "Portuguese");
    
    int n1, n2;
    
    printf("Digite o valor de n1: ");
    scanf("%i", &n1);
    printf("Digite o valor de n2: ");
    scanf("%i", &n2);
    
    trocarValores(&n1, &n2);
    
    printf("\nValores apos a troca.");
    printf("\nO valor de n1 e %i", n1);
    printf("\nO valor de n2 e %i", n2);
}