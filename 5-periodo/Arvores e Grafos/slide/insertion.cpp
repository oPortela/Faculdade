#include <stdio.h>
#include<locale.h>

void insertionSort(int arr[], int n) {
    int i, chave, j;
    for (i = 1; i < n; i++) {
        chave = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > chave) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = chave;
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

main() {
	setlocale(LC_ALL,"Portuguese");
    int arr[] = {12, 11, 13, 5, 6, 4, 1, 89, 45, 22, 22, 47, 0, 27};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Tamanho da memória em Bytes alocada para o Array: %d \n", sizeof(arr));
    printf("Tamanho em Bytes: %d \n", sizeof(arr[0]));
	printf("Quantidade de Elementos no Array: %d \n", n);
    printf("\n Array Desordenado: ");
    printArray(arr, n);
    insertionSort(arr, n);
    printf("\n Array ordenado: ");
    printArray(arr, n);
 
}

