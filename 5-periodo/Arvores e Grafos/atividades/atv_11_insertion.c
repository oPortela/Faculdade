#include <stdio.h>
#define TAM 10

void insertionSort(int arr[], int n) {
	int i, key, j;
	for (i = 1; i < n; i++) {
		key = arr[i];
		j = i - 1;
		while(j >= 0 && arr[j] > key) {
			arr[j + 1] = arr[j];
			j = j - 1;
		}
		arr[j + 1] = key;
	}
}

int main() {
	int i;
	int lista[] = {10,9,8,7,6,5,4,3,2,1};
	
	/*for (i = 0; i < TAM; i++){
		printf("%d item: ", i + 1);
		scanf("%d", &lista[i]);
	}*/
	
	//Lista desordenada
	for (i = 0; i < TAM; i++){
		printf("%d ", lista[i]);
	}
	
	insertionSort(lista, TAM);
	printf("\n\n\n");
	//Lista ordenada
	for (i = 0; i < TAM; i++){
		printf("%d ", lista[i]);
	}
}