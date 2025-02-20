#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct No{
	char nome[10];
	struct No* prox;
	struct No* ant;
}No;

const char* nome_numero(int numero) {
    switch (numero) {
        case 0: return "zero";
        case 1: return "um";
        case 2: return "dois";
        case 3: return "tres";
        case 4: return "quatro";
        case 5: return "cinco";
        case 6: return "seis";
        case 7: return "sete";
        case 8: return "oito";
        case 9: return "nove";
        case 10: return "dez";
        default: return "";
    }
}

No* criar_no(int valor){
	No* novo_no = (No*)malloc(sizeof(No));
	if(novo_no == NULL){
		printf("Erro ao alocar a memória!!!\n");
		exit(1);
	}
	strcpy(novo_no->nome, nome_numero(valor));
	novo_no->prox = novo_no->ant = NULL;
	return novo_no;
}


void ordem_alfabetica(No** cabeca, int valor) {
    No* novo_no = criar_no(valor);

    if (*cabeca == NULL) {
        *cabeca = novo_no;
        novo_no->prox = novo_no;
        novo_no->ant = novo_no;
    } else {
        No* atual = *cabeca;

        do {
            if (strcmp(novo_no->nome, atual->nome) < 0) {

                novo_no->prox = atual;
                novo_no->ant = atual->ant;
                atual->ant->prox = novo_no;
                atual->ant = novo_no;

                if (atual == *cabeca) {
                    *cabeca = novo_no;
                }
                return;
            }
            atual = atual->prox;
        } while (atual != *cabeca);

        novo_no->prox = *cabeca;
        novo_no->ant = (*cabeca)->ant;
        (*cabeca)->ant->prox = novo_no;
        (*cabeca)->ant = novo_no;
    }
}

void lista(No* cabeca) {
    if (cabeca == NULL) {
        printf("Lista vazia!\n");
        return;
    }

    No* atual = cabeca;
    do {
        printf("%s ", atual->nome);
        atual = atual->prox;
    } while (atual != cabeca);
    printf("\n");
}

int main() {
    No* cabeca = NULL;  

    for (int i = 0; i <= 10; i++) {
        ordem_alfabetica(&cabeca, i);
    }

    printf("Lista em ordem alfabética:\n");
    lista(cabeca);

    return 0;
}