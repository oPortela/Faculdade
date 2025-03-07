//Implementação do metodo Bubble Sort

#include <stdio.h>
#define TAM 10

void bubbleSort(int arr[], int n) {
	int i, j, temp;
	for (i = 0; i < n - 1; i++) {
		for (j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]){
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

int main() {
	int i;
	int lista[10];
	
	for (i = 0; i < TAM; i++){
		printf("%d item: ", i + 1);
		scanf("%d", &lista[i]);
	}
	
	//Lista desordenada
	for (i = 0; i < TAM; i++){
		printf("%d ", lista[i]);
	}
	
	bubbleSort(lista, TAM);
	printf("\n\n\n");
	//Lista ordenada
	for (i = 0; i < TAM; i++){
		printf("%d ", lista[i]);
	}
}