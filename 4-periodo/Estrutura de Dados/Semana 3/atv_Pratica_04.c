#include <stdio.h>
#include <math.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    
    char lojas[8][20];  
    char produtos[4][20];  
    float preco[8][4];  
    int i, j;
    
    for (i = 0; i < 8; i++) {
        printf("Nome da %iª loja: ", i + 1);
        scanf(" %[^\n]", lojas[i]);  
    }
    
    for (i = 0; i < 4; i++) {
        printf("Digite o %iº produto vendido: ", i + 1);
        scanf(" %[^\n]", produtos[i]); 
    }
    
    for (i = 0; i < 8; i++) {
        printf("\nDigite o valor dos produtos na loja %s:\n", lojas[i]);
        for (j = 0; j < 4; j++) {
            printf("%s: R$ ", produtos[j]);
            scanf("%f", &preco[i][j]);
        }
    }
    
    printf("\n\n* Tabela de valores *\n");
    printf("---------------------\n");
    printf("Lojas\t\t");
    for (j = 0; j < 4; j++) {
        printf("%s\t", produtos[j]);
    }
    printf("\n");
    
    for (i = 0; i < 8; i++) {
        printf("%s\t", lojas[i]);
        for (j = 0; j < 4; j++) {
            printf("R$ %.2f\t", preco[i][j]);
        }
        printf("\n");
    }
}
