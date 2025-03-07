#include <stdio.h>

#define TAM 5

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    int trocou; // Flag para indicar se houve troca

    for (i = 0; i < n - 1; i++) {
        trocou = 0; // Inicializa como 0 (nenhuma troca feita)

        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Troca os elementos
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                
                trocou = 1; // Marca que houve troca
            }
        }

        // Se não houve troca na passagem, o vetor já está ordenado
        if (trocou == 0) {
            break;
        }
    }
}

int main() {
    int lista[TAM] = {3, 2, 1, 4, 5};
    int i;

    printf("Lista original: ");
    for (i = 0; i < TAM; i++) {
        printf("%d ", lista[i]);
    }

    bubbleSort(lista, TAM);

    printf("\nLista ordenada: ");
    for (i = 0; i < TAM; i++) {
        printf("%d ", lista[i]);
    }

    return 0;
}
