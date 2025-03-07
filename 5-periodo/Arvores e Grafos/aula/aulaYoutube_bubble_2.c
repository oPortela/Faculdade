#include <stdio.h>
#define TAM 10

int main () {
	int i, aux, flag;
	int lista[TAM];
	
	for (i = 0;  i < TAM; i++) {
		printf("%d item: ", i+1);
		scanf("%d", &lista[i]);
	}
	
	printf("\nLista desordenada: ");
	for (i = 0; i < TAM; i++) {
		printf("%d ", lista[i]);
	}
	
	flag = 1;
	while(flag) {
		flag = 0;
		for (i = 0; i < TAM - 1; i++) {
			if (lista[i] > lista[i+1]){
				aux = lista[i];
				lista[i] = lista[i+1];
				lista[i+1] = aux;
				flag = 1;
			}
		}
	}
	
	printf("\nLista ordenada: ");
	for (i = 0; i < TAM; i++) {
		printf("%d ", lista[i]);
	}
}