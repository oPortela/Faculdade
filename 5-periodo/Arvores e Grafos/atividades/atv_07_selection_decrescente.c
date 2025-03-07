//Execicio 07
//Implementação do metodo Selection Sort

#include <stdio.h>
#define TAM 5

void selectionSortDecrescente(int arr[], int n) {
	int i, j, min_idx, temp;
	for (i = 0; i < n-1; i++) { 
		min_idx = i;
		for (j = i + 1; j < n; j++) {
			if (arr[j] > arr[min_idx]) {
				min_idx = j; 
			}
		}
		temp = arr[min_idx];
		arr[min_idx] = arr[i];
		arr[i] = temp;
	}
}

void selectionSort(int arr[], int n) {
	int i, j, min_idx, temp;
	for (i = 0; i < n-1; i++) { 
		min_idx = i;
		for (j = i + 1; j < n; j++) {
			if (arr[j] < arr[min_idx]) {
				min_idx = j; 
			}
		}
		temp = arr[min_idx];
		arr[min_idx] = arr[i];
		arr[i] = temp;
	}
}

int main() {
	int i;
	int lista[TAM];
	
	for (i = 0; i < TAM; i++){
		printf("%d item: ", i + 1);
		scanf("%d", &lista[i]);
	}
	
	//Lista desordenada
	for (i = 0; i < TAM; i++){
		printf("%d ", lista[i]);
	}
	
	selectionSort(lista, TAM);
	printf("\n\n\n");
	//Lista ordenada
	printf("Lista com o Selection Sort crescente: \n");
	for (i = 0; i < TAM; i++){
		printf("%d ", lista[i]);
	}
	
	selectionSortDecrescente(lista, TAM);
	printf("\n\n\n");
	//Lista ordenada decrescente
	printf("Lista com o Selection Sort decrescente: \n");
	for (i = 0; i < TAM; i++){
		printf("%d ", lista[i]);
	}
}