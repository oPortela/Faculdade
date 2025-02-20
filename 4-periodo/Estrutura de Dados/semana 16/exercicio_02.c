#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No* proximo;
} No;

typedef struct {
    No* inicio;
    No* fim;
} Fila;

Fila* criarFila() {
    Fila* fila = (Fila*)malloc(sizeof(Fila));
    fila->inicio = NULL;
    fila->fim = NULL;
    return fila;
}

void destruirFila(Fila* fila) {
    No* atual = fila->inicio;
    while (atual != NULL) {
        No* temp = atual;
        atual = atual->proximo;
        free(temp);
    }
    free(fila);
}

void enqueue(Fila* fila, int valor) {
    No* novoNo = (No*)malloc(sizeof(No));
    novoNo->valor = valor;
    novoNo->proximo = NULL;

    if (fila->fim == NULL) {
        fila->inicio = novoNo;
        fila->fim = novoNo;
    } else {
        fila->fim->proximo = novoNo;
        fila->fim = novoNo;
    }

    printf("Elemento %d adicionado à fila.\n", valor);
}

int dequeue(Fila* fila) {
    if (fila->inicio == NULL) {
        printf("Erro: Fila vazia!\n");
        return -1;
    }

    No* temp = fila->inicio;
    int valorRemovido = temp->valor;

    fila->inicio = fila->inicio->proximo;

    if (fila->inicio == NULL) {
        fila->fim = NULL;
    }

    free(temp);

    printf("Elemento %d removido da fila.\n", valorRemovido);
    return valorRemovido;
}

void exibirFila(Fila* fila) {
    if (fila->inicio == NULL) {
        printf("Fila vazia!\n");
        return;
    }

    No* atual = fila->inicio;
    printf("Fila: ");
    while (atual != NULL) {
        printf("%d ", atual->valor);
        atual = atual->proximo;
    }
    printf("\n");
}

int main() {
    Fila* fila = criarFila();

    enqueue(fila, 10);
    enqueue(fila, 20);
    enqueue(fila, 30);
    enqueue(fila, 40);

    exibirFila(fila);

    dequeue(fila);
    dequeue(fila);

    exibirFila(fila);

    dequeue(fila);
    dequeue(fila);
    dequeue(fila);

    destruirFila(fila);
}
