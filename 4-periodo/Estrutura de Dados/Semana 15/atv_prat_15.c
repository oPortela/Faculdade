#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include<locale.h>

typedef struct Pedido {
    int id;
    char nomeCliente[50];
    char descricao[100];
    char status[20];
    time_t horario;
    struct Pedido *proximo;
} Pedido;

Pedido *primeiro = NULL;

void adicionarPedido(int id, const char *nomeCliente, const char *descricao, const char *status, time_t horario) {
    Pedido *novo = (Pedido *)malloc(sizeof(Pedido));
    novo->id = id;
    strcpy(novo->nomeCliente, nomeCliente);
    strcpy(novo->descricao, descricao);
    strcpy(novo->status, status);
    novo->horario = horario;
    novo->proximo = NULL;

    if (!primeiro) {
        primeiro = novo;
    } else {
        Pedido *temp = primeiro;
        while (temp->proximo) {
            temp = temp->proximo;
        }
        temp->proximo = novo;
    }
    printf("Pedido %d adicionado com sucesso.\n", id);
}

void removerPedido(int id) {
    Pedido *temp = primeiro, *anterior = NULL;

    while (temp && temp->id != id) {
        anterior = temp;
        temp = temp->proximo;
    }

    if (!temp) {
        printf("Pedido %d nao encontrado.\n", id);
        return;
    }

    if (!anterior) {
        primeiro = temp->proximo;
    } else {
        anterior->proximo = temp->proximo;
    }

    free(temp);
    printf("Pedido %d removido com sucesso.\n", id);
}

void atualizarStatus(int id, const char *novoStatus) {
    Pedido *temp = primeiro;

    while (temp && temp->id != id) {
        temp = temp->proximo;
    }

    if (!temp) {
        printf("Pedido %d nao encontrado.\n", id);
        return;
    }

    strcpy(temp->status, novoStatus);
    printf("Status do pedido %d atualizado para %s.\n", id, novoStatus);
}

void buscarPorCliente(const char *nomeCliente) {
    Pedido *temp = primeiro;
    int encontrado = 0;

    while (temp) {
        if (strcmp(temp->nomeCliente, nomeCliente) == 0) {
            printf("ID: %d, Cliente: %s, Descricao: %s, Status: %s, Horario: %s",
                   temp->id, temp->nomeCliente, temp->descricao, temp->status, ctime(&temp->horario));
            encontrado = 1;
        }
        temp = temp->proximo;
    }

    if (!encontrado) {
        printf("Nenhum pedido encontrado para o cliente %s.\n", nomeCliente);
    }
}

void exibirPorStatus(const char *status) {
    Pedido *temp = primeiro;

    while (temp) {
        if (strcmp(temp->status, status) == 0) {
            printf("ID: %d, Cliente: %s, Descricao: %s, Status: %s, Horario: %s",
                   temp->id, temp->nomeCliente, temp->descricao, temp->status, ctime(&temp->horario));
        }
        temp = temp->proximo;
    }
}

void ordenarPorHorario(int crescente) {
    if (!primeiro) return;

    Pedido *i, *j;
    for (i = primeiro; i->proximo; i = i->proximo) {
        for (j = i->proximo; j; j = j->proximo) {
            if ((crescente && i->horario > j->horario) ||
                (!crescente && i->horario < j->horario)) {
                Pedido temp = *i;
                *i = *j;
                *j = temp;
            }
        }
    }
}

void listarPedidos() {
    Pedido *temp = primeiro;
    int encontrado = 0;

    while (temp) {
        printf("ID: %d, Cliente: %s, Descricao: %s, Status: %s, Horario: %s",
               temp->id, temp->nomeCliente, temp->descricao, temp->status, ctime(&temp->horario));
        temp = temp->proximo;
        encontrado += 1;
    }
    
    if (!encontrado) {
        printf("Nenhum pedido feito no sistema.\n");
    }
}

void liberarMemoria() {
    Pedido *temp;

    while (primeiro) {
        temp = primeiro;
        primeiro = primeiro->proximo;
        free(temp);
    }
    printf("Memoria liberada.\n");
}

int main() {
	setlocale(LC_ALL, "Portuguese");
	
    int opcao, id;
    char nomeCliente[50], descricao[100], status[20];
    time_t horario;

    do {
        printf("\n1. Adicionar Pedido\n");
        printf("2. Remover Pedido\n");
        printf("3. Atualizar Status\n");
        printf("4. Buscar por Cliente\n");
        printf("5. Exibir por Status\n");
        printf("6. Ordenar Pedidos por Horario\n");
        printf("7. Listar Todos os Pedidos\n");
        printf("8. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("ID do Pedido: ");
                scanf("%d", &id);
                printf("Nome do Cliente: ");
                scanf(" %[^\n]", nomeCliente);
                printf("Descricao do Pedido: ");
                scanf(" %[^\n]", descricao);
                printf("Status (Aguardando, Em Preparacao, Concluido): ");
                scanf(" %[^\n]", status);
                horario = time(NULL);
                adicionarPedido(id, nomeCliente, descricao, status, horario);
                break;

            case 2:
                printf("ID do Pedido para remover: ");
                scanf("%d", &id);
                removerPedido(id);
                break;

            case 3:
                printf("ID do Pedido para atualizar: ");
                scanf("%d", &id);
                printf("Novo Status: ");
                scanf(" %[^\n]", status);
                atualizarStatus(id, status);
                break;

            case 4:
                printf("Nome do Cliente para buscar: ");
                scanf(" %[^\n]", nomeCliente);
                buscarPorCliente(nomeCliente);
                break;

            case 5:
                printf("Status dos pedidos para exibir: ");
                scanf(" %[^\n]", status);
                exibirPorStatus(status);
                break;

            case 6:
                printf("Ordenar por horario (1 = Crescente, 0 = Decrescente): ");
                int crescente;
                scanf("%d", &crescente);
                ordenarPorHorario(crescente);
                break;

            case 7:
                listarPedidos();
                break;

            case 8:
                liberarMemoria();
                printf("Encerrando o programa.\n");
                break;

            default:
                printf("Opcao invalida.\n");
        }
    } while (opcao != 8);

    return 0;
}
