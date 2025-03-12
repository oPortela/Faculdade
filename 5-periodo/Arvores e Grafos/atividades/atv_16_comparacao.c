#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void insertionSort(int arr[], int size) {
    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int partition(int arr[], int low, int high) {
    int pivot = arr[low];  
    int i = low + 1;
    int j = high;

    while (i <= j) {
        while (i <= high && arr[i] <= pivot) i++;
        while (arr[j] > pivot) j--;

        if (i < j)
            swap(&arr[i], &arr[j]);
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

void generateRandomArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 1000;
    }
}

void copyArray(int src[], int dest[], int size) {
    for (int i = 0; i < size; i++) {
        dest[i] = src[i];
    }
}

void testPerformance(int size) {
    int *arr1 = (int *)malloc(size * sizeof(int));
    int *arr2 = (int *)malloc(size * sizeof(int));

    if (!arr1 || !arr2) {
        printf("Erro ao alocar memória.\n");
        return;
    }

    generateRandomArray(arr1, size);
    copyArray(arr1, arr2, size);

    clock_t start, end;
    double time_taken;

    start = clock();
    insertionSort(arr1, size);
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("InsertionSort para %d elementos: %f segundos\n", size, time_taken);

    start = clock();
    quickSort(arr2, 0, size - 1);
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("QuickSort para %d elementos: %f segundos\n\n", size, time_taken);

    free(arr1);
    free(arr2);
}

int main() {
    srand(time(NULL));

    printf("Teste com 100 elementos:\n");
    testPerformance(100);

    printf("Teste com 500 elementos:\n");
    testPerformance(500);

    printf("Teste com 1000 elementos:\n");
    testPerformance(1000);

    printf("Teste com 5000 elementos:\n");
    testPerformance(5000);

    printf("Teste com 10000 elementos:\n");
    testPerformance(10000);

    return 0;
}
