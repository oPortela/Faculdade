#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

// Estrutura para armazenar os dados dos produtos
typedef struct Produto {
    int codigo;
    char nome[100];
    float preco;
    int estoque;
    char embalagem[50];
    int fornecedor;
    int codauxiliar;
    struct Produto *anterior;
    struct Produto *proximo;
} Produto;

// Ponteiro para o início e fim da lista de produtos
Produto *cabeca = NULL;
Produto *cauda = NULL;

// Função para encontrar um produto pelo código
Produto* encontrar_produto(int codigo) {
    Produto* atual = cabeca;
    while (atual != NULL) {
        if (atual->codigo == codigo) {
            return atual;
        }
        atual = atual->proximo;
    }
    return NULL;
}

// Função para cadastrar produtos
void cadastrar_produto(int codigo, char *nome, float preco, int estoque, char *embalagem, int fornecedor, int codauxiliar) {
    if (encontrar_produto(codigo) == NULL) {
        Produto *novo = (Produto *)malloc(sizeof(Produto));
        novo->codigo = codigo;
        strcpy(novo->nome, nome);
        novo->preco = preco;
        novo->estoque = estoque;
        strcpy(novo->embalagem, embalagem);
        novo->fornecedor = fornecedor;
        novo->codauxiliar = codauxiliar;
        novo->anterior = NULL;
        novo->proximo = NULL;

        if (cabeca == NULL) {
            cabeca = novo;
            cauda = novo;
        } else {
            cauda->proximo = novo;
            novo->anterior = cauda;
            cauda = novo;
        }
        printf("Produto cadastrado com sucesso!\n");
    } else {
        printf("Produto com código já existente!\n");
    }
}

// Função para excluir produtos
void excluir_produto(int codigo) {
    Produto* produto = encontrar_produto(codigo);
    if (produto != NULL) {
        if (produto->anterior != NULL) {
            produto->anterior->proximo = produto->proximo;
        } else {
            cabeca = produto->proximo;
        }
        if (produto->proximo != NULL) {
            produto->proximo->anterior = produto->anterior;
        } else {
            cauda = produto->anterior;
        }
        free(produto);
        printf("Produto excluído com sucesso!\n");
    } else {
        printf("Produto não encontrado!\n");
    }
}

// Função para editar produtos
void editar_produto(int codigo, char *nome, float preco, int estoque, char *embalagem, int fornecedor, int codauxiliar) {
    Produto* produto = encontrar_produto(codigo);
    if (produto != NULL) {
        if (nome != NULL) strcpy(produto->nome, nome);
        produto->preco = preco;
        produto->estoque = estoque;
        if (embalagem != NULL) strcpy(produto->embalagem, embalagem);
        produto->fornecedor = fornecedor;
        produto->codauxiliar = codauxiliar;
        printf("Produto editado com sucesso!\n");
    } else {
        printf("Produto não encontrado!\n");
    }
}

// Função para pesquisar produtos
void pesquisar_produto(int codigo) {
    Produto* produto = encontrar_produto(codigo);
    if (produto != NULL) {
        printf("Código: %d\n", produto->codigo);
        printf("Nome: %s\n", produto->nome);
        printf("Preço: R$%.2f\n", produto->preco);
        printf("Estoque: %d\n", produto->estoque);
        printf("Embalagem: %s\n", produto->embalagem);
        printf("Fornecedor: %d\n", produto->fornecedor);
        printf("Cod Barras: %d\n", produto->codauxiliar);
    } else {
        printf("Produto não encontrado!\n");
    }
}

// Função Principal
int main() {
    setlocale(LC_ALL, "portuguese");
    int op;
    while (1) {
        printf("\n1 - Inserir Produtos\n");
        printf("2 - Pesquisar Produtos\n");
        printf("3 - Editar Produtos\n");
        printf("4 - Excluir Produtos\n");
        printf("Escolha uma das opções acima: ");
        scanf("%d", &op);

        switch (op) {
            case 1: {
                int codigo, estoque, fornecedor, codauxiliar;
                char nome[100], embalagem[50];
                float preco;

                printf("Código: ");
                scanf("%d", &codigo);
                printf("Descrição: ");
                scanf(" %[^\n]", nome);
                printf("QT. Estoque: ");
                scanf("%d", &estoque);
                printf("Embalagem: ");
                scanf(" %[^\n]", embalagem);
                printf("Cod. Fornecedor: ");
                scanf("%d", &fornecedor);
                printf("Cod. Barras: ");
                scanf("%d", &codauxiliar);
                printf("Preço: ");
                scanf("%f", &preco);

                cadastrar_produto(codigo, nome, preco, estoque, embalagem, fornecedor, codauxiliar);
                break;
            }
            case 2: {
                int codigo;
                printf("Qual produto deseja pesquisar: ");
                scanf("%d", &codigo);
                pesquisar_produto(codigo);
                break;
            }
            case 3: {
                int codigo, estoque, fornecedor, codauxiliar;
                char nome[100], embalagem[50];
                float preco;

                printf("Qual produto deseja alterar: ");
                scanf("%d", &codigo);
                printf("Descrição: ");
                scanf(" %[^\n]", nome);
                printf("Preço: ");
                scanf("%f", &preco);
                printf("Estoque: ");
                scanf("%d", &estoque);
                printf("Embalagem: ");
                scanf(" %[^\n]", embalagem);
                printf("Fornecedor: ");
                scanf("%d", &fornecedor);
                printf("Cod. Barras: ");
                scanf("%d", &codauxiliar);

                editar_produto(codigo, nome, preco, estoque, embalagem, fornecedor, codauxiliar);
                break;
            }
            case 4: {
                int codigo;
                char confirm;

                printf("Qual produto deseja excluir: ");
                scanf("%d", &codigo);
                printf("Deseja mesmo excluir o produto %d? (S para sim, N para não): ", codigo);
                scanf(" %c", &confirm);

                if (confirm == 'S' || confirm == 's') {
                    excluir_produto(codigo);
                } else {
                    printf("Operação abortada\n");
                }
                break;
            }
            default:
                printf("ERRO! Opção inválida.\n");
        }

        char continuar;
        printf("Deseja continuar? (s/n): ");
        scanf(" %c", &continuar);
        if (continuar != 's' && continuar != 'S') {
            break;
        }
    }

    // Liberar memória alocada
    Produto* atual = cabeca;
    while (atual != NULL) {
        Produto* temp = atual;
        atual = atual->proximo;
        free(temp);
    }

    return 0;
}

