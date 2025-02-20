#include <stdio.h>
#include <stdlib.h>

typedef struct No {
    int valor;
    struct No* proximo;
} No;

typedef struct {
    No* inicio;
} FilaPrioridade;

FilaPrioridade* criarFila() {
    FilaPrioridade* fila = (FilaPrioridade*)malloc(sizeof(FilaPrioridade));
    fila->inicio = NULL;
    return fila;
}

void destruirFila(FilaPrioridade* fila) {
    No* atual = fila->inicio;
    while (atual != NULL) {
        No* temp = atual;
        atual = atual->proximo;
        free(temp);
    }
    free(fila);
}

void exibirFila(FilaPrioridade* fila) {
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

void enqueue(FilaPrioridade* fila, int valor) {
    No* novoNo = (No*)malloc(sizeof(No));
    novoNo->valor = valor;
    novoNo->proximo = NULL;

    if (fila->inicio == NULL || valor < fila->inicio->valor) {
        novoNo->proximo = fila->inicio;
        fila->inicio = novoNo;
    } else {
        No* atual = fila->inicio;
        while (atual->proximo != NULL && atual->proximo->valor <= valor) {
            atual = atual->proximo;
        }
        novoNo->proximo = atual->proximo;
        atual->proximo = novoNo;
    }

    printf("Elemento %d inserido na fila.\n", valor);
    exibirFila(fila);
}

int dequeue(FilaPrioridade* fila) {
    if (fila->inicio == NULL) {
        printf("Erro: Fila vazia!\n");
        return -1;
    }

    No* temp = fila->inicio;
    int valorRemovido = temp->valor;
    fila->inicio = fila->inicio->proximo;
    free(temp);

    printf("Elemento %d removido da fila.\n", valorRemovido);
    exibirFila(fila);
    return valorRemovido;
}

int main() {
    FilaPrioridade* fila = criarFila();

    enqueue(fila, 30);
    enqueue(fila, 10);
    enqueue(fila, 20);
    enqueue(fila, 40);
    enqueue(fila, 15);

    dequeue(fila);
    dequeue(fila);
    dequeue(fila);
    dequeue(fila);
    dequeue(fila);
    dequeue(fila);

    destruirFila(fila);
}
