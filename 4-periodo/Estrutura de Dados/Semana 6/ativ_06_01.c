#include<stdio.h>
#include<stdlib.h>

main(){
	int tam, i;
	float soma=0, media;
	
	printf("\n Digite a quantidade de notas: ");
	scanf("%d", &tam);
	
	float *notas = (int *)malloc(tam * sizeof(int));
	
	if(notas == NULL){
		printf("ERRO NA ALOCAÇÃO DE MEMORIA! \n");
		return 1;
	}
	
	printf("\n------ Digite as notas abaixo ------\n");
	for(i = 0; i < tam; i++){
		printf("Digite a %i nota: ", i + 1);
		scanf("%f", &notas[i]);
	}
	
	for(i = 0; i < tam; i++){
		soma += *(notas + i);
	}
	
	media = soma / tam;
	
	printf("\n A media das %i notas e %f.", tam, media);
	
	free(notas);
}