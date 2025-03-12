//Implementação do metodo Bubble Sort

#include <stdio.h>
#define TAM 10

#include <stdio.h>
#define SIZE 10

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort(int arr[], int pos[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
                swap(&pos[j], &pos[j + 1]);
            }
        }
    }
}

void exibirPosicoes(int arr[], int pos[], int n) {
    printf("\nNumero | Posicao Inicial | Posicao Final\n");
    printf("--------------------------------------\n");
    
    for (int i = 0; i < n; i++) {
        printf("  %d     |        %d        |        %d\n", arr[i], pos[i], i);
    }
}

int main() {
    int arr[SIZE];
    int pos[SIZE];

	for (int i = 0; i < SIZE; i++){
		printf("%d item: ", i + 1);
		scanf("%d", &arr[i]);
	}
	printf("\n");

    for (int i = 0; i < SIZE; i++) {
        pos[i] = i;
    }

    printf("Vetor original:\n");
    for (int i = 0; i < SIZE; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    bubbleSort(arr, pos, SIZE);


    printf("\nVetor ordenado:\n");
    for (int i = 0; i < SIZE; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");


    exibirPosicoes(arr, pos, SIZE);

    return 0;
}
