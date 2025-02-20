#include <stdio.h>
#include <math.h>
#include <locale.h>

int somarValores(int n1, int n2, int n3){
	int resultado, i;
	
	for(i = n2 + 1; i <= n3-1; i++){
		if(i % n1 == 0){
			resultado += i;
		}
	}
	
	return resultado;
}


int main() {
    setlocale(LC_ALL, "Portuguese");

	int a, b, c, soma, i;
	
	printf("Digite o valor de A: ");
	scanf("%i", &a);

	while(a<=1){
		printf("O valor de A não pode ser menor ou igual à 1. Digite novamente o valor de A: ");
		scanf("%i", &a);
	}
	
	printf("Digite o valor de B: ");
	scanf("%i", &b);
	
	while(b<0){
		printf("O valor de B não pode ser negativo. Digite novamente o valor de B: ");
		scanf("%i", &b);
	}
	
	printf("Digite o valor de C: ");
	scanf("%i", &c);
	
	while(c<0){
		printf("O valor de C não pode ser negativo. Digite novamente o valor de C: ");
		scanf("%i", &c);
	}
	
	soma = somarValores(a, b, c);
	
	printf("A soma dos valores que estão entre %i e %i e são divisiveis por %i é de %i.", b, c, a, soma);
}