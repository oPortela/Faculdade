#include<stdio.h>
#include<locale.h>


void trocarValores(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
	setlocale(LC_ALL, "Portuguese");
	
    int x, y;

    printf("Digite o valor de x: ");
    scanf("%d", &x);
    printf("Digite o valor de y: ");
    scanf("%d", &y);

    printf("\nAntes da troca: x = %d, y = %d\n", x, y);

    trocarValores(&x, &y);

    printf("Depois da troca: x = %d, y = %d\n", x, y);

    return 0;
}
