#include <stdio.h>
#include <math.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    
    int i, qtdPositivo = 0, qtdNegativo = 0;
    int vetor[8];
    
    for (i = 0; i < 8; i++) {
        printf("Digite o valor do %iº número: ", i + 1);
        scanf("%i", &vetor[i]);
    }
    
    for (i = 0; i < 8; i++) {
        if (vetor[i] > 0) {
            qtdPositivo += 1;
        } else if (vetor[i] < 0) {
            qtdNegativo += 1;
        }
    }
    
    int vetorPositivo[qtdPositivo];
    int vetorNegativo[qtdNegativo];
    
    int posicaoPositiva = 0, posicaoNegativa = 0;
    
    for (i = 0; i < 8; i++) {
        if (vetor[i] > 0) {
            vetorPositivo[posicaoPositiva] = vetor[i];
            posicaoPositiva++;
        } else if (vetor[i] < 0) {
            vetorNegativo[posicaoNegativa] = vetor[i];
            posicaoNegativa++;
        }
    }
    
    printf("\nVetor positivo:\n");
    for (i = 0; i < qtdPositivo; i++) {
        printf("%i ", vetorPositivo[i]);
    }
    
    printf("\n--------------------------------------------------\n");
    
    printf("\nVetor negativo:\n");
    for (i = 0; i < qtdNegativo; i++) {
        printf("%i ", vetorNegativo[i]);
    }
    
    return 0;
}
