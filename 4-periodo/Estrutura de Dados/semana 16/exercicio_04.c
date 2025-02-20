#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

typedef struct Cliente {
    char nome[50];
    struct Cliente* proximo;
} Cliente;

typedef struct {
    Cliente* inicio;
    Cliente* fim;
} Fila;

Fila* criarFila() {
    Fila* fila = (Fila*)malloc(sizeof(Fila));
    fila->inicio = NULL;
    fila->fim = NULL;
    return fila;
}

void destruirFila(Fila* fila) {
    Cliente* atual = fila->inicio;
    while (atual != NULL) {
        Cliente* temp = atual;
        atual = atual->proximo;
        free(temp);
    }
    free(fila);
}

void exibirFila(Fila* fila) {
    if (fila->inicio == NULL) {
        printf("Fila vazia!\n");
        return;
    }
    Cliente* atual = fila->inicio;
    printf("Fila atual: ");
    while (atual != NULL) {
        printf("%s ", atual->nome);
        atual = atual->proximo;
    }
    printf("\n");
}

void enqueue(Fila* fila, const char* nome) {
    Cliente* novoCliente = (Cliente*)malloc(sizeof(Cliente));
    strcpy(novoCliente->nome, nome);
    novoCliente->proximo = NULL;

    if (fila->fim == NULL) {
        fila->inicio = novoCliente;
        fila->fim = novoCliente;
    } else {
        fila->fim->proximo = novoCliente;
        fila->fim = novoCliente;
    }

    printf("Cliente %s entrou na fila.\n", nome);
    exibirFila(fila);
}

void dequeue(Fila* fila) {
    if (fila->inicio == NULL) {
        printf("Erro: Fila vazia!\n");
        return;
    }

    Cliente* temp = fila->inicio;
    printf("Atendendo cliente: %s\n", temp->nome);
    sleep(2); 

    fila->inicio = fila->inicio->proximo;
    if (fila->inicio == NULL) {
        fila->fim = NULL;
    }

    free(temp);
    exibirFila(fila);
}

int main() {
    Fila* fila = criarFila();

    enqueue(fila, "João");
    enqueue(fila, "Maria");
    enqueue(fila, "Pedro");
    enqueue(fila, "Ana");

    dequeue(fila);
    dequeue(fila);
    enqueue(fila, "Lucas");
    enqueue(fila, "Mariana");

    dequeue(fila);
    dequeue(fila);
    dequeue(fila);
    dequeue(fila);

    destruirFila(fila);
}
