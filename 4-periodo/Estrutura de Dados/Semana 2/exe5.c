#include<stdio.h>
#include<math.h>
#include<locale.h>

void numAleatorio(int qtde);

main(){
	setlocale(LC_ALL,"Portuguese");
	
	int num;
	
	printf("Digite a quantidade de valores aleatórios que gostaria de gerar: ");
	scanf("%i", &num);
//Chamando procedimento aleatorio
	printf("\n");
	numAleatorio(num);
}

//****************
void numAleatorio(qtde){
	int i;
	for(i=1; i<=qtde; i++){
		printf("%5i",1+rand()%6);
		if(i%5 == 0){
			printf("\n");
		}
	}
}