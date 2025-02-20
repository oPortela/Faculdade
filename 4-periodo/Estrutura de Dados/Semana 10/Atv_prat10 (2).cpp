#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NOME 40
#define MAX_TELEFONE 15
#define MAX_EMAIL 40
#define MAX_DATA 5

typedef struct Contato {
    char nome[MAX_NOME];
    char telefone[MAX_TELEFONE];
    char celular[MAX_TELEFONE];
    char email[MAX_EMAIL];
    char data_aniversario[MAX_DATA];
    struct Contato* prox;
} Contato;

typedef struct {
    Contato* head;
} Agenda;

Agenda* cria_agenda() {
    Agenda* nova_agenda = (Agenda*)malloc(sizeof(Agenda));
    nova_agenda->head = NULL;
    return nova_agenda;
}

void insere_contato(Agenda* agenda, Contato* novo_contato) {
    Contato* atual = agenda->head;
    Contato* anterior = NULL;

    while (atual != NULL && strcmp(atual->nome, novo_contato->nome) < 0) {
        anterior = atual;
        atual = atual->prox;
    }

    if (anterior == NULL) {
        novo_contato->prox = agenda->head;
        agenda->head = novo_contato;
    } else {
        novo_contato->prox = atual;
        anterior->prox = novo_contato;
    }
}

void lista_contatos(Agenda* agenda) {
    Contato* atual = agenda->head;
    while (atual != NULL) {
        printf("Nome: %s, Telefone: %s, Celular: %s, Email: %s, Aniversario: %s\n", 
               atual->nome, atual->telefone, atual->celular, atual->email, atual->data_aniversario);
        atual = atual->prox;
    }
}

Contato* busca_contato(Agenda* agenda, const char* nome) {
    Contato* atual = agenda->head;
    while (atual != NULL) {
        if (strcmp(atual->nome, nome) == 0) {
            return atual;
        }
        atual = atual->prox;
    }
    return NULL;
}

void remove_contato(Agenda* agenda, const char* nome) {
    Contato* atual = agenda->head;
    Contato* anterior = NULL;

    while (atual != NULL && strcmp(atual->nome, nome) != 0) {
        anterior = atual;
        atual = atual->prox;
    }

    if (atual == NULL) {
        printf("Contato não encontrado!\n");
        return;
    }

    if (anterior == NULL) {
        agenda->head = atual->prox;
    } else {
        anterior->prox = atual->prox;
    }
    
    free(atual);
    printf("Contato removido com sucesso!\n");
}

void atualiza_contato(Agenda* agenda, const char* nome) {
    Contato* contato = busca_contato(agenda, nome);
    if (contato == NULL) {
        printf("Contato não encontrado!\n");
        return;
    }

    printf("Atualizando contato %s\n", contato->nome);
    printf("Novo Telefone: ");
    scanf("%s", contato->telefone);
    printf("Novo Celular: ");
    scanf("%s", contato->celular);
    printf("Novo Email: ");
    scanf("%s", contato->email);
    printf("Nova Data de Aniversário: ");
    scanf("%s", contato->data_aniversario);
    printf("Contato atualizado com sucesso!\n");
}

void remove_duplicados(Agenda* agenda) {
    Contato* atual = agenda->head;
    while (atual != NULL && atual->prox != NULL) {
        Contato* verificacao = atual;
        while (verificacao->prox != NULL) {
            if (strcmp(atual->nome, verificacao->prox->nome) == 0) {
                Contato* duplicado = verificacao->prox;
                verificacao->prox = duplicado->prox;
                free(duplicado);
            } else {
                verificacao = verificacao->prox;
            }
        }
        atual = atual->prox;
    }
}

void libera_agenda(Agenda* agenda) {
    Contato* atual = agenda->head;
    while (atual != NULL) {
        Contato* temp = atual;
        atual = atual->prox;
        free(temp);
    }
    free(agenda);
}

int main() {
    Agenda* agenda = cria_agenda();
    int opcao;

    do {
        printf("\nMenu:\n");
        printf("1. Inserir Contato\n");
        printf("2. Listar Contatos\n");
        printf("3. Buscar Contato\n");
        printf("4. Editar Contato\n");
        printf("5. Remover Contato\n");
        printf("6. Remover Contatos Duplicados\n");
        printf("7. Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        getchar();  // Limpar o buffer

        switch (opcao) {
            case 1: {
                Contato* novo = (Contato*)malloc(sizeof(Contato));
                printf("Nome: ");
                fgets(novo->nome, MAX_NOME, stdin);
                novo->nome[strcspn(novo->nome, "\n")] = 0;  // Remove newline
                printf("Telefone: ");
                fgets(novo->telefone, MAX_TELEFONE, stdin);
                novo->telefone[strcspn(novo->telefone, "\n")] = 0;
                printf("Celular: ");
                fgets(novo->celular, MAX_TELEFONE, stdin);
                novo->celular[strcspn(novo->celular, "\n")] = 0;
                printf("Email: ");
                fgets(novo->email, MAX_EMAIL, stdin);
                novo->email[strcspn(novo->email, "\n")] = 0;
                printf("Data de Aniversário (DD/MM): ");
                fgets(novo->data_aniversario, MAX_DATA, stdin);
                novo->data_aniversario[strcspn(novo->data_aniversario, "\n")] = 0;
                insere_contato(agenda, novo);
                break;
            }
            case 2:
                lista_contatos(agenda);
                break;
            case 3: {
                char nome[MAX_NOME];
                printf("Nome do contato a buscar: ");
                fgets(nome, MAX_NOME, stdin);
                nome[strcspn(nome, "\n")] = 0;
                Contato* contato = busca_contato(agenda, nome);
                if (contato) {
                    printf("Contato encontrado: %s, Telefone: %s, Celular: %s, Email: %s, Aniversario: %s\n",
                           contato->nome, contato->telefone, contato->celular, contato->email, contato->data_aniversario);
                } else {
                    printf("Contato não encontrado!\n");
                }
                break;
            }
            case 4: {
                char nome[MAX_NOME];
                printf("Nome do contato a editar: ");
                fgets(nome, MAX_NOME, stdin);
                nome[strcspn(nome, "\n")] = 0;
                atualiza_contato(agenda, nome);
                break;
            }
            case 5: {
                char nome[MAX_NOME];
                printf("Nome do contato a remover: ");
                fgets(nome, MAX_NOME, stdin);
                nome[strcspn(nome, "\n")] = 0;
                remove_contato(agenda, nome);
                break;
            }
            case 6:
                remove_duplicados(agenda);
                printf("Duplicados removidos!\n");
                break;
            case 7:
                libera_agenda(agenda);
                printf("Saindo...\n");
                break;
            default:
                printf("Opção inválida!\n");
                break;
        }
    } while (opcao != 7);

    return 0;
}

