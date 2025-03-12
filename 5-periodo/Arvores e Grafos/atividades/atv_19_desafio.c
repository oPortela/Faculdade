#include <stdio.h>
#include <string.h>

#define MAX 100

typedef struct {
    char nome[50];
    int pontos;
} Jogador;

void mostrarRanking(Jogador ranking[], int tamanho) {
    printf("\nRanking Atualizado:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d. %s - %d pontos\n", i + 1, ranking[i].nome, ranking[i].pontos);
    }
}

void insertionSort(Jogador ranking[], int *tamanho, Jogador novo) {
    int i = *tamanho - 1;

    while (i >= 0 && ranking[i].pontos < novo.pontos) {
        ranking[i + 1] = ranking[i];
        i--;
    }

    ranking[i + 1] = novo;
    (*tamanho)++;
}

int main() {
    Jogador ranking[MAX] = {
        {"Matheus", 16},
        {"Pedro", 10},
        {"Marcos", 15}
    };
    int tamanho = 3;
    Jogador novoJogador;

    printf("Digite 'sair' como nome para encerrar.\n");

    while (1) {
        printf("\nDigite o nome do novo jogador: ");
        scanf("%s", novoJogador.nome);

        if (strcmp(novoJogador.nome, "sair") == 0) {
            break;
        }

        printf("Digite os pontos do novo jogador: ");
        scanf("%d", &novoJogador.pontos);

        insertionSort(ranking, &tamanho, novoJogador);
        mostrarRanking(ranking, tamanho);
    }

    printf("\nFinalizando o programa...\n");
    return 0;
}
