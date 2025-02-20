#include <stdio.h>
#include <math.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

	int matriz[10][20], matrizNova[10][20];
	int vetor[10];
	int i, j;
	
	for(i=0; i<10; i++){
		printf("* Linha %i *\n",i + 1);
		for(j=0; j<20; j++){
			printf("Posicao %ix%i : ",i+1, j+1);
			scanf("%i",&matriz[i][j]);
		}
	}
	
	for(i=0; i<10; i++){
		for(j=0; j<20; j++){
			vetor[i] += matriz[i][j];
		}
	}
	
	for(i=0; i<10; i++){
		for(j=0; j<20; j++){
			matrizNova[i][j] = matriz[i][j] * vetor[i];	
		}
	}
	
	printf("\n\n\n");
	printf("* Matriz resultante * \n");
	printf("---------------------");
	for(i=0; i<10; i++){
		printf("\n");
		for(j=0; j<20; j++){
			printf("[%i] ",matrizNova[i][j]);
		}
	}
}