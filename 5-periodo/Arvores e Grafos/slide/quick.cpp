#include <stdio.h>
#include<locale.h>

void swap(int* a, int* b) {
    int t = *a;
    *a = *b;
    *b = t;
}

int partition(int arr[], int low, int high) {
    int pivo = arr[high];
    int i = low - 1;
    for (int j = low; j <= high - 1; j++) {
        if (arr[j] <= pivo) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

main() {
	setlocale(LC_ALL,"Portuguese");	
    int arr[] = {10, 7, 8, 9, 1, 5, 66, 77, 20, 100, 3};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("Array desordenado: ");
    printArray(arr, n);
    quickSort(arr, 0, n - 1);
	printf("\nArray ordenado: ");
    printArray(arr, n);

}

