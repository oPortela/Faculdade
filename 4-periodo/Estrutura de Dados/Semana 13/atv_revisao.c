#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Tarefa {
    int id;
    char titulo[50];
    int prioridade;
    char data_criacao[11];
    struct Tarefa* anterior;
    struct Tarefa* proximo;
} Tarefa;


Tarefa* criar_tarefa(int id, const char* titulo, int prioridade, const char* data_criacao) {
    Tarefa* nova = (Tarefa*)malloc(sizeof(Tarefa));
    nova->id = id;
    strcpy(nova->titulo, titulo);
    nova->prioridade = prioridade;
    strcpy(nova->data_criacao, data_criacao);
    nova->anterior = NULL;
    nova->proximo = NULL;
    return nova;
}

void adicionar_tarefa(Tarefa** cabeca, Tarefa* nova_tarefa) {
    if (*cabeca == NULL) {
        *cabeca = nova_tarefa;
        return;
    }

    Tarefa* atual = *cabeca;
    while (atual != NULL && atual->prioridade <= nova_tarefa->prioridade) {
        atual = atual->proximo;
    }

    if (atual == NULL) { 
        Tarefa* ultimo = *cabeca;
        while (ultimo->proximo != NULL) {
            ultimo = ultimo->proximo;
        }
        ultimo->proximo = nova_tarefa;
        nova_tarefa->anterior = ultimo;
    } else if (atual->anterior == NULL) { 
        nova_tarefa->proximo = *cabeca;
        (*cabeca)->anterior = nova_tarefa;
        *cabeca = nova_tarefa;
    } else { 
        nova_tarefa->proximo = atual;
        nova_tarefa->anterior = atual->anterior;
        atual->anterior->proximo = nova_tarefa;
        atual->anterior = nova_tarefa;
    }
}

void remover_tarefa(Tarefa** cabeca, int id) {
    Tarefa* atual = *cabeca;
    while (atual != NULL && atual->id != id) {
        atual = atual->proximo;
    }
    if (atual == NULL) {
        printf("Tarefa com ID %d não encontrada.\n", id);
        return;
    }
    if (atual->anterior != NULL) {
        atual->anterior->proximo = atual->proximo;
    } else {
        *cabeca = atual->proximo; 
    }
    if (atual->proximo != NULL) {
        atual->proximo->anterior = atual->anterior;
    }
    free(atual);
    printf("Tarefa com ID %d removida.\n", id);
}

void buscar_tarefa(Tarefa* cabeca, int id) {
    Tarefa* atual = cabeca;
    while (atual != NULL && atual->id != id) {
        atual = atual->proximo;
    }
    if (atual == NULL) {
        printf("Tarefa com ID %d não encontrada.\n", id);
    } else {
        printf("ID: %d, Título: %s, Prioridade: %d, Data de Criação: %s\n", 
               atual->id, atual->titulo, atual->prioridade, atual->data_criacao);
    }
}

void listar_tarefas(Tarefa* cabeca) {
    Tarefa* atual = cabeca;
    printf("Tarefas em ordem de prioridade:\n");
    while (atual != NULL) {
        printf("ID: %d, Título: %s, Prioridade: %d, Data de Criação: %s\n", 
               atual->id, atual->titulo, atual->prioridade, atual->data_criacao);
        atual = atual->proximo;
    }
}

void listar_tarefas_inverso(Tarefa* cabeca) {
    Tarefa* atual = cabeca;
    if (atual == NULL) {
        printf("Lista vazia.\n");
        return;
    }

    while (atual->proximo != NULL) {
        atual = atual->proximo;
    }
    printf("Tarefas em ordem inversa:\n");
    while (atual != NULL) {
        printf("ID: %d, Título: %s, Prioridade: %d, Data de Criação: %s\n", 
               atual->id, atual->titulo, atual->prioridade, atual->data_criacao);
        atual = atual->anterior;
    }
}


void liberar_tarefas(Tarefa* cabeca) {
    while (cabeca != NULL) {
        Tarefa* proximo = cabeca->proximo;
        free(cabeca);
        cabeca = proximo;
    }
}

int main() {
    Tarefa* cabeca = NULL;
    int opcao, id, prioridade;
    char titulo[50], data_criacao[11];

    do {
        printf("\nSistema de Gerenciamento de Tarefas\n");
        printf("1. Adicionar Tarefa\n");
        printf("2. Remover Tarefa\n");
        printf("3. Buscar Tarefa\n");
        printf("4. Listar Tarefas (Ordem de Prioridade)\n");
        printf("5. Listar Tarefas (Ordem Inversa)\n");
        printf("0. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("ID da tarefa: ");
                scanf("%d", &id);
                printf("Título da tarefa: ");
                scanf(" %[^\n]", titulo);
                printf("Prioridade da tarefa: ");
                scanf("%d", &prioridade);
                printf("Data de criação (DD/MM/AAAA): ");
                scanf("%s", data_criacao);
                adicionar_tarefa(&cabeca, criar_tarefa(id, titulo, prioridade, data_criacao));
                break;
            case 2:
                printf("ID da tarefa a remover: ");
                scanf("%d", &id);
                remover_tarefa(&cabeca, id);
                break;
            case 3:
                printf("ID da tarefa a buscar: ");
                scanf("%d", &id);
                buscar_tarefa(cabeca, id);
                break;
            case 4:
                listar_tarefas(cabeca);
                break;
            case 5:
                listar_tarefas_inverso(cabeca);
                break;
            case 0:
                liberar_tarefas(cabeca);
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida.\n");
        }
    } while (opcao != 0);

    return 0;
}
