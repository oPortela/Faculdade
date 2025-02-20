#include<stdio.h>
#include<math.h>
#include<locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    
    int vetor1[10], vetor2[10], vetorFinal[20];
    int i;
    
    for(i = 0; i < 10; i++) {
        printf("Digite o %iº número do vetor1: ", i + 1);
        scanf("%i", &vetor1[i]);
    }
    
    printf("\n--------------------------------------------------\n");

    for(i = 0; i < 10; i++) {
        printf("Digite o %iº número do vetor2: ", i + 1);
        scanf("%i", &vetor2[i]);
    }
    
    // Intercalando os vetores
    for(i = 0; i < 10; i++) {
        vetorFinal[2 * i] = vetor1[i];       
        vetorFinal[2 * i + 1] = vetor2[i];  
    }
    
    printf("\nVetor final:\n");
    for(i = 0; i < 20; i++) {
        printf("%i ", vetorFinal[i]);
    }
}
