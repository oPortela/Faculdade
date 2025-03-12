#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int medianOfThree(int arr[], int low, int high) {
    int mid = low + (high - low) / 2;

    if (arr[low] > arr[mid])
        swap(&arr[low], &arr[mid]);
    if (arr[low] > arr[high])
        swap(&arr[low], &arr[high]);
    if (arr[mid] > arr[high])
        swap(&arr[mid], &arr[high]);

    swap(&arr[mid], &arr[low]);
    return arr[low];  
}

int partitionClassic(int arr[], int low, int high) {
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

int partitionMedianOfThree(int arr[], int low, int high) {
    int pivot = medianOfThree(arr, low, high); 
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

void quickSortClassic(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionClassic(arr, low, high);
        quickSortClassic(arr, low, pi - 1);
        quickSortClassic(arr, pi + 1, high);
    }
}

void quickSortMedian(int arr[], int low, int high) {
    if (low < high) {
        int pi = partitionMedianOfThree(arr, low, high);
        quickSortMedian(arr, low, pi - 1);
        quickSortMedian(arr, pi + 1, high);
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
        printf("Erro.\n");
        return;
    }

    generateRandomArray(arr1, size);
    copyArray(arr1, arr2, size);

    clock_t start, end;
    double time_taken;

    start = clock();
    quickSortClassic(arr1, 0, size - 1);
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("QuickSort Classico para %d elementos: %f segundos\n", size, time_taken);

    start = clock();
    quickSortMedian(arr2, 0, size - 1);
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("QuickSort com Mediana de Tres para %d elementos: %f segundos\n\n", size, time_taken);

    free(arr1);
    free(arr2);
}

int main() {
    srand(time(NULL));

    printf("Teste com 1000 elementos:\n");
    testPerformance(1000);

    printf("Teste com 10000 elementos:\n");
    testPerformance(10000);

    printf("Teste com 50000 elementos:\n");
    testPerformance(50000);

    return 0;
}
