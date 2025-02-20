#include <stdio.h>
#include <math.h>
#include <locale.h>

//Função de média aritmética
float mediaAritmetica(float nota[]){
	int i, resultado;
	float soma;
	
	/*for(i=0; i<sizeof(nota); i++){
		soma += nota[i]; 
	}*/
	
	for(i=0; i<3; i++){
		soma += nota[i]; 
	}
	
	resultado = soma / 3;
	
	return resultado;
}

//Função de média ponderada
float mediaPonderada(float nota[]){
	int i, resultado, somaPesos;
	float soma;
	const int pesos[] = {5, 3, 2};
	
	/*for(i=0; i<sizeof(nota); i++){
		soma += nota[i] * pesos[i]; 
	}
	
	for(i=0; i<sizeof(pesos); i++){
		somaPesos += pesos[i];
	}*/
	
	for(i=0; i<3; i++){
		soma += nota[i] * pesos[i]; 
	}
	
	for(i=0; i<3; i++){
		somaPesos += pesos[i];
	}
	
	resultado = soma / somaPesos;
	
	return resultado;
}

int main() {
    setlocale(LC_ALL, "Portuguese");
	
	float notas[3], media;
	int i;
	char tipoMedia;
	
	for(i=0; i<3; i++){
		printf("Digite a nota %i do aluno: ", i+1);
		scanf("%f", &notas[i]);
	}
	
	printf("Qual o tipo de média deseja calcular (P-Ponderada / A-aritmética): ");
	scanf(" %c", &tipoMedia);
	tipoMedia = toupper(tipoMedia);
	
	while((tipoMedia != 'A') && (tipoMedia != 'P')){
		printf("Não existe essa média. Selecione a opção novamente (P-Ponderada / A-aritmética): ");
		scanf("%c", &tipoMedia);
		tipoMedia = toupper(tipoMedia);
	}
	
	if(tipoMedia = "A"){
		media = mediaAritmetica(notas);
	}else if(tipoMedia = "P"){
		media = mediaPonderada(notas);
	}
	
	printf("A média do aluno é de %.2f.", media);
	
}