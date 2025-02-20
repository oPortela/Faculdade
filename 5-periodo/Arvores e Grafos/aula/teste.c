#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Função para preencher o vetor em ordem decrescente
void preencher_vetor(int *vetor, int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        vetor[i] = tamanho - i;
    }
}

// Bubble Sort
void bubble_sort(int *vetor, int tamanho, int *comparacoes, int *movimentacoes) {
    *comparacoes = 0;
    *movimentacoes = 0;
    for (int i = 0; i < tamanho - 1; i++) {
        for (int j = 0; j < tamanho - i - 1; j++) {
            (*comparacoes)++;
            if (vetor[j] > vetor[j + 1]) {
                int temp = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = temp;
                (*movimentacoes)++;
            }
        }
    }
}

// Selection Sort
void selection_sort(int *vetor, int tamanho, int *comparacoes, int *movimentacoes) {
    *comparacoes = 0;
    *movimentacoes = 0;
    for (int i = 0; i < tamanho - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < tamanho; j++) {
            (*comparacoes)++;
            if (vetor[j] < vetor[min_idx]) {
                min_idx = j;
            }
        }
        if (min_idx != i) {
            int temp = vetor[i];
            vetor[i] = vetor[min_idx];
            vetor[min_idx] = temp;
            (*movimentacoes)++;
        }
    }
}

// Função para medir o tempo de execução e chamar o algoritmo de ordenação
void executar_algoritmo(void (*algoritmo)(int*, int, int*, int*), int *vetor, int tamanho, char *nome_algoritmo) {
    clock_t inicio, fim;
    int comparacoes, movimentacoes;

    // Copiar o vetor original para não alterá-lo
    int *vetor_copia = (int*)malloc(tamanho * sizeof(int));
    for (int i = 0; i < tamanho; i++) {
        vetor_copia[i] = vetor[i];
    }

    inicio = clock();
    algoritmo(vetor_copia, tamanho, &comparacoes, &movimentacoes);
    fim = clock();

    double tempo_execucao = ((double)(fim - inicio)) / CLOCKS_PER_SEC * 1000; // Tempo em milissegundos

    printf("%s:\n", nome_algoritmo);
    printf("  Tempo de execução: %.2f ms\n", tempo_execucao);
    printf("  Comparações: %d\n", comparacoes);
    printf("  Movimentações: %d\n", movimentacoes);

    free(vetor_copia);
}

int main() {
    int tamanhos[] = {100, 1000, 10000};
    int num_tamanhos = sizeof(tamanhos) / sizeof(tamanhos[0]);

    for (int i = 0; i < num_tamanhos; i++) {
        int tamanho = tamanhos[i];
        int *vetor = (int*)malloc(tamanho * sizeof(int));

        preencher_vetor(vetor, tamanho);

        printf("Tamanho do vetor: %d\n", tamanho);
        executar_algoritmo(bubble_sort, vetor, tamanho, "Bubble Sort");
        executar_algoritmo(selection_sort, vetor, tamanho, "Selection Sort");
        printf("----------------------------------------\n");

        free(vetor);
    }

    return 0;
}