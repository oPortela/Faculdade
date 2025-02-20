#include<stdio.h>
#include<math.h>
#include<locale.h>

#define tam 5
#define lin 3
#define col 3

main(){
	setlocale(LC_ALL,"Portuguese");
	
	int vnum[tam]; //declarando um vetor
	int mnotas[lin][col]; //declaranndo uma matriz
	int i, j;
	
//preenchendo um vetor
	for(i=0; i<tam; i++){
		printf("Indice [%i]: ",i);
		scanf("%i",&vnum[i]);
	}
	
//preenchendo uma matriz
	for(i=0; i<lin; i++){
		printf("* Linha %i *\n",i);
		for(j=0; j<col; j++){
			printf("Coluna [%i]",j);
			scanf("%i",&mnotas[i][j]);
		}
	}
	
	system("cls");
	printf("   Indice   Valor   \n");
	printf("--------------------- \n");
	for(i=0; i<tam; i++){
		printf("   %i   [%i]\n",i,vnum[i]);
	}

//Imprimindo a matriz
	printf("\n\n\n");
	printf("* Mostrando a Matriz * \n");
	printf("---------------------");
	for(i=0; i<lin; i++){
		printf("\n");
		for(j=0; j<col; j++){
			printf("[%i] ",mnotas[i][j]);
		}
	}
}