#include <stdio.h>

// Definição da estrutura Produto
typedef struct {
    char nome[50];
    float preco;
} Produto;

// Função para ordenar os produtos pelo preço usando Selection Sort
void ordenarPorPreco(Produto produtos[], int n) {
    int i, j, minIndex;
    Produto temp;
    
    for (i = 0; i < n - 1; i++) {
        minIndex = i;
        for (j = i + 1; j < n; j++) {
            if (produtos[j].preco < produtos[minIndex].preco) {
                minIndex = j;
            }
        }
        // Troca os elementos
        temp = produtos[i];
        produtos[i] = produtos[minIndex];
        produtos[minIndex] = temp;
    }
}

// Função para exibir os produtos
void exibirProdutos(Produto produtos[], int n) {
    printf("Lista de Produtos Ordenados por Preço:\n");
    for (int i = 0; i < n; i++) {
        printf("%s - R$ %.2f\n", produtos[i].nome, produtos[i].preco);
    }
}

int main() {
    Produto produtos[] = {
        {"Notebook", 3500.00},
        {"Mouse", 80.00},
        {"Teclado", 120.00},
        {"Monitor", 900.00},
        {"Cadeira Gamer", 1500.00},
        {"Sanfona Gamer", 193.89}
    };
    
    int n = sizeof(produtos) / sizeof(produtos[0]);
    
    ordenarPorPreco(produtos, n);
    exibirProdutos(produtos, n);
    
    return 0;
}