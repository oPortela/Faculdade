#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

typedef struct Node {
    char url[MAX];
    struct Node* next;
} Node;

void push(Node** top, const char* url) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    if (new_node == NULL) {
        printf("Erro ao alocar memoria!\n");
        return;
    }
    strcpy(new_node->url, url);
    new_node->next = *top;
    *top = new_node;
}

void pop(Node** top) {
    if (*top == NULL) {
        printf("Nao ha paginas para voltar.\n");
        return;
    }
    Node* temp = *top;
    *top = (*top)->next;
    free(temp);
}

void print_history(Node* top) {
    if (top == NULL) {
        printf("Historico vazio.\n");
        return;
    }
    printf("Historico de navegaçao:\n");
    Node* current = top;
    while (current != NULL) {
        printf("%s\n", current->url);
        current = current->next;
    }
}

void free_stack(Node* top) {
    while (top != NULL) {
        Node* temp = top;
        top = top->next;
        free(temp);
    }
}

void display_menu() {
    printf("\nMenu de opçoes:\n");
    printf("1. Navegar para uma nova pagina\n");
    printf("2. Voltar para a pagina anterior\n");
    printf("3. Exibir historico de navegacao\n");
    printf("4. Sair\n");
}

int main() {
    Node* history_stack = NULL;
    int choice;
    char url[MAX];

    while (1) {
        display_menu();
        printf("Escolha uma opcao: ");
        scanf("%d", &choice);
        getchar();

        switch (choice) {
            case 1:
                printf("Digite a URL: ");
                fgets(url, MAX, stdin);
                url[strcspn(url, "\n")] = '\0';
                push(&history_stack, url);
                printf("Navegando para: %s\n", url);
                break;

            case 2:
                pop(&history_stack);
                break;

            case 3:
                print_history(history_stack);
                break;

            case 4:
                free_stack(history_stack);
                printf("Saindo do programa...\n");
                return 0;

            default:
                printf("Opcao invalida. Tente novamente.\n");
        }
    }

    return 0;
}
