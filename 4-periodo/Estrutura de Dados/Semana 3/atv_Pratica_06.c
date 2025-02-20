#include <stdio.h>
#include <math.h>
#include <locale.h>

int somaEntreValores(int n1, int n2){
	int resultado, i;
	
	for(i=n1 + 1; i<=n2 - 1; i++){
		resultado += i;
	}
	
	return resultado;
}

int main() {
    setlocale(LC_ALL, "Portuguese");
	
	int i, n1, n2, soma = 0;
	
	printf("Digite o valor inicial: ");
	scanf("%i", &n1);
	
	while(n1<=0){
		printf("O valor não pode ser negativo. Digite novamente o valor inicial: ");
		scanf("%i", &n1);
	}
	
	printf("DIgite o valor final: ");
	scanf("%i", &n2);
	
	while(n2<=0){
		printf("O valor não pode ser negativo. Digite novamente o valor final: ");
		scanf("%i", &n2);
	}
	
	soma = somaEntreValores(n1, n2);
	
	
	printf("O valor da soma dos números entre %i e %i é de %i.", n1, n2, soma);
}