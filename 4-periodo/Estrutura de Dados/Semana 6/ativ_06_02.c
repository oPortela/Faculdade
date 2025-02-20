#include<stdio.h>
#include<stdlib.h>
#include<locale.h>


main(){
	setlocale(LC_ALL, "Portuguese");
	
	int tam, i, pares = 0, impares = 0;
	
	int *vetor = (int *)malloc(tam * sizeof(int));
	
	printf("\nDigite a quantidade de numeros que deseja: \n");
	scanf("%d", &tam);
	
	for(i=0; i<tam; i++){
		printf("Digite o %i valor: ", i + 1);
		scanf("%i", &vetor[i]);
	}
	
	for(i=0; i<tam; i++){
		if(vetor[i] % 2 == 0){
			pares += 1;
		}else{
			impares += 1;
		}
	}
	
	for(i=0; i<tam; i++){
		printf("[%i] ", vetor[i]); 
	}
	
	printf("\nDos numeros acima %i são pares e %i são impares.", pares, impares);
	
	free(vetor);
}