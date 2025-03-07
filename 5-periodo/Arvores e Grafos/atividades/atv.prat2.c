#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high, int *comparacoes, int *movimentacoes) {
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j < high; j++) {
        (*comparacoes)++;
        if (arr[j] < pivot) {
            i++;
            swap(&arr[i], &arr[j]);
            (*movimentacoes) += 3;
        }
    }
    swap(&arr[i + 1], &arr[high]);
    (*movimentacoes) += 3;
    return (i + 1);
}

void quickSort(int arr[], int low, int high, int *comparacoes, int *movimentacoes) {
    if (low < high) {
        int pi = partition(arr, low, high, comparacoes, movimentacoes);
        quickSort(arr, low, pi - 1, comparacoes, movimentacoes);
        quickSort(arr, pi + 1, high, comparacoes, movimentacoes);
    }
}

void insertionSort(int arr[], int n, int *comparacoes, int *movimentacoes) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key) {
            (*comparacoes)++;
            arr[j + 1] = arr[j];
            (*movimentacoes)++;
            j = j - 1;
        }
        arr[j + 1] = key;
        (*movimentacoes)++;
    }
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

void preencherVetor(int arr[], int n, int tipo) {
    if (tipo == 0) {
        for (int i = 0; i < n; i++) arr[i] = i + 1;
    } else if (tipo == 1) {
        for (int i = 0; i < n; i++) arr[i] = n - i;
    } else {
        for (int i = 0; i < n; i++) arr[i] = rand() % 10000;
    }
}

void executarTeste(int tamanho, int tipo) {
    int *arr = (int *)malloc(tamanho * sizeof(int));
    clock_t inicio, fim;
    double tempo;
    int comparacoes, movimentacoes;
    
    printf("\nTeste com vetor tamanho %d\n", tamanho);
    
    preencherVetor(arr, tamanho, tipo);
    comparacoes = movimentacoes = 0;
    inicio = clock();
    insertionSort(arr, tamanho, &comparacoes, &movimentacoes);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000;
    printf("Insertion Sort\t%.2f ms\t%d\t%d\n", tempo, comparacoes, movimentacoes);
    
    preencherVetor(arr, tamanho, tipo);
    comparacoes = movimentacoes = 0;
    inicio = clock();
    quickSort(arr, 0, tamanho - 1, &comparacoes, &movimentacoes);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000;
    printf("Quick Sort\t%.2f ms\t%d\t%d\n", tempo, comparacoes, movimentacoes);
    
    free(arr);
}

int main() {
    srand(time(NULL));
    printf("Algoritmo\tTempo (ms)\tComparacoes\tMovimentacoes\n");
    executarTeste(100, 0);
    executarTeste(100, 1);
    executarTeste(100, 2);
    executarTeste(1000, 0);
    executarTeste(1000, 1);
    executarTeste(1000, 2);
    executarTeste(10000, 0);
    executarTeste(10000, 1);
    executarTeste(10000, 2);
    return 0;
}
