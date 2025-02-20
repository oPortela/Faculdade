#include<stdio.h>
#include<stdlib.h>

main(){
	int tam;
	
	printf("\n Digite o tamanho do vetor: ");
	scanf("%d", &tam);
	
	//Alocando a memoria para o vetor
	int *vetDinamico = (int *)malloc(tam * sizeof(int));
	
	//Verificando se a alocação falhou ou não
	if(vetDinamico == NULL){
		printf("ERRO NA ALOCAÇÂO DE MEMÓRIA!\n");
		return 1; //Sai com status de erro
	}
	
	//Preenchendo o vetor
	printf("*** DIgite os elementos do vetor. ***\n");
	for(int i = 0; i < tam; i++){
		scanf("%d", &vetDinamico[i]);
	}
	
	printf("*** Vetor digitado. ***");
	for(int i = 0; i < tam; i++){
		printf("[%d]", vetDinamico[i]);
	}
	
	printf("\n\n");
	
	//Liberando objeto da memoria
	free(vetDinamico);
}