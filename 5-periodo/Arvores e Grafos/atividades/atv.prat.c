#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(int arr[], int n, int *comparacoes, int *movimentacoes) {
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            (*comparacoes)++;
            if (arr[j] > arr[j + 1]) {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                (*movimentacoes) += 3;
            }
        }
    }
}

void selectionSort(int arr[], int n, int *comparacoes, int *movimentacoes) {
    int i, j, min_idx, temp;
    for (i = 0; i < n - 1; i++) {
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            (*comparacoes)++;
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        if (min_idx != i) {
            temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
            (*movimentacoes) += 3;
        }
    }
}

void preencherVetorDecrescente(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = n - i;
    }
}

void executarTeste(int tamanho) {
    int *arr = (int *)malloc(tamanho * sizeof(int));
    clock_t inicio, fim;
    double tempo;
    int comparacoes, movimentacoes;
    
    // Bubble Sort
    preencherVetorDecrescente(arr, tamanho);
    comparacoes = movimentacoes = 0;
    inicio = clock();
    bubbleSort(arr, tamanho, &comparacoes, &movimentacoes);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000;
    printf("Bubble Sort\t%d\t%.2f ms\t%d\t%d\n", tamanho, tempo, comparacoes, movimentacoes);
    
    // Selection Sort
    preencherVetorDecrescente(arr, tamanho);
    comparacoes = movimentacoes = 0;
    inicio = clock();
    selectionSort(arr, tamanho, &comparacoes, &movimentacoes);
    fim = clock();
    tempo = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000;
    printf("Selection Sort\t%d\t%.2f ms\t%d\t%d\n", tamanho, tempo, comparacoes, movimentacoes);
    
    free(arr);
}

int main() {
    printf("Algoritmo\tTamanho\tTempo (ms)\tComparacoes\tMovimentacoes\n");
    executarTeste(100);
    executarTeste(1000);
    executarTeste(10000);
    return 0;
}
