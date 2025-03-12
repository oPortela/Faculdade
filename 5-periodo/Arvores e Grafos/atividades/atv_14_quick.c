#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high) {
    int pivot = arr[low]; 
    int i = low + 1;
    int j = high;

    while (i <= j) {
        while (i <= high && arr[i] <= pivot) i++;  
        while (arr[j] > pivot) j--;               

        if (i < j) {
            swap(&arr[i], &arr[j]);  
        }
    }

    swap(&arr[low], &arr[j]);  
    return j;  
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high); 
        quickSort(arr, low, pi - 1);  
        quickSort(arr, pi + 1, high); 
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void testQuickSort(int size) {
    int *arr = (int *)malloc(size * sizeof(int));
    if (!arr) {
        printf("Erro ao alocar memória.\n");
        return;
    }

    srand(time(NULL));
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 1000; 
    }

    printf("Array original:\n");
    printArray(arr, size);

    // Aplicando QuickSort
    quickSort(arr, 0, size - 1);

    printf("Array ordenado:\n");
    printArray(arr, size);

    free(arr);
}

int main() {
    printf("Teste com 10 elementos:\n");
    testQuickSort(10);

    printf("\nTeste com 20 elementos:\n");
    testQuickSort(20);

    printf("\nTeste com 50 elementos:\n");
    testQuickSort(50);

    return 0;
}
