#include<stdio.h>
#include<locale.h>

int soma(int *array, int tamanho) {
    int total = 0;
    for (int i = 0; i < tamanho; i++) {
        total += array[i];
    }
    return total;
}

int main() {
	setlocale(LC_ALL, "Portuguese");
	
    int n;

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &n);

    int array[n];

    printf("Digite os elementos do vetor:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }

    int resultado = soma(array, n);
    
    printf("A soma dos elementos do vetor é: %d\n", resultado);

    return 0;
}
