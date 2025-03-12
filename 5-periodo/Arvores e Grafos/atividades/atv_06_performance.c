#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(int arr[], int n) {
	int i, j, temp;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n - 1 - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
} 

void selectionSort(int arr[], int n) {
	int i, j, min_idx, temp;
	for(i = 0; i < n - 1; i++) {
		min_idx = i;
		for(j = i + 1; j < n; j++) {
			if (arr[j] < arr[min_idx]) {
				min_idx = j;
			}
		}
		temp = arr[min_idx];
		arr[min_idx] = arr[i];
		arr[i] = temp;
	}
}

void fillArray(int arr[], int n) {
	for (int i = 0; i < n; i++) {
		arr[i] = rand() % 10000;
	}
}

void copyArray(int source[], int dest[], int n) {
    for (int i = 0; i < n; i++) {
        dest[i] = source[i];
    }
}

void testSorting(int n) {
    int *arr1 = (int *)malloc(n * sizeof(int));
    int *arr2 = (int *)malloc(n * sizeof(int));
    
    fillArray(arr1, n);
    copyArray(arr1, arr2, n);
    
    clock_t start, end;
    double time_taken;
    
    start = clock();
    bubbleSort(arr1, n);
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("BubbleSort para %d elementos: %f segundos\n", n, time_taken);
    
    start = clock();
    selectionSort(arr2, n);
    end = clock();
    time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("SelectionSort para %d elementos: %f segundos\n", n, time_taken);
    
    free(arr1);
    free(arr2);
}

int main() {
	srand(time(NULL));
	
	int sizes[] = {100,1000,5000,10000};
	int num_sizes = sizeof(sizes) / sizeof(sizes[0]);
	
	for(int i = 0; i < num_sizes; i++) {
		testSorting(sizes[i]);
		printf("-----\n");
	}
}