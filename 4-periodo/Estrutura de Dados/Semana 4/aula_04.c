#include <stdio.h>
#include <locale.h>

void ordenar(int *x, int *y) {
	int temp;
	if(*x<*y){
		temp = *x;
		*x = *y;
		*y = temp;
	}
}

main(){
	int a, b;
	
	printf("Digite o primeiro Valor: ");
	scanf("%d", &a);
	printf("DIgite o segundo Valor: ");
	scanf("%d", &b);
	
	ordenar(&a, &b);
	printf("O Maior valor: %d\n", a);
	printf("O Menor valor: %d\n", b);
}