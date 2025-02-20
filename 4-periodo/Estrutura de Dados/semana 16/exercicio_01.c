#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int capacidade;
    int inicio;
    int fim;
    int tamanho;
    int* elementos;
} Fila;

Fila* criarFila(int capacidadeMax) {
    Fila* fila = (Fila*)malloc(sizeof(Fila));
    fila->capacidade = capacidadeMax;
    fila->inicio = 0;
    fila->fim = -1;
    fila->tamanho = 0;
    fila->elementos = (int*)malloc(capacidadeMax * sizeof(int));
    return fila;
}

void destruirFila(Fila* fila) {
    free(fila->elementos);
    free(fila);
}

void enqueue(Fila* fila, int elemento) {
    if (fila->tamanho == fila->capacidade) {
        printf("Erro: Fila cheia!\n");
        return;
    }
    fila->fim = (fila->fim + 1) % fila->capacidade;
    fila->elementos[fila->fim] = elemento;
    fila->tamanho++;
    printf("Elemento %d adicionado à fila.\n", elemento);
}

int dequeue(Fila* fila) {
    if (fila->tamanho == 0) {
        printf("Erro: Fila vazia!\n");
        return -1;
    }
    int elementoRemovido = fila->elementos[fila->inicio];
    fila->inicio = (fila->inicio + 1) % fila->capacidade;
    fila->tamanho--;
    printf("Elemento %d removido da fila.\n", elementoRemovido);
    return elementoRemovido;
}

void exibirFila(Fila* fila) {
    if (fila->tamanho == 0) {
        printf("Fila vazia!\n");
        return;
    }
    printf("Fila: ");
    for (int i = 0; i < fila->tamanho; i++) {
        int index = (fila->inicio + i) % fila->capacidade;
        printf("%d ", fila->elementos[index]);
    }
    printf("\n");
}

int main() {
    Fila* fila = criarFila(5);

    enqueue(fila, 10);
    enqueue(fila, 20);
    enqueue(fila, 30);
    enqueue(fila, 40);
    enqueue(fila, 50);

    exibirFila(fila);

    enqueue(fila, 60);

    dequeue(fila);
    dequeue(fila);

    exibirFila(fila);

    dequeue(fila);
    dequeue(fila);
    dequeue(fila);

    dequeue(fila);

    destruirFila(fila);
}
