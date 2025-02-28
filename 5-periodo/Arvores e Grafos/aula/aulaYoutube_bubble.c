#include <stdio.h>
#define N 9

int lista[N]={4,5,8,2,9,1,3,7,6};
int trocas = 0;
int comp = 0;

void main() {
	int k;
	
	printf("Bubble Sort\n\n");
	printf("Lista original: ");
	for(k = 0; k < N; k++){
		printf("%d ", lista[k]);
	}
	bubbleSort(lista, N);
	printf("\nLista ordenada: ");
	for(k = 0; k < N; k++){
		printf("%d ", lista[k]);
	}
	
	printf("\n\nComparacoes: %d\ntrocas: %d\n\n", comp, trocas);
}

void bubbleSort(int *lista, int tamanho) {
	int i, aux;
	int flag = 1;
	while(flag) {
		flag = 0;
		for(i=0; i < tamanho -1; i++){
			comp++;
			if(lista[i] > lista[i+1]) {
				aux = lista[i];
				lista[i] = lista[i+1];
				lista[i+1] = aux;
				flag = 1;
				trocas++;
			}
		}
	}
}