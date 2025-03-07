//Implementação do metodo Bubble Sort

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define TAM 10

void bubbleSort(int arr[], int n, int *comparacoes, int *movimentacoes) {
	int i, j, temp;
	for (i = 0; i < n - 1; i++) {
		for (j = 0; j < n - i - 1; j++) {
			(*comparacoes)++;
			if (arr[j] > arr[j + 1]){
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
	for (i = 0; i < n-1; i++) { 
		min_idx = i;
		for (j = i + 1; j < n; j++) {
			(*comparacoes)++;
			if (arr[j] < arr[min_idx]) {
				min_idx = j; 
			}
		}
		temp = arr[min_idx];
		arr[min_idx] = arr[i];
		arr[i] = temp;
		(*movimentacoes) += 3;
	}
}

int main() {
	int i;
    int listaOriginal[TAM], listaBubble[TAM], listaSelection[TAM];
    clock_t inicioBubble, fimBubble, inicioSelection, fimSelection;
    double tempoBubble, tempoSelection;
    int compBubble = 0, movBubble = 0, compSelection = 0, movSelection = 0;

    // Entrada de dados
    for (i = 0; i < TAM; i++) {
        printf("%d item: ", i + 1);
        scanf("%d", &listaOriginal[i]);
    }

    // Criar cópias para cada algoritmo
    for (i = 0; i < TAM; i++) {
        listaBubble[i] = listaOriginal[i];
        listaSelection[i] = listaOriginal[i];
    }

    // Exibir lista original
    printf("\nLista original: ");
    for (i = 0; i < TAM; i++) {
        printf("%d ", listaOriginal[i]);
    }

    // Ordenação com Bubble Sort
    inicioBubble = clock();
    bubbleSort(listaBubble, TAM, &compBubble, &movBubble);
    fimBubble = clock();
    tempoBubble = ((double)(fimBubble - inicioBubble)) / CLOCKS_PER_SEC * 1000;

    // Exibir lista ordenada pelo Bubble Sort
    printf("\nLista ordenada pelo Bubble Sort: ");
    for (i = 0; i < TAM; i++) {
        printf("%d ", listaBubble[i]);
    }

    // Ordenação com Selection Sort
    inicioSelection = clock();
    selectionSort(listaSelection, TAM, &compSelection, &movSelection);
    fimSelection = clock();
    tempoSelection = ((double)(fimSelection - inicioSelection)) / CLOCKS_PER_SEC * 1000;

    // Exibir lista ordenada pelo Selection Sort
    printf("\nLista ordenada pelo Selection Sort: ");
    for (i = 0; i < TAM; i++) {
        printf("%d ", listaSelection[i]);
    }
	
	printf("\n\n\n\n");
	printf("No Bubble Sort temos os seguintes dados: Tempo: %f, Comparacoes: %d, Movimentacoes: %d", tempoBubble, compBubble, movBubble);
	printf("\n\n");
	printf("No Selection Sort temos os seguintes dados: Tempo: %f, Comparacoes: %d, Movimentacoes: %d", tempoSelection, compSelection, movSelection);
	
	return 0;
}